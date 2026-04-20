# 🧠 Crilly Weekly Synthesis — Week of 14–20 April 2026

**Data coverage:** Granola (21 signals), HubSpot (17 signals), Churn history (30 venues), SMS (empty). **Gaps:** Slack signals (not received in structured form), Deal Score CSV (not provided), Mixpanel (no credentials). This is Crilly's baseline synthesis — lifecycle labels are inferred from signal age and leadership context.

---

## 🔥 Rising Themes This Week

### 1. Deal economics don't match venue reality — discount depth and structure are structurally unworkable for a significant segment

**Heat: HIGH**
**Lifecycle: CHRONIC (inferred — churn data confirms this pattern over 18+ months)**
**Signal count: 14 | Sources: 3 (Granola, HubSpot, Churn)**
**Recurrence: Chronic**

**Problem statement:** Venues operating on thin margins ($2–$4/meal) cannot sustain EatClub's minimum discount thresholds (often 25–30%), and the flat daily deal window ignores how venues actually think about capacity — by meal period, staff shift, and cover count. When venues can't configure deals that match their economics, they either run unprofitable deals and churn, or disengage immediately.

**Mom Test quality: STRONG.** Sam Benjamin reports a direct pattern from two weeks of live venue conversations: pitching spare capacity per meal period resonates, but the current flat deal structure forces venues into a single discount across hours with wildly different conversion rates. Churn records from Hells Bellz (30% unviable on thin margins), Restaurant 233 ($2/meal margin makes any discount impossible), and Zio Pino (can't go above 20%) confirm this with specific dollar figures. Famished Wolf's AM call documents $4,000 gross from 210 discounted customers over 3 weeks with the owner questioning whether EC customers ever convert to full-paying regulars.

**OKR: OKR 2 (Deal Performance) primary; OKR 3 (Churn) secondary**
**OST branch:** Deal performance → Venue-led revenue actions; Churn reduction → Friction in core venue experience
**Journey stage:** Activation → Ongoing engagement → Renewal/churn decision
**Recommended action: Discovery ticket** — Sam's meal-period-based deal structure proposal needs product scoping immediately. 18,000 deals are configured in a model that leadership acknowledges is wrong.

---

### 2. BDM sign quality and handover failure are responsible for 40% of all churn — and the business has no systematic fix

**Heat: HIGH**
**Lifecycle: CHRONIC (inferred — Adam Glegg cites this as a long-standing pattern with quantified impact)**
**Signal count: 10 | Sources: 3 (Granola, HubSpot, Churn)**
**Recurrence: Chronic**

**Problem statement:** 40% of all EatClub churn happens within 40–60 days of sign-up. Venues are being signed that don't fit EatClub's ICP ("a kebab shop in the back of Tumba"), BDMs can close in 10 minutes without the venue truly understanding the product, and there is no structured handover to AMs. Venues get onboarded but the business is never actually up and running. By the time the AM makes contact, the venue has already dropped its deals and decided to leave.

**Mom Test quality: STRONG.** Adam Glegg cited a specific, quantified statistic (40% early churn within 60 days) from a cross-functional workshop involving Sam Benjamin and Luke Maurel. Allen Luo reported that "BDMs lie and do whatever they have to do to get them signed up" and described a specific 90-minute conflict between Sam and Luke about sales targets vs. churn. The Cheeky Beans (HubSpot) submitted a cancellation request two weeks after joining that went unactioned by the BDM for months. Sam Benjamin's proposed deal-locking intervention ("lock deals for two weeks, then the AM calls as the first optimisation") is itself evidence of how broken the current handover is.

**OKR: OKR 3 (Churn) primary; OKR 1 (AM Optimisation) secondary** — bad signs create downstream AM workload
**OST branch:** Churn reduction → Onboarding journey quality; AM optimisation → System automation opportunities
**Journey stage:** Onboarding → Activation (the gap between sign and first successful deal is where venues die)
**Recommended action: Escalate to Luke + Sam** — This requires a joint Sales/AM process intervention. The two-week deal lock proposal should be evaluated as a near-term fix. Longer term, ICP scoring at sign-up and a structured BDM→AM handover protocol need product support.

---

### 3. AMs are spending hours on deal configuration and venue settings that should be self-serve

**Heat: HIGH**
**Lifecycle: CHRONIC (inferred — Sam Benjamin describes 50 AMs globally affected, Adam Glegg flagged 5 venues this week alone)**
**Signal count: 7 | Sources: 2 (Granola, HubSpot)**
**Recurrence: Chronic**

**Problem statement:** When a venue needs to change 10 deals, it costs an hour of AM time. Fifty AMs globally are doing manual deal configuration, boost enabling, and venue setting changes instead of revenue-generating activities. Venues cannot manage their own configuration through Partner Portal — they can't enable boosts independently, can't adjust deal structures without AM intervention, and can't modify venue settings. This is the single largest block of recoverable AM time.

**Mom Test quality: STRONG.** Sam Benjamin provided a specific cost model: "I want to change 10 deals and I take an hour of account manager time. That is super expensive." Adam Glegg flagged 5 specific venues this week where manual AM intervention was happening for things that should be venue self-serve. Adam also reported that Sam has started building AM tools independently without product engagement — including a rebuilt signup form deployed to BDMs — which signals both urgency and frustration with the pace of change.

**OKR: OKR 1 (AM Optimisation) — this is the direct target**
**OST branch:** AM optimisation → Manual AM task reduction; AM optimisation → Venue self-serve capability
**Journey stage:** Ongoing engagement (this is a constant operational drain, not episodic)
**Recommended action: Discovery ticket** — Audit the top 5 AM tasks by time cost. Cross-reference with Partner Portal capability gaps. Sam's independent tool-building is a leading indicator that product needs to own this space before shadow IT becomes the standard.

---

### 4. Venues go dark and no one knows until it's too late — silence is the most common churn precursor

**Heat: HIGH**
**Lifecycle: CHRONIC (inferred — Garibaldi Pizzeria has been unreachable since November 2025; churn data shows this as a repeating pattern)**
**Signal count: 9 | Sources: 2 (HubSpot, Churn)**
**Recurrence: Chronic**

**Problem statement:** Venues disengage gradually — they stop answering calls, stop logging into Partner Portal, stop honouring deals — but the system has no automated way to detect this pattern before it becomes terminal. By the time an AM notices, the venue has often been dark for weeks or months. Staff at venues sometimes actively block AM contact. The result: venues are listed as active on the platform while operationally they have already left.

**Mom Test quality: STRONG.** Garibaldi Pizzeria has been unreachable since November 2025 — five months of documented silence while the venue accumulated negative Google reviews and stopped honouring EC deals. Crust Pizza Mortdale's staff told a customer "we don't do EatClub anymore" while the venue was still listed as live. I Love Manoush's staff systematically refused to provide the owner's availability. No22 Café required three months of weekly contact attempts before confirming the owner had no intention of returning.

**OKR: OKR 3 (Churn) primary; OKR 1 (AM Optimisation) secondary** — AMs are manually chasing ghosts
**OST branch:** Churn reduction → Friction in core venue experience; AM optimisation → System automation opportunities
**Journey stage:** AM relationship → Renewal/churn decision point
**Recommended action: Discovery ticket** — A "silence score" combining days since last Partner Portal login, days since last AM response, days since last deal redemption, and days since last SMS reply would automate what AMs currently do by gut feel. Sam Benjamin asked the right question: "How do I make sure AMs are going to venues before they churn instead of after?"

---

### 5. Platform integrity failures are causing direct, measurable financial losses to venues

**Heat: MEDIUM → HIGH (rising)**
**Lifecycle: RISING (specific high-cost incidents this week; churn data shows the pattern has existed but was latent)**
**Signal count: 6 | Sources: 2 (HubSpot, Churn)**
**Recurrence: Recurring**

**Problem statement:** Venues are losing real money due to system-level issues they can't control: Lightspeed integration misconfigurations causing double-discounting ($9,000–$12,000 loss at Brick Lane Market), deals continuing to run while a venue is closed (Kake Da Dhaba), offerless diners consuming capacity without any deal (Kate Hunt's venue), and customers gaming the discount window. These are not perception issues — they are actual financial losses that destroy trust faster than any value demonstration can rebuild it.

**Mom Test quality: STRONG.** Brick Lane Market's owner documented a 22% margin hit in cost of goods from double-discounting, estimated at $9,000–$12,000 in losses, in a Gong-recorded call. Kate Hunt (restaurant manager) wrote a detailed complaint documenting offerless dining losses, customers arriving without bookings outside discount windows, and explicitly asked "how are we meant to combat this without cancelling our partnership?" Kake Da Dhaba's owner reported that deals were still being redeemed while the venue was closed and staff were processing takeaway orders on discount — a system integrity failure.

**OKR: OKR 3 (Churn) — platform trust erosion is a direct churn accelerant**
**OST branch:** Churn reduction → Friction in core venue experience
**Journey stage:** Ongoing engagement → Renewal/churn decision (these incidents flip the churn switch immediately)
**Recommended action: Escalate (Brick Lane) + Discovery ticket (offerless dining / deal-while-closed)** — The Brick Lane integration issue needs immediate resolution and financial reconciliation. The pattern of deals running during closures and offerless dining losses needs a systematic product investigation.

---

## 📋 All Signals This Week — Classified

### Granola Signals (April 13–16, 2026)

| Signal summary | Speaker | Who affected | Mom Test | OKR | Theme | OST branch |
|---|---|---|---|---|---|---|
| 40% of all churn is early churn within 60 days; ICP mismatch | Adam Glegg | All venues, BDMs | STRONG | OKR 3 | BDM sign quality | Churn → Onboarding quality |
| BDMs not handing over to AMs; venues onboarded but not running | Adam Glegg | All AMs, new venues | STRONG | OKR 3 | BDM sign quality | Churn → Onboarding quality |
| Venues don't understand product; drop deals then churn; no sales tools | Adam Glegg | New venues, BDMs | STRONG | OKR 3 | BDM sign quality | Churn → Onboarding quality |
| No sales tools or venue pitching for BDMs; 10-min sign-up facilitation is terrible | Adam Glegg | BDMs | STRONG | OKR 3 | BDM sign quality | Churn → Onboarding quality |
| 5 venues flagged for manual AM work that should be self-serve | Adam Glegg | AMs, 5 venues | STRONG | OKR 1 | AM manual work | AM opt → Manual task reduction |
| Partner Portal rising as a theme alongside venue config and dine visibility | Adam Glegg | Venues | MEDIUM | OKR 2 | Visibility gap | Deal perf → PP engagement |
| Data isolated across HubSpot, Slack, Granola; no cross-system visibility | Adam Glegg | All internal teams | STRONG | OKR 1 | Visibility gap | AM opt → System automation |
| BDMs lie to sign venues; no handover; Sam/Luke conflict on targets vs churn | Allen Luo | BDMs, AMs, new venues | STRONG | OKR 3 | BDM sign quality | Churn → Onboarding quality |
| No clarity on Sam's work; API keys given without product review | Allen Luo | Product, AMs | STRONG | OKR 1 | AM manual work | AM opt → System automation |
| Venue config can't be self-managed; dine visibility massive problem; boosts need AM | Adam Glegg | AMs, venues | MEDIUM | OKR 1 | AM manual work | AM opt → Venue self-serve |
| Dine visibility flagged as massive problem in Crilly | Adam Glegg | Venues | MEDIUM | OKR 2 | Visibility gap | Deal perf → Deal score visibility |
| 10 deal changes = 1 hour AM time; 50 AMs globally doing manual config not revenue work | Sam Benjamin | All AMs | STRONG | OKR 1 | AM manual work | AM opt → Manual task reduction |
| AMs going to venues after churn instead of before; need proactive signals | Sam Benjamin | AMs, at-risk venues | STRONG | OKR 3 | Venue silence | Churn → Surfacing value through data |
| Systems don't speak to each other; field teams need live intelligence | Sam Benjamin | AMs, field teams | STRONG | OKR 1 | Visibility gap | AM opt → System automation |
| Sam rebuilt signup form without product; deploying external-facing changes unilaterally | Adam Glegg | Product, BDMs | STRONG | OKR 1 | AM manual work | AM opt → System automation |
| Lock deals for first 2 weeks; AM calls at end of lock as first optimisation | Sam Benjamin | New venues, AMs | STRONG | OKR 3 | BDM sign quality | Churn → Onboarding quality |
| Spare capacity per meal period resonates; "spare capacity" as term doesn't land | Sam Benjamin | Venues, BDMs | STRONG | OKR 2 | Deal economics | Deal perf → Venue-led revenue |
| Deal structure needs meal-period breakdown; 18,000 deals done wrong way | Sam Benjamin | All venues | STRONG | OKR 2 | Deal economics | Deal perf → Venue-led revenue |
| Luke requested deal score history investigation | Martin Heal | AMs, venues | MEDIUM | OKR 2 | Visibility gap | Deal perf → Deal score visibility |
| Onboarding flow has too many steps; could pre-fill services; less BDM/AM touch | Vinni Lazaro | BDMs, AMs, new venues | MEDIUM | OKR 1 | BDM sign quality | AM opt → Manual task reduction |
| 10-min close demo; empty tables = $0 narrative; Hop Jack prospect example | Sam Benjamin | BDMs | STRONG | OKR 2 | BDM sign quality | Deal perf → Venue-led revenue |

### HubSpot Signals (April 13–20, 2026)

| Signal summary | Type | Venue | Churn signal | Mom Test | OKR | Theme |
|---|---|---|---|---|---|---|
| Unresponsive rep + offerless dining + customers gaming system + threatening cancellation | CS ticket | (Kate Hunt, unnamed) | Intent to leave | STRONG | OKR 3 | Platform integrity |
| 5+ months unreachable; negative Google reviews; not honouring deals | CS ticket | Garibaldi Pizzeria | Silence | STRONG | OKR 3 | Venue silence |
| Immediate cancellation due to cost concerns; all deals self-disabled | CS ticket | Oh! Dumplings | Intent to leave | STRONG | OKR 3 | Deal economics |
| Indefinite disablement requested; possible temp closure | CS ticket | Pizza E Vino - Glebe | Intent to leave | MEDIUM | OKR 3 | Venue silence |
| Confirmed churn: deals running while closed, costs increasing, refused retention | CS ticket | Kake Da Dhaba | Intent to leave | STRONG | OKR 3 | Platform integrity |
| Business sold; last day Friday | CS ticket | Leega Korean BBQ | Intent to leave | STRONG | — | N/A (business sold) |
| Pause or cancel; undergoing restaurant changes | CS ticket | Sekka Dining | Intent to leave | MEDIUM | OKR 3 | Venue silence |
| Cancellation request from Feb ignored by BDM; saved this week | CS ticket | The Cheeky Beans | At risk | MEDIUM | OKR 3 | BDM sign quality |
| Cancellation requested; no detail | CS ticket | Mr Chu Contemporary | Intent to leave | MEDIUM | OKR 3 | Venue silence |
| Cancel all 25% offers; expenses too high | CS ticket | (Bishal, unnamed) | Intent to leave | WEAK | OKR 3 | Deal economics |
| Pause requested; platform feels "cheap"; wants AM call | CS ticket | Thien Nga Richmond | At risk | STRONG | OKR 3 | Deal economics |
| Staff refusing EC orders; "haven't done EC for weeks" | CS ticket | Crust Pizza Mortdale | Silence | STRONG | OKR 3 | Venue silence |
| Pause requested; no context | CS ticket | Oramesti Indonesian | At risk | WEAK | OKR 3 | Venue silence |
| Explicit opt-out: "take me out" | CS ticket | Dishoom | Intent to leave | STRONG | OKR 3 | Venue silence |
| Double payment complaint; no response from anyone | CS ticket | (unnamed) | Debt | MEDIUM | OKR 3 | Platform integrity |
| Declining performance post-discount change; $4k/3wk margin concern; questioning value | AM note | Famished Wolf | At risk | STRONG | OKR 3 | Deal economics |
| Lightspeed double-discounting; $9-12k loss; 22% margin hit | AM note | Brick Lane Market | Debt | STRONG | OKR 3 | Platform integrity |

### Churn History (Nov 2023 – Feb 2024) — Pattern Validation

| Category | Count | Key pattern |
|---|---|---|
| Price / margin | 13 (43%) | Dominant driver. Specific margins cited: $2/meal, 30% unviable, can't exceed 20%. Recurring theme: discount depth exceeds what the venue's economics can support. |
| Business closed | 5 (17%) | Mix of permanent closures and temporary events (renovations, landlord disputes) recorded as full churns. |
| No engagement | 4 (13%) | Owners requested pauses then went completely silent. Staff blocked AM contact at multiple venues. |
| Other | 4 (13%) | Includes EC-initiated removal, seasonal over-trading, and EC customer behaviour complaints. |
| Product / operational | 2 (7%) | Business model changes (functions-only pivot) making EC structurally incompatible. |
| Sold | 1 (3%) | Ownership change with no re-onboarding follow-up. |
| Notes quality | 13 WEAK / 7 MEDIUM / 10 STRONG | 43% of churns have zero or near-zero documentation. Critical gap for learning. |

---

## 🗺️ OST Update

### AM Optimisation (OKR 1)

| Branch | Status | Evidence this week |
|---|---|---|
| **Manual AM task reduction** | 🔴 Strengthened heavily | Sam Benjamin quantified cost (10 deals = 1 hour). Adam Glegg flagged 5 venues. 50 AMs globally affected. This is the single most concrete OKR 1 opportunity. |
| **Venue self-serve capability** | 🔴 Strengthened | Boosts, deal config, venue settings all require AM. Partner Portal rising as a theme. Multiple CS tickets direct venues to Partner Portal for actions they should already be able to do. |
| **System automation opportunities** | 🟡 New sub-branch | Sam building tools without product (signup form, AM tools). Data silos across HubSpot/Slack/Granola. Allen Luo flagged API key governance risk. This is both an opportunity (automate what Sam is doing manually) and a risk (shadow IT). |

### Deal Performance (OKR 2)

| Branch | Status | Evidence this week |
|---|---|---|
| **Partner Portal engagement** | 🟡 Rising signal | Flagged in Crilly as a theme. CS tickets show venues being directed to PP but no evidence they complete actions. No Mixpanel data to confirm. |
| **Venue-led revenue actions** | 🔴 Strengthened | Meal-period deal structure would enable venues to optimise by service window. Current flat structure forces bad configs. 18,000 deals are misconfigured per Sam. |
| **Deal score visibility and trust** | 🟡 Weak signal | Luke requested deal score history investigation via Martin Heal. No venue-level signal on deal score confusion this week. Need Mixpanel data. |

### Churn Reduction (OKR 3)

| Branch | Status | Evidence this week |
|---|---|---|
| **Friction in core venue experience** | 🔴 Critical | Platform integrity failures (double-discounting, offerless dining, deals while closed) are direct financial losses. 6 signals across HubSpot and churn. |
| **Onboarding journey quality** | 🔴 Strengthened heavily | 40% early churn stat. BDM sign quality. Handover failure. Deal-locking proposal. 10 signals from leadership workshops. |
| **Surfacing product value through data** | 🟡 Rising | Famished Wolf owner can't tell if EC customers convert. C9 Docklands paid fees for months without using platform. Venues can't see what EC is worth. |
| **Product fit for enterprise / Groups** | ⚪ No signal | No Group-level or enterprise-specific signals this week. |

---

## ⚠️ Friction Stack Watch

**These venues show compounding signals across 2+ journey stages or sources. Flag to Luke immediately.**

### 🚨 CRITICAL — Active churn in progress

| Venue | restID | Signals | Friction stack | Action |
|---|---|---|---|---|
| **Garibaldi Pizzeria** | Unknown | HubSpot: 5+ months unreachable, negative Google reviews, not honouring deals, URGENT ticket | Silence (5 months) → Deal integrity failure → Reputation damage | **Escalate to Luke immediately.** This venue is damaging EC's brand on Google while being completely unreachable. |
| **Brick Lane Market** | Unknown | HubSpot AM note: Lightspeed double-discounting, $9–12k loss, 22% margin hit | Integration failure → Financial loss → Trust erosion | **Escalate to Luke + Eng.** If the integration issue isn't resolved with financial reconciliation, this venue will churn on pure economics. |
| **Kate Hunt's venue** (name unknown) | Unknown | HubSpot: Unresponsive rep + offerless dining losses + customers gaming system + explicit cancellation threat | AM relationship failure → Platform integrity → Intent to leave | **Escalate to Luke.** Multiple compounding failures with an articulate operator who has documented everything. |

### ⚠️ HIGH RISK — Churn trajectory active

| Venue | restID | Signals | Friction stack | Action |
|---|---|---|---|---|
| **The Famished Wolf Kensington** | Unknown | HubSpot AM note: Declining revenue, $4k margin concern, questioning if EC customers convert, gave 1-month window | Deal economics → Value perception gap → Conditional stay | AM Orel has next check-in May 18. Need to deliver value evidence before that call or this churns. |
| **Kake Da Dhaba** | Unknown | HubSpot: Confirmed "venue to be churned." Deals ran while closed, costs increasing, refused retention offer | Platform integrity failure → Cost pressure → Confirmed churn | Already lost. Post-mortem needed — deals running while venue was closed is a system bug. |
| **Crust Pizza Mortdale** | Unknown | HubSpot: Staff refusing EC orders, venue believes they stopped EC "weeks ago" | Operational disconnect → Silence → Active brand damage | Paused until end of month but venue is operationally gone. Confirm actual status with owner. |
| **Thien Nga Richmond** | Unknown | HubSpot: Owner says platform is "cheap," requesting AM call to discuss pausing | Value perception → Churn consideration | Owner is still open to conversation — this is saveable if AM acts within 48 hours. |
| **Dishoom** | Unknown | HubSpot: Owner (Raj) sent explicit opt-out message | Intent to leave — single event, no prior signal visible | Immediate AM outreach required. |

### 👀 WATCH — Incomplete signal, needs follow-up

| Venue | Signals | Note |
|---|---|---|
| The Cheeky Beans | Cancellation request from Feb ignored by BDM; saved this week | Underlying dissatisfaction unresolved. BDM handover failure pattern. |
| Oh! Dumplings | Immediate cancellation, cost concerns, all deals self-disabled | Active churn. Retention attempt status unknown. |
| Mr Chu Contemporary | Cancellation requested, no supporting detail | Need to understand the reason before this can be themed. |
| Sekka Dining | Pause or cancel during restaurant changes | Conditional — will cancel if pause unavailable. |

---

## 💡 Synthesis Notes

### What surprised me

**The Sam Benjamin governance issue is louder than it looks.** Two separate sources (Adam Glegg and Allen Luo) independently flagged that Sam is building and deploying external-facing tools — a rebuilt signup form, AM tools, direct API access — without product involvement. This isn't just a process complaint. It means the friction in AM tooling is so acute that the Global Head of Sales is building around the system rather than through it. Product should treat Sam's builds as the highest-fidelity signal of what AMs actually need — then bring them into the roadmap properly before governance becomes a crisis.

**40% early churn is the number that should change everything.** If four out of ten churning venues leave within 60 days, the single highest-leverage intervention for OKR 3 isn't in retention — it's in sign quality and onboarding. Sam's deal-locking proposal (lock for 2 weeks, AM calls at unlock as first optimisation) is an elegant near-term fix that also creates a structured handover touchpoint. This deserves fast prototyping.

**Churn documentation is alarmingly poor.** 43% of historical churns have zero or near-zero notes. We can't learn from churn we don't document. This is itself a product opportunity — structured churn exit forms in Hub or Partner Portal that force specific fields (reason category, venue contact, retention attempts, financial context).

### What is missing

- **Slack signals** were not received in structured form. These cover 8 channels including churn, debt, incidents — critical for cross-referencing.
- **Deal Score data** was not provided. Deal score = 0 is defined as a critical churn signal. Without this, I can't identify venues with no active deals.
- **Mixpanel data** is unavailable (no credentials). Partner Portal engagement is a rising theme but I have zero quantitative data on logins, deal edits, or page views.
- **restIDs for this week's HubSpot venues** are missing. Without restIDs, I cannot cross-reference these venues against churn history, deal scores, or Mixpanel.
- **Venue financials** — none of the live signals include venue revenue or deal volume data that would allow sizing the economic impact.

### Interview questions to sharpen weakest signals

| Theme | Question | Target |
|---|---|---|
| Partner Portal engagement | "Walk me through the last time you logged into Partner Portal. What were you trying to do, and did you finish?" | 3–5 venues that recently changed deal settings |
| Deal score trust | "When you see your deal score, what action does that number make you take? If it went to zero, what would you do?" | Venues in Band 3–4 |
| Offerless dining | "Tell me about the last time a customer arrived expecting a deal you didn't recognise. What happened?" | Kate Hunt's venue + 2–3 others flagged for deal integrity |
| BDM handover | "Think back to when you first started with EatClub. At what point did you feel like you understood how to use the platform?" | Venues signed in last 60 days |
| AM value | "If your Account Manager disappeared tomorrow, what would you not be able to do?" | Venues with high AM contact frequency |

### What would move OKR 1 or OKR 2 most based on this week's signals

**OKR 1 (AM Optimisation):** The single highest-leverage move is making deal configuration self-serve in Partner Portal. Sam quantified it: 10 deals = 1 hour of AM time × 50 AMs globally. If even 30% of deal changes shift to venue self-serve, that's the 10 hours/month target for a large segment of the portfolio. Audit the top 5 AM tasks by time, build self-serve for the top 2, and watch AM capacity unlock.

**OKR 2 (Deal Performance):** Meal-period deal structuring. Sam's insight that venues think in service windows (12–2 lunch, 2–3 shoulder, 3–5 afternoon) rather than flat daily windows is the most actionable signal this week. A deal builder that lets venues set discount by meal period would simultaneously improve deal quality (right discount at the right time), increase venue engagement (they configure what makes sense to them), and reduce AM workload (venues own their own structure). This is a three-OKR signal.

---

## Routing Block