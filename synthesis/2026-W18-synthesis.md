**Sources available this run**: Slack (10 channels, 347 messages), HubSpot (300 tickets / 200 notes scanned), Churn CSV (21 AU churns from 30 rows), Mixpanel (9,239 events across 1,413 unique venues)
**Sources unavailable / failed**: Granola (no customer-facing meetings in window — agent skipped), Deal Score (parsed 30 rows but returned 0 drops / 0 rises / 0 zero-score — pipeline likely incomplete; W16's 397 zero-score venues remain unverifiable)
**Confidence note**: This is a **moderate-confidence** run. HubSpot only scanned ~6% of tickets and ~3% of notes — pages 4+ unscanned due to budget, and all 9 watch list venues had zero in-window HubSpot activity in scanned records. Watch list coverage is therefore **low**. Granola absence means no venue-voice meeting data for a second consecutive week. Deal Score returning zero signals is suspicious — either the data pipeline is stale or the CSV doesn't contain W17 score movements; treat T001 counts as carried forward from W16, not validated. Mixpanel is high-volume (1,413 venues) but can't distinguish AM-operated sessions from venue-operated without user-ID enrichment; bulk-edit pattern detection (20+ edits in 1 session) is the best proxy. Approximately 18 lower-priority Slack signals were noted in coverage but not individually surfaced — most are additional T010 T&C abuse instances and T007 manual config requests, meaning both themes are *under*counted in the signal table below.

---

## 🔥 Rising themes this week

### 1. T007 — Venues cannot self-serve on Partner Portal, so AMs do it for them — while the portal itself is broken

**Theme tag**: T007
**Heat**: 🔴 **HIGH**
**Signal count**: 19+ explicit (3 Slack + 16 Mixpanel bulk-edit patterns) — coverage notes indicate 20+ *additional* manual requests not individually surfaced
**Source count**: 3 (Slack, Mixpanel, Churn)
**Lifecycle**: CHRONIC (5+ weeks)

**Problem statement**: Venues lack the ability (or awareness) to configure deal settings, NCI boosts, seat times, guest limits, and no-show buffers via Partner Portal — forcing AMs to perform these changes on their behalf. This week the problem compounded: the portal itself crashed during deal updates (Elliot Rayment, 23 Apr), and the deal prediction backend server (dpc.eatclubhub.com) hit a read timeout starting ~23:59 on 23 Apr (Martin Heal), meaning the system that should automate deal optimisation was also down. Meanwhile, Mixpanel captured 16 venues where a single session generated 20–74 offer edits — the signature of an AM bulk-editing on behalf of a venue, not genuine self-serve.

**Mom Test quality**: **STRONG** — Observable behaviour with measurable cost. Verbatim: *"hey I am trying to update a load of deals on the partner portal but it keeps crashing"* (Elliot Rayment, AM, tech-halp-super-urgent, 23 Apr). Tania Marinopoulos requested seat-time changes for 6 NVG Group venues simultaneously via Slack because the portal doesn't support it. Mixpanel shows 74 edits in 1 session for restID D8EA79FC — no venue operator does 74 edits; that's an AM.

**OKR**: OKR 1 (Primary) — this is the single most direct path to removing 10 hrs/month of manual AM work
**OST branch**: Manual AM task reduction → Venue self-serve capability
**Journey stage**: Ongoing engagement
**Recommended action**: **Discovery ticket** — scope the top 5 actions AMs perform on behalf of venues (NCI boost, seat time, guest limit, no-show buffer, bulk offer edit) and build self-serve flows. Separately, **Escalate** the portal crash + deal prediction server outage to engineering immediately.

---

### 2. T010 — Customer T&C abuse is directly causing venue churn, and venues have no enforcement tools

**Theme tag**: T010
**Heat**: 🔴 **HIGH**
**Signal count**: 4 surfaced + 8+ additional in coverage notes = 12+
**Source count**: 2 (Slack, HubSpot)
**Lifecycle**: RISING (3 weeks)

**Problem statement**: Customers are systematically abusing booking T&Cs — redeeming dine-in offers for takeaway, breaching max-pax limits, arriving outside time windows, and walking out after redeeming. Venues have no tools to flag, block, or recover from these incidents. The platform's resolution process ("we'll contact the customer") is not accepted by venue owners as adequate. This week, Onda Bar & Eatery churned specifically over this. The Last Jar (EC9FABAF) is at its 4th cancellation attempt citing this issue. Lulo Spice & Bar accumulated $160.74 in debt while refusing to pay, explicitly citing T&C abuse as justification. Coverage notes indicate 8+ additional incidents (Chapati CBD pax breaches, VECINO bottomless menu abuse, Les Bubbles double-redemption, Paradiso, KebabG, Como Garden redeem-in-advance) not individually surfaced.

**Mom Test quality**: **STRONG** — Specific past behaviour with financial consequence. Verbatim: *"The owner demands refunds for reservations T&C breaches. After multiple attempts at trying to explain our procedures and how we can support his team by contacting customers, he won't accept this as a solution. Escalated to both Emma, he has chosen to cancel."* (Jessie Helyar on Onda Bar, churned_or_changed, 24 Apr). Forno 88 $643 takeaway fraud attempt from W16 remains unresolved.

**OKR**: OKR 3 — Churn reduction (friction in core venue experience)
**OST branch**: Friction in core venue experience → Customer compliance enforcement
**Journey stage**: Ongoing engagement → Renewal-churn decision
**Recommended action**: **Discovery ticket** — scope venue-facing T&C enforcement tools (customer flagging, automatic refund triggers, repeat-offender blocking). Interview The Last Jar (Bryony) and Onda Bar owner for specific incident patterns.

---

### 3. T006 — When AMs are unreachable, cancellation requests go unactioned and venues escalate to legal threats

**Theme tag**: T006
**Heat**: 🔴 **HIGH**
**Signal count**: 3 signals
**Source count**: 2 (Slack, HubSpot)
**Lifecycle**: RISING (3 weeks)

**Problem statement**: There is no automated routing when an AM is unreachable or when cancellation/deactivation requests arrive. Venues send cancellation requests that sit unanswered — sometimes for weeks — during which the platform continues running offers and charging the venue. This week ARRA Coffee & Wine sent multiple deactivation requests starting 18 April with *zero response and zero action taken*. Their venue remained active, customers continued redeeming offers, and the owner is now threatening formal legal action. Separately, Tatva Indian Kitchen's owner has been trying to reach Josephine (AM) for a week with no success and gave an ultimatum: call by tomorrow or cancel. Corlam Kitchen emailed their cancellation on 13 April to the wrong inbox — by the time Tania Marinopoulos found it, the venue owner refused all discussion.

**Mom Test quality**: **STRONG** — Verbatim: *"You have continued to operate promotions without my consent despite multiple written requests to deactivate... directly resulting in financial loss to my business... If this matter is not resolved immediately, I will have no choice but to pursue formal legal action to recover damages"* (ARRA Coffee & Wine, HubSpot ticket 44900678208, 26 Apr). This is the strongest Mom Test signal in the entire run — specific, past-tense, financially quantified, with stated consequence.

**OKR**: OKR 1 — System automation gap (also OKR 3 — direct churn cause)
**OST branch**: System automation → OOO/coverage routing
**Journey stage**: AM relationship → Renewal-churn decision
**Recommended action**: **Escalate immediately** — ARRA Coffee & Wine needs same-day deactivation and a senior apology (legal risk). **Jira ticket** — implement automated routing for cancellation/deactivation requests in HubSpot when no owner is assigned or owner is OOO. **Jira ticket** — add SLA alerting for any cancellation request unanswered after 48 hours.

---

### 4. T011 — Billing failures are eroding venue trust through delayed refunds, double charges, and failed transactions

**Theme tag**: T011
**Heat**: 🔴 **HIGH**
**Signal count**: 5 signals
**Source count**: 2 (Slack, Churn)
**Lifecycle**: CHRONIC (4+ weeks)

**Problem statement**: Venues are experiencing billing failures across multiple vectors: refunds promised but never delivered (Mr Ramen San, $65.63 outstanding since March + additional unauthorized deductions post-cancellation); overcharges refunded to wrong payment method (La Vallee, $780.40 to EatClub card instead of registered credit card); double-taps at terminal where neither charge reaches the venue (Bumbles Cafe); and repeated failed transactions with no root-cause explanation (Mr Chu Contemporary Eatery, $112.11 + $368.65). Mr Ramen San churned this week directly over billing. Their owner Royston explicitly said he'll consider reactivating only when refund proof is provided — trust is broken at the receipt level.

**Mom Test quality**: **STRONG** — Dollar amounts, dates, specific transaction failures. Verbatim: *"we have not received any refund of $65.63. Please provide us the date or receipt transaction that your company had refunded us. Apart from that, for the last 2 weeks we received further money deduction from our account even though you confirmed all rewards program and account for Mid City has been closed."* (Mr Ramen San owner, via Jessie Helyar churn evidence). Mr Chu venue demanding *"proof of those technical issues have been resolved and will not happen again in the future"* — venues are now requiring written guarantees.

**OKR**: OKR 3 — Churn reduction (friction in core venue experience)
**OST branch**: Friction in core venue experience → Billing/settlement trust
**Journey stage**: Ongoing engagement → Renewal-churn decision
**Recommended action**: **Discovery ticket** — audit refund pipeline for failure modes (wrong card, delayed processing, post-cancellation deductions). Mr Ramen San needs immediate refund proof sent to owner. Mr Chu needs engineering investigation of April 1 and April 15 failed transactions.

---

### 5. T002 / T003 — Double dipping and POS integration gaps are co-occurring, and First Table is winning the venues we lose

**Theme tags**: T002 (CHRONIC, 5+ weeks) + T003 (RISING, 3 weeks)
**Heat**: 🔴 **HIGH**
**Signal count**: T002: 2 signals | T003: 1 signal (5 venues) | Co-occurring: Brutal Embr Group
**Source count**: 1 (Slack) — single-source weakness
**Lifecycle**: T002 CHRONIC / T003 RISING — co-occurrence pattern strengthening weekly

**Problem statement**: Double dipping (customers stacking EatClub discounts with venue's own specials or competitor platforms) and POS integration gaps are compounding into a single competitive loss pattern. This week, 4 Pines - Welcome To Brunswick churned citing double dipping across 5 Bepoz terminals with 56% repeat customers, stating he's "losing money" and the settlement process is "uneconomical." Separately, Brutal Embr Group (5 venues — Dolly Wine Bar, Oliveti, Lune Bar, Spread Deli x2) churned to **First Table** specifically because First Table integrates with **Lightspeed + Now Book It**, giving them offer management + booking + POS in one platform. The AM (Gabriella Szabo) tried to use EatClub's new POS integration as a save argument, but Brutal Embr runs Lightspeed — and the integration isn't there yet. Annata also flagged a customer who used both First Table and EatClub for the same booking.

**Mom Test quality**: **STRONG** — Verbatim (4 Pines): *"His main concern... customers double dipping on their terminal on already in-place daily pub specials... He advised that he's losing money on those deals already and that more than half (56%) of his customers are repeat."* (Aaron Pantazis, churned_or_changed, 22 Apr). Verbatim (Brutal Embr): *"They want to consolidate all their offers and marketing through one platform and have decided to go with First Table... primarily due to integrating with now book it platform and the ability to run preferred offers with functionality."* (Gabriella Szabo, churned_or_changed, 21 Apr).

**OKR**: OKR 3 — Churn reduction (competitive loss vector)
**OST branch**: Product fit → POS integration / competitive positioning; Friction in core venue experience → Double-dipping prevention
**Journey stage**: Ongoing engagement → Renewal-churn decision
**Recommended action**: **Discovery ticket** — map all venues on Lightspeed, Bepoz, and other top POS systems to quantify exposure to First Table competitive threat. Prioritise Lightspeed integration given 6+ venue losses in 2 weeks specifically citing it. For double dipping: investigate POS-level enforcement (RedCat talking point from W16 not resolving it).

---

## 📋 All signals this week — classified

| # | Signal summary | Source | Author | Team | Who affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 Pines churn: double dipping on 5 Bepoz terminals, 56% repeat, losing money, settlement uneconomical | Slack | Aaron Pantazis | AM | 4 Pines (D783F41A) | STRONG | OKR3 | T002 | Friction → double-dipping |
| 2 | Annata: customer used both First Table and EatClub for same booking, venue requesting refund | Slack | Jasmine Jung | AM | Annata (342C2191) | STRONG | OKR3 | T002 | Friction → double-dipping |
| 3 | Brutal Embr Group (5 venues) churned to First Table for Lightspeed + Now Book It integration | Slack | Gabriella Szabo | AM | Dolly Wine Bar, Oliveti, Lune Bar, Spread Deli x2 | STRONG | OKR3 | T003 | Product fit → POS integration |
| 4 | Gogyo Surry Hills: group churn, busy season + own promos, POC hid behind directors | Churn | Elliot Rayment | AM | Gogyo Surry Hills (6437076F) | MEDIUM | OKR3 | T004 | Product fit → group retention |
| 5 | Gogyo Fitzroy: same group churn as Surry Hills | Churn | Elliot Rayment | AM | Gogyo Fitzroy (F6EC22AE) | MEDIUM | OKR3 | T004 | Product fit → group retention |
| 6 | Tom Phat: 2 DI offers redeemed Saturday when only TA scheduled — phantom one-off offer? | Slack | Cameron Landis | Unknown | Tom Phat (D9813551) | MEDIUM | OKR1 | T005 | System automation → deal integrity |
| 7 | ARRA Coffee & Wine: multiple deactivation requests since Apr 18, zero response, legal threat | HubSpot | Unknown | Unknown | ARRA Coffee & Wine | STRONG | OKR1 | T006 | System automation → OOO routing |
| 8 | Tatva Indian Kitchen: owner can't reach Josephine for a week, threatening cancellation | Slack | Nina Alcaraz | Unknown | Tatva Indian Kitchen | STRONG | OKR1 | T006 | System automation → OOO routing |
| 9 | Corlam Kitchen: emailed wrong inbox Apr 13, owner refuses all discussion, early churn | Slack | Tania Marinopoulos | AM | Corlam Kitchen (7A429331) | MEDIUM | OKR1 | T006 | System automation → OOO routing |
| 10 | NVG Group (6 venues): manual seat-time change request via Slack | Slack | Tania Marinopoulos | AM | Banksia, Aspendeli, Bonbeach, Eastwood, Mackie, Uncles Panini | STRONG | OKR1 | T007 | Manual AM task reduction |
| 11 | Partner Portal crashing during bulk deal updates | Slack | Elliot Rayment | AM | All portal-using AMs/venues | STRONG | OKR1 | T007 | Venue self-serve → portal stability |
| 12 | Deal prediction server (dpc.eatclubhub.com) read timeout since 23:59 Apr 23 | Slack | Martin Heal | Unknown | System-wide | STRONG | OKR1 | T007 | System automation → infrastructure |
| 13 | 16 Mixpanel bulk-edit venues (20–74 edits in single session) — AM-operated, not self-serve | Mixpanel | — | AM (inferred) | 16 venues (see restIDs below) | STRONG | OKR1 | T007 | Manual AM task reduction |
| 14 | Zircon Restaurant: looked at numbers, not making money, 41 customers, early churn | Churn | Cameron Landis | Unknown | Zircon (38E8ED66) | MEDIUM | OKR3 | T009* | Onboarding → value demonstration |
| 15 | Chaan Thai: can't maintain margin at 20% deals, saved March, churning again | Churn | Matthew Behan | BDM | Chaan Thai (9ECE95AC) | STRONG | OKR3 | T009* | Onboarding → deal economics education |
| 16 | Harry's Cafe churn: GST on commission not explained at sale, small cafe, no profit margin | Slack | Nicole Orr | AM | Harry's Cafe (F223B4E7) | STRONG | OKR3 | T009 | Onboarding → fee transparency |
| 17 | Noi Quattro + Pasta Factory (2 venues): giveaway miscommunication at sign-up | Slack | Jordana Anderson | Unknown | Noi Quattro (E8D421CC), Pasta Factory (74F0107F) | MEDIUM | OKR3 | T009 | Onboarding → promise alignment |
| 18 | Suanie's Cafe: frustrated that cancellation ≠ email as told at sign-up, declined all help | Slack | Elodie Fitzsimmons | Unknown | Suanie's Cafe (2C9BB1B4) | MEDIUM | OKR3 | T009 | Onboarding → exit process clarity |
| 19 | Khao Thai Little Bay churn: not seeing income difference, rising costs, not economical | Churn | Aaron Pantazis | AM | Khao Thai (70BFD0C5) | STRONG | OKR3 | T009 | Onboarding → value demonstration |
| 20 | Onda Bar churn: owner demands refunds for T&C breaches, won't accept contact-customer process | Slack | Jessie Helyar | Unknown | Onda Bar (5B6B3FC8) | STRONG | OKR3 | T010 | Friction → T&C enforcement |
| 21 | Mr Lee Malaysian Cuisine: 2 separate dine-in-for-takeaway incidents same week | HubSpot | Unknown | Unknown | Mr Lee Malaysian Cuisine | MEDIUM | OKR3 | T010 | Friction → T&C enforcement |
| 22 | Lulo Spice & Bar: customers arriving outside times, debt $160.74, refuses to pay citing T&C abuse | Slack + Churn | Cameron Landis | Unknown | Lulo Spice & Bar (C2E82FF1) | STRONG | OKR3 | T010/T013 | Friction → T&C enforcement |
| 23 | 8+ additional T&C abuse incidents in coverage (Chapati, VECINO, Les Bubbles, etc.) | Slack | Various | Various | Multiple venues | MEDIUM | OKR3 | T010 | Friction → T&C enforcement |
| 24 | Mr Ramen San churn: $65.63 refund outstanding since March + unauthorized post-cancellation charges | Slack + Churn | Jessie Helyar | Unknown | Mr Ramen San (51077CCA) | STRONG | OKR3 | T011 | Friction → billing trust |
| 25 | La Vallee $780.40 overcharge refunded to EatClub card instead of credit card | Slack | Tom McGay | AM | La Vallee customer | STRONG | OKR3 | T011 | Friction → billing trust |
| 26 | Bumbles Cafe: customer tapped twice, both charged from bank, neither reached venue | Slack | Pippa Keddie | AM | Bumbles Cafe (9F2D70F5) | MEDIUM | OKR3 | T011 | Friction → billing trust |
| 27 | Mr Chu: failed transactions Apr 1 + Apr 15 ($112 + $369), venue demanding proof of fix | Slack | Gabriella Szabo | AM | Mr Chu (659D0AA3) | STRONG | OKR3 | T011 | Friction → billing trust |
| 28 | Just Fresh Made: payment for Apr 13–19 not received | HubSpot | Pippa Keddie | AM | Just Fresh Made | MEDIUM | OKR3 | T011 | Friction → settlement reliability |
| 29 | Khao Thai Little Bay: no response to any contact, Aaron asking for in-person visit | Slack | Aaron Pantazis | AM | Khao Thai (70BFD0C5) | MEDIUM | OKR3 | T012 | Churn prediction → silence alerts |
| 30 | Mr D'z Cafe: no response to phone/email/text/IG DM, no txns since Feb, manually paused | Slack | Lukas Symonds | AM | Mr D'z Cafe (AFD46A0F) | STRONG | OKR3 | T012 | Churn prediction → silence alerts |
| 31 | Rascals Deli: closed on Google, no response since end of March | Slack (unmapped→T012) | Gabriella Szabo | AM | Rascals Deli (7289A236) | MEDIUM | OKR3 | T012 | Churn prediction → silence alerts |
| 32 | Yum Yum Tree (watch list): 1 portal session, 0 edits, 4 offers views — browsing not acting | Mixpanel | — | — | Yum Yum Tree (7831FFCB) | WEAK | OKR2 | T012* | Portal engagement → disengagement signal |
| 33 | Alexander Mediterranean (watch list): 1 session, 0 edits, 2 performance clicks — browsing only | Mixpanel | — | — | Alexander Med. (7D4929E5) | WEAK | OKR2 | T012/T013* | Portal engagement → disengagement signal |
| 34 | M Yong Tofu: offerless only, wants off but can't opt out, doesn't see value at 10% + $49 | Churn | Aaron Pantazis | AM | M Yong Tofu (13F64025) | STRONG | OKR3 | — | Product fit → offerless flexibility |
| 35 | Baba Ganouj: "I didn't like it" (repeated), early churn, missing transaction investigation | Churn | Matthew Behan | BDM | Baba Ganouj (A09F313F) | WEAK | OKR3 | — | Early churn → activation failure |
| 36 | Nurish Cafe: commission too high, running at loss, likely closing | Churn | Brianna Quinn | Unknown | Nurish Cafe (C97E55D0) | MEDIUM | OKR3 | — | External factors |
| 37 | East and Co Balwyn: churned but still receiving offerless transactions (3 instances this pattern) | Slack (unmapped) | Nicole Orr | AM | East and Co (5B7B39D6) | STRONG | OKR1 | NEW* | System automation → churn suppression |
| 38 | Contract not capturing deals set up via sign-up page | Slack (unmapped) | Katrina Siquian | BDM | Unknown | MEDIUM | OKR1 | NEW* | Onboarding → funnel integrity |
| 39 | Thunder Eatery: offers live in portal but not showing in app until Apr 28 | Slack | Emma Viezzi | BDM | Thunder Eatery (3C1C1477) | MEDIUM | OKR2 | — | Portal → app visibility sync |
| 40 | Gami Chicken & Beer Lilydale: venue closed, legal notices on door, needs removal | HubSpot | Unknown | Unknown | Gami Chicken (UNKNOWN) | MEDIUM | OKR3 | — | — |

**Churn CSV — venue closed/sold (not product-addressable, 8 venues)**: Di Francesco Cucina (closed), NC's Chaat and Dosa House (closed), Monsoon Palace (sold to Chedda Boy), Pot au Pho Bar Mornington (closed indefinitely), San Churro Southbank (sold back to HO), Mr Toast (sold, new owner not interested), Sideshow Burgers Rosanna (ownership change — re-signed), The Lil Hut Bardwell Park (sold), Rascals Deli (closed on Google). Melrose Restaurant churned with "missing features" and no further detail (Sam McKenzie unable to reach).

**Mixpanel bulk-edit restIDs (T007 evidence)**: D8EA79FC (74 edits), 6B7CCCDA (53), 9FACBEFE (34), 5E4330B3 (30), E72B41F4 (27), 8FE36B44 (26), 6AE576BC (26), 9E801D96 (25), 50C16601 (25), 4D8E5869 (23), 5C47DBB8 (22), BF61378B (21), F0329B86 (21), 31170ECD (20), 5340EBF5 (20). All 1-session patterns.

\* *Collector-mapped theme retained; asterisk indicates mapping is plausible but not explicitly confirmed by venue voice.*

---

## 🗺️ OST update

### OKR 1 root: Scale AM Optimisation

**Manual AM task reduction** — **STRENGTHENED SIGNIFICANTLY**
T007 is now the single highest-volume theme in the system. This week produced 16 Mixpanel bulk-edit patterns (observable AM labour), 3 Slack signals (portal crash, server outage, 6-venue manual seat-time change), and coverage notes documenting 20+ additional manual NCI boost and config requests. The portal being simultaneously *broken* and *insufficient for self-serve* is creating a compounding OKR1 failure: AMs can't even automate their workarounds. Sub-opportunity: NCI boost enablement and seat-time changes are the two most frequent manual request types — both should be highest-priority self-serve candidates.

**System automation** — **STRENGTHENED (new failure vector)**
T006 upgraded from "vacation coverage gap" to "any-scenario coverage gap." ARRA Coffee & Wine demonstrates that it's not just AM vacations — it's any scenario where a request enters the system without an owner. The pattern: (1) venue sends cancellation request, (2) no owner assigned or owner unavailable, (3) request sits unanswered, (4) platform continues operating on venue's behalf without consent, (5) financial harm accrues, (6) venue escalates. This is a system-design failure, not a people failure. Sub-opportunity: HubSpot workflow to auto-assign or escalate any deactivation/cancellation ticket not actioned within 48 hours.

**Venue self-serve capability** — **UNCHANGED (still blocked)**
Suanie's Cafe was offered portal training and declined — "lack of trust." Until T007's portal stability is resolved, pushing self-serve adoption is counterproductive. Venues won't trust a tool that crashes.

### OKR 2 root: Drive Deal Performance Through System-Led Actions

**Partner Portal engagement** — **MIXED**
Mixpanel shows 1,413 unique venues with portal events this week — a healthy base. But the signal-to-noise ratio is concerning: most high-edit venues are likely AMs, not venue operators. Among the ~84 venues with 10–19 edits, we can't confirm self-serve vs AM-operated without user-ID enrichment. Performance tab engagement remains very low — the vast majority of venues have 0 performance-tab clicks.

**Deal score visibility and trust** — **NO NEW DATA**
Deal score collector returned zero signals. T001 (397 zero-score venues as of W16) remains structurally invisible. No AM flagged zero-score accounts this week. No Slack discussion. This is a silent OKR2 blocker — venues with score=0 have no deals to engage with.

**Watch list Mixpanel signals** — **WEAK DISENGAGEMENT PATTERN**
Yum Yum Tree Victoria Park (WATCH: AM non-responsive complaint) logged 1 session with 4 offers-tab views but 0 edits. Alexander Mediterranean (WATCH: $266 debt, 14-day silence) logged 1 session with 2 performance clicks but 0 edits. Both are looking without acting — the portal isn't converting their attention into behaviour change.

### OKR 3 root: Churn Reduction

**Friction in core venue experience** — **ESCALATING**
T010 and T011 are both producing confirmed churns (Onda Bar, Mr Ramen San) with clear causal chains. T010 has crossed the 12+ signal threshold and is now the highest-volume churn driver among product-addressable themes. T011's billing failures are producing legal-adjacent language ("remove our bank account details from your system completely").

**POS integration / competitive loss** — **STRENGTHENED (First Table pattern confirmed)**
The Brutal Embr 5-venue loss to First Table validates the Spread Deli pattern from W15. First Table's advantage is specifically Lightspeed + Now Book It integration. This is now 6+ venues lost to the same competitor for the same reason in 2 weeks. A Lightspeed venue count would quantify total exposure.

**Onboarding journey quality** — **STRENGTHENED (new root cause)**
T009 is RISING with 4+ new signals. The most specific pattern is fee/discount misunderstanding at point of sale: GST on commission not explained (Harry's), giveaway mechanics miscommunicated (Noi Quattro, Fress from W16), "discount applies to total bill" confusion. The unmapped signal about contracts not capturing sign-up-page deals (Katrina Siquian) may be a root cause — if deals configured at sign-up aren't persisting to the contract, that's the mechanism creating the expectation gap.

**Group churn pattern** — **NEW INSTANCE**
Gogyo (2 venues, Surry Hills + Fitzroy) is a new group cascade churn alongside Ramen Ippudo (8 venues, W16). That's 2 group churns in 2 weeks, 10 venues total. The Gogyo reason differs (busy season + own promotions) from Ippudo, but the structural vulnerability is the same: when a group decision-maker says no, multiple venues exit simultaneously with no venue-level save opportunity.

---

## ⚠️ Friction stack watch

### 🚨 ARRA Coffee & Wine — CRITICAL / LEGAL RISK
**restID**: UNKNOWN — needs immediate lookup
**Signals**: T006 (HubSpot: multiple deactivation requests unanswered since Apr 18, legal threat)
**Analysis**: Single-source but EXTREME severity. Venue has been explicitly requesting deactivation for 8+ days with zero response. Platform continued operating offers without consent, causing ongoing financial harm. Owner threatening formal legal action. **This requires same-day senior intervention. Flag to Luke and Pan immediately.**

### 🚨 The Last Jar — CRITICAL / 4th CANCEL ATTEMPT
**restID**: EC9FABAF-1C92-4C45-8C6F-79B836A09D20
**Signals**: T010 (W16 watch list: 4th cancel request from Bryony citing dine-in-for-takeaway abuse, booking walk-outs; 3 prior retain attempts failed)
**Analysis**: No new in-window signals (HubSpot watch list scan found nothing in scanned pages), but existing watch list status is CRITICAL. 4 cancellation attempts over T&C abuse with 3 failed retains = this venue will churn. The question is whether the churn teaches us anything about systemic T&C enforcement failure. **Flag to Luke — if retaining, needs fundamentally different offer (venue-side enforcement tool), not another save call.**

### Garibaldi Pizzeria — CRITICAL / UNRESOLVED FROM W15
**restID**: UNKNOWN — needs lookup
**Signals**: W15+W16 multi-channel urgent contacts from Angie, CS escalation
**Analysis**: No new in-window signals found (HubSpot coverage gap likely — venue was not in scanned pages). Carried from W15 watch list. **Flag to Luke — status unknown, needs manual check.**

### Lulo Spice & Bar — CHURNED / FRICTION STACK CONFIRMED
**restID**: C2E82FF1-730F-4921-A6BE-26B963856D69
**Signals**: T010 (arrival time T&C abuse) + T013 ($160.74 debt) + early churn + blacklisted
**Sources**: 2 (Slack + Churn)
**Journey stages**: Activation → Ongoing engagement → Renewal-churn decision (3 stages)
**Analysis**: Classic friction stack — signed Nov 2025, churned, re-signed March, debt accumulated within 3 weeks, T&C abuse complaints, owner dodged calls, now blacklisted. The re-sign-then-rapid-churn pattern suggests the original churn reason was never resolved. Debt now in collections (Nancy Tandual).

### Mr Ramen San The Nova — CHURNED / FRICTION STACK CONFIRMED
**restID**: 51077CCA-E630-4551-BB38-1CED8858F7F9
**Signals**: T011 (delayed refund $65.63 since March + unauthorized post-cancellation charges) + offerless issues
**Sources**: 2 (Slack + Churn)
**Journey stages**: Ongoing engagement → Billing dispute → Renewal-churn decision
**Analysis**: Refund pipeline failure is the root cause. Owner Royston has said he'll reactivate if refund proof is provided. Emma (senior) emailed receipt — awaiting response. Winback possible if billing team delivers quickly.

### 4 Pines - Welcome To Brunswick — CHURNING / MULTI-THEME
**restID**: D783F41A-4BBE-4799-8982-BDA5275B5BC8
**Signals**: T002 (double dipping, 56% repeat, 5 POS terminals) + T003 (Bepoz + Lightspeed on food truck) + settlement process frustration
**Sources**: 1 (Slack)
**Journey stages**: Ongoing engagement → Renewal-churn decision
**Analysis**: Referred to Kane Russell (AM), offered fee waiver + offerless. Still refusing — "feels too convoluted." The double dipping problem on 5 terminals suggests a fundamental POS-level enforcement gap. Even if POS integration existed for Bepoz, the venue has mixed systems (Bepoz + Lightspeed). This is a product architecture problem, not an AM save problem.

### Tatva Indian Kitchen — AT RISK / IMMEDIATE
**restID**: UNKNOWN — needs lookup
**Signals**: T006 (owner can't reach AM Josephine for a week, cancellation ultimatum)
**Sources**: 1 (Slack)
**Analysis**: Josephine Fatorma (AM) appears unreachable. Owner gave deadline of "tomorrow" (from 23 Apr post). If no contact made by 24 Apr, venue likely already in churn pipeline. **Check if Josephine is on leave. If so, reassign immediately.**

### Annata — WATCH / ACTIVE BUT FLAGGING
**restID**: 342C2191-4A42-4E46-A5A1-A735B0EA08F0
**Signals**: T002 (double dipping with First Table) + Mixpanel (11 offer edits, 10 offers views — actively engaged)
**Sources**: 2 (Slack + Mixpanel)
**Analysis**: Venue is still engaged on portal but flagged a customer who used both First Table and EatClub for the same booking. If this incident is not resolved satisfactorily, it could escalate. AM Jasmine Jung is handling. Good intervention opportunity — venue is still bought in.

### Watch list venues with no new signals (HubSpot coverage gap):
- **Masala Flames** (6A3A7879): ESCALATING. No in-window signals. No Slack discussion. 5+ month iOS bug. Engineering owner still absent.
- **Lumen Alley** (B0A4E510): ESCALATING. No in-window signals. Deal revert 2nd occurrence. Configuration trust broken.
- **La Botte Pizza Pascoe Vale** (DB6BD926): WATCH. No new signals. Monitor.
- **Everest MoMo Station** (D82CAAD0): WATCH. No new signals. Cancel email from March still unactioned, $148.08 dispute.
- **Delhi Darbar Surfers Paradise** (B6D9E9C6): WATCH. No new signals. Billing bug (Invalid membershipBillingDay 0).
- **Yum Yum Tree Victoria Park** (7831FFCB): WATCH. Mixpanel shows browsing-not-acting. "No one bothered to call me" from W16.
- **Alexander Mediterranean** (7D4929E5): WATCH. Mixpanel shows 2 performance clicks, 0 edits. $266 debt, 14-day silence.

---

## 💡 Synthesis notes

**What surprised me:**

The ARRA Coffee & Wine signal is the most alarming thing in this run. A venue has been explicitly requesting deactivation for 8+ days, received zero response, is still being charged, and is threatening legal action. This isn't a product signal — it's an operational emergency. The fact that it appeared in HubSpot (which only scanned ~6% of tickets) means there could be *other* similar cases in the unscanned 94%. This is a T006 escalation that suggests the problem isn't just AM vacations — it's that the cancellation/deactivation workflow has no failsafe at all.

The Brutal Embr 5-venue loss to First Table is the most strategically important churn this week. It's not a venue that "didn't see value" — it's a venue group that *did* see value in a competitor's integration architecture. First Table is winning specifically on Lightspeed + Now Book It integration. With Spread Deli from W15 (same group, confirmed), this is 5 venues from a single decision. How many more Lightspeed venues are in the portfolio and vulnerable to the same pitch?

Tom McGay — flagged in T001 as having 28 zero-score accounts — authored the La Vallee $780.40 refund signal this week. An AM with 28 disengaged venues is still actively handling high-dollar billing disputes. This is OKR1 in miniature: AM time is being consumed by reactive firefighting instead of proactive engagement with their dormant portfolio.

**What is missing:**

1. **Deal score data**: The collector returned zero signals. Either the CSV is stale or the pipeline is broken. We have no Week 17 zero-score count and no movement data. T001 (397 zero-score venues) is being tracked on faith, not data.
2. **Venue voice from meetings**: Granola has been empty for 2 consecutive weeks. Without meeting data, all signals are second-hand (AM/BDM reports). We're not hearing venue owners directly.
3. **HubSpot depth**: 94% of tickets unscanned. The 9 watch list venues all returned zero results. ARRA Coffee & Wine may be the tip of a larger backlog of unactioned requests.
4. **User-ID on Mixpanel**: We can't distinguish AM-operated portal sessions from venue-operated ones. The bulk-edit heuristic (20+ edits in 1 session) is a proxy, but venues with 10–19 edits could be either. This limits OKR2 measurement.
5. **Post-churn interviews**: 21 venues churned this week. We have churn notes for all, but zero structured post-churn interviews. The signal quality would dramatically improve with even 3–5 exit interviews per week.

**Interview questions to sharpen weakest signals:**

| Theme | Questions |
|---|---|
| T010 (T&C abuse) | "When a customer abuses the booking T&C, what do you do right now? How long does it take to resolve? What would 'having control' over this look like to you?" |
| T007 (Portal self-serve) | "When you need to change your deal settings, what's the first thing you do? Have you tried Partner Portal? What happened?" |
| T009 (Onboarding) | "Before you signed up, what did you understand about how the discount works? What surprised you in the first month?" |
| T002 (Double dipping) | "Can you walk me through the last time you caught a customer double dipping? How did you know? What did it cost you?" |
| T011 (Billing) | "When you check your settlement, what are you looking for? When was the last time something didn't match?" |

**What would move OKR 1 most?**

Building self-serve flows for the top 5 AM-performed actions on Partner Portal: (1) NCI boost toggle, (2) seat-time changes, (3) guest-limit adjustments, (4) no-show buffer settings, (5) bulk offer editing. The 16 Mixpanel bulk-edit patterns represent minimum ~5 hours of AM time *this week alone* on just the bulk-edit subset. The portal crash and deal prediction server outage need to be resolved first — you can't drive self-serve adoption on a broken tool. Separately, implementing automated HubSpot routing for cancellation/deactivation requests (T006) would prevent the ARRA-style failures without requiring any AM time at all.

**What would move OKR 2 most?**

Performance tab engagement is near-zero across most venues. Venues are logging into Portal, viewing offers, even editing — but not looking at how their deals perform. The system isn't surfacing "what should I do next?" in a way that connects to revenue outcomes. A guided action prompt on login ("Your Thursday deals drove 12 covers last week — want to extend to Wednesdays?") would be the smallest intervention with the largest potential OKR2 impact. But this depends on deal prediction working — which it wasn't for part of this week.

---

## Routing block