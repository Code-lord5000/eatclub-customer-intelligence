# Synthesis Log — 2026-03-31 (Run 3)

**Period covered**: 2026-03-29 → 2026-03-31
**Run number**: 3 (W14b)
**Prior run**: 2026-03-30-synthesis-r2.md

---

## Signal counts by source

| Source | Signals | Notes |
|---|---|---|
| Slack #churned_or_changed | 40 | VERY active — primary signal source |
| Slack #urgent | 20 | ECPay alerts + CS venue reports |
| Slack #customer-feedback | 0 | Dead channel — 5th consecutive run |
| Slack #am-team | 0 | Dead channel — 5th consecutive run |
| Slack #cs-am | 0 | Dead channel — 5th consecutive run |
| Sam Benjamin | 0 | No messages this period |
| Granola | 8 | Rich meeting signals — onboarding, bookings, settlement |
| HubSpot tickets | 100 | Analyzed batch: deal confusion 24%, app/tech 17%, churn intent 7% |
| HubSpot deals | 0 | No recent closed-lost — dead source, 5th run |
| Jira SD | 8 | SD-700 to SD-707 |
| Hidden signals | 5 | Post-churn loyalty leak, enterprise inconsistency, triple friction stack |
| Mixpanel | 0 | EU endpoint required, queries failed — behavioural layer absent |
| **Total** | **~81** | |

---

## Themes identified

### 1. BDM Signing Quality — 12/12 (CRITICAL, CHRONIC, 4th run)
**New signals this period:**
- Jaipur Palace: Managers approved deal increases while owner was overseas in Bali. Owner now demands discount reimbursement. (Josephine, #churned, Mar 31)
- Chicci: After two save attempts + Kane's help, only $11 revenue in 2 months. (Nicole, #churned, Mar 31)
- York Street Espresso Bar: AOV $18, TA only, double dipping, can't be integrated. (Jessie, #churned, Mar 31)
- Shila Kitchen: Wrong contract rate — BDM mistake on agreement. (Jenny, #churned, Mar 31)
- Spice Aura: NEW venue — (1) Promised no fees by agent, charged $163; (2) 30% discount too high; (3) Can't delete or reduce offers below 20%. TRIPLE STACK. (CS via #urgent, Mar 31)
- Ravneels Curry House: No results in first month, early churn. (Aaron, #churned, Mar 31)
- Ceylon Girl's Cafe: Owner refused all solutions, struggling financially, cancelling all services including Uber Eats. (Aaron, #churned, Mar 31)
- Cafe De Rolls: Not enough margin, owner trying to sell business. (Josephine, #churned, Mar 31)
- Granola: 30hrs/week manual data entry in onboarding, 10% menus incorrect, map markers error-prone, menu digitization crisis (6 offshore staff)
**Sources**: 3+ (Slack #churned, Slack #urgent, Granola)
**Mom Test**: ALL STRONG — specific past behaviours
**Delivery status**: ZERO JIRA COVERAGE — DELIVERY GAP
**Action**: Card updated, remains ready-to-raise

### 2. Venue Deal Control — 11/12 (UP from 10, ACCELERATING)
**New signals:**
- SD-700: Still open in "Waiting for customer" — venue AND AM can't edit offers (Petit Bistro)
- Spice Aura: Can't delete offers, can't reduce below 20% (#urgent, Mar 31)
- Binny'z Pizza: FOUR consecutive delete attempts for 40% TA offers, reason "badTime" (#urgent, Mar 31)
- Le Feu Oasis: Needs time-based deal control — runs in-house deals until 3pm, wants EC offers only after (#urgent, Mar 31)
- Martina Rose Bay: Request to permanently remove Friday/Saturday offers and change deal timing (#urgent, Mar 31)
- Oden Sake Bar: Reduce pax to 4 per table (#churned, Mar 30)
- Garden State Diner: Complex boost request showing system limitations (#churned, Mar 30)
- 10+ ECPay alerts for offer edit/delete requests from Partner Portal
**Sources**: 3 (Slack #urgent, Slack #churned, SD tickets)
**Mom Test**: STRONG
**Delivery status**: IDEA-356 in Concept only — NOT in Discovery
**Action**: Card updated, heat raised to 11/12

### 3. T&C Friction & Venue Trust — 8/12 (UP from 7, STABLE-TO-ACCELERATING)
**Recurring signals:**
- Hayashi: 2% rebate to prevent churn, "takes a magnifying glass to every T&C breach" (Jai, #churned, Mar 30)
- Como Garden: Same group, dropped from 60k/quarter, 2% rebate (Jai, #churned, Mar 30)
- Little B by Bruno&Co: Regulars using deal for coffee only, AOV $15, owner doesn't see value (Jessie, #churned, Mar 30)
- Ambra Spirits: "EC devalues their offering to their regulars" (Gabi, #churned, Mar 30)
- Maya Lounge: Peak hour redemption upset, seating time reduced to 90min (Elodie, #churned, Mar 30)
**Sources**: 1 (Slack #churned)
**Mom Test**: STRONG
**IDEA-350/351/355 in Concept** — T&C enforcement ideas exist but not in Discovery

### 4. EC Card Payment Reliability — 9/12 (STABLE)
**New signals:**
- SD-707: Kom Coffee + Kom Coffee Roasters Square terminals mapped incorrectly — transactions going to wrong venue, customers charged full amount (Mar 30)
- HubSpot: Multiple card issuance failures, payment declines
**Matches SMS baseline B1**: ~172 CS interventions/day CHRONIC

### 5. Support Response Time — 9/12 (STABLE)
- SD-700 still in "Waiting for customer" — no resolution
- Granola confirmed systemic support gaps

### 6. Deal Score Trust — 11/12 (COOLING)
- No new signals this period
- REST-229/235/236 shipped — may be addressing this

### 7. Commission Dispute — 8/12 (COOLING)
- No new signals
- IDEA-344/348/349 in Discovery (Q2 initiative)

### 8. Settlement Payment Failures — 8/12 (STABLE)
- Granola: Settlement integration incomplete for bookings, SMS billing flow missing (~10¢/message)
- IDEA-291 in Discovery

### NEW: Bookings Launch Risk — 7/12 (NEW)
- Granola: Launching with minimal preparation — no restaurant flow, no design work, built as "black box" with day-before notice
- AMs have 30/month targets but no formal training
- REST-71/66/70/68 (Obee integration) all In Progress
- Sources: 1 (Granola only)
- Mom Test: STRONG

---

## Hidden signals

| Type | Signal | Venues/AMs | Implication |
|---|---|---|---|
| Post-churn leak | BB Thai Town + Little Bangkok: Churned but still receiving offerless loyalty transactions | Gabriella (AM) | Product gap — churned venues not properly disconnected from loyalty |
| Enterprise inconsistency | Gami Chicken & Beer: New Gami venues signed at different rates, AM got "no advice or help from anyone at EatClub" | Tania (AM) | Enterprise/groups management broken — HQ relationships not functioning |
| Triple friction stack | Spice Aura: BDM mis-sold (no fees) + 30% too high + can't control offers — ALL on a brand new venue | CS, Josephine (AM) | Perfect case study of onboarding failure cascading to churn |
| Volume anomaly | 8+ venue closures/sales in 48hrs (Goodhope, Hot Yum Pot, Mr Burch, Fresh Cafe, Isla Bar, Krish Indian, Bomba, Armadela, Purna Kitchen, Chagos) | Multiple AMs | Easter period? Seasonal spike? Or accelerating venue mortality? |
| Venue self-serve broken | Binny'z Pizza: 4 consecutive delete attempts from Partner Portal, all failed with "badTime" | CS | Self-serve portal not functioning for basic operations |

---

## Friction stack alerts

| Venue | Sources | Signal types | Risk level |
|---|---|---|---|
| Spice Aura | #urgent (CS), #churned | BDM mis-sold + discount too high + can't control offers | 🚨 CRITICAL |
| Hayashi + Como Garden | #churned (2 runs) | T&C enforcement + revenue decline + rebate negotiation | 🔴 HIGH |
| Kom Coffee / Kom Coffee Roasters | SD-707 | Square terminal mapping + wrong venue transactions | 🔴 HIGH |

---

## Drift detection

| Theme | Direction | Runs tracked | Signal trend | Action |
|---|---|---|---|---|
| BDM Signing Quality | 🔴 Accelerating | 4 (run 0→3) | 10→10→12→12 | ESCALATE — delivery gap |
| Venue Deal Control | 🔴 Accelerating | 4 (run 0→3) | 8→8→10→11 | ESCALATE — IDEA-356 still Concept only |
| T&C Friction | 🟡 Stable | 3 (run 1→3) | —→7→8 | Watch — same venues recurring |
| EC Card Reliability | 🟡 Stable | 3 (run 1→3) | —→9→9 | Watch — CHRONIC per SMS baseline |
| Support Response | 🟡 Stable | 3 (run 1→3) | —→9→9 | Watch |
| Deal Score Trust | 🟢 Cooling | 4 (run 0→3) | 11→11→11→11 (no new signals) | Watch — REST-229/235/236 shipped |
| Commission Dispute | 🟢 Cooling | 3 (run 0→3) | 8→8→8 (no new signals) | Watch — IDEA-344/348/349 in Discovery |
| Settlement Failures | 🟡 Stable | 4 (run 0→3) | 8→8→8→8 | Watch — IDEA-291 in Discovery |
| Bookings Launch Risk | NEW | 1 | — | Monitor — launch imminent |

---

## Delivery context map

**BEING BUILT NOW**: REST-71/66/70/68 (Bookings/Obee), REST-243/244 (Customer.io survey), REST-21 (Venue signup VGS), REST-189 (Region selector), REST-48 (Audience Targeting v2), REST-183/207 (Grow DB)
**IN DISCOVERY**: IDEA-344/348/349 (AM tooling Q2), IDEA-329 (Groups), IDEA-291 (Net Settlement)
**IN CONCEPT**: IDEA-356 (Portal self-serve), IDEA-355 (Double-dipping), IDEA-350/351 (T&C enforcement), IDEA-354 (Venue closure), IDEA-352 (Payment reconciliation)
**NO COVERAGE**: BDM Signing Quality (12/12 heat, 4 runs)

---

## Cards created or updated

- Updated: PROBLEM-bdm-signing-quality.md (8 new signals)
- Updated: PROBLEM-venue-deal-control.md (7 new signals, heat 10→11)
- Updated: PROBLEM-tc-friction-venue-trust.md (5 recurring signals, heat 7→8)
- Updated: PROBLEM-ec-card-payment-reliability.md (1 new signal)
- Updated: PROBLEM-support-response-time.md (SD-700 still open)
- Updated: PROBLEM-settlement-payment-failures.md (Granola bookings signal)
- Created: PROBLEM-bookings-launch-risk.md (NEW, 7/12)

---

## Mixpanel status
- Endpoint attempted: mcp-eu.mixpanel.com (via fallback mcp__d1218b36 server)
- Partner Portal (3834354): Only 1 deal-related event found ("Page view - offers/edit/:dealId") — insufficient for enable/disable analysis
- Consumer Apps (3747444): Not queried — EU endpoint confirmed as correct
- **Status**: ⚠️ Failed — behavioural layer absent this run
- Qualitative signals carry full weight unmodified

---

## Open questions for Adam
1. Spice Aura is a perfect case study of the BDM signing quality problem — BDM promised no fees, set 30% discount, venue can't self-serve to fix. Worth interviewing this venue owner before they churn?
2. 8+ venue closures/sales this period — is this Easter-related seasonality or accelerating mortality? Worth checking against historical closure rates.
3. Bookings launching with minimal preparation per Granola. What's the product team's exposure if AMs can't hit 30/month targets?
4. Gami Chicken & Beer: Enterprise group signed at inconsistent rates. Is the enterprise/groups problem worse than IDEA-329 currently captures?
5. BB Thai Town + Little Bangkok loyalty leak: Is there a known process for disconnecting churned venues from offerless/loyalty? This feels like a systemic gap.
