**Sources available this run**: Slack (10 AU channels, 114 messages), HubSpot (300 tickets, 200 notes), Churn (21 AU closures), Mixpanel (4,952 events across 931 venues)
**Sources unavailable / failed**: Granola (url_not_accessible on 1 meeting — Eatclub x Vault x Mastercard billing optimisation; unlikely venue signal anyway), Deal Score (skipped — day 3 of month, CSV resets on 1st; no deal score movement data available)
**Confidence note**: Moderate-high on qualitative signals (Slack + HubSpot + Churn align well), moderate on quantitative (Mixpanel available but venue names unresolved for restIDs; deal score absent means the 397-venues-at-zero benchmark from T005 cannot be refreshed). HubSpot notes pipeline was effectively empty — 197 of 200 notes were Slack/Teams placeholder stubs with no body. This means AM relationship quality data is missing. Granola failure removes strategic meeting context. Multiple authors (Jordan Wellard, Jessie Helyar, Elodie Fitzsimmons, Cameron Landis, Lyann, Brianna Quinn, Nancy Tandual) are not in staff_directory — likely CS or newer hires. Their team defaults to "unknown." No watch list venues except La Botte and Yum Yum Tree generated new signals this window — the silence from Garibaldi (CRITICAL) and The Last Jar (CRITICAL) is itself a signal worth investigating.

---

### 🔥 Rising themes this week

---

**1. Venues cannot self-serve basic configuration — AMs absorb every change**
- **Theme tag**: T002
- **Heat**: HIGH
- **Signal count**: 19 signals across 3 sources (Slack, HubSpot, Mixpanel)
- **Lifecycle**: CHRONIC (6+ weeks)
- **Problem statement**: Venues have no way to make routine configuration changes — opening hours, guest limits, NCI/RCI boosts, surcharges, dining time windows — through Partner Portal. Every change requires an AM or BDM to manually process the request via Slack or HubSpot. This week alone: 8 distinct config requests surfaced in Slack's churned_or_changed channel (Honki Tonki 4pax/90min cap, Chargrill Charlie's 1hr window, Grand View Hotel 1.5hr window, Frankston Curry Club NCI+RCI, Geppetto NCI+RCI, Ladygreen NCI+RCI, La Perla NCI+2hr window, Yenyum Thai 90min). 3 more came through HubSpot tickets (Chuck Trailer's recurring hours, Teaology Lab surcharge + offer count, AUN Japanese holiday hours + guest limit). Critically, Mixpanel reveals 6 venues where a single user made 20–62 offer edits in one session — the behavioural fingerprint of an AM bulk-editing on behalf of a venue, not venue self-serve. BDMs are also absorbing this work: Prudence Madigan (BDM) submitted a guest limit change for La Botte and I Sapori.
- **Mom Test quality**: STRONG — *"I have attempted to update our hours but it seems to be only allowing '1 off' updates. Could you please update our hours of operation to: Mon-Fri: 4pm-9pm"* (Chuck Trailer's, HubSpot). 62 offer edits in 1 session from a single restID (Mixpanel). These are specific, repeated, quantifiable manual tasks.
- **OKR**: OKR1 (primary — direct AM hour drain), OKR2 (secondary — Portal self-serve gap)
- **OST branch**: Manual AM task reduction → Venue self-serve capability (recurring hours, guest limits, NCI/RCI, surcharges, dining windows)
- **Journey stage**: Ongoing engagement
- **Recommended action**: Discovery ticket — the Chuck Trailer's "1 off updates" complaint is the sharpest signal; it names the exact product gap. Combine with Mixpanel bulk-edit data to size the AM time impact.

---

**2. Venues don't believe EatClub is worth what they're paying — and can't see their own ROI**
- **Theme tag**: T005
- **Heat**: HIGH
- **Signal count**: 11 signals across 3 sources (Slack, HubSpot, Churn)
- **Lifecycle**: CHRONIC (6+ weeks)
- **Problem statement**: Venues are churning because they conclude EatClub is unprofitable for them. The reasoning varies — high food costs vs. discount depth (Oramesti, 35% COGS), margins too thin at 20% offers (Chaan Thai, "saved in March but churning again"), commission structure on offerless transactions perceived as unfair (M Yong Tofu), or just "not seeing any difference in income" (Khao Thai). Underlying all of these: venues are benchmarking EatClub against full-price revenue rather than incremental covers, and Performance tab — the only in-product ROI visibility tool — has near-zero usage. Of the top 100 Portal users this window, the majority had 0 performance-tab clicks. Only 7 venues had 7+ performance clicks. Venues are managing offers blind, then concluding the platform isn't working.
- **Mom Test quality**: STRONG — *"His main concern is low margins due to high food costs (min 35%) and low menu pricing, and he is comparing EatClub performance to full-price trading rather than treating it as incremental revenue"* (Oramesti, Elodie Fitzsimmons). *"Venue cannot maintain their profit margin with even 20% deals. They run way too lean. Saved in March but churning again"* (Chaan Thai, Matthew Behan). 5 confirmed churns this window cite financial/value reasons with specific economics.
- **OKR**: OKR3 (primary — direct churn driver), OKR2 (secondary — Performance tab underperformance)
- **OST branch**: Surfacing product value through data → Performance tab discoverability & utility; Friction in core venue experience → post-sale ROI education
- **Journey stage**: Ongoing engagement → Renewal-churn decision (most T005 signals are at the churn decision point)
- **Recommended action**: Discovery ticket — the compounding of "venue can't see ROI" (Performance tab near-zero) with "venue concludes ROI is negative" (churns) is the central loop to break. Investigate whether Performance tab is undiscoverable, unusable, or showing unhelpful data.

---

**3. Customer abuse eroding venue trust — now being weaponised to justify non-payment**
- **Theme tag**: T003
- **Heat**: HIGH
- **Signal count**: 5 signals across 3 sources (Slack, HubSpot, Churn)
- **Lifecycle**: CHRONIC (6+ weeks)
- **Problem statement**: Customers are exploiting EatClub offers in ways venues cannot prevent — dual-account fraud to stack discounts, dine-in vouchers used for takeaway, arriving hours outside booking windows to game higher offers, and serial no-shows. Venues bear the full financial loss with no systemic enforcement mechanism. New this week: Bang Bang St Kilda lost $360.26 in a single incident where a customer booked under two names to combine a 35% + 10% discount, and the venue was charged commission on both. At Geppetto Trattoria, customer Noah Walkinshaw redeemed 10+ offers across lunch and dinner over a month without showing up. The dangerous escalation flagged last week — venues using T&C abuse as grounds for non-payment — is now confirmed: Lulo Spice churned with $160.74 debt, owner explicitly stated *"he didn't have to [pay] because customers weren't following T's and C's."*
- **Mom Test quality**: STRONG — *"A customer who booked with us under one name, and also receiving a 35% and additional 10% discount under a different name... This has resulted in a loss for us of $360.26 (as we were charged commission as well). There were 2 other tables that day that did the same thing"* (Bang Bang, HubSpot). Specific dollar amounts, named customers, repeated incidents.
- **OKR**: OKR3 (primary — direct churn driver and now debt justification)
- **OST branch**: Friction in core venue experience → Customer behaviour enforcement mechanisms
- **Journey stage**: Ongoing engagement
- **Recommended action**: Escalate — the T&C-abuse-as-debt-justification pattern (Lulo Spice) is a financial risk that will compound. Discovery ticket for systemic customer enforcement (repeat offender detection, booking-time compliance checks, multi-account detection).

---

**4. Group and franchise venues churn in cascades — no product layer to detect or prevent it**
- **Theme tag**: T006
- **Heat**: HIGH
- **Signal count**: 5 signals across 2 sources (Slack, Churn)
- **Lifecycle**: RISING (3 weeks) — pattern now confirmed with new cascade events
- **Problem statement**: EatClub has no group-level product layer. When a group-level decision-maker decides to leave, all venues churn simultaneously with no early warning. This week Gogyo confirmed the exact pattern previously identified: AM (Elliot Rayment) could not access the decision-making directors; the point-of-contact *"hid behind the directors decision and would not include them on any meeting attempts."* Result: 2 venues churned (Surry Hills + Fitzroy). Separately, Mr Ramen San Nova confirmed the cascade churn from a $65.63 billing error — the owner (Royston) has now escalated to cancelling the Nova site as well, pending proof of refund. San Churro shows a third pattern: franchise-level ownership changes (Surfers Paradise sold, Southbank sold back to HO) occurring simultaneously with no franchise-level relationship to coordinate.
- **Mom Test quality**: STRONG — *"Group churned as they are coming into their busy season... My POC hid behind the directors decision and would not include them on any meeting attempts"* (Gogyo, Elliot Rayment AM). This is the identical pattern to the Ramen Ippudo cascade from prior weeks, independently reproduced. Confirmed.
- **OKR**: OKR3 (primary — multi-venue churn from single decision)
- **OST branch**: Product fit for enterprise-Groups → Group account layer, multi-venue visibility, group-level decision-maker access
- **Journey stage**: Renewal-churn decision (group-level)
- **Recommended action**: Discovery ticket — the Gogyo and Mr Ramen San cascades validate the thesis with zero ambiguity. The product question is now: what does a minimum viable group layer look like that gives AMs visibility above individual venue?

---

**5. Debt accumulation + venue silence = predictable churn — still no automated detection**
- **Theme tag**: T007
- **Heat**: HIGH
- **Signal count**: 5 signals across 2-3 sources (Slack, Churn, Watch list carryover)
- **Lifecycle**: CHRONIC (6+ weeks)
- **Problem statement**: Venues with outstanding balances who go silent for 14+ days are on a predictable path to churn. This week's confirmation: Lulo Spice churned with $160.74 debt after dodging BDM calls and refusing payment (citing T&C abuse). Khukuri Restaurant churned after being "non responsive to any of our communication" across three different EatClub contacts (Otis, Elodie, Gabriella). San Churro Surfers Paradise generated a DD dispute after sale — old owner contesting charges that hit the new owner's account. Watch list venues remain unresolved: Alexander Mediterranean ($266 debt, 14+ day silence, no new signal), Everest MoMo Station ($148.08 dispute, cancel email from March still not actioned).
- **Mom Test quality**: STRONG — *"I spoke to him yesterday — complained about EC customers arriving outside of arrival times... I asked if he was going to pay his debt and he said he didn't have to because customers weren't following T's and C's — cancelling this account as early churn and have blacklisted in HS — Nancy to pursue debts"* (Lulo Spice, Cameron Landis). Specific debt amounts, specific timelines, confirmed outcome.
- **OKR**: OKR3 (primary — debt + silence → churn)
- **OST branch**: Friction in core venue experience → automated debt-silence detection and AM alerting
- **Journey stage**: Ongoing engagement → AM relationship → Renewal-churn decision (full stack)
- **Recommended action**: Discovery ticket — the detection signal is clear and quantifiable ($ debt + days silent). The question is whether this can be automated to trigger AM/CS intervention before the venue decides to churn.

---

**Notable: T001 (Mismatched expectation at sale) is FADING**
T001 was tagged RISING but generated zero strong signals this window. Zaiqah (surprise decision-maker who "hates discounting") and Muse Noosa (husband hard no despite wife being open) weakly echo the BDM-didn't-secure-full-buy-in pattern, but neither involves the discount-applies-to-total-bill or commission surprise dynamics that define T001. Recommend moving lifecycle to FADING. Monitor next run.

**Notable: T004 (Platform reliability and trust) holds at RISING**
6 scattered signals (Hecho en Mexico login failure, Onice double charge, Yum Yum Tree card decline, Amici Pizza not visible post-onboarding, Win back boost error on Customs House Hotel, Three Little Pigs portal hours mismatch) across 2 sources. These are different bugs rather than a single systematic failure. RISING lifecycle confirmed, but capped at Medium heat due to scatter. The Masala Flames iOS visibility bug (5+ months, ESCALATING on watch list) remains the highest-severity individual T004 issue but generated no new signals this window.

---

### 📋 All signals this week — classified

| # | Signal summary | Source | Author | Team | Who affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|---|
| 1 | La Botte + I Sapori: 4 guest max request via BDM | Slack | Prudence Madigan | BDM | Venues (La Botte, I Sapori) | STRONG | OKR1 | T002 | Venue self-serve: guest limits |
| 2 | Honki Tonki: customer Yi Ee arrived 2hrs late + others used dine-in for takeaway; refund requested | Slack | Gabriella Szabo | AM | Honki Tonki | STRONG | OKR3 | T003 | Customer behaviour enforcement |
| 3 | Hecho en Mexico: venue can't login to dashboard, error on 2 emails + incognito | Slack | Poppy Hill | BDM | Hecho en Mexico | STRONG | OKR2 | T004 | Portal access barriers |
| 4 | Onice: customer double-charged (card declined then went through), venue wants clarity | Slack | Jasmine Jung | AM | Onice | MEDIUM | OKR2 | T004 | Billing/payment reliability |
| 5 | KiKi Pan Asian: owner requested or threatened churn, wants Earn turned off | Slack | Jordan Wellard | Unknown | KiKi Pan Asian | MEDIUM | OKR3 | T005 | Value perception |
| 6 | BOBBYQ: disabling deals for months, $2k offerless revenue, won't discuss — confirmed churn | Slack | Jessie Helyar | Unknown | BOBBYQ | STRONG | OKR3 | T005 | Value perception |
| 7 | Oramesti: 35% food costs, comparing EC to full-price, rejected 20% and Loyalty — confirmed churn | Slack | Elodie Fitzsimmons | Unknown | Oramesti | STRONG | OKR3 | T005 | Post-sale ROI education |
| 8 | Cafe 5: frustrated with 30% offers, reduced to 15%, still wants to leave, rejected Loyalty | Slack | Elodie Fitzsimmons | Unknown | Cafe 5 | STRONG | OKR3 | T005 | Value perception |
| 9 | Zaiqah: surprise decision-maker (parents), cultural opposition to discounting — churn | Slack | Lukas Symonds | AM | Zaiqah | MEDIUM | OKR3 | T001 | BDM buy-in verification |
| 10 | Muse Noosa: wife open but husband hard no, 3 people tried — churn | Slack | Jessie Helyar | Unknown | Muse Noosa | WEAK | OKR3 | T001 | BDM buy-in verification |
| 11 | Liliana's Trattoria: standing firm on leaving, no reason given — churn | Slack | Pippa Keddie | AM | Liliana's Trattoria | WEAK | OKR3 | — | — |
| 12 | Khukuri: non-responsive to 3 contacts (Otis, Elodie, Gabriella) — churn | Slack | Gabriella Szabo | AM | Khukuri | STRONG | OKR3 | T007 | Debt + silence detection |
| 13 | San Churro Surfers: sold business, DD dispute with old owner, new charges hit new owner | Slack | Pippa Keddie | AM | San Churro Surfers | MEDIUM | OKR3 | T007 | Billing transition on venue sale |
| 14 | Honki Tonki: 4pax + 90min dining cap request (manual) | Slack (cov.) | Gabriella Szabo | AM | Honki Tonki | STRONG | OKR1 | T002 | Venue self-serve: guest/time limits |
| 15 | Chargrill Charlie's Bondi + Annandale: 1hr offer window (manual, 2-venue request) | Slack (cov.) | — | — | Chargrill Charlie's x2 | STRONG | OKR1 | T002/T006 | Venue self-serve: time windows / group config |
| 16 | Grand View Hotel: 1.5hr window request (manual) | Slack (cov.) | — | — | Grand View Hotel | STRONG | OKR1 | T002 | Venue self-serve: time windows |
| 17 | Frankston Curry Club: NCI+RCI request (manual) | Slack (cov.) | — | — | Frankston Curry Club | STRONG | OKR1 | T002 | Venue self-serve: NCI/RCI |
| 18 | Geppetto: NCI+RCI request (manual) | Slack (cov.) | — | — | Geppetto | STRONG | OKR1 | T002 | Venue self-serve: NCI/RCI |
| 19 | Ladygreen: NCI+RCI request (manual) | Slack (cov.) | — | — | Ladygreen | STRONG | OKR1 | T002 | Venue self-serve: NCI/RCI |
| 20 | La Perla: NCI + 2hr window request (manual) | Slack (cov.) | — | — | La Perla | STRONG | OKR1 | T002 | Venue self-serve: NCI + time windows |
| 21 | Yenyum Thai: 90min limit request (manual) | Slack (cov.) | — | — | Yenyum Thai | STRONG | OKR1 | T002 | Venue self-serve: time limits |
| 22 | Geppetto: Noah Walkinshaw 10+ no-show redemptions over 1 month | Slack (cov.) | Jay Franklin | AM | Geppetto | STRONG | OKR3 | T003 | Repeat offender detection |
| 23 | Amici Pizza: not visible in app post-onboarding | Slack (cov.) | Jesstoni Santiago | Unknown | Amici Pizza | STRONG | OKR2 | T004 | Onboarding reliability |
| 24 | Customs House Hotel: Win back boost error | Slack (cov.) | Tom McGay | AM | Customs House Hotel | MEDIUM | OKR2 | T004 | Feature reliability |
| 25 | Three Little Pigs: portal hours differ from live configuration | Slack (cov.) | Matthew Cahill | BDM | Three Little Pigs | MEDIUM | OKR2 | T004 | Config sync reliability |
| 26 | Mala Mia: product too rigid for event-driven operators; can't edit offers daily | Slack (unmap.) | Elodie Fitzsimmons | Unknown | Mala Mia | MEDIUM | OKR1 | T002 | Real-time offer self-serve for high-frequency operators |
| 27 | Oramesti: comparing EC to full-price yield, not incremental — framing gap | Slack (unmap.) | Elodie Fitzsimmons | Unknown | Oramesti | MEDIUM | OKR3 | T005 | Post-sale ROI education |
| 28 | REST-406: recurring platform error noted as semi-frequent by product team | Slack (unmap.) | Adam Glegg | Unknown (eng) | Unknown | WEAK | OKR2 | T004 | Platform error triage |
| 29 | Bang Bang: $360.26 loss from dual-account discount stacking + commission charged on both | HubSpot | — | — | Bang Bang St Kilda | STRONG | OKR3 | T003 | Multi-account fraud detection |
| 30 | Yum Yum Tree: EatClub card declined twice at venue, app showed 6% anytime | HubSpot | — | — | Yum Yum Tree Vic Park | STRONG | OKR2 | T004 | Payment reliability |
| 31 | Chuck Trailer's: can't update recurring hours, Portal only allows "1 off" updates | HubSpot | — (mentions Elliot) | — | Chuck Trailer's Bondi | STRONG | OKR1 | T002 | Venue self-serve: recurring hours |
| 32 | Teaology Lab: surcharge + offer count change requested via AM | HubSpot | Matthew Behan | BDM | Teaology Lab | MEDIUM | OKR1 | T002 | Venue self-serve: surcharges |
| 33 | The Terrace Thai: wants to permanently disable dine-in deals, reason unclear | HubSpot | — | — | The Terrace Thai | MEDIUM | OKR3 | — | Unclear — needs AM follow-up |
| 34 | Siew's Kopitiam: deleting 30% offer, reason "offerTooHigh" | HubSpot | — | — | Siew's Kopitiam | MEDIUM | OKR3 | T005 | Value perception: discount depth |
| 35 | Bodrum Essendon: deleting Sunday offers, reason "other" | HubSpot | Tom McGay | AM | Bodrum Essendon | WEAK | OKR3 | — | Unclear |
| 36 | AUN Japanese: holiday hours + guest limit (6→4) change via AM | HubSpot | — | — | AUN Japanese | MEDIUM | OKR1 | T002 | Venue self-serve: guest limits + holidays |
| 37 | Mr Ramen San Nova: $65.63 refund dispute → cascade to Nova cancellation, waiting on receipt proof | Churn | Jessie Helyar | Unknown | Mr Ramen San (Nova + Mid City) | STRONG | OKR3 | T006/T007 | Group cascade / billing trust |
| 38 | Zircon: "looked at numbers, not making money" after 1 month, AOV $110, 41 customers | Churn | Cameron Landis / Kane Russell | Unknown / AM | Zircon | STRONG | OKR3 | T005 | Early activation value visibility |
| 39 | Monsoon Palace: venue sold to Chedda Boy, couldn't convert new owner | Churn | Lyann / Nader Masrour | Unknown / AM | Monsoon Palace | HIGH-conf | OKR3 | — | Venue-sold conversion process |
| 40 | M Yong Tofu: on offerless, 10% commission + $49 fee, wants off but can't — churn | Churn | Aaron Pantazis | AM | M Yong Tofu | STRONG | OKR3 | T005 | Offerless value perception |
| 41 | Di Francesco Cucina: venue closed permanently | Churn | Tom McGay | AM | Di Francesco | HIGH-conf | OKR3 | — | — (unpreventable) |
| 42 | Khao Thai: "not seeing any difference in income," rising food/delivery costs — churn | Churn | Aaron Pantazis | AM | Khao Thai | STRONG | OKR3 | T005 | ROI visibility |
| 43 | NC's Chaat: owner closed venue, business too slow, returning to IT career | Churn | Cameron Landis | Unknown | NC's Chaat | HIGH-conf | OKR3 | — | — (unpreventable) |
| 44 | Lulo Spice: $160.74 debt, re-signed then paused 3 weeks later, using T&C abuse as non-payment justification — blacklisted | Churn | Cameron Landis / Nancy Tandual | Unknown | Lulo Spice | STRONG | OKR3 | T003/T007 | T&C abuse → debt justification |
| 45 | Gogyo Surry Hills: group churn, POC "hid behind directors decision," won't include them in meetings | Churn | Elliot Rayment | AM | Gogyo (group) | STRONG | OKR3 | T006 | Group decision-maker access |
| 46 | Gogyo Fitzroy: same group churn as Surry Hills — identical pattern | Churn | Elliot Rayment | AM | Gogyo (group) | STRONG | OKR3 | T006 | Group decision-maker access |
| 47 | Baba Ganouj: "I didn't like it" × 6, early churn, missing transactions | Churn | Matthew Behan | BDM | Baba Ganouj | WEAK | OKR3 | T001 | BDM sale quality |
| 48 | Melrose: churn request with no details, AM trying to reach out | Churn | Sam McKenzie | AM | Melrose | WEAK | OKR3 | — | — |
| 49 | San Churro Southbank: sold back to HO, new owners incoming | Churn | Matthew Behan | BDM | San Churro (franchise) | MEDIUM | OKR3 | T006 | Franchise conversion |
| 50 | Pot au Pho Mornington: closed indefinitely, may sell or close completely | Churn | Tania Marinopoulos | AM | Pot au Pho | HIGH-conf | OKR3 | — | — (unpreventable) |
| 51 | Mr Toast: sold, new owner not interested in third-party partners | Churn | Brianna Quinn | Unknown | Mr Toast | HIGH-conf | OKR3 | — | Venue-sold conversion |
| 52 | Sideshow Burgers: ownership change, need to re-sign with new ABN — new owner signed | Churn | Elodie Fitzsimmons | Unknown | Sideshow Burgers | HIGH-conf | OKR3 | — | Venue-sold re-sign |
| 53 | The Lil Hut: sold, not interested in referral bonus | Churn | — | — | The Lil Hut | HIGH-conf | OKR3 | — | Venue-sold conversion |
| 54 | My Place: owner called to cancel, BDM Otis reaching out | Churn | Gabriella Szabo | AM | My Place | MEDIUM | OKR3 | T005 | — |
| 55 | Nurish Cafe: "commission too high," "everything very expensive," venue running at a loss | Churn | Kane Russell / Brianna Quinn | AM / Unknown | Nurish Cafe | STRONG | OKR3 | T005 | Value vs. cost perception |
| 56 | Chaan Thai: can't maintain margin at 20%, saved in March, churning again | Churn | Matthew Behan | BDM | Chaan Thai | STRONG | OKR3 | T005 | Discount depth economics |
| 57 | Rascals Deli: permanently closed on Google, non-responsive since end of March | Churn | Gabriella Szabo | AM | Rascals Deli | HIGH-conf | OKR3 | — | — (unpreventable) |
| 58–63 | 6 Mixpanel bulk edit patterns: restIDs with 20–62 edits in single sessions (AM-on-behalf editing) | Mixpanel | — | — (likely AMs) | 6 unnamed venues | STRONG | OKR1 | T002 | AM manual work quantification |
| 64 | Mixpanel aggregate: 931 venues active on Portal; top 100 by edits shown; majority with 0 performance-tab clicks | Mixpanel | — | — | All Portal venues | STRONG | OKR2 | T005 | Performance tab engagement gap |

*Note: 94 additional Mixpanel portal_engaged_venue signals (5–19 edits each) omitted from table for brevity. They confirm broad Portal offers-tab usage but near-absent Performance tab usage.*

---

### 🗺️ OST update

**OKR 1 Root: Manual AM task reduction / Venue self-serve capability / System automation**

| Branch | Status | Evidence this week |
|---|---|---|
| Recurring hours management | **STRENGTHENED** | Chuck Trailer's explicitly names the gap: "only allowing '1 off' updates." AUN requests holiday hours via ticket. |
| Guest limit / party size self-serve | **STRENGTHENED** | La Botte, AUN, Honki Tonki — 3 separate requests for guest cap changes this window alone. |
| NCI/RCI boost self-serve | CHRONIC — unchanged | Frankston Curry Club, Geppetto, Ladygreen — identical to prior weeks. |
| Dining time window management | **STRENGTHENED** | Chargrill Charlie's (1hr), Grand View Hotel (1.5hr), La Perla (2hr), Yenyum Thai (90min) — 4 requests. |
| Surcharge management | NEW | Teaology Lab requests 10% surcharge for specific date via BDM. |
| Real-time offer flexibility | NEW (weak) | Mala Mia churned because EC "isn't flexible enough" for daily event-driven offer changes. Single signal. |
| AM bulk-edit quantification | **NEW — quantified** | 6 venues × 20–62 edits/session in Mixpanel. First behavioural proof at scale. |

**OKR 2 Root: Partner Portal engagement / Venue-led revenue actions / Deal score visibility**

| Branch | Status | Evidence this week |
|---|---|---|
| Performance tab discoverability & utility | **STRENGTHENED (negatively)** | Of top 100 Portal users, majority show 0 performance clicks. Only 7 venues have 7+ clicks. The tab is functionally invisible. |
| Portal login/access barriers | RISING | Hecho en Mexico can't login (error on 2 emails + incognito). |
| Portal engagement depth | **CONFIRMED** | Engagement is offers-edit-centric. Venues come in, edit offers, leave — never exploring performance data. |
| Deal score zero population | UNCERTAIN | Deal score data unavailable this run (day 3 of month). Cannot refresh 397-venue-at-zero benchmark. |

**OKR 3 Root: Friction in core experience / Product fit for enterprise / Onboarding quality / Surfacing value**

| Branch | Status | Evidence this week |
|---|---|---|
| Customer behaviour enforcement | CHRONIC — unchanged | Bang Bang ($360 fraud), Geppetto (10+ no-shows), Honki Tonki (late arrivals, takeaway fraud). No systemic solution. |
| T&C abuse → debt justification | **NEW ESCALATION** | Lulo Spice explicitly refused to pay $160.74 citing customer T&C violations. Weaponised. |
| Group/enterprise product layer | **STRENGTHENED — confirmed** | Gogyo cascade (2 venues, identical to Ramen Ippudo pattern). Mr Ramen San Nova cascade confirmed. San Churro franchise × 2. |
| Value perception / ROI visibility | **STRENGTHENED** | 5 financial churns this window. Performance tab near-zero usage compounds the problem — venues can't see their own numbers. |
| Billing/payment reliability | RISING | Onice double charge, Yum Yum Tree card decline, Mr Ramen San refund dispute. 3 different billing failure modes. |
| Venue-sold transition | NEW | 5 of 21 churns are venue sales. Conversion rate of new owners appears very low. Only Sideshow Burgers re-signed. |
| Post-sale ROI education | **WEAKENED** | Oramesti explicitly compared EC to full-price yield. If even AMs (Elodie) notice the framing gap, the onboarding/activation education isn't working. |

---

### ⚠️ Friction stack watch

**1. Yum Yum Tree Victoria Park** — restID: 7831FFCB-CFC7-4B48-A98B-564D4B4E29E2
- **Status**: UPGRADE TO CRITICAL
- Signals:
  - HubSpot (T004): EatClub card declined twice at venue — consumer-facing payment failure
  - Watch list (AM relationship): "No one bothered to call me" — AM non-responsiveness
  - Watch list (Renewal-churn): Pause request W16
- **Analysis**: Three journey stages affected (Ongoing engagement, AM relationship, Renewal-churn). Payment failure + AM silence + pause request = active friction stack. The card decline is particularly dangerous because it's a consumer-facing failure that the venue witnesses — reinforces the "platform doesn't work" narrative.
- **⚠️ Flag to Luke**: This venue needs an AM call within 48 hours. The pause request + "no one called me" + card decline is the classic pre-churn stack.

**2. Honki Tonki — Hindley Street** — restID: 52C271EE-7E18-41E3-876E-C0D6FA4CF0C3
- **Status**: WATCH → ESCALATING
- Signals:
  - Slack (T003): Customer arrived 2hrs late, others used dine-in for takeaway — AM requesting CS refund action
  - Slack coverage (T002): Manual request for 4pax + 90min dining cap
  - Mixpanel: 6 offer edits, 4 offers-tab views, 1 performance-tab click — venue is actively engaged on Portal
- **Analysis**: Two themes (T002, T003) across 2 sources (Slack, Mixpanel). Venue is actively trying to use the platform (Mixpanel confirms engagement) but is being hit by customer abuse they can't prevent AND config limitations they can't self-serve. The T003 + T002 combo is the friction stack: bad customers create urgency → venue needs faster config changes → can't self-serve → depends on AM → AM becomes the bottleneck.

**3. La Botte Pizza — Pascoe Vale** — restID: DB6BD926-E4E9-4884-919A-725DD772E9BC
- **Status**: WATCH (maintained)
- Signals:
  - Watch list (T003): T&C abuse from prior weeks
  - Slack (T002): 4 guest max request via BDM Prudence Madigan
- **Analysis**: Two themes (T002, T003) across 2 weeks. The guest limit request may itself be a response to the T&C abuse — venue trying to limit party sizes to reduce abuse exposure. If so, the T002 self-serve gap is blocking the venue's own attempt to mitigate T003 risk.

**4. Gogyo Group** (Surry Hills: 6437076F / Fitzroy: F6EC22AE)
- **Status**: CHURNED — post-mortem priority
- Signals:
  - Churn (T006): Group-level decision, POC gatekeeping, AM locked out of directors
  - Identical to Ramen Ippudo pattern from prior weeks
- **Analysis**: This is not a friction stack in progress — it's a completed cascade churn. But it must be noted because it validates T006 with zero ambiguity. The same pattern has now occurred at least 3 times (Ramen Ippudo, Mr Ramen San, Gogyo). Post-mortem: what would have had to be true to detect this before the POC communicated the decision?

**5. Mr Ramen San** (Nova: 51077CCA / Mid City: prior churn)
- **Status**: CRITICAL — rescue in progress
- Signals:
  - Churn (T006/T007): $65.63 refund dispute → cascade to Nova, waiting on receipt proof
  - AM Jessie Helyar escalated to Emma (senior) for apology
  - Owner Royston says he'll "consider reactivating The Nova" once refund is confirmed
- **Analysis**: This is a T006 cascade that may be reversible. The rescue hinges on proving the refund was made. Emma emailed the receipt — outcome pending. If the refund proof satisfies Royston, Nova may reactivate. But the $65.63 error cost at least 2 venue-months of revenue. This is the poster child for T006 + T007 compounding.

**Watch list venues with no new signals — status unchanged, silence is the signal:**
- **Garibaldi Pizzeria** (CRITICAL): No signals. Angie's urgent W15+W16 outreach appears unresolved. ⚠️ Flag to Luke.
- **The Last Jar** (CRITICAL): No signals. 4th cancel attempt unresolved. ⚠️ Flag to Luke.
- **Masala Flames** (ESCALATING): No signals. iOS bug 5+ months, engineering owner still needed.
- **Lumen Alley** (ESCALATING): No signals. Deal revert issue from W15+W16.
- **Alexander Mediterranean** (WATCH): No signals. $266 debt + 14+ day silence persists.
- **Everest MoMo Station** (WATCH): No signals. March cancel email still not actioned, $148.08 dispute.
- **Delhi Darbar** (WATCH): No signals. Billing bug (membershipBillingDay 0) + pause request.

---

### 💡 Synthesis notes

**What surprised me:**

1. **The Gogyo churn is word-for-word the T006 prediction.** Elliot Rayment's description — "My POC hid behind the directors decision and would not include them on any meeting attempts" — reproduces the Ramen Ippudo pattern exactly. This theme is no longer hypothetical. It's a confirmed, repeating structural vulnerability.

2. **Performance tab usage is catastrophically low.** I expected it to be low. I did not expect the majority of the top 100 most-engaged Portal users to have zero performance-tab clicks. These are venues actively editing offers — the most engaged cohort — and even they aren't looking at their data. This isn't a discoverability problem; it might be a product-market fit problem for the tab itself. If the most engaged venues aren't using it, who is it for?

3. **5 of 21 churns this window were venue sales.** That's 24%. And only 1 (Sideshow Burgers) re-signed the new owner. The venue-sold conversion process appears to be nearly non-existent. This is silent, recurring revenue loss with no product or process solution.

4. **The T002 bulk-edit Mixpanel pattern is damning.** 62 offer edits in a single session is not a venue self-serving. That's an AM spending 30+ minutes doing what the system should do. Six venues showed this pattern in a 3-day window. Extrapolated across the month and the full AM team, this is likely hundreds of hours.

**What is missing:**

- **Deal score data**: Cannot assess whether the 397 venues at score zero is growing, shrinking, or static. This is the single most important missing metric for T005.
- **Granola / meeting transcripts**: No strategic context from AM meetings this window.
- **HubSpot notes**: Effectively empty (197/200 stubs). AM sentiment and relationship quality data is completely missing.
- **Venue names for Mixpanel restIDs**: The 6 bulk-edit venues and the 7 performance-tab-curious venues cannot be identified by name, preventing AM follow-up.
- **Garibaldi Pizzeria resolution**: CRITICAL status since W15 with zero visibility into what happened.

**Interview questions to sharpen weakest signals:**

For T005 (value perception — the "why" is still fuzzy):
1. "When you say EatClub isn't worth it, what number would you need to see to change your mind? What would 'worth it' look like?"
2. "Have you ever looked at the Performance tab in Partner Portal? What did you expect to find there? What did you actually find?"
3. "When you think about the customers EatClub sends you, how many of them come back without an offer?"

For T002 (prioritising which self-serve capability to build first):
4. "If you could change one thing about your EatClub setup right now without calling us, what would it be?"
5. "How often do you need to change your opening hours or guest limits? Daily? Weekly? Monthly?"

For T006 (understanding group decision-making):
6. "Who in your organisation actually decides whether you stay on platforms like EatClub? Have we ever spoken to them?"

**What would move OKR 1 most?**

Build recurring schedule management and guest limit self-serve in Partner Portal. Chuck Trailer's "1 off updates" complaint is the exact spec: venues need to set permanent hours and have them persist. The 8 dining-window / guest-limit / NCI requests this week are all the same shape: "let me set a rule and have it stick." If venues could self-serve these, the 8+ weekly Slack config requests and the Mixpanel bulk-edit sessions largely disappear. This is the highest-leverage intervention for OKR 1.

**What would move OKR 2 most?**

Fix the Performance tab problem. Right now, even the most engaged Portal users don't look at it. Two possible interventions: (a) surface key performance metrics (covers driven, repeat rate, revenue attributed) directly on the offers page so venues see ROI without navigating away; (b) send a periodic performance summary via email/push that doesn't require Portal login. The goal is not to make venues click on a tab — it's to make venues see their numbers. If they see their numbers, the "not worth it" narrative from T005 has something to compete with.

---

### Routing block