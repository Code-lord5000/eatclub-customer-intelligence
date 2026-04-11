# Crilly Synthesis — 2026-W15 (April 7–11, 2026)

**Sources available**: Churn/Pause CSV (96 records, 141 total April), Deal Score CSV (4,314 venues)
**Sources unavailable this run**: Slack (8 channels), Granola meeting transcripts, HubSpot, SMS, Mixpanel
**Confidence note**: This synthesis is running on 2 of 7 signal sources. Themes flagged here should be treated as confirmed from structured data but may be missing context that Slack/Granola/SMS would provide. Severity is likely *understated*.

---

## 🔥 Rising Themes This Week

### 1. Integration Delays Are Causing Batch Early Churn Before Venues Ever Go Live

**Heat**: 🔴 **HIGH**
**Signal count**: 11 venues, 1 source (churn CSV), single-day event (April 10)
**Recurrence**: NEW — first time this pattern appears as a batch event at this scale
**Problem statement**: Venues that have signed and are waiting on POS/booking integration are sitting in limbo with no active deals. When the integration stalls, they churn before they ever experience value. 11 venues paused on the same day with identical notes, suggesting a systemic pipeline blockage — likely a single integration partner or internal resource bottleneck rather than 11 independent failures.
**Mom Test quality**: **STRONG** — These aren't opinions. These venues literally left because of a specific, observable failure. The behaviour (mass same-day pause) is the evidence.
**OKR**: OKR 3 (Churn Reduction) — primary. OKR 1 (AM Optimisation) — secondary, because AMs are likely spending time manually managing venues stuck in integration queue.
**OST branch**: Churn reduction → Onboarding journey quality; AM optimisation → System automation opportunities
**Journey stage**: Onboarding / Activation (never reached activation)
**Recommended action**: **🚨 ESCALATE** — This is not a product insight to sit on. 11 venues lost in a single day to the same root cause. Immediate questions: (1) Which integration partner(s) are blocked? (2) What is the current integration backlog? (3) Is there an SLA with integration partners, and was it breached? (4) Were these venues warned, or did they just go silent? Route to Pan/Luke immediately with request for integration pipeline audit.

**Cross-reference**: Several of these Melbourne venues (Cinder, Ember - Sorrento, Continental - Sorrento, Cee Cee's - Sorrento, Doutta Galla) may be part of a group or share a common POS system. The Sorrento cluster (3 venues) is particularly suspicious — same suburb, same day, likely same operator or same POS. If this is a group, the integration failure cost us a group relationship, not just individual venues.

---

### 2. Venues Cannot Prevent Customers From Stacking EatClub Discounts on Already-Discounted Items ("Double Dipping")

**Heat**: 🔴 **HIGH**
**Signal count**: 6 venues across 2 regions (4 Burpengary cluster + Ravenspur Sydney + Bricco e Bacco London), 1 source
**Recurrence**: **RECURRING** — this has appeared in prior weeks. The Burpengary cluster makes it acute this week.
**Problem statement**: Venues running their own promotions (happy hours, lunch specials, set menus) have no mechanism to prevent EatClub offers from being redeemed on top of those discounted items. This means the venue eats a double discount — their own promotion PLUS the EatClub %. The AM response is "we integrate with RedCat" — which is either (a) not actually solving the problem, since all 4 venues still churned, or (b) the integration isn't live yet for these venues (see Theme 1). Either way, the answer isn't working.
**Mom Test quality**: **STRONG** — "Customers are redeeming 30% off on already discounted items" is a specific, observed behaviour with direct financial impact. Not hypothetical.
**OKR**: OKR 3 (Churn Reduction) — direct. OKR 2 (Deal Performance) — venues need control over when/where deals apply to keep deals running confidently.
**OST branch**: Churn reduction → Friction in core venue experience; Deal performance → Venue-led revenue actions (venues can't safely run deals alongside their own promos)
**Journey stage**: Ongoing engagement → Renewal/churn decision
**Recommended action**: **Discovery ticket** — The "integrate with RedCat" response is being given identically by AMs to 4 venues in the same suburb. If the integration solves this, why are they churning? If it doesn't solve this, we're giving venues a false promise. Need to understand: (1) What does the RedCat integration actually do re: item-level exclusions? (2) Can venues currently exclude specific items/categories from EatClub offers? (3) If not, what would that require? (4) What % of venues run concurrent internal promotions?

**Burpengary note**: 4 venues in one suburb, all churning for the same reason, all told the same thing. This looks like one BDM signed a cluster, all hit the same wall, and word spread between them. Classic small-market network effect working against us.

---

### 3. Manchester Market Launch Is Failing at the Commission Education Stage

**Heat**: 🔴 **HIGH**
**Signal count**: 9 venues, 1 source, single market
**Recurrence**: **NEW** as a cluster, but commission misconception is **CHRONIC** across all markets (18 misconception records this week total)
**Problem statement**: Manchester venues are churning in their first weeks because they did not understand the commission/payment model at point of sale. Multiple patterns compound: (1) BDMs who signed venues have left or are unreachable, (2) AMs inherited accounts with no context, (3) at least one venue (Sushi Doki) was signed despite not being ICP, (4) debt is accumulating because venues refuse to pay what they didn't understand they owed. This is a new-market playbook failure, not a product failure — but it becomes a product problem when the onboarding flow doesn't catch and correct the misconception before the venue goes live.
**Mom Test quality**: **STRONG** — "Beppe wasn't happy during our initial meeting as he wasn't aware of the service charge commission" / "confusion around the commission — I've chased the GM for payments" / "not ICP, should not have been signed." These are specific past events.
**OKR**: OKR 3 (Churn Reduction) — primary. OKR 1 (AM Optimisation) — AMs are spending time chasing payments and explaining commission that should have been clear from sign-up.
**OST branch**: Churn reduction → Onboarding journey quality; AM optimisation → Manual AM task reduction (chasing payments = pure waste if the root cause is sign-up clarity)
**Journey stage**: Onboarding (commission education) → AM relationship (inherited broken relationships)
**Recommended action**: **Escalate to Sam Benjamin (Sales)** — This is a BDM quality/process issue at root. Product actions: (1) Audit the Arrows onboarding flow for Manchester — does it include explicit commission acknowledgement? (2) Should there be a "commission confirmation" gate before first deal goes live? (3) Can the Partner Portal surface commission structure more prominently? Also escalate to Luke — AMs in Manchester are firefighting BDM mistakes, which is a direct OKR 1 cost.

**Linked venues**: Fress Restaurant & Khau Galli are explicitly linked (same ownership). One owner's confusion has already taken two venues offline and created a debt dispute.

---

### 4. Group/Enterprise Accounts Churn in Cascades — One Decision-Maker Takes Multiple Venues Off Platform

**Heat**: 🟡 **MEDIUM-HIGH**
**Signal count**: 3 groups, 9+ venues, 1 source
**Recurrence**: **CHRONIC** — group churn has been flagged in prior weeks
**Problem statement**: When a group operations manager or owner decides to leave, every venue in the group leaves simultaneously. This week: (1) Chahoud Group / Adelaide — Tom (ops manager) is consolidating all marketing to a competitor, taking 5 venues with him. (2) Gemelli Group / Gold Coast — 2 venues paused "following on from other venues in group." (3) Possible Sorrento cluster in Melbourne (3 integration-blocked venues in same suburb). The platform has no group-level relationship management, no group-level deal or reporting view, and no early-warning system when a group begins to disengage.
**Mom Test quality**: **STRONG** — "They want to consolidate all their offers and marketing through one platform" is a specific competitive loss with a stated reason. The Gemelli cascade is observed behaviour.
**OKR**: OKR 3 (Churn Reduction) — direct. A single group churn event can be 3-10x the impact of an individual venue churn.
**OST branch**: Churn reduction → Product fit for enterprise / Groups
**Journey stage**: Renewal/churn decision point
**Recommended action**: **Discovery ticket** — (1) How many active venues are part of multi-venue groups? (2) What % of churn volume comes from group cascades? (3) What would a "group account" look like in Partner Portal / Hub? (4) Should AMs have a group-level view showing aggregate engagement across all venues under one operator? **Interview**: Get to Tom (Chahoud Group) — what platform are they consolidating to, and what does "consolidate all offers and marketing" mean specifically?

---

### 5. Venues Lose Control of When Deals Are Active and Cannot React in Real-Time

**Heat**: 🟡 **MEDIUM**
**Signal count**: 4-5 venues, 1 source
**Recurrence**: **RECURRING**
**Problem statement**: Venues cannot easily turn deals off when they need to (Central Lounge — "owner is furious, was emailing and calling to take off deals"), cannot control which hours deals are visible (Pizze Baby — got a 1-star review because a customer saw a deal during hours the venue considered booking-only), and cannot see redemptions happening in real time (Dawg Boys — "wants to see offers being redeemed in real time"). The gap: deal activation/deactivation is not sufficiently in the venue's hands, and when it isn't, the AM becomes the bottleneck (OKR 1 cost) and the venue takes reputation damage (churn risk).
**Mom Test quality**: **STRONG** — "Owner is furious he was emailing and calling Rosh to take off deals" is a specific, high-stakes past event. "Got a 1-star review from a customer who tried to redeem" is a concrete negative outcome.
**OKR**: OKR 2 (Deal Performance) — venues need confidence that they control when deals run. OKR 1 (AM Optimisation) — AMs are the current off-switch, which is manual and slow.
**OST branch**: Deal performance → Venue-led revenue actions; AM optimisation → Venue self-serve capability
**Journey stage**: Ongoing engagement
**Recommended action**: **Discovery ticket** — (1) Can venues currently pause/unpause deals themselves via Partner Portal? If yes, is the UX discoverable? If no, this is a critical self-serve gap. (2) What is the latency between a venue requesting a deal change and it going live? (3) Would a "panic button" (instant deal pause) in Partner Portal reduce AM load?

---

## 📋 All Signals This Week — Classified

| # | Signal Summary | Source | Author Team | Who Affected | Mom Test | OKR | Theme | OST Branch |
|---|---------------|--------|------------|--------------|---------|-----|-------|------------|
| 1 | 11 venues paused April 10 — identical "integration delay" note | Churn CSV | System/AM | 11 venues (Melb/Bris/GC) | STRONG | OKR 3, OKR 1 | Integration Delay | Onboarding quality |
| 2 | 4 Burpengary venues churn — double dipping, told "we integrate with RedCat" | Churn CSV | AM/BDM | 4 venues (Brisbane) | STRONG | OKR 3, OKR 2 | Double Dipping | Core venue experience friction |
| 3 | Ravenspur (Syd) — running own happy hour, can't coexist with EC deals | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Double Dipping | Core venue experience friction |
| 4 | Bricco e Bacco (Lon) — internal promos + booking fees + integration failure | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Double Dipping + Integration | Core experience + Onboarding |
| 5 | 9 Manchester early churns — commission misconception, BDM handoff failures | Churn CSV | AM | 9 venues (Manchester) | STRONG | OKR 3, OKR 1 | Manchester Launch Failure | Onboarding quality |
| 6 | Sushi Doki (Manchester) — "not ICP, should not have been signed" | Churn CSV | AM (Marco) | 1 venue | STRONG | OKR 3 | Manchester Launch Failure | Onboarding quality |
| 7 | Fress + Khau Galli linked — same owner, commission confusion, refusing to pay debt | Churn CSV | AM | 2 venues | STRONG | OKR 3 | Manchester Launch Failure + Debt | Onboarding + Financial |
| 8 | Chahoud Group / Adelaide — Tom consolidating to competitor, 5 venues leaving | Churn CSV | AM | 5 venues (Adelaide) | STRONG | OKR 3 | Group Cascade Churn | Enterprise/Groups |
| 9 | Gemelli Group / Gold Coast — 2 venues paused following other group venues | Churn CSV | AM | 2 venues | STRONG | OKR 3 | Group Cascade Churn | Enterprise/Groups |
| 10 | Central Lounge (GC) — owner furious, couldn't reach AM to remove deals during promo | Churn CSV | AM | 1 venue | STRONG | OKR 1, OKR 2 | Venue Control Gap | Self-serve capability |
| 11 | Pizze Baby (Syd) — 1-star review from customer trying to redeem outside hours | Churn CSV | AM | 1 venue | STRONG | OKR 3, OKR 2 | Venue Control Gap | Core experience friction |
| 12 | Dawg Boys (Bris) — wants real-time redemption visibility | Churn CSV | AM | 1 venue | MEDIUM | OKR 2 | Venue Control Gap | Venue-led revenue actions |
| 13 | 7 Sydney venues paused April 9 — identical templated "outstanding invoices" note | Churn CSV | Admin | 7 venues (Sydney) | STRONG | OKR 3 | Debt Batch Pause | Financial friction |
| 14 | Man-O-Salwa (Melb) — blocked EC transactions from bank, $969 owing | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Debt | Financial friction |
| 15 | Raato Ghar (Syd) — deal score 756 → 0, paused for $1k balance | Churn CSV + Deal Score | AM | 1 venue | STRONG | OKR 3 | Debt + Score Collapse | Financial friction |
| 16 | Mishy's (Syd) — "no support for venues," likes Offerless, pays herself $75k | Churn CSV | AM | 1 venue | STRONG | OKR 3, OKR 2 | Support Gap / Customer Quality | AM relationship + Deal performance |
| 17 | Harry's Cafe (Melb) — "unaware of GST on top of commission" | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Fee Misconception | Onboarding quality |
| 18 | Lardo & Bastardo (Lon) — integration failure with booking system, detailed email | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Integration Delay | Onboarding quality |
| 19 | 284 venues with deal score = 0 | Deal Score CSV | System | 284 venues | STRONG (behavioural) | OKR 3, OKR 2 | Silent Disengagement | Deal performance + Churn |
| 20 | 94 venues with deal score drop ≥ 50 | Deal Score CSV | System | 94 venues | STRONG (behavioural) | OKR 2, OKR 3 | Deal Performance Decline | Deal performance |
| 21 | 6 customer quality complaints across 4 regions | Churn CSV | AM | 6 venues | MEDIUM | OKR 3 | Customer Quality | Core experience friction |
| 22 | Second Wife (Melb) — "simply text me requesting to cancel while I was away" | Churn CSV | AM | 1 venue | STRONG | OKR 3, OKR 1 | AM Availability Gap | AM relationship |
| 23 | TYGA (Manchester) — "impossible to get hold of, doesn't respond to emails" | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Unreachable Venue | AM relationship |
| 24 | Balgowla Burgers (Syd) — "going to increase prices by 40% on other platforms to afford discount" | Churn CSV | AM | 1 venue | STRONG | OKR 3 | Margin/Economics | Core experience friction |

---

## 🗺️ OST Update

### AM Optimisation (OKR 1)

| Sub-branch | Status | This Week's Evidence |
|-----------|--------|---------------------|
| **Manual AM task reduction** | 🔺 Strengthened | AMs are the off-switch for deals (Central Lounge), AMs chasing payments for commission confusion (Manchester 9), AMs manually managing integration-stuck venues. All waste. |
| **Venue self-serve capability** | 🔺 Strengthened | Venues cannot pause deals themselves (Central Lounge), cannot see redemptions in real time (Dawg Boys), cannot adjust business hours to control offer visibility (Pizze Baby). Partner Portal self-serve gaps are directly creating AM workload. |
| **System automation opportunities** | 🔺 Strengthened | Debt batch pause (7 Sydney venues) was admin-driven, not system-triggered. Integration delay batch (11 venues) sat until they churned — no automated escalation. Deal score = 0 for 284 venues with no system-led outreach. |

### Deal Performance (OKR 2)

| Sub-branch | Status | This Week's Evidence |
|-----------|--------|---------------------|
| **Partner Portal engagement** | ⚠️ Unknown — no Mixpanel data this week | Can't assess. Need Mixpanel for W15. |
| **Venue-led revenue actions** | 🔺 Strengthened (negatively) | 284 venues at score = 0. 94 venues with score drops ≥ 50. Venues are *reducing* deal activity, not increasing it. |
| **Deal score visibility and trust** | Unchanged | No new direct signals. But 284 venues at 0 raises the question: do they know their score is 0? Does it matter to them? |

### Churn Reduction (OKR 3)

| Sub-branch | Status | This Week's Evidence |
|-----------|--------|---------------------|
| **Friction in core venue experience** | 🔺 Strengthened | Double dipping (6 venues), lack of deal control (4 venues), customer quality (6 venues), business hours mismatch (Pizze Baby) |
| **Product fit for enterprise / Groups** | 🔺 Strengthened | Chahoud Group (5 venues), Gemelli Group (2 venues), possible Sorrento cluster (3 venues). Group churn = 10+ venues this week from 3 cascades. |
| **Onboarding journey quality** | 🔺🔺 Significantly strengthened | Integration delays (11 venues), Manchester commission misconception (9 venues), GST surprise (Harry's Cafe), not-ICP signing (Sushi Doki). 20+ venues churned before ever reaching steady-state. |
| **Surfacing product value through data** | Unchanged | Mishy's signal ("no support, likes Offerless") hints venues aren't seeing value — but single signal. |

---

## ⚠️ Friction Stack Watch

These venues show compounding signals across 2+ sources or 2+ journey stages. **Flag to Luke immediately.**

### CRITICAL — Multi-source confirmed

| Venue | restID | Signals | Sources | Friction Stack |
|-------|--------|---------|---------|---------------|
| **Raato Ghar** (Sydney) | — | Deal score 756 → 0 + paused for $1k debt | Churn CSV + Deal Score CSV | Financial (debt) + Engagement collapse (score → 0). Two-source confirmation. AM: Nader Masrour. |
| **ESQ Bar & Dining** (Sydney) | — | Deal score 256.25 → 0 + paused April 9 "outstanding invoices" | Churn CSV + Deal Score CSV | Financial (debt) + Engagement collapse (score → 0). AM: Elliot Rayment. Part of the 7-venue Sydney batch pause. |

### HIGH RISK — Multi-stage friction within single source

| Venue | restID | Signals | Friction Stack |
|-------|--------|---------|---------------|
| **Fress + Khau Galli** (Manchester) | — | Commission misconception + debt refusal + linked ownership (2 venues) | Onboarding failure → Financial dispute → AM chasing → 2 venues at risk. AM has in-person meeting next week — this is a save-or-lose moment. |
| **Bricco e Bacco** (London) | — | Integration failure + internal promo conflict + booking fee accumulation + refund request | Onboarding (integration) + Ongoing (double dipping) + Financial (fees). 3-layer friction stack. |
| **Central Lounge** (Gold Coast) | — | AM unreachable + deals running during internal promo + owner furious | AM relationship failure + Control gap + Trust damage. |
| **Chahoud Group — 5 venues** (Adelaide) | — | Group consolidation to competitor, single decision-maker | If Tom leaves, 5 venues churn simultaneously. May already be past the save window. |

### WATCH — Score collapse, no churn record yet (potential pre-churn)

| Venue | restID | AM | Score Change | Note |
|-------|--------|-----|-------------|------|
| Bakmi Lim Noodle Project QV | — | Jay Franklin | 339 → 13 (−326) | No churn record. Severe decline. |
| Tradies Cafe & Bar | — | Lukas Symonds | 457.5 → 155 (−302.5) | No churn record. Check engagement. |
| Chargrill Charlie's - Annandale | — | Jordan Wellard | 292.5 → 6 (−286.5) | Near-zero. Pre-churn? |
| Burgerlot - Collingwood | — | Jay Franklin | 280 → 0 (−280) | Score = 0, no churn record = silent disengage. |
| Bean Counter | — | Gabriella Szabo | 268.75 → 0 (−268.75) | Score = 0, no churn record. Adelaide market. |

**Note for Luke**: Jay Franklin has 2 venues in the top-5 biggest score declines this week (Bakmi Lim and Burgerlot). Worth checking his full portfolio for broader disengagement pattern.

---

## 💡 Synthesis Notes

### What surprised me

1. **The integration delay batch is the single most alarming signal this week.** 11 venues on the same day is not a churn problem — it's a systems failure. These venues didn't choose to leave; they were never given the chance to start. This is pre-churn churn, and it's entirely within our control to fix. If this happened once, it will happen again.

2. **Manchester is a market-level failure, not a venue-level problem.** 9 of 96 records this week (nearly 10%) are Manchester early churns with a single root cause: venues didn't understand what they were signing up for. At least one venue was not ICP. AMs inherited accounts from BDMs without context. This is a repeatable new-market risk pattern — if we launch in other UK cities, the same thing will happen without a playbook change.

3. **Group churn accounted for ~12–15 venues this week from just 3 cascade events.** That's 12–15% of the week's churn from 3 decisions by 3 people. The concentration risk is extreme and we have no group-level tooling to detect or prevent it.

4. **The "double dipping" response is broken.** Four AMs in the same suburb gave the same answer ("we integrate with RedCat") to four venues who all still churned. Either the integration doesn't solve the problem, or the integration isn't available to these venues. Either way, the AM script is wrong and we're losing venues to a known, named problem with an apparently-known but non-functional solution.

5. **284 venues at deal score = 0 is a massive silent disengagement pool.** That's 6.6% of all tracked venues with no active deals. Without Mixpanel data this week, I can't tell you how many of those are logging into Partner Portal. But if a significant portion are also not logging in, that's a 200+ venue pre-churn cohort sitting unaddressed.

### What is missing

- **Slack signals**: Would tell us if the integration delay was discussed internally, whether there's a known blocker, and whether AMs were warned.
- **Granola / meeting transcripts**: Would give us the Tom (Chahoud Group) meeting content, the Fress/Khau Galli in-person meeting outcome, and any AM-leadership conversations about Manchester.
- **HubSpot tickets**: Would reveal whether any of the 284 score-zero venues have open support tickets.
- **Mixpanel / Partner Portal data**: Critical for understanding whether score-zero venues have simply stopped logging in (disengaged) or are logging in but not finding value (product gap).
- **SMS data**: Would show whether AMs are actively reaching out to declining-score venues, or whether the 14-day silence threshold is being breached.
- **restIDs for churn records**: Most churn records this week lack restIDs, making cross-referencing with deal score data name-based only. Data hygiene issue.

### Interview questions that would sharpen the weakest signals

**For double dipping (to AMs and/or RedCat integration team):**
1. "Walk me through what happens when a RedCat-integrated venue has an internal promo running and a customer tries to redeem an EatClub offer on a discounted item. Does the POS block it?"
2. "For the 4 Burpengary venues — were they actually integrated with RedCat, or were they told integration was *available*?"
3. "How many venues currently run internal promotions concurrently with EatClub deals?"

**For integration delays (to engineering / integrations team):**
1. "What is the current integration backlog by POS partner? Which partner(s) are the 11 April-10 venues waiting on?"
2. "What is the average time from sign-up to integration-live, by POS type?"
3. "Is there a timeout policy — i.e., after X days of integration delay, does anything happen automatically?"

**For group churn (to Luke / AMs):**
1. "How many of our active venues are part of multi-venue groups? Do we track group membership in Hub?"
2. "When one venue in a group pauses, is there any alert or flag on sibling venues?"
3. "For Chahoud Group specifically — which competitor is Tom consolidating to, and what does their group offering look like?"

**For Manchester (to Sam Benjamin / BDM team):**
1. "What does the Manchester BDM sign-up flow include for commission education? Is there a written acknowledgement step?"
2. "How many Manchester venues were signed by BDMs who are no longer with the company?"
3. "What ICP criteria were applied to Manchester signings? Was Sushi Doki an exception or a pattern?"

### What would move OKR 1 and OKR 2 most based on this week's signals

**OKR 1 — AM Optimisation:**
The single highest-leverage action is **giving venues a self-serve deal pause/unpause in Partner Portal**. This week's signals show AMs acting as human API endpoints — venues call/email the AM to turn deals off, and when the AM is unavailable (Central Lounge, Second Wife), the venue churns. Every deal toggle that goes through an AM is wasted AM time AND a churn risk.

**OKR 2 — Deal Performance:**
The 284 venues at score = 0 are the biggest opportunity and the biggest risk simultaneously. A system-led action — e.g., Partner Portal surfacing "You have no active deals. Here's what you're missing" with a one-click deal activation — would directly target the OKR 2 metric. But we need Mixpanel data to understand: are these venues not logging in (awareness problem), or logging in and not acting (motivation/UX problem)? This distinction determines whether the intervention is a push notification vs. a Partner Portal redesign.

---

## Routing Block

```routing
{
  "jira_tickets": [
    {
      "theme": "Integration Delay Batch Churn",
      "okr": "OKR 3 (Churn Reduction), OKR 1 (AM Optimisation)",
      "problem_statement": "11 venues paused on April 10 due to integration delays. Venues that sign but cannot integrate churn before activation, wasting BDM acquisition effort, AM onboarding time, and venue goodwill. No automated escalation exists when integration exceeds expected timelines."
    },
    {
      "theme": "Double Dipping — No Item-Level Deal Exclusion",
      "okr": "OKR 3 (Churn Reduction), OKR 2 (Deal Performance)",
      "problem_statement": "Venues running internal promotions cannot prevent EatClub offers from stacking on already-discounted items, resulting in unsustainable double discounts. The stated RedCat integration workaround is not preventing churn. 6+ venues affected this week across 3 regions."
    },
    {
      "theme": "Venue Self-Serve Deal Control (Pause/Unpause/Hours)",
      "okr": "OKR 1 (AM Optimisation), OKR 2 (Deal Performance)",
      "problem_statement": "Venues cannot independently pause, unpause, or adjust deal hours in real time via Partner Portal. AMs are the manual bottleneck for deal state changes. When AMs are unavailable, venues take reputation damage (1-star reviews) and churn. Each AM deal-toggle request is avoidable manual work."
    }
  ],
  "interview_questions": [
    {
      "theme": "Group/Enterprise Churn Cascades",
      "questions": [
        "How many active venues belong to multi-venue groups, and do we track group membership in Hub?",
        "Tom at Chahoud Group — which competitor are they consolidating to, and what does 'consolidate all marketing to one platform' specifically mean?",
        "When one venue in a group pauses or churns, what (if anything) happens to alert AMs about sibling venues?",
        "What would a 'group account' view need to contain to be useful to AMs?"
      ]
    },
    {
      "theme": "284 Venues at Deal Score = 0",
      "questions": [
        "For venues with score = 0, what % have logged into Partner Portal in the last 14 days? (Mixpanel query needed)",
        "Do AMs currently have visibility into which of their venues have score = 0? Is there an alert?",
        "For venues that recovered from score = 0 to active deals, what triggered the recovery — AM outreach, venue self-serve, or system nudge?"
      ]
    },
    {
      "theme": "Manchester Commission Misconception",
      "questions": [
        "Is there a written commission acknowledgement step in the Manchester Arrows onboarding flow?",
        "How many Manchester venues were signed by BDMs who have since left the company?",
        "What ICP screening was applied during the Manchester launch — was Sushi Doki an exception?"
      ]
    }
  ],
  "friction_alerts": [
    {
      "venue": "Raato Ghar",
      "rest_id": "unknown — cross-reference name in Hub",
      "signals": ["Deal score 756 → 0", "Paused for $1k debt", "AM: Nader Masrour"]
    },
    {
      "venue": "ESQ Bar & Dining",
      "rest_id": "unknown — cross-reference name in Hub",
      "signals": ["Deal score 256.25 → 0", "Paused April 9 outstanding invoices", "AM: Elliot Rayment"]
    },
    {
      "venue": "Fress Restaurant & Bar + Khau Galli (linked ownership)",
      "rest_id": "unknown",
      "signals": ["Commission misconception", "Debt refusal", "AM meeting next week — save window open"]
    },
    {
      "venue": "Chahoud Group — 5 Adelaide venues",
      "rest_id": "unknown",
      "signals": ["Spread Deli Glenelg, Dolly Wine Bar, Oliveti, Lune Bar, Spread Deli Unley", "All consolidating to competitor", "Single ops manager decision"]
    },
    {
      "venue": "Central Lounge",
      "rest_id": "unknown",
      "signals": ["Deals ran during internal promo", "Owner furious", "AM communication failure"]
    },
    {
      "venue": "Bricco e Bacco",
      "rest_id": "unknown",
      "signals": ["Integration failure", "Double dipping on set menu", "Booking fees accumulating", "Refund request outstanding"]
    }
  ],
  "watch_list": [
    "Bakmi Lim Noodle Project QV (Melbourne, AM: Jay Franklin) — score 339 → 13",
    "Tradies Cafe & Bar (Canberra, AM: Lukas Symonds) — score 457.5 → 155",
    "Chargrill Charlie's - Annandale (Sydney, AM: Jordan Wellard) — score 292.5 → 6",
    "Burgerlot - Collingwood (Melbourne, AM: Jay Franklin) — score 280 → 0, no churn record",
    "Bean Counter (Adelaide, AM: Gabriella Szabo) — score 268.75 → 0, no churn record",
    "Jay Franklin portfolio — 2 of top-5 score declines this week",
    "Sorrento cluster (Ember, Continental, Cee Cee's) — possible group operator behind integration delay",
    "Mishy's (Sydney) — expressed interest in Offerless product, save opportunity",
    "284 venues total at score = 0 — requires Mixpanel cross-reference to identify pre-churn cohort"
  ]
}
```
