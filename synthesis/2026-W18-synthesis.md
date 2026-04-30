**Sources available this run**: Slack, HubSpot, Churn, Mixpanel
**Sources unavailable / failed**: Granola (no customer-facing meetings in window — agent skipped), Dealscore (parsed 30 rows, returned 0 signals — no score changes detected)
**Confidence note**: This run covers a narrow ~1.75-hour window (02:01–03:46 UTC, 30 Apr 2026) for Slack and HubSpot. Churn data is more complete (21 AU churns from full CSV parse). Mixpanel covers a full day (153 unique venues, capped at 100). The narrow Slack/HubSpot window means signal counts are understated — 3 billing disputes in under 2 hours suggests a much higher daily rate. Granola absence means no AM meeting colour this run. Dealscore returning zero signals is a coverage gap — the 397 zero-score venues from W16 remain unverified. Heat scores for T001 carry forward on chronic rule but are unrefreshed.

---

### 🔥 Rising themes this week

**1. T011 — Billing disputes and refund confusion**
- **Theme tag**: T011
- **Heat**: 🔴 HIGH
- **Signal count**: 5 signals / 3 sources (Slack, HubSpot, Churn)
- **Lifecycle**: CHRONIC (4+ weeks — migrated from SMS baseline, now confirmed with live signals)
- **Problem statement**: Venues and consumers can't get timely clarity on charges, transactions, and refunds. When proof of refund isn't provided, venues lose trust and churn — sometimes pulling sibling venues with them. Three billing disputes surfaced in a single 2-hour Slack window, suggesting this is constant background noise for CS and AMs.
- **Mom Test quality**: STRONG — *"We have not received any refund of $65.63. Please provide us the date or receipt... Since we continue to have issues with Eatclub for Mid City site, we decided to stop entire partnership with Eatclub for Nova site as well."* (Mr Ramen San, confirmed churn, 2 venues lost). Shiraaz: *"They are claiming that we are not transparent on the contract specifications and billing processes. They said they want to disable our service until this matter is resolved."*
- **OKR**: OKR3 (Churn Reduction)
- **OST branch**: Friction in core venue experience
- **Journey stage**: Ongoing engagement → Renewal-churn decision
- **Recommended action**: **Discovery ticket** — Map the full billing dispute lifecycle (charge → query → CS ticket → AM escalation → refund → confirmation). The refund-proof gap (Mr Ramen San waited weeks for a receipt) is a specific, fixable system failure. Also: the consumer-side complaint ($230.55 venue overcharge + unauthorized tip) suggests billing friction flows in both directions.

---

**2. T007 — Partner Portal self-serve gap: AMs manually doing venue config**
- **Theme tag**: T007
- **Heat**: 🔴 HIGH
- **Signal count**: 3 clean Slack signals this run / 1 source (Slack)
- **Lifecycle**: CHRONIC (4+ weeks)
- **Problem statement**: Venues cannot perform basic configuration changes — NCI boost, takeaway enable, offer adjustments — through Partner Portal. AMs must request these through ops Slack channels, burning time on both sides. In a 1.75-hour window, Aaron Pantazis submitted 2 manual requests and Tania Marinopoulos submitted 1. Extrapolated across a full day and 23 AMs, this is the single highest-volume manual task category.
- **Mom Test quality**: STRONG — *"Please add NCI boost on all their daily 25% deals"* (Aaron, Big Belly Burgers). *"Can we enable TA... On the phone with the venue now and wants to do the TA test order"* (Aaron, Wise Guys — real-time AM bottleneck). *"TA issue fixed at Le Feu Oasis. Please can we enable TA"* (Tania — AM had to follow up on a fix and then separately request enablement).
- **OKR**: OKR1 (primary — direct manual AM work), OKR2 (venues can't self-serve)
- **OST branch**: Manual AM task reduction / Venue self-serve capability
- **Journey stage**: Ongoing engagement
- **Recommended action**: **Discovery ticket** — Audit all config actions currently gated behind ops channels (NCI boost, TA enable, seat times, guest limits, no-show buffer, boost removal — at least 6 distinct action types identified across W16-W17). Size the volume: how many of these requests flow through Slack daily? Which can be exposed in Partner Portal with appropriate guardrails?

---

**3. T004 — Group cascade churn: Gogyo adds to pattern**
- **Theme tag**: T004
- **Heat**: 🟡 MEDIUM
- **Lifecycle**: RISING (W2 — 2nd distinct group affected)
- **Signal count**: 2 signals / 1 source (Churn)
- **Problem statement**: When a multi-venue group decides to churn, all venues go simultaneously and AMs have no path to the decision-makers. Gogyo (Surry Hills + Fitzroy) is the second group cascade after Ramen Ippudo (8 venues, W16). The AM's point of contact "hid behind the directors decision and would not include them on any meeting attempts." Group churn amplifies venue loss by 2–8x per event.
- **Mom Test quality**: STRONG — *"Group churned as they are coming into their busy season and they have also started a two for one promotion on the first Wednesday of every month. My POC hid behind the directors decision and would not include them on any meeting attempts."* (Elliot Rayment, AM)
- **OKR**: OKR3 (Churn Reduction)
- **OST branch**: Product fit for enterprise-Groups
- **Journey stage**: Renewal-churn decision
- **Recommended action**: **Interview** — Two group cascades in two weeks is a pattern. Interview Elliot Rayment on the Gogyo situation: What warning signs existed before the group decision? When was the last meaningful contact with actual decision-makers? What would have needed to exist in the system to flag this earlier?

---

**4. T009 — Onboarding expectation gap: financial viability misalignment**
- **Theme tag**: T009
- **Heat**: 🟡 MEDIUM
- **Lifecycle**: RISING (W3)
- **Signal count**: 3 signals / 1 source (Churn)
- **Problem statement**: Venues sign up expecting revenue uplift but discover that discount costs + commission + monthly fees erode margins they can't afford to lose — especially under rising food and labour costs. This week's churns include Khao Thai ("not seeing any difference in income"), Nurish Cafe ("commission is too high, running at a loss"), and Chaan Thai ("cannot maintain profit margin with even 20% deals"). The common thread: the value proposition wasn't stress-tested against the venue's actual margins during sales.
- **Mom Test quality**: MEDIUM — Specific financial complaints but framed as opinions about platform economics rather than documented cost analysis. *"With rising operating costs, it has become difficult for us to continue offering additional discounts"* (Khao Thai). *"Venue cannot maintain their profit margin with even 20% deals. They run way too lean. Saved in March but churning again"* (Chaan Thai — repeat churn after prior save attempt).
- **OKR**: OKR3 (Churn Reduction)
- **OST branch**: Onboarding journey quality / Surfacing product value through data
- **Journey stage**: Activation → Renewal-churn decision
- **Recommended action**: **Watch + Interview** — This is the third consecutive week with margin-mismatch churns. Interview BDMs (Matthew Behan flagged Chaan Thai, Aaron Pantazis flagged Khao Thai) on how margin feasibility is assessed during sales. Is there a pre-sign calculator or margin check?

---

**5. T001 — Deal score zero venues accumulating (DATA GAP)**
- **Theme tag**: T001
- **Heat**: 🔴 HIGH (chronic default — maintained on accumulated evidence)
- **Signal count**: 0 signals this run / 0 sources
- **Lifecycle**: CHRONIC (4+ weeks)
- **Problem statement**: 397 venues at deal score = 0 as of W16, up from 284 in W15 (+113 in one week). No system alert exists. No new data this run — dealscore collector parsed the CSV but returned zero score changes. The structural risk remains: every score-0 venue is invisible to the churn detection system.
- **Mom Test quality**: N/A this run (no new signals)
- **OKR**: OKR3 (Churn Reduction)
- **OST branch**: Friction in core venue experience / Surfacing product value through data
- **Journey stage**: Ongoing engagement → Renewal-churn decision
- **Recommended action**: **Escalate (data gap)** — The dealscore collector needs to be checked. Returning 0 signals from a known population of 397+ zero-score venues suggests either a data pipeline issue or the CSV format changed. This theme cannot be properly tracked without working dealscore ingestion.

---

### 📋 All signals this week — classified

**Slack signals (9)**

| Signal summary | Source | Author | Author team | Who affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| Shiraaz Geelong: transaction not showing, contract transparency complaint, threatening to disable | Slack #cs-and-am | Harold Paet | Unknown team | Venue owner (Qaser Khan) | STRONG | OKR3 | T011 | Friction in core venue experience |
| Smokin' Joes Pizza: venue sold/closed, confirmed by drive-by | Slack #churned_or_changed | Tom McGay | AM | Venue (closed) | STRONG | OKR3 | Unmapped (involuntary closure) | N/A |
| Big Belly Burgers: NCI boost request on all daily 25% deals | Slack #churned_or_changed | Aaron Pantazis | AM | AM time + venue config | STRONG | OKR1/OKR2 | T007 | Manual AM task reduction |
| Pickled Monkey Brewing: disputing charge from last week | Slack #cs-and-am | Harold Paet | Unknown team | Venue owner | MEDIUM | OKR3 | T011 | Friction in core venue experience |
| Buteko: refund processing confusion, both venue and consumer contacted CS | Slack #cs-and-am | Jai Richards | Unknown team | Venue + Consumer | MEDIUM | OKR3 | T011 | Friction in core venue experience |
| Cafe Gold Coast: live but offers can't be redeemed | Slack #tech-halp-super-urgent | Mitch Thompson | BDM | New venue (go-live blocked) | MEDIUM | OKR3 | Unmapped (go-live activation bug) | Onboarding journey quality |
| La Botte Pizza: BDM at venue for GUID onboarding tap | Slack #sales-admin | Karen Sbaiz - Trinidad | Unknown team | Watch list venue | N/A | N/A | N/A (operational) | N/A |
| Le Feu Oasis: TA enable request after issue fix | Slack #sales-admin | Tania Marinopoulos | AM | AM time + venue config | STRONG | OKR1/OKR2 | T007 | Manual AM task reduction |
| Wise Guys Pizza: TA enable request, AM on phone with venue | Slack #sales-admin | Aaron Pantazis | AM | AM time + venue (waiting) | STRONG | OKR1/OKR2 | T007 | Manual AM task reduction |

**HubSpot signals (5)**

| Signal summary | Source | Author | Author team | Who affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| La Botte: new deal, completed product testing + demos | HubSpot | Prudence Madigan | BDM | Watch list venue (positive) | N/A | N/A | N/A (expansion) | N/A |
| Unknown venue: full account close process executed | HubSpot | Fernando Magistrado | Unknown team | Churned venue | MEDIUM | OKR3 | Unmapped | N/A |
| MoonChild Bistro: reignition, completed demos | HubSpot | Tania Marinopoulos | AM | Reactivation | N/A | N/A | N/A (positive) | N/A |
| Unknown venue: re-enabled after month in pause | HubSpot | Liel Cohen | Unknown team | Paused venue | LOW | N/A | N/A (positive) | N/A |
| Consumer: $230.55 refund request — venue overcharged + unauthorized $25.10 tip | HubSpot | Unknown | Unknown team | Consumer + venue | MEDIUM | OKR3 | T011 / T010 | Friction in core venue experience |

**Churn signals (21)**

| Signal summary | Source | Author | Author team | Who affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|---|---|
| Mr Ramen San Nova: refund not processed, cancelling both venues, demanding bank details removed | Churn | Jessie Helyar | Unknown team | 2 venues (Mid City + Nova) | STRONG | OKR3 | T011 | Friction in core venue experience |
| Zircon Restaurant: early churn, "numbers not working", AOV $110, 41 customers | Churn | Kane Russell / Cameron Landis | AM / Unknown | Venue owner (Asanka) | MEDIUM | OKR3 | T009 | Onboarding journey quality |
| Monsoon Palace: venue sold to Chedda Boy, couldn't convert new owner | Churn | Nader Masrour | AM | Venue (sold) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| M Yong Tofu: offerless model unsustainable, wants lower than 20% deals | Churn | Aaron Pantazis | AM | Venue owner | MEDIUM | OKR3 | T009 | Surfacing product value |
| Di Francesco Cucina: venue closed | Churn | Tom McGay | AM | Venue (closed) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| Khao Thai Little Bay: rising costs, not seeing income difference, offered offerless but refused | Churn | Aaron Pantazis | AM | Venue owner | MEDIUM | OKR3 | T009 | Onboarding journey quality |
| NC's Chaat and Dosa House: venue closed, owner returned to IT | Churn | Cameron Landis | Unknown team | Venue (closed) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| Rascals Deli: permanently closed on Google, owner unreachable since March | Churn | Gabriella Szabo | AM | Venue (closed) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| Chaan Thai: can't maintain profit margin even at 20%, saved in March but churning again | Churn | Matthew Behan | BDM | Venue owner | STRONG | OKR3 | T009 | Onboarding journey quality |
| Lulo Spice & Bar: $160.74 debt, T&C abuse (arrival times), re-sign → pause → blacklist | Churn | Cameron Landis / Nancy Tandual | Unknown team | Venue + AM | STRONG | OKR3 | T010 + T013 | Friction in core venue experience |
| Gogyo Surry Hills: group churn, too full, POC blocked director access | Churn | Elliot Rayment | AM | 2+ venue group | STRONG | OKR3 | T004 | Product fit for enterprise-Groups |
| Baba Ganouj: "I didn't like it", early churn, missing transactions | Churn | Matthew Behan | BDM | Venue owner (Sally) | WEAK | OKR3 | Unmapped (early churn, vague) | Onboarding journey quality |
| Melrose Restaurant: "missing features", no details, trying to reach out | Churn | Sam McKenzie | AM | Venue owner | WEAK | OKR3 | Unmapped (vague) | Product experience |
| San Churro Southbank: venue sold back to HO, new owners incoming | Churn | Matthew Behan | BDM | Venue (sold) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| Gogyo Fitzroy: group churn (same group as Surry Hills) | Churn | Elliot Rayment | AM | 2+ venue group | STRONG | OKR3 | T004 | Product fit for enterprise-Groups |
| Pot au Pho Bar Mornington: closed indefinitely, may sell or close | Churn | Tania Marinopoulos | AM | Venue (closed) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| Mr Toast: sold, new owner rejected EC + all third parties | Churn | Brianna Quinn | Unknown team | Venue (sold) | STRONG | OKR3 | Unmapped (involuntary) | N/A |
| Sideshow Burgers Rosanna: ownership change, re-signing with new contract | Churn | Elodie Fitzsimmons | Unknown team | Technical churn (re-sign) | STRONG | N/A | Unmapped (positive churn/re-sign) | N/A |
| The Lil Hut Bardwell Park: sold, no referral interest | Churn | Unknown | Unknown team | Venue (sold) | MEDIUM | OKR3 | Unmapped (involuntary) | N/A |
| My Place: called to cancel, BDM (Otis) attempting save | Churn | Gabriella Szabo | AM | Venue owner (Izi) | WEAK | OKR3 | Unmapped (vague early churn) | N/A |
| Nurish Cafe Bondi Junction: fees too high, running at loss, closing down | Churn | Kane Russell / Brianna Quinn | AM / Unknown | Venue owner | MEDIUM | OKR3 | T009 | Onboarding journey quality |

**Mixpanel — aggregate summary (not individually tabled)**

153 unique venues engaged with Partner Portal. Top-line:
- 15 venues with 3+ offer edits (active deal managers)
- ~52 venues made at least 1 offer edit
- ~23 venues clicked Performance tab (only 15% of engaged venues)
- 1 venue made 7 performance tab clicks with 0 offer edits (data-exploration-only session)
- 0 watch list hits
- Dominant pattern: venues come to edit offers, not to review performance data. Performance tab engagement remains strikingly low relative to offers engagement. This is the OKR2 gap in quantified form.

---

### 🗺️ OST update

**OKR 1 — Scale AM Optimisation**

| Branch | Status |
|---|---|
| **Manual AM task reduction** | STRENGTHENED. 3 manual config requests in 1.75 hours (NCI boost, TA enable x2). Aaron Pantazis alone submitted 2. Extrapolated across a full day and 23 AMs, this is the most volume-dense automation opportunity. |
| **Venue self-serve capability** | STRENGTHENED. The Mixpanel data shows venues *are* using Partner Portal for offers (52+ venues edited offers today). But they can't do NCI boost, TA enable, or other config changes there — they must go through AM → ops channel. The portal is half-built for self-serve. |
| **System automation** | NO CHANGE. No new signals on automated alerting, OOO routing, or proactive system actions this run. T006 (AM vacation coverage gap) had no new evidence. |

**OKR 2 — Drive Deal Performance Through System-Led Actions**

| Branch | Status |
|---|---|
| **Partner Portal engagement** | STRENGTHENED with nuance. 153 venues active in one day is a positive baseline. But only 15% clicked Performance tab — venues manage offers but don't explore revenue data. The one venue with 7 performance clicks and 0 edits is interesting: they looked at data extensively but didn't take action. Why? |
| **Venue-led revenue actions** | WEAKENED. Venues are editing offers (good) but not being guided to revenue-driving actions. The 3 Slack config requests (T007) show that some revenue actions (NCI boost, TA enable) still require AM intervention — venues can't self-serve into higher performance. |
| **Deal score visibility and trust** | NO CHANGE (data gap). Dealscore collector returned 0 signals. Cannot assess. |

**OKR 3 — Churn Reduction**

| Branch | Status |
|---|---|
| **Friction in core venue experience** | STRENGTHENED (negative). T011 billing disputes are the dominant friction signal: 5 instances across 3 sources, 1 confirmed churn with group contagion (Mr Ramen San losing both venues). Lulo Spice adds T&C abuse + debt. |
| **Product fit for enterprise-Groups** | STRENGTHENED (negative). Gogyo is the 2nd group cascade in 2 weeks (after Ramen Ippudo). Pattern is clear: AMs can't access group-level decision-makers; when the decision is made, it's final and affects all venues simultaneously. |
| **Onboarding journey quality** | STRENGTHENED (negative). 3 margin-mismatch churns (Khao Thai, Nurish Cafe, Chaan Thai) + early churns (Zircon, Baba Ganouj, My Place). Venues sign without understanding the economics. Chaan Thai was "saved in March but churning again" — save didn't address root cause. |
| **Surfacing product value through data** | WEAKENED. Mixpanel shows 85% of portal-engaged venues ignore Performance tab. If venues can't see or understand their EatClub-driven revenue, they default to "I'm not seeing a difference" (Khao Thai) or "numbers aren't working" (Zircon). |

---

### ⚠️ Friction stack watch

**1. Mr Ramen San — Mid City + The Nova (Little Bourke St)**
- **restID**: 51077CCA-E630-4551-BB38-1CED8858F7F9 (Nova); Mid City restID unknown
- **Signals**: Churn (confirmed) — $65.63 refund not processed → proof of payment never sent → trust destroyed → both venues cancelled → demanding bank details removed
- **Journey stages**: Ongoing engagement (billing dispute) → Renewal-churn decision (group contagion)
- **Friction stack**: Refund processing failure (T011) → AM/CS communication gap → escalation to Emma (leadership) → still unresolved weeks later → sibling venue pulled into churn
- **Analysis**: This is the textbook friction cascade. A $65.63 problem became a 2-venue loss. The refund was apparently made but proof was never sent to the venue until very late ("Emma emailed the receipt today; waiting on response"). The delay between refund and confirmation destroyed trust. Even after escalation to a senior role, the venue had to ask multiple times. The Nova may still be saveable if proof arrives quickly — Royston "will consider reactivating" if refunds confirmed.
- ⚠️ **FLAG TO LUKE**: Active save opportunity on Nova if refund receipt is confirmed. Time-sensitive.

**2. Shiraaz Geelong Indian Restaurant**
- **restID**: UNKNOWN — needs lookup
- **Signals**: Slack #cs-and-am — transaction not showing on venue's end + contract transparency complaint → threatening to disable
- **Journey stages**: Ongoing engagement (transaction discrepancy) → Renewal-churn decision (disable threat)
- **Friction stack**: Missing transaction visibility (T011) → venue feels contract terms aren't transparent → QC'd (paused?) pending AM call
- **Analysis**: Harold Paet (CS) routed to an AM but the venue owner (Qaser Khan) is already at disable-threat stage. This mirrors the early stage of Mr Ramen San: a billing discrepancy that, if unresolved, compounds into churn. Needs immediate AM callback.
- ⚠️ **FLAG TO LUKE**: New churn risk — needs AM assignment and same-day callback.

**3. Lulo Spice & Bar**
- **restID**: C2E82FF1-730F-4921-A6BE-26B963856D69
- **Signals**: Churn (confirmed) — resigned in March → paused 3 weeks later due to $160.74 debt → owner dodging calls → complained about T&C abuse (arrival times) → refused to pay debt → blacklisted
- **Journey stages**: Activation (re-sign) → Ongoing engagement (T&C abuse, debt accumulation) → Renewal-churn decision (blacklisted)
- **Friction stack**: Re-sign (T009 — expectations reset?) → T&C abuse frustration (T010) → debt accumulation (T013) → refusal to pay → complete relationship breakdown
- **Analysis**: Classic 3-layer friction stack. The venue was churned once, re-signed, then hit every friction point in sequence. The owner's position — "he didn't have to pay because customers weren't following T's and C's" — reveals that T&C abuse directly enables debt disputes. T010 and T013 are linked.

**4. Garibaldi Pizzeria (existing watch list — CRITICAL, no new signals)**
- **restID**: UNKNOWN — needs lookup
- **Notes**: Still CRITICAL from W15-W16. Angie urgently contacting multiple channels. No signals this run across any source. Silence on a CRITICAL venue is itself a signal.
- ⚠️ **FLAG TO LUKE**: No activity visible on Garibaldi across Slack, HubSpot, or Churn. If no AM is actively engaged, this is slipping.

**5. The Last Jar (existing watch list — CRITICAL, no new signals)**
- **restID**: EC9FABAF-1C92-4C45-8C6F-79B836A09D20
- **Notes**: 4th cancel request from Bryony. No new signals this run. Silence suggests either save attempt in progress off-channel, or venue has been let go.

---

### 💡 Synthesis notes

**What surprised me:**
- **48% of this week's churns are involuntary** (venue closed or sold). 10 of 21 churned venues simply ceased to exist — not a product or service failure. This inflates the churn rate in ways that no product intervention can address. If EatClub separated involuntary churn (closure/sale) from voluntary churn (dissatisfaction), the actionable churn rate would drop meaningfully. The Sideshow Burgers signal is encouraging: ownership changed and the new owner is re-signing. There may be an opportunity to systematize new-owner conversion for sold venues.
- **T011 velocity is alarming.** 3 billing disputes in under 2 hours on Slack, plus a confirmed 2-venue churn from a single unprocessed refund. This is not a new theme — it was migrated from SMS baseline data — but this is the first run where live, high-confidence signals stack up across multiple sources simultaneously. Billing friction appears to be constant background noise that CS and AMs absorb every day.
- **The churn collector is over-mapping to T007.** Four financial-viability churns (Zircon, Chaan Thai, Lulo Spice, My Place) were mapped to T007 (Partner Portal self-serve gap) by the collector, but their evidence describes margin pressure and economic unsustainability, not self-serve gaps. This inflates T007's churn-linked signal count. I corrected these to T009 and other themes in my analysis. The collector's theme-matching logic should be reviewed.

**What is missing:**
- **Dealscore data is a blind spot.** 397 zero-score venues were identified in W16 and we have no update. The dealscore collector parsed the CSV but returned nothing. Either the input data has changed format, the threshold logic isn't matching, or there genuinely were no changes — but the latter seems unlikely.
- **Granola silence means we lose AM meeting context.** No meetings this window = no qualitative insight from venue conversations. The quantitative signals (Slack requests, churns) don't tell us what AMs are hearing in calls. Were any of the churn venues flagged in prior AM meetings?
- **No insight on T005 (deal settings reverting).** This was RISING in W16 with 4 venues affected. Zero signals this run. Either it's been fixed, it's happening off-channel, or the narrow window missed it.
- **Watch list venues are silent.** 7 of 9 watch list venues produced zero signals across all sources. For CRITICAL venues (Garibaldi, The Last Jar), silence is itself concerning.

**Interview questions to sharpen weakest signals:**

For **T004 (Group cascade churn)** — interview Elliot Rayment (AM):
1. "Walk me through the last 4 weeks with Gogyo. When did you first sense the group was considering leaving?"
2. "You mentioned the POC hid behind the directors — had you ever had direct contact with the directors? What would you have needed to reach them?"
3. "If the system had flagged 'multiple venues in this group showing declining deal engagement' 6 weeks ago, what would you have done differently?"

For **T009 (Financial viability churn)** — interview Aaron Pantazis (AM, flagged Khao Thai + M Yong Tofu) and Matthew Behan (BDM, flagged Chaan Thai):
1. "Chaan Thai was saved in March but churned again. What was the save offer? Why didn't it hold?"
2. "When a venue says 'the numbers don't work even at 20%', do you have access to their actual margin data? What would help you assess viability before churn?"
3. "How often do you encounter venues where the BDM's original pitch didn't match the venue's economic reality?"

For **T011 (Billing disputes)** — interview Harold Paet (CS, surfaced 2 of 3 Slack billing disputes):
1. "How many billing dispute tickets do you handle per day on average?"
2. "When a venue disputes a charge, what's the typical resolution path and how long does it take?"
3. "In the Shiraaz case, the venue said contract specs and billing processes aren't transparent. What specifically are they confused about?"

**What would move OKR 1 most:**
Exposing NCI boost, takeaway enable, and offer configuration in Partner Portal self-serve. The T007 signals are precise, repeated, and directly measurable. Three requests in 1.75 hours × projected across a full day × 23 AMs = significant manual hours. This is the most concrete, highest-confidence OKR 1 opportunity in the current signal set.

**What would move OKR 2 most:**
The Mixpanel data reveals the gap: venues use Partner Portal for offer management but almost never engage with performance data (85% skip the Performance tab). Two levers:
1. Make performance insights unavoidable — surface them in the offers flow rather than gating them behind a separate tab.
2. Connect performance data to recommended actions ("Your Thursday lunch deals drove 12 extra covers last week — want to extend to Friday?"). The venue with 7 performance clicks and 0 edits is a clue: even when venues look at data, they don't know what action to take.

---

### Routing block