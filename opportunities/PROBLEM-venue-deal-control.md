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

### 2026-W15 (Apr 1 — Run 4)
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Ngon Brisbane: Requested recurring offers permanently removed. Will "create offers manually moving forward." | Slack #urgent (Mar 31) | STRONG | WORKAROUND — venue bypassing recurring offer feature entirely. Product feature being avoided. |
| Partner Portal RCI limitation: Can't choose specific time slots for RCI offers. Kane: "if its RCI - venue has to do it through partner portal" but portal can't select specific times. | Slack (Mar 31, Kane Russell) | STRONG | Self-serve gap — venues and AMs both blocked on basic time-based deal control. |
| GT's Bar Noosa: Double dipping issues. No Square/Lightspeed integration. | Slack #churned_or_changed (Mar 31) | MEDIUM | Integration gap blocking deal control for venue without POS. |
| Continuing high volume of ECPay bot deal edit/delete alerts — Saigon Alley, Sassy Cocktail Bar, LoukouMADNESS, and others requesting changes via portal | Slack #urgent (Mar 31-Apr 1) | MEDIUM | Sustained high volume of portal-initiated changes. |
| **Mixpanel: Offer disabled events UP 48% over 7 days (449→667/day)**. Offer edited stable (273-383/day). Offer deleted low (0-56/day). | Mixpanel Partner Portal (3834354) | HIGH confidence | BEHAVIOURAL CONFIRMATION — rising disable rate validates qualitative signals. Venues are increasingly disabling offers rather than editing them. |
| HubSpot: 1 "Change/Delete Offer" ticket + 4 "Offers" tickets in 48hrs | HubSpot tickets | MEDIUM | CS ticket pipeline for deal changes continuing. |

### 2026-W14b (Mar 30)
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| SD-700: Petit Bistro & Wine Bar — venue/staff admin CANNOT edit offers for the day. AM Elliot also tried, no luck. Created new offer attempt also failed. | Jira SD (New, Mar 30) | STRONG | Self-serve is technically BROKEN, not just limited. AM also blocked. |
| Barrel N Basket: HS wants ALL offers reduced to 20% ASAP. CS left ticket. | Slack #urgent (Mar 30, Jesstoni Santiago) | MEDIUM | Urgent discount reduction routed through CS |
| Chicken Bandits: "would like to reduce deals to just 10% as they only have low profit ASAP" | Slack #urgent (Mar 30, Lyann Bayno) | STRONG | Explicit margin pressure — venue needs immediate control |
| Lilong by Taste of Shanghai: Change deal time 13:30–18:00 → 13:30–17:00 | Slack #urgent (Mar 30, Jesstoni Santiago) | MEDIUM | Time change routed through CS |
| The Maya Lounge: Modify seating time 3hrs → 90min. "Owner was very upset customers redeem offers too late during peak hours and not supporting their business." | Slack #churned_or_changed (Mar 30, Elodie Fitzsimmons) | STRONG | Peak hour friction — setup doesn't match venue operating reality |
| Burwood Teppanyaki House: Delete offer Mon/All Day/20%/DI. Reason: staffIssue | Slack #urgent (Mar 30, ECPay bot) | MEDIUM | Staff capacity driving deal change |
| JA Square: Delete offer Wed/All Day/30%/DI. Reason: badTime | Slack #urgent (Mar 30, ECPay bot) | MEDIUM | Timing mismatch |
| Polly Bar: Asked to remove offers for this week, added to HDS until Monday | Slack #urgent (Mar 30, Victoria Toledo) | MEDIUM | Temporary pause routed through AM |
| Kane Russell: "right now I only have access to do NCI. RCI needs to be activated by the account themselves" — admin tool limitation | Slack #churned_or_changed (Mar 30) | MEDIUM | Internal tooling gap — CS can't execute all deal types |
| Emma Viezzi asks Luke: "Do we have any guidelines on reducing seating time to 90 mins?" — no documented process | Slack #churned_or_changed (Mar 30) | MEDIUM | Process gap for common venue request |
| 6+ ECPay bot deal edit/delete alerts in single afternoon session | Slack #urgent (Mar 30) | MEDIUM | Continuing high volume of portal-initiated changes |

### 2026-W14a (Mar 28-30 — prior run)
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
| 2026-W15 | 6 | Slack #urgent, #churned, Mixpanel, HubSpot | 11/12 | MIXPANEL CONFIRMED — offer disables UP 48% (449→667/day). Ngon bypassing recurring offers entirely. RCI time slot limitation. |
| 2026-W14b | 11 | Slack #urgent, #churned_or_changed, Jira SD | 10/12 | ESCALATING — SD-700 confirms self-serve is technically broken. 11 signals, 3 sources. |
| 2026-W14a | 3 | Slack #urgent | 8/12 | Steady volume — deal change requests continuing |
| 2026-W13 | 8 | Slack #urgent, Jira SD, Granola | 8/12 | First run — high volume, medium quality |

**Current status**: 🔴🔴 CRITICAL — Heat 11/12 sustained. Mixpanel CONFIRMS rising disable rate (48% increase over 7 days). Venues bypassing recurring offers entirely (Ngon). RCI time slots not functional. IDEA-356 still Concept only.

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
