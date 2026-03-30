# Problem Card — Settlement & Payment Failures

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

Failed settlements go undetected because monitoring is manual, and when debt accumulates ($10k+/week from 8-9 unnoticed failures), it becomes a sudden crisis that damages the venue relationship and accelerates churn. This is amplified by all platforms (Uber Eats, DoorDash, EatClub) settling on the same day (Monday), creating acute cash flow pressure for venues — especially those on high-percentage deals.

---

## OST branch

- [x] Friction in core venue experience
- [ ] Product fit for enterprise/Groups
- [ ] Onboarding journey quality
- [ ] Surfacing product value through data
- [ ] AM efficiency / internal tooling

**Journey stage**: [ ] Onboarding  [ ] Activation  [x] Ongoing engagement  [ ] AM relationship  [x] Renewal/churn decision

---

## Signal log

### 2026-W13
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Manual monitoring required for failed settlements; $10k+ debt accumulates weekly from 8-9 unnoticed payment failures | Granola meetings | STRONG | Specific $ amounts, specific failure count |
| Jay: "all platforms take money out on the same day — Monday. If we're doing big deals and they're not good with cash flow, the money starts coming out on the same day" | AM call transcript (Mar 25) | STRONG | Specific platform timing pattern |
| Jay: "that's my first question [to venues] — how does your settlement with other platforms work?" — proactive workaround | AM call transcript (Mar 25) | STRONG | AM workaround behaviour |
| Need for automated alerts for payment failures identified | Granola meetings | WEAK | Solution-shaped but problem grounded |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W13 | 4 | Granola, AM transcript | 8/12 | First run — high severity, medium frequency |

**Current status**: 🟡 Stable — known issue, partially in discovery

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| Venues with failed settlements | 8-9 failures going unnoticed per period | Recurring across platform |
| Venues on high-% deals with poor cash flow | Jay's week 6-7 pattern | Subset of new signings |
| AMs dealing with debt conversations | Jay's first question is about settlement | All AMs |

---

## What they're doing instead (workarounds)

- Jay proactively asks venues about settlement timing with other platforms at first meeting
- Manual monitoring of failed settlements (someone checking periodically)
- AMs doing debt collection conversations that damage relationships

---

## Friction stack connections

- Connected to **BDM Signing Quality**: venues not educated on settlement at sign-up
- Connected to **Deal Score Trust**: debt conversations can lead to deal changes → score impact

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → IDEA-291 (Net Settlement — in Discovery)
- [ ] In delivery

**Last updated**: 2026-03-28
**Owner**: Adam Glegg
