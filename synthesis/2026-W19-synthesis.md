**Sources available this run**: Slack, HubSpot, Deal Score, Churn, Mixpanel
**Sources unavailable / failed**: Granola (no customer-facing meetings in window — agent skipped)
**Confidence note**: This run covers a ~27-hour window (2026-05-03 20:20 to 2026-05-04 23:20) for real-time sources, not a full week. Deal score data covers the first 4 days of the April month-end cycle (4,426 venues parsed). Slack activity was light — 6 of 10 AU channels returned zero messages. HubSpot notes were largely empty Slack-sync stubs. No Granola meeting data means zero direct venue-owner voice this run — all qualitative evidence is AM-reported, CS-reported, or venue-submitted tickets. Heat scores should be read as directional within a narrow window; weekly cadence will sharpen confidence. Twelve authors appearing in signals are not found in the staff directory (Orel Cohen Berenson, Jordan Wellard, Jessie Helyar, Brianna Quinn, Jai Richards, Mark Savaille, Cameron Landis, Nancy Tandual, Elodie Fitzsimmons, Nestor Acuram, Jesstoni Santiago, Lyann) — either the directory is incomplete or these are recent hires/contractors. Team attribution for their signals defaults to "unknown team."

---

## 🔥 Rising Themes This Week

### 1. T003 — Customers exploiting offers in ways venues can't prevent or the platform can't enforce

**Theme tag**: T003
**Heat**: 🔴 HIGH
**Signal count**: 6 qualitative | **Source count**: 2 (Slack, HubSpot)
**Lifecycle**: CHRONIC (4+ weeks) — default HIGH heat; this run reinforces with single-day epidemic-level DI-for-TA volume

**Problem statement**: Customers are using dine-in vouchers for takeaway, arriving in oversized parties, and redeeming outside booking conditions. The platform has no systemic enforcement mechanism, so every incident requires manual CS intervention — contact the customer, explain T&Cs, request refund for the venue. Three separate DI-for-TA incidents appeared in cs-and-am within a single day (Curryville, My Little Siam, Honki Tonki), plus a 15-person party on a 2-person booking at Seasons Provedore and a repeat offender pattern at Gilbees. This is not isolated abuse — it's a structural gap where the platform permits behavior it then has to manually clean up.

**Mom Test quality**: STRONG — every signal describes a specific observed incident with identifiable cost to the venue.
> "Please reach out to these customers who have redeemed dine in offers and asked for take away. Please advise cx of T&Cs and ask for a refund for the venue." — Gabriella Szabo (AM), Honki Tonki
> "Booked at venue and brought 15 people. Refunding venue for 9 pax of float. Please call to charge back and warn them of T&Cs" — Tom McGay (AM), Seasons Provedore

**OKR**: OKR3 (Churn Reduction) — primary. Also OKR1 (AM/CS operational drag).
**OST branch**: OKR3: Friction in core venue experience → Customer behavior enforcement gap
**Journey stage**: Ongoing engagement
**Recommended action**: **Discovery ticket** — Scope the DI-for-TA enforcement problem: what would it take to prevent takeaway redemption on dine-in offers at the platform level? Current CS manual intercept workflow is unscalable and burning capacity. Also investigate party-size enforcement at booking level.

---

### 2. T005 — Venues don't believe EatClub is worth what they pay, and the platform can't show them otherwise

**Theme tag**: T005
**Heat**: 🔴 HIGH
**Signal count**: 9 qualitative + 49 deal score drops (27 venues to zero) | **Source count**: 4 (Slack, HubSpot, Churn, Deal Score)
**Lifecycle**: CHRONIC (4+ weeks) — default HIGH; reinforced by the largest deal score hemorrhage in the dataset this run

**Problem statement**: Venues are disengaging from deals en masse — 27 venues hit deal score 0 from positive scores in the first 4 days of the month. Qualitative signals converge on the same root: venues can't see their ROI. The Performance tab exists in Partner Portal but ~65-70% of actively engaged Portal users never click it even once (Mixpanel data). Venues are editing offers blind. When they can't see value, they stop running deals, and when they stop running deals, the AM has to manually convince them to re-engage — or they churn. Five confirmed churns this run cite economics/value directly (Zircon, Khao Thai, Chaan Thai, M Yong Tofu, Nurish Cafe).

**Mom Test quality**: STRONG — specific past behavior with stated cost/consequence.
> "He looked at the numbers and they weren't making any money — just over a month on the platform." — Cameron Landis (unknown team) re: Zircon Restaurant
> "Commission/percentage is too high. Everything is very expensive now — making the current partnership unsustainable." — Nurish Cafe (venue-submitted HubSpot ticket)
> "Cannot maintain their profit margin with even 20% deals. They run way too lean. Saved in March but churning again." — Matthew Behan (BDM) re: Chaan Thai

**OKR**: OKR2 (Deal Performance) — primary. Also OKR3 (Churn).
**OST branch**: OKR2: Deal score visibility and trust → Performance tab adoption. OKR3: Surfacing product value through data.
**Journey stage**: Ongoing engagement → Renewal-churn decision
**Recommended action**: **Escalate** — The Performance tab non-adoption is the single highest-leverage OKR2 blocker. Venues managing deals without seeing results creates a doom loop: no visibility → no engagement → deal score drops → AM manual intervention → churn. Needs product investigation into why Performance tab isn't being used and what would make it the first thing venues check.

---

### 3. T006 — Multi-venue operators churn as a group and the platform has no early warning

**Theme tag**: T006
**Heat**: 🔴 HIGH
**Signal count**: 7+ (2 confirmed group churns + 3 deal score group patterns) | **Source count**: 3 (Churn, HubSpot, Deal Score)
**Lifecycle**: RISING (3 weeks) — normally capped at Medium but meets override criteria: 6+ signals across 2+ sources AND active churn risk with confirmed venue losses

**Problem statement**: EatClub has no relationship layer above the individual venue. When a group operator decides to leave, there's no structural way to detect or prevent the cascade. This run confirms two new group patterns: Gogyo (Surry Hills + Fitzroy, both churned — "POC hid behind the directors decision and would not include them on any meeting attempts") and Chargrill Charlie's (Drummoyne requesting termination citing "head office required," while Annandale dropped from 292→6 and Bondi from 187→3). Additionally, Burrito Bar (Burpengary + Caboolture both hit 0), and Mr Ramen San's cascade continues — The Nova threatening to cease "effective immediately" over a still-unresolved $65.63 refund from Mid City.

**Mom Test quality**: STRONG — confirmed group churns with specific behavioral evidence.
> "Group churned as they are coming into their busy season… My POC hid behind the directors decision and would not include them on any meeting attempts." — Elliot Rayment (AM) re: Gogyo
> "Head office required [termination]. Also, I have closed the deal every day last week, why you still charge me?" — Chargrill Charlie's Drummoyne (venue-submitted)
> "Since we continue to have issues with Eatclub for Mid City site, we decided to stop entire partnership with Eatclub for Nova site as well." — Mr Ramen San owner

**OKR**: OKR3 (Churn Reduction) — primary.
**OST branch**: OKR3: Product fit for enterprise-Groups → Group account layer / Multi-venue early warning
**Journey stage**: AM relationship → Renewal-churn decision
**Recommended action**: **Discovery ticket** — Define what a "group account" looks like: shared dashboard, group-level contact mapping, cascade risk alerting when one venue in a group shows churn signals. The Gogyo evidence is particularly instructive — AM couldn't reach decision-makers because the POC gatekept. A group layer would need to map the decision hierarchy, not just the operational contact.

---

### 4. T002 — Venues can't self-serve basic configuration, so AMs absorb the cost manually

**Theme tag**: T002
**Heat**: 🔴 HIGH
**Signal count**: 8 | **Source count**: 3 (Slack, HubSpot, Mixpanel)
**Lifecycle**: CHRONIC (4+ weeks) — default HIGH; Mixpanel bulk edit patterns provide first quantitative confirmation of AM proxy editing

**Problem statement**: Venues need to change sitting times, max pax, offer time windows, and trading hours — but Partner Portal doesn't support these changes. Every request becomes a Slack message or HubSpot ticket that an AM or CS agent processes manually. When the AM is unavailable (vacation, departure), the request goes unanswered and the venue is stuck. This run captures 3 manual config requests in Slack (Stockroom Cafe sitting time, Jin Bar max pax, Global Kitchen trading hours), 2 in HubSpot (GoGiYo time exclusion, Nawabi Taste offer change), 1 AM vacation coverage gap (Pizza Miltonio), and 2 Mixpanel sessions with 28 and 23 offer edits in a single sitting — almost certainly AMs editing on behalf of venues rather than self-serve.

**Mom Test quality**: MEDIUM-STRONG — specific requests with operational cost, but no direct venue-owner quotes about frustration (signals are all AM/CS-reported).
> "Could you please update the sitting time to 1.5 hours? It's a small café in a business building." — Jasmine Jung (AM), Stockroom Cafe
> "We are currently running our own early bird promotion… customers using EatClub are receiving double discounts. To avoid this overlap, we would like to exclude dinner from EatClub." — GoGiYo Korean BBQ (venue-submitted)

**OKR**: OKR1 (Scale AM Optimisation) — primary. This is the most direct OKR1 opportunity.
**OST branch**: OKR1: Venue self-serve capability → Partner Portal config self-serve / OKR1: Manual AM task reduction → Automate config change requests
**Journey stage**: Ongoing engagement
**Recommended action**: **Discovery ticket** — Prioritize the top 3 highest-volume manual config changes for Portal self-serve: sitting time, max pax, and meal-period/time-window exclusions. These are simple value writes that shouldn't require human intermediation.

---

### 5. T007 — Post-cancellation billing failures are creating new debt-churn loops and legal risk

**Theme tag**: T007
**Heat**: 🔴 HIGH
**Signal count**: 6 | **Source count**: 3 (Slack, HubSpot, Churn)
**Lifecycle**: CHRONIC (4+ weeks) — default HIGH; this run surfaces a new and dangerous sub-pattern: venues being billed after confirmed cancellation

**Problem statement**: The classic T007 pattern — debt accumulates, venue goes silent, churn becomes inevitable — remains active. But this run reveals a compounding failure: venues that have already cancelled are still being charged. Chapman Lane Cafe cancelled under Rob (since departed), continued to be billed, submitted 3 duplicate escalation tickets, and is now threatening legal action. Chargrill Charlie's Drummoyne says "I have closed the deal every day last week, why you still charge me?" Yogurbella sold the business, stopped offers, still being debited. These aren't debt-silence patterns — they're system failures creating new debt that shouldn't exist, and they carry legal and reputational risk beyond normal churn.

**Mom Test quality**: STRONG — specific actions, specific charges, specific consequences.
> "I canceled my account but still you are taking money from my account. I will take illegal action and I am going to cancel your direct debit from bank. I emailed you so many times but still I don't get any response." — Chapman Lane Cafe owner (HubSpot ticket)
> "He said he didn't have to [pay his debt] because customers weren't following T's and C's." — Cameron Landis (unknown team) re: Lulo Spice ($160.74 debt, using T&C abuse as non-payment justification)

**OKR**: OKR3 (Churn Reduction) — primary.
**OST branch**: OKR3: Friction in core venue experience → Post-cancellation billing process / AM departure handover
**Journey stage**: Renewal-churn decision (and post-churn — this is damaging the brand after the relationship has already ended)
**Recommended action**: **Escalate to Luke** — Chapman Lane Cafe needs immediate intervention (legal threat). **Discovery ticket** — Map the billing deactivation workflow: when a venue is confirmed churned, what prevents continued charging? The Chapman Lane case suggests an AM departure without handover left the cancellation unactioned. The Chargrill Charlie's and Yogurbella cases suggest closing deals doesn't stop fee billing.

---

## 📋 All Signals This Week — Classified

### Qualitative Signals (Slack, HubSpot, Churn)

| Signal summary | Source | Author | Team | Affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| La Cabra Mexican: asked to cancel 2 months ago, went on loyalty, now wants to pause, not interested in loyalty only | Slack | Orel (Ellie) | Unknown | La Cabra (venue) | S | OKR3 | T005 | Value data |
| Bittersweet: removed deals, went offerless, owner "just doesn't want to deal with it," no-showed meetings, ignoring calls | Slack | Lukas Symonds | AM | Bittersweet (venue) | M | OKR3 | T005 | Value data |
| Sekka Dining: early pause, not interested in offers, multiple reconnect attempts failed | Slack | Jasmine Jung | AM | Sekka Dining (venue) | M | OKR3 | T005 | Value data |
| Shiroi Orange: paused hub a day after first transaction, doesn't want to be on platform | Slack | Nader Masrour | AM | Shiroi Orange (venue) | S | OKR3 | T001 | Onboarding |
| Blue Heaven: retail store connected to restaurant, can't prevent offer use on retail items → churn | Slack | Jordan Wellard | Unknown | Blue Heaven (venue) | S | OKR3 | T004 | Venue friction |
| Bistro Bondi: closed due to landlord lease dispute | Slack | Jordan Wellard | Unknown | Bistro Bondi (venue) | S | OKR3 | — | External |
| ARRA Coffee & Wine: venue sold, disable account | Slack | Jay Franklin | AM | ARRA (venue) | S | — | — | External |
| Chapman Lane: still being charged after cancellation, AM (Rob) departed, no handover, CS can't find account owner | Slack | Nestor Acuram | Unknown (CS?) | Chapman Lane (venue) | S | OKR3 | T007 | Post-cancel billing |
| Pizza Miltonio: AM on vacation, no coverage assigned, venue issue unresolved | Slack | Jesstoni Santiago | Unknown (CS?) | Pizza Miltonio (venue) | M | OKR1 | T002 | Manual task |
| Gilbees Wine Bar: customer booked Friday night, redeemed EC offer improperly, venue proactively caught it, "having a lot of EC customer issues of this nature" | Slack | Cameron Landis | Unknown | Gilbees (venue) | S | OKR3 | T003 | Venue friction |
| Curryville: customer used DI deal for TA, CS asked to contact and explain T&Cs | Slack | Jessie Helyar | Unknown | Curryville (venue) | S | OKR3 | T003 | Venue friction |
| My Little Siam: customer used DI deal for TA, venue charged customer difference, refund needed | Slack | Jessie Helyar | Unknown | My Little Siam (venue) | S | OKR3 | T003 | Venue friction |
| Honki Tonki: multiple customers redeemed DI offers for TA, venue requesting CS enforcement | Slack | Gabriella Szabo | AM | Honki Tonki (venue) | S | OKR3 | T003 | Venue friction |
| Seasons Provedore: customer booked for 2, brought 15, refunding venue for 9 pax float | Slack | Tom McGay | AM | Seasons Provedore (venue) | S | OKR3 | T003 | Venue friction |
| Stockroom Cafe: AM requesting sitting time update to 1.5 hours | Slack | Jasmine Jung | AM | Stockroom (venue) | M | OKR1 | T002 | Self-serve |
| Jin Bar: BDM requesting max pax limit to 4 | Slack | Aashna Lal | BDM | Jin Bar (venue) | M | OKR1 | T002 | Self-serve |
| Global Kitchen: trading hours mismatch between HubSpot and contract | Slack | Angelica | Unknown | Global Kitchen (venue) | M | OKR1 | T002 | Self-serve |
| Chapman Lane (HubSpot): "I canceled but still you are taking money. I will take illegal action." 3 duplicate tickets filed. | HubSpot | Venue owner | Venue | Chapman Lane (venue) | S | OKR3 | T007 | Post-cancel billing |
| Chargrill Charlie's Drummoyne: "Head office required termination. I closed the deal every day, why still charging me?" | HubSpot | Venue owner | Venue | CC Drummoyne (venue) + group | S | OKR3 | T006/T007 | Groups + billing |
| Millers Espresso: "charged for sales that never came through my cafe, no response, cancel immediately" | HubSpot | Venue owner | Venue | Millers Espresso (venue) | S | OKR3 | T007 | Venue friction |
| Yogurbella: "sold business, stopped offer, still being debited" | HubSpot | Venue owner | Venue | Yogurbella (venue) | S | OKR3 | T007 | Post-cancel billing |
| GoGiYo: "own early bird promo overlaps with EC, customers getting double discounts, want to exclude dinner" | HubSpot | Venue owner | Venue | GoGiYo (venue) | S | OKR1 | T002 | Self-serve |
| The Frankston Curry Club: customer took takeaway on DI deal | HubSpot | Venue owner | Venue | Frankston Curry Club (venue) | S | OKR3 | T003 | Venue friction |
| The Nawabi Taste: "want to change our offers — 10% off 4:30-6:30pm, remove 25% off" submitted via ticket | HubSpot | Venue owner | Venue | Nawabi Taste (venue) | M | OKR1 | T002 | Self-serve |
| Som Saa Wok and Grill: consumer reports "inflated pricing — 40% off still higher than walk-in price" | HubSpot | Consumer | Consumer | Som Saa (venue reputation) | M | OKR3 | — | Venue friction |
| Malee Made in Thailand: consumer ordered, drove there, closed, money taken | HubSpot | Consumer | Consumer | Malee (consumer) | M | OKR2 | T004 | Portal/platform |
| Mr Ramen San The Nova: $65.63 refund unresolved for months, further deductions after cancellation, ceasing Nova partnership | Churn | Jessie Helyar | Unknown | Mr Ramen San group (2 venues) | S | OKR3 | T006/T007 | Groups + billing |
| Zircon Restaurant: "looked at numbers, not making money, just over a month on platform." AOV $110, 41 customers. | Churn | Cameron Landis, Kane Russell | Unknown, AM | Zircon (venue) | S | OKR3 | T005 | Value data |
| Monsoon Palace: venue sold to Chedda Boy, couldn't convert new owner | Churn | Lyann, Nader Masrour | Unknown, AM | Monsoon Palace (venue) | S | OKR3 | — | External |
| M Yong Tofu: on offerless, only paying 10% + $49, wants to cancel, offered lower rate on return | Churn | Aaron Pantazis | AM | M Yong Tofu (venue) | S | OKR3 | T005 | Value data |
| Di Francesco Cucina: venue closed, offers to be disabled | Churn | Tom McGay | AM | Di Francesco (venue) | S | OKR3 | — | External |
| Khao Thai: "not seeing any difference in income, rising costs, not economical." Offered offerless, declined. | Churn | Aaron Pantazis | AM | Khao Thai (venue) | S | OKR3 | T005 | Value data |
| NC's Chaat and Dosa House: venue closed, owner returning to IT career | Churn | Cameron Landis | Unknown | NC's Chaat (venue) | S | OKR3 | — | External |
| Rascals Deli: permanently closed on Google, unreachable since end of March | Churn | Gabriella Szabo | AM | Rascals Deli (venue) | S | OKR3 | — | External |
| Chaan Thai: "cannot maintain profit margin with even 20% deals, saved in March but churning again" | Churn | Matthew Behan | BDM | Chaan Thai (venue) | S | OKR3 | T005 | Value data |
| Lulo Spice: $160.74 debt, using T&C abuse as grounds for non-payment, owner dodging calls, blacklisted | Churn | Cameron Landis, Nancy Tandual | Unknown, Unknown | Lulo Spice (venue) | S | OKR3 | T003/T007 | Venue friction + billing |
| Gogyo Surry Hills: group churn, "POC hid behind directors decision," wouldn't include directors in meetings | Churn | Elliot Rayment | AM | Gogyo group (2+ venues) | S | OKR3 | T006 | Groups |
| Gogyo Fitzroy: identical group churn pattern | Churn | Elliot Rayment | AM | Gogyo group | S | OKR3 | T006 | Groups |
| Baba Ganouj: "I didn't like it" (repeated 4x), early churn, BDM in contact | Churn | Matthew Behan | BDM | Baba Ganouj (venue) | W | OKR3 | T001 | Onboarding |
| Melrose Restaurant: no details given, trying to reach out | Churn | Sam McKenzie | AM | Melrose (venue) | W | OKR3 | — | Unknown |
| San Churro Southbank: owner sold venue back to HO, new owners incoming | Churn | Matthew Behan | BDM | San Churro (venue) | S | OKR3 | — | External |
| Pot au Pho Mornington: venue closed indefinitely, may sell or close permanently | Churn | Tania Marinopoulos | AM | Pot au Pho (venue) | S | OKR3 | — | External |
| Mr Toast: new owner doesn't want third-party partners, not convertible | Churn | Brianna Quinn | Unknown | Mr Toast (venue) | S | OKR3 | — | External |
| Sideshow Burgers Rosanna: ownership change, need to rechurn and resign new contract | Churn | Elodie Fitzsimmons | Unknown | Sideshow (venue) | S | OKR3 | — | External |
| The Lil Hut: venue sold, new owner not interested in EC referral | Churn | — | — | The Lil Hut (venue) | M | OKR3 | — | External |
| My Place: called to cancel, financial reasons, BDM Otis contacted | Churn | Gabriella Szabo | AM | My Place (venue) | M | OKR3 | T005 | Value data |
| Nurish Cafe: "commission too high, everything expensive, running at a loss, likely closing" | Churn | Kane Russell, Brianna Quinn | AM, Unknown | Nurish Cafe (venue) | S | OKR3 | T005 | Value data |

### Deal Score Patterns (60 signals total — notable entries below)

| Pattern | Venues | AM concentration | OKR | Theme |
|---|---|---|---|---|
| **Critical drops (≥300 pts)**: Vegan Thai-Riffic 935→0, Thai Ginger 935→0, Raato Ghar 756→0, Cozy Pizza 637→0, Frankston Curry Club 795→244, Say Cheeese 935→465, Maximoon 807→448, Bakmi Lim 339→13 | 8 venues | Jessie Helyar ×3, Tom McGay ×2, Nader Masrour ×1, Aaron Pantazis ×1, Jay Franklin ×1 | OKR2 | T005 |
| **Score to zero (from 100+)**: 27 venues dropped to 0 from positive scores in 4 days | 27 venues | Jordan Wellard ×6, Jai Richards ×5, Mark Savaille ×4, Jessie Helyar ×4, Tom McGay ×3 | OKR2 | T005 |
| **Group patterns**: CC Annandale 292→6, CC Bondi 187→3 (matches Drummoyne cancel request); Burrito Bar Burpengary 146→0, Burrito Bar Caboolture 148→0 | 4 venues (2 groups) | Jordan Wellard, Brianna Quinn; Mark Savaille ×2 | OKR3 | T006 |
| **Watch list hits**: The Last Jar 42→0, Lumen Alley 14→0, Delhi Darbar 32→0, Masala Flames (6A3A) 6→0, Masala Flames (225D) 0→14, La Botte Pizza 69→12 | 5 venues (6 entries) | Various | OKR2/3 | T004/T005 |
| **Score rises (≥500)**: Pizza Miltonio 135→900, Salt Bar 0→698, Zambrero Kwinana/Buranda/Rockingham Central all 0→532 | 5 venues | Matthew Behan ×1, Jessie Helyar ×1, Elliot Rayment ×3 | OKR2 | Positive |

### Mixpanel Portal Patterns (100 signals, 617 unique venues)

| Pattern | Evidence | OKR | Theme |
|---|---|---|---|
| **Bulk edit (AM proxy)**: 2 sessions with 28 and 23 edits respectively — single sessions with high edit counts indicate AM editing on behalf of venue | restIDs: E2F0C0ED, D8EA79FC | OKR1 | T002 |
| **Performance tab avoidance**: ~65-70% of top 100 engaged venues had 0 performance-tab clicks despite active offer editing | 617 unique venues, ~430 never clicked Performance | OKR2 | T005 |
| **Healthy self-serve**: ~30 venues with 5+ edits AND offers-tab views in proportion = genuine self-serve behavior | Various | OKR2 | Positive |

---

## 🗺️ OST Update

### OKR 1: Scale AM Optimisation

**Manual AM task reduction** — STRENGTHENED
- 3 new manual config requests (sitting time, max pax, trading hours) in a single day across Slack
- 2 HubSpot tickets for offer changes/time exclusions that should be Portal self-serve
- AM vacation gap surfaced again (Pizza Miltonio) — no formal coverage protocol
- AM departure gap surfaced (Chapman Lane — Rob left, no handover, venue billed post-cancel)

**Venue self-serve capability** — STRENGTHENED
- GoGiYo explicitly needs time-window exclusion to prevent double-discounting with own promotions
- Nawabi Taste submitting basic offer changes via HubSpot ticket rather than Portal
- Mixpanel confirms 2 bulk-edit sessions that are almost certainly AMs editing on behalf of venues

**System automation** — NO CHANGE
- No new signals. Opportunity remains: automate the DI-for-TA enforcement (currently manual CS workflow) and post-cancellation billing deactivation.

### OKR 2: Drive Deal Performance Through System-Led Actions

**Partner Portal engagement** — MIXED
- 617 venues active in a 2-day window = positive adoption signal
- But most engagement is offer-editing only; Performance tab is being ignored
- 2 bulk-edit sessions suggest some "engagement" is AM proxy, not venue self-serve

**Venue-led revenue actions** — WEAKENED
- 27 venues hit deal score 0 from positive scores in 4 days
- 8 critical drops (≥300 pts) — venues pulling back sharply, not gradually
- This suggests venues are making active decisions to disengage from deals, not drifting

**Deal score visibility and trust** — STATUS QUO / WEAKENED
- No direct signals about deal score confusion this run
- But mass withdrawal from deals + Performance tab avoidance = venues managing blind
- New sub-opportunity: the 3 Zambrero activations (all 0→532) show that when venues DO engage, deal scores respond dramatically — this is a proof point that could be surfaced to other venues

### OKR 3: Churn Reduction

**Friction in core venue experience** — STRENGTHENED (most active this run)
- DI-for-TA at epidemic volume (3 venues in one day)
- Post-cancellation billing failures (3 venues: Chapman Lane, CC Drummoyne, Yogurbella)
- Blue Heaven: platform can't scope offers to restaurant vs. retail — structural gap
- 21 churns in this window, 5 explicitly citing financial/value reasons

**Product fit for enterprise-Groups** — STRENGTHENED
- Gogyo: 2-venue cascade confirmed. POC gatekeeper pattern identical to Ramen Ippudo.
- Chargrill Charlie's: 3-venue group pattern forming (Drummoyne cancel, Annandale and Bondi score collapse)
- Burrito Bar: 2-venue coordinated score drop to 0
- Mr Ramen San: cascade from $65.63 continues to expand

**Onboarding journey quality** — WEAKENED (new evidence)
- Shiroi Orange: paused day after first transaction (earliest possible signal of mismatched expectation)
- Baba Ganouj: "I didn't like it" ×4, early churn

**Surfacing product value through data** — CRITICAL GAP CONFIRMED
- ~65-70% of active Portal users never click Performance tab
- Venues are editing offers without any visibility into what's working
- This is the connective tissue between OKR2 and OKR3: if venues could see value, they'd keep running deals; if they keep running deals, they don't churn

---

## ⚠️ Friction Stack Watch

### ⛔ Chapman Lane Cafe | restID: UNKNOWN — needs lookup
**Sources**: Slack (cs-and-am) + HubSpot (3 duplicate tickets)
**Journey stages**: AM relationship (broken — AM departed) + Renewal-churn decision (post-churn billing failure)
**Signals**:
- Venue cancelled under Rob (since departed), no handover trail
- Still being charged, multiple emails sent with no response
- 3 duplicate HubSpot tickets filed
- Owner threatening legal action: "I will take illegal action"
- CS asking "who is now handling this account?" in Slack — no one knows

**Analysis**: This is the most operationally urgent item this run. The venue has already churned — the problem is EatClub is still charging them after cancellation with no one assigned to resolve it. This creates legal exposure and reputational damage. **FLAG TO LUKE IMMEDIATELY.**

### ⛔ The Last Jar | restID: EC9FABAF-1C92-4C45-8C6F-79B836A09D20
**Sources**: Watch List (CRITICAL, W16) + Deal Score (42→0)
**Journey stages**: Ongoing engagement (deal score zero) + Renewal-churn decision (4th cancel attempt)
**Signals**:
- 4th cancel request from Bryony (from watch list history)
- Deal score dropped to 0 — venue fully disengaged from deals
- T&C abuse cited (dine-in for takeaway, booking walk-outs)
- AM: Josephine Fatorma (AM)
- 3 prior retain attempts failed

**Analysis**: With deal score at 0 and 4th cancel request, this venue is almost certainly irrecoverable. Recommend clean exit to preserve relationship for potential re-sign. **FLAG TO LUKE.**

### 🔴 Mr Ramen San group | restIDs: 51077CCA (Nova, churned), Mid City (previously churned)
**Sources**: Churn (confirmed Nova churn threat) + Historical (Mid City billing dispute)
**Journey stages**: AM relationship + Renewal-churn decision (cascade)
**Signals**:
- $65.63 refund from Mid City still unresolved after months
- Further deductions from account after cancellation
- Owner Royston "decided to stop entire partnership with Eatclub for Nova site as well"
- Escalated to Emma for senior apology; waiting on refund receipt confirmation
- AM: Jessie Helyar (unknown team)

**Analysis**: Classic T006 group cascade from a $65.63 billing error. The dollar amount is trivial; the trust damage is total. Emma has sent the receipt — response pending. If Nova can be saved, it depends entirely on whether the refund proof is accepted. Time-sensitive.

### 🔴 Chargrill Charlie's group | restIDs: DA61BCCD (Drummoyne), E0D640EF (Annandale), 4EA934A7 (Bondi)
**Sources**: HubSpot (Drummoyne cancel request) + Deal Score (Annandale 292→6, Bondi 187→3)
**Journey stages**: Ongoing engagement (deal score collapse) + Renewal-churn decision (head office mandate)
**Signals**:
- Drummoyne: "head office required" termination + billing complaint
- Annandale: deal score 292→6 (Jordan Wellard, unknown team)
- Bondi: deal score 187→3 (Brianna Quinn, unknown team)
- Group decision cascading across at least 3 locations

**Analysis**: Head office has decided. Individual venue AMs likely can't prevent this — needs Sam Benjamin / group relationship owner to intervene at HO level if salvageable. At minimum, identify how many CC locations are on EatClub and monitor all of them.

### 🟡 Masala Flames Indian Cuisine | restIDs: 6A3A7879 (primary, watch list), 225D80DE (secondary)
**Sources**: Deal Score (6A3A→0, 225D→14) + Watch List (ESCALATING, W14–W16)
**Journey stages**: Activation (iOS dine-in invisible 5+ months) + Ongoing engagement (deal score at 0)
**Signals**:
- iOS dine-in invisible for 5+ months per watch list
- Zero Slack discussion this run — bug going silent
- No engineering DRI assigned
- Deal score for primary restID dropped to 0
- Two restIDs in deal score data — may indicate separate locations or data duplication
- AM: Pippa Keddie (AM)

**Analysis**: This is a 5-month-old activation failure with no owner. The silence this run is alarming — if no one is tracking the fix, it will simply persist indefinitely. The venue is accumulating friction: can't be found on iOS + deal score at zero + no visible progress. Needs engineering DRI assignment.

### 🟡 Lumen Alley Coffee & Bagels | restID: B0A4E510-B0D2-4892-A311-5066FCA654F4
**Sources**: Deal Score (14→0) + Watch List (ESCALATING, W15–W16)
**Journey stages**: Ongoing engagement (deal revert) + Renewal-churn decision (score at 0)
**Signals**:
- Deal score dropped to 0
- Deal revert was 2nd occurrence (W15+W16 per watch list)
- Platform trust broken — venue configures deals, platform reverts them
- AM: Tania Marinopoulos (AM)

**Analysis**: Deal score at 0 with a recurring deal revert bug = venue has likely given up trying to manage deals. If the revert bug isn't resolved, no amount of AM outreach will restore engagement.

### 🟡 The Frankston Curry Club | restID: 11DC1A88 (deal score) / unknown (HubSpot)
**Sources**: HubSpot (T&C abuse report) + Deal Score (795→244, -550)
**Journey stages**: Ongoing engagement (deal score crash + customer abuse)
**Signals**:
- Customer took takeaway on DI deal (HubSpot report)
- Deal score dropped 550 points — one of the largest critical drops this run
- AM: Aaron Pantazis (AM)

**Analysis**: Two friction layers stacking: customer abuse eroding trust + massive deal score drop suggesting deal pullback. Worth AM proactive check-in.

### 🟡 Delhi Darbar — Surfers Paradise | restID: B6D9E9C6-5C0D-486D-B5A4-43B9C81D66A5
**Sources**: Deal Score (32→0) + Watch List (WATCH, W16)
**Journey stages**: Ongoing engagement (deal score zero) + AM relationship (billing bug)
**Signals**:
- Deal score dropped to 0
- Invalid membershipBillingDay 0 bug (from watch list)
- Pause requested W16
- AM: Pippa Keddie (AM)

**Analysis**: Billing bug + deal score at 0 + pause request = three friction layers. The billing bug is a platform failure, not a venue decision — needs technical resolution.

---

## 💡 Synthesis Notes

### What surprised me

**The post-cancellation billing cluster is new and dangerous.** Three venues this run (Chapman Lane, Chargrill Charlie's Drummoyne, Yogurbella) are being charged after confirmed cancellation. This isn't the T007 "debt accumulates → silence → churn" pattern — it's a process failure where billing continues after the relationship has ended. Chapman Lane's legal threat makes this urgent. The AM departure handover gap (Chapman Lane was Rob's) suggests there's no automated billing deactivation when churn is confirmed — it relies on a human to turn it off, and when that human leaves, nobody else knows to do it.

**DI-for-TA has crossed from "recurring problem" to "daily operational load."** Three separate incidents in cs-and-am in a single day, each requiring manual CS intervention (contact customer, explain T&Cs, process refund). The Slack drift observation nails it: "the manual CS intercept workflow is absorbing significant CS capacity with no systemic fix." This is now both a T003 (venue trust) and an OKR1 problem (CS capacity drain).

**Performance tab non-adoption is the hidden OKR2 killer.** The Mixpanel data tells a clear story: venues are editing offers but ~65-70% never look at performance data. They're managing deals blind. This explains the deal score hemorrhage — venues pull back because they can't see what's working. It also explains the T005 churn pattern — "I looked at the numbers and they weren't making money" is what happens when the only "numbers" venues see are their own till, not EatClub's attribution.

**The staff directory has significant gaps.** 12 authors in this run's signals don't appear in either the AM or BDM list. Several of these (Jordan Wellard, Jessie Helyar, Brianna Quinn, Jai Richards) appear multiple times as venue account managers. This limits team attribution confidence and suggests the directory needs updating.

### What is missing

1. **Granola data** — No meeting transcripts means no direct venue-owner voice on problems. All qualitative evidence is mediated through AM notes, CS channels, or venue-submitted tickets. We're hearing about venue problems, not hearing from venues.
2. **Watch list venue activity** — Zero watch list hits in Slack or HubSpot this run. Garibaldi Pizzeria (CRITICAL) has gone completely silent across all channels. Alexander Mediterranean ($266 debt, 14+ day silence) extends another week with no visible outreach.
3. **AM proactive outreach data** — We can see when venues contact EatClub (HubSpot tickets) and when AMs process churns (Slack), but we can't see AM proactive outreach. For the deal score drops (27 venues to zero), we don't know if AMs are reaching out or if these venues are silently disengaging.
4. **Jordan Wellard concentration** — 6 Sydney venues under this one person all dropping significantly. Is this an AM performance issue, a regional market issue, or are these connected venues? Can't determine without directory confirmation and additional context.

### Interview questions to sharpen weakest signals

**T005 — Performance tab non-adoption** (sharpening the "why"):
- "When you log into Partner Portal, what are you trying to find out? Walk me through your last session."
- "Have you ever looked at the Performance tab? What did you expect to see vs. what you actually saw?"
- "When you decide whether to change your deals, what information do you use? Where do you get it?"

**T006 — Group account needs** (sharpening the "what"):
- For Chargrill Charlie's HO (if accessible): "When you decided to pull venues off EatClub, who was involved in that decision? What information would have changed it?"
- For any multi-venue operator: "How do you currently compare performance across your venues? What does your head office look at?"

**T001 — Early churn expectation gap** (sharpening the "when"):
- For Shiroi Orange owner: "What did you expect to happen after your first day on the platform? What actually happened?"
- For recently onboarded venues (within 30 days): "Is the product working the way you thought it would when you signed up? What's different?"

### What would move OKR 1 most?

**Unblock Portal self-serve for the top 3 manual config changes: sitting time, max pax, and time-window exclusions.** This run captured 5 distinct manual requests for these exact config changes (Stockroom Cafe, Jin Bar, Global Kitchen, GoGiYo, Nawabi Taste) plus 2 Mixpanel bulk-edit sessions that are almost certainly AMs editing on behalf of venues. These are simple value writes — the venue knows what they want, but the Portal doesn't let them do it. Every one of these creates a Slack message or HubSpot ticket that an AM or CS agent has to process. Multiply across the full venue base and this is likely the single largest category of avoidable AM manual work.

### What would move OKR 2 most?

**Make the Performance tab the default landing state — or surface its core insight (ROI attribution) directly in the offers editing flow.** Venues are engaging with the Portal for offer management (617 unique venues in 2 days), but they're not crossing to Performance. The data is there; the behavior gap is navigation. If venues saw "this deal generated $X in revenue this week" inline with their offer editing, they'd have the feedback loop needed to make better deal decisions. This is the missing link between "venues engage with Portal" and "venues take revenue-driving actions."

---

## Routing Block