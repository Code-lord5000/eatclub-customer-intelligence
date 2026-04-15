# Crilly W16 Synthesis — Week of 13–16 April 2026

**Run date:** 2026-04-16
**Sources ingested:** Slack (8 channels — live), Mixpanel (top events list only — aggregate counts unavailable, API format issue), HubSpot (403 scope error — tickets unavailable this run), Granola (MCP not available in current environment)
**Prior context loaded:** memory.json (partial — file truncated at line 49 due to corruption), agents_memory.json (full)
**Confidence note:** Slack is live for the first time this run cycle. HubSpot tickets and Granola meetings remain dark. Severity ratings reflect Slack-only signal density — treat as floor.

---

## 🔥 Rising themes this week

---

### 1. Deal settings silently reverting — venues can't trust their own configuration

**Heat:** HIGH
**Signal count:** 4 distinct venues, 3 Slack channels
**Recurrence:** RISING (W15 first confirmed, W16 now 4 instances)
**Lifecycle:** RISING (3 weeks) — base score × 1.2
**OKR:** OKR1 (AM rework), OKR2 (venue engagement broken), OKR3 (churn risk from trust loss)
**OST branch:** System automation opportunities; Friction in core venue experience

**Problem statement:** Venue deal settings — recurring schedules, discount levels, offer toggles — are reverting to earlier configurations without AM or venue intervention. This has now affected at least 4 named venues in a single week. Venues cannot trust that changes they make (or AMs make on their behalf) will persist. Every revert requires an AM to investigate, re-apply, and communicate — hours of manual work that shouldn't exist, and silent revenue loss when no one notices.

**Evidence:**
- **Lumen Alley Coffee & Bagels** (B0A4E510): Deals changed without intervention — **second occurrence** (Renee flagged via ticket + Slack, "now the second time this issue has happened")
- **Taketori Fusion Japanese**: "Removed 30%s and changed recurring schedule but reverted to original setup done upon onboarding. Also hasn't closed the store for dine-in today and tomorrow."
- **Rice Paper Scissors Fitzroy**: Selected "disable" during holiday hours pop-up — deals remained live. Venue emailed complaint.
- **Ombre Italian Newstead**: TA orders processing with offers turned off (separate toggle failure same underlying bug class)

**Mom Test quality:** STRONG — all four are specific past behaviours described by AMs relaying venue experience.
**Journey stage:** Ongoing engagement — deal management. All post-activation.
**Recommended action:** ESCALATE — Jira discovery ticket. Holiday hours interaction with deal settings appears to be a specific failure mode. Lumen Alley having a second occurrence elevates this above a one-off.

---

### 2. Partner Portal self-serve gap — AMs manually doing what venues should own

**Heat:** HIGH
**Signal count:** 8+ distinct AM requests this week (CLM0UPW4U + C08EUGM8347)
**Recurrence:** CHRONIC (observed every week since W12)
**Lifecycle:** CHRONIC — add +2 to base heat score
**OKR:** OKR1 (primary), OKR2 (secondary)
**OST branch:** Venue self-serve capability; Manual AM task reduction

**Problem statement:** AMs route routine venue configuration through an ops Slack channel because Partner Portal does not support these actions. Requests include: NCI boost activation, boost removal, guest limit changes, seat time changes, no-show buffer removal. The Limerick Arms explicitly stated "Can't enable NCI boost on 25% deals on the partner portal." Eight distinct instances in a single week; at 175+ venues per AM this is a compounding bottleneck. Each request consumes AM time that the system should absorb.

**Evidence this week:**
- **The Limerick Arms** (B7F15903): "Can't enable NCI boost on 25% deals on the partner portal" → manual request via channel
- **Ronnies Pizza House** (8D804C6C): NCI activation on lunch 12pm–4pm 30% → manual request
- **Zaab** (CBEB1310): Remove 5% boosts → manual request
- **Chapati - Melbourne CBD** (691B5503): Limit guests to 4 → manual request
- **Phat Lon** (507AD055): Change seat time to 1.5hrs → manual request
- **Seven Spices Modern Indian** (DE1B0ED4): Change sitting time 3hr → 2hr → manual request
- **Cook & Archie's**: Remove no-show buffer → manual request
- **Rigatoni + Seasons Provedore**: Turn off RIA → manual request
- **30+ menu digitisation tickets in <24h**: Ops team flagging as unsustainable — AMs not setting expectations with venues

**Mom Test quality:** STRONG — named AMs, named venues, recurring weekly pattern.
**Journey stage:** Ongoing engagement (all post-activation). Some at Renewal/churn decision (venues pausing or frustrated).
**Recommended action:** Jira discovery ticket. NCI boost toggle and seat configuration are the two highest-frequency gaps — prioritise these first.

---

### 3. Masala Flames iOS dine-in visibility bug — 5+ months unresolved, multi-channel

**Heat:** HIGH
**Signal count:** 3 reports this week (2 AMs independently), prior HubSpot ticket
**Recurrence:** CHRONIC (5+ months per AM reports)
**Lifecycle:** CHRONIC — add +2 to base heat score
**OKR:** OKR3 (direct churn risk), OKR1 (AM time investigating)
**OST branch:** Friction in core venue experience

**Problem statement:** Masala Flames Indian Cuisine's dine-in deals are not visible on the iOS app for at least 5 months. They ARE visible on desktop and Android. The venue is fully live but customers on iOS cannot see or redeem dine-in offers. This is direct daily revenue loss. Two AMs reported this independently in the same week without referencing each other — meaning no engineering owner has been assigned and the bug is not in a visible fix queue.

**Evidence:**
- **C094UFR4ENQ**: "Masala flames dine in deals are not showing on the app... this issue has been on going for 5 months. They are showing on desktop but just not the APPS. I just re-added their deals too." AM flagging ECPAY may need enabling.
- **C08EUGM8347**: Second AM independently: "Masala as their dine in deals don't show on the APP and haven't for ages. Are you able to please enable ECPAY?"
- **Prior week (agents_memory.json)**: HubSpot ticket already raised: "Masala Flames — iOS deal visibility bug, 5 months"
- **restID:** 6A3A7879-EACD-4ACF-BA44-770D4608CF9C

**Mom Test quality:** STRONG — specific, past, ongoing. Two AMs confirming independently.
**Cross-reference:** Masala Flames appears in ops channel AND tech channel this week. High-confidence friction stack.
**Recommended action:** ESCALATE immediately. 5 months unresolved is not acceptable. Assign engineering owner now. ECPAY enabling may be the fix — test first, then build permanent fix.

---

### 4. AM vacation coverage gap enabling churn

**Heat:** MEDIUM–HIGH
**Signal count:** 5 instances this week (C08E9UM3VAR)
**Recurrence:** RISING (W15: "The Nuns Pool — AM on vacation, no action taken"; W16: 5 new instances)
**Lifecycle:** RISING (2 weeks) × 1.2
**OKR:** OKR1 (system should cover), OKR3 (churn risk)
**OST branch:** System automation opportunities; AM relationship friction

**Problem statement:** When AMs go on vacation, no automatic handover or routing exists. Venues requesting to cancel sit unassigned. CS manually asks Slack "who can I assign this to?" — which depends on someone noticing the message. This is a systemic gap that produces one class of entirely preventable churn.

**Evidence:**
- **Friends & Flowers Cafe**: "Would like to cancel their contract with EatClub effective immediately. AM is currently on vacation. Can someone kindly assist?" — No one named as backup.
- **Anatel (Sydney)**: AM on vacation status, ticket unassigned
- **Crazy Bites HS**: AM on leave, CS left ticket and asked anyone to pick up
- Multiple "it looks like [AM] is on vacation. Who can I assign a ticket to?" messages in CS channel
- **Jai on leave**: "Can I please be tagged in everything for WA from tomorrow to Monday so nothing is missed" — manual workaround, entirely dependent on one person's foresight

**Mom Test quality:** STRONG — Friends & Flowers is a real active cancel request with no owner.
**Journey stage:** AM relationship → Renewal/churn decision point.
**Recommended action:** Discovery ticket — automated OOO routing in HubSpot. If AM has vacation status, open tickets and incoming pause/cancel requests should auto-route to a named backup. This is a single HubSpot workflow change.

---

### 5. Onboarding expectation gap driving late-stage churn

**Heat:** MEDIUM
**Signal count:** 4 named venues with clear expectation mismatch; ~6 implicit in ownership-change + "no value" churns
**Recurrence:** RISING (W15 pattern, W16 new named examples)
**Lifecycle:** RISING (2 weeks) × 1.2
**OKR:** OKR3 (primary), OKR1 (AM rescue time)
**OST branch:** Onboarding journey quality; Surfacing product value through data

**Problem statement:** Venues are churning 1–3 months after sign-up citing expectations set at sign-up that were not met or not clearly communicated. The misalignments are consistent: discount applies to total bill (not just EatClub share), calibre of brand mix on platform, and economics of promotional giveaways. By the time AMs discover the mismatch, the venue is at churn decision point.

**Evidence:**
- **Sushi Mami** (62B1C84B): "Policies weren't clearly communicated at the start (especially the discount applying to the total bill), which led to misunderstandings and financial losses." Also: "EatClub customers can't be identified at the table."
- **Honest Crust Sourdough Pizza** (4FC9DDA9): "Calibre of brands on EatClub is lower than what they were originally told, and several brands they were told would be signing haven't joined."
- **Persian Kebab House** (B05AAD6F): "Has not seen the value in EatClub despite being offered lower-priced deals and promotions. These offers were not well received."
- **Fress Restaurant & Bar** (1265C332): "Miscommunication regarding a burger giveaway when signing up — wasn't happy about 1. having to pay for part of the food cost, 2. not having a clear timeline on when giveaway would happen."

**Mom Test quality:** MEDIUM-STRONG — specific past events but reported via AM notes, not directly from venue.
**Journey stage:** Onboarding/Activation → Churn decision point. All failed at expectation gap between sign-up and first weeks live.
**Recommended action:** Interview — what do venues believe they're signing up for vs. what first 30 days delivers? Also watch the "discount applies to total bill" specific — this may warrant a proactive welcome communication clarification.

---

## 📋 All signals this week — classified

| Signal | Source | Team | Who affected | Mom Test | OKR | Theme | OST branch |
|--------|---------|------|--------------|----------|-----|-------|------------|
| Lumen Alley deal revert (2nd occurrence) | CLM0UPW4U | AM | Venue | STRONG | OKR1/2/3 | Deal settings reverting | System automation |
| Taketori Fusion schedule revert | C08EUGM8347 | AM | Venue | STRONG | OKR1/2/3 | Deal settings reverting | System automation |
| Rice Paper Scissors holiday disable failed | C08EUGM8347 | AM | Venue | STRONG | OKR1/2/3 | Deal settings reverting | System automation |
| Ombre Italian TA with offers off | CLM0UPW4U | AM | Venue | STRONG | OKR1/3 | Deal settings reverting | System automation |
| Limerick Arms — NCI not in portal | CLM0UPW4U | AM | Venue | STRONG | OKR1/2 | Self-serve gap | Venue self-serve |
| Ronnies Pizza NCI via channel | CLM0UPW4U | AM | Venue | STRONG | OKR1/2 | Self-serve gap | Venue self-serve |
| Zaab boost removal via channel | CLM0UPW4U | AM | Venue | STRONG | OKR1 | Self-serve gap | Manual AM task |
| 30+ menu digitisation tickets in 24h | C08EUGM8347 | Ops | AM team | MEDIUM | OKR1 | Self-serve gap | Manual AM task |
| Masala Flames iOS 5-month bug (2 AMs) | C094UFR4ENQ + C08EUGM8347 | AM + Tech | Venue | STRONG | OKR3 | iOS visibility bug | Core experience |
| Friends & Flowers cancel, AM on leave | C08E9UM3VAR | CS | Venue | STRONG | OKR1/3 | AM coverage gap | System automation |
| Multiple "who do I assign to?" | C08E9UM3VAR | CS | AM team | STRONG | OKR1 | AM coverage gap | System automation |
| Sushi Mami — discount miscommunication | CLM0UPW4U | AM | Venue | MEDIUM | OKR3 | Onboarding expectation gap | Onboarding quality |
| Honest Crust — brand calibre promise | CLM0UPW4U | AM | Venue | MEDIUM | OKR3 | Onboarding expectation gap | Onboarding quality |
| Fress Restaurant — burger giveaway miscomm | CLM0UPW4U | AM | Venue | STRONG | OKR3 | Onboarding expectation gap | Onboarding quality |
| Life of Chi churn — double dipping + Ipos | CLM0UPW4U | AM | Venue | STRONG | OKR3 | Double dipping T002 + POS T003 | Core experience |
| The Last Jar — 4th cancel, T&C abuse | CLM0UPW4U | AM | Venue | STRONG | OKR3 | Customer T&C abuse | Core experience |
| 6+ dine-in for takeaway enforcement | C08E9UM3VAR | CS | Customer | STRONG | OKR3 | Customer T&C abuse | Core experience |
| Forno 88 — $643 takeaway fraud attempt | C08E9UM3VAR | CS | Customer | STRONG | OKR3 | Customer quality | Core experience |
| Everest MoMo — cancel email unactioned, $148 dispute | CLM0UPW4U | AM | Venue | STRONG | OKR3 | AM responsiveness | AM relationship |
| Garibaldi Pizzeria — Angie urgent, multi-channel | C08E9UM3VAR + CLM0UPW4U | CS + AM | Venue | STRONG | OKR3 | Watch list venue | Friction stack |
| Delhi Darbar billing error (billingDay: 0) | C09D1CS6D1N | System | Venue | STRONG | OKR3 | UK billing bugs | UK market |
| UK venue charged £298.66 before go-live | C099KA8RHV3 | UK AM | Venue | STRONG | OKR3 | UK billing bugs | UK market |
| Masala Brick Lane £1,031 debt, paused | C099KA8RHV3 | UK AM | Venue | STRONG | OKR3 | UK debt | UK market |
| Khanoon Thai + Palmyra's — fraud risk | C099KA8RHV3 | UK AM | Venue | STRONG | OKR3 | UK fraud | UK market |
| QBR stats showing $0 for active venues | C08EUGM8347 | AM | Venue/AM | STRONG | OKR2 | Reporting inaccuracy | Deal score visibility |
| 3DS blocking card addition on Android | C094UFR4ENQ | Eng | Customer | STRONG | OKR3 | Technical incident | Core experience |
| Partner signup form broken (cardId) | C094UFR4ENQ | Eng | BDM/New venues | STRONG | OKR3 | Technical incident | Onboarding |
| Yum Yum Tree — "no one bothered to call me" | C09D1CS6D1N | Venue | Venue | STRONG | OKR3 | AM non-responsiveness | AM relationship |
| Second Wife — zero transactions, lease ended | CLM0UPW4U | AM | Venue | STRONG | OKR3 | Deal score zero T001 | Churn model |
| Viet Soul UK — dispute over time-window claim | C09D1CS6D1N | UK | Venue | STRONG | OKR3 | Customer quality UK | UK market |
| Earlwood Izakaya — "no direct rep to speak to" | C09D1CS6D1N | Venue | Venue | STRONG | OKR1/3 | AM accessibility | AM relationship |

---

## 🗺️ OST update

### OKR1 — AM Optimisation

**Strengthened this week:**
- Self-serve gap evidence is overwhelming. NCI boost, seat time, guest limit, boost removal, no-show buffer — all going through Slack instead of Partner Portal. This is the clearest OKR1 opportunity in current data.
- AM coverage gap during vacation has a simple systemic fix (HubSpot OOO routing) that would prevent an identifiable class of churn.
- 30+ menu digitisation tickets in <24h is a manual bottleneck that is becoming unsustainable at current scale, let alone at target AM:venue ratio of 350–400.

**Weakened:**
- No new data on Billie AI assistant usage or adoption this week (Granola unavailable).

**New sub-opportunity:**
- Automated vacation routing: When AM is on OOO status, incoming pause/cancel tickets and active churn risks should auto-route to a designated backup or a triage queue. This is one HubSpot workflow.

---

### OKR2 — Deal Performance Through System-Led Actions

**Strengthened this week:**
- Mixpanel top events confirm Partner Portal engagement IS occurring: Offer edited, Page view - offers/active, and Nav link clicked - offer-performance are all in the top 20 events by unique users. Venues ARE using the portal — but the gaps in what they can do there are driving them back to AMs.
- NCI activation requests via Slack are venues WANTING to engage in revenue-driving actions but being blocked by missing self-serve capability. Demand exists; supply doesn't.

**Weakened:**
- QBR stats showing $0 for venues doing ~$7k/month net: If venues can't trust the data in the portal, they won't act on it. This is a silent OKR2 killer — every inaccurate QBR report is a venue who now distrusts the platform as a decision-making surface.

**New sub-opportunity:**
- Fix QBR reporting bug before building any new engagement features. The trust prerequisite for OKR2 is accurate data. One venue reported their $0 QBR stats; this is almost certainly not isolated.

---

### OKR3 — Churn Reduction

**Strengthened this week:**
- Friction stacking clearly operating: multiple venues showing signals across 2+ sources and 2+ journey stages (see Friction Stack section).
- Life of Chi churn explicitly named both double dipping (T002) AND POS integration gap (T003) in the same note. First confirmed co-occurrence. These two themes are compounding, not independent.
- Customer T&C abuse (dine-in for takeaway, max pax breaches) is creating genuine venue frustration. The Last Jar at 4th cancel attempt is the leading indicator of what this theme produces if unresolved.

**Weakened:**
- Cannot confirm if deal score zero count (T001 — 397 venues at W16) has grown or shrunk. HubSpot unavailable; no CSV data.
- No Granola data to confirm or deny AM team sentiment or internal escalations.

---

## ⚠️ Friction stack watch

### 🔴 ACTIVE CHURN RISK — Garibaldi Pizzeria
- **Signals this week:** Angie urgently contacting multiple channels (C08E9UM3VAR), customer complaint about menu pricing (C08E9UM3VAR). W15: escalation across multiple channels.
- **Sources:** 2+ channels, 2+ weeks, 2+ journey stages (Ongoing engagement + AM relationship)
- **restID:** Unknown — needs lookup
- **Action:** Flag to Luke Maurel — IMMEDIATELY. Second consecutive week with multi-channel urgent signals.

---

### 🔴 ACTIVE CHURN RISK — The Last Jar
- **Signals:** 4th cancel request from Bryony. Previous retain attempts have not addressed root cause (customers using dine-in for takeaway, booking + walk-out). Now explicitly includes multiple T&C dimensions.
- **restID:** EC9FABAF-1C92-4C45-8C6F-79B836A09D20
- **Stage:** Renewal/churn decision. 4th request = treat as confirmed churn unless root causes addressed.
- **Action:** Flag to Luke. Not a save-by-discount case — root cause is platform abuse. Consider whether blocking repeat T&C offenders is feasible.

---

### 🟠 ESCALATING — Masala Flames Indian Cuisine
- **Signals:** iOS visibility bug 5+ months unresolved. Two AMs reporting independently in same week. Prior HubSpot ticket exists.
- **restID:** 6A3A7879-EACD-4ACF-BA44-770D4608CF9C
- **Stage:** Ongoing engagement — bug preventing deal visibility, likely suppressing deal score artificially
- **Action:** Engineering — immediate. ECPAY enabling is the suspected fix, test now.

---

### 🟠 ESCALATING — Lumen Alley Coffee & Bagels
- **Signals:** Deal revert 2nd occurrence (W15 + W16). Prior HubSpot ticket raised. Watch list from W15.
- **restID:** B0A4E510-B0D2-4892-A311-5066FCA654F4
- **Stage:** Ongoing engagement — deal management trust broken by recurring revert
- **Action:** Engineering + AM — urgent. Second occurrence makes this a priority.

---

### 🟡 WATCH — Friends & Flowers Cafe
- **Signals:** Active cancel request, AM on vacation, no coverage assigned
- **restID:** Unknown — needs lookup
- **Stage:** Renewal/churn decision — unattended
- **Risk:** Every day without response while venue is actively requesting cancellation increases no-save probability.

---

### 🟡 WATCH — Yum Yum Tree Victoria Park (7831FFCB)
- **Signals:** Pause request citing fees + "no one bothered to call me" on record
- **Stage:** AM relationship → churn decision
- **Risk:** Non-responsiveness complaint documented. If not actioned, confirms venue's belief.

---

### 🟡 WATCH — Everest MoMo Station (D82CAAD0)
- **Signals:** Went live March 12. Sent cancel email March 18. Not actioned. Now disputing $148.08 charge ("did not want to receive any more transactions").
- **Stage:** Activation → immediate exit (never retained)
- **Risk:** Financial dispute + unactioned cancellation = likely chargeback + negative WOM.

---

## 💡 Synthesis notes

**What surprised me:**
1. **Volume of self-serve gap signals**: Eight distinct AM requests through ops channels in a single week is not sampling noise — it is structural. The Partner Portal exists but doesn't cover the actions that AMs and venues need most. NCI boost and seat configuration alone would eliminate a meaningful fraction of these requests.
2. **Two AMs flagging Masala Flames independently**: Neither referenced the other. This means the bug has no visible owner in any shared queue. 5 months of silence on a deal-visibility bug is a significant process failure.
3. **Life of Chi churn cited both T002 and T003 simultaneously**: "Too busy in the evenings" + "can't run lunch offers because of his own specials" (double dipping) + "Ipos no integration" = these three failure modes are operating as a cluster, not independently.
4. **QBR stats showing $0 for an active venue**: This came through in the incidents channel as a side note, not a major alert. If this is widespread, the entire OKR2 engagement strategy is undermined. Venues using their QBR to decide whether EatClub is working for them will see $0 and draw the obvious conclusion.
5. **"No one bothered to call me"** (Yum Yum Tree): This is the clearest venue voice signal of the week. It's a pause request but the framing is a relationship complaint. The venue didn't churn because of fees — they paused because they felt ignored.

**What is missing:**
- HubSpot tickets (403 scope error): Support Pipeline and URGENT AM Follow-Up pipelines likely contain additional friction stack signals not visible in Slack.
- Mixpanel aggregate counts: Cannot compare W16 event counts to W15 baseline. Top events list confirms the events exist — but trend direction is unknown.
- Granola meetings: All AM/BDM/CS meeting context invisible this run.
- Deal score zero count: T001 is our highest-recurrence chronic theme but cannot be updated without CSV or HubSpot access.
- memory.json is corrupted (truncated at line 49) — venue_watch_list and OKR baselines did not load.

**Interview questions for weakest signals:**

For T011 (Onboarding expectation gap):
- "What did you think would happen in your first month on EatClub vs. what actually happened?"
- "When did the discount-on-total-bill mechanic first affect your margin? Was that explained at sign-up?"
- "What did the person who signed you up tell you about the type of restaurants on the platform?"

For T010 (Customer T&C abuse):
- "When a customer uses a dine-in offer for takeaway — how often? What does it cost you each time?"
- "When you raise a T&C issue with EatClub, what happens next? Is that fast enough?"
- "If EatClub could flag repeat T&C offenders before they arrived, would that change your view of the platform?"

**What would move OKR1 and OKR2 most:**
- **OKR1:** NCI boost toggle in Partner Portal + automated AM vacation routing. These two changes alone eliminate a significant fraction of the manual ops channel requests and prevent one identifiable class of churn.
- **OKR2:** Fix the QBR stats bug before deploying any new engagement features. Venues need accurate data before they'll act on the portal as a decision surface. One known venue at $0; assume more.

---

## Routing block

```routing
{
  "jira_tickets": [
    {
      "theme": "Deal settings silently reverting",
      "okr": "OKR1/OKR2/OKR3",
      "problem_statement": "Venue recurring deal schedules and offer toggles revert to earlier configurations without intervention. 4 confirmed venues in W16, including Lumen Alley (2nd occurrence). The holiday hours pop-up interaction appears to be a specific trigger. Venues cannot trust their configuration, requiring AM rework weekly.",
      "priority": "HIGH"
    },
    {
      "theme": "NCI boost and core deal settings not available in Partner Portal self-serve",
      "okr": "OKR1",
      "problem_statement": "AMs route NCI activation, boost removal, seat time, guest limit, and no-show buffer requests through Slack ops because Partner Portal doesn't support these. 8+ distinct instances W16. The Limerick Arms explicitly confirmed can't enable NCI boost. At target 350–400 venues/AM, this becomes structurally unmanageable.",
      "priority": "HIGH"
    },
    {
      "theme": "AM vacation coverage — no automated routing for cancel and churn-risk venues",
      "okr": "OKR1/OKR3",
      "problem_statement": "When AMs are on leave, incoming pause/cancel requests have no auto-routing. Friends & Flowers Cafe actively requested cancellation with AM on vacation — no backup named. One HubSpot OOO workflow would prevent this class of loss.",
      "priority": "MEDIUM"
    }
  ],
  "escalations": [
    {
      "theme": "Masala Flames iOS visibility bug — 5+ months unresolved",
      "okr": "OKR3",
      "problem_statement": "Dine-in deals for Masala Flames (6A3A7879-EACD-4ACF-BA44-770D4608CF9C) not visible on iOS app for 5+ months. Two AMs reporting independently in same week. ECPAY enabling is suspected fix. Assign engineering owner immediately.",
      "priority": "CRITICAL"
    }
  ],
  "interview_questions": [
    {
      "theme": "Onboarding expectation gap",
      "questions": [
        "What did you think would happen in your first month on EatClub vs. what actually happened?",
        "When did you first feel the discount-on-total-bill mechanic affecting your margin? Was that explained at sign-up?",
        "What did the person who signed you up tell you about the calibre or type of restaurants on the platform?",
        "Was there a moment where you thought 'this isn't what I was told'? What happened then?"
      ]
    },
    {
      "theme": "Customer T&C abuse impact on venue",
      "questions": [
        "When a customer uses a dine-in offer for takeaway — how often does that happen at your venue?",
        "What does it cost you each time — financially and in time spent chasing it?",
        "When you raise a T&C issue with EatClub, what's the actual resolution process like?",
        "If EatClub could flag or block customers who had previously broken T&Cs, would that change your view of staying?"
      ]
    }
  ],
  "friction_alerts": [
    {
      "venue": "Garibaldi Pizzeria",
      "rest_id": "UNKNOWN — needs lookup",
      "signals": ["Angie urgently contacting multiple channels W15 + W16", "Customer complaint about menu pricing", "CS escalation 2+ channels"],
      "flag_to": "Luke Maurel — IMMEDIATE"
    },
    {
      "venue": "The Last Jar",
      "rest_id": "EC9FABAF-1C92-4C45-8C6F-79B836A09D20",
      "signals": ["4th cancel request from Bryony", "T&C abuse: dine-in for takeaway + customer booking walk-outs", "3 prior retain attempts failed"],
      "flag_to": "Luke Maurel — IMMEDIATE"
    },
    {
      "venue": "Masala Flames Indian Cuisine",
      "rest_id": "6A3A7879-EACD-4ACF-BA44-770D4608CF9C",
      "signals": ["iOS visibility bug 5+ months", "Two AMs independently reporting W16", "Prior HubSpot ticket unresolved"],
      "flag_to": "Engineering + assigned AM — URGENT"
    },
    {
      "venue": "Lumen Alley Coffee & Bagels",
      "rest_id": "B0A4E510-B0D2-4892-A311-5066FCA654F4",
      "signals": ["Deal revert 2nd occurrence W15 + W16", "AM ticket raised", "Watch list from W15"],
      "flag_to": "Engineering — URGENT"
    },
    {
      "venue": "Friends & Flowers Cafe",
      "rest_id": "UNKNOWN — needs lookup",
      "signals": ["Active cancel request", "AM on vacation", "No coverage assigned"],
      "flag_to": "Luke Maurel — same-day"
    }
  ],
  "watch_list": [
    "Yum Yum Tree Victoria Park (7831FFCB) — fees complaint + AM non-responsive, pause requested",
    "Everest MoMo Station (D82CAAD0) — cancel email unactioned, $148 dispute",
    "Delhi Darbar Surfers Paradise (B6D9E9C6) — billing bug membershipBillingDay:0",
    "Viet Soul UK (4F18F0AB) — customer claim dispute outside deal hours",
    "Masala Brick Lane UK — £1,031 debt, paused",
    "QBR stats $0 bug — likely affects more than one venue; investigate scope",
    "3DS Android rollout — halted, monitor customer sign-up completion rate",
    "Life of Chi churn — first confirmed T002+T003 co-occurrence; watch for pattern in upcoming churns"
  ]
}
```

---

## Data quality notes for next run

1. **HubSpot tickets**: 403 MISSING_SCOPES. Requires `tickets` read scope added to MCP OAuth config. Coordinate with HubSpot admin.
2. **Mixpanel aggregate counts**: 400 Invalid JSON Format on `event` parameter. Correct format likely requires JSON array (e.g. `["Offer edited"]`). Also: event names in agents_memory.json ("Partner Portal Login", "Deal Edit") do not match actual Mixpanel event names ("Offer edited", "Page view - offers/active"). Update agents_memory.json event name mapping.
3. **Granola MCP**: Not available in current tool environment. No meeting data this run. Check MCP configuration.
4. **memory.json**: File is corrupted — JSON truncated at line 49 with shell commands embedded. File needs repair before next run. venue_watch_list, OKR baselines, jira_tickets_raised, and saved_venues sections did not load.
