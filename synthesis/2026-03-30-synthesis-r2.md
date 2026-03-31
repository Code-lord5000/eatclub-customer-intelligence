# Synthesis Log — 2026-03-30 (Run 2)

**Period covered**: 2026-03-30 (48h window — same calendar day as run 1 but new signals surfaced throughout the day)
**Run type**: Scheduled (Cowork, every 2 days)
**Agent version**: COWORK_AGENT.md

---

## Signal volume

| Source | Signals pulled | Notes |
|---|---|---|
| Slack #customer-feedback | 0 | 4th consecutive zero — confirmed inactive |
| Slack #am-team | 0 | 4th consecutive zero — confirmed inactive |
| Slack #urgent | ~30+ | ECPay bot alerts continue. Human signals: Barrel N Basket (reduce to 20%), Chicken Bandits (reduce to 10% "low profit"), Eat Thai Paddington (disabled, no transactions), Lilong (time change), Polly Bar (offers removed), Pizzeria 1760 (closed Apr 3-5) |
| Slack #cs-am | 0 | 4th consecutive zero — confirmed inactive |
| Slack #churned_or_changed | 12 | EXTREMELY RICH: 4 explicit churns with reasons (Little B, Little Rice Bowl, That Viet Place, Gami), 2 T&C friction signals (Hayashi, Como Garden), 1 deal restructure (Famished Wolf settled), 2 venue closures (Old Quarter sold, Armadela closed), seating time change (Maya Lounge), process gap (Emma asks about seating time guidelines), admin limitation (Kane: can't do RCI) |
| Slack #ecpayuk-ops | 15+ | UK payment failures: Homeboy Bar (H M, 2x FAILED AUTH + refund), AperiPasta (William, FAILED AUTH), Tacacho (Gabriel, FAILED AUTH). Missed refund flagged by Jeroen. Dialpad call summaries + text messages. Venue info accuracy issue (Noisy Oyster hours wrong). |
| Slack (Sam Benjamin) | 0 | No messages this period |
| HubSpot (churn + notes) | 3 closed-lost | All old records (Hut & Soul, Nomad, Dosa Hut). HubSpot continues to produce zero useful new signal — 4th consecutive run. |
| Granola (meetings) | 1 | **HIGH VALUE**: Onboarding Process Analysis meeting (Mar 30, 4:15 AM). Mapped entire post-contract onboarding bottleneck: photo quality, manual menu digitization (9 Manila staff), go-live preferences friction, manual verification, group signup form needs redesign. |
| Jira SD | 13 | NEW: SD-703 (RIA during HDS — bug), SD-702 (password reset error), SD-701 (Sushi E popup — Merivale ASAP), SD-700 (venue/AM CAN'T edit offers — broken self-serve). STILL BLOCKED: SD-699/572/337/165 (EC Card setup x4). |
| Confluence | 10 pages checked | No new pages since last run. Existing: Churned or Changed repo, Venue Feedback Synthesis, Deal Management Analysis, Onboarding Journey Iteration 1. |
| **Total** | **~75** | UP from ~65. Richer #churned_or_changed channel + Granola meeting. HubSpot remains dead. |

---

## Delivery context loaded

**Active REST delivery (In Progress / In Review)**: 11 tickets
- REST-243: Customer.io Survey Delivery (In Review, Mitchell Fox) — NEW
- REST-244: Customer.io Interview CTA (In Progress, Mitchell Fox) — NEW
- REST-66/70/68: Obee API Integration (In Progress, Martin Heal) — NEW
- REST-207: Verified email endpoint (In Progress, vaishali.mangwani) — NEW
- REST-225: Currency icon in PP (In Review, Martin Heal)
- REST-21: FE Venue signup VGS integration (In Progress, Cameron Darragh)
- REST-183: FE PP Grow Your Database email templates (In Review, Mitchell Fox)
- REST-189: FE New Venue Support 100km region selector (In Progress, Mitchell Fox)
- REST-48: Audience Targeting v2 (In Progress)

**New completions since last run**:
- REST-242: Customer.io SDK installed (Mar 30)
- REST-206: Email verification endpoint (Mar 30)
- REST-188: New UK regions website support (Mar 30)
- REST-246: Correct boost type in Hub (Mar 29)

**Open IDEA tickets**: 30 total (no change from last run). Key for signal mapping:
- IDEA-344/348/349: AM Tooling Phase 1–3 (Discovery)
- IDEA-356: Portal Self-Serve & POS (Concept) — SD-700 validates urgency
- IDEA-350/351: T&C Enforcement (Concept) — new T&C friction card adds different dimension
- IDEA-353: Automated Refund Workflow (Concept) — missed refund in UK validates need

**Delivery context map**:
- BEING BUILT NOW → Customer.io surveys, Obee integration, VGS integration, Grow Your Database, UK regions
- IN DISCOVERY → AM Tooling, Groups Onboarding, Net Settlement, Portal Self-Serve
- RECENTLY SHIPPED → Customer.io SDK, email verification, UK regions website, correct boost type in Hub
- NO COVERAGE → BDM signing quality / onboarding process (STILL zero Jira), T&C friction/venue trust (new, IDEA-350/351 exist but address enforcement, not venue experience of enforcement)

---

## Themes identified

| Theme | Heat score | OST branch | Mom Test quality | Status |
|---|---|---|---|---|
| BDM Signing Quality & Onboarding | 12/12 | Onboarding quality | STRONG (3 explicit churns + Granola meeting) | Recurring — **DELIVERY GAP** — ⬆️ UP from 10 |
| Venue Deal Control & Self-Service | 10/12 | Core venue friction | STRONG (SD-700 broken self-serve) | Recurring — ⬆️ UP from 8 — ESCALATING |
| EC Card / Payment Reliability | 9/12 | Core venue friction | Mixed | Recurring — stable, 4 SD tickets still blocked |
| Support & Tech Response Time | 9/12 | Core venue friction | STRONG (SD-700 + missed refund) | Recurring — stable |
| T&C Friction & Venue Trust | 7/12 | Core venue friction | STRONG (Hayashi + Como Garden) | **NEW CARD CREATED** |
| AM Efficiency / Non-RGA Work | 7/12 | AM efficiency | — (no new signals) | Stable — no Sam Benjamin activity |

---

## Framework application notes

### Mom Test filter
- **STRONG**: Little B by Bruno&Co ("regulars using deal for coffee only, AOV $15, EC doesn't fit"), That Viet Place (failed churn save after AM+Sam intervention, "poor ICP not worth keeping"), Hayashi + Como Garden ("magnifying glass to every T&C breach", high-performing, extreme churn risk — commercial concession made), The Maya Lounge ("very upset customers redeem too late during peak"), SD-700 (venue AND AM both unable to edit offers — specific technical failure), Eat Thai Paddington (disabled due to no transactions), H M at Homeboy Bar (card failed, refund requested, "I had enough money")
- **MEDIUM**: Barrel N Basket (reduce to 20% ASAP), Chicken Bandits (10% low profit), Granola onboarding meeting (institutional discussion, not direct venue voice but maps specific bottlenecks), Bema Burgers (ghost kitchen replacement)
- **WEAK**: Gami Chicken & Beer churn (no reason), ECPay bot alerts (system-generated), HubSpot closed-lost (old records)

### Problem statement translations
- "Hayashi takes magnifying glass to every T&C breach, at extreme churn risk" → **Problem**: Venues that successfully drive revenue through EatClub are still at risk of leaving because the cumulative management burden of T&C enforcement — even when individual incidents are minor — makes the partnership feel adversarial and the revenue not worth the overhead
- "SD-700: Venue can't edit offers, AM can't either" → **Problem**: The self-serve offer management tools in Partner Portal have technical failures that block both venues AND AMs from basic operations, eliminating any workaround and creating complete dependency on backend intervention
- "9 Manila staff manually digitize menus from PDFs" → **Problem**: The pipeline between contract signing and first-deal-live requires extensive manual labor (menu scanning, photo verification, address checking) that creates quality inconsistencies, delays go-live, and makes the team a bottleneck rather than an accelerator
- "Chicken Bandits wants 10% because low profit" → **Problem**: Venues with thin margins can't sustain even moderate discount percentages, and when they discover this post-signing, their only recourse is requesting CS intervention to reduce deals to survival levels

### OST branch mapping
All signals mapped to existing branches. T&C friction is within Branch 1 (Core venue friction) but is a distinct problem from venue gaming — it's the venue's EXPERIENCE of enforcement, not venues violating rules.

### Friction stack detection
**No individual venue appeared across 2+ named sources this period.**

**Segment-level stacks**:
1. **Post-signing ICP failure cascade**: BDM signs wrong venue type → venue gets low traction → AM attempts churn save → save fails → churn. That Viet Place is the complete arc (signed → churn saved by AM + Sam → continued disabling deals → churned anyway). This is the clearest friction stack this run.
2. **EC Card → disabled venue**: Eat Thai Paddington had no successful transactions → was disabled. If this is card-related, it connects to the 4 blocked SD tickets.

### Heat scoring detail
| Theme | Frequency | Source diversity | Mom Test | Recurrence | Total |
|---|---|---|---|---|---|
| BDM Signing Quality | 3 (7 signals) | 2 (Slack, Granola) | 3 (strong) | 3 (chronic) | **12/12** |
| Venue Deal Control | 3 (11 signals) | 3 (Slack #urgent, #churned_or_changed, Jira SD) | 2 (mixed) | 3 (chronic) | **10/12** |
| EC Card Reliability | 2 (7 signals) | 2 (SD, Slack) | 2 (mixed) | 2 (seen before) | **9/12** |
| Support Response Time | 2 (4 signals) | 2 (Jira SD, Slack) | 3 (strong) | 3 (chronic) | **9/12** |
| T&C Friction | 2 (4 signals) | 1 (Slack) | 3 (strong) | 1 (new) | **7/12** |

---

## Friction stack alerts

| Venue / AM / Segment | Sources appearing in | Risk level | Action taken |
|---|---|---|---|
| **That Viet Place (FRICTION STACK)** | Slack #churned_or_changed (failed churn save) | **High** | Complete arc: signed → churn saved by AM + Sam → continued disabling → churned. AM says "poor ICP." This is the friction stack model in action. |
| **Hayashi + Como Garden (group)** | Slack #churned_or_changed (T&C friction, rebate) | **High** | High-performing group at extreme churn risk despite revenue. Rebate offered = commercial escalation. |
| **Segment: EC Card (consumer-side)** | Jira SD (4 blocked) + Slack #ecpayuk-ops + Slack #urgent (Eat Thai disabled) | **Medium** | Unchanged from last run — 4 SD tickets still blocked. Eat Thai disabled adds venue-impact dimension. |

---

## Repo changes

**Cards updated**:
- /opportunities/PROBLEM-venue-deal-control.md — 11 new signals, heat UP to 10/12. SD-700 (broken self-serve) is strongest signal.
- /opportunities/PROBLEM-bdm-signing-quality.md — 7 new signals including Granola meeting. Heat UP to 12/12 (CRITICAL).
- /opportunities/PROBLEM-ec-card-payment-reliability.md — 7 new signals (UK failures, Eat Thai disabled, missed refund). Heat stable 9/12.
- /opportunities/PROBLEM-support-response-time.md — 4 new signals (SD-700, SD-703, missed refund, Merivale ASAP). Heat stable 9/12.

**Cards created**:
- /opportunities/PROBLEM-tc-friction-venue-trust.md — NEW: High-performing venues at churn risk from T&C enforcement friction (Heat 7/12)

**IDEA tickets raised**: None (per agent rules — Adam decides)

**OST updated**: Yes — all branches updated. Branch 1 at 36/12 combined. Branch 2 at 12/12. New card linked.

---

## Signal quality assessment

**Strongest signals this period (STRONG Mom Test)**:
1. **That Viet Place** — FAILED CHURN SAVE. Was saved by AM + Sam, still churned. "Poor ICP not worth keeping TA only." The complete friction-to-churn arc.
2. **Hayashi + Como Garden** — High-performing venues at extreme churn risk from T&C friction. 2% rebate = commercial concession to manage relationship. Group signal = replicable pattern.
3. **Little B by Bruno&Co** — "Regulars using deal for coffee only, AOV $15." Specific business reason for churn.
4. **SD-700** — Venue AND AM both unable to edit offers. Self-serve is broken, not just limited. No workaround.
5. **Granola onboarding meeting** — Mapped full post-contract bottleneck: 9 Manila staff for menus, photo quality, verification, go-live friction.
6. **Eat Thai Paddington** — Disabled because no transactions. Payment reliability directly impacted venue availability.

**Weakest signals this period**:
- **HubSpot**: 4th consecutive run with zero useful signal. The 3 closed-lost deals are years-old records. **This source should be investigated or dropped.**
- **Sam Benjamin**: No messages in the period. Previous run's RGA manifesto was the last signal.
- **Slack #customer-feedback, #am-team, #cs-am**: 4th consecutive zero. **Recommend formally removing from search list.**

---

## Coverage gaps

**What couldn't be answered from this period's signals:**
1. **Scale of T&C friction churn risk**: Hayashi + Como Garden are a group — how many other high-performing venues have similar T&C frustration? Needs Mixpanel analysis: churn rate segmented by revenue band.
2. **Why Eat Thai Paddington had zero transactions**: Is this a card/payment issue, a venue setup issue, or a demand issue? The signal is ambiguous.
3. **Onboarding bottleneck impact on time-to-first-deal**: Granola meeting describes the process but not the outcome metrics. How many days between signing and first live deal? What's the drop-off?
4. **Whether Customer.io surveys (REST-243) will generate venue feedback signals**: This could fill the #customer-feedback gap if deployed.

**Persistent thin sources:**
- **HubSpot**: 4 runs, zero signal. Structural issue with how AMs use HubSpot or what the MCP surfaces.
- **Slack #customer-feedback, #am-team, #cs-am**: Confirmed inactive for 4 periods. Replace with: #churned_or_changed, #ecpayuk-ops, #gtm-announcements.

---

## Open questions for Adam

1. **BDM Signing Quality is now at 12/12 heat with ZERO Jira coverage.** That Viet Place is a failed churn save — AM + Sam both intervened and it still churned. The Granola meeting mapped the full post-contract bottleneck. Is it time to raise an IDEA ticket? This is the highest-heat delivery gap in the repo.

2. **T&C Friction — a new problem dimension.** Hayashi and Como Garden are high-performing venues getting rebates because T&C friction is eroding the relationship. This is different from venue gaming (Rao's Bar) — these venues aren't violating T&Cs, they're frustrated by enforcement. IDEA-350/351 address detection, not the venue experience. Worth separate discovery?

3. **SD-700 — self-serve is broken.** Petit Bistro can't edit offers. AM Elliot can't either. New offer creation also failed. This isn't "self-serve is limited" — it's "self-serve doesn't work." Is this a known bug or new? Does it connect to IDEA-356 (Portal Self-Serve)?

4. **HubSpot as a signal source — drop it?** 4 runs, zero useful signal. Either AMs aren't logging notes in HubSpot, or the MCP connection doesn't surface them. Should I stop searching HubSpot and reallocate time to richer sources?

5. **Channel search list**: Formally replace #customer-feedback, #am-team, #cs-am (all 4 runs zero) with #churned_or_changed, #ecpayuk-ops, #gtm-announcements?
