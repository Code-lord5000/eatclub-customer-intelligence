# HubSpot Signal Capture — Guide

HubSpot is the richest longitudinal source in the repo. Unlike Slack (reactive, real-time) and Granola (strategic/meeting), HubSpot contains field notes written by AMs and BDMs at the moment of customer contact — before the signal has been interpreted by anyone upstream.

## What to pull from HubSpot

### 1. Churn reasons (highest value)
- Lost deal reasons logged at churn
- AM notes on final conversations with churned venues
- Any "reason for leaving" fields

Look for: **exact language venues used**, not AM's interpretation. If the note says "venue said they weren't getting enough covers" that's different from "venue felt ROI was unclear."

### 2. Deal lost reasons (BDM pipeline)
- Reasons deals didn't close in the first place
- Objections logged during sales process
- Competitor mentions

### 3. AM call notes (ongoing accounts)
- Any notes logged after venue check-ins
- Escalation notes
- "Venue flagged..." entries

### 4. Deal stage stagnation
- Deals sitting in same stage for 30+ days — often signals a friction problem neither side has named yet

---

## How to log HubSpot signals

When pulling from HubSpot, use the standard signal template but add:

**HubSpot record**: [Deal/Contact/Company name or ID]
**AM/BDM**: [who wrote the note]
**Date of note**: [when it was logged — not when you're capturing it]

This matters for frequency tracking — a churn reason logged 6 months ago that keeps reappearing is a different signal than one that's new this week.

---

## Queries to run weekly

These are the HubSpot views worth checking each Monday:

| What | Why |
|---|---|
| Deals closed-lost in last 7 days | Fresh churn reasons |
| Deals with no activity in 21+ days | Silent venue precursors |
| Contacts with "escalation" in notes | AM-flagged friction |
| New deals with deal score = 0 | Activation failures |
| Any note containing "competitor" | Market positioning signals |

---

## The synthesis question for HubSpot data

When Claude processes HubSpot signals, the key question is:

> **Is this a one-venue problem or a pattern?**

A single venue saying "the app is confusing" is noise. Five venues in different cities in the same month saying "we couldn't figure out how to change the deal" is a usability problem worth a problem card.

HubSpot is where patterns become undeniable — because the data has timestamps, deal values, and AM names attached.
