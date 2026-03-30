# Problem Card — Support & Tech Response Time

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

When venues need operational support — terminal exclusions, refunds, menu updates, customer callbacks — the response takes weeks rather than days because there is no formal support rotation, no ticket visibility for AMs, and no SLAs. This erodes venue trust in EatClub and makes AMs unable to deliver on promises, compounding other friction points toward churn.

---

## OST branch

- [x] Friction in core venue experience
- [ ] Product fit for enterprise/Groups
- [ ] Onboarding journey quality
- [ ] Surfacing product value through data
- [x] AM efficiency / internal tooling

**Journey stage**: [ ] Onboarding  [ ] Activation  [x] Ongoing engagement  [x] AM relationship  [x] Renewal/churn decision

---

## Signal log

### 2026-W13
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Tom: "5-10 unresolved issues that venues have with me… sitting on a terminal exclusion for about a week… no visibility over how long we're waiting for tickets" | AM call transcript (Mar 25) | STRONG | Specific count, specific duration |
| Tom: "we don't get status updates, we don't see who's assigned, there's nothing about that" on tech ticket system | AM call transcript (Mar 25) | STRONG | Specific workflow gap |
| Tom: "venues losing faith in EatClub… they do the minimum with the platform so their risk is at an all-time low" | AM call transcript (Mar 25) | STRONG | Direct churn impact described |
| Wok & Wild: "requesting menu update not done after multiple attempts of contacting us" + requesting customer email database | Slack #urgent | STRONG | Venue frustrated after repeated attempts |
| Vi handling most production issues alone with no formal support rotation | Granola meetings | MEDIUM | Structural gap confirmed |
| Engineers pulled off sprint work for urgent fixes; AMs waiting months for bug fixes | Granola meetings | MEDIUM | Systemic pattern |
| Tech/CS/ops failing AMs with slow response times (10+ business days) | Granola meetings | STRONG | Specific timeframe |
| Cafe Brunelli "can't configure the tablet to make it work — closed the venue today because of tablet issue" | Slack #urgent | STRONG | Venue closed due to unresolved tech issue |
| Soul Origin UNSW "still waiting for tablet replacement as the ones they have is not charging" | Slack #urgent | MEDIUM | Ongoing hardware issue |
| Sprint retro action items: formal on-call documentation, support triage, QA hiring | Confluence retro (Mar 27) | MEDIUM | Team acknowledges gap |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W13 | 10 | AM transcript, Granola, Slack #urgent, Confluence | 9/12 | First run — multi-source, strong quality |

**Current status**: 🔴 Rising

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| Venues with pending support requests | Tom's 5-10 unresolved, Wok & Wild, Cafe Brunelli, Soul Origin UNSW | Unknown — likely dozens at any time |
| AMs across all markets | Tom's testimony, structural gap across team | Full AM team |
| Engineering (Vi specifically) | Vi doing solo production support | 1 engineer overloaded |

---

## What they're doing instead (workarounds)

- AMs "bumping" CS-AM channel messages repeatedly — "I've bumped it three times this week"
- AMs disabling deals and posting one-offs as workarounds (My Little Siam integration issue, Tom's terminal issue)
- AMs physically visiting venues to apologise and smooth things over
- Tom promising "we're working on it" to venues while knowing nothing is happening
- Venue (Wok & Wild) requesting direct access to customer email database to bypass EatClub

---

## Friction stack connections

- Connected to **Deal Score Trust**: unresolved issues cause deal changes that affect deal score
- Connected to **Venue Deal Control**: manual changes needed when self-serve isn't available
- Connected to **BDM Signing Quality**: poorly set up venues generate more support tickets

---

## Assumptions to test

| Assumption | Type | Importance | Evidence strength | How to test |
|---|---|---|---|---|
| Average support ticket resolution time exceeds 5 business days | Feasibility | High | Strong (10+ days cited) | Pull SD ticket data: time-to-resolution distribution |
| Venues with unresolved support tickets churn at a higher rate | Desirability | High | Medium — Tom describes trust erosion | Correlate SD tickets with churn data in Mixpanel |
| A formal triage + SLA process would reduce resolution time by 50%+ | Feasibility | Medium | Weak | Benchmark current vs. target; pilot with 1 support person |

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → {IDEA-XXX}
- [ ] In delivery

**Last updated**: 2026-03-28
**Owner**: Adam Glegg
