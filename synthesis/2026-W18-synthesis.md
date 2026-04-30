**Sources available this run**: Slack (10 AU channels, 175 messages), HubSpot (300 tickets + 300 notes scanned), Churn (30 rows parsed, 21 AU churns in window), Mixpanel (4,158 events across 885 unique venues)

**Sources unavailable / failed**: Granola (no customer-facing meetings in window — skipped), Deal Score (CSV parsed but returned 0 drops, 0 rises, 0 zero-score venues — suspect collector mismatch given T001 reported 397 zero-score venues in W16)

**Confidence note**: 3-day window (Mon 27 Apr – Thu 30 Apr) limits full-week pattern visibility. HubSpot budget exhausted at 300 tickets/300 notes — some AU-relevant tickets may be missed from a pipeline exceeding 125K records. Deal Score returning zero is almost certainly a data quality issue, not evidence the problem resolved — T001 heat carried from prior week but cannot be validated this run. Granola absence means no AM-meeting signals; qualitative voice-of-venue from face-to-face is missing entirely. Mixpanel capped at top 100 of 885 venues; long-tail engagement not captured. Churn data tenure fields appear to reflect contract period rather than actual time on platform — do not treat as reliable tenure measurement.

---

### 🔥 Rising themes this week

---

**1. Partner Portal self-serve gap — AMs manually doing venue configuration**
- **Theme tag**: T007
- **Heat**: HIGH
- **Signal count**: 15+ signals across 4 sources (Slack 8+, HubSpot 4, Mixpanel 3, Churn 4)
- **Lifecycle**: CHRONIC (5+ weeks)
- **Problem statement**: Venues cannot configure key deal parameters — NCI boost, seat times, guest limits, no-show buffer, item exclusions, first-time-customer limits — through Partner Portal. Every request becomes manual AM work, consuming hours weekly per AM and creating bottlenecks where venues wait for changes that should be instant.
- **Mom Test quality**: STRONG — Behavioural evidence from multiple angles. Mixpanel detected 3 sessions with 21–28 offer edits in a single sitting, consistent with an AM batch-editing on behalf of venues. HubSpot shows Tania Marinopoulos submitting identical offer structures for Gami Chicken x2 venues. Slack coverage documents 8+ distinct manual config requests in a single week (Bang Bang x2, David's Master Pot x3, Tran Tran, Garden State Diner, Bavarian Sizzle, Handcrafted Pizza). Churn source confirms downstream impact: Zircon (couldn't self-optimise, early churn), Chaan Thai (saved in March, churning again because margins don't work at 20% and no lower option), Lulo Spice ($160 debt, wants 5–10% offers, "knows this isn't an option").
- **Verbatim**: *"HS would like to have the following offers only, effective immediately & permanent. I did a one-off for tomorrow: 11:00 am – 12:00 pm: 35% off (1 Dine-in voucher) All Day: 20% off (Unlimited Takeaway & Dine-in vouchers)"* — Tania Marinopoulos (AM), HubSpot, for Gami Chicken
- **Verbatim**: *"Hi Jordan, We need to update the offer to 20% all day every day. From 3-5:30pm, 25%. Also can you limit the offer to first time customers?"* — Eddie (venue owner, Madame Trang), via HubSpot. Note: "first time customers" is not a Portal-available filter.
- **OKR**: OKR1 (primary — every manual request is AM time that should be self-serve), OKR2 (secondary — venues can't take revenue actions independently)
- **OST branch**: Venue self-serve capability / Manual AM task reduction
- **Journey stage**: Ongoing engagement
- **Recommended action**: **Discovery ticket** — Scope a Partner Portal self-serve expansion covering: (1) time-slot-specific offer configuration, (2) NCI/RCI boost toggle, (3) guest/party-size limits, (4) item/category exclusion, (5) first-time-customer offer restriction. The Mixpanel bulk-edit detector should become an automated flag: when single-user sessions exceed 15 edits, prompt the venue for self-serve onboarding.

---

**2. Customer T&C abuse creating venue friction — no tooling to manage offenders**
- **Theme tag**: T010
- **Heat**: HIGH
- **Signal count**: 7 signals across 2 sources (Slack 2 + 5 in coverage notes, Churn 1)
- **Lifecycle**: RISING (3 weeks, volume increasing)
- **Problem statement**: Dine-in customers ordering takeaway, breaching max pax, arriving outside time windows, and stacking in-house offers with EC deals. Venues are frustrated and churning. There is no mechanism for venues or AMs to flag, warn, or block repeat offenders. AMs don't know what the protocol is. When repeated enough, this becomes the churn reason.
- **Mom Test quality**: STRONG — Tania Marinopoulos (AM) explicitly asked for a process that doesn't exist. Lulo Spice churned citing customer T&C violations as justification for non-payment of debt. Coverage notes confirm 5 additional dine-in-for-takeaway incidents this run (Maikhana, Basilico Prospect, Terronia Cocktail Bar — 2 breaches in 5 days on a new venue, Beans and Beers Torquay, Suliya Korean Pocha).
- **Verbatim**: *"What is the process of flagging a customer? And can we please reach out and let her know if she does it again we will suspend her account or something? Not sure what the protocol is for repeat offenders..."* — Tania Marinopoulos (AM), Slack #cs-and-am, re: Le Feu Oasis
- **Verbatim**: *"customers weren't following T's and C's... I asked if he was going to pay his debt and he said he didn't have to because customers weren't following T's and C's"* — Cameron Landis (unknown team), Churn, re: Lulo Spice & Bar
- **OKR**: OKR3 (friction in core venue experience driving churn), OKR1 (AMs manually chasing CS to resolve individual incidents)
- **OST branch**: Friction in core venue experience
- **Journey stage**: Ongoing engagement → Renewal-churn decision
- **Recommended action**: **Discovery ticket** — Design a customer behaviour flagging system: (1) venue-initiated T&C violation report in Partner Portal, (2) automated warning to flagged customers, (3) suspension/ban capability for repeat offenders, (4) clear internal protocol documentation for AMs and CS. Terronia Cocktail Bar (2 breaches in 5 days, new venue) makes this an onboarding-stage risk as well.

---

**3. Double dipping — customers stacking discounts across platforms or with in-house specials**
- **Theme tag**: T002
- **Heat**: HIGH
- **Signal count**: 5 signals from 2 sources (Slack 4, HubSpot 1 — Pickled Monkey confirmed across both)
- **Lifecycle**: CHRONIC (4+ weeks)
- **Problem statement**: Customers are using EatClub deals simultaneously with other discount platforms (First Table) or in-venue specials (happy hour items, weekly specials). Venues absorb the margin loss and blame EatClub. The TA tablet workaround exists but is reactive and requires AM intervention. No systemic prevention. This co-occurs with T003 (POS integration) and T010 (T&C abuse) and is now a confirmed churn driver.
- **Mom Test quality**: STRONG — Three independent double-dipping incidents in one run. Pickled Monkey Brewing churned explicitly citing double dipping (confirmed via both Slack churn request and HubSpot debt demand). Annata documented a specific First Table + EatClub double dip with receipts. Little Lamb Burpengary BDM setting up TA tablet specifically to prevent churn from double dipping. Thornbury Taphouse churned with "EC customers were using offers on their specials."
- **Verbatim**: *"She was adamant... She doesn't like eat club customers and she says that they complain a lot. She also mentioned that they had been double dipping."* — Nader Masrour (AM), Slack, re: Pickled Monkey Brewing
- **Verbatim**: *"They double-dipped by using both First Table and EatClub. I've attached the First Table receipt and the payment details the venue received through EatClub"* — Jasmine Jung (AM), Slack, re: Annata
- **OKR**: OKR3 (direct churn cause)
- **OST branch**: Friction in core venue experience
- **Journey stage**: Ongoing engagement → Renewal-churn decision
- **Recommended action**: **Discovery ticket** — This is the third consecutive week with churn-confirmed double-dipping. Investigate: (1) cross-platform detection at transaction level (can EC detect when a First Table booking overlaps?), (2) item/category exclusion on Portal (connects to T007 — venues should be able to exclude already-discounted items), (3) scope of Burpengary TA tablet workaround — is it scalable? The T002 + T007 intersection (item exclusion) may be the most efficient single fix.

---

**4. Onboarding expectation gap — BDM promises diverging from product reality**
- **Theme tag**: T009
- **Heat**: MEDIUM
- **Signal count**: 4 signals across 2 sources (Slack 2, Churn 2)
- **Lifecycle**: RISING (3 weeks)
- **Problem statement**: Venues are churning within months because what they were told during sales doesn't match their experience. Common gaps: giveaway/commission structure misunderstanding, refund promises that AMs can't honour, "no perceived value" because venue can't see ROI. The most severe instance this run (Busan Baby) involved a BDM promising offerless transaction refunds that the AM could not confirm, leading to legal threats.
- **Mom Test quality**: MEDIUM overall, one STRONG signal — Khau Galli churned citing "miscommunication around a giveaway when joining and commission confusion" (secondhand but specific). Khao Thai said "not seeing any difference in income" (specific perceived outcome). Busan Baby is STRONG: BDM Alex explicitly told owner Ginny that EatClub would refund offerless transactions; AM Gabriella could not guarantee this; owner now threatening legal action. OTiS pause request includes specific pricing model misalignment ("Make it cheaper for 1 or do a percentage of sales or a monthly subscription rather than both").
- **Verbatim**: *"Requested a full refund from the commission and discounts so far after miscommunication around a giveaway when joining and commission confusion"* — Jordana Anderson (unknown team), Slack, re: Khau Galli
- **OKR**: OKR3 (onboarding journey quality → early churn), OKR1 (AMs cleaning up BDM-set expectations)
- **OST branch**: Onboarding journey quality
- **Journey stage**: Onboarding → Activation → Renewal-churn decision
- **Recommended action**: **Interview** — Need to sharpen: How common is the giveaway/commission misunderstanding? Is this a BDM scripting issue or a structural product complexity issue? Does the Arrows onboarding flow cover commission mechanics? Busan Baby requires immediate management review (see Friction Alerts).

---

**5. Debt accumulation triggering churn risk**
- **Theme tag**: T013
- **Heat**: MEDIUM
- **Signal count**: 3 signals across 3 sources (Slack 1, HubSpot 1, Churn 1)
- **Lifecycle**: CHRONIC (4+ weeks)
- **Problem statement**: Venues with outstanding balances escalate from silence to active hostility to churn. The debt-and-silence combination (T013 + T012) remains the classic churn predictor. This run adds a new pattern: venues disputing debt by citing customer T&C violations as justification for non-payment (Lulo Spice). When debt and T&C abuse co-occur, the venue feels entitled to withhold payment, and the relationship becomes adversarial.
- **Mom Test quality**: STRONG — Three distinct venues with specific financial stakes. The Red Chair: "I managed to get the debt paid but haven't been able to reach the owner since to reactivate. I've been chasing this since January." Pickled Monkey (HubSpot): "Do not debt our card as we have stopped using eat club." Lulo Spice: "$160.74 debt, owner dodging BDM calls... said he didn't have to [pay] because customers weren't following T's and C's."
- **Verbatim**: *"Do not debt our card as we have stopped using eat club"* — Pickled Monkey Brewing venue, HubSpot ticket
- **OKR**: OKR3 (churn trigger)
- **OST branch**: Friction in core venue experience
- **Journey stage**: Ongoing engagement → Renewal-churn decision
- **Recommended action**: **Watch** — Monitor for T013 + T010 co-occurrence expanding. The Lulo Spice pattern (T&C abuse → debt refusal → churn) is new and dangerous. If venues learn they can cite T&C violations as grounds for non-payment, debt collection becomes much harder. Prioritise T010 tooling to prevent this pattern from spreading.

---

### 📋 All signals this week — classified

**Slack (15 signals)**

| Signal summary | Source | Author | Team | Affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| Yum Yum Tree + 4 venues: churn/pause batch, loyalty deactivation requested | Slack #churned | Libby Egan | AM | 5 venues (incl. Chopsticks Viet x2, Gill St Deli, Claypot) | STRONG | OKR3 | T012 | Core venue friction |
| Busan Baby / Seoul Sweetie: owner Ginny threatening legal action, demanding full refund, BDM promised refund AM couldn't confirm, multi-team coordination failure | Slack #churned | Gabriella Szabo | AM | 2 venues | STRONG | OKR3, OKR1 | T009 + T006 + T011 | Onboarding quality |
| Open Sesame HS: 3 venues planning to stop for 3 months, trying another platform | Slack #cs-and-am | Rose Indicio | Unknown | 3 venues | MEDIUM | OKR3 | T003 (adjacent) | Core venue friction |
| The Red Chair: debt paid but owner unreachable since January, venue sold, account closed | Slack #churned | Jessie Helyar | Unknown | 1 venue | STRONG | OKR3 | T013 + T012 | Core venue friction |
| Pickled Monkey Brewing: adamant churn, "doesn't like EC customers," double dipping cited | Slack #churned | Nader Masrour | AM | 1 venue | STRONG | OKR3 | T002 | Core venue friction |
| Thornbury Taphouse: churn, EC customers using offers on specials, POS integration attempted and failed | Slack #churned | Cameron Landis | Unknown | 1 venue | STRONG | OKR3 | T002 + T003 | Core venue friction |
| Little Lamb Burpengary: setting up TA tablet to save churn from double dipping | Slack #sales-admin | Mark Savaille | Unknown | 1 venue | STRONG | OKR3 | T002 | Core venue friction |
| Annata: customer double-dipped First Table + EatClub, receipts provided | Slack #cs-and-am | Jasmine Jung | AM | 1 venue | STRONG | OKR3 | T002 | Core venue friction |
| Dao Noodle / Eastbourne Alley: auto holiday hours applied for Anzac Day despite venues being open, also happened at Easter | Slack #tech-halp | Mandy Tramer | BDM | 2+ venues | STRONG | OKR2 | T005 | Deal score trust |
| Le Feu Oasis: repeat T&C offender, no flagging/blocking mechanism, AM asking for process | Slack #cs-and-am | Tania Marinopoulos | AM | 1 venue | STRONG | OKR3, OKR1 | T010 | Core venue friction |
| Smoky Charcoal Chicken: waive monthly for 3 months due to previous billing issues | Slack #churned | Jai Richards | Unknown | 1 venue | MEDIUM | OKR3 | T011 | Core venue friction |
| Pleiku in Brunswick: pause requested, customer charged 10% commission outside offer time | Slack #churn-appt | Automated | System | 1 venue | MEDIUM | OKR3 | T011 | Core venue friction |
| INC-19 resolved: business profile payment rollout sync with DB | Slack #incidents | Incident | System | Platform-wide | HIGH (incident) | OKR2 | Unmapped | Portal engagement |
| OTiS: pricing model too expensive, discounting existing customers, can't exclude happy hour items | Slack #churn-appt | Automated | System | 1 venue | MEDIUM | OKR2, OKR3 | T007 + T009 | Venue-led revenue / Self-serve |
| Khau Galli: churn after giveaway miscommunication and commission confusion | Slack #churned | Jordana Anderson | Unknown | 1 venue | MEDIUM | OKR3 | T009 | Onboarding quality |

**HubSpot (9 signals)**

| Signal summary | Source | Author | Team | Affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| Luca Joondalup: tried reaching AM for a week, multiple tickets + text, threatening to close 2 accounts | HubSpot | Venue owner | Venue | 2 accounts | STRONG | OKR1, OKR3 | T006 | System automation |
| Dachshund Coffee Hunters Hill: closing business | HubSpot | Venue owner | Venue | 1 venue | HIGH (conf.) | OKR3 | Unmapped (closure) | — |
| Pickled Monkey Brewing: "Do not debt our card as we have stopped using eat club" | HubSpot | Venue owner | Venue | 1 venue | STRONG | OKR3 | T013 | Core venue friction |
| Volume One Espresso: pause request, "see how we go" | HubSpot | Venue owner | Venue | 1 venue | WEAK | OKR3 | Unmapped | — |
| Myra's Kitchen: wants to remove EatClub day | HubSpot | Venue owner | Venue | 1 venue | WEAK | OKR3 | Unmapped | — |
| Gami Chicken Point Cook: AM submitting permanent offer change on behalf of venue | HubSpot | Tania Marinopoulos | AM | 1 venue | STRONG | OKR1 | T007 | AM task reduction |
| Gami Chicken Carnegie: identical AM-submitted offer change | HubSpot | Tania Marinopoulos | AM | 1 venue | STRONG | OKR1 | T007 | AM task reduction |
| Caffe Primo Firle: venue wants offer changed from 25% to 20% | HubSpot | Elodie Fitzsimmons | Unknown | 1 venue | MEDIUM | OKR2 | T007 | Venue self-serve |
| Madame Trang: venue wants offer update + first-time customer limit (not available on Portal) | HubSpot | Venue owner | Venue | 1 venue | STRONG | OKR2 | T007 | Venue self-serve |

**Churn (21 signals — 12 controllable, 9 venue closures/sales)**

| Signal summary | Source | Author | Team | Affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| Mr Ramen San Nova: $65.63 refund not received, demanding bank details removal, pulling Nova venue too | Churn | Jessie Helyar | Unknown | 2 venues (group) | STRONG | OKR3 | T011 | Core venue friction |
| Zircon: early churn, "numbers not making money," AOV $110, 41 customers in ~1 month | Churn | Cameron Landis / Kane Russell | Unknown / AM | 1 venue | STRONG | OKR1 | T007 | Value through data |
| M Yong Tofu: on offerless, wants to be on without it, can't opt out | Churn | Aaron Pantazis | AM | 1 venue | MEDIUM | OKR3 | T007 | Self-serve capability |
| Khao Thai Little Bay: "not seeing any difference in income," rising costs | Churn | Aaron Pantazis | AM | 1 venue | STRONG | OKR3 | T009 | Value through data |
| Chaan Thai: "cannot maintain profit margin with even 20% deals," saved March, churning again | Churn | Matthew Behan | BDM | 1 venue | STRONG | OKR1 | T007 | Self-serve capability |
| Lulo Spice: $160 debt, customers outside arrival times, wants 5-10% offers, citing T&C as non-payment justification | Churn | Cameron Landis / Nancy Tandual | Unknown / Unknown | 1 venue | STRONG | OKR3 | T010 + T013 | Core venue friction |
| Gogyo Surry Hills: group churn, busy season, running own promos, POC hiding behind directors | Churn | Elliot Rayment | AM | 1 venue (group) | STRONG | OKR3 | T004 | Enterprise/Groups |
| Gogyo Fitzroy: same group churn | Churn | Elliot Rayment | AM | 1 venue (group) | STRONG | OKR3 | T004 | Enterprise/Groups |
| Baba Ganouj: "I didn't like it" × 4 notes, early churn | Churn | Matthew Behan | BDM | 1 venue | WEAK | OKR3 | T009 | Onboarding quality |
| My Place: early churn, financial, referred to BDM Otis | Churn | Gabriella Szabo | AM | 1 venue | WEAK | OKR1 | T007 | Value through data |
| Nurish Cafe: "commission too high, everything very expensive now," running at a loss | Churn | Brianna Quinn / Kane Russell | Unknown / AM | 1 venue | MEDIUM | OKR3 | T009 (adjacent) | Value through data |
| Melrose: no details, trying to reach out | Churn | Sam McKenzie | AM | 1 venue | WEAK | OKR3 | Unmapped | — |
| **9 venue closures/sales**: Monsoon Palace (sold), Di Francesco Cucina (closed), NC's Chaat (closed), Rascals Deli (closed), Pot au Pho (closed), Mr Toast (sold, couldn't convert), San Churro (sold to HO), Sideshow Burgers (ownership change, re-signing), The Lil Hut (sold) | Churn | Various | Various | 9 venues | HIGH (conf.) | OKR3 | Unmapped (uncontrollable) | — |

**Mixpanel (4 notable + 96 engagement telemetry)**

| Signal summary | Source | Author | Team | Affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| Yum Yum Tree (7831FFCB): 1 session, 0 edits, 3 offers views — minimal engagement from churning venue | Mixpanel | — | — | 1 venue (watch list) | STRONG (behav.) | OKR2 | T012 | Portal engagement |
| Bulk edit pattern: 28 offer edits in 1 session (restID E3E5F488) — AM editing on behalf of venue | Mixpanel | — | — | 1 venue + AM | STRONG (behav.) | OKR1 | T007 | AM task reduction |
| Bulk edit pattern: 24 offer edits in 1 session (restID 6E2C2CF4) | Mixpanel | — | — | 1 venue + AM | STRONG (behav.) | OKR1 | T007 | AM task reduction |
| Bulk edit pattern: 21 offer edits in 1 session (restID 6B7CCCDA) | Mixpanel | — | — | 1 venue + AM | STRONG (behav.) | OKR1 | T007 | AM task reduction |
| **96 additional Portal engagement signals**: 885 unique venues active, median 6-8 offer edits per engaged venue. Performance tab usage remains very low (majority = 0 clicks). Positive OKR2 signal overall. | Mixpanel | — | — | 885 venues | — | OKR2 | — | Portal engagement |

---

### 🗺️ OST update

**OKR 1 — Scale AM Optimisation**

| Branch | This run | Direction |
|---|---|---|
| **Manual AM task reduction** | STRENGTHENED. 3 Mixpanel bulk-edit patterns (21–28 edits/session) quantitatively prove AMs are doing venue config work through Portal. Gami x2 HubSpot tickets show the same AM (Tania) submitting identical offer structures across multiple venues — template work that should be automated. 8+ manual config requests in Slack coverage notes (NCI, RCI, seat times, party size). Busan Baby showed 3 internal staff touching one churn case without coordination — time multiplied by disorganisation. | ▲ |
| **Venue self-serve capability** | STRENGTHENED. Madame Trang owner explicitly asked for first-time-customer offer limit — a feature not available in Portal. OTiS requested item exclusion ("I can't exclude items so people can use it on heavily discounted happy hour items"). Caffe Primo wants to change discount from 25% to 20% — a simple operation requiring AM intermediation. Gap between what Portal can do and what venues need to do independently is widening as venue sophistication increases. | ▲ |
| **System automation** | WEAKENED. Luca Joondalup went a full week with no AM response across multiple tickets — no escalation triggered. Busan Baby had 3+ internal parties acting on the same case without the assigned AM's knowledge — no single-owner routing. T005 holiday hours auto-applied incorrectly with no venue notification or override mechanism. Each of these is a missing workflow. | ▼ |

**OKR 2 — Drive Deal Performance Through System-Led Actions**

| Branch | This run | Direction |
|---|---|---|
| **Partner Portal engagement** | POSITIVE. 885 unique venues engaged in 3 days across 4,158 events. Offer edit activity is healthy — top venues making 15-19 edits per session. This suggests a meaningful cohort of self-serve venues is emerging. Portal is being used. | ▲ |
| **Venue-led revenue actions** | WEAKENED by T007 constraints. Venues want to take more sophisticated actions (time-slot-specific offers, first-time customer limits, item exclusions) but Portal doesn't support them. Demand for self-serve is outpacing capability. Additionally, OTiS feedback — "It isn't bringing people in so much as giving discounts to people who already come here" — challenges the core value proposition for some venue types. | ▼ |
| **Deal score visibility and trust** | NO MOVEMENT. Deal score collector returned zero signals. T001 (397 zero-score venues W16) not validated. No AM or venue discussion of deal score in any channel. Performance tab clicks remain very low in Mixpanel (most venues = 0). Venues are managing deals but not understanding their impact. | — |

**OKR 3 — Churn Reduction**

| Branch | This run | Direction |
|---|---|---|
| **Friction in core venue experience** | STRENGTHENED (negatively). T002 (double dipping), T010 (T&C abuse), and T013 (debt) all produced confirmed churn signals this run. New pattern identified: T010 + T013 co-occurrence at Lulo Spice where venue cited T&C violations as justification for non-payment of debt. 21 churns in 3 days (12 controllable) is elevated. | ▲▲ |
| **Product fit for enterprise-Groups** | NEW EVIDENCE. Gogyo group (2 venues, Surry Hills + Fitzroy) churned — second group cascade after Ramen Ippudo. AM Elliot Rayment: "My POC hid behind the directors decision and would not include them on any meeting attempts." EatClub has no group-level relationship management tool. POC gatekeeping is a structural vulnerability. Mr Ramen San also pulling Nova venue after billing dispute at Mid City — single-owner multi-venue cascade emerging as pattern. | ▲ |
| **Onboarding journey quality** | STRENGTHENED (negatively). Khau Galli (giveaway miscommunication), OTiS (pricing model surprise), Busan Baby (BDM promise that AM couldn't honour). The discount-applies-to-total-bill and giveaway mechanics are the most common specific misalignments. BDM-to-AM handoff is where expectations diverge most. | ▲ |
| **Surfacing product value through data** | WEAKENED. Khao Thai: "not seeing any difference in income." M Yong Tofu: cancelled because couldn't see value in offerless. Zircon: "numbers weren't making money." Performance tab underutilised per Mixpanel. Venues that churn for "financial" reasons may be failing to see ROI that actually exists — but the platform isn't showing it to them. | ▼ |

---

### ⚠️ Friction stack watch

**1. Busan Baby / Seoul Sweetie** ⚠️ IMMEDIATE ESCALATION TO LUKE
- **restIDs**: DFD83978-6FCA-445A-97A4-72FA6F8FFA8D / 666D8C05-21AA-4BF7-A9E4-A0A86A8AD2E5
- **Signals**: T009 (BDM promised refund on offerless transactions) + T006 (AM not informed of other staff involvement) + T011 (full refund demanded on all offerless since 1 April) + legal threat
- **Sources**: Slack (Gabriella Szabo)
- **Journey stages**: Onboarding → Activation → Renewal-churn decision (full stack)
- **Analysis**: This is the most dangerous signal this run. Owner Ginny is threatening legal action. Three internal parties (BDM Alex, Mandy Tramer, Jay Franklin) touched this case without the assigned AM (Gabriella) knowing. The BDM told the owner EatClub would refund offerless transactions — a commitment the AM couldn't confirm. Owner says "she can't get a straight answer from anyone" and calls EC "fraudulent and liars." This is a process failure, not a venue failure. Requires immediate senior intervention. Recommend Pan or Luke call Ginny directly.

**2. Pickled Monkey Brewing** ⚠️ CONFIRMED CHURN
- **restID**: 628911A8-F348-4958-BD7A-8915B7FB3D14
- **Signals**: T002 (double dipping cited in churn call) + T013 (HubSpot: "Do not debt our card")
- **Sources**: Slack (Nader Masrour) + HubSpot (venue owner)
- **Journey stages**: Ongoing engagement → Renewal-churn decision
- **Analysis**: Two-source confirmation. Venue owner was adamant on call — "waste of time" to meet in person. Double dipping was the stated reason. Debt demand arriving via HubSpot suggests outstanding balance. Classic T002 + T013 co-occurrence.

**3. Yum Yum Tree Victoria Park** — escalated from WATCH to CRITICAL
- **restID**: 7831FFCB-CFC7-4B48-A98B-564D4B4E29E2
- **Signals**: T012 (in churn/pause batch) + Mixpanel (1 session, 0 edits, 3 offers views — looking but not acting)
- **Sources**: Slack (Libby Egan) + Mixpanel
- **Journey stages**: Ongoing engagement → Renewal-churn decision
- **Analysis**: Prior-week note: "No one bothered to call me" (AM non-responsive complaint). Now in Libby's churn/pause batch. Mixpanel shows the venue logged in and viewed offers tab 3 times but made no edits — possible "last look" before disengaging. Friction stack: T012 (silence) + T006 (AM non-response) + now churn.

**4. Mr Ramen San (Mid City + The Nova)**
- **restIDs**: 51077CCA-E630-4551-BB38-1CED8858F7F9 (Nova), Mid City (unknown restID)
- **Signals**: T011 ($65.63 refund not received, demanding bank details removal) + cascade to 2nd venue
- **Sources**: Churn (Jessie Helyar)
- **Journey stages**: Ongoing engagement → Renewal-churn decision
- **Analysis**: Billing dispute at Mid City has now caused churn at Nova. Owner Royston "still wants proof we paid the refund." This is a T004-adjacent pattern — single owner pulling multiple venues due to unresolved issue at one. Emma (senior) emailed receipt, waiting on response. If Nova is lost, this becomes a 2-venue cascade from a single $65.63 billing error.

**5. Thornbury Taphouse** — CONFIRMED CHURN
- **restID**: E69B286F-99D3-41CD-A93C-EBE8839EF373
- **Signals**: T002 (offers on specials) + T003 (POS integration attempted, owner dragged feet) + refund demand
- **Sources**: Slack (Cameron Landis)
- **Journey stages**: Ongoing engagement → Renewal-churn decision
- **Analysis**: T002 + T003 co-occurrence confirmed for the second time (after Life of Chi W16). Venue tried POS integration but owner didn't follow through, then demanded refund for all redeemed offers on specials. The item exclusion gap (T007) would have prevented this — if the venue could exclude specials from EC offers, the double-stacking wouldn't occur.

**6. Lulo Spice & Bar** — CONFIRMED CHURN
- **restID**: C2E82FF1-730F-4921-A6BE-26B963856D69
- **Signals**: T010 (customers outside arrival times) + T013 ($160.74 debt, refusing to pay, citing T&C violations)
- **Sources**: Churn (Cameron Landis)
- **Journey stages**: Ongoing engagement → Renewal-churn decision
- **Analysis**: New dangerous pattern: venue using T&C abuse incidents as justification for non-payment. "He said he didn't have to pay because customers weren't following T's and C's." Previously churned in Nov 2025, resigned March, paused 3 weeks later. Account blacklisted. If this logic spreads to other venues with T&C complaints, debt collection becomes systemically harder.

**7. Annata** — ACTIVE BUT AT RISK
- **restID**: 342C2191-4A42-4E46-A5A1-A735B0EA08F0
- **Signals**: T002 (First Table double dip documented with receipts) + Mixpanel (5 offer edits, 11 offers views — actively engaged)
- **Sources**: Slack (Jasmine Jung) + Mixpanel
- **Journey stages**: Ongoing engagement
- **Analysis**: Interesting tension — this venue is actively managing their offers on Portal (healthy engagement) while simultaneously dealing with cross-platform customer abuse. An engaged venue that could churn if the double-dipping issue isn't resolved. Worth proactive AM outreach.

---

### 💡 Synthesis notes

**What surprised me:**

1. **Busan Baby is the worst internal coordination failure I've seen in Crilly's memory.** Three staff touched one churn case — BDM, senior BDM, and a different AM — without the assigned AM knowing. The BDM made a refund commitment the company may not be able to honour. This isn't a product problem, it's a process catastrophe that will repeat without HubSpot ticket ownership enforcement.

2. **The T010 + T013 co-occurrence at Lulo Spice is a new and contagious pattern.** If venues learn they can cite customer misbehaviour as grounds for non-payment, every T&C abuse incident becomes a potential debt refusal. The fix isn't collections — it's T010 tooling (flag/block bad customers) so venues never feel the T&C abuse in the first place.

3. **885 venues active on Portal in 3 days is a genuinely positive OKR2 signal** that risks being drowned out by churn noise. Self-serve IS happening. The problem isn't adoption — it's capability ceiling. Venues are hitting the wall of what Portal lets them do, and the overflow becomes AM workload.

4. **Gogyo is the second group cascade in recent weeks** (after Ramen Ippudo). The pattern is identical: AM can't access decision-makers, POC gatekeeps. EatClub has no group-level account management framework. Two data points don't make a trend, but the structural vulnerability is clear.

5. **Performance tab usage is abysmal.** Across hundreds of engaged venues, most show 0 performance-tab clicks. Venues are managing deals blind — editing offers without understanding impact. This is the biggest untapped lever for OKR2.

**What is missing:**

- **Deal score data is a black hole this run.** T001 (397 zero-score venues) cannot be validated. The collector parsed a CSV but found nothing. Either the data source has changed, the file is stale, or the parser is misconfigured. This needs investigation before next run.
- **Granola absence** means zero qualitative AM-meeting signals. Key context from face-to-face venue conversations is invisible this run.
- **HubSpot scan was budget-limited** (300 tickets/notes). Watch list venues showed no in-window activity, but they may have tickets outside the sampled range.
- **Two unmapped signals worth tracking**: (a) Da Vinci order routing failure — order showed "sent" but venue never received it, suggesting a silent drop in the order relay pipeline; (b) Subzilla Deli — venue threatening to cancel because EC customer left a negative Google review that dropped their rating from 4.8 to 4.7. Neither fits existing themes but could be emerging patterns.

**Interview questions to sharpen weakest signals:**

- **T009 (Onboarding expectation gap)**: "Walk me through what you were told about commission and discounts when you signed up. At what point did reality diverge from expectation? Was there a specific moment where you realised the economics weren't what you expected?"
- **T004 (Group cascade)**: "When the decision was made to leave EatClub, who made it? Was it your decision or a head-office directive? What would have changed your mind? Did you feel your AM had access to the right people?"
- **OTiS pricing model**: "You mentioned EC gives discounts to people who already come here. How do you currently distinguish between new and returning customers? If EC could target offers only at new customers, would that change your view?"
- **Performance tab**: "When you log into Partner Portal, do you look at your deal performance? What information would you need to see to decide whether to increase or decrease your offers?"

**What would move OKR 1 most?**

Build Partner Portal self-serve for the 5 config actions that generate the most manual requests: (1) time-slot-specific offer creation/editing, (2) NCI/RCI boost toggle, (3) guest/party-size limits, (4) item/category exclusion, (5) first-time-customer offer restriction. Mixpanel bulk-edit detection should auto-flag sessions >15 edits and prompt venues for self-serve activation. Conservative estimate: each self-serve action eliminates 10-15 minutes of AM time per occurrence. With 8+ occurrences per week across the team, this is 2+ hours/week recovered immediately, scaling as adoption grows.

**What would move OKR 2 most?**

Two interventions: (1) Make Performance tab the default landing page on Portal login, or add a "How are your deals performing?" banner to the offers tab — most venues never click Performance despite active engagement. (2) Fix T005 (deal settings reverting / holiday hours auto-application) — if venues can't trust their configuration is stable, they won't invest in optimising it. Trust precedes engagement.

---

### Routing block