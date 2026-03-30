# Synthesis Log — 2026-03-28

**Period covered**: 2026-03-26 → 2026-03-28
**Run type**: Scheduled (Cowork)
**Agent version**: COWORK_AGENT.md
**Additional input**: AM team call transcript (Sam Benjamin recording, Mar 25, 1h51m via Gong)

---

## Signal volume

| Source | Signals pulled | Notes |
|---|---|---|
| Slack #customer-feedback | 0 | Channel had no messages in period |
| Slack #am-team | 0 | Channel had no messages in period |
| Slack #urgent | 50+ | Dominated by ECPay Alerts (deal edits/deletes) + CS agent routing. Key human signals: venue pauses, billing concerns, tablet issues, POS integration, menu update failures |
| Slack #cs-am | 0 | Channel had no messages in period |
| Slack (Sam Benjamin) | 0 | No Slack messages from Sam in period |
| Slack (other/DMs) | 2 | Oke's churn risk on Milk London; Martin's data analysis proposal to Adam |
| HubSpot (churn + notes) | 1 | 1 closed-lost deal (Bar Zero — old record). Thin signal set. |
| Granola (meetings) | 6 meetings | Rich signal: AM pain points, sprint performance, production support, workflow inefficiencies, group onboarding, deal score anomalies |
| Atlassian (SD tickets) | 4 | SD-697 menu bug, SD-696 referral link, SD-695 card setup, SD-694 free trial |
| AM call transcript (uploaded) | 1 recording | EXTREMELY rich — 1h51m candid AM team call with Sam Benjamin. ~30 distinct signals. Strongest signal source this period. |
| **Total** | **~65** | Heavily weighted toward AM transcript + Granola. Slack #urgent high volume but mostly operational noise. |

---

## Themes identified

| Theme | Heat score | OST branch | Mom Test quality | Status |
|---|---|---|---|---|
| Deal Score Trust & Transparency | 11/12 | AM efficiency | Mostly STRONG | New — POST-RELEASE FEEDBACK |
| BDM Signing Quality & Venue Setup | 10/12 | Onboarding | Mostly STRONG | New — **DELIVERY GAP** |
| Support & Tech Response Time | 9/12 | Core friction + AM efficiency | Mostly STRONG | New |
| Venue Deal Control & Self-Service | 8/12 | Core venue friction | Mixed | New — chronic |
| Settlement & Payment Failures | 8/12 | Core venue friction | Mostly STRONG | New — partially in discovery (IDEA-291) |
| Commission & Dispute Process | 8/12 | AM efficiency | Mostly STRONG | New — **DELIVERY GAP** |
| Group Account Management | 6/12 | Enterprise/Groups | Mixed | New — in discovery (IDEA-329) |

---

## Friction stack alerts

| Venue / AM / Segment | Sources appearing in | Risk level | Action taken |
|---|---|---|---|
| Milk London (UK) | Slack #urgent (disabling offers) + Slack thread (AM flagged churn risk) | Medium | AM Oke negotiated stay — reduced tables, strategic times. Monitor. |
| **Segment: Venues signed at 35% unlimited** | AM transcript (Jay, Tom, Elliot) + Slack #urgent (multiple downgrades) + Granola (poor BDM signings) | **High** | System-level friction stack: BDM signing → week 6-7 settlement shock → deal downgrades → AM penalised → AM disengages → venue churns. Created problem card. |

*Note: No single venue appeared across 2+ named sources with enough specificity this period. The segment-level friction stack above is the critical finding.*

---

## Repo changes

**Cards updated**:
- None (first run — all cards are new)

**Cards created**:
- /opportunities/PROBLEM-deal-score-trust.md — AMs can't trust deal score, spend hours tracking manually
- /opportunities/PROBLEM-bdm-signing-quality.md — Venues signed with unsustainable deals, non-ICP, missing onboarding
- /opportunities/PROBLEM-support-response-time.md — Weeks-long waits for basic venue support requests
- /opportunities/PROBLEM-venue-deal-control.md — High volume of manual deal change requests
- /opportunities/PROBLEM-settlement-payment-failures.md — Failed settlements undetected, debt accumulates
- /opportunities/PROBLEM-commission-dispute-process.md — AM commission verification broken, disputes expire

**IDEA tickets raised**: None (per agent rules — Adam decides)

**OST updated**: Yes — all branches updated with heat scores, cards linked, sub-opportunities added

---

## Signal quality assessment

**Strongest signals this period** (STRONG Mom Test quality):
- AM call transcript: Jay's 730-point loss, Tom's nightly tracking, Nicole's 6.5K/month venues penalised, Elliot's "losing sleep" — all reference specific past behaviours with concrete numbers
- Granola: $10k+ weekly debt from 8-9 unnoticed payment failures — specific $ amounts
- Slack: Wok & Wild "not done after multiple attempts" — specific venue, repeated failure

**Weakest signals this period** (flagged for interview follow-up):
- HubSpot was very thin — only 1 old closed-lost deal. Either HubSpot isn't being used for churn logging, or the MCP connection is limited.
- Slack #customer-feedback, #am-team, #cs-am all returned zero messages — these channels may be inactive, renamed, or restricted.

**Interview questions to add to next AM/venue session**:
1. "Walk me through what happens in the first 6 weeks after a venue goes live. When do you first see signs that things aren't right?" (Validates week 6-7 pattern)
2. "When a venue needs something fixed — a terminal excluded, a refund processed — what's the fastest it's ever been resolved? What's the slowest?" (Calibrates support SLA)
3. "If deal score was perfectly accurate and live, would you still feel negatively about it? What would need to change about the metric itself?" (Separates accuracy from fairness)

---

## Coverage gaps

What couldn't be answered from this period's signals:
- Venue-side sentiment: Almost all signals are AM-perspective. No direct venue voice this period (no #customer-feedback messages, no HubSpot venue notes). Need venue interviews.
- Scale quantification: We know the problems exist but don't know what % of venues are affected by each. Mixpanel data analysis needed.
- BDM perspective: Strong AM testimony about BDM practices, but no BDM voice. Risk of one-sided framing.

What sources were thin or missing:
- **HubSpot**: Essentially no useful signals. Is close-lost reason being logged? Are AM notes being captured?
- **Slack #customer-feedback, #am-team, #cs-am**: Zero messages. Channels may be dead, renamed, or access-restricted. Investigate.
- **Sam Benjamin**: No Slack messages found despite being flagged as a frequent signal source. May post in private channels.

---

## Open questions

Things the synthesis raised that need human judgment from Adam:

- **Deal score post-release feedback**: REST-229, REST-235, REST-236, REST-213, REST-228 all shipped recently with deal score logic changes. The AM transcript suggests the fundamental trust and incentive problems persist. Is the recently shipped work expected to address the specific issues AMs raised (churn save penalty, transparency, changelog)? Or are these still gaps?

- **BDM signing quality — who owns this?** This is the biggest delivery gap: Heat 10/12 with zero Jira or Confluence coverage. Is this a Product problem, a Sales Ops problem, or both? Does the Q2 OKR "Scale AM Optimisation" include upstream signing quality, or only downstream AM workflow?

- **AM transcript — how to use it**: This recording is extraordinary signal. Should it be shared (anonymised) with Mark/Alan? Should it inform the Q2 planning directly? Is there a risk that AMs feel surveilled rather than heard?

- **Slack channel gaps**: Are #customer-feedback, #am-team, #cs-am active channels? Should the agent search different channels next run?

- **Martin's data analysis proposal**: Martin shared a detailed Claude analysis of event-stream-based churn prediction. Worth reviewing — could be a meaningful capability uplift if EatClub can provide event stream data. Is this worth exploring with engineering?
