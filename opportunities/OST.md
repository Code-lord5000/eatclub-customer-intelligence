# Opportunity Solution Tree — EatClub Restaurant Product

> This document is fed by the signal repo. It should update weekly as synthesis runs.
> The OST is not a backlog. It's a map of the problem space — solutions live in Jira.

---

## Desired outcome (root)

**Reduce venue churn from ~8% toward 4%**

Framed as: increase the number of venues that find enough value in EatClub to stay active, engaged, and growing on the platform.

---

## Opportunity branches

### Branch 1: Friction in core venue experience

_Venues are losing trust or motivation to engage because the product makes routine tasks harder than they should be._

**Signal heat this period**: 🔴 High (Easter suppressed Slack — EC card 9/12 chronic with NEW failure mode: EFTPOS debit-without-approval. 2 confirmed closed venue complaints on Good Friday. T&C edge case: outsourced payment at same physical location.)
**Active problem cards**:
- /opportunities/PROBLEM-venue-deal-control.md (Heat 11/12) ⬆️ UP from 10 — Spice Aura triple-stack + multiple time-based deal requests + Portal deletion failures
- /opportunities/PROBLEM-ec-card-payment-reliability.md (Heat 9/12) — stable, Kom Coffee terminal mapping error (SD-707)
- /opportunities/PROBLEM-support-response-time.md (Heat 9/12) — SD-700 still open "Waiting for customer"
- /opportunities/PROBLEM-settlement-payment-failures.md (Heat 8/12)
- /opportunities/PROBLEM-tc-friction-venue-trust.md (Heat 8/12) ⬆️ UP from 7 — recurring signals (Hayashi, Como Garden, Little B, Ambra Spirits, Maya Lounge)

**Sub-opportunities surfacing from signals**:
- [x] Support response SLA: venues waiting weeks for terminal exclusions, refunds, menu updates — eroding trust
- [x] Self-serve deal management: SD-700 still open + 4 deletion failures (Binny'z Pizza "badTime" errors) + Spice Aura can't delete/reduce below 20% + time-based control requests (Le Feu, Martina Rose Bay)
- [x] Settlement timing & failure detection: manual monitoring, all-platform Monday settlement crunch
- [x] EC Card / payment reliability: Terminal mapping errors (Kom Coffee SD-707 + Kom Coffee Roasters), transactions routing to wrong venue
- [x] T&C friction: Hayashi + Como Garden at extreme churn risk despite high performance. Rebates being offered as relationship management. New recurring signals: Little B (AOV $15 damage), Ambra Spirits (devalues offering), Maya Lounge (peak hour conflict).
- [x] Time-based deal control: Le Feu Oasis (in-house deals until 3pm) + Martina Rose Bay (Friday/Saturday removal)
- [ ] Venue gaming / T&C enforcement: Rao's Bar giving inflated menu to EC users (emerging, watch)
- [ ] Venue info accuracy: Noisy Oyster — venue hours wrong, customer arrived to closed door (NEW signal W14b). The Bird + Rocco Pizzeria — closed Easter Friday with no notice in app (Run 5). Consider: proactive closure prompt in Partner Portal for public holidays.
- [ ] Outsourced payment disambiguation: Ciaooo/Lory's Tiramisu — outsourced dessert venue at same physical location created invalid multi-tap. T&C rules not designed for this edge case (Run 5).

---

### Branch 2: Onboarding journey quality

_Venues aren't reaching the "aha moment" — first successful deal, first tables filled — before they disengage._

**Signal heat this period**: 🔴 High (Easter silence — no new churn signals, but onboarding automation now in active delivery). BDM signing quality holds at 12/12 (6th run, zero Jira coverage). Bookings post-launch week 1 quiet (Easter). HubSpot connector build started (Allen/Claude, Apr 2). Group sign-up form: 133 hrs/month manual labour quantified.
**Active problem cards**:
- /opportunities/PROBLEM-bdm-signing-quality.md (Heat 12/12) ⬆️ SUSTAINED from 10 — CRITICAL, CHRONIC, 4th run
- /opportunities/PROBLEM-bookings-launch-risk.md (Heat 9/12) ⬆️ UP from 7 — **LAUNCHED TODAY** with settlement gaps, no AM training, UK cities simultaneous

**Sub-opportunities surfacing from signals**:
- [x] BDM signing quality: venues signed at unsustainable deals, non-ICP venues, missing data. New signals: Jaipur Palace (overseas approval), Chicci (11 revenue after 2 saves), York Street (AOV $18), Shila Kitchen (wrong rate), Spice Aura (triple-stack: no-fees promise + 30% too high + can't self-serve), Ravneels (no results month 1), Ceylon Girl's (refused solutions), Cafe De Rolls (no margin, selling business)
- [x] Week 6-7 churn cliff: predictable drop point when initial excitement fades
- [x] ICP / brand mismatch at sign-up: Ambra Spirits, Little B by Bruno&Co (regulars exploit deals for coffee)
- [x] Early churn from low-activity venues: Pizza Da Italia, That Viet Place (FAILED churn save)
- [x] Post-contract onboarding bottleneck: 30hrs/week manual menu entry, 10% menus incorrect, map marker errors, 6 offshore staff (Granola W14b)
- [x] Bookings readiness: launching without restaurant flow design, no AM training (30/month targets), SMS billing integration incomplete
- [ ] Cuisine-specific onboarding: one-size-fits-all approach doesn't work across venue types
- [ ] Ghost kitchen / wrong venue type selection: Bema Burgers replaced by better venue from same group (NEW W14b)
- [ ] POS integration trigger on sign-up: currently a Slack-to-POS-team manual process. MVP = automated flag on sign-up → triggers POS team workflow (Run 5, Product trio)
- [ ] Group ABN capture: group-level ABN needed for contract but not in current sign-up form (Run 5, Vinni to add)
- [ ] Group contract addendum flow: adding new venues post-contract requires manual addendum process — not yet scoped (Run 5)

---

### Branch 3: Surfacing product value through data

_Venues can't see whether EatClub is working for them, so they make churn decisions without full information._

**Signal heat this period**: ⚪ Low (no direct signals this period)
**Active problem cards**:

**Sub-opportunities surfacing from signals**:
- [ ] Venue performance visibility (indirect signal: Insights page net revenue fix recently shipped REST-204)
- [ ] Customer.io survey delivery in progress (REST-243 In Review) — could generate value perception data

---

### Branch 4: Product fit for enterprise / Groups market

_Multi-venue operators can't manage their EatClub presence at the portfolio level — individual venue tools don't scale._

**Signal heat this period**: 🟡 Medium (6/12 baseline + Gami signal emerging)
**Active problem cards**:

**Sub-opportunities surfacing from signals**:
- [ ] Group account linking: Nicole's embarrassment at not seeing grouped venues
- [ ] Missing contact data across multi-venue portfolios
- [x] Multi-venue deal restructuring: Famished Wolf (4 venues) — now settled on 25% x 10/day + 35% x 2/day after NCI boost deletion
- [x] Enterprise onboarding chaos: Gami Chicken & Beer — new venues signed at different rates, AM got "no advice or help from anyone at EatClub" (Tania, W14b)
- [ ] Granola meeting: group signup form redesign identified as needed (NEW W14b)

---

### Branch 5: AM efficiency and internal tooling

_AMs are spending time on manual tasks that reduce the time they have to add genuine value to venues._

**Signal heat this period**: 🔴 High (19/12 combined — stable)
**Active problem cards**:
- /opportunities/PROBLEM-deal-score-trust.md (Heat 11/12) — no new signals, REST-229/235/236 shipped
- /opportunities/PROBLEM-commission-dispute-process.md (Heat 8/12) — no new signals, IDEA-344/348/349 in Discovery Q2

**Sub-opportunities surfacing from signals**:
- [x] Deal score trust & transparency: AMs can't trust score, spend hours tracking manually
- [x] Commission dispute process: no transparent verification, disputes expire, AMs lose pay
- [x] Churn save penalty: saving venues from churn = negative deal score impact, perverse incentive
- [ ] AM wins visibility: no way to prove saves, upgrades, or loyalty sign-ups reliably
- [ ] Non-RGA work consuming AM/BDM time: Sam Benjamin's internal AI tool — no new signals this period
- [x] Kane Russell admin limitations: "right now I only have access to do NCI. RCI needs to be activated by the account themselves" (NEW W14b)
- [x] Bookings AM readiness: 30/month targets without formal training (NEW W14b)
- [ ] Zendesk rollout for Jerome's team — landing this quarter, not on roadmap until Roy's onboarding conversation Apr 1 (Run 5)
- [ ] A/B testing framework: no testing infrastructure exists — historically blocked. Justin Hancock (new CPO) flagged as risk. Unlocking this is prerequisite for measuring anything shipped (Run 5)
- [ ] AI training rollout at UK venues: Assenheims 56 (5 London sites) + A1 Sushi trained on Exploration deals/offers (Apr 3). Track 30-day activation and retention impact (Run 5)

---

## How to use this document

After each weekly synthesis:
1. Update **Signal heat this week** for each branch based on synthesis output
2. Link any new problem cards created to the relevant branch
3. Add emerging sub-opportunities that synthesis identified
4. Note any signals that don't fit existing branches — new branches may need to be added

The OST should feel like it's growing toward you from the data, not being imposed top-down from strategy.

---

## Branch priority — last updated 2026-04-04 (run 5)

| Branch | Heat | Problem cards | Discovery tickets | Notes |
|---|---|---|---|---|
| Core venue friction | 🔴 High | 5 | IDEA-291, IDEA-356, IDEA-353 | Easter signal drought — but EC card 9/12 chronic with NEW failure mode (EFTPOS debit-without-approval). 2 closed venue Good Friday complaints. Ciaooo outsourced payment T&C edge case. Deal control: no new signals, Mixpanel week 2 data needed. |
| Onboarding | 🔴 High | 2 | None for BDM (DELIVERY GAP — 6th run) | HubSpot connector NOW IN BUILD (Allen/Claude, Apr 2). 133 hrs/month manual onboarding labour quantified. BDM signing quality 12/12 held (Easter silence). Bookings post-launch week 1 quiet. Real signal from April 7+. |
| AM efficiency | 🟡 Medium | 2 | IDEA-344/348/349 (AM Tooling) | NEW: Justin Hancock joins as CPO (Apr 2), Roy Tarabine joins payments stream (Apr 1). A/B testing framework gap flagged. Zendesk rollout for Jerome's team this quarter (not on roadmap until Apr 1). AI training rollout at UK venues. |
| Enterprise/Groups | 🟡 Medium | 0 | IDEA-329 (Groups Onboarding) | Group sign-up form in active development. Billing confirmed at venue level. Group ABN + POS trigger to be added to form. Contract addendum flow not yet scoped. |
| Value surfacing | ⚪ Low | 0 | IDEA-210, IDEA-232 (AT V2) | No direct signals. No A/B testing framework — blocking measurement of everything else. |
