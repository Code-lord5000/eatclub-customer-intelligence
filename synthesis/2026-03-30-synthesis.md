# Synthesis Log — 2026-03-30

**Period covered**: 2026-03-28 → 2026-03-30
**Run type**: Scheduled (Cowork, every 2 days)
**Agent version**: COWORK_AGENT.md

---

## Signal volume

| Source | Signals pulled | Notes |
|---|---|---|
| Slack #customer-feedback | 0 | Channel still inactive — 2nd consecutive zero |
| Slack #am-team | 0 | Channel still inactive — 2nd consecutive zero |
| Slack #urgent | ~40+ | Dominated by ECPay bot alerts. 4 human signals: Alyra Cafe (upset owner, refund + billing), Punch Lane (deal timing change), The Chapter 24 (permanently removing offers), British Patagonia (deleting offer, "offerTooHigh") |
| Slack #cs-am | 0 | Channel still inactive — 2nd consecutive zero |
| Slack #churned_or_changed | 4 | NEW SOURCE discovered this run. Pizza Da Italia (early churn, $260/3wk), Ambra Spirits (explicit churn — "EC devalues offering"), Armadela VNO (closed), Famished Wolf x4 (deal restructure) |
| Slack #ecpayuk-ops | 10+ | UK payment failures: Stage Brasserie, Notes Coffee, Mallow Borough, Firebird Soho, Cu4tro, Kanada-ya. Consumer issues: Rao's Bar (inflated menu for EC users), Saporitalia (fully booked), Bar Jackie (no breakfast) |
| Slack (Sam Benjamin) | 1 | RGA manifesto in #gtm-announcements — strategic signal about AI + internal tool to remove non-RGA work |
| HubSpot (churn + notes) | 1 | 1 closed-lost: Dosa Hut Aspley (old record). Notes: all automated Arrows uploads + 1 Gong note (Alzado x EatClub). HubSpot still producing minimal useful signal. |
| Granola (meetings) | 0 new (Mar 27 data) | No meetings recorded Mar 28–30. Prior Mar 27 data (already captured in W13 run) still resonant: sprint velocity 127/237, Vi solo production, $10k+/wk settlement debt. |
| Jira SD | 7 | SD-699/572/337/165: EC Card setup issues (4 tickets, ALL Blocked Internally). SD-698: Missing confirmation email. SD-694: Free trial not working. SD-645: Boost authorisation (resolved). |
| Confluence | 10 pages checked | No new pages in "Product" space since Mar 28. Rovo search returned existing relevant pages: Deal Score Logic doc, Churned or Changed repo, Venue Feedback Synthesis, Groups PRD. |
| **Total** | **~65** | Weighted toward Slack operational signals + SD tickets. New source: #churned_or_changed provides direct venue churn voice. Granola gap (no meetings in window). |

---

## Delivery context loaded

**Active REST delivery (In Progress / In Review)**: 5 tickets
- REST-188: FE New Venue Support - UK regions (Mitchell Fox)
- REST-21: FE Venue signup VGS integration (Cameron Darragh)
- REST-183: FE PP Grow your database email templates (Mitchell Fox, In Review)
- REST-189: FE New Venue Support - 100km region selector (Mitchell Fox)
- REST-48: Audience Targeting v2 (Epic)

**Open IDEA tickets**: 30 total. Key for signal mapping:
- IDEA-344/348/349: AM Tooling Phase 1–3 (Discovery)
- IDEA-329: Groups Onboarding (Discovery)
- IDEA-291: Net Settlement (Discovery)
- IDEA-356: Portal Self-Serve & POS (Concept)
- IDEA-327: Deal Score Offer setup & Optimisation (Concept)
- IDEA-264: Deal prediction & management (In Design)
- IDEA-353: Automated Refund Workflow (Concept)
- IDEA-352: Payment Reconciliation Dashboard (Concept)
- IDEA-355: Double-Dipping & Multi-Offer Abuse (Concept)
- IDEA-350/351: T&C Enforcement — Pax Size / Dine-In validation (Concept)

**Recently completed REST (last 30 days)**: 20 tickets. Key:
- REST-229: Deal Score Change History rework (Mar 24)
- REST-235: New Business Logic for Deal Score (Mar 25)
- REST-236: Deal Score reignition live date in Hub (Mar 25)
- REST-204: Net Revenue Calculations on Insights page (Mar 27)
- REST-170/231/169: Payments repo 3DS + cryptogram cache (Mar 24-27)
- REST-238: Grow Your Database webhook (Mar 27)
- REST-143: Guest manager visibility logic (Mar 27)

**Delivery context map**:
- BEING BUILT NOW → UK regions support, VGS integration, Audience Targeting v2, Grow Your Database
- IN DISCOVERY → AM Tooling, Groups Onboarding, Net Settlement, Portal Self-Serve
- RECENTLY SHIPPED → Deal Score logic changes, Net Revenue Insights, Payments 3DS
- NO COVERAGE → EC Card reliability (4 blocked SD tickets), BDM signing quality (still zero), venue gaming/T&C enforcement (IDEA exists but Concept only)

---

## Themes identified

| Theme | Heat score | OST branch | Mom Test quality | Status |
|---|---|---|---|---|
| EC Card / Payment Reliability | 9/12 | Core venue friction | Mixed (specific failures + consumer names, but consumer-side) | NEW — **DELIVERY GAP** |
| Venue Deal Control & Self-Service | 8/12 | Core venue friction | Medium | Recurring — chronic, stable |
| BDM Signing Quality (via churn signals) | 7/12 (incremental) | Onboarding quality | Strong (Ambra Spirits explicit churn) | Recurring — still **DELIVERY GAP** |
| AM Efficiency / Non-RGA Work | 7/12 (incremental) | AM efficiency | Medium (Sam's strategic framing) | Recurring — IDEA-344/348/349 in discovery |
| Venue Gaming / T&C Violations | 6/12 | Core venue friction (or new branch) | Strong (specific incident) | NEW — watch |
| Deal Score Trust | — (no new direct signals) | AM efficiency | — | Stable — post-release feedback period continuing |

---

## Framework application notes

### Mom Test filter
- **STRONG**: Ambra Spirits churn reason ("tight margins, EC devalues offering to regulars" — specific past decision with stated rationale), Pizza Da Italia early churn ($260 revenue figure), Alyra Cafe (owner upset about specific billing + misuse issues), Rao's Bar (venue actively giving EC customers different menu + inflated prices)
- **MEDIUM**: Deal change requests (observable behaviour but no stated reason beyond "offerTooHigh"), Sam Benjamin RGA manifesto (strategic framing, not specific past behaviour), Famished Wolf deal restructure
- **WEAK**: HubSpot automated notes (no human signal content)

### Problem statement translations
- Signal: "Rao's Bar gave different menu with inflated prices to EC customers" → **Problem**: Venues can selectively degrade the dining experience for EatClub customers without detection, undermining consumer trust in the platform and generating refund disputes that damage the venue-EatClub relationship
- Signal: "Ambra Spirits — EC devalues offering to regulars" → **Problem**: Venues whose brand and margin position is premium perceive EatClub as diluting their offering to existing customers rather than adding incremental ones — this is an ICP validation problem at sign-up, not an engagement problem
- Signal: "4 SD tickets for EC Card setup blocked" → **Problem**: Customers cannot reliably set up or use the EatClub payment card, creating failed transactions and refund requests that reduce venue transaction volume and erode consumer confidence

### OST branch mapping
All signals mapped to existing branches. Venue gaming (Rao's Bar) could justify a new branch ("Platform integrity / T&C enforcement") but signal volume is too low (1) — flagging for observation.

### Friction stack detection
**No individual venue friction stacks identified this period.**

**Segment-level stack observed**: EC Card setup failures (4 SD tickets) → payment declines at venues (UK ops channel) → refund requests from consumers → reduced venue transaction volume. This is a consumer-side friction stack that eventually impacts venue metrics and AM conversations.

### Heat scoring detail
| Theme | Frequency | Source diversity | Mom Test | Recurrence | Total |
|---|---|---|---|---|---|
| EC Card / Payment Reliability | 3 (9+ signals) | 2 (SD + Slack) | 2 (mixed) | 2 (new but echoes settlement) | **9/12** |
| Venue Deal Control | 2 (3-5 signals) | 1 (Slack only) | 2 (mixed) | 3 (chronic) | **8/12** |
| BDM Signing Quality (incremental) | 1 (2 churn signals) | 1 (#churned_or_changed) | 3 (strong) | 2 (seen before) | **7/12** |
| AM Efficiency (incremental) | 1 (Sam's post) | 1 (Slack) | 2 (medium) | 3 (chronic) | **7/12** |
| Venue Gaming | 1 (1 signal) | 1 (Slack) | 3 (strong) | 1 (new) | **6/12** |

---

## Friction stack alerts

| Venue / AM / Segment | Sources appearing in | Risk level | Action taken |
|---|---|---|---|
| **Segment: EC Card users (consumer-side)** | Jira SD (4 blocked tickets) + Slack #ecpayuk-ops (multiple payment failures) | **Medium** | No venue-level friction stack but consumer payment reliability is systemically impaired. 4 of 7 active SD tickets are card setup issues — all blocked internally. |
| Pizza Da Italia | Slack #churned_or_changed (early churn) | Low | Single source but notable: $260 revenue in 3+ weeks, uncontactable. Classic early churn pattern. |
| Ambra Spirits | Slack #churned_or_changed (explicit churn) | Low | Single source but high-quality signal: explicit "not right fit" — ICP/brand mismatch. |

*No venue appeared across 2+ named sources this period.*

---

## Repo changes

**Cards updated**:
- /opportunities/PROBLEM-venue-deal-control.md — appended 3 new signals from #urgent (Punch Lane, Chapter 24, British Patagonia)
- /opportunities/PROBLEM-bdm-signing-quality.md — appended 2 churn signals (Pizza Da Italia early churn, Ambra Spirits ICP mismatch)
- /opportunities/PROBLEM-support-response-time.md — appended Alyra Cafe signal (upset owner, refund + billing)

**Cards created**:
- /opportunities/PROBLEM-ec-card-payment-reliability.md — NEW: Customers cannot reliably set up or use EC payment card (Heat 9/12)

**IDEA tickets raised**: None (per agent rules — Adam decides)

**OST updated**: Yes — all branches updated with this period's heat, new card linked

---

## Signal quality assessment

**Strongest signals this period** (STRONG Mom Test):
- Ambra Spirits: explicit churn reason with specific business rationale — "tight margins, increasing costs, EC devalues offering to regulars"
- Rao's Bar: venue actively providing different menu with inflated prices to EatClub customers — specific observable gaming behaviour
- Pizza Da Italia: $260 revenue in 3+ weeks, uncontactable — concrete early churn with specific numbers
- Alyra Cafe: owner upset about refund, customers misusing offers, billing confusion — multi-faceted venue frustration

**Weakest signals this period**:
- HubSpot: Still producing zero useful AM/venue notes. 3rd run with minimal HubSpot signal. Either AM notes aren't being logged, or the MCP connection doesn't surface them. **This is a persistent coverage gap.**
- Granola: No meetings in the 48-hour window (weekend/end of week). Gap is expected but means we lost 2 days of meeting intelligence.
- Slack #customer-feedback, #am-team, #cs-am: 3rd consecutive zero. These channels appear to be inactive or restricted.

**New source discovered**: #churned_or_changed — this channel contains direct churn actions with explicit venue reasons. **Extremely valuable.** Should be added to the standard search list permanently.

---

## Coverage gaps

**What couldn't be answered from this period's signals:**
- Direct venue voice on EC Card issues — all signals are consumer-side (SD tickets) or operational (UK ops). No venue perspective on how failed consumer payments affect their experience.
- Whether Sam's internal AI/RGA tool overlaps with IDEA-344/348/349 AM Tooling — the manifesto implies a separate build. Adam needs to clarify scope boundaries.
- Scale of UK payment failures — volume is visible but conversion impact is not. Mixpanel data needed.

**Persistent thin sources:**
- **HubSpot**: 3rd run with no useful AM notes. Investigate: are AMs logging notes elsewhere? Is there a different HubSpot object type to query?
- **Slack #customer-feedback, #am-team, #cs-am**: All confirmed inactive for 3 consecutive periods. Recommend removing from standard search and replacing with: #churned_or_changed, #ecpayuk-ops, #gtm-announcements.
- **Granola**: Gap is timing-dependent (no meetings on weekends). Not a structural issue.

---

## Open questions for Adam

1. **Sam's internal AI/RGA tool**: Sam announced in #gtm-announcements that an internal tool is "being built specifically for how we sell, how we prospect, how we follow up, and how we manage venues." Is this the same as IDEA-344/348/349 (AM Tooling)? Or a parallel Sales Ops build? If parallel, how do we ensure they complement rather than conflict?

2. **EC Card reliability — who owns this?**: 4 of 7 active SD tickets are card setup issues, all Blocked Internally. This is a consumer-side problem but it directly impacts venue transaction volume. Is this a Product problem, a Payments team problem, or VGS integration (REST-21 in progress)?

3. **Ambra Spirits churn pattern — "EC devalues offering"**: This is a fundamentally different churn reason from the usual margin/settlement complaints. It's a brand/positioning objection. Does this signal a need for ICP criteria at sign-up (BDM quality card) or a need for a different product positioning (EatClub Black / premium tier per IDEA-162)?

4. **Channel search list update**: #customer-feedback, #am-team, #cs-am have been zero for 3 runs. I found #churned_or_changed this run — it's gold. Should I replace the inactive channels with: #churned_or_changed, #ecpayuk-ops, #gtm-announcements, #churn-appt-req?

5. **Rao's Bar — venue gaming**: A customer reported Rao's Bar gave them "a menu with vastly different items and inflated prices." IDEA-350/351 exist for T&C enforcement but are in Concept. Is this pattern worth escalating, or is it an isolated incident?
