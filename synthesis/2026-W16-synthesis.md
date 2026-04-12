# Crilly Synthesis — 2026-W16 (April 13, 2026)

**Sources available**: Churn CSV (30 historical records), Pause CSV (288 records, 47 from April 2026), Deal Score CSV (4,314 venues, as of 11/04/26)
**Sources unavailable this run**: Slack (8 channels), Granola meeting transcripts, HubSpot, SMS, Mixpanel
**Confidence note**: Running on 2 of 7 signal sources for the second consecutive week. Structured data (churn/pause/deal score) is reliable and high signal-density, but absence of Slack and Granola means in-flight AM conversations, meeting context, and soft escalation signals are invisible. Severity is likely understated. Priority themes identified here are supported by hard behavioural evidence — treat confidence ratings as floor, not ceiling.

---

## 🔥 Rising Themes This Week

### 1. Group/Enterprise Accounts Continue to Cascade-Churn — Platform Has No Group Relationship Layer

**Heat**: 🔴 **HIGH**
**Signal count**: 8 venues, 1 source
**Recurrence**: **CHRONIC** (4+ weeks — Chahoud Group W15, Gemelli Group W15, Sorrento cluster W15, now Ramen Ippudo)
**Lifecycle**: CHRONIC (4+ weeks)
**Problem statement**: When a group operations manager or corporate decision-maker exits the platform, every venue in the group exits simultaneously. This week: Ramen Ippudo — 8 venues across Melbourne and Sydney paused on 02/04/2026 within a 48-hour window. AM note: *"group churn — hiding behind directors decision and I am trying to get through to the discussion maker."* The framing "too full / too busy" is a proxy for a corporate directive that the AM has no visibility into and no escalation path to reach. Combined with W15's Chahoud Group (5 venues, Adelaide) and Gemelli Group (2 venues, Gold Coast), this is now 15+ venues lost in two weeks to the same failure mode: no group-level relationship management, no group-level signal visibility, no early warning when a group begins to disengage.
**Mom Test quality**: **STRONG** — 8 simultaneous closures with near-identical timestamps is observable behaviour, not opinion. AM quote confirms corporate decision-making dynamic, not individual venue feedback.
**OKR**: OKR 3 (Churn Reduction) — primary. A single group churn event is 5-10x the impact of individual venue churn.
**OST branch**: Churn reduction → Product fit for enterprise / Groups
**Journey stage**: Renewal / churn decision point (corporate layer, above venue level)
**Recommended action**: **Escalate to Pan/Luke** — Group churn has now appeared in 4 consecutive weeks with named groups and specific venues. This is not anecdotal. Questions requiring immediate answers: (1) How many active venues are part of multi-venue groups? (2) What % of total churn volume by venue-count comes from group cascades? (3) Does Hub currently identify group/operator relationships at all? (4) Who is the Ramen Ippudo corporate contact — this is a save window that likely closes in days.

---

### 2. POS Integration Gap Is Now a Competitive Disadvantage, Not Just a Product Limitation

**Heat**: 🔴 **HIGH**
**Signal count**: 4 venues, 1 source (2 explicit competitor displacements, 2 integration-blocked churns)
**Recurrence**: **RISING** (3 weeks — integration blocking onboarding in W14/W15, now also enabling competitor wins in W16)
**Lifecycle**: RISING (3 weeks, escalating from delay/friction to active competitive loss)
**Problem statement**: The integration gap is operating on two distinct failure channels this week. Channel 1 — Competitive displacement: Spread Deli (2 venues, Adelaide) explicitly chose First Table over EatClub because First Table integrates with Lightspeed POS + Now Book It reservations, supports preferred offers, and presents as a unified management stack. AM note: *"They want to consolidate all their offers and marketing through one platform… primarily due to integrating with now book it platform and the ability to run preferred offers."* EatClub's walk-in-only positioning was not sufficient. Channel 2 — Operational deadlock: Life of Chi (Sydney) churned because they use Ipos, for which EatClub has no integration, meaning they cannot run lunch deals without double-dipping risk. AM note: *"Venue uses Ipos so no integration possible at this stage… Owner is still adamant he won't be coming back onto the platform as the venue is too busy in the evenings and no lunch deals available until an integration is possible."* These are distinct failure modes but share a root: EatClub's integration surface area is insufficient for the POS diversity of its venue base and the integration depth of its competitors.
**Mom Test quality**: **STRONG** — Spread Deli is a specific competitive loss with a named competitor and a stated reason. Life of Chi is a documented AM escalation that failed to resolve due to a confirmed product gap.
**OKR**: OKR 3 (Churn Reduction) — direct. OKR 2 (Deal Performance) — venues that can't integrate safely won't run deals confidently.
**OST branch**: Churn reduction → Friction in core venue experience; Churn reduction → Onboarding journey quality
**Journey stage**: Spread Deli: Renewal / churn decision. Life of Chi: Ongoing engagement → Churn decision.
**Recommended action**: **Discovery ticket + Engineering escalation** — (1) Which POS systems are in the active venue base — what % are on Lightspeed, Ipos, and other non-integrated systems? (2) What is the revenue impact of venues that can't safely run deals due to integration gaps? (3) What does First Table's Lightspeed integration actually do — is it item-level exclusions, time-based deal visibility, or something else? (4) Prioritise Ipos integration — this is an explicit unlock for Life of Chi and likely a class of Sydney/Melbourne inner-suburb venues.

---

### 3. Silent Portfolio Disengagement Is Accelerating — 397 Venues at Zero Deal Score

**Heat**: 🔴 **HIGH**
**Signal count**: 397 venues (deal score = 0), 1 source
**Recurrence**: **RISING** (W15: 284 venues at zero. W16: 397 venues at zero. +113 venues in one week.)
**Lifecycle**: RISING (2 weeks, volume increasing at pace)
**Problem statement**: The number of venues with deal score = 0 has increased by 113 in one week (284 → 397). Deal score = 0 means no active deals — which is the platform's primary churn predictor. These venues are silent: they haven't churned, they haven't complained, they haven't made contact. They are simply not running deals. AMs may not know. The system is not acting. These 397 venues are in a pre-churn holding pattern that will likely convert to active churn within 2-4 weeks without intervention. AM concentration in the highest-risk cohort: Tom Mcgay (28 zero-score venues), Elodie Fitzsimmons (22), Aaron Pantazis (18), Gabriella Szabo (17), Elliot Rayment (17). Additionally: venues with the steepest single-week score declines include Tradies Cafe & Bar (Canberra, Lukas Symonds: −302 pts), Say Cheeese West End (Brisbane, Matthew Behan: −470 pts), Bean Counter (Adelaide, Gabriella Szabo: score → 0).
**Mom Test quality**: **STRONG** (behavioural) — Score = 0 is observable fact, not opinion. The +113 week-on-week increase is directional data that demands action.
**OKR**: OKR 2 (Deal Performance) — primary. OKR 3 (Churn Reduction) — direct downstream consequence.
**OST branch**: Deal performance → Venue-led revenue actions; Deal performance → Deal score visibility and trust; AM optimisation → System automation opportunities
**Journey stage**: Ongoing engagement (declining) → Pre-churn
**Recommended action**: **Escalate to Luke + Discovery ticket** — (1) Does Billie or Hub surface an alert when a venue's deal score hits zero? If not, this is a straightforward automation win for OKR 1. (2) What is the conversion rate from deal score = 0 to confirmed churn — what's the typical lag? (3) Tom Mcgay has 28 zero-score accounts — is this a capacity issue, a portfolio quality issue, or a regional market signal? Needs immediate portfolio review. (4) Should there be a system-triggered "re-engagement nudge" to venues when score approaches zero?

---

### 4. Financial Distress Is Multi-Layered — Debt, Insolvency, and an AI Feature Creating Traps

**Heat**: 🔴 **HIGH**
**Signal count**: 5 distinct venues/situations, 1 source
**Recurrence**: **RISING** (debt signals chronic, but insolvency detection failure and AI-generated financial trap are new acute signals this week)
**Lifecycle**: RISING (3 weeks debt signals, but two new signal types elevate urgency)
**Problem statement**: Three distinct financial distress patterns visible this week:

**Pattern A — Uncollectable high-value debt**: Rashays Top Ryde (Sydney), managed by Luke Maurel/Elliot Rayment, carries >$50,000 outstanding. AM note: *"called head of franchise today and have been chasing their accounts payable team with no response."* High-value franchise account with no collections resolution path.

**Pattern B — Undetected operator insolvency**: Cony's (Sydney) + sister venue Nikkia entered voluntary administration (confirmed 08/04/2026). EatClub had no early-warning system for operator financial health. This is not a product UX failure — it's a risk screening gap that, when it hits a multi-venue operator, takes multiple accounts offline simultaneously with no recovery path.

**Pattern C — AI deal generator creating financial traps**: Silver Fox Cafe (Sydney), AM: Jordan Wellard. AM note: *"Owner had set a revenue goal and turned on the AI deal generator and deals are too high."* The owner used a product feature (AI deal generator) in good faith to optimise revenue, the feature set discounts too aggressively, and now the venue cannot pay its outstanding balance. A product designed to help a venue has created a debt situation. This is a NEW and alarming signal type — it implies the AI deal generator lacks guardrails that would prevent it from setting deals beyond a venue's margin threshold.

**Mom Test quality**: **STRONG** — All three patterns are specific past events with named venues, confirmed debts, and documented AM notes. Not hypothetical.
**OKR**: OKR 3 (Churn Reduction) — all three patterns are direct churn drivers.
**OST branch**: Churn reduction → Friction in core venue experience (Pattern C); churn reduction → Product fit for enterprise/Groups (Patterns A & B)
**Journey stage**: Pattern A: AM relationship (ongoing debt); Pattern B: Renewal / churn decision; Pattern C: Ongoing engagement → Churn (product-caused)
**Recommended action**: **Discovery ticket (Pattern C — highest urgency for product team)** — The AI deal generator issue is the most actionable product problem here. (1) What constraints does the AI deal generator apply when setting discount levels? Does it have access to venue margin data? (2) Can the feature generate deals that create an unpayable debt situation? (3) Is there a review/confirm step before AI-generated deals go live? Patterns A & B require non-product escalation: collections escalation for Rashays, risk assessment protocol for multi-venue operators.

---

### 5. Venues Cannot Prevent Double Dipping — Chronic, Still Unresolved, Now Driving Competitor Wins

**Heat**: 🟡 **MEDIUM-HIGH**
**Signal count**: 4 venues, 1 source
**Recurrence**: **CHRONIC** (5+ weeks — appeared in W13, W14, W15, W16)
**Lifecycle**: CHRONIC (5+ weeks)
**Problem statement**: Venues running their own promotions (lunch specials, happy hours) have no reliable mechanism to prevent EatClub offers from being redeemed on top of their discounted items. This week's signals: Burpengary cluster (Little Lamb, Dawg Boys) — both flagging double dipping, both told "we integrate with RedCat" (which did not save the W15 Burpengary venues from churning). Life of Chi — double dipping is the direct reason they cannot run lunch deals and have now churned. Spread Deli — explicitly cited First Table's ability to support "preferred offers" as part of their decision to leave, implying deal-control flexibility is a competitive factor. This theme is now in its fifth consecutive week. The RedCat integration talking point is being deployed by AMs but is not resolving the problem for venues that aren't on RedCat, and even for those that are, it appears the capability is either not being activated or not sufficient.
**Mom Test quality**: **STRONG** — Life of Chi's churn is directly traceable to this problem. Spread Deli's competitor choice explicitly references offer control. Both are specific past events with documented AM notes.
**OKR**: OKR 3 (Churn Reduction) — direct. OKR 2 (Deal Performance) — venues unwilling to run deals because of double-dipping risk.
**OST branch**: Churn reduction → Friction in core venue experience; Deal performance → Venue-led revenue actions
**Journey stage**: Ongoing engagement → Churn decision (recurring friction)
**Recommended action**: **Interview + Discovery ticket** — This is CHRONIC and has now enabled at least one confirmed competitor win. (1) What does the RedCat integration actually do re: item-level exclusions — does it solve this problem or just get mentioned? (2) For venues *not* on RedCat, what is the product-level solution? (3) Can venues currently exclude specific item categories from EatClub offers in Partner Portal? If not, this is the gap. Interview Dawg Boys / Little Lamb Burpengary — still active, specific experience available.

---

## 📋 All Signals This Week — Classified

| # | Signal Summary | Source | Author Team | Who Affected | Mom Test | OKR | Theme | OST Branch |
|---|---------------|--------|------------|--------------|---------|-----|-------|------------|
| 1 | Ramen Ippudo 8 venues paused 02/04 — "directors decision," AM can't reach decision-maker | Pause CSV | AM (Elliot Rayment) | 8 venues (Melb/Syd) | STRONG | OKR 3 | Group Cascade Churn | Enterprise/Groups |
| 2 | Spread Deli 2 venues — moved to First Table (Lightspeed integration + preferred offers) | Pause CSV | AM (Gabriella Szabo) | 2 venues (Adelaide) | STRONG | OKR 3, OKR 2 | POS Integration Gap + Competitor Displacement | Core experience friction |
| 3 | Life of Chi (Syd) — Ipos no integration, can't run lunch deals, churned after escalation failed | Pause CSV | AM (Elliot Rayment) | 1 venue | STRONG | OKR 3 | POS Integration Gap | Onboarding quality / Core friction |
| 4 | 397 venues at deal score = 0 (vs 284 last week, +113) | Deal Score CSV | System | 397 venues | STRONG (behavioural) | OKR 2, OKR 3 | Silent Disengagement | Deal performance + Churn |
| 5 | Tom Mcgay — 28 zero-score venues (highest AM concentration) | Deal Score CSV | System | 28 venues (Melb) | STRONG (behavioural) | OKR 1, OKR 3 | AM Capacity / Portfolio Risk | Manual AM task reduction |
| 6 | Say Cheeese West End (Bris) — score dropped −470 pts this month | Deal Score CSV | System | 1 venue (Matthew Behan) | STRONG | OKR 2, OKR 3 | Score Collapse | Deal performance |
| 7 | Tradies Cafe & Bar (Cbr) — score dropped −302 pts, still active | Deal Score CSV | System | 1 venue (Lukas Symonds) | STRONG | OKR 2, OKR 3 | Score Collapse | Deal performance |
| 8 | Rashays Top Ryde (Syd) — $50k+ debt, franchise accounts payable unresponsive | Pause CSV | AM (Luke/Elliot) | 1 venue | STRONG | OKR 3 | High-Value Debt Escalation | Financial friction |
| 9 | Cony's + Nikkia (Syd) — operator entered voluntary administration, no prior warning signal | Pause CSV | AM (Jasmine Jung) | 2 venues | STRONG | OKR 3 | Undetected Insolvency | Financial screening |
| 10 | Silver Fox Cafe (Syd) — AI deal generator set deals too high, venue now in debt | Pause CSV | AM (Jordan Wellard) | 1 venue | STRONG | OKR 3, OKR 2 | AI Feature Trap | Core experience friction |
| 11 | Frankie & George (Bris) — 6+ months unresponsive, menu wrong, AM: "never had a response" | Pause CSV | AM (Jessie Helyar) | 1 venue | STRONG | OKR 1, OKR 3 | Unreachable Venue / Profile Decay | AM relationship |
| 12 | Seoul Sweetie + Busan Baby (Adel) — CS signalled churn intent but AM not notified | Pause CSV | CS→AM gap | 2 venues (Gabriella Szabo) | STRONG | OKR 1, OKR 3 | CS-AM Coordination Failure | Manual AM task reduction |
| 13 | Little Lamb + Dawg Boys (Burpengary) — double dipping, told "we integrate with RedCat" | Pause CSV | AM (Mark Savaille) | 2 venues | STRONG | OKR 3, OKR 2 | Double Dipping | Core experience friction |
| 14 | Penang Chinese Cuisine (Sunshine Coast) — 6 tables, owner trusting staff not portal, 0 customers | Pause CSV | AM (Lukas Symonds) | 1 venue | STRONG | OKR 2, OKR 3 | Low Digital Literacy / Partner Portal Adoption | Deal performance |
| 15 | Doitao Thai Hunters Hill — $3.5k/month revenue from EC, still unconvinced of value | Pause CSV | AM | 1 venue | MEDIUM | OKR 2 | Value Perception Gap | Deal score visibility and trust |
| 16 | Newmarket Hotel Port Adelaide — $935 zero-balance, new portfolio start 12/04 | Deal Score CSV | System | 1 venue (Elodie Fitzsimmons) | STRONG | OKR 2 | New Venue Zero Score | Deal performance |
| 17 | Ab's Street Bites (Melb) — score −247 pts (319 → 72) | Deal Score CSV | System | 1 venue (Brianna Quinn) | STRONG | OKR 2 | Score Decline | Deal performance |
| 18 | Biryani Place Springwood (Bris) — score −192 pts (314 → 121) | Deal Score CSV | System | 1 venue (Jessie Helyar) | STRONG | OKR 2 | Score Decline | Deal performance |

---

## 🗺️ OST Update

### AM Optimisation (OKR 1)

| Sub-branch | Status | This Week's Evidence |
|-----------|--------|---------------------|
| **Manual AM task reduction** | 🔺 Strengthened | CS-AM coordination failure (Seoul Sweetie/Busan Baby) means AMs are receiving venue churn signals late or not at all. 6+ months of AM outreach to Frankie & George with zero response — no system intervention triggered. Both are AM time costs the system should be handling. |
| **Venue self-serve capability** | ⚠️ Partially weakened | Silver Fox AI deal generator issue raises a concern: if self-serve tools can generate financial traps, the case for *more* self-serve requires guardrails discussion. Penang Chinese — owner won't use Partner Portal, trusts staff. Digital literacy gap limits self-serve potential for a segment of the venue base. |
| **System automation opportunities** | 🔺 Strengthened | 397 venues at zero deal score with no system-triggered intervention. Tom Mcgay's 28 zero-score accounts suggest no automation is flagging AM portfolio overload. CS-AM handoff is manual and failing. All three are automation opportunities. |

### Deal Performance (OKR 2)

| Sub-branch | Status | This Week's Evidence |
|-----------|--------|---------------------|
| **Partner Portal engagement** | ⚠️ Unknown — no Mixpanel data | Can't assess. Second consecutive week without Mixpanel. Penang Chinese confirms at least some owners are not using Partner Portal. |
| **Venue-led revenue actions** | 🔻 Weakening | Zero deal score up from 284 → 397 (+113 in one week). Venues are moving away from deal activity at pace. Doitao Thai has $3.5k/month revenue from EatClub and still doesn't perceive value — suggests the value isn't being surfaced by the platform itself. |
| **Deal score visibility and trust** | 🔺 Newly flagged concern | Silver Fox: venue owner used AI deal generator "to set a revenue goal" — suggesting they don't understand how deal scores or deal economics work. Penang Chinese: owner counting footfall from memory, not checking portal. Deal score is not understood by venue owners as a decision-making tool. |

### Churn Reduction (OKR 3)

| Sub-branch | Status | This Week's Evidence |
|-----------|--------|---------------------|
| **Friction in core venue experience** | 🔺 Strengthened | Double dipping (chronic, now linked to competitor win). AI deal generator trap (new — product-caused friction). Life of Chi deadlock (POS gap = complete product-market misfit). |
| **Product fit for enterprise / Groups** | 🔺🔺 Significantly strengthened | Ramen Ippudo (8 venues) adds to Chahoud/Gemelli cascade pattern from W15. Now 15+ venues in 2 weeks from group churn. No group relationship layer visible in any product surface. |
| **Onboarding journey quality** | 🔺 Strengthened | Spread Deli churn was post-sign — the venue went live and then left. Integration mismatch should be screened at sign-up (what POS do you use? do you run concurrent promotions?). Life of Chi's Ipos situation should have been caught before they ever went live. |
| **Surfacing product value through data** | 🔺 Newly strengthened | Doitao Thai case — $3.5k/month in EatClub revenue, AM knows this, venue owner doesn't. The data exists but isn't surfaced in a way the venue owner absorbs. Penang Chinese — owner trusting staff hearsay over transaction data. Both suggest Partner Portal is failing to communicate value to the owner layer. |

---

## ⚠️ Friction Stack Watch

Venues showing compounding signals across 2+ sources or 2+ journey stages. **Flag to Luke immediately.**

### CRITICAL — Active multi-source confirmation

| Venue | restID | Signals | Sources | Friction Stack |
|-------|--------|---------|---------|---------------|
| **Ramen Ippudo group (8 venues)** | Multiple | 8 simultaneous pauses + group corporate decision in progress + AM escalation stalled | Pause CSV (AM note) | Group cascade churn in motion. Corporate layer inaccessible to AM. Save window closing. Flag to Pan/Luke immediately — this requires executive-level outreach to Ippudo corporate, not AM-level retention. |
| **Rashays Top Ryde** | — | $50k+ debt + franchise accounts payable unresponsive + Luke Maurel involved (escalated to Head of AM) | Pause CSV | Financial dispute at franchise level. Head of AM already engaged. Needs legal/collections escalation path, not AM action. |
| **Cony's + Nikkia (Sydney)** | — | Voluntary administration confirmed + multi-venue operator + no prior warning signal in data | Pause CSV | Insolvency hit with zero product-side warning. Two venues lost. Risk: are other venues in this operator's group affected? |

### HIGH RISK — Single source, multi-stage friction

| Venue | restID | Signals | Friction Stack |
|-------|--------|---------|---------------|
| **Silver Fox Cafe (Sydney)** | — | AI deal generator → debt → pause | Product-caused friction (tool created debt) → Financial distress → churn risk. AM: Jordan Wellard. Immediate question: can the debt be forgiven given it was system-generated? This creates a precedent conversation. |
| **Life of Chi (Sydney)** | — | Ipos integration unavailable → double dipping → refused contact → churned → escalation to Sean failed | Onboarding mismatch (wrong POS) → Ongoing friction → AM relationship failure → Confirmed churn. Already lost. Flag as case study for integration screening pre-sign. |
| **Spread Deli — Glenelg + Unley (Adelaide)** | — | Competitor pitch → Lightspeed integration advantage → preferred offers gap → confirmed exit to First Table | Competitive loss confirmed. 2 venues. Now lost. Flag to Sam Benjamin — competitor intelligence on First Table's integration stack. |
| **Frankie & George (Brisbane)** | — | 6+ months unresponsive + menu/profile decay + AM escalating for help | AM relationship breakdown → Profile decay (incorrect menu live) → approaching silent churn. AM: Jessie Helyar. Needs in-venue visit or admin escalation. |

### WATCH — Score collapse, no churn record yet (pre-churn candidates)

| Venue | AM | Score Change | Note |
|-------|-----|-------------|------|
| Say Cheeese - West End (Bris) | Matthew Behan | −470 pts this month | Largest single-week decline in portfolio |
| Tradies Cafe & Bar (Cbr) | Lukas Symonds | −302 pts | Flagged in W15 watch list — now declining further |
| Bean Counter (Adelaide) | Gabriella Szabo | → 0 | Adelaide market softness pattern |
| Ab's Street Bites (Melb) | Brianna Quinn | −247 pts (319 → 72) | Approaching zero |
| Biryani Place Springwood (Bris) | Jessie Helyar | −192 pts (314 → 121) | Declining |

**Tom Mcgay portfolio alert**: 28 zero-score venues in a single AM's book is anomalous. Either portfolio is overloaded (capacity), the Melbourne market segment he covers is soft, or there's been a period of low AM engagement. Needs a portfolio health review with Luke.

---

## 💡 Synthesis Notes

**What surprised me:**

The AI deal generator trap (Silver Fox Cafe) is a new signal category that hasn't appeared before. A venue owner using a product feature in good faith — setting a revenue goal, turning on the AI generator — and ending up in debt is a fundamentally different problem from the usual "venue doesn't understand the pricing model." This one is product-caused. If the AI deal generator can produce deals that leave a venue unable to pay, it needs guardrails before it gets deployed to more venues. Worth understanding: how many venues have the AI deal generator enabled? Are there others in the same situation who haven't surfaced yet?

**What is missing:**

Without Slack and Granola, this synthesis has no visibility into: (1) what AMs are saying to each other about the Ramen Ippudo situation — is there a save plan being discussed? (2) Whether Luke or Pan have had any discussions this week about the deal score trend — the 397 zero-score venues is a number that should be alarming at leadership level. (3) Any HubSpot ticket patterns that would confirm or extend the double-dipping / integration signals in the churn data.

For the third consecutive week, the absence of Slack and Granola is the primary confidence limiter. The structured CSVs are high-signal but only capture confirmed events — they miss in-progress conversations, soft escalations, and AM sentiment.

**What would sharpen the weakest signals:**

- *AI deal generator trap* (WEAK causal understanding): Interview Jordan Wellard and the Silver Fox owner. What exactly happened? What did the AI set the discount to? Did the venue have visibility into the deal before it went live?
- *Doitao Thai value perception gap*: Interview the owner. $3.5k/month in EatClub revenue and still unconvinced — what does "convinced" look like to them? What data would change their view?
- *Penang Chinese digital literacy gap*: Is this one owner or a class of owners? How many venues in the base are 55+, single-location, non-digital-native?

**What would move OKR 1 or OKR 2 most based on this week's signals:**

OKR 1 (AM Efficiency): The highest-leverage single action is a system alert when a venue's deal score hits zero — so AMs don't have to manually monitor 400 at-risk venues. This is a small build with an immediate addressable impact of 397 venues currently unmonitored.

OKR 2 (Deal Performance): The Doitao Thai signal points to a value communication gap: the venue's EatClub revenue is a data point the AM knows but the venue doesn't feel. If Partner Portal surfaced "EatClub has driven $X in revenue for you this month" prominently, it would give venue owners a reason to stay engaged without AM prompting. The 397 zero-score venues likely include many who have simply forgotten the platform exists.

---

```routing
{
  "jira_tickets": [
    {
      "theme": "AI Deal Generator Lacks Guardrails",
      "okr": "OKR 3",
      "problem_statement": "The AI deal generator can produce discount levels that leave venues unable to pay their outstanding balance. Silver Fox Cafe (Sydney) is a confirmed case — owner used the feature in good faith to set a revenue goal and ended up in debt. No evidence of safeguards that prevent AI-generated deals from exceeding venue margin thresholds."
    },
    {
      "theme": "Zero Deal Score Has No System-Triggered AM Alert",
      "okr": "OKR 1 + OKR 3",
      "problem_statement": "397 venues currently have deal score = 0 (up from 284 last week) with no automated escalation to the assigned AM. Deal score = 0 is the platform's strongest churn predictor. AMs are not alerted; venues receive no system-led re-engagement. This is a direct OKR 1 automation opportunity and OKR 3 churn risk."
    },
    {
      "theme": "Group/Operator Relationship Layer Missing in Hub and Partner Portal",
      "okr": "OKR 3",
      "problem_statement": "When a multi-venue operator makes a corporate decision to exit, every venue in the group churns simultaneously and EatClub has no early warning system. 15+ venues lost in 2 weeks (Ramen Ippudo 8, Chahoud Group 5, Gemelli 2) to this failure mode. Hub does not identify group/operator relationships; there is no group-level engagement signal."
    }
  ],
  "interview_questions": [
    {
      "theme": "AI Deal Generator Trap (Silver Fox)",
      "questions": [
        "Walk me through exactly what happened — when you turned on the AI deal generator, what did it set the discount to, and how did you find out there was a problem?",
        "Was there a step where you confirmed or approved the deal before it went live?",
        "What would you have expected the feature to do differently?"
      ]
    },
    {
      "theme": "Value Perception Gap (Doitao Thai)",
      "questions": [
        "You've been driving around $3,500/month in revenue through EatClub — what does success look like to you that isn't happening?",
        "When you think about whether EatClub is worth it, what data do you look at?",
        "Is there a number or outcome that would make you feel confident it's working?"
      ]
    },
    {
      "theme": "Competitor Displacement via Integration Stack (Spread Deli)",
      "questions": [
        "When First Table presented their Lightspeed and Now Book It integration, what problem did that solve for you that EatClub wasn't solving?",
        "What does 'preferred offers' mean in practice for how your team manages the deals day-to-day?",
        "If EatClub had that same integration, would you have stayed?"
      ]
    }
  ],
  "friction_alerts": [
    {
      "venue": "Ramen Ippudo (8 venues — Melbourne + Sydney)",
      "rest_id": "Multiple — see pause CSV 02/04/2026",
      "signals": ["8-venue simultaneous pause", "Group corporate directive", "AM escalation stalled", "Save window closing"]
    },
    {
      "venue": "Rashays Top Ryde",
      "rest_id": "Unknown",
      "signals": ["$50,000+ outstanding debt", "Franchise accounts payable unresponsive", "Luke Maurel escalated"]
    },
    {
      "venue": "Silver Fox Cafe (Sydney)",
      "rest_id": "Unknown",
      "signals": ["AI deal generator created unpayable debt", "Paused", "Debt forgiveness question open"]
    },
    {
      "venue": "Frankie & George (Brisbane)",
      "rest_id": "Unknown",
      "signals": ["6+ months unresponsive", "Wrong menu live on profile", "AM Jessie Helyar requesting help"]
    }
  ],
  "watch_list": [
    "Tom Mcgay portfolio — 28 zero-score accounts (capacity or market signal?)",
    "Say Cheeese West End (Bris) — largest score decline this month (−470 pts)",
    "Tradies Cafe & Bar (Cbr) — was on W15 watch list, continuing to decline",
    "Bean Counter (Adelaide) — score → 0, Adelaide market softness pattern",
    "Manchester market — W15 showed 9 early churns from commission misconception, not confirmed resolved",
    "Burpengary micro-cluster (Bris) — double dipping complaints continuing, Mark Savaille territory",
    "Spread Deli competitive loss — intelligence needed on First Table Lightspeed integration depth",
    "Cony's/Nikkia voluntary administration — confirm no other venues in operator group"
  ]
}
```
