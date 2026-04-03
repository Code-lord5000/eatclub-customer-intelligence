# Synthesis Log — 2026-04-01 (Run 4)

**Period covered**: 2026-03-30 → 2026-04-01
**Run number**: 4 (W15)
**Prior run**: 2026-03-31-synthesis.md

---

## Signal counts by source

| Source | Signals | Notes |
|---|---|---|
| Slack #churned_or_changed | 28 | RECORD VOLUME — 28 churned/churning venues with reasons |
| Slack #urgent | 15+ | ECPay bot alerts + partner portal deal change requests |
| Slack #ecpayuk-ops | 5 | UK payment failures: Pasta Nostra, The Sea The Sea, Hungry Taco |
| Slack hidden signals | 4 | Luke HubSpot export pain, Ngon workaround, form save failures, RCI limitation |
| Sam Benjamin | 0 | No messages this period (2nd consecutive) |
| Granola | 10 | VERY RICH — onboarding cost quantified ($200k), bookings launch, menu AI, system fragmentation, UK launch |
| HubSpot tickets | 200 | Analyzed: cold call 22.5%, training 17.5%, IAO menu 12%, billing 7.5%, card issues 6%, refunds 3.5% |
| HubSpot deals | 0 | Same old closed-lost records (Hut & Soul, Nomad, Dosa Hut, Tarboosh). 6th run with zero useful deal signal. |
| HubSpot notes | 1 | Memby — avoidant behaviour signal |
| Jira SD | — | Pulled via Atlassian MCP |
| Mixpanel | ✅ SUCCESS | Partner Portal: offer disabled UP 48% (449→667/day). Consumer: deal sharing healthy (500-853/day). |
| **Total** | **~98** | UP from ~81. Record churn volume + Mixpanel success + rich Granola. |

---

## Themes identified

### 1. BDM Signing Quality — 12/12 (CRITICAL, CHRONIC, 5th run)
**New signals this period:**
- Ice Bar/Mirror Bar: POOR ICP — experience venues with entry fees, customers arrive to discover fee. Pippa tried everything. (Slack #churned, Mar 31)
- Taxiboat: 3rd time churning. Owner screening calls. "Not happy with EC's policies." Kane advised blacklist. (Slack #churned, Mar 31)
- Pokkoi Kitchen: FAILED SAVE — was performing well. F2F cancelled last minute. BDM + Emma escalation failed. (Slack #churned, Mar 31)
- X74: Cost of living pressure — can't afford EC. May rejoin in 6 months. (Slack #churned, Mar 31)
- GT's Bar Noosa: Customer reporting failures + double dipping + no integration + early churn. (Slack #churned, Mar 31)
- Kumbira Cafe: Settlement misunderstanding — part-owner thinks EC taking all money. BDM Dylan explained multiple times. (Slack #churned, Mar 31)
- Subway Prahran: Pricing dispute. Won't increase deals unless inflated pricing allowed. (Slack #churned, Mar 31)
- Bright Star Cafe: Early churn, owner unresponsive, not ICP. (Slack #churned, Mar 31)
- Burgertory: Franchise fees increasing, selling. (Slack #churned, Mar 31)
- Mr. Wu Dumpling Bar: Debt collectors, weeks of chasing. (Slack #churned, Mar 31)
- 8+ venue sales/closures: Magic of India, Hot Yum Pot, Bomba, FlameNFork, Fresh Cafe, Isla Bar, Goodhope, Mr Burch (Slack #churned, Mar 31)
- Granola: Onboarding efficiency crisis quantified — $200k annual FTE cost, 30hrs/week manual process, banking details don't auto-populate, map markers error-prone, 3 conflicting sources for hours. (Granola, Mar 30-31)
- Granola: Menu digitization — 6 offshore staff, 10% incorrect, Charlie has AI scraping solution not yet integrated. (Granola, Mar 30-31)
**Sources**: 3+ (Slack #churned, Granola, HubSpot)
**Mom Test**: STRONG — specific past behaviours, quantified costs, failed saves
**Delivery status**: ZERO JIRA COVERAGE — DELIVERY GAP (5th consecutive run)
**Action**: Card updated, remains ready-to-raise. HIGHEST PRIORITY.

### 2. Venue Deal Control — 11/12 (SUSTAINED, MIXPANEL CONFIRMED)
**New signals:**
- Ngon Brisbane: Bypassing recurring offers entirely — will "create offers manually" (WORKAROUND signal)
- Partner Portal RCI limitation: Can't select specific time slots. Kane blocked.
- GT's Bar: Double dipping + no integration
- **Mixpanel: Offer disabled events UP 48% over 7 days (449→667/day)** — BEHAVIOURAL CONFIRMATION
- Continuing high volume of ECPay bot deal edit/delete alerts
- HubSpot: 5 deal-related tickets (offers + change/delete)
**Sources**: 4 (Slack, Mixpanel, HubSpot, Jira SD)
**Mom Test**: STRONG
**Delivery status**: IDEA-356 in Concept only — NOT in Discovery
**Action**: Card updated, heat sustained at 11/12. Mixpanel corroboration is HIGH confidence.

### 3. Bookings Launch Risk — UP to 9/12 (LAUNCHED TODAY!)
**New signals:**
- **LAUNCHED TODAY (April 1)** with settlement integration incomplete
- UK cities (Leeds, Cardiff, Liverpool) launching simultaneously with incomplete processes
- No dedicated PM (just Simone), product team not involved in discovery
- Enablement session needed but not yet scheduled
- Comparison to OpenTable problematic — feature gaps acknowledged
**Sources**: 2 (Granola, inferred from timing)
**Mom Test**: STRONG
**Delivery status**: REST-71/66/70/68 (Obee integration) In Progress
**Action**: Card updated, heat UP to 9/12. Monitor post-launch signals urgently.

### 4. EC Card Payment Reliability — 9/12 (STABLE)
**New signals:**
- UK failures: Pasta Nostra (FAILED AUTH), The Sea The Sea (insufficient funds), Hungry Taco (duplicate)
- HubSpot: 12 payment-related tickets (card setup 7, payment issues 4, declined 1)
- Card missing issues (Roxanne at Callooh Callay Shoreditch)
**Matches SMS baseline B1**: ~172 CS interventions/day CHRONIC

### 5. T&C Friction & Venue Trust — 8/12 (STABLE)
- Subway Prahran: Pricing manipulation attempt (inflated pricing for deals)
- Ice Bar/Mirror Bar: ICP mismatch with discount model
- No new explicit T&C enforcement signals
- Stable at 8/12

### 6. Support Response Time — 9/12 (STABLE)
- GT's Bar: Reports customers but doesn't receive responses
- HubSpot: 200 tickets in 48hrs — sustained CS volume
- Stable

### 7. Deal Score Trust — 11/12 (COOLING, 2nd run no signals)
- No new signals (2nd consecutive run)
- REST-229/235/236 shipped — may be addressing

### 8. Commission Dispute — 8/12 (COOLING)
- No new signals
- IDEA-344/348/349 in Discovery (Q2)

### 9. Settlement Payment Failures — 8/12 (STABLE)
- Kumbira: Settlement misunderstanding — part-owner thinks EC taking all money
- Granola: Bookings settlement integration incomplete
- IDEA-291 in Discovery

### EMERGING: Venue Mortality / Market Pressure — 6/12 (2nd run)
- 8+ venue sales/closures this period (2nd consecutive run with this volume)
- Cost of living explicitly cited (X74)
- Mr. Wu Dumpling Bar in collections
- Burgertory franchise fees increasing
- May be Easter seasonal effect OR accelerating market pressure
- Not yet a problem card — monitoring for 3rd run recurrence

---

## Hidden signals

| Type | Signal | Venues/AMs | Implication |
|---|---|---|---|
| Workaround | Luke DM to Adam: "we should've built an export for hubspot for every venue. It'd update all this information in one go" | Luke Maurel | Manual HubSpot venue data sync — no automated pipeline between systems |
| Workaround | Ngon Brisbane: Bypassing recurring offers, will "create offers manually" | Ngon (venue) | Recurring offer feature being actively avoided — product gap |
| Normalised pain | Partner Portal RCI: Can't select specific time slots. Kane: "if its RCI - venue has to do it through partner portal" | Kane Russell, venues | Known limitation treated as normal — RCI time control fundamentally broken |
| Technical friction | Ashish: Venue onboarding form save failures for Olive Oil & Butter. Needed rollback to fix. | Ashish (dev), venue | Onboarding form has bugs requiring engineering intervention |
| Post-churn leak | BB Thai Town + Little Bangkok STILL receiving offerless transactions. Loyalty removal requested. | Gabriella (AM) | REPEAT from Run 3 — churned venues not properly disconnected (CHRONIC) |
| Volume anomaly | 8+ venue closures/sales this period (2nd consecutive run) | Multiple | Easter period? Or accelerating venue mortality in Australian market? |

---

## Friction stack alerts

| Venue | Sources | Signal types | Risk level |
|---|---|---|---|
| GT's Bar Noosa | #churned_or_changed | Customer reporting failures + double dipping + no integration + early churn | 🚨 CRITICAL — multi-vector failure |
| Kumbira Cafe | #churned_or_changed | Settlement misunderstanding + doesn't want weekend deals + partner disagreement | 🔴 HIGH |
| Subway Prahran | #churned_or_changed | Pricing dispute + refuses solutions + only 1 deal + saved in Nov now deteriorating | 🔴 HIGH |
| Ice Bar/Mirror Bar | #churned_or_changed | ICP mismatch + entry fees + majority redemptions unclaimed + failed save | 🔴 HIGH — BDM should never have signed |

---

## Drift detection

| Theme | Direction | Runs tracked | Signal trend | Action |
|---|---|---|---|---|
| BDM Signing Quality | 🔴 Accelerating | 5 (run 0→4) | 10→10→12→12→12 | ESCALATE — 5th run ZERO delivery coverage. RECORD churn volume. |
| Venue Deal Control | 🔴 Accelerating | 5 (run 0→4) | 8→8→10→11→11 | ESCALATE — Mixpanel CONFIRMS rising disables (+48%). IDEA-356 still Concept. |
| Bookings Launch Risk | 🔴 Critical | 2 (run 3→4) | —→7→9 | LAUNCHED TODAY — monitor urgently |
| T&C Friction | 🟡 Stable | 4 (run 1→4) | —→7→8→8 | Watch |
| EC Card Reliability | 🟡 Stable | 4 (run 1→4) | —→9→9→9 | Watch — CHRONIC per SMS baseline |
| Support Response | 🟡 Stable | 4 (run 1→4) | —→9→9→9 | Watch |
| Deal Score Trust | 🟢 Cooling | 5 (run 0→4) | 11→11→11→11→11 (no new signals 2 runs) | Watch — REST shipped |
| Commission Dispute | 🟢 Cooling | 4 (run 0→4) | 8→8→8→8 (no new signals) | Watch — IDEA in Discovery |
| Settlement Failures | 🟡 Stable | 5 (run 0→4) | 8→8→8→8→8 | Watch — new bookings settlement signal |
| Venue Mortality | 🟡 Emerging | 2 (run 3→4) | —→5→6 | Monitor — 3rd run = pattern |

---

## Delivery context map

**BEING BUILT NOW**: REST-71/66/70/68 (Bookings/Obee), REST-243/244 (Customer.io survey), REST-21 (Venue signup VGS), REST-189 (Region selector), REST-48 (Audience Targeting v2), REST-183/207 (Grow DB)
**IN DISCOVERY**: IDEA-344/348/349 (AM tooling Q2), IDEA-329 (Groups), IDEA-291 (Net Settlement)
**IN CONCEPT**: IDEA-356 (Portal self-serve), IDEA-355 (Double-dipping), IDEA-350/351 (T&C enforcement), IDEA-354 (Venue closure), IDEA-352 (Payment reconciliation)
**NO COVERAGE**: BDM Signing Quality (12/12 heat, 5 runs), Venue Mortality/Market Pressure (emerging)

---

## Mixpanel status
- **Endpoints used**: mcp__3e1b458b (standard) and mcp__d1218b36 (EU)
- **Partner Portal (3834354)**: ✅ SUCCESS
  - Offer disabled: 449→667/day over 7 days (UP 48%) — HIGH confidence
  - Offer edited: 273-383/day — stable
  - Offer deleted: 0-56/day — low, spike on 3/27
  - Campaign disables: Very low (1-2 events) — possible instrumentation gap or rarely used
- **Consumer Apps (3747444)**: ✅ SUCCESS
  - Deal sharing confirmations: 500-853/day — healthy consumer engagement
- **Status**: ✅ First successful Mixpanel run — behavioural layer active
- **Key finding**: Rising offer disable rate CORROBORATES venue deal control qualitative signals (HIGH confidence)

---

## HubSpot helpdesk summary

```
HUBSPOT HELPDESK SUMMARY — Mar 30-Apr 1
Total tickets: 200 (created or updated in 48hrs)

CATEGORY BREAKDOWN:
Cold call - no meeting:  45 (22.5%) — BDM activity, not product signal
3 Day Training:          35 (17.5%) — onboarding process
IAO Menu:                24 (12.0%) — menu setup demand
Demo apps:               20 (10.0%) — sales enablement
Billing Issues:          15 (7.5%)  — payment friction
EC Card setup:            7 (3.5%)  — card friction
Refund Requests:          7 (3.5%)  — customer dissatisfaction
Closed Restaurant:        5 (2.5%)  — churn
Deal not honoured:        5 (2.5%)  — T&C signal
EatClub Card payment:     4 (2.0%)  — card friction
Offers:                   4 (2.0%)  — deal control
Other/misc:              29 (14.5%) — includes General Enquiry, Special Occasion, etc.

VOLUME FLAG: Unable to compare vs prior period (no prior HubSpot ticket baseline in synthesis logs)

RECURRING VENUES:
- None detected in this period (cross-reference limited)

CHURN INTENT TICKETS:
- 5 "Closed Restaurant" tickets — cross-ref with Slack churned data

STRONGEST PROBLEM LANGUAGE:
- "Payment gets decline" — Card declined
- "Double Charge - Refund Request - Everest MoMo Station" — Billing
- "Refund Request for Incorrectly Charged Payment" — Billing
- Memby note: "has been very avoidant again. Had meeting booked for last week but he kept saying not today as he's too busy..." — Venue evasion
```

---

## Cards created or updated

- Updated: PROBLEM-bdm-signing-quality.md (14 new signals, heat sustained 12/12, $200k cost quantified)
- Updated: PROBLEM-venue-deal-control.md (6 new signals incl. Mixpanel, heat sustained 11/12)
- Updated: PROBLEM-bookings-launch-risk.md (5 new signals, heat UP 7→9, LAUNCHED TODAY)
- Stable: PROBLEM-ec-card-payment-reliability.md (new UK failures, 9/12)
- Stable: PROBLEM-tc-friction-venue-trust.md (8/12)
- Stable: PROBLEM-support-response-time.md (9/12)
- Stable: PROBLEM-settlement-payment-failures.md (8/12, new bookings signal)
- Cooling: PROBLEM-deal-score-trust.md (11/12, no new signals 2nd run)
- Cooling: PROBLEM-commission-dispute-process.md (8/12, no new signals)

---

## Open questions for Adam

1. **Bookings LAUNCHED TODAY with known gaps.** Settlement integration incomplete, no AM training, UK cities launching simultaneously. What is the immediate monitoring plan? Should we create a dedicated post-launch signal channel?

2. **BDM Signing Quality: 5th run at 12/12 with ZERO Jira coverage.** This is the longest-running delivery gap in the repo. 28 churned/churning venues this period (RECORD). Granola quantified onboarding cost at $200k annually. Is it time to raise the IDEA ticket?

3. **Mixpanel confirms offer disable rate rising 48% (449→667/day).** This is the first successful Mixpanel run. The behavioural data validates venue deal control signals at HIGH confidence. Combined with Ngon bypassing recurring offers entirely — venues are increasingly giving up on self-serve. Worth escalating IDEA-356 from Concept to Discovery?

4. **8+ venue closures/sales for 2nd consecutive run.** Is this Easter seasonality, or is the Australian restaurant market under accelerating pressure? Worth checking against historical closure rates from AM team.

5. **System fragmentation risk**: Billy, Crilly, Jeroen's AI tools all diverging without governance. Granola flagged need for alignment meeting before Easter. Is this happening?

6. **Post-churn loyalty leak still unresolved**: BB Thai Town + Little Bangkok still receiving offerless transactions (2nd consecutive run). Is there a known disconnection process?
