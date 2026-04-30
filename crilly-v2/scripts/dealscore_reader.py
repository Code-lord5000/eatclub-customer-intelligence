"""
Dealscore CSV reader: identifies deal score signals deterministically.

NO Claude agent involved. Pure Python parsing the latest dealscore CSV
and outputting the same JSON envelope shape as the v2 collector agents.

Signal types extracted:
- score_drop_critical: change <= -300 (serious decline)
- score_drop_significant: change <= -100 (moderate decline)
- score_danger_zone: current < 100 AND change is negative (low and falling)
- score_rise: change >= +100 (positive signal)
- watch_list_movement: any change touching a watch list venue

Month-start behaviour:
- Days 1-3 of each month: CSV resets to zero, no signals extracted.
  Returns a coverage note explaining the skip.

Usage:
    from dealscore_reader import collect_dealscore_signals
    brief = collect_dealscore_signals(last_run_at, themes, watch_list)
"""

import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path

SIGNALS_BASE = Path.home() / "PM/customer-repo/signals/dealscore"

# Thresholds — based on observed range of 0-1000ish
CRITICAL_DROP_THRESHOLD = -300
SIGNIFICANT_DROP_THRESHOLD = -100
RISE_THRESHOLD = 100
DANGER_ZONE_SCORE = 100
MONTH_START_SKIP_DAYS = 3  # Skip days 1-3 of each month


def _load_latest_csv():
    """Returns path to most recent CSV in dealscore folder, or None."""
    if not SIGNALS_BASE.exists():
        return None
    files = sorted(SIGNALS_BASE.glob("*.csv"), key=os.path.getmtime, reverse=True)
    return files[0] if files else None


def _parse_csv(csv_path):
    """Parses dealscore CSV. Handles dynamic 'Current (<date>)' column header."""
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        current_col = None
        for col in reader.fieldnames or []:
            if col.startswith("Current"):
                current_col = col
                break
        for row in reader:
            row["_current_score"] = row.get(current_col, "") if current_col else ""
            row["_current_col_name"] = current_col or "Current"
            rows.append(row)
    return rows


def _safe_int(value):
    """Converts CSV value to int; returns None on failure."""
    if value is None or value == "":
        return None
    try:
        return int(float(str(value).replace(",", "").strip()))
    except (ValueError, TypeError):
        return None


def _venue_in_watchlist(venue_name, watch_list):
    """Case-insensitive match against watch list."""
    if not venue_name:
        return False
    venue_lower = venue_name.lower().strip()
    for w in watch_list:
        if w.get("venue", "").lower().strip() == venue_lower:
            return True
    return False


def _build_signal(signal_type, row, change, current, start, watch_list_hit,
                  theme_id=None, okr=None, confidence="high"):
    """Constructs a signal in the standard envelope format."""
    venue = row.get("Venue", "").strip()
    change_str = f"{change:+d}" if change is not None else "unknown"
    return {
        "type": signal_type,
        "venue": venue or None,
        "rest_id": row.get("Rest ID", "").strip() or "UNKNOWN",
        "evidence": (
            f"Deal score: start={start}, change={change_str}, current={current}. "
            f"AM: {row.get('AM Name', 'unknown').strip()}. "
            f"Region: {row.get('Region', 'unknown').strip()}."
        ),
        "confidence": confidence,
        "maps_to_okr": okr or "OKR2",
        "maps_to_theme": theme_id,
        "am_name": row.get("AM Name", "").strip() or None,
        "region": row.get("Region", "").strip() or None,
        "suburb": row.get("Suburb", "").strip() or None,
        "postcode": row.get("Postcode", "").strip() or None,
        "watch_list_hit": watch_list_hit,
        "score_start": start,
        "score_change": change,
        "score_current": current,
    }


def _empty_brief(last_run_at, now_iso, coverage_notes):
    return {
        "source": "dealscore",
        "window": {"from": last_run_at, "to": now_iso},
        "signals": [],
        "unmapped_signals": [],
        "theme_drift_observations": [],
        "counts": {
            "total_signals": 0,
            "high_confidence": 0,
            "watch_list_hits": 0,
            "theme_evidence_count": 0,
            "new_signal_count": 0,
            "unmapped_signal_count": 0,
            "theme_drift_count": 0,
            "score_drops_critical": 0,
            "score_drops_significant": 0,
            "score_danger_zone": 0,
            "score_rises": 0,
        },
        "coverage_notes": coverage_notes,
    }


def collect_dealscore_signals(last_run_at, themes=None, watch_list=None):
    """Main entry point. Returns JSON brief in standard envelope shape."""
    themes = themes or []
    watch_list = watch_list or []
    now_iso = datetime.now(timezone.utc).isoformat()

    # Month-start skip — CSV resets to zero on 1st, data meaningless for first 3 days
    today = datetime.now(timezone.utc)
    if today.day <= MONTH_START_SKIP_DAYS:
        return _empty_brief(
            last_run_at, now_iso,
            f"Dealscore skipped — day {today.day} of month. "
            f"CSV resets to zero on the 1st. Re-runs after day {MONTH_START_SKIP_DAYS} will have meaningful data."
        )

    csv_path = _load_latest_csv()
    if not csv_path:
        return _empty_brief(
            last_run_at, now_iso,
            f"No dealscore CSV found in {SIGNALS_BASE}."
        )

    rows = _parse_csv(csv_path)

    # Find theme for value/engagement mapping (T005 — high fees / misconception of value)
    value_theme_id = None
    for t in themes:
        if "fees" in (t.get("theme") or "").lower() or "value" in (t.get("theme") or "").lower():
            value_theme_id = t.get("theme_id")
            break

    signals = []
    watch_list_hits = 0
    drops_critical = 0
    drops_significant = 0
    danger_zone_count = 0
    rises = 0
    rows_with_no_change = 0

    for row in rows:
        venue = row.get("Venue", "").strip()
        change = _safe_int(row.get("Change"))
        current = _safe_int(row.get("_current_score"))
        start = _safe_int(row.get("Start Balance"))
        is_watch = _venue_in_watchlist(venue, watch_list)

        if is_watch:
            watch_list_hits += 1

        # Skip rows with no change — not a signal
        if change is None or change == 0:
            rows_with_no_change += 1
            # Still flag watch list venues even with no change
            if is_watch:
                signals.append(_build_signal(
                    "watch_list_no_change", row, change, current, start,
                    True, theme_id=None, okr="OKR2", confidence="low"
                ))
            continue

        # CRITICAL drop — serious decline
        if change <= CRITICAL_DROP_THRESHOLD:
            drops_critical += 1
            signals.append(_build_signal(
                "score_drop_critical", row, change, current, start,
                is_watch, theme_id=value_theme_id, okr="OKR2", confidence="high"
            ))
            continue

        # SIGNIFICANT drop — moderate decline
        if change <= SIGNIFICANT_DROP_THRESHOLD:
            drops_significant += 1
            # Extra flag if also in danger zone
            if current is not None and current < DANGER_ZONE_SCORE:
                danger_zone_count += 1
                signals.append(_build_signal(
                    "score_danger_zone", row, change, current, start,
                    is_watch, theme_id=value_theme_id, okr="OKR2", confidence="high"
                ))
            else:
                signals.append(_build_signal(
                    "score_drop_significant", row, change, current, start,
                    is_watch, theme_id=value_theme_id, okr="OKR2", confidence="medium"
                ))
            continue

        # RISE — positive signal
        if change >= RISE_THRESHOLD:
            rises += 1
            signals.append(_build_signal(
                "score_rise", row, change, current, start,
                is_watch, theme_id=None, okr="OKR2", confidence="medium"
            ))
            continue

        # Watch list venue with any movement below main thresholds
        if is_watch and abs(change) > 0:
            signals.append(_build_signal(
                "watch_list_movement", row, change, current, start,
                True, theme_id=None, okr="OKR2", confidence="medium"
            ))

    # Cap at 60 — prioritise watch list hits and critical drops
    if len(signals) > 60:
        critical = [s for s in signals if s["type"] in ("score_drop_critical", "score_danger_zone", "watch_list_movement")]
        others = [s for s in signals if s not in critical]
        others.sort(key=lambda s: abs(s.get("score_change") or 0), reverse=True)
        signals = critical + others[:60 - len(critical)]
        coverage_extra = f" Output capped at 60 (total signals before cap: {len(signals) + len(others)})."
    else:
        coverage_extra = ""

    return {
        "source": "dealscore",
        "window": {"from": last_run_at, "to": now_iso},
        "signals": signals,
        "unmapped_signals": [],
        "theme_drift_observations": [],
        "counts": {
            "total_signals": len(signals),
            "high_confidence": sum(1 for s in signals if s["confidence"] == "high"),
            "watch_list_hits": watch_list_hits,
            "theme_evidence_count": sum(1 for s in signals if s.get("maps_to_theme")),
            "new_signal_count": 0,
            "unmapped_signal_count": 0,
            "theme_drift_count": 0,
            "score_drops_critical": drops_critical,
            "score_drops_significant": drops_significant,
            "score_danger_zone": danger_zone_count,
            "score_rises": rises,
            "rows_with_no_change": rows_with_no_change,
        },
        "coverage_notes": (
            f"Parsed {len(rows)} venues from {csv_path.name} (day {today.day} of month). "
            f"Critical drops (≤{CRITICAL_DROP_THRESHOLD}): {drops_critical}. "
            f"Significant drops (≤{SIGNIFICANT_DROP_THRESHOLD}): {drops_significant}. "
            f"Danger zone (current<{DANGER_ZONE_SCORE} and falling): {danger_zone_count}. "
            f"Rises (≥{RISE_THRESHOLD}): {rises}. "
            f"Watch list hits: {watch_list_hits}. "
            f"No-change rows skipped: {rows_with_no_change}.{coverage_extra}"
        ),
    }


if __name__ == "__main__":
    import sys
    last_run_at = sys.argv[1] if len(sys.argv) > 1 else datetime.now(timezone.utc).isoformat()

    memory_file = Path.home() / "PM/customer-repo/crilly-v2/memory.json"
    if memory_file.exists():
        memory = json.loads(memory_file.read_text())
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
    else:
        themes = []
        watch_list = []

    brief = collect_dealscore_signals(last_run_at, themes, watch_list)
    print(json.dumps(brief, indent=2, default=str))
