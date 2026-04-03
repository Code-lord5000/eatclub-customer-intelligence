#!/usr/bin/env python3
"""
EatClub SMS Log Processor
Run this locally against any Aircall SMS CSV export.
Output appends to synthesis/SMS-BASELINE.md automatically.

Usage:
    python3 process-sms-csv.py path/to/your-sms-export.csv

Requirements:
    Python 3.7+ (no external dependencies)
"""

import csv
import sys
import os
from collections import Counter, defaultdict
from datetime import datetime

def process_sms_csv(filepath):
    print(f"\nProcessing: {filepath}")

    rows = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"  Total rows: {len(rows)}")

    # Split inbound/outbound
    external = [r for r in rows if r.get('direction') == 'external']
    internal = [r for r in rows if r.get('direction') == 'internal']

    # Text field — Aircall uses encrypted_aes_text despite the name
    def get_text(r):
        return r.get('encrypted_aes_text', r.get('encrypted_text', '')).strip()

    # Date range
    dates = [r['date'][:10] for r in rows if r.get('date')]
    date_min = min(dates) if dates else 'unknown'
    date_max = max(dates) if dates else 'unknown'

    # --- OUTBOUND SIGNAL COUNTS ---
    outbound_signals = {
        'card_setup_failure': 0,
        'payment_timeout': 0,
        'duplicate_payment': 0,
        'offer_not_started': 0,
        'offer_expired': 0,
        'compensation_voucher': 0,
        'uninformed_venue_apology': 0,
    }

    for r in internal:
        msg = get_text(r).lower()
        if "haven't set up your eatclub digital card" in msg:
            outbound_signals['card_setup_failure'] += 1
        if 'timed out' in msg and 'payment' in msg:
            outbound_signals['payment_timeout'] += 1
        if 'same as another payment' in msg:
            outbound_signals['duplicate_payment'] += 1
        if "offer hasn't started" in msg:
            outbound_signals['offer_not_started'] += 1
        if 'offer has expired' in msg:
            outbound_signals['offer_expired'] += 1
        if any(w in msg for w in ['extra $', 'make it up', '$10 off', '$15 off', '$20 off', 'use this code']):
            outbound_signals['compensation_voucher'] += 1
        if any(w in msg for w in ['not informed', 'we are not informed', 'closed venue', 'closed today']):
            outbound_signals['uninformed_venue_apology'] += 1

    # --- INBOUND SIGNAL CATEGORIES ---
    inbound_categories = defaultdict(list)

    for r in external:
        msg = get_text(r)
        msg_lower = msg.lower()
        if not msg or len(msg) < 3:
            continue

        if any(w in msg_lower for w in ['closed', 'close', 'lights were off', 'locked', 'not open']):
            inbound_categories['venue_closed'].append(msg)
        if any(w in msg_lower for w in ['refund', 'charged twice', 'charged me', 'double charge']):
            inbound_categories['refund_billing'].append(msg)
        if any(w in msg_lower for w in ['how do i cancel', 'how do we cancel', 'cancel the order',
                                         'no option', "doesn't seem to be an option", "can't cancel"]):
            inbound_categories['no_cancellation_selfserve'].append(msg)
        if any(w in msg_lower for w in ['annoying', 'unimpressed', 'misleading', 'won\'t be using',
                                         'poor service', 'disappointing', 'never again', 'not happy']):
            inbound_categories['churn_sentiment'].append(msg)
        if any(w in msg_lower for w in ["no way to", "can't turn off", "can't change", "can't update",
                                         "deactivate it", "turn off", "how do i", "how do we",
                                         "no option", "can not update"]):
            inbound_categories['venue_selfserve_gap'].append(msg)
        if any(w in msg_lower for w in ['missing', 'wrong order', 'wrong item']):
            inbound_categories['wrong_missing_order'].append(msg)
        if any(w in msg_lower for w in ['thank', 'thanks', 'great', 'appreciate', 'perfect', 'awesome']):
            inbound_categories['positive'].append(msg)

    # --- BUILD OUTPUT ---
    days = max(1, (datetime.fromisoformat(date_max) - datetime.fromisoformat(date_min)).days + 1)
    lines = []

    lines.append(f"\n---\n")
    lines.append(f"## Period: {date_min} to {date_max} ({days} days)\n")
    lines.append(f"**Processed**: {datetime.now().strftime('%Y-%m-%d')}  \n")
    lines.append(f"**Source file**: {os.path.basename(filepath)}  \n")
    lines.append(f"**Total messages**: {len(rows):,} ({len(internal):,} outbound / {len(external):,} inbound)\n\n")

    lines.append("### Outbound automated signals (product failure indicators)\n\n")
    lines.append("| Signal | Count | Daily rate | Baseline comparison |\n")
    lines.append("|---|---|---|---|\n")

    baselines = {
        'card_setup_failure':      ('B1 card setup failure', 172),
        'payment_timeout':         ('B3 payment timeout', 38),
        'duplicate_payment':       ('B6 duplicate payment', 5),
        'offer_not_started':       ('B5 offer timing', 18),
        'offer_expired':           ('B5 offer timing', 18),
        'compensation_voucher':    ('Cost baseline', 218),
        'uninformed_venue_apology':('B2 venue closure', 8),
    }

    for key, count in outbound_signals.items():
        daily = round(count / days, 1)
        baseline_name, baseline_rate = baselines.get(key, ('—', None))
        if baseline_rate:
            diff = daily - baseline_rate
            comparison = f"{'↑' if diff > 0 else '↓'} {abs(diff):.1f}/day vs Dec 2024 baseline"
        else:
            comparison = "No baseline"
        lines.append(f"| {key.replace('_', ' ').title()} | {count:,} | {daily}/day | {comparison} |\n")

    lines.append("\n### Inbound customer signal categories\n\n")
    lines.append("| Category | Count | % of inbound |\n")
    lines.append("|---|---|---|\n")
    total_inbound = len(external)

    for cat, msgs in sorted(inbound_categories.items(), key=lambda x: -len(x[1])):
        pct = len(msgs) / total_inbound * 100 if total_inbound else 0
        lines.append(f"| {cat.replace('_', ' ').title()} | {len(msgs)} | {pct:.1f}% |\n")

    lines.append("\n### Strongest verbatim signals this period\n\n")
    lines.append("(Highest-signal inbound customer messages — for problem card evidence)\n\n")

    high_signal_cats = ['churn_sentiment', 'venue_selfserve_gap', 'no_cancellation_selfserve']
    for cat in high_signal_cats:
        msgs = inbound_categories.get(cat, [])
        if msgs:
            lines.append(f"**{cat.replace('_', ' ').title()}:**\n")
            for msg in msgs[:5]:
                lines.append(f"> {msg[:250]}\n\n")

    return ''.join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process-sms-csv.py path/to/sms-export.csv")
        print("       python3 process-sms-csv.py file1.csv file2.csv file3.csv")
        sys.exit(1)

    # Find baseline file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    baseline_path = os.path.join(repo_root, 'synthesis', 'SMS-BASELINE.md')

    if not os.path.exists(baseline_path):
        print(f"Error: Baseline file not found at {baseline_path}")
        sys.exit(1)

    # Process each CSV
    all_output = []
    for filepath in sys.argv[1:]:
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
        output = process_sms_csv(filepath)
        all_output.append(output)

    if not all_output:
        print("No files processed.")
        sys.exit(1)

    # Append to baseline
    with open(baseline_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(all_output))

    print(f"\n✅ Done. Findings appended to:\n   {baseline_path}")
    print("\nNext steps:")
    print("  1. Review the appended findings in SMS-BASELINE.md")
    print("  2. git add . && git commit -m 'Add SMS period: [dates]' && git push")
    print("  3. The agent will pick up the updated baseline on next Cowork run")


if __name__ == '__main__':
    main()
