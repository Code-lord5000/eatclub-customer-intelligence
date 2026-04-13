# Crilly Synthesis — 2026-W16b (April 13, 2026)

**Sources available**: Slack (4 channels: churn, pause alerts, CS/AM ops, incidents)
**Sources unavailable this run**: Granola meeting transcripts (MCP tool not present in session), HubSpot, SMS, Churn CSV, Deal Score CSV, Mixpanel
**Confidence note**: Running on 1 of 7 signal source types (Slack only). The W16 synthesis (same day, earlier run) used structured CSVs with no Slack. This synthesis is the complement — rich in qualitative AM and CS signals, blind to portfolio-wide quantitative baselines. Treat together with W16 for full picture. Signal heat scores here are based on Slack frequency and proximate evidence only; cross-referencing with deal score and churn CSV would likely elevate several themes.

---

## 🔥 Rising Themes This Week

### 1. Deal Settings Reverting or Ignoring Venue Choices — System Reliability Crisis

**Heat**: 🔴 **HIGH**
**Signal count**: 4 venues, 2 sources (incidents channel + churn channel)
**Recurrence**: **RISING** (Lumen Alley explicitly states this is the second time it has happened to them; multi-venue cluster coincides with Easter long weekend)
**Lifecycle**: RISING (2+ weeks, at least one venue with confirmed recurrence)

**Problem statement**: Venues are configuring their deal settings — disabling deals for public holidays, removing high-discount tiers, adjusting schedules — and the system is silently ignoring or overriding those choices. Rice Paper Scissors Fitzroy selected disable before the Easter long weekend and deals stayed live on Sunday and Monday. Taketori Fusion Japanese removed 30% deals and changed their recurring schedule; both reverted to the original onboarding setup. Lumen Alley flagged deals changing without any intervention from their side or EatClub's side — this is the second time. Ombre Italian Newstead received a takeaway order while offers were turned off. The venue experiences this as the platform acting against their instructions. The cost is direct: unintended redemptions at margins they've explicitly chosen not to offer, operational disruption, and erosion of trust in the platform as something they control.

**Mom Test quality**: **STRONG** — "Before the holiday a pop-up showed up where they selected their normal opening hours and chose to disable deals. They said they clicked 'disable,' but for some reason the deals were still live on Sun & Mon." (Rice Paper Scissors). "Deals were changing without any intervention from either her side or ours, and this is now the second time this issue has happened." (Lumen Alley AM). Specific past behaviour, named dates, financial consequence.

**OKR**: OKR 2 (Deal Performance) — primary. OKR 3 (Churn Reduction) — Lumen Alley is a confirmed early churn where deal reliability was a contributing factor.

**OST branch**: Deal performance → Deal score visibility and trust; Churn reduction → Friction in core venue experience

**Journey stage**: Ongoing engagement — but Lumen Alley has crossed to churn decision

**Recommended action**: **Escalate + Discovery ticket** — (1) What is the actual failure mode? Holiday hours override logic? Schedule conflict resolution? (2) How many venues had deal activity over the Easter long weekend that contradicts their configured settings? (3) Is there an audit log that AMs or venues can access? (4) Lumen Alley is already churned — engineering needs to identify whether their deal-reverting issue and the broader Easter cluster are the same root cause or separate bugs.

---

### 2. Customer Quality / T&C Abuse Is Destroying Venue Deal Economics

**Heat**: 🔴 **HIGH**
**Signal count**: 6 venues, 2 sources (churn channel + CS/AM ops channel)
**Recurrence**: **CHRONIC** (customer quality as a churn driver has appeared in prior weeks; this week has the highest concentration of specific, named incidents)
**Lifecycle**: CHRONIC

**Problem statement**: Across this week's signals, venues are losing money because EatClub customers are systematically circumventing offer terms: redeeming dine-in vouchers for takeaway orders, booking via the venue's own website to bypass app redemption, arriving with parties of 10–12 when the offer is for 2–4, and in at least one case leaving without paying. The venues bear the cost. La Botte Pizza - Pascoe Vale lost approximately $200 in one week from customers booking via the venue website with large groups, leading the owner to drop all deals from 25% and 30% to 20% and threaten to leave. Plat Coffee churned explicitly citing "low quality customers who only cared about discount." Lumen Alley early-churned after a string of customers doing the wrong thing in their first two weeks. Earlwood Izakaya paused citing "booking before dining" and "commission to EatClub user even though they pay in full" — suggesting the commission model itself is perceived as unfair when customer behaviour is broken.

The CS team is being used as the mitigation layer: AMs are asking CS to call individual customers to educate them on T&Cs. This doesn't scale and doesn't prevent the next violation.

**Mom Test quality**: **STRONG** — La Botte: specific dollar amount, specific behaviour (website bookings, 10-person parties, T&C breaches over months), deal score reduction as observable consequence. Plat Coffee: owner statement at churn — direct and unambiguous. Lumen Alley: stated reason for early churn with reference to specific incidents.

**OKR**: OKR 3 (Churn Reduction) — primary. OKR 2 (Deal Performance) — venues actively reducing deal depth in response to customer quality.

**OST branch**: Churn reduction → Friction in core venue experience; Deal performance → Venue-led revenue actions

**Journey stage**: Ongoing engagement → Churn decision point (multiple venues)

**Recommended action**: **Discovery ticket** — (1) What is the current rate of T&C breach redemptions across the platform? (2) Is there any system-level detection of anomalous redemption patterns (large party size vs booking, dine-in vs TA)? (3) What does the current CS response workflow look like — how many T&C breach contacts does CS handle per week? (4) What would automated T&C enforcement look like at redemption time vs post-hoc? Interview La Botte owner — this is a near-save situation with strong specificity.

---

### 3. Sold-Business and Insolvency Churn — Macro Signal Worth Tracking

**Heat**: 🟡 **MEDIUM**
**Signal count**: 12+ venues, 2 sources (churn channel + pause alerts channel)
**Recurrence**: **RISING** (Jak's Group this week is the largest single group liquidation seen in these channels; sold-business pause cluster of 7 venues in pause alerts is high volume)
**Lifecycle**: RISING (2–3 weeks)

**Problem statement**: This week produced an unusually high volume of churns and pauses attributed to business sales and insolvency. Jak's Group — 7 venues across London (Jak's Bar, Jak's Kings Road, Jak's Cafe, Jak's Mayfair, MILA, The Beauchamp, Zefi) — churned simultaneously after the owner's company went into liquidation. The AM is attempting to repitch the new operators. In the pause alerts channel, 7 additional venues paused citing "sold business" (The Lil Hut x3 — Bardwell Park, Arncliffe, Bondi; Little Lebanon x2 — main + Victoria Park; The Hibiscus Tree; Souvlaki GR Windsor). Additionally: Cony's Bar entered voluntary administration with outstanding debt; Jumi's Cafe in financial difficulty; TacoBar citing cost of living and fuel prices; Subway Crows Nest citing financial difficulty.

The product implication is limited (EatClub can't prevent businesses from selling or closing), but two sub-signals are actionable: (1) EatClub currently has no early detection mechanism when a multi-venue group is in financial distress — the AM finds out when the churn request arrives. (2) The sold-business cluster suggests the AM handover process for ownership changes is undefined — new owners default to not continuing.

**Mom Test quality**: **MEDIUM** — Direct churn reasons stated by AMs who confirmed with venue owners. Behavioural evidence is the churn itself, not a hypothetical.

**OKR**: OKR 3 (Churn Reduction) — limited direct leverage, but ownership-change retention is an addressable sub-problem.

**OST branch**: Churn reduction → Product fit for enterprise / Groups; Churn reduction → Onboarding journey quality (re-onboarding for new owners)

**Journey stage**: Renewal / churn decision point

**Recommended action**: **Watch** — Track whether the sold-business volume is seasonal (post-Easter) or a sustained macro trend. One actionable sub-question: when a venue changes ownership, is there a defined re-onboarding process? The Jak's Group situation warrants a direct BDM escalation — 7 venues with new operators is a material retainment opportunity.

---

### 4. Manual AM Workload From Hub/Portal Gaps Is Constant and Invisible

**Heat**: 🟡 **MEDIUM**
**Signal count**: 5 requests this week, 1 source (churn channel — being used as ops request channel)
**Recurrence**: **CHRONIC** (appears every week in the churn channel)
**Lifecycle**: CHRONIC

**Problem statement**: AMs are using the churn channel as a request queue for routine venue configuration changes that the system does not currently support self-serve: max party size changes (Bumbles Cafe, The Walrus Waverley), NCI toggle (The Walrus Waverley), membership fee waivers (Riwayat), opening hours updates (Mama Made Roti via CS). Every one of these is a manual handoff: AM identifies a venue need → posts in Slack → waits for CS/ops to action → confirms done. At scale, this is a significant hidden AM time cost. Walrus Waverley required two separate requests this week (party size change and NCI toggle) — same venue, same AM, same channel, two manual touches.

These are precisely the actions the Q2 OKR 1 target (remove 10 hours/month of manual AM work per venue) should be addressing.

**Mom Test quality**: **STRONG (behavioral)** — The requests are directly observable. AMs are doing this every week. The volume is understated because we only see the churn channel; other channels likely have similar patterns.

**OKR**: OKR 1 (AM Optimisation) — primary.

**OST branch**: AM optimisation → Manual AM task reduction; AM optimisation → Venue self-serve capability

**Journey stage**: Ongoing engagement (operational)

**Recommended action**: **Discovery ticket** — (1) Conduct a 2-week audit of the churn channel and CS channel for AM requests that are purely operational config changes. (2) Categorise by action type — which are the most frequent? Party size, NCI, fee waivers, hours? (3) Map each against current Hub / Partner Portal capabilities — what exists but is undiscoverable vs what genuinely doesn't exist? (4) Fee waivers in particular seem like they should be within AM authority in Hub rather than requiring CS intervention.

---

### 5. AM Vacation Coverage Gaps Are Creating Escalation Black Holes

**Heat**: 🟡 **MEDIUM**
**Signal count**: 4+ incidents, 1 source (CS/AM ops channel)
**Recurrence**: **NEW** (concentrated this week, likely Easter holiday pattern)
**Lifecycle**: NEW — cap at Medium heat regardless of volume

**Problem statement**: CS agents repeatedly surfaced this week that they cannot route tickets or escalate venue issues when the assigned AM is on vacation. Three different CS agents asked the channel who to assign tickets to for three different AMs on leave. More acutely: The Nuns' Pool reached out saying they have contacted EatClub multiple times about removing their venue — their AM is on vacation and no one is acting. This is a direct churn/escalation risk. The system has no fallback routing for AM absence.

**Mom Test quality**: **MEDIUM** — CS asking "who do I assign tickets to" is operational frustration but not a venue-direct signal. The Nuns' Pool situation is STRONG — multiple contacts with no resolution, confirmed AM unavailability.

**OKR**: OKR 1 (AM Optimisation) — AM absence creates cascading manual work for CS. OKR 3 (Churn Reduction) — The Nuns' Pool is an active risk.

**OST branch**: AM optimisation → System automation opportunities; Churn reduction → AM relationship (responsiveness)

**Journey stage**: AM relationship → potential churn decision (The Nuns' Pool)

**Recommended action**: **Watch + immediate escalation for The Nuns' Pool** — (1) The Nuns' Pool needs to be actioned today — who is the covering AM? (2) Is there a holiday coverage protocol? Does HubSpot have an "AM away" routing rule? (3) If this is post-Easter clustering, track whether it resolves next week. If not, it's a process gap worth a discovery ticket.

---

### 6. iOS Deal Visibility Bug — 5-Month Unresolved Fault (Masala Flames)

**Heat**: 🟡 **MEDIUM**
**Signal count**: 1 venue (named), additional unnamed scope likely, 1 source (incidents channel)
**Recurrence**: **CHRONIC** (5 months by venue report)
**Lifecycle**: CHRONIC — add +2 to base heat score

**Problem statement**: Masala Flames Indian Cuisine (6A3A7879-EACD-4ACF-BA44-770D4608CF9C) has had their dine-in deals not displaying on the iOS app for 5 months. The deals show on desktop but not on any iOS device. The technical note surfaced is: "Partner Signup not found for restaurant ID." The AM re-added their deals which did not resolve the issue. This venue has been invisible to every EatClub iOS user for 5 months — a silent revenue loss the venue likely doesn't fully understand. The "Partner Signup not found" error suggests a data integrity issue in the venue's account record that likely affects a class of venues, not just Masala Flames.

**Mom Test quality**: **STRONG** — "this issue has been on going for 5 months." Specific platform (iOS vs desktop), specific error message surfaced.

**OKR**: OKR 2 (Deal Performance) — a venue whose deals are invisible to iOS cannot generate revenue from the platform. OKR 3 (Churn Reduction) — a venue generating no value from the platform is at high churn risk.

**OST branch**: Churn reduction → Friction in core venue experience; Deal performance → Venue-led revenue actions

**Journey stage**: Ongoing engagement (completely blocked)

**Recommended action**: **Investigate + escalate to engineering** — (1) Query the venue database for all records with "Partner Signup not found" status — this is a data integrity issue that may affect many venues silently. (2) Masala Flames AM needs an immediate workaround and a timeline. (3) Why did re-adding deals not resolve this? The error is at account level, not deal level.

---

## 📋 All Signals This Week — Classified

| Signal summary | Source | Author team | Who affected | Mom Test quality | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|
| Rice Paper Scissors Fitzroy: disabled deals, stayed live over Easter | Incidents | AM | Venue | STRONG | OKR 2, OKR 3 | Deal settings reverting | Deal score visibility and trust |
| Taketori Fusion Japanese: removed 30%s + schedule, both reverted to onboarding setup | Incidents | AM | Venue | STRONG | OKR 2, OKR 3 | Deal settings reverting | Deal score visibility and trust |
| Lumen Alley: deals changed without intervention, 2nd time (now churned) | Incidents + Churn | AM | Venue | STRONG | OKR 2, OKR 3 | Deal settings reverting + Customer quality | Friction in core venue experience |
| Ombre Italian Newstead: TA order when offers were turned off | Incidents | AM | Venue | STRONG | OKR 2 | Deal settings reverting | Deal score visibility and trust |
| La Botte Pizza Pascoe Vale: ~$200 lost, website bookings + large parties + TA on dine-in, dropped deals, threatening to leave | CS | AM | Venue | STRONG | OKR 2, OKR 3 | Customer quality / T&C abuse | Friction in core venue experience |
| Plat Coffee: churned — "low quality customers who only cared about discount" | Churn | AM | Venue | STRONG | OKR 3 | Customer quality / T&C abuse | Friction in core venue experience |
| Lumen Alley: early churn — customers doing wrong thing in first 2 weeks | Churn | AM | Venue | STRONG | OKR 3 | Customer quality / T&C abuse | Friction in core venue experience |
| Est Ovest: customer used dine-in 30% voucher for takeaway via phone order | CS | AM | Venue / Customer | MEDIUM | OKR 2 | Customer quality / T&C abuse | Friction in core venue experience |
| Gilbees Wine Bar: customer broke T&Cs on Friday night booking | CS | AM | Venue / Customer | MEDIUM | OKR 2 | Customer quality / T&C abuse | Friction in core venue experience |
| Earlwood Izakaya: pause — "booking before dining", commission on full-pay, no direct sales rep | Pause alerts | System bot | Venue | MEDIUM | OKR 2, OKR 3 | Customer quality / T&C abuse | Friction in core venue experience |
| Nanyang Kitchen: customer tap declined, left without paying $54.81 | CS | AM | Venue | MEDIUM | OKR 3 | Customer quality / T&C abuse | Friction in core venue experience |
| Jak's Group: 7 venues churned — company in liquidation | Churn | AM | Group / 7 venues | STRONG | OKR 3 | Sold-business / insolvency | Product fit for enterprise / Groups |
| 7 venues paused citing "sold business" (Lil Hut x3, Little Lebanon x2, Hibiscus Tree, Souvlaki GR) | Pause alerts | System bot | 7 venues | STRONG | OKR 3 | Sold-business / insolvency | — |
| Cony's Bar: voluntary administration, outstanding debt | Churn | AM | Venue | STRONG | OKR 3 | Sold-business / insolvency | — |
| TacoBar Seaford: cost of living / fuel, paused 2 weeks no difference, churned | Churn | AM | Venue | STRONG | OKR 3 | Economic pressure | — |
| Riwayat: fees too high, fuel prices (pause + fee waiver saved) | Churn + Pause alerts | AM + System bot | Venue | STRONG | OKR 3 | Economic pressure | — |
| Jumi's Cafe: financial difficulties, early churn | Churn | AM | Venue | MEDIUM | OKR 3 | Economic pressure | — |
| Subway Crows Nest: financial difficulty, pause | Pause alerts | System bot | Venue | MEDIUM | OKR 3 | Economic pressure | — |
| Bumbles Cafe: party size change request (manual) | Churn | AM | AM | STRONG (behavioral) | OKR 1 | Manual AM work from Hub gaps | Manual AM task reduction |
| Walrus Waverley: 2 manual requests (party size + NCI toggle) | Churn | AM | AM | STRONG (behavioral) | OKR 1 | Manual AM work from Hub gaps | Manual AM task reduction |
| Riwayat: membership fee waiver request (manual) | Churn | AM | AM | STRONG (behavioral) | OKR 1 | Manual AM work from Hub gaps | Manual AM task reduction |
| Mama Made Roti: opening hours change via CS | CS | CS | AM | STRONG (behavioral) | OKR 1 | Manual AM work from Hub gaps | Venue self-serve capability |
| The Nuns' Pool: contacted multiple times about venue removal, AM on vacation | CS | CS | Venue | STRONG | OKR 3, OKR 1 | AM vacation coverage gap | AM relationship / responsiveness |
| CS asking 3x who to assign tickets to — AMs on vacation | CS | CS | CS | MEDIUM | OKR 1 | AM vacation coverage gap | System automation opportunities |
| Masala Flames: iOS deals not showing, 5 months, Partner Signup not found error | Incidents | AM | Venue | STRONG | OKR 2, OKR 3 | iOS deal visibility bug | Friction in core venue experience |
| "Live now" filter showing irrelevant venues | Incidents | AM | Venue/Consumer | MEDIUM | OKR 2 | App display bug | Deal score visibility and trust |
| Alexander Mediterranean: $266 debt, unable to contact, churn | Churn | AM | Venue | STRONG | OKR 3 | Debt / non-contact | — |
| Man-O-Salwa: $969.35 debt, blocked EC bank transactions | Churn | AM | Venue | STRONG | OKR 3 | Debt / non-contact | — |
| Roseberry Street Cafe: margins impacted, ALL retention offers declined, churned | Churn | AM | Venue | STRONG | OKR 3 | Economic pressure | — |
| Garibaldi Pizzeria: urgent customer complaint, owner Angie calling repeatedly | CS | AM | Venue | STRONG | OKR 3 | Customer quality / AM responsiveness | AM relationship |
| Bittersweet: technical issues, wouldn't reconsider even if resolved | Pause alerts | System bot | Venue | MEDIUM | OKR 3 | Technical trust | — |
| Specialty Cafetiere: "can't see transactions on till" — pause | Pause alerts | System bot | Venue | MEDIUM | OKR 2 | Technical / visibility gap | Deal score visibility and trust |

---

## 🗺️ OST Update

### OKR 1 Root — AM Optimisation

**Manual AM task reduction**
- Strengthened: 5 manual Hub requests this week (party size, NCI, fee waiver, hours) are direct evidence. The Walrus Waverley required two separate requests from one AM for one venue. This is the baseline state, not an edge case.
- New sub-opportunity identified: Fee waivers as AM authority. Currently requires CS/ops. Should be within AM capability in Hub with guardrails (e.g., max 3 months, requires Luke approval above a threshold).

**System automation opportunities**
- Strengthened: AM vacation routing is manual and broken. The Nuns' Pool situation is a direct churn risk created by an automation gap.
- Question open: Does Hub currently show AM availability status? If not, that's a prerequisite for any routing logic.

**Venue self-serve capability**
- Weakened this week: No new evidence of venues successfully self-serving in Partner Portal. The Earlwood Izakaya pause note specifically mentions "no direct sales representative to speak to" — suggesting venues don't know where to go.

---

### OKR 2 Root — Deal Performance

**Deal score visibility and trust**
- Significantly weakened: Four venues confirmed their deal settings were ignored by the platform over Easter. If venues can't trust that their configuration choices are honoured, they will stop making configuration choices. La Botte Pizza has already demonstrated this: customer quality issues → dropped deal depth 25/30→20 → threatening to leave. The causal chain from deal unreliability to lower deal scores is direct.
- Open question: Do affected venues have visibility into an audit log? If not, the distrust is compounded by inability to self-diagnose.

**Partner Portal engagement / Venue-led revenue actions**
- No direct signals this week (no Mixpanel data available). The customer quality signals suggest some venues are actively disengaging from deal management (reducing depth, stopping deals) — but motivation is external, not product friction.

---

### OKR 3 Root — Churn Reduction

**Friction in core venue experience**
- Significantly elevated: Deal settings reliability is now a direct friction signal with named venues and confirmed churn. Masala Flames has been invisible on iOS for 5 months — this is a deep-friction state.

**Product fit for enterprise / Groups**
- Strengthened (negative): Jak's Group = 7 simultaneous venue churns due to company liquidation. No group-level relationship layer, no early warning. Consistent with W16 finding that group churn is chronic.

**AM relationship (responsiveness)**
- Weakened this week: The Nuns' Pool contacted multiple times with no response due to AM absence. Garibaldi Pizzeria escalating urgently through multiple channels. Earlwood Izakaya explicitly noting "no direct sales representative to speak to." This is a perception problem as much as an operational one.

---

## ⚠️ Friction Stack Watch

### 🔴 Lumen Alley Coffee & Bagels — CONFIRMED CHURN, FRICTION STACK
**restID**: B0A4E510-B0D2-4892-A311-5066FCA654F4
**Signals across sources**:
- Incidents channel: Deals changing without intervention over Easter, second time this has happened
- Churn channel: Early churn — customers doing the wrong thing in first 2 weeks, not happy with platform, referred to BDM still not interested
**Analysis**: This is a completed friction stack. The venue entered the platform with a difficult customer quality experience AND experienced repeated deal reliability failures. Neither was resolved. The deal settings bug may have made the customer quality problem worse (offers running when they shouldn't = more opportunity for misuse). Flag to engineering to determine if the deal reliability failure is one of the confirmed Easter bugs.

---

### 🔴 The Nuns' Pool — ACTIVE ESCALATION RISK
**restID**: Not provided in signals
**Signals across sources**:
- CS channel: Venue contacted EatClub multiple times requesting removal, AM on vacation, no action taken
**Analysis**: A venue trying to leave that is being ignored due to AM absence. Every unanswered contact increases churn hostility and reputational risk. Requires immediate coverage assignment and response today.

---

### 🟡 La Botte Pizza — Pascoe Vale — ACTIVE CHURN RISK
**restID**: DB6BD926-E4E9-4884-919A-725DD772E9BC
**Signals across sources**:
- CS channel: T&C abuse causing financial loss, deal depth reduced, threatening to leave
**Analysis**: Owner is still present and engaged but expressing clear distress. Has already taken unilateral action (reduced deals). Is asking for CS to contact specific customers — this is a venue still trying to make it work. Window is open. Escalate to AM.

---

### 🟡 Riwayat — Traditional Pakistani Feast — WATCH
**restID**: BC57B7B9-59BF-46C3-A75C-A92854BFCE2A
**Signals across sources**:
- Pause alerts: Self-paused citing fees too high, fuel prices
- Churn channel: Pause saved with 3-month membership fee waiver, meeting scheduled for July
**Analysis**: Multi-source, fee sensitivity confirmed. Saved for now but the underlying economics concern is real. The July meeting is the key retention checkpoint. Note for AM to prepare a value demonstration before that call.

---

### 🟡 Alexander Mediterranean Restaurant — Gladesville — CHURN RISK + DEBT
**restID**: 7D4929E5-5BD1-4A10-9808-B95244B38A95
**Signals**: Churn channel — $266 outstanding balance, multiple contact attempts failed, churn requested
**Analysis**: 14+ day silence + debt = critical churn signals per the model. Churn has been requested but not yet confirmed executed. If outstanding balance, escalate to Nancy/Amor for debt recovery.

---

## 💡 Synthesis Notes

**What surprised me this week:**

1. The Easter long weekend produced a cluster of deal reliability failures that the individual AM reports in isolation might not trigger an engineering escalation. Looking across 4 simultaneous reports — Rice Paper Scissors, Taketori, Lumen Alley, Ombre Italian — this is clearly a systemic issue with how the platform handles schedule overrides and public holiday deal logic. The fact that Lumen Alley's AM noted "this is the second time" confirms it's not a one-off. This deserves an engineering post-mortem.

2. The customer quality theme is louder this week than in prior weeks. Six venues across two channels surfacing T&C abuse in a single week — and three of those venues are in churn or pre-churn states — suggests the manual CS escalation workflow (AM asks CS to call customer) is not resolving the underlying problem. The question is whether there's a systemic detection mechanism possible at redemption time.

3. The "sold business" volume is striking — 7 venues in pause alerts alone, plus Jak's Group (7 venues, liquidation). This may be a post-Easter macro signal. Worth watching over next 2–3 weeks to determine if it's a trend or a spike.

**What is missing:**

- Granola meeting transcripts: absent this run. Any AM, BDM, or leadership meetings this week discussing deal reliability post-Easter, the La Botte situation, or the Jak's Group would significantly sharpen the deal settings bug theme and the customer quality theme.
- HubSpot: no CS ticket data. The volume of T&C breach contacts is unknown — CS may be handling 20 per week or 200 per week. This changes the sizing of Theme 2 significantly.
- Deal Score CSV: without it, we can't see how many venues are currently at zero score, or whether the La Botte deal depth reduction (25/30→20) shows up in the score trend.
- Mixpanel: no Partner Portal engagement data. Can't assess whether venues are self-serving any of the actions they're currently asking AMs to do manually.

**Interview questions to sharpen the weakest signals:**

*For the deal settings reverting bug (currently STRONG, but causation unclear):*
- "Walk me through exactly what you did before the Easter weekend and what you expected to happen."
- "When did you first notice the deals were running? What triggered you to check?"
- "Has this happened before, outside of the Easter period?"

*For the customer quality theme (currently STRONG, but systemic scope unknown):*
- "How often does this happen in a typical week at your venue?"
- "What do you do when a customer tries to use an offer incorrectly? Walk me through the last time it happened."
- "If EatClub could automatically prevent a customer from using a dine-in offer for takeaway — would that solve the problem, or is it more than that?"

*For AM vacation coverage (currently MEDIUM, needs depth):*
- "What do you do when you're going on leave? Is there a formal handover process?"
- "Has a venue ever churned while you were on leave that you think might have been prevented?"

**What would move OKR 1 most based on this week's signals:**

The five manual Hub request types identified this week (party size, NCI toggle, fee waiver, opening hours, membership fee) are the most direct OKR 1 evidence available. A Partner Portal or Hub audit of which actions generate the most Slack requests would immediately reveal the highest-leverage self-serve build. Fee waivers specifically are a retention tool that is currently gatekept behind CS — giving AMs direct authority in Hub would speed save conversions.

**What would move OKR 2 most based on this week's signals:**

Fixing the deal settings reliability bug (deals reverting, running when disabled) is prerequisite to OKR 2. Venues will not confidently manage deals through Partner Portal if they don't trust the platform to honour their choices. The iOS deal visibility bug (Masala Flames, 5 months) is a silent OKR 2 failure — those venues appear to be engaged but are generating zero consumer impressions.

---

## Routing Block

```routing
{
  "jira_tickets": [
    {
      "theme": "Deal settings reverting / ignoring venue choices",
      "okr": "OKR 2 + OKR 3",
      "problem_statement": "Venues configuring deal settings (disabling deals, removing offers, adjusting schedules) are finding those choices ignored or overridden — particularly around public holidays. Confirmed instances: Rice Paper Scissors Fitzroy, Taketori Fusion Japanese, Lumen Alley (2nd occurrence), Ombre Italian Newstead. Root cause unknown; potential issue with holiday hours override logic or schedule conflict resolution. Engineering post-mortem required."
    },
    {
      "theme": "Customer quality / T&C abuse destroying venue deal economics",
      "okr": "OKR 2 + OKR 3",
      "problem_statement": "Venues are losing margin to customers circumventing offer terms (dine-in vouchers for takeaway, website bookings with oversized parties, non-payment). Current response is CS manually contacting individual customers — not scalable. Confirmed churn signals: Plat Coffee, Lumen Alley. Active risk: La Botte Pizza. Discovery needed on detection rate, CS volume, and whether system-level enforcement is possible at redemption."
    },
    {
      "theme": "Manual AM work from Hub limitations — party size, NCI, fee waivers, hours",
      "okr": "OKR 1",
      "problem_statement": "AMs are using the Slack churn channel as a request queue for routine venue configuration changes not supported self-serve in Hub or Partner Portal. Recurring action types this week: max party size (x2), NCI toggle, membership fee waiver, opening hours. Audit of 2-week channel history needed to size; each type should be mapped to Hub/Portal capability gap."
    }
  ],
  "interview_questions": [
    {
      "theme": "AM vacation coverage gaps — system has no fallback routing",
      "questions": [
        "What do you do when you're going on leave — is there a formal handover process?",
        "Has a venue ever escalated or churned while you were away that might have been prevented?",
        "What would good AM coverage during leave look like to you — a backup AM, a CS routing rule, something else?"
      ]
    },
    {
      "theme": "iOS deal visibility bug — Masala Flames 5-month fault",
      "questions": [
        "When did you first notice the deals weren't showing on iOS?",
        "Have you received any communication from EatClub about this in the last 5 months?",
        "How has this affected your redemption volume — do you have a sense of how many customers you've missed?"
      ]
    }
  ],
  "friction_alerts": [
    {
      "venue": "Lumen Alley Coffee & Bagels",
      "rest_id": "B0A4E510-B0D2-4892-A311-5066FCA654F4",
      "signals": [
        "Early churn — customers doing the wrong thing in first 2 weeks, referred to BDM still not interested",
        "Incidents channel — deals changing without intervention over Easter, second time this has occurred",
        "Two-source, two-stage friction stack: customer quality + deal reliability failure"
      ]
    },
    {
      "venue": "The Nuns' Pool",
      "rest_id": "unknown",
      "signals": [
        "CS channel — venue contacted multiple times requesting removal, AM on vacation, no action",
        "Active escalation risk — requires same-day response"
      ]
    },
    {
      "venue": "La Botte Pizza - Pascoe Vale",
      "rest_id": "DB6BD926-E4E9-4884-919A-725DD772E9BC",
      "signals": [
        "CS channel — T&C abuse causing ~$200 loss in one week",
        "Owner dropped all deals from 25%/30% to 20% unilaterally",
        "Threatening to leave — window still open"
      ]
    },
    {
      "venue": "Alexander Mediterranean Restaurant - Gladesville",
      "rest_id": "7D4929E5-5BD1-4A10-9808-B95244B38A95",
      "signals": [
        "Churn channel — $266 outstanding balance, multiple contact attempts failed",
        "14+ day silence + debt = critical churn signal per model"
      ]
    },
    {
      "venue": "Masala Flames Indian Cuisine",
      "rest_id": "6A3A7879-EACD-4ACF-BA44-770D4608CF9C",
      "signals": [
        "Incidents channel — iOS deals not showing for 5 months",
        "Error: Partner Signup not found for restaurant ID",
        "Silent OKR 2 failure — zero iOS impressions for extended period"
      ]
    }
  ],
  "watch_list": [
    "Jak's Group new operators — 7 venues, BDM attempting to repitch. Active save window.",
    "Riwayat - Traditional Pakistani Feast (BC57B7B9) — saved with 3-month fee waiver, July meeting set. AM to prepare value demonstration before July.",
    "Sold-business churn cluster (7 venues in pause alerts) — monitor next 2 weeks for trend vs spike",
    "Easter long weekend deal reliability bug — watch for additional AM reports this week as AMs return from leave",
    "Bittersweet (5C2ED178) — paused for technical issues, explicitly said would not reconsider even if resolved. Low probability save but worth one CS contact.",
    "Garibaldi Pizzeria — Angie urgently contacting multiple channels. Ensure ticket is resolved and AM follows up directly.",
    "Earlwood Izakaya (ADDA7FB0) — 'no direct sales representative to speak to' is both a product signal (discoverability) and a churn signal."
  ]
}
```
