# Synthesis Log — 2026-04-04 (Run 5)

**Period covered**: 2026-04-01 → 2026-04-04 (Easter long weekend)
**Run number**: 5 (W15, post-Easter)
**Prior run**: 2026-04-01-synthesis.md
**Signal context**: ⚠️ Significantly lower volume than prior runs — Easter long weekend (Good Friday Apr 3, Easter Sat Apr 4). Slack silent. Primary signal source this run: Granola meetings (Apr 1–2) + HubSpot helpdesk.

---

## Signal counts by source

| Source | Signals | Notes |
|---|---|---|
| Slack #churned_or_changed | 0 | ZERO — Easter long weekend. First run with no Slack signal. |
| Slack #urgent / #ecpayuk-ops | 0 | Easter silence — not absence of problems |
| Granola | 5 new meetings | Rich: onboarding automation, new PM/CPO, team structure, bookings status, group sign-up. April 1–2. |
| HubSpot tickets | 115,220 total pool | Newest 50 reviewed. EC card failures, refund requests, closed venue complaints, AI training rollout signal. |
| Mixpanel | Not pulled | No change since Run 4. |
| **Total** | ~20 actionable signals | Low volume, but strategically important — team/delivery signals dominate |

---

## 🔥 Rising themes this week

---

### Theme 1: Onboarding Automation — HubSpot data sync gap now being closed

**Heat**: Medium (active delivery — graduated from discovery)
**Signal count**: 3 signals, 1 source (Granola)
**Recurrence**: Recurring (Run 4 flagged $200k annual cost; Run 5 = active solution confirmed)
**Problem statement**: Every venue that signs with EatClub requires a team member to manually copy sign-up form data into HubSpot — ~10 minutes per venue, error-prone, with no automated sync between systems. At ~400 venues/month, this consumes ~133 hours/month of onboarding team capacity. Data gaps (e.g. membership billing day only in HubSpot, not in EatClub DB) compound the problem.
**Mom Test quality**: STRONG — "Karen's team spends 5-10 minutes per venue copying contract details between systems." Quantified, specific, confirmed across multiple Granola meetings. Allen now building the HubSpot connector.
**OST branch**: Onboarding journey quality (Branch 2)
**Journey stage**: Onboarding (first 30 days)
**Recommended action**: ✅ In delivery — HubSpot connector being built by Allen (using Claude, structured class approach). Monitor for go-live signal. Flag to Adam: data model mapping with Jerome is the next blocker.

**Signals this week:**

- *Onboarding data meeting (Apr 2)*: Agreed sequencing — HubSpot integration first (form → HubSpot push), then menu upload automation, then first-payment lifecycle agent. Source of truth stays in EatClub DB; HubSpot used only for comms. Allen to map HubSpot fields vs EatClub data model — gap identified: membership billing day lives only in HubSpot.
- *Product trio sync (Apr 1)*: ~400 venues/month × 20 min avg = ~8,000 mins/month = ~133 hrs. Goal is to redeploy offshore team to customer support (not eliminate roles). Google pre-fill for venue data is unreliable — AI agent/scrape-and-validate approach proposed instead.
- *First-payment lifecycle engine (Apr 2)*: Cameron pitching $1 test charge lifecycle engine to Will (payments team) next week. UK identified as priority (highest first-payment fail rate). VGS not yet live anywhere — current wallet/Stripe flow still active.

---

### Theme 2: EC Card Payment Reliability — Easter weekend signals confirm chronic pattern

**Heat**: High
**Signal count**: 4 signals, 1 source (HubSpot)
**Recurrence**: Chronic (Runs 1–5, 9/12 heat)
**Problem statement**: Consumers cannot reliably use the EatClub payment card at venues — encountering EFTPOS declines (sometimes with funds debited), Google Wallet setup failures, and discount non-application. Each failure generates a refund request and leaves the consumer paying full price. Venue transaction volumes are silently eroded.
**Mom Test quality**: STRONG — "My EatClub card was declined at the restaurant, so I had to pay the full amount" (Kavita, Apr 3). "Customer swipe the card but transaction did not get approved on Eftpos machine but customer's account has been debited by Eat Club" (Grace Arrow Smith, Apr 2). Specific, past behaviour, quantified loss.
**OST branch**: Friction in core venue experience (Branch 1)
**Journey stage**: Ongoing engagement
**Recommended action**: Watch — CHRONIC signal with no new Jira movement. The $1 charge lifecycle engine (Cameron pitching) may surface pre-payment failures earlier, but doesn't address in-venue EFTPOS reliability. Raise with engineering: does VGS address the active SD tickets?

**Signals this week:**

- *EC Card declined at restaurant, paid full amount* (Kavita, HubSpot Apr 3): Booking made, card declined, customer paid full £ and wants 20% refund. — STRONG
- *EFTPOS tap not approved but account debited* (Grace Arrow Smith, HubSpot Apr 2): Northbridge Brewing Co. Transaction date Apr 2 ~11am. EFTPOS showed no approval, but EatClub debited $78.90. Receipt attached. Double-charge risk. — STRONG
- *Google Wallet EC card disappeared, can't re-add* (HubSpot Apr 3): Customer deleted card from wallet, now can't add back. No in-app path to re-add. — MEDIUM
- *EC Card can't be added to wallet at all* (HubSpot Apr 3): "I am trying to use the app but can't add a card to my wallet or even have a card appear." — MEDIUM

---

### Theme 3: Bookings — First post-launch week, no failure signals yet

**Heat**: Medium (monitoring)
**Signal count**: 2 signals, 1 source (Granola standup)
**Recurrence**: Recurring (heat: 9/12 from Run 4 launch)
**Problem statement**: Bookings launched April 1 with known gaps — settlement integration for SMS billing incomplete, no AM training, and UK cities (Leeds, Cardiff, Liverpool, Bristol) launching simultaneously with AU. The first week of real-world load on this product has now passed. No explicit failure signals have surfaced, but it's Easter weekend with lower venue activity — a misleadingly quiet first week.
**Mom Test quality**: MEDIUM — no consumer failure signals yet. The problem evidence is structural (known gaps at launch), not behavioural.
**OST branch**: Onboarding journey quality / Core venue friction (Branches 1 & 2)
**Journey stage**: Activation
**Recommended action**: Watch closely next week. Easter has suppressed dining activity and inbound complaints. First real signal week will be April 7+. Bristol release unblocked this week (tickets 175, 176). AB integration confirmed done in standup.

---

### Theme 4: Venue info accuracy — Confirmed closed venues, Easter effect

**Heat**: Low
**Signal count**: 2 signals, 1 source (HubSpot)
**Recurrence**: Recurring — Noisy Oyster venue hours issue flagged in Run 3. Now two more.
**Problem statement**: Venues listed as open on the EatClub platform are sometimes closed when consumers arrive — creating wasted journeys, lost trust, and refund/complaint overhead. Easter weekend amplifies this: many venues close with no notice in the app.
**Mom Test quality**: STRONG — "Hi I had a booking with the bird today at 5pm, We arrived and the Venue was closed" (Clare, Apr 3). "Rocco Pizzeria is actually closed today. We got to the restaurant and found it shut" (Michelle, Apr 3). Specific past behaviour, named venues.
**OST branch**: Friction in core venue experience (Branch 1)
**Journey stage**: Ongoing engagement
**Recommended action**: Watch — two signals in a single day (Good Friday). May be seasonal. But connects to existing venue hours accuracy sub-opportunity. If this recurs post-Easter, escalate — it's a direct consumer trust failure.

---

### Theme 5: Product team structural transition — new PM/CPO, new delivery model

**Heat**: Medium (strategic signal)
**Signal count**: 3 signals, 2 sources (Granola)
**Recurrence**: New — first run with these signals
**Problem statement**: EatClub's product team is undergoing simultaneous structural changes: Justin Hancock (fractional/consulting, ex-Cedar Labs) joined as CPO/Head of Product on April 2; Roy Tarabine joined the payments & internal tools stream; Mark Dohnt is transitioning from product to design. The product/design boundary is undefined. No A/B testing framework exists (historically blocked). The leadership acknowledged risk: "amplifying a mess only creates a false emergency" — engineering practices need to improve before aggressive AI integration. These changes represent both an opportunity (fresh leadership, potential to unlock A/B testing, JPD alignment) and delivery risk (knowledge in transition, roadmap ownership unclear).
**Mom Test quality**: MEDIUM — these are structural signals from internal meetings, not venue behaviour. Not Mom Test applicable per se.
**OST branch**: AM efficiency / internal tooling (Branch 5) — delivery capacity risk
**Journey stage**: N/A (internal)
**Recommended action**: Watch — this is not a Jira ticket, but it will shape delivery capacity for all other branches. Priority: get Justin across the OST, the chronic delivery gap on BDM signing quality, and the A/B testing blocker. The Melbourne workshop with Sam and Luke (~April 14) is the next milestone.

---

## 📋 All signals this week — classified

| Signal summary | Source | Who affected | Mom Test quality | Theme | OST branch |
|---|---|---|---|---|---|
| HubSpot connector: sign-up form → HubSpot push now scoped and in build (Allen + Claude) | Granola — Onboarding data meeting (Apr 2) | Onboarding team, venues | STRONG | Onboarding automation | Branch 2 |
| Product trio: 133 hrs/month manual onboarding labour quantified; offshore team to redeploy to CS | Granola — Product trio sync (Apr 1) | Onboarding team | STRONG | Onboarding automation | Branch 2 |
| $1 charge lifecycle engine for first-payment failures — Cameron pitching to Will, UK priority | Granola — Onboarding data meeting (Apr 2) | Venues, payments team | MEDIUM | Onboarding automation | Branch 2 |
| EC Card declined at restaurant (Kavita, Apr 3) — paid full price, wants 20% refund | HubSpot ticket | Consumer | STRONG | EC Card reliability | Branch 1 |
| EFTPOS tap not approved but account debited $78.90 — Grace Arrow Smith, Northbridge Brewing Co (Apr 2) | HubSpot ticket | Consumer + venue | STRONG | EC Card reliability | Branch 1 |
| Google Wallet EC card disappeared, can't re-add | HubSpot ticket | Consumer | MEDIUM | EC Card reliability | Branch 1 |
| Can't add card to wallet at all — "card doesn't appear" | HubSpot ticket | Consumer | MEDIUM | EC Card reliability | Branch 1 |
| Bookings: AB integration confirmed done; Bristol unblocked (tickets 175, 176) | Granola — Standup (Apr 2) | Product/eng team | MEDIUM | Bookings post-launch | Branches 1+2 |
| The Bird: customer arrived, venue closed Good Friday | HubSpot ticket | Consumer | STRONG | Venue hours accuracy | Branch 1 |
| Rocco Pizzeria: customer arrived, venue closed Good Friday | HubSpot ticket | Consumer | STRONG | Venue hours accuracy | Branch 1 |
| Justin Hancock joins as CPO/Head of Product (Apr 2) | Granola — Adam/Justin weekly | Internal delivery | MEDIUM | Team structure | Branch 5 |
| Roy Tarabine joins payments & internal tools PM stream | Granola — Adam/Roy (Apr 1) | Internal delivery | MEDIUM | Team structure | Branch 5 |
| No A/B testing framework — historically blocked (Justin flagged as risk) | Granola — Adam/Justin weekly | Product practice | MEDIUM | Team structure | Branch 5 |
| Zendesk rollout to Jerome's team — not on roadmap until today (Apr 1) | Granola — Adam/Roy (Apr 1) | Jerome's team | MEDIUM | AM tooling / internal | Branch 5 |
| Mark moving from product to design — product/design boundary needs definition | Granola — Adam/Justin weekly | Product team | MEDIUM | Team structure | Branch 5 |
| "Amplifying a mess creates a false emergency" — engineering quality must come before AI acceleration | Granola — Adam/Justin weekly | All product delivery | WEAK (principle, not data) | Team structure | Branch 5 |
| Ciaooo double-tap: dessert at Lory's Tiramisu (outsourced, same physical venue) flagged as invalid tap | HubSpot ticket | Consumer | STRONG | T&C edge case — outsourced payment | Branch 1 |
| AI platform training rollout: Assenheims 56 (5 London locations) + A1 Sushi — HubSpot tickets logged as training complete | HubSpot tickets (Apr 3) | UK venues, BDMs | MEDIUM | New capability: AI-assisted training | Branch 5 |
| Dining credit not received — My Neighbours Dumpling + Mangal 2, UK (Apr 3) | HubSpot tickets | UK consumers | MEDIUM | Billing reliability | Branch 1 |
| Voucher code not working — Heart of Balham HOB (Apr 3) | HubSpot ticket | Consumer | STRONG | EC Card / billing | Branch 1 |
| Group sign-up form: billing stays per venue, Google pre-fill unreliable, POS flag to automate | Granola — Product trio (Apr 1) | Onboarding team, venues | STRONG | Onboarding automation | Branch 2 |
| Crilly (this tool) described to Justin as weekly signal synthesis → OST output | Granola — Adam/Justin weekly | Product leadership | — | Internal context | — |

---

## 🗺️ OST update

### Branch 1: Friction in core venue experience
**What strengthened this week?**
- EC Card reliability confirmed chronic — 4 signals over an Easter weekend when volume is suppressed. When normalised for lower activity, rate is consistent with prior weeks.
- NEW signal type: EFTPOS-approved-but-not-approved with account debited (double-charge risk). Distinct from auth decline — this is a settlement timing/sync failure. Worth escalating to engineering.
- Ciaooo/Lory's Tiramisu: NEW edge case — outsourced dessert venue at same physical location. Consumer penalised for venue's internal payment setup. Classic T&C friction sub-type: rules designed for intent, not edge cases.
- Venue hours accuracy: 2 confirmed Easter Friday closures not surfaced in app. Small number but high consumer cost.

**What weakened or contradicted?**
- No #ecpayuk-ops signals this week (Easter). Cannot tell if UK payment failure rate changed.

**New sub-opportunities surfacing:**
- [ ] Proactive venue closure communication: Venues should be prompted to flag public holiday closures in Partner Portal. Simple feature, high consumer trust impact.
- [ ] Outsourced payment disambiguation: The Ciaooo case reveals a gap where same-location outsourced vendors create invalid multi-tap scenarios. T&C needs either a product fix or better consumer communication.

---

### Branch 2: Onboarding journey quality
**What strengthened this week?**
- HubSpot integration is now in active development (Allen/Claude). The onboarding cost is now quantified at two figures: $200k/year annual FTE (Run 4, Granola) and 133 hrs/month manual labour (Run 5, Product trio). Both point to the same bottleneck.
- Group sign-up form design feedback in progress — Cam reviewed and sent notes.
- Google pre-fill approach resolved: AI agent (scrape + flag) rather than auto-populate.
- Bookings: AB integration confirmed complete this week. First post-launch sprint clean.

**What weakened or contradicted?**
- Sam "vibe-coded" solutions from a London hotel room (Justin/Adam meeting). This is both a validation (stakeholder has customer context and can build) and a risk signal (ungoverned AI builds without SDLC = instability).
- Still no post-launch failure signals for Bookings. Too early to read either way.

**New sub-opportunities surfacing:**
- [ ] POS integration trigger on sign-up: Currently a Slack-to-POS-team manual process. MVP: automated flag on venue sign-up → triggers POS team workflow.
- [ ] Group ABN capture: Group-level ABN needed for contract but not currently in sign-up form (Vinni to add).

---

### Branch 3: Surfacing product value through data
**What changed?** No new signals. Crilly now operational and described to Justin as the weekly OST output tool. No A/B testing framework still — Justin flagged as blocker. Measurement gap is persistent.

---

### Branch 4: Product fit for enterprise/Groups
**What strengthened this week?**
- Group sign-up form: billing confirmed at venue level (per Poppy). Even within groups, bank details entered per venue. Simplifies group-level deal management but adds per-venue setup time.
- Groups design: Cam's feedback being actioned before next sprint.

**New sub-opportunities surfacing:**
- [ ] Group contract addendum flow: Adding new venues post-contract requires a manual addendum process. Not yet scoped.

---

### Branch 5: AM efficiency and internal tooling
**What strengthened this week?**
- AI platform training at UK venues (Assenheims 56 ×5, A1 Sushi): Logged as HubSpot tickets — AMs now delivering AI-assisted training to venues on exploration deals and offers. First evidence this is being operationalised at scale in UK. New capability worth tracking.
- Crilly operational: confirmed producing OST output weekly. Justin aligned on it in first 1:1.
- Zendesk rollout for Jerome's team this quarter: NEW item. Not on roadmap until Roy's onboarding conversation. Roy needs to scope and optimise.
- JPD alignment: Roy flagged JPD usage inconsistent across team. Mark resisted. Justin as new CPO = opportunity to reset.

**What changed in team structure?**
- Justin joins: fractional CPO/Head of Product background. Priorities: scaling PM impact, A/B testing, tiered feature launch framework, and measurement discipline.
- Roy Tarabine joins: payments & internal tools stream. Needs to get close to problems before solutions. Roadmap was previously a black box under Mark.
- Mark pivots to design: product/design boundary to be defined. Do not push process changes until Justin's influence lands.

---

## ⚠️ Friction stack watch

**No multi-source venue stacking this period** — Slack was silent (Easter). Cannot confirm or deny.

**Carry-over from Run 4 (still unresolved):**
- BB Thai Town + Little Bangkok: still receiving offerless transactions post-churn (Run 3 + Run 4). No update this run. This is a CHRONIC post-churn leak. Flag to Luke if not already resolved.

**Post-Easter monitoring list** (venues to watch next week):
- The Bird: closed Good Friday per customer complaint. Check if this was planned or a surprise. If surprise, check for T&C / Closed Restaurant ticket cross-reference.
- Rocco Pizzeria: same as above.
- Any venues that triggered EC card failures this week — Grace Arrow Smith at Northbridge Brewing Co specifically flagged a debit-without-EFTPOS-approval scenario. Worth pulling the Stripe log for Apr 2.

---

## 💡 Synthesis notes

**What surprised me this week?**

The most significant signal this run is not a venue complaint — it's the product team restructure. Justin joining as CPO/Head of Product on April 2, the same week Crilly runs for the first time, is a natural forcing function to get the OST in front of fresh eyes. The risk: a new leader inheriting an acceleration mandate ("10-15x output via AI") without first establishing measurement infrastructure or A/B testing. Justin correctly named this: "amplifying a mess only creates a false emergency." The Melbourne workshop in ~10 days with Sam and Luke is the next cultural moment.

**What's missing from the signal set?**

- Zero Slack signal this week. Easter is the obvious explanation, but it means we have no visibility on what was happening at venue level over the long weekend (Good Friday is one of the busiest dining days in AU). The closed venue complaints (The Bird, Rocco Pizzeria) suggest the Easter period surfaced real consumer trust issues that may be underreported.
- No Mixpanel data this run. The offer disable trend (up 48% in Run 4) needs a second week of data to confirm trajectory.
- No post-launch Bookings feedback. Week 1 is entirely under Easter cover. Week 2 (April 7+) will be the real signal.
- No HubSpot notes from AMs about specific venues this period. Likely Easter-related but leaves a gap in AM-proximity signals.

**EFTPOS debit-without-approval: new failure mode, not previously classified**

The Grace Arrow Smith ticket (April 2) is worth isolating. Prior EC card failures were auth declines — consumer's card doesn't work, no charge occurs. This is different: the EFTPOS terminal showed no approval, but EatClub's system still debited the consumer's account. This is a settlement/reconciliation failure, not an auth failure. If this is a recurring pattern, it represents a higher-severity issue than a plain decline (consumers are double-paying without knowing it). Recommend: pull Stripe logs for similar patterns in the past 30 days.

**Interview questions to sharpen weak signals:**

For *venue hours accuracy / Easter closures*:
- "How did you communicate your Easter hours to EatClub? Did anyone prompt you to update them?"
- "If you were closed for a public holiday, what did you expect EatClub to do with your listing?"

For *AI platform training at UK venues (Assenheims 56)*:
- "What does the training session cover? Is it being delivered by AMs or via an automated tool?"
- "Are venues that receive training showing different activation or retention patterns 30 days out?"

For *product team structural transition*:
- "What's on Justin's priority list for the first 30 days? What's he been told the biggest problems are?"

---

## Cards updated this run

- **PROBLEM-ec-card-payment-reliability.md** → Updated: new signals (EFTPOS debit-without-approval, Kavita card decline, Google Wallet re-add failure). New sub-failure mode flagged.
- **PROBLEM-bdm-signing-quality.md** → Stable: no new signals this run (Easter). Heat holds at 12/12 but signal drought means drift detection shows first run without new fuel.
- **OST.md** → Updated: Branch 1 (new sub-opps: venue closure comms, outsourced payment disambiguation), Branch 2 (new sub-opps: POS trigger, group ABN), Branch 4 (group contract addendum), Branch 5 (Zendesk, AI training rollout, team structure changes).

---

## Drift detection

| Theme | Direction | Runs tracked | Signal trend | Action |
|---|---|---|---|---|
| BDM Signing Quality | ⚪ Quiet (Easter) | 5 (run 0→5) | 10→10→12→12→12→(0 new signals) | Watch — Easter explains silence. Likely to return to 12/12 next week. STILL zero Jira coverage. |
| Venue Deal Control | ⚪ Quiet | 5 (run 0→5) | 8→8→10→11→11→(0 new signals) | Watch — need Mixpanel week 2 to confirm +48% trend. |
| Bookings Launch Risk | 🟡 Monitoring | 3 (run 3→5) | 7→9→(no failures detected, Easter) | Watch — real signal week starts April 7. |
| EC Card Reliability | 🔴 Chronic + new failure mode | 5 (run 1→5) | 9→9→9→9→9+ | Escalate EFTPOS debit-without-approval to engineering. New failure mode, not just auth decline. |
| Onboarding Automation | 🟢 In Delivery | 2 (run 4→5) | flagged→active build | Track delivery: HubSpot connector (Allen), menu automation, $1 charge engine (Cameron). |
| Venue Hours Accuracy | 🟡 Emerging | 2 (run 3→5) | 1→(2 Easter closures) | Watch — 3rd recurrence = pattern. Consider proactive closure prompt in Partner Portal. |
| T&C Friction | ⚪ Quiet | 5 | 7→8→8→8→(no new) | Watch |
| Support Response Time | ⚪ Quiet | 5 | 9→9→9→9→(no new) | Watch |
| Deal Score Trust | ⚪ Quiet (3rd run no signals) | 5 | 11→11→11→11→(no new) | Cooling — REST shipped. |
| Commission Dispute | ⚪ Quiet (4th run no signals) | 5 | 8→8→8→8→(no new) | Cooling — IDEA in Discovery. |
| Settlement Failures | ⚪ Quiet | 5 | 8→8→8→8→(no new) | Watch — $1 charge engine coming. Net settlement in commercials (Apr 2 meeting). |
| Venue Mortality | ⚪ Quiet (Easter) | 3 (run 3→5) | 5→6→(no new) | Watch — Easter explains silence. |
| Team/Delivery Capacity | 🆕 New | 1 (run 5) | — → flagged | Watch — Justin/Roy joining. Mark transition. A/B gap. Workshop April ~14. |
| AI Training Rollout (UK) | 🆕 New | 1 (run 5) | — → emerging | Interesting positive signal. Track retention impact of trained venues. |

---

## Open questions for Adam

1. **EFTPOS debit-without-approval** — Grace Arrow Smith at Northbridge Brewing Co (Apr 2). Account debited $78.90 despite EFTPOS showing no approval. This is a different failure mode from auth decline — it's a settlement reconciliation failure. Is this a known pattern? Worth pulling Stripe logs for similar events over the past 30 days before the $1 charge engine work starts.

2. **BB Thai Town + Little Bangkok** — still receiving offerless transactions (flagged Runs 3 and 4). Has this been resolved? If not, the post-churn disconnection process is broken and this is an active financial leak.

3. **Justin's first 30 days** — what does he know about the OST? Has he seen the synthesis logs? The A/B testing gap is a blocker on measuring anything we ship. Is unlocking this a priority in his mandate?

4. **Melbourne workshop (April ~14)** — Sam and Luke attending. This is the first alignment opportunity since bookings launched. Synthesis logs 1–5 should be the prep material. Do you want Crilly to produce a briefing doc ahead of it?

5. **AI platform training at UK venues** — Assenheims 56 (5 sites) trained on Apr 3, A1 Sushi also. Who is running this? Is it a formal rollout or ad hoc AM activity? Does it correlate with improved activation or retention? Worth checking 30-day outcomes for early-trained venues.

6. **Bookings: week 1 signal drought** — Easter. Week 2 (April 7+) will be the real test. Settlement integration for SMS billing still outstanding. Is there a comms plan for AMs if they start hitting edge cases?
