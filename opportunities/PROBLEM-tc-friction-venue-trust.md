# Problem Card — T&C Friction & Venue Trust Erosion

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

Even high-performing venues that generate significant revenue through EatClub experience cumulative friction from T&C enforcement — perceived breaches, customer behaviour they can't control, and dining dynamics that don't match their setup (peak hour redemptions, regulars exploiting deals for low-value orders). The compounding effect of managing these issues makes the partnership feel adversarial rather than collaborative, pushing otherwise successful venues toward churn not because EatClub doesn't work, but because the management overhead of T&C issues outweighs the revenue benefit.

---

## OST branch

- [x] Friction in core venue experience
- [ ] Product fit for enterprise/Groups
- [ ] Onboarding journey quality
- [ ] Surfacing product value through data
- [ ] AM efficiency / internal tooling

**Journey stage**: [ ] Onboarding  [ ] Activation  [x] Ongoing engagement  [x] AM relationship  [x] Renewal/churn decision

---

## Signal log

### 2026-W14b (Mar 30)
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Hayashi Japanese Restaurant: "High performing venue that takes a magnifying glass to every T&C breach. Venue is at extreme risk of churning." Adding 2% rebate to keep deals high and ease relationship strain. | Slack #churned_or_changed (Mar 30, Jai Richards) | STRONG | High-performing venue at churn risk BECAUSE of T&C friction, not despite it. Rebate = commercial concession to manage relationship damage. |
| Como Garden (same group as Hayashi): "Previously high performing venue that took a magnifying glass to every transaction/T&C breach. Venue has dropped off a cliff since last year (prev 60kQ)." Adding 2% rebate. | Slack #churned_or_changed (Mar 30, Jai Richards) | STRONG | Revenue dropped from 60k/quarter. Same T&C friction pattern. Multi-venue group signal — pattern is replicable. |
| The Maya Lounge: "Owner was very upset customers redeem offers too late during their peak hours and not supporting their business." Requested seating time 3hrs → 90min. | Slack #churned_or_changed (Mar 30, Elodie Fitzsimmons) | STRONG | Venue feels EC customers are disrupting peak operations. Setup doesn't match venue operating reality. |
| Little B by Bruno&Co: "Regulars using the deal and only ordering coffee." AOV $15. Venue doesn't see value. | Slack #churned_or_changed (Mar 30, Jessie Helyar) | STRONG | Regulars exploiting deals for minimum-value orders. Venue can't control which customers use EC. |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W14b | 4 | Slack #churned_or_changed | 7/12 | NEW CARD — 4 signals, 1 source, strong Mom Test, new theme |

**Current status**: 🟡 New — watching. Strong quality signals but single source. If this appears in Granola/HubSpot/SD, heat will rise quickly.

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| High-performing venues (60k+ quarterly) | Hayashi, Como Garden — both high revenue, both at churn risk | Unknown — requires analysis of churn by revenue band |
| Venues in dining categories with "regular" customer base | Little B (cafe regulars), Hayashi (repeat diners) | Likely cafes, casual dining, local neighbourhood restaurants |
| Venues with peak-hour sensitivity | The Maya Lounge — peak hours disrupted by late EC redemptions | Restaurants with narrow peak windows |

---

## What they're doing instead (workarounds)

- AMs offering rebates (2%) to offset T&C frustration and keep deals high (Hayashi, Como Garden)
- Venues reducing deals to minimum (Little B dropped to 20%) hoping to limit exposure
- Venues requesting seating time reductions to control peak-hour impact (Maya Lounge)
- Venues eventually churning when workarounds feel insufficient (Little B)

---

## Friction stack connections

- Connected to **Venue Deal Control**: venues adjust deals to manage T&C impact, generating deal change requests
- Connected to **BDM Signing Quality**: venues not educated at sign-up about how T&C works, what customer behaviour to expect
- Distinct from **Venue Gaming** (Rao's Bar): this is venues feeling wronged BY T&C enforcement, not venues violating T&Cs

---

## Assumptions to test

| Assumption | Type | Importance | Evidence strength | How to test |
|---|---|---|---|---|
| High-performing venues churn at meaningful rates due to T&C friction | Desirability | High | Medium (2 venues confirmed, 1 group) | Correlate churn data with T&C dispute frequency for venues with >$30k quarterly revenue |
| Rebates are an effective short-term retention tool for T&C-frustrated venues | Viability | Medium | Weak (just started) | Track Hayashi + Como Garden retention after rebate implementation |
| Venues lack control over which customers use their EatClub deals (regulars vs new) | Desirability | High | Strong (NCI exists but venues don't always use it) | Interview 5 venues about customer mix expectations vs reality |
| Peak-hour redemption timing is controllable through existing deal setup tools | Feasibility | Medium | Unknown | Audit whether current deal time slots + seating time settings give venues adequate control |

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → {IDEA-XXX}
- [ ] In delivery

**Last updated**: 2026-03-30
**Owner**: Adam Glegg
