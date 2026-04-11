import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE = Path.home() / "PM/customer-repo/crilly-v2"
API_KEY = os.environ["ANTHROPIC_API_KEY"]
ENV_ID = (BASE / "ENVIRONMENT_ID.txt").read_text().strip()

AGENT_IDS = {
    "slack":        (BASE / "AGENT_SLACK_ID.txt").read_text().strip(),
    "granola":      (BASE / "AGENT_GRANOLA_ID.txt").read_text().strip(),
    "hubspot":      (BASE / "AGENT_HUBSPOT_ID.txt").read_text().strip(),
    "sms":          (BASE / "AGENT_SMS_ID.txt").read_text().strip(),
    "churn":        (BASE / "AGENT_CHURN_ID.txt").read_text().strip(),
    "dealscore":    (BASE / "AGENT_DEALSCORE_ID.txt").read_text().strip(),
    "mixpanel":     (BASE / "AGENT_MIXPANEL_ID.txt").read_text().strip(),
    "orchestrator": (BASE / "AGENT_ORCH_ID.txt").read_text().strip(),
}

HEADERS = [
    "-H", f"x-api-key: {API_KEY}",
    "-H", "anthropic-version: 2023-06-01",
    "-H", "anthropic-beta: managed-agents-2026-04-01",
    "-H", "content-type: application/json",
]

def curl(method, url, data=None):
    cmd = ["curl", "-sS", "--fail-with-body"]
    if method == "POST":
        cmd += ["-X", "POST"]
    cmd += HEADERS
    cmd += [url]
    if data:
        cmd += ["-d", json.dumps(data)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"curl failed: {result.stderr}\n{result.stdout}")
    return json.loads(result.stdout)

def run_session(name, agent_id, message):
    print(f"  Starting {name}...")
    try:
        # Create session
        session = curl("POST", "https://api.anthropic.com/v1/sessions", {
            "agent": agent_id,
            "environment_id": ENV_ID,
            "title": f"crilly-{name}-{datetime.now().strftime('%Y%m%d')}"
        })
        session_id = session["id"]

        # Send message
        curl("POST", f"https://api.anthropic.com/v1/sessions/{session_id}/events", {
            "events": [{"type": "user.message", "content": [{"type": "text", "text": message}]}]
        })

        # Poll until idle
        output = []
        while True:
            status = curl("GET", f"https://api.anthropic.com/v1/sessions/{session_id}")
            if status.get("status") == "idle":
                break
            import time; time.sleep(5)

        # Get events
        events = curl("GET", f"https://api.anthropic.com/v1/sessions/{session_id}/events")
        for event in events.get("events", []):
            if event.get("type") == "agent.message":
                for block in event.get("content", []):
                    if block.get("type") == "text":
                        output.append(block["text"])

        result = "".join(output)
        print(f"  {name} done ({len(result)} chars)")
        return result

    except Exception as e:
        print(f"  {name} failed: {e}")
        return "[]"

def run_collectors():
    prompts = {
        "slack":     "Pull Slack signals from the last 7 days. Return structured JSON array only.",
        "granola":   "Pull Granola meeting signals from the last 7 days. Return structured JSON array only.",
        "hubspot":   "Pull HubSpot CS tickets and AM notes from the last 7 days. Return structured JSON array only.",
        "sms":       "Pull SMS signals from the CSV provided. Return structured JSON array only.",
        "churn":     "Pull churn data from the CSV provided. Return structured JSON array including summary block.",
        "dealscore": "Pull deal score data from the CSV provided. Return structured JSON array including summary block.",
        "mixpanel":  "Pull Partner Portal engagement data from the last 7 days. Return structured JSON array including summary block.",
    }
    print("Running collectors in parallel...")
    with ThreadPoolExecutor(max_workers=7) as executor:
        futures = {
            name: executor.submit(run_session, name, AGENT_IDS[name], prompt)
            for name, prompt in prompts.items()
        }
    return {name: f.result() for name, f in futures.items()}

def run_orchestrator(signals):
    print("Running orchestrator...")
    message = "\n\n".join([f"## {name} signals\n{data}" for name, data in signals.items()])
    return run_session("orchestrator", AGENT_IDS["orchestrator"], message)

def save_synthesis(output):
    week = datetime.now().strftime("%Y-W%W")
    try:
        routing_start = output.index("```routing")
        synthesis = output[:routing_start].strip()
    except ValueError:
        synthesis = output

    path = Path.home() / f"PM/customer-repo/synthesis/{week}-synthesis.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text(synthesis)
    print(f"Synthesis saved: {path}")
    os.system(f'cd ~/PM/customer-repo\\ 2 && git add synthesis/ && git commit -m "chore: weekly synthesis {week}" && git push origin main')

def handle_routing(output):
    try:
        start = output.index("```routing") + len("```routing")
        end = output.index("```", start)
        routing = json.loads(output[start:end].strip())
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Could not parse routing block: {e}")
        return

    week = datetime.now().strftime("%Y-W%W")

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
    signals = run_collectors()
    print("\nAll collectors complete.\n")
    output = run_orchestrator(signals)
    print("\nOrchestrator complete.\n")
    save_synthesis(output)
    handle_routing(output)
    print("\n✅ Crilly run complete.\n")
