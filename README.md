# EatClub Customer Intelligence Repo

A living system for building proximity to real customer and field problems — before they get interpreted into solution requests.

## The problem this solves

By the time a stakeholder brings a problem to product, it has usually already been filtered through their mental model and converted into a solution. This repo short-circuits that path — pulling raw signals directly from where problems live (Slack, HubSpot, meetings, support) and synthesising them into structured problem intelligence using product-rigorous frameworks.

**The goal is not to capture everything. It's to see themes before anyone else names them.**

---

## How it works

```
Raw signals (Slack, HubSpot, Granola, Support)
        ↓
Weekly dump into /signals/{source}/YYYY-WW.md
        ↓
Run synthesis script → Claude applies product frameworks
        ↓
Problem cards created/updated in /opportunities/
        ↓
OST branches updated, discovery tickets raised in Jira
```

---

## Repo structure

```
/signals/
  /slack/          Raw channel signal dumps — #customer-feedback, #am-team, #urgent, #cs-am
  /granola/        Meeting notes — Pan, Sam, Luke, Jeroen sessions
  /hubspot/        AM/BDM call notes, churn reasons, deal lost reasons
  /support/        SD ticket patterns, recurring issues

/opportunities/    Problem cards — one per named opportunity
/synthesis/        Weekly synthesis outputs — themes, rising signals, OST mapping
/scripts/          Claude synthesis prompts and automation helpers
```

---

## Weekly cadence

| When | What |
|---|---|
| Monday | Dump signals from prior week into /signals/ |
| Monday | Run synthesis script — update opportunity cards |
| Tuesday | Review rising themes — flag for discovery |
| Ongoing | Add signals as they surface — don't batch everything to Monday |

---

## Core discipline

Every signal gets translated into a **problem statement**, not a solution request.

> ❌ "Luke says we need push notifications"
> ✅ "Venues are missing time-sensitive deal activity because they're not in the product at the moment the event happens"

The synthesis step does this translation automatically — but you need to log the raw signal first.
