# Problem Card — Venue Deal Control & Self-Service Friction

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

Venues cannot easily manage their deals, menus, and operational settings through self-serve tools — generating a high volume of manual change requests through CS and #urgent that consume AM/CS time, delay venue operations, and create errors (e.g. "too many offers, I did a mistake please cancel it"). The friction between what venues want to do and what they can do creates a dependency on EatClub staff for basic operational changes.

---

## OST branch

- [x] Friction in core venue experience
- [ ] Product fit for enterprise/Groups
- [ ] Onboarding journey quality
- [ ] Surfacing product value through data
- [ ] AM efficiency / internal tooling

**Journey stage**: [ ] Onboarding  [x] Activation  [x] Ongoing engagement  [ ] AM relationship  [ ] Renewal/churn decision

---

## Signal log

### 2026-W14
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Punch Lane Wine Bar: Venue requested to remove 3pm-5pm recurring offer and change deal timing to 12pm-4pm | Slack #urgent (Mar 30, Nestor) | MEDIUM | Deal timing change routed through CS |
| The Chapter 24: Venue requested to permanently remove Tuesday offers | Slack #urgent (Mar 30, Nestor → Jay) | MEDIUM | Venue reducing engagement — permanent removal |
| British Patagonia (London): Wants to delete Mon/All Day/25%/DI offer, reason "offerTooHigh" — posted from Partner Portal | Slack #urgent (Mar 30, ECPay) | MEDIUM | Venue self-identified offer as too high |

### 2026-W13
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| 20+ ECPay deal edit/delete alerts in 48hrs — venues actively trying to manage deals through portal with varying success | Slack #urgent | MEDIUM | High volume of observable behaviour |
| Vino e Cucina: "too many offers i did a mistake please cancel it" — 2 deletion requests in rapid succession | Slack #urgent | STRONG | Venue error caused by unclear UI |
| Blackburn Cafe: 8 deal edits in a single session — Tue, Thu, Fri, Sat across different percentages | Slack #urgent | MEDIUM | Suggests trial-and-error, not confident self-serve |
| Mazcina Resto Bar: venue called to change hours + adjust deal timing, already posted one-off deal | Slack #urgent | MEDIUM | Multiple channels needed for one change |
| SD-697: Menu bug — price shows "35% off from 2pm" but no deal at 2pm (venue has no deals today) | Jira SD | STRONG | Technical bug causing confusion |
| Kashi Indian: deleted offers on Fri + Sat citing "offerTooHigh" | Slack #urgent | MEDIUM | Venue felt deal % was wrong |
| Manual menu typing identified as solvable "in 2 seconds with AI" | Granola meetings | WEAK | Solution-shaped but problem is valid |
| Nestor logging 5 deal change requests for different venues in single shift | Slack #urgent | MEDIUM | CS volume indicator |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W14 | 3 | Slack #urgent | 8/12 | Steady volume — deal change requests continuing |
| 2026-W13 | 8 | Slack #urgent, Jira SD, Granola | 8/12 | First run — high volume, medium quality |

**Current status**: 🟡 Stable — chronic background signal

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| Venues actively managing deals | 20+ edit/delete requests in 48hrs | High proportion of active venues |
| CS team (Nestor, Gladys, Hyacinth, Frency, Harold) | Multiple CS agents routing requests | Full CS shift team |
| AMs receiving overflow requests | Tom's terminal example, multiple AM tags in #urgent | Most AMs |

---

## What they're doing instead (workarounds)

- Venues calling CS to make deal changes (generating tickets and #urgent messages)
- Venues posting one-off deals when they can't edit recurring ones (Mazcina, Blackburn Cafe)
- Venues disabling all deals and re-creating rather than editing (Blackburn Cafe pattern)
- CS agents manually routing requests to AMs via #urgent with venue details

---

## Friction stack connections

- Connected to **Support Response Time**: self-serve gaps increase support ticket volume
- Connected to **BDM Signing Quality**: venues with poor initial setup need more deal changes
- Connected to **Settlement & Payments**: venues adjusting deals to manage cash flow impact

---

## Assumptions to test

| Assumption | Type | Importance | Evidence strength | How to test |
|---|---|---|---|---|
| Most deal edit requests could be self-served if PP UX were improved | Feasibility | High | Medium | Categorise last 100 #urgent deal requests: which were preventable? |
| Venues making errors in deal setup (Vino e Cucina) need undo/preview capabilities | Usability | Medium | Strong | PP session recordings, talk to 3 venues |

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → {IDEA-XXX}
- [ ] In delivery

**Last updated**: 2026-03-30
**Owner**: Adam Glegg
