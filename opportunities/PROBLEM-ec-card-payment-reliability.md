# Problem Card — EC Card & Payment Reliability

> One card per named problem. Cards get richer over time — never start fresh, always append.

---

## Problem statement

Customers cannot reliably set up or use the EatClub payment card — encountering errors during card linking (Apple Pay, digital card setup), payment declines at venues, and failed auth transactions — creating a cascade of refund requests, consumer frustration, and reduced transaction volume at venues. When consumers can't pay, venues don't get EatClub customers through the door, and the core value proposition breaks down.

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
| SD-699: Customer cannot link EC card to Apple Pay — error message on setup | Jira SD (Blocked Internally) | STRONG | Specific failure, ticket blocked |
| SD-572: Digital card setup error — "sorry, card is unavailable" — persists through reinstall, sign out, re-add | Jira SD (Blocked Internally) | STRONG | Customer tried 3 troubleshooting steps |
| SD-337: EC Card setup — customer redirected to banking app for verification, fails silently after completing | Jira SD (Blocked Internally) | STRONG | Specific UX failure point |
| SD-165: EC Card setup — white screen after adding card, ongoing for 3+ weeks | Jira SD (Blocked Internally) | STRONG | 3-week-old unresolved issue |
| Stage Brasserie (London): Richard Lindsay FAILED AUTH twice (decline reason 83), £56.49 + £56.50, submitted refund — "card didn't work, I had enough money" | Slack #ecpayuk-ops | STRONG | Specific customer, specific amounts, specific failure code |
| Notes Coffee Roasters (London): Denise Valencia FAILED AUTH £19.05, submitted refund — "card didn't work and I didn't get refund of the offer" | Slack #ecpayuk-ops | STRONG | Failed payment + no refund = double frustration |
| Mallow Borough (London): Sagun Soni FAILED AUTH £60.53 (insufficient funds), submitted refund — "the card didn't work" | Slack #ecpayuk-ops | MEDIUM | Insufficient funds = consumer-side, but refund flow triggered |
| Casa Tua Camden: Beatriz Cruz Trigo — "paid with eatclub card but discount wasn't applied", £115 total bill | Slack #ecpayuk-ops | STRONG | Payment went through but discount logic failed |
| Cu4tro Restaurant (London): Daniel Haigh FAILED AUTH twice £58.19, decline reason "do_not_honor" | Slack #ecpayuk-ops | MEDIUM | Repeated failure at same venue |
| Multiple additional failed auths at Firebird Soho, Kanada-ya Carnaby, Masala Brick Lane in single evening | Slack #ecpayuk-ops | MEDIUM | Volume pattern in UK market |

---

## Heat tracker

| Week | Signal count | Sources | Heat | Notes |
|---|---|---|---|---|
| 2026-W14 | 10+ | Jira SD, Slack #ecpayuk-ops | 9/12 | First identification — high volume, multi-source |

**Current status**: 🔴 Rising — 4 of 7 active SD tickets are card setup issues, ALL blocked internally

---

## Who is affected

| Segment | Evidence | Scale estimate |
|---|---|---|
| Consumers trying to set up EC Card | 4 SD tickets with distinct failure modes | Unknown — potentially widespread |
| UK consumers at venues | 6+ failed auths in single evening period | UK market payment reliability |
| Venues losing transactions | Failed payments = no EatClub customer revenue | Indirect but significant |

---

## What they're doing instead (workarounds)

- Consumers submitting refund requests after failed payments (Richard Lindsay, Denise Valencia, Sagun Soni, Beatriz Cruz Trigo)
- Consumer tried close/reopen app, sign out/in, reinstall — still failed (SD-572)
- Consumer tried different card — still failed (SD-165)
- Some consumers simply don't complete card setup and abandon

---

## Friction stack connections

- Connected to **Settlement & Payment Failures**: both are payment infrastructure issues affecting venue cash flow
- Connected to **Support Response Time**: card issues go Blocked Internally with no resolution path visible
- Potentially connected to **Venue Deal Control**: if consumers can't pay, venue transaction metrics drop

---

## Assumptions to test

| Assumption | Type | Importance | Evidence strength | How to test |
|---|---|---|---|---|
| EC Card setup failures affect a significant percentage of new users | Feasibility | High | Medium (4 tickets suggest pattern, not isolated) | Mixpanel: card setup completion rate, drop-off point |
| UK payment failures are higher than AU | Feasibility | High | Weak (only UK signals visible in #ecpayuk-ops) | Compare UK vs AU failure rates in Stripe dashboard |
| REST-21 (VGS integration) will address the card setup issues | Feasibility | High | Unknown | Ask engineering: does VGS fix the 4 blocked SD scenarios? |
| Failed payments directly reduce venue transaction volume in measurable ways | Desirability | High | Medium | Correlate venues with high failure rates to transaction metrics |

---

## Discovery status

- [x] Signal only — watching
- [ ] Interview questions drafted
- [ ] Interviews conducted (N={n})
- [ ] IDEA ticket raised → {IDEA-XXX}
- [ ] In delivery

**Last updated**: 2026-03-30
**Owner**: Adam Glegg
