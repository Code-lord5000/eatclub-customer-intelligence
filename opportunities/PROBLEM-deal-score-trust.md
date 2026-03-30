# Problem Card — Deal Score Trust & Transparency

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

Account Managers cannot trust their deal score as an accurate, real-time reflection of their performance because the score constantly changes without explanation, lags behind reality, and penalises desirable behaviours (like saving churning venues by dropping deals). As a result, AMs spend hours manually tracking score changes instead of working with venues, dread commission week, and lose pay for legitimate work — undermining motivation and reducing time available for venue value-add.

---

## OST branch

- [ ] Friction in core venue experience
- [ ] Product fit for enterprise/Groups
- [ ] Onboarding journey quality
- [ ] Surfacing product value through data
- [x] AM efficiency / internal tooling

**Journey stage**: [ ] Onboarding  [ ] Activation  [ ] Ongoing engagement  [x] AM relationship  [x] Renewal/churn decision

---

## Signal log

### 2026-W13
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Jay: "deal score was all over the place… every month there's a change, it's fixed then it breaks" — lost 730pts across 2 accounts in one week | AM call transcript (Mar 25) | STRONG | References specific recurring behaviour over 12 months |
| Tom: "I've seen the thing change like five times… I'm logging what the deal score was originally, why it's changed — super time consuming" — spends hours nightly tracking | AM call transcript (Mar 25) | STRONG | Specific workaround behaviour |
| Jay saved 3 Schnitz venues from churn (2-hour meeting), got -90 points per venue, dispute declined | AM call transcript (Mar 25) | STRONG | Concrete example of perverse incentive |
| Tom: "8 new loyalty signs but it never got fixed… I've had two months of pushing loyalty and been paid for none of it" | AM call transcript (Mar 25) | STRONG | Specific loss, manual tracking failure |
| Nicole: "I can't wrap my head around [deal score] at 100 percent" — has venues doing 6.5K/month on 15% but penalised | AM call transcript (Mar 25) | STRONG | Revenue growth not reflected in score |
| Elliot: "people are losing sleep over anticipating comms day or disputes day" | AM call transcript (Mar 25) | STRONG | Emotional impact across team |
| Deal score anomalies identified — enabled/disabled status causing calculation problems, holiday deals disabling unexpectedly | Granola meeting notes | MEDIUM | Technical root cause confirmed |
| Commission deal score trust problems; no credit for saving/fixing accounts | Granola meeting notes | MEDIUM | Corroborates AM transcript signals |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W13 | 8 | AM transcript, Granola meetings | 11/12 | First run — extremely high signal density |

**Current status**: 🔴 Rising — POST-RELEASE FEEDBACK on recently shipped deal score logic changes (REST-229, REST-235, REST-236, REST-213, REST-228)

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| All AMs (Melbourne, Sydney, UK) | Multiple AMs speaking on transcript — Jay, Tom, Nicole, Elliot, Sean, Jasmine, others | Full AM team (~15-20 AMs) |
| Venues indirectly | AMs spend time tracking score instead of working venues; venues with saved accounts get worse AM attention | All active venues |

---

## What they're doing instead (workarounds)

- Tom keeps a large manual notes document logging deal score changes daily — "I waste a lot of time trying to keep these notes logged, looking at the deal score every day"
- AMs manually calculate what's in their best interest before every venue meeting
- Jay tracks every dispute in personal notes and chases across multiple managers (Sophie → Kane → Luke)
- AMs avoid engaging with "toxic" high-deal-score venues (35% unlimited) because any change = point loss
- AMs avoid saving churning venues because saves result in negative points

---

## Friction stack connections

- Connected to **BDM Signing Quality**: poorly signed venues (35% unlimited) create inevitable deal score drops for AMs
- Connected to **Commission Dispute Process**: deal score inaccuracy forces disputes, which then fail
- Connected to **Support Response Time**: AMs can't focus on venues when occupied by commission tracking

---

## Assumptions to test

| Assumption | Type | Importance | Evidence strength | How to test |
|---|---|---|---|---|
| Recent deal score logic changes (REST-229 etc.) address the calculation bugs AMs described | Feasibility | High | Weak — AMs still frustrated post-ship | Compare new logic against specific AM examples from transcript |
| AMs would trust a live, accurate deal score even if they still lost points for churn saves | Desirability | High | Medium | Interview 3-4 AMs: separate "accuracy" from "fairness" |
| A transparent deal score changelog would reduce hours spent manual tracking | Desirability | High | Strong (workaround evidence) | Build lightweight prototype, test with 2 AMs |
| Rewarding venue revenue growth (not just deal score) would better align AM incentives | Viability | High | Medium — Nicole's suggestion | Model AM commission under blended metric |

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → {IDEA-XXX}
- [ ] In delivery

**Last updated**: 2026-03-28
**Owner**: Adam Glegg
