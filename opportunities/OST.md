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

**Signal heat this period**: 🔴🔴 CRITICAL (36/12 combined — deal control ESCALATING, new T&C friction card)
**Active problem cards**:
- /opportunities/PROBLEM-venue-deal-control.md (Heat 10/12) ⬆️ UP from 8 — SD-700 confirms self-serve is technically broken
- /opportunities/PROBLEM-ec-card-payment-reliability.md (Heat 9/12) — stable, 4 SD tickets still blocked
- /opportunities/PROBLEM-support-response-time.md (Heat 9/12) — SD-700 + SD-703 + missed refund
- /opportunities/PROBLEM-settlement-payment-failures.md (Heat 8/12)
- /opportunities/PROBLEM-tc-friction-venue-trust.md (Heat 7/12) ⚠️ NEW — high-performing venues at churn risk from T&C friction

**Sub-opportunities surfacing from signals**:
- [x] Support response SLA: venues waiting weeks for terminal exclusions, refunds, menu updates — eroding trust
- [x] Self-serve deal management: SD-700 confirms self-serve is broken (not just limited). High volume of manual change requests continues
- [x] Settlement timing & failure detection: manual monitoring, all-platform Monday settlement crunch
- [x] EC Card / payment reliability: 4 of 7 active SD tickets are card setup issues, all blocked internally. UK payment failures continuing.
- [x] T&C friction: Hayashi + Como Garden at extreme churn risk despite high performance. Rebates being offered as relationship management.
- [ ] Venue gaming / T&C enforcement: Rao's Bar giving inflated menu to EC users (emerging, watch)
- [ ] Venue info accuracy: Noisy Oyster — venue hours wrong, customer arrived to closed door (NEW signal W14b)

---

### Branch 2: Onboarding journey quality

_Venues aren't reaching the "aha moment" — first successful deal, first tables filled — before they disengage._

**Signal heat this period**: 🔴🔴 CRITICAL (12/12) — highest heat ever. Failed churn save + 3 explicit ICP churns + Granola meeting mapping onboarding bottlenecks
**Active problem cards**:
- /opportunities/PROBLEM-bdm-signing-quality.md (Heat 12/12) ⬆️ UP from 10 — CRITICAL

**Sub-opportunities surfacing from signals**:
- [x] BDM signing quality: venues signed at unsustainable deals, non-ICP venues, missing data
- [x] Week 6-7 churn cliff: predictable drop point when initial excitement fades
- [x] ICP / brand mismatch at sign-up: Ambra Spirits, Little B by Bruno&Co (regulars exploit deals for coffee)
- [x] Early churn from low-activity venues: Pizza Da Italia, That Viet Place (FAILED churn save)
- [x] Post-contract onboarding bottleneck: 9 Manila staff manual menu digitization, photo quality issues, go-live preferences friction (NEW — Granola W14b)
- [ ] Cuisine-specific onboarding: one-size-fits-all approach doesn't work across venue types
- [ ] Ghost kitchen / wrong venue type selection: Bema Burgers replaced by better venue from same group (NEW W14b)

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

**Signal heat this period**: 🟡 Medium (6/12)
**Active problem cards**:

**Sub-opportunities surfacing from signals**:
- [ ] Group account linking: Nicole's embarrassment at not seeing grouped venues
- [ ] Missing contact data across multi-venue portfolios
- [x] Multi-venue deal restructuring: Famished Wolf (4 venues) — now settled on 25% x 10/day + 35% x 2/day after NCI boost deletion
- [ ] Granola meeting: group signup form redesign identified as needed (NEW W14b)

---

### Branch 5: AM efficiency and internal tooling

_AMs are spending time on manual tasks that reduce the time they have to add genuine value to venues._

**Signal heat this period**: 🔴 High (19/12 combined — stable)
**Active problem cards**:
- /opportunities/PROBLEM-deal-score-trust.md (Heat 11/12) ⚠️ POST-RELEASE FEEDBACK
- /opportunities/PROBLEM-commission-dispute-process.md (Heat 8/12)

**Sub-opportunities surfacing from signals**:
- [x] Deal score trust & transparency: AMs can't trust score, spend hours tracking manually
- [x] Commission dispute process: no transparent verification, disputes expire, AMs lose pay
- [x] Churn save penalty: saving venues from churn = negative deal score impact, perverse incentive
- [ ] AM wins visibility: no way to prove saves, upgrades, or loyalty sign-ups reliably
- [ ] Non-RGA work consuming AM/BDM time: Sam Benjamin's internal AI tool — no new signals this period
- [ ] Kane Russell admin limitations: "right now I only have access to do NCI. RCI needs to be activated by the account themselves" (NEW W14b)

---

## How to use this document

After each weekly synthesis:
1. Update **Signal heat this week** for each branch based on synthesis output
2. Link any new problem cards created to the relevant branch
3. Add emerging sub-opportunities that synthesis identified
4. Note any signals that don't fit existing branches — new branches may need to be added

The OST should feel like it's growing toward you from the data, not being imposed top-down from strategy.

---

## Branch priority — last updated 2026-03-30 (run 2)

| Branch | Heat | Problem cards | Discovery tickets | Notes |
|---|---|---|---|---|
| Core venue friction | 🔴🔴 36/12 | 5 | IDEA-291, IDEA-356, IDEA-353 | NEW card: T&C friction (7/12). Deal control UP to 10/12 — SD-700 self-serve broken. |
| Onboarding | 🔴🔴 12/12 | 1 | None — **DELIVERY GAP** | CRITICAL. 3 explicit ICP churns + failed churn save + Granola maps full onboarding bottleneck. |
| AM efficiency | 🔴 19/12 | 2 | IDEA-344/348/349 (AM Tooling) | Stable. No new Sam Benjamin signals this period. |
| Enterprise/Groups | 🟡 6/12 | 0 | IDEA-329 (Groups Onboarding) | Famished Wolf settled on new deal structure. Granola flagged group signup form. |
| Value surfacing | ⚪ Low | 0 | IDEA-210, IDEA-232 (AT V2) | No signals. Customer.io survey (REST-243) could change this. |
