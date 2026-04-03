# PROBLEM: Bookings product launching without adequate venue/AM readiness

## Problem statement
The bookings product is launching to market before the restaurant-side experience has been designed, before AMs have been formally trained, and before critical integrations (SMS billing, settlement) are complete — creating risk of poor venue first-impressions, AM overwhelm, and customer experience failures.

## OST branch
**Onboarding quality** (primary) / **AM efficiency** (secondary)

## Current status
🔴 CRITICAL — **LAUNCHED TODAY (April 1, 2026)** with known gaps. Settlement integration incomplete, no AM training, no restaurant flow designed. UK cities also launching simultaneously. Monitor post-launch signals urgently.

## Heat tracker

| Period | Frequency | Sources | Mom Test | Recurrence | Total |
|---|---|---|---|---|---|
| W15 (Apr 1) | 3pt (6+ signals) | 2pt (Granola + inferred) | 3pt (STRONG) | 2pt (seen before) | **9/12** ⬆️ |
| W14b (Mar 31) | 2pt (3-5 signals) | 1pt (Granola only) | 3pt (STRONG) | 1pt (NEW) | **7/12** |

## Signal log

| Date | Source | Signal | Mom Test | Author |
|---|---|---|---|---|
| 2026-04-01 | Granola | **LAUNCHED TODAY** — Easy Bookings live with settlement integration still incomplete. SMS costs (~10¢/message) lack billing flow. | STRONG | Meeting notes |
| 2026-04-01 | Granola | UK cities (Leeds, Cardiff, Liverpool) launching simultaneously — incomplete processes, no regression testing checklist. | STRONG | Meeting notes |
| 2026-04-01 | Granola | No dedicated PM for bookings (just Simone). Product team not involved in discovery. | STRONG | Meeting notes |
| 2026-04-01 | Granola | Comparison to OpenTable problematic — significant feature gaps acknowledged. | MEDIUM | Meeting notes |
| 2026-04-01 | Granola | Enablement session with Ella, Emma, Darcy, Luke, Sophie needed but not yet scheduled. | STRONG | Meeting notes |
| 2026-03-31 | Granola | Bookings launching with no restaurant flow or design work completed. Built as "black box" with day-before notice. | STRONG | Meeting notes |
| 2026-03-31 | Granola | AMs have 30/month booking targets but no formal training completed. | STRONG | Meeting notes |
| 2026-03-31 | Granola | Settlement integration incomplete for bookings — SMS billing flow missing (~10¢/message). Similar complexity to previous credit rebate issues. | STRONG | Meeting notes |
| 2026-03-31 | Granola | "Product team receiving fully-formed solutions rather than discovering root problems" | MEDIUM | Meeting notes |

## Who is affected
- **Venue owners**: Will be onboarded to bookings without adequate product experience design
- **AMs**: Expected to sell 30/month with no training or materials
- **Customers**: May encounter incomplete booking flow
- **Product team**: Exposure to post-launch firefighting

## Workarounds described
None — launch has not happened yet.

## Friction stack connections
- If bookings fail for a venue AND they already have deal/T&C friction → accelerated churn risk
- Settlement integration gap connects to PROBLEM-settlement-payment-failures.md

## Delivery status
REST-71/66/70/68 (Obee integration) In Progress — backend being built, but no restaurant-side product flow designed.

## Assumptions to test
1. Do AMs understand the bookings product well enough to sell it effectively?
2. Is the venue onboarding flow for bookings intuitive enough for self-serve?
3. What happens when SMS billing events occur before the billing flow is built?

## Discovery status
No separate discovery — this emerged from delivery-side Granola meetings. Needs product attention.
