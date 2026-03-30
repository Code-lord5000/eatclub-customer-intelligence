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

**Signal heat this period**: 🔴 High (26/12 combined across sub-problems — new card added)
**Active problem cards**:
- /opportunities/PROBLEM-ec-card-payment-reliability.md (Heat 9/12) ⚠️ NEW — DELIVERY GAP
- /opportunities/PROBLEM-support-response-time.md (Heat 9/12)
- /opportunities/PROBLEM-venue-deal-control.md (Heat 8/12)
- /opportunities/PROBLEM-settlement-payment-failures.md (Heat 8/12)

**Sub-opportunities surfacing from signals**:
- [x] Support response SLA: venues waiting weeks for terminal exclusions, refunds, menu updates — eroding trust
- [x] Self-serve deal management: high volume of manual change requests reveals PP friction
- [x] Settlement timing & failure detection: manual monitoring, all-platform Monday settlement crunch
- [x] EC Card / payment reliability: 4 of 7 active SD tickets are card setup issues, all blocked internally. UK payment failures high volume.
- [ ] Venue gaming / T&C enforcement: Rao's Bar giving inflated menu to EC users (emerging, watch)

---

### Branch 2: Onboarding journey quality

_Venues aren't reaching the "aha moment" — first successful deal, first tables filled — before they disengage._

**Signal heat this period**: 🔴 High (10/12) — new churn signals validate
**Active problem cards**:
- /opportunities/PROBLEM-bdm-signing-quality.md (Heat 10/12)

**Sub-opportunities surfacing from signals**:
- [x] BDM signing quality: venues signed at unsustainable deals (35% unlimited), non-ICP venues, missing data
- [x] Week 6-7 churn cliff: predictable drop point when initial excitement fades and cash flow pressure hits
- [ ] Cuisine-specific onboarding: one-size-fits-all approach doesn't work across venue types
- [ ] ICP / brand mismatch at sign-up: Ambra Spirits churned because "EC devalues offering to regulars" — premium venues reject discount positioning (NEW signal W14)
- [ ] Early churn from low-activity venues: Pizza Da Italia made $260 in 3+ weeks, went dark (NEW signal W14)

---

### Branch 3: Surfacing product value through data

_Venues can't see whether EatClub is working for them, so they make churn decisions without full information._

**Signal heat this period**: ⚪ Low (no direct signals this period)
**Active problem cards**:

**Sub-opportunities surfacing from signals**:
- [ ] Venue performance visibility (indirect signal: Insights page net revenue fix recently shipped REST-204)

---

### Branch 4: Product fit for enterprise / Groups market

_Multi-venue operators can't manage their EatClub presence at the portfolio level — individual venue tools don't scale._

**Signal heat this period**: 🟡 Medium (6/12)
**Active problem cards**:

**Sub-opportunities surfacing from signals**:
- [ ] Group account linking: Nicole's embarrassment at not seeing grouped venues
- [ ] Missing contact data across multi-venue portfolios
- [ ] Multi-venue deal restructuring: Famished Wolf (4 venues) coordinating deal changes through CS (NEW signal W14)

---

### Branch 5: AM efficiency and internal tooling

_AMs are spending time on manual tasks that reduce the time they have to add genuine value to venues._

**Signal heat this period**: 🔴 High (19/12 combined — Sam Benjamin's RGA manifesto validates direction)
**Active problem cards**:
- /opportunities/PROBLEM-deal-score-trust.md (Heat 11/12) ⚠️ POST-RELEASE FEEDBACK
- /opportunities/PROBLEM-commission-dispute-process.md (Heat 8/12)

**Sub-opportunities surfacing from signals**:
- [x] Deal score trust & transparency: AMs can't trust score, spend hours tracking manually
- [x] Commission dispute process: no transparent verification, disputes expire, AMs lose pay
- [x] Churn save penalty: saving venues from churn = negative deal score impact, perverse incentive
- [ ] AM wins visibility: no way to prove saves, upgrades, or loyalty sign-ups reliably
- [ ] Non-RGA work consuming AM/BDM time: Sam Benjamin announced internal AI tool being built to remove non-RGA work — validates problem, question is whether this overlaps IDEA-344/348/349 (NEW signal W14)

---

## How to use this document

After each weekly synthesis:
1. Update **Signal heat this week** for each branch based on synthesis output
2. Link any new problem cards created to the relevant branch
3. Add emerging sub-opportunities that synthesis identified
4. Note any signals that don't fit existing branches — new branches may need to be added

The OST should feel like it's growing toward you from the data, not being imposed top-down from strategy.

---

## Branch priority — last updated 2026-03-30

| Branch | Heat | Problem cards | Discovery tickets | Notes |
|---|---|---|---|---|
| Core venue friction | 🔴 26/12 | 4 | IDEA-291, IDEA-356, IDEA-353 | Highest heat — NEW EC Card reliability card (9/12). 4 of 7 SD tickets blocked. |
| AM efficiency | 🔴 19/12 | 2 | IDEA-344/348/349 (AM Tooling) | Stable high heat. Sam Benjamin building parallel AI/RGA tool — scope overlap question. |
| Onboarding | 🔴 10/12 | 1 | None — **DELIVERY GAP** | BDM signing quality still zero Jira coverage. New churn signals: ICP mismatch (Ambra), early churn (Pizza Da Italia). |
| Enterprise/Groups | 🟡 6/12 | 0 | IDEA-329 (Groups Onboarding) | Famished Wolf 4-venue deal restructure adds signal. |
| Value surfacing | ⚪ Low | 0 | IDEA-210, IDEA-232 (AT V2) | No direct signals. REST-204 (net revenue fix) recently shipped. |
