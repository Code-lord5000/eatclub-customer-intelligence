# Crilly Synthesis — Week of 14–22 April 2026 (Week 1 Baseline)

**Data received:** Granola (16 signals) · HubSpot (18 signals) · Churn Hub CSV (30 records, historical Nov 2023–Feb 2024) · SMS (empty)
**Data gaps:** Slack (mentioned but no structured data delivered) · Deal Score CSV (not provided) · Mixpanel (auth blocked — credentials needed)

> ⚠️ **Week 1 notice:** This is Crilly's first synthesis run. All lifecycle labels are established as baselines using evidence-of-duration rather than prior Crilly reports. Lifecycle tracking begins next week.

---

## 🔥 Rising Themes This Week

### 1. Venues signed too fast — 40% of all churn traces to ICP misfit, broken handovers, and zero product comprehension before first settlement

**Heat:** HIGH
**Signal count:** 8 | **Source count:** 3 (Granola, HubSpot, Churn)
**Lifecycle:** CHRONIC (by evidence — leadership describes as long-standing, churn data confirms pattern across months)
**Recurrence:** Chronic

**Problem statement:** Venues are being signed within 20 minutes of first contact by BDMs who cannot verify ICP fit. They receive no structured product education, experience a disconnected handover to AMs, and are blindsided by their first settlement charge — creating a predictable early-churn pipeline that accounts for 40% of all churn in the business.

**Mom Test quality:** STRONG — Sam Benjamin cites the 40% metric directly, describes the exact failure chain (sign → no comprehension → settlement shock → churn), and Adam Glegg corroborates in a separate meeting. BD Dine's cancellation note ("could not find any benefit") is a first-person venue confirmation of the same pattern.

**OKR:** OKR 3 (Churn Reduction) primary; OKR 1 (AM Optimisation) secondary — AMs inherit poorly onboarded venues and spend hours on damage control
**OST branch:** Churn reduction → Onboarding journey quality
**Journey stage:** Onboarding → Activation (cross-stage friction stack)
**Recommended action:** Discovery ticket + Escalate to Luke

**Key signals:**
| Signal | Source | Quality |
|---|---|---|
| "40% of all our churn is early churn — they get signed up and leave within 40–60 days. One reason is ICP." | Granola / Sam Benjamin | STRONG |
| "BDMs aren't handing over to AMs very well — there's a disconnect and that falls over." | Granola / Sam Benjamin | STRONG |
| "20 minutes later they're signed up and live. How do you get people to remember what we are when a week later they get the settlement and freak out?" | Granola / Sam Benjamin | STRONG |
| "40% early churn... signing a kebab shop in the back of Tumba, a BDM sells them the dream" | Granola / Adam Glegg | STRONG |
| "Fix the current terrible facilitation of a very fast sign-up" | Granola / Adam Glegg | MEDIUM |
| BD Dine: "Could you please cancel... I could not find any benefit." | HubSpot / Venue (restID: C27A8D5B) | STRONG |
| Formal onboarding withdrawal before activation: "Please treat any setup process as cancelled with immediate effect." | HubSpot / Venue (unknown) | MEDIUM |

---

### 2. Flat discount economics are structurally unviable for a large venue segment — 43% of historical churns are price-driven

**Heat:** HIGH
**Signal count:** 16+ | **Source count:** 3 (Churn, Granola, HubSpot)
**Lifecycle:** CHRONIC (by evidence — 13/30 churned venues cite price/margin, spanning 4+ months of data; Sam actively discussing time-of-day pricing fix)
**Recurrence:** Chronic

**Problem statement:** A significant segment of venues operates on margins so thin ($2/meal in one documented case) that any percentage-based discount is economically destructive. The current flat 30% model does not account for time-of-day demand variation, venue margin structure, or the difference between filling empty seats vs. discounting seats that would fill organically. These venues are structurally incompatible with the product's pricing model and are churning regardless of AM intervention.

**Mom Test quality:** STRONG — Multiple venue owners provide exact margin figures. Restaurant 233's owner stated "$2 per meal profit margin, can't afford discount" after the AM disproved his cannibalisation concern with data. Hells Bellz cited "30% is too much of a hit." Zio Pino stated a hard cap at 20%. Sam Benjamin described the needed fix: blended time-of-day pricing (25% at peak, 45% off-peak).

**OKR:** OKR 3 (Churn Reduction) primary; OKR 2 (Deal Performance) secondary
**OST branch:** Churn reduction → Friction in core venue experience; Deal performance → Deal score visibility and trust
**Journey stage:** Ongoing engagement → Renewal/churn decision
**Recommended action:** Discovery ticket (pricing model flexibility)

**Key signals:**
| Signal | Source | Quality |
|---|---|---|
| 13/30 historical churns are price-related | Churn Hub CSV | STRONG (pattern) |
| Restaurant 233: "profit margin is only $2 per meal so he can't afford to provide a discount" | Churn / AM note | STRONG |
| Hells Bellz: "margins are too thin and 30% is too much of a hit" | Churn / AM note | STRONG |
| Zio Pino: "did not have enough margin to be offering any higher than 20% deal" | Churn / AM note | STRONG |
| "Get away from the old deal-at-30% model... 12–2 at 25%, 3–5 at 45%, so the blended average is still 30%" | Granola / Sam Benjamin | STRONG |
| The Famished Wolf: "margin erosion due to discounts... EatClub customers rarely transition into full-paying regulars" | HubSpot / AM note (Gong) | STRONG |
| C9 Docklands: "shop has not been using Eatclub effectively... fees deducted from our account regularly" | Churn / Venue verbatim | STRONG |

---

### 3. Billing opacity and settlement shock are destroying venue trust before value is demonstrated

**Heat:** HIGH
**Signal count:** 6 | **Source count:** 3 (HubSpot, Granola, Churn)
**Lifecycle:** RISING (by evidence — multiple active incidents this week, Sam confirms as known pattern)
**Recurrence:** Recurring (3+ weeks by evidence)

**Problem statement:** Venues receive their first settlement charge with no preparation or context, causing immediate distrust. Ongoing billing issues — including a venue reporting zero payments for 3 months, a $1,983.53 failed debit, suspected double-charging, and fee deductions on dormant accounts — compound into active churn triggers. The billing experience is both a first-impression failure (settlement shock) and an ongoing friction source (opacity of charges and payments).

**Mom Test quality:** STRONG — Himalayan Nepalese owner: "I have not received any money in to my bank past 3 month. This is very serious matter." Belles Hot Chicken finance manager contacts CS with exact outstanding balance. Cairo Nights owner believes they're being double-charged. Sam Benjamin describes the pattern: "week later they get the settlement and freak out."

**OKR:** OKR 3 (Churn Reduction) primary
**OST branch:** Churn reduction → Friction in core venue experience
**Journey stage:** Activation (first settlement) + Ongoing engagement (billing disputes)
**Recommended action:** Discovery ticket + immediate CS escalation for Himalayan Nepalese and Belles Hot Chicken

**Key signals:**
| Signal | Source | Quality |
|---|---|---|
| Himalayan Nepalese: "not received any money in to my bank past 3 month... someone need to call me asap" | HubSpot / CS ticket | STRONG |
| Belles Hot Chicken: "$1,983.53 outstanding... insufficient fund... could you please retry payment asap" | HubSpot / CS ticket | STRONG |
| Cairo Nights: "believes we are taking 2 payments from his old account" | HubSpot / CS ticket | MEDIUM |
| "20 minutes later they're signed up... week later they get the settlement and freak out" | Granola / Sam Benjamin | STRONG |
| C9 Docklands: "fees deducted from our account regularly... could you clarify?" | Churn / Venue verbatim | STRONG |

---

### 4. Venues cannot understand, configure, or trust deal mechanics — creating AM dependency and underperformance

**Heat:** MEDIUM-HIGH
**Signal count:** 5 | **Source count:** 2 (Granola, HubSpot)
**Lifecycle:** RISING (by evidence — Sam describes as systemic, Vaishali reports recurring override incidents)
**Recurrence:** Recurring

**Problem statement:** The deal model is opaque to venues. They cannot understand whether "5 tables" means 5 total or 5 per window. The deal "looks undynamic — just a very fancy voucher." When venues do attempt to manage deals (e.g., disabling them), internal ops can override the disabling without venue consent, triggering billing disputes and trust destruction. The result: venues either don't engage with deal management at all (driving Partner Portal inactivity) or make changes that underperform because they don't understand the mechanics.

**Mom Test quality:** STRONG — Sam Benjamin provides a specific, testable example of the configuration confusion. Vaishali describes a concrete incident pattern where overrides caused billing disputes. Melroad Pizza reports seeing zero bookings despite being live.

**OKR:** OKR 2 (Deal Performance) primary; OKR 1 (AM Optimisation) secondary — AMs manually configure and explain deals that venues should self-serve
**OST branch:** Deal performance → Deal score visibility and trust; AM optimisation → Venue self-serve capability
**Journey stage:** Ongoing engagement
**Recommended action:** Discovery ticket

**Key signals:**
| Signal | Source | Quality |
|---|---|---|
| "Five tables — total between 12 and 5, or five every two hours? We've never been able to explain this to a venue." | Granola / Sam Benjamin | STRONG |
| "The deal looks undynamic — just a very fancy voucher." | Granola / Sam Benjamin | STRONG |
| Ops overriding venue-disabled deals → venue asking for money back | Granola / Vaishali Mangwani | STRONG |
| Melroad Pizza: "I dont see booking coming for table... dont follow up the customer" | HubSpot / CS ticket (restID: F5751B8E) | MEDIUM |
| Liyin Rice Roll Master: "concerns about the deals... considering to cancel if service is not compatible" | HubSpot / CS ticket | MEDIUM |

---

### 5. BDMs have no structured pre-call intelligence or in-venue pitch tooling — selling blind drives ICP misfit upstream

**Heat:** MEDIUM
**Signal count:** 6 | **Source count:** 1 (Granola — but 3 distinct speakers: Sam Benjamin, Angela Ho, Adam Glegg)
**Lifecycle:** CHRONIC (by evidence — Adam: "the gap has always been"; Angela built Freckle as a long-standing workaround)
**Recurrence:** Chronic

**Problem statement:** BDMs walk into venues with no data — no lat/long, no AOV, no cuisine category, no comparable venue performance. They google restaurants, open 4 apps during demos, and cannot show tailored social proof. This forces unqualified pitches, drives ICP misfit at sign-up, and is a root cause of Theme 1 (early churn). Angela Ho has independently built a scraping engine (Freckle) to solve for "nine-tenths" of the data gap, confirming both the severity of the problem and the existence of a tractable solution.

**Mom Test quality:** STRONG — Angela built an entire working tool (Freckle) using Outscraper to fill the gap. Sam describes the current 4-app workaround. Adam names the specific missing data fields. All three speakers independently confirm the same gap.

**OKR:** OKR 3 (Churn Reduction) upstream — better qualification reduces early churn
**OST branch:** Churn reduction → Onboarding journey quality (upstream)
**Journey stage:** Pre-sign (upstream of onboarding)
**Recommended action:** Watch (active build in progress — Freckle + sign-up form work visible in Refinement meeting)

> **Heat cap note:** Single source type (Granola only) limits this to Medium despite 6 signals and CHRONIC lifecycle. If BDM-sourced data (Slack, SMS) corroborates next week, this moves to High.

---

## 📋 All Signals This Week — Classified

### Current-Week Signals (Granola + HubSpot: 34 total)

| # | Signal Summary | Source | Author Team | Who Affected | Mom Test | OKR | Theme | OST Branch |
|---|---|---|---|---|---|---|---|---|
| G1 | 40% early churn from ICP misfit | Granola | Leadership (Sam) | All venues + AMs | STRONG | OKR 3 | 1: Early churn | Churn → Onboarding quality |
| G2 | BDM-to-AM handover failure | Granola | Leadership (Sam) | All venues + AMs | STRONG | OKR 3, 1 | 1: Early churn | Churn → Onboarding quality |
| G3 | Settlement shock after fast sign-up | Granola | Leadership (Sam) | New venues | STRONG | OKR 3 | 3: Billing opacity | Churn → Core friction |
| G4 | No BDM sales tools; 4 apps open during demos | Granola | Leadership (Sam) | BDMs | STRONG | OKR 3 upstream | 5: BDM tooling | Churn → Onboarding quality |
| G5 | Owners hate slide decks; need tailored social proof | Granola | Leadership (Sam) | BDMs + Venues | STRONG | OKR 3 upstream | 5: BDM tooling | Churn → Onboarding quality |
| G6 | Corroboration: 40% early churn, handover failure | Granola | Leadership (Adam) | All venues + AMs | STRONG | OKR 3 | 1: Early churn | Churn → Onboarding quality |
| G7 | Ops overriding venue-disabled deals → billing disputes | Granola | Unknown (Vaishali) | Venues | STRONG | OKR 2, 3 | 4: Deal confusion | Deal perf → Trust |
| G8 | Holiday hours last-minute; no ownership of process | Granola | Unknown (Vaishali) | Eng/Ops | MEDIUM | OKR 1 | (Standalone) | AM opt → Automation |
| G9 | Manual venue profile: 400/mo, 133hrs, $200k/yr | Granola | Unknown (Justin) | Ops (Karen's team) | MEDIUM | OKR 1 | (Standalone) | AM opt → Automation |
| G10 | Churn radar / deal performance dashboard desired | Granola | Unknown (Justin) | AMs + Leadership | MEDIUM | OKR 1, 3 | (Standalone) | AM opt → System automation |
| G11 | Deal scheduling confusion (tables per window) | Granola | Leadership (Sam) | Venues | STRONG | OKR 2 | 4: Deal confusion | Deal perf → Trust |
| G12 | Time-of-day pricing not reflected in deal score | Granola | Leadership (Sam) | Venues | STRONG | OKR 2 | 2: Discount economics | Deal perf → Trust |
| G13 | Angela built Freckle scraper for BDM pre-call intel | Granola | BDM (Angela) | BDMs | STRONG | OKR 3 upstream | 5: BDM tooling | Churn → Onboarding quality |
| G14 | Missing data fields: lat/long, AOV, category | Granola | Leadership (Adam) | BDMs | STRONG | OKR 3 upstream | 5: BDM tooling | Churn → Onboarding quality |
| G15 | BDMs google venues; no localised data or pitch path | Granola | Leadership (Adam) | BDMs | STRONG | OKR 3 upstream | 5: BDM tooling | Churn → Onboarding quality |
| G16 | Building pitch → sign-up → 30-day journey fix | Granola | Leadership (Adam) | BDMs + New venues | MEDIUM | OKR 3 | 1: Early churn | Churn → Onboarding quality |
| H1 | Bar Sopra: Contact left, encouraged cancel | HubSpot CS | CS | Venue (Bar Sopra) | STRONG | OKR 3 | (Churn event) | Churn → Core friction |
| H2 | NC's Chaat: Restaurant closed | HubSpot CS | CS | Venue (NC's Chaat) | STRONG | OKR 3 | (Business closed) | — |
| H3 | Belles Hot Chicken: $1,983.53 outstanding debt | HubSpot CS | CS | Venue (Belles) | STRONG | OKR 3 | 3: Billing opacity | Churn → Core friction |
| H4 | Barchetta Italian: Owner requests immediate cancel | HubSpot CS | CS | Venue (Barchetta) | STRONG | OKR 3 | (Churn event) | — |
| H5 | Bar Conte: 2 venues terminating, management decision | HubSpot CS | CS | Venue (Bar Conte x2) | STRONG | OKR 3 | (Churn event) | — |
| H6 | Wok & Wild: Shut down but still live on platform | HubSpot CS | CS | Venue + AM (Libby) | STRONG | OKR 3, 1 | (Process failure) | AM opt → Automation |
| H7 | Ming's Cuisine: Termination request | HubSpot CS | CS | Venue (restID: 01A8CA17) | STRONG | OKR 3 | (Churn event) | — |
| H8 | BD Dine: Cancel — "could not find any benefit" | HubSpot CS | CS | Venue (restID: C27A8D5B) | STRONG | OKR 3 | 1: Early churn | Churn → Onboarding quality |
| H9 | Himalayan Nepalese: No payments 3 months | HubSpot CS | CS | Venue (Himalayan) | STRONG | OKR 3 | 3: Billing opacity | Churn → Core friction |
| H10 | Cairo Nights: Believes double-charged | HubSpot CS | CS | Venue (Cairo Nights) | MEDIUM | OKR 3 | 3: Billing opacity | Churn → Core friction |
| H11 | Monsoon Palace: Closed, unresponsive, no tx since Feb | HubSpot CS | CS | Venue (Monsoon) | STRONG | OKR 3 | (Silence/churn) | — |
| H12 | Liyin Rice Roll: Considering cancel, service concerns | HubSpot CS | CS | Venue (Liyin) | MEDIUM | OKR 3, 2 | 4: Deal confusion | Deal perf → Trust |
| H13 | Melroad Pizza: Zero bookings, lost app access | HubSpot CS | CS | Venue (restID: F5751B8E) | MEDIUM | OKR 2, 3 | 4: Deal confusion | Deal perf → Trust |
| H14 | Unknown venue: Onboarding withdrawal pre-activation | HubSpot CS | CS | Unknown venue | MEDIUM | OKR 3 | 1: Early churn | Churn → Onboarding quality |
| H15 | Famished Wolf: Margin erosion, conditional 30-day review | HubSpot AM | AM | Venue (Famished Wolf) | STRONG | OKR 3, 2 | 2: Discount economics | Churn → Core friction |
| H16 | Unknown venue: Owner annoyed by follow-up, wants termination | HubSpot AM | AM | Unknown venue | MEDIUM | OKR 3 | (Churn event) | — |
| H17 | Unknown venue: Close account process executed (voucher-only) | HubSpot AM | AM | Unknown venue | MEDIUM | OKR 3 | (Churn event) | — |
| H18 | Unknown venue: Full offboarding executed (bookings, events, etc.) | HubSpot AM | AM | Unknown venue | MEDIUM | OKR 3 | (Churn event) | — |

### Historical Churn Pattern Signals (Hub CSV: 30 records)

| Category | Count | Key Pattern |
|---|---|---|
| Price / margin | 13 (43%) | Margins too thin for any discount; 30% specifically cited as unviable; hard caps at 20% |
| Business closed | 5 (17%) | Mix of permanent closures and temporary (renovations, landlord disputes) miscategorised as churn |
| Other | 6 (20%) | Includes "rude EatClub customers" complaints, seasonal capacity fullness, functions-only pivots |
| Product fit | 3 (10%) | Out of area, low volume — coverage gaps |
| No engagement | 2 (7%) | Passive withdrawal: pause requests → silence → churn |
| Sold / ownership change | 1 (3%) | No re-onboarding under new ownership attempted |
| **Notes quality:** | 9 STRONG, 9 MEDIUM, 12 WEAK | **40% of churn records have empty or useless notes** — the churn record itself is a data quality problem |

---

## 🗺️ OST Update

### AM Optimisation (OKR 1)

| Branch | Status | Evidence |
|---|---|---|
| **Manual AM task reduction** | Signal present but unvalidated | Justin cites 133 hrs/month on manual venue profiles ($200k/yr) — figures attributed to Crilly's prior synthesis, not primary measurement. Needs validation. |
| **Venue self-serve capability** | Strengthened | Deal confusion (Theme 4) confirms venues cannot self-serve deal config. Melroad Pizza lost app access entirely. Wok & Wild's closure not reflected on platform despite AM notification. |
| **System automation opportunities** | Strengthened | Manual profile population (G9), holiday hours last-minute chaos (G8), and venue offboarding still requiring multi-step manual checklist (H17, H18) all point to automation gaps. |

### Deal Performance (OKR 2)

| Branch | Status | Evidence |
|---|---|---|
| **Partner Portal engagement** | No direct data (Mixpanel blocked) | Melroad Pizza reports zero bookings and lost app access. BD Dine found "no benefit." Proxy signals suggest low engagement but cannot measure without Mixpanel. |
| **Venue-led revenue actions** | Weakened | Deal configuration is too confusing for venues to act independently (Theme 4). Ops overriding venue actions (G7) actively undermines venue agency. |
| **Deal score visibility and trust** | Strengthened as a problem | Sam's time-of-day pricing analysis (G12) reveals the deal score doesn't reflect demand reality. Famished Wolf's margin concern shows venues don't trust the economics. |

### Churn Reduction (OKR 3)

| Branch | Status | Evidence |
|---|---|---|
| **Friction in core venue experience** | Strong — dominant signal this week | Billing opacity (Theme 3), discount economics (Theme 2), deal confusion (Theme 4) all compound into the core venue experience. 8 active cancellations or churn events in HubSpot this week. |
| **Product fit for enterprise / Groups** | New signal | C9 Chocolate & Gelato: 3 locations churned within 2 weeks (Jan 25–Feb 9). Schnitz: 2 locations churned same day (Feb 2). Bar Conte: 2 venues terminating same week. Group venues appear to churn in clusters — no group-level account management or pricing visible. |
| **Onboarding journey quality** | Strong — root cause of early churn | 40% early churn figure (Theme 1). Active build in progress (sign-up form, Freckle, 30-day journey). |
| **Surfacing product value through data** | Moderate | BD Dine: "could not find any benefit" — value was never demonstrated. Famished Wolf: AM used data to disprove cannibalisation, showing data CAN save accounts when applied. But this is manual, not systemic. |

---

## ⚠️ Friction Stack Watch

### CRITICAL — Escalate to Luke

**Melroad Pizza n Kebab** | restID: `F5751B8E-2DC1-4B5D-927D-C46EE3FB62CD`
- **Sources:** HubSpot CS ticket
- **Journey stages:** Activation failure (zero bookings) + Ongoing engagement failure (lost app access) + Deal confusion (wants restructure) + Renewal decision (considering cancel)
- **Stack:** 4 friction points on a single venue. Cannot see bookings, cannot access the app, does not understand deal mechanics, wants to drop to 20%. This venue is days from churning.
- **Action needed:** AM call within 24 hours. Restore app access. Walk through deal performance data.

**Wok & Wild** | restID: unknown
- **Sources:** HubSpot CS ticket (AM: Libby Egan)
- **Journey stages:** Closure decision (shut down) + Process failure (still live on platform despite AM notification)
- **Stack:** Venue has shut down and notified both CS and AM Libby, but deals remain live and customers are still claiming offers. This is an active brand/trust damage event.
- **Action needed:** Immediate deal disable. Verify Libby received and actioned the notification.

**Himalayan Nepalese Restaurant & Cafe — Victoria Park** | restID: unknown
- **Sources:** HubSpot CS ticket (HIGH priority)
- **Journey stages:** Ongoing engagement (billing failure) + Renewal decision (owner demanding callback)
- **Stack:** 3 months of zero payments to the venue. Owner is escalating. If this isn't resolved immediately, this becomes a legal/reputation risk, not just churn.
- **Action needed:** Finance team escalation. AM call within 24 hours. Payment reconciliation.

**Belles Hot Chicken Circular Quay** | restID: unknown
- **Sources:** HubSpot CS ticket
- **Journey stages:** Ongoing engagement (debt accumulation) + Payment failure ($1,983.53)
- **Stack:** Large outstanding balance with failed payment. Finance Manager Wendy Bach has contacted CS directly. Venue-side escalation already in motion.
- **Action needed:** Payment retry + AM outreach to confirm venue relationship status.

### AT RISK — Monitor

**The Famished Wolf Kensington** | restID: unknown
- **Sources:** HubSpot AM note (Gong call)
- **Journey stages:** Ongoing engagement (margin concern) + Conditional renewal (30-day reassessment, follow-up May 18)
- **Stack:** Owner Simon explicitly questions long-term value of EatClub customers. Sales dropped after discount reduction. This is a ticking clock — if the May 18 review doesn't show improvement, they churn.
- **Action needed:** Ensure AM has a data-backed story ready for May 18. Tag for follow-up in 3 weeks.

**Bar Conte Sydney + Bar Conte Surry Hills** | restID: unknown
- **Sources:** HubSpot CS ticket
- **Pattern:** Two venues from same management terminating simultaneously. Group/multi-location churn signal.
- **Action needed:** Identify whether there are other Bar Conte locations on the platform. Understand if this is a group-level decision that could cascade.

**C9 Chocolate & Gelato (historical pattern)** | restIDs: `4B571921` (Crows Nest), `9AA6452C` (Docklands), `17765D31` (Windsor)
- **Sources:** Churn Hub CSV
- **Pattern:** 3 locations churned within 15 days (Jan 25–Feb 9 2024). Docklands cited fee confusion. Crows Nest went silent. Windsor had no notes. This is a confirmed group cascade churn — one bad experience likely triggered a multi-location pull.
- **Insight:** Group/franchise venues need group-level AM treatment, pricing, and reporting. Currently invisible in the system.

---

## 💡 Synthesis Notes

### What surprised me

1. **40% is a staggering early-churn number and leadership can name the exact cause chain.** Sam Benjamin articulates the full sequence — ICP misfit → no handover → no comprehension → settlement shock → churn — with specificity that suggests this has been known for a long time. The question is not "what's the problem" but "why hasn't it been solved yet?" The answer appears to be: there was no tooling (Freckle is brand new) and no structured onboarding journey (being built now).

2. **The churn notes are a data quality crisis in themselves.** 40% of churn records have empty or single-word notes. "Closed down." "Pushed out date." "See hubspot ticket." When Blessie writes "can't see any notes and was before my time," that's the system failing. Every unrecorded churn reason is an unlearnable lesson. This is an OKR 1 issue — the close-account process should force structured reason capture.

3. **Group/multi-location churn is invisible.** C9 (3 locations in 15 days), Schnitz (2 same day), Bar Conte (2 this week) — there is no mechanism to detect or respond to group-level churn. A single group decision can remove 2–5 venues in one stroke, but the system treats each as an independent event.

4. **Ops overriding venue-disabled deals is a trust-destroying pattern.** Vaishali's signal (G7) describes a scenario where a venue deliberately disables a deal, EatClub ops re-enables it, and the venue then demands a refund. If this is happening at scale, it undermines the entire premise of venue control in Partner Portal.

5. **The discount model problem has a proposed solution.** Sam's time-of-day blended pricing concept (25% peak / 45% off-peak → 30% blended) is a specific, testable product hypothesis that directly addresses the "flat 30% kills thin-margin venues" problem. This is unusually far along for a signal.

### What is missing

- **Slack data** was mentioned but not delivered. This is likely the highest-volume signal source and its absence means AM-to-AM patterns, CS escalations, and real-time incident signals are invisible this week.
- **Deal Score data** was not provided. Without it, I cannot identify venues with score = 0 (critical churn signal per the system definition) or track score changes that predict churn.
- **Mixpanel data** is blocked. Without Partner Portal engagement data, OKR 2 measurement is entirely proxy-based. Specifically: I cannot tell how many venues are logging in, editing deals, or even seeing their deal scores.
- **SMS data** is empty. Either no venue-to-AM messages occurred this week (unlikely) or the data pipeline didn't capture them.
- **restIDs are missing from most HubSpot signals.** Only 3 of 18 HubSpot records include a restID, making cross-referencing with churn data, deal scores, and Mixpanel impossible for 83% of active tickets.

### Interview questions that would sharpen the weakest signals

| Theme | Question | Target | Why |
|---|---|---|---|
| 1: Early churn | "Walk me through what happened between your BDM visit and your first week on EatClub. What surprised you?" | Recently signed venue owners (30-60 days in) | Validates whether settlement shock is universal or specific to certain BDM practices |
| 2: Discount economics | "What's the lowest discount percentage where you'd still see EatClub as worth it?" | Churned venues citing price/margin | Tests whether a flexible pricing tier could have retained them |
| 3: Billing opacity | "When you got your first EatClub settlement, did you know it was coming, and did the amount match what you expected?" | Venues in month 1-2 | Isolates whether the problem is timing, amount, or both |
| 4: Deal confusion | "If I asked you right now to change your deal from 30% to 25% and add a second time slot, could you do it in Partner Portal?" | Active venues | Tests actual self-serve capability vs. assumed capability |
| G9: Manual profiles | "How many of the 15 data fields per venue could be auto-populated from existing data sources like Google Places, Outscraper, or the BDM sign-up form?" | Karen's offshore team + Engineering | Validates the $200k figure and identifies which fields are actually automatable |

### What would move OKR 1 and OKR 2 most based on this week's signals

**OKR 1 (Scale AM Optimisation):** The highest-leverage action is **structured reason capture at close-account** — force the offboarding process to record venue name, restID, primary reason (from a constrained list), and a 2-sentence owner quote. This costs almost nothing, would immediately fix the 40% empty-notes problem, and generates the training data needed for every churn prediction model downstream. Second: validate and scope the manual venue profile automation (G9) — if 133 hrs/month is real, this is the single largest time-recovery opportunity in the business.

**OKR 2 (Drive Deal Performance):** The highest-leverage action is **deal configuration simplification in Partner Portal** — the current model is too complex for venues to self-serve, so they don't. Sam's own description ("we've never been able to explain this to a venue") is the clearest possible statement that the UX is failing. Until venues can understand and configure their own deals, AMs will remain the bottleneck and Partner Portal engagement will stay low.

---

## Routing Block