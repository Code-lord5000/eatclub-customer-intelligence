import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE = Path.home() / "PM/customer-repo/crilly-v2"

# Load API key from .env file
from pathlib import Path as EnvPath
env_file = EnvPath(__file__).parent.parent / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()


API_KEY = os.environ["ANTHROPIC_API_KEY"]
ENV_ID = (BASE / "ENVIRONMENT_ID.txt").read_text().strip()

def _resolve_agent_id(name):
    """Read v2 agent ID if available, fall back to current production ID.

    During the rebuild, new collectors talk to new agents (V*_READY files).
    Production _ID.txt files are NOT touched until final coordinated swap.
    """
    v2_path = BASE / f"AGENT_{name.upper()}_ID_V2_READY.txt"
    v4_path = BASE / f"AGENT_{name.upper()}_ID_V4_READY.txt"  # HubSpot is v4
    legacy_path = BASE / f"AGENT_{name.upper()}_ID.txt"
    if v4_path.exists():
        return v4_path.read_text().strip()
    if v2_path.exists():
        return v2_path.read_text().strip()
    return legacy_path.read_text().strip()


AGENT_IDS = {
    "slack":        _resolve_agent_id("slack"),
    "granola":      _resolve_agent_id("granola"),
    "hubspot":      _resolve_agent_id("hubspot"),
    "orchestrator": (BASE / "AGENT_ORCH_ID.txt").read_text().strip(),
    # NOTE: v2 rebuild changes:
    #   - sms removed: B1-B6 baselines migrated to T011-T013 in memory.json
    #   - mixpanel removed: not consumed by orchestrator in v2 architecture
    #   - churn, dealscore, mixpanel handled by Python readers (no agents)
    #   - slack/granola/hubspot resolve to v2/v4 agent IDs from _V*_READY.txt files
}

HEADERS = [
    "-H", f"x-api-key: {API_KEY}",
    "-H", "anthropic-version: 2023-06-01",
    "-H", "anthropic-beta: managed-agents-2026-04-01",
    "-H", "content-type: application/json",
]

# Track failures for end-of-run summary
SESSION_FAILURES = []


class CurlError(Exception):
    def __init__(self, status_code, message, is_retryable):
        self.status_code = status_code
        self.message = message
        self.is_retryable = is_retryable
        super().__init__(f"HTTP {status_code}: {message}")


def curl(method, url, data=None, max_time=300):
    """Single curl call. Returns parsed JSON or raises CurlError with classification."""
    cmd = ["curl", "-sS", "--fail-with-body", "--max-time", str(max_time),
           "-w", "\n__HTTP_STATUS__:%{http_code}"]
    if method == "POST":
        cmd += ["-X", "POST"]
    cmd += HEADERS
    cmd += [url]
    if data:
        cmd += ["-d", json.dumps(data)]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Parse HTTP status code from curl output
    stdout = result.stdout
    status_code = None
    if "__HTTP_STATUS__:" in stdout:
        parts = stdout.rsplit("__HTTP_STATUS__:", 1)
        stdout = parts[0]
        try:
            status_code = int(parts[1].strip())
        except ValueError:
            status_code = None

    if result.returncode != 0 or (status_code and status_code >= 400):
        error_body = stdout or result.stderr
        is_retryable = status_code is not None and 500 <= status_code < 600
        # 499 (client disconnected) is NOT retryable — same prompt will fail again
        if status_code == 499:
            is_retryable = False
        raise CurlError(status_code or 0, error_body[:500], is_retryable)

    return json.loads(stdout)


def curl_with_retry(method, url, data=None, max_time=300, max_attempts=3):
    """Retry wrapper. Retries 5xx with exponential backoff. Never retries 499 or 4xx."""
    last_error = None
    for attempt in range(max_attempts):
        try:
            return curl(method, url, data, max_time=max_time)
        except CurlError as e:
            last_error = e
            if not e.is_retryable:
                raise
            if attempt < max_attempts - 1:
                backoff = 2 ** (attempt + 1)  # 2s, 4s, 8s
                print(f"    Retry {attempt+1}/{max_attempts-1} after {backoff}s (HTTP {e.status_code})")
                time.sleep(backoff)
    raise last_error


def run_session(name, agent_id, message):
    print(f"  Starting {name}...")
    try:
        # Create session
        session = curl_with_retry("POST", "https://api.anthropic.com/v1/sessions", {
            "agent": agent_id,
            "environment_id": ENV_ID,
            "title": f"crilly-{name}-{datetime.now().strftime('%Y%m%d')}"
        })
        session_id = session["id"]

        # Send message
        curl_with_retry("POST", f"https://api.anthropic.com/v1/sessions/{session_id}/events", {
            "events": [{"type": "user.message", "content": [{"type": "text", "text": message}]}]
        })

        # Poll until idle — extended to 30 min (360 polls × 5s)
        output = []
        time.sleep(5)
        seen_running = False
        timed_out = True
        current = None
        for _ in range(360):
            status = curl_with_retry("GET", f"https://api.anthropic.com/v1/sessions/{session_id}")
            current = status.get("status")
            if current == "running":
                seen_running = True
            if current == "idle" and seen_running:
                timed_out = False
                break
            time.sleep(5)

        if timed_out:
            msg = f"Session did not reach idle within 30 minutes (last status: {current})"
            print(f"  {name} TIMED OUT: {msg}")
            SESSION_FAILURES.append({"agent": name, "reason": "timeout", "detail": msg})
            return "[]"

        # Get events
        events = curl_with_retry("GET", f"https://api.anthropic.com/v1/sessions/{session_id}/events")
        for event in events.get("data", []):
            if event.get("type") == "agent.message":
                for block in event.get("content", []):
                    if block.get("type") == "text":
                        output.append(block["text"])

        result = "".join(output)
        if not result.strip():
            msg = "Session completed but returned empty output"
            print(f"  {name} EMPTY: {msg}")
            SESSION_FAILURES.append({"agent": name, "reason": "empty_output", "detail": msg})
            return "[]"

        print(f"  {name} done ({len(result)} chars)")
        return result

    except CurlError as e:
        reason = "http_499_client_disconnect" if e.status_code == 499 else f"http_{e.status_code}"
        print(f"  {name} FAILED: HTTP {e.status_code} — {e.message[:200]}")
        SESSION_FAILURES.append({"agent": name, "reason": reason, "detail": e.message[:500]})
        return "[]"
    except Exception as e:
        print(f"  {name} FAILED (unexpected): {type(e).__name__}: {e}")
        SESSION_FAILURES.append({"agent": name, "reason": "unexpected", "detail": str(e)[:500]})
        return "[]"


def _load_state_file():
    """Read last_run_at from state.json, default to 7 days ago."""
    state_path = BASE / "state.json"
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text())
            return state.get("last_run_at")
        except (json.JSONDecodeError, KeyError):
            pass
    # Default: 7 days ago
    from datetime import timedelta
    return (datetime.utcnow() - timedelta(days=7)).isoformat() + "Z"


def _save_state_file():
    """Write current run timestamp to state.json for next run's last_run_at."""
    state_path = BASE / "state.json"
    state = {"last_run_at": datetime.utcnow().isoformat() + "Z"}
    state_path.write_text(json.dumps(state, indent=2))


def _load_run_context():
    """Load themes, watch list, and staff directory from memory.json."""
    memory_path = BASE / "memory.json"
    if not memory_path.exists():
        print("   ⚠️  memory.json not found — using empty context")
        return [], [], {"ams": [], "bdms": []}
    memory = json.loads(memory_path.read_text())
    themes = [
        {
            "theme_id": t.get("theme_id"),
            "theme": t.get("theme"),
            "okr": t.get("okr"),
            "description": t.get("notes", ""),
            "lifecycle": t.get("lifecycle", "CHRONIC"),
        }
        for t in memory.get("chronic_themes", [])
    ]
    watch_list = memory.get("venue_watch_list", [])
    raw_dir = memory.get("staff_directory", {})
    staff_directory = {
        "ams": raw_dir.get("ams", []),
        "bdms": raw_dir.get("bdms", []),
    }
    return themes, watch_list, staff_directory


def _build_collector_user_message(last_run_at, themes, watch_list, extra=None):
    """Standard user message format passed to all v2 agents."""
    payload = {
        "last_run_at": last_run_at,
        "themes": themes,
        "venue_watch_list": watch_list,
    }
    if extra:
        payload.update(extra)
    return json.dumps(payload, indent=2)


def _get_jira_in_flight():
    """Pull in-flight Jira tickets and use Haiku to extract suppressible signal patterns.

    Returns:
        list of dicts: [{"ticket_key": "REST-123", "title": "...", "suppression_tag": "..."}]
        Empty list if Jira call or Haiku call fails (graceful — don't block the run).
    """
    jira_email = os.environ.get("JIRA_EMAIL")
    jira_token = os.environ.get("JIRA_API_TOKEN")
    if not (jira_email and jira_token):
        print("   ⚠️  Jira credentials not set — skipping suppression filter")
        return []

    # JQL: tickets in product lane "Restaurant 1" (10168), status In Progress or In Validation
    jql = (
        'project = "IDEA" AND status in ("In Progress", "In Validation") '
        'AND "Product Lane[Dropdown]" = "Restaurant 1"'
    )

    import base64
    auth_b64 = base64.b64encode(f"{jira_email}:{jira_token}".encode()).decode()

    cmd = [
        "curl", "-sS", "--fail-with-body", "--max-time", "30",
        "-H", f"Authorization: Basic {auth_b64}",
        "-H", "Accept: application/json",
        f"https://eatclubapp.atlassian.net/rest/api/3/search?jql={jql}&fields=summary,status&maxResults=50",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"   ⚠️  Jira fetch failed: {result.stderr[:200]}")
        return []

    try:
        data = json.loads(result.stdout)
        tickets = [
            {
                "ticket_key": t["key"],
                "title": t["fields"]["summary"],
                "status": t["fields"]["status"]["name"],
            }
            for t in data.get("issues", [])
        ]
    except (json.JSONDecodeError, KeyError) as e:
        print(f"   ⚠️  Jira response parse failed: {e}")
        return []

    if not tickets:
        print("   ↳ No in-flight Restaurant 1 tickets")
        return []

    print(f"   ↳ {len(tickets)} in-flight Restaurant 1 tickets")

    # Haiku call: turn ticket titles into suppression tags
    haiku_prompt = (
        "You receive a list of in-flight Jira tickets. For each ticket, write a one-sentence "
        "tag describing what kind of CUSTOMER SIGNAL it would suppress. Tags should be specific "
        "enough to match real signals (e.g. 'venue reports deal score zero on iOS') but short.\n\n"
        f"Tickets:\n{json.dumps(tickets, indent=2)}\n\n"
        "Return ONLY a JSON array, one object per input ticket, like:\n"
        '[{"ticket_key": "REST-123", "title": "<original>", "suppression_tag": "<your tag>"}]\n\n'
        "Do not include any text before or after the JSON."
    )

    haiku_payload = {
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 1500,
        "messages": [{"role": "user", "content": haiku_prompt}],
    }

    haiku_cmd = [
        "curl", "-sS", "--fail-with-body", "--max-time", "60",
        "-X", "POST",
        *HEADERS,
        "-d", json.dumps(haiku_payload),
        "https://api.anthropic.com/v1/messages",
    ]
    haiku_result = subprocess.run(haiku_cmd, capture_output=True, text=True)
    if haiku_result.returncode != 0:
        print(f"   ⚠️  Haiku call failed — returning raw tickets without tags")
        return [{"ticket_key": t["ticket_key"], "title": t["title"], "suppression_tag": t["title"]}
                for t in tickets]

    try:
        response = json.loads(haiku_result.stdout)
        text = response["content"][0]["text"].strip()
        # Strip code fences if present
        if text.startswith("```"):
            text = text.split("```")[1].lstrip("json").strip()
        suppression_list = json.loads(text)
        return suppression_list
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"   ⚠️  Could not parse Haiku output: {e} — returning raw titles")
        return [{"ticket_key": t["ticket_key"], "title": t["title"], "suppression_tag": t["title"]}
                for t in tickets]


def run_collectors():
    """v2 collector orchestration."""
    print("📋 Loading run context...")
    last_run_at = _load_state_file()
    themes, watch_list, staff_directory = _load_run_context()
    print(f"   last_run_at: {last_run_at}")
    print(f"   themes: {len(themes)} loaded ({', '.join(t['theme_id'] for t in themes)})")
    print(f"   watch_list: {len(watch_list)} venues")
    print(f"   staff_directory: {len(staff_directory['ams'])} AMs, {len(staff_directory['bdms'])} BDMs")

    # Granola pre-check — determine if there are customer-facing meetings
    print("\n📞 Running Granola pre-check...")
    sys.path.insert(0, str(BASE / "scripts"))
    try:
        from granola_precheck import get_customer_meetings_and_context
        granola_context = get_customer_meetings_and_context(last_run_at)
        meetings_count = len(granola_context.get("meetings", []))
        print(f"   {granola_context['stats']['meetings_in_window']} meetings in window, "
              f"{meetings_count} customer-facing")
    except Exception as e:
        print(f"   ⚠️  Granola pre-check failed: {e}")
        granola_context = {"meetings": []}
        meetings_count = 0

    # Build agent prompts (v2 format: structured JSON in user message)
    # Note: staff_directory is NOT passed to collectors — they emit names, not teams.
    # Team resolution happens in the orchestrator using staff_directory.
    agent_prompts = {
        "slack":   _build_collector_user_message(last_run_at, themes, watch_list),
        "hubspot": _build_collector_user_message(last_run_at, themes, watch_list),
    }
    if meetings_count > 0:
        agent_prompts["granola"] = _build_collector_user_message(
            last_run_at, themes, watch_list,
            extra={"meetings": granola_context["meetings"]}
        )
    else:
        print("   ↳ Granola agent SKIPPED — no customer-facing meetings this window")

    # Run agent collectors in parallel
    print(f"\n🤖 Running {len(agent_prompts)} agent collectors in parallel...")
    with ThreadPoolExecutor(max_workers=len(agent_prompts)) as executor:
        futures = {
            name: executor.submit(run_session, name, AGENT_IDS[name], prompt)
            for name, prompt in agent_prompts.items()
        }
        agent_results = {name: f.result() for name, f in futures.items()}

    # If Granola was skipped, inject placeholder brief
    if "granola" not in agent_results:
        agent_results["granola"] = json.dumps({
            "source": "granola",
            "window": {"from": last_run_at, "to": datetime.utcnow().isoformat() + "Z"},
            "signals": [],
            "unmapped_signals": [],
            "theme_drift_observations": [],
            "counts": {"total_signals": 0, "high_confidence": 0, "watch_list_hits": 0,
                       "theme_evidence_count": 0, "new_signal_count": 0,
                       "unmapped_signal_count": 0, "theme_drift_count": 0},
            "coverage_notes": "No customer-facing meetings in window — agent skipped."
        })

    # Run Python readers (no agent, no token cost)
    print("\n📊 Running Python readers (dealscore, churn, mixpanel)...")
    try:
        from dealscore_reader import collect_dealscore_signals
        agent_results["dealscore"] = json.dumps(
            collect_dealscore_signals(last_run_at, themes, watch_list)
        )
        print(f"   ✓ dealscore")
    except Exception as e:
        print(f"   ⚠️  dealscore failed: {e}")
        agent_results["dealscore"] = json.dumps({"source": "dealscore", "signals": [],
                                                  "coverage_notes": f"Reader error: {e}"})

    try:
        from churn_reader import collect_churn_signals
        agent_results["churn"] = json.dumps(
            collect_churn_signals(last_run_at, themes, watch_list)
        )
        print(f"   ✓ churn")
    except Exception as e:
        print(f"   ⚠️  churn failed: {e}")
        agent_results["churn"] = json.dumps({"source": "churn", "signals": [],
                                             "coverage_notes": f"Reader error: {e}"})

    try:
        from mixpanel_reader import collect_mixpanel_signals
        agent_results["mixpanel"] = json.dumps(
            collect_mixpanel_signals(last_run_at, themes, watch_list)
        )
        print(f"   ✓ mixpanel")
    except Exception as e:
        print(f"   ⚠️  mixpanel failed: {e}")
        agent_results["mixpanel"] = json.dumps({"source": "mixpanel", "signals": [],
                                                 "coverage_notes": f"Reader error: {e}"})

    return agent_results


def run_orchestrator(signals, themes, watch_list, staff_directory):
    print("Running orchestrator...")

    # Pull jira suppression out of signals dict — it goes in its own top-level key
    jira_suppression_raw = signals.pop("_jira_suppression", "[]")
    try:
        jira_suppression = json.loads(jira_suppression_raw)
    except (json.JSONDecodeError, TypeError):
        jira_suppression = []

    # Parse each collector brief from JSON string → dict
    collector_briefs = {}
    for name, data in signals.items():
        try:
            collector_briefs[name] = json.loads(data)
        except (json.JSONDecodeError, TypeError):
            collector_briefs[name] = {
                "source": name,
                "signals": [],
                "coverage_notes": f"Could not parse collector output: {str(data)[:200]}"
            }

    message = json.dumps({
        "themes": themes,
        "venue_watch_list": watch_list,
        "staff_directory": staff_directory,
        "jira_suppression": jira_suppression,
        "collector_briefs": collector_briefs,
    }, indent=2)

    return run_session("orchestrator", AGENT_IDS["orchestrator"], message)


def save_synthesis(output):
    week = datetime.now().isocalendar()[0].__str__() + "-W" + str(datetime.now().isocalendar()[1]).zfill(2)
    try:
        routing_start = output.index("```routing")
        synthesis = output[:routing_start].strip()
    except ValueError:
        synthesis = output

    path = Path.home() / f"PM/customer-repo/synthesis/{week}-synthesis.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text(synthesis)
    print(f"Synthesis saved: {path}")
    os.system(f'cd ~/PM/customer-repo && git add synthesis/ && git commit -m "chore: weekly synthesis {week}" && git push origin main')


def handle_routing(output):
    try:
        start = output.index("```routing") + len("```routing")
        end = output.index("```", start)
        routing = json.loads(output[start:end].strip())
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Could not parse routing block: {e}")
        return

    week = datetime.now().isocalendar()[0].__str__() + "-W" + str(datetime.now().isocalendar()[1]).zfill(2)

    for ticket in routing.get("jira_tickets", []):
        print(f"TODO Jira: [{ticket.get('okr','')}] {ticket['theme']}")

    iqs = routing.get("interview_questions", [])
    if iqs:
        iq_path = Path.home() / f"PM/customer-repo/synthesis/interview-questions-{week}.md"
        with open(iq_path, "w") as f:
            for iq in iqs:
                f.write(f"## {iq['theme']}\n")
                for q in iq["questions"]:
                    f.write(f"- {q}\n")
                f.write("\n")
        print(f"Interview questions saved: {iq_path}")

    for alert in routing.get("friction_alerts", []):
        print(f"TODO Slack DM Luke: {alert.get('venue')} ({alert.get('rest_id','no restID')})")

    watch = routing.get("watch_list", [])
    if watch:
        print(f"Watch list ({len(watch)} items):")
        for item in watch:
            print(f"  - {item}")


if __name__ == "__main__":
    print(f"\n🧠 Crilly v2 starting — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    # Load context once at top level — passed to orchestrator after collectors run
    themes, watch_list, staff_directory = _load_run_context()

    signals = run_collectors()
    print("\nAll collectors complete.\n")

    print("🚦 Pulling in-flight Jira tickets for suppression...")
    suppression_list = _get_jira_in_flight()
    signals["_jira_suppression"] = json.dumps(suppression_list)

    output = run_orchestrator(signals, themes, watch_list, staff_directory)
    print("\nOrchestrator complete.\n")

    # Save full output including routing block
    save_full_output(output)

    # Save synthesis doc
    save_synthesis(output)

    # Parse routing and update memory.json
    print("\n📝 Updating memory.json...")
    routing = handle_routing(output)
    _update_memory(routing, output)

    # Commit everything in one shot
    week = datetime.now().isocalendar()[0].__str__() + "-W" + str(datetime.now().isocalendar()[1]).zfill(2)
    os.system(
        f'cd ~/PM/customer-repo && '
        f'git add synthesis/ crilly-v2/memory.json crilly-v2/logs/ && '
        f'git commit -m "chore: weekly synthesis {week} + memory update" && '
        f'git push origin main'
    )

    _save_state_file()

    # Loud failure summary
    if SESSION_FAILURES:
        print("\n⚠️  SESSION FAILURES THIS RUN:")
        for f in SESSION_FAILURES:
            print(f"  - {f['agent']}: {f['reason']}")
            print(f"    {f['detail'][:200]}")
        print()
    else:
        print("\n✅ All sessions completed successfully.\n")

    print("\n✅ Crilly run complete.\n")
def save_full_output(output):
    """Save complete orchestrator output including routing block to logs/."""
    week = datetime.now().isocalendar()[0].__str__() + "-W" + str(datetime.now().isocalendar()[1]).zfill(2)
    logs_path = BASE / "logs"
    logs_path.mkdir(exist_ok=True)
    path = logs_path / f"{week}-full-output.txt"
    path.write_text(output)
    print(f"Full output saved: {path}")


def _update_memory(routing, output):
    """Update memory.json after every run."""
    if not routing:
        print("   ⚠️  No routing block — memory.json not updated")
        return

    memory_path = BASE / "memory.json"
    if not memory_path.exists():
        print("   ⚠️  memory.json not found — skipping update")
        return

    memory = json.loads(memory_path.read_text())
    week = datetime.now().isocalendar()[0].__str__() + "-W" + str(datetime.now().isocalendar()[1]).zfill(2)

    memory["last_updated"] = datetime.utcnow().strftime("%Y-%m-%d")
    memory["last_run_week"] = week

    import re
    fired_theme_ids = set(re.findall(r'T0\d\d', output))
    print(f"   Themes fired this run: {', '.join(sorted(fired_theme_ids)) or 'none detected'}")

    for theme in memory.get("chronic_themes", []):
        if theme["theme_id"] in fired_theme_ids:
            theme["recurrence_count"] = theme.get("recurrence_count", 0) + 1
            theme["last_seen"] = week
            print(f"   ↳ {theme['theme_id']} recurrence_count → {theme['recurrence_count']}, last_seen → {week}")

    friction_alerts = routing.get("friction_alerts", [])
    existing_rest_ids = {v.get("rest_id"): v for v in memory.get("venue_watch_list", [])}
    existing_names = {v.get("venue"): v for v in memory.get("venue_watch_list", [])}

    for alert in friction_alerts:
        venue_name = alert.get("venue", "")
        rest_id = alert.get("rest_id", "UNKNOWN")
        signals = alert.get("signals", [])
        notes = " | ".join(signals)[:300]
        existing = existing_rest_ids.get(rest_id) or existing_names.get(venue_name)
        if existing:
            existing["last_seen"] = week
            existing["notes"] = notes
            print(f"   ↳ Watch list updated: {venue_name}")
        else:
            memory["venue_watch_list"].append({
                "venue": venue_name,
                "rest_id": rest_id,
                "status": "WATCH",
                "notes": notes,
                "first_flagged": week,
                "last_seen": week,
            })
            print(f"   ↳ Watch list NEW: {venue_name}")

    memory_path.write_text(json.dumps(memory, indent=2))
    print(f"   ✅ memory.json updated for {week}")


def replay_from_last_output():
    """Re-run post-processing from last saved full output. No collectors, no cost."""
    week = datetime.now().isocalendar()[0].__str__() + "-W" + str(datetime.now().isocalendar()[1]).zfill(2)
    log_path = BASE / "logs" / f"{week}-full-output.txt"

    if not log_path.exists():
        print(f"No full output found at {log_path}")
        return

    print(f"📂 Replaying from: {log_path}")
    output = log_path.read_text()

    save_synthesis(output)

    print("\n📝 Updating memory.json...")
    routing = handle_routing(output)
    _update_memory(routing, output)

    os.system(
        f'cd ~/PM/customer-repo && '
        f'git add synthesis/ crilly-v2/memory.json && '
        f'git commit -m "chore: replay memory update {week}" && '
        f'git push origin main'
    )
    print("\n✅ Replay complete.\n")
