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

### 2026-W15 post-Easter (Apr 1–4 — Run 5)
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| Kavita: EC Card declined at restaurant — had to pay full price and wants 20% refund. Receipt attached. | HubSpot ticket (Apr 3) | STRONG | Classic in-venue card failure — consumer absorbs cost, EC absorbs refund liability |
| Grace Arrow Smith at Northbridge Brewing Company: EFTPOS tap not approved on machine BUT account debited $78.90 (~11am Apr 2) | HubSpot ticket (Apr 3) | STRONG | 🆕 NEW FAILURE MODE — debit-without-EFTPOS-approval. Settlement/reconciliation failure, not auth decline. Higher severity than standard decline. Pull Stripe logs for similar events. |
| Consumer: deleted EC card from Google Wallet, can't find way to add it back. Also requesting 30% discount refund. | HubSpot ticket (Apr 3) | MEDIUM | Google Wallet re-add path missing or broken. Second wallet-specific issue in 4 runs. |
| Consumer: "trying to use the app but can't add a card to my wallet or even have a card appear" | HubSpot ticket (Apr 3) | MEDIUM | Card setup failure on fresh attempt — consistent with SD-572/165 pattern |

### 2026-W14b (Mar 30)
| Signal | Source | Mom Test quality | Notes |
|---|---|---|---|
| H M at Homeboy Bar (London): FAILED AUTH x2 for £60.18 (insufficient_funds), then submitted refund for £88.31 — "card didn't work, I had enough money" | Slack #ecpayuk-ops (Mar 30) | STRONG | Same consumer, repeated failure, explicit "card didn't work" + contradicts decline reason |
| William Franzén at AperiPasta Prosecco Bar: FAILED AUTH £45.70 (insufficient_funds) + Stripe decline $71.85 | Slack #ecpayuk-ops (Mar 30) | MEDIUM | Consumer-side (insufficient funds) but generates venue-impacting decline |
| Gabriel Banner at Tacacho @ Van Gogh Cottage: FAILED AUTH £26.54 (decline reason: 100) + Stripe decline x2 $36.50 | Slack #ecpayuk-ops (Mar 30) | MEDIUM | Unusual decline code (100), repeated failures |
| Eat Thai Paddington: "venue does not have a successful transaction for today, I disabled them for now, awaiting response from HS" | Slack #urgent (Mar 30, Jesstoni Santiago) | STRONG | Payment failure caused venue to be DISABLED — direct impact on venue operations |
| Refund request was MISSED by support team — Jeroen had to ask Blessie to check, found it unprocessed | Slack #ecpayuk-ops (Mar 30, Jeroen → Blessie) | STRONG | Refund process gap — consumer waited longer because request fell through cracks |
| SD-699/572/337/165: All 4 EC Card setup tickets STILL Blocked Internally — no status change since last run | Jira SD (Mar 30) | STRONG | Chronic blockers, no resolution progress |
| Miryu Numao at Noisy Oyster: "venue closes at 4:00 but I chose to arrive at 5:30" — venue info accuracy issue causing failed dining experiences | Slack #ecpayuk-ops (Mar 30) | MEDIUM | Not card-specific but venue data accuracy affects consumer experience |

### 2026-W14a (Mar 28-30 — prior run)
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
| 2026-W15 post-Easter | 4 | HubSpot | 9/12 | Stable. NEW failure mode: EFTPOS debit-without-approval (Grace Arrow Smith, Apr 2). 4 signals over Easter weekend (suppressed volume). Google Wallet re-add broken. |
| 2026-W14b | 7 | Jira SD, Slack #ecpayuk-ops, Slack #urgent | 9/12 | Continuing — new UK payment failures, Eat Thai disabled, missed refund. 4 SD tickets still blocked. |
| 2026-W14a | 10+ | Jira SD, Slack #ecpayuk-ops | 9/12 | First identification — high volume, multi-source |

**Current status**: 🔴 Chronic, new failure mode — EFTPOS debit-without-approval is a settlement/reconciliation failure distinct from auth declines. 4 of 7 SD tickets still blocked internally. Google Wallet re-add path broken.

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

**Last updated**: 2026-04-04
**Owner**: Adam Glegg
