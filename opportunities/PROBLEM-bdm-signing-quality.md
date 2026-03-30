# Problem Card — BDM Signing Quality & Venue Setup

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

Venues are being signed with unsustainable deal structures (35% × unlimited offers) and without adequate onboarding (settlement explanation, Partner Portal walkthrough, ICP validation), creating a predictable wave of churn risk at weeks 6-7 that AMs inherit but cannot prevent — and are penalised for fixing. The downstream cost is avoidable churn, negative AM deal score impacts, and wasted AM time firefighting accounts that were set up to fail.

---

## OST branch

- [ ] Friction in core venue experience
- [ ] Product fit for enterprise/Groups
- [x] Onboarding journey quality
- [ ] Surfacing product value through data
- [ ] AM efficiency / internal tooling

**Journey stage**: [x] Onboarding  [x] Activation  [ ] Ongoing engagement  [ ] AM relationship  [x] Renewal/churn decision

---

## Signal log

### 2026-W13
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Jay: "I've lost 730 points across two accounts… set up on 35% × 2000 offers daily. That seems silly." Week 6-7 drop pattern. | AM call transcript (Mar 25) | STRONG | Specific numbers, recurring pattern |
| Tom: "I had a bakery get signed at $71 AOV… sells gingerbread men and slices. Never been ICP." (Rowley's Bakery Newport) | AM call transcript (Mar 25) | STRONG | Specific venue, specific failure |
| Tom: "BDMs signing extra 6-8 venues knowing some will churn each month to hit targets" | AM call transcript (Mar 25) | STRONG | Systemic incentive misalignment |
| Nicole: "we hired ESL BDMs that can speak Mandarin and we can't even have a conversation with those venues but we're still marked on deal score" | AM call transcript (Mar 25) | STRONG | Communication gap → AM penalty |
| Nicole: venues not grouped, missing mobile numbers in HubSpot — "really embarrassing when he said I've got Holly's Kitchen" | AM call transcript (Mar 25) | STRONG | Missing data at sign-up |
| Elliot: "BDMs signing at 30-35%… haven't been onboarded properly, don't understand settlement… most likely to churn in first 30 days" | AM call transcript (Mar 25) | STRONG | Direct pattern observation |
| Jay: "different strategies for all these different venues — Italian different, Japanese different, cafes different — but there's only one equation BDMs use" | AM call transcript (Mar 25) | STRONG | One-size-fits-all signing approach |
| Poor quality venue signings from BDMs flagged in Granola meeting | Granola meetings | MEDIUM | Corroborates transcript |
| Multiple #urgent messages: venues wanting deal changes/deletions shortly after onboarding — Blackburn Cafe (8 edits in a row), Vino e Cucina ("too many offers I did a mistake") | Slack #urgent | MEDIUM | Observable post-sign chaos |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W13 | 9 | AM transcript, Granola, Slack #urgent | 10/12 | First run — high signal, strong quality |

**Current status**: 🔴 Rising

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| Venues signed at 35% unlimited | Jay's 2 accounts, Tom's portfolio, pattern across all AMs | ~20-30% of new signings (estimate) |
| Non-ICP venues (bakeries, low-AOV cafes) | Tom's bakery example, Jay's bubble tea | Unknown but flagged repeatedly |
| AMs inheriting poor signings | All AMs on transcript | Full AM team |
| ESL venue owners | Nicole's Mandarin-speaking venue portfolio | Subset of new signings |

---

## What they're doing instead (workarounds)

- AMs avoid engaging with high-deal-score accounts (35% unlimited) because any change = point loss
- Jay proactively drops deals to save venues, accepts point penalty: "I dropped all the deals just to keep them on the platform"
- AMs try to "build out a proper schedule" for each venue but this takes 3+ hours per venue
- Tom avoids calling new venues early because interaction risks deal score loss
- BDMs sign extra venues anticipating some will churn — creating volume over quality

---

## Friction stack connections

- Directly feeds **Deal Score Trust**: poorly signed venues create inevitable score drops
- Feeds **Settlement & Payment Failures**: venues not educated on settlement timing at sign-up
- Feeds **Support Response Time**: poorly set up venues generate more support tickets

---

## Assumptions to test

| Assumption | Type | Importance | Evidence strength | How to test |
|---|---|---|---|---|
| Week 6-7 is a consistent churn risk point for poorly signed venues | Desirability | High | Strong (multiple AMs confirm) | Mixpanel cohort analysis: churn by sign-up deal % and week |
| BDM signing criteria (ICP, AOV, deal %) are not enforced systematically | Viability | High | Strong | Audit last 60 days of signings: deal %, AOV, churn rate |
| Venues signed at lower deals (15-25%) retain better than 35% unlimited | Desirability | High | Medium — Nicole's 15% venues doing well | Data analysis: retention by initial deal structure |
| A BDM "signing quality score" would reduce downstream churn | Viability | Medium | Weak | Model what a quality score looks like, test with Luke/Sam |

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → {IDEA-XXX}
- [ ] In delivery

**Last updated**: 2026-03-28
**Owner**: Adam Glegg
