# Final Project Review: CampusLoop

*Reviewed: `01-research.md`, `02-strategy.md`, `03-copywriting.md`, `04-prototype/index.html` (current version, after the developer's fix pass) and `05-qa-report.md` (which describes the page before that fix pass). November 2026.*

## Executive Summary

The team turned a broad brief ("reusable cups for German campuses") into a focused B2B/B2G proposition: **CampusLoop**, a white-label cup deposit system for Studierendenwerke that books the deposit on the student card, charges per cup instead of a monthly fee, and links campuses through shared return and clearing. The chain from research to page is unusually disciplined. The research is well sourced and honest about its gaps, the strategy builds only on those findings and marks unknowns as "insufficient information", the copy keeps those caveats, and the prototype reproduces the copy faithfully. QA found no blocking issues, and the fix pass resolved the two misleading claims (a real-city example that read like a live network, and an unsupported speed claim) plus most of the quick fixes. **Verdict: a credible, honest demo and a sound basis for customer discovery, but not yet a validated business.** The weak points are upstream, not on the page: the core differentiator (cross-campus return) is the least evidenced claim, the first pilot target conflicts with the team's own research, the roadmap timeline does not reach the PPWR deadline it is built around, and there is no cost model behind "low per-cup fee".

## Deliverables Overview

| Stage | Output | Status |
|---|---|---|
| 1. Research | `01-research.md`: regulation (VerpackG, PPWR, packaging taxes), competitors (RECUP, Vytal, Relevo, in-house systems), buyer and user profiles, barriers and opportunities, ~15 sources | ✅ Complete. Strong sourcing, gaps clearly flagged (no campus return-rate data, PPWR dates unverified, procurement cycle is an estimate) |
| 2. Strategy | `02-strategy.md`: positioning, segments, differentiation table, 4-phase GTM, channels, risks | ✅ Complete. Consistent with research; one target-choice conflict and one timeline error (see below) |
| 3. Copywriting | `03-copywriting.md`: slogan, hero, 5 benefits, CTAs, student line, 8 pitch-deck points | ⚠️ Complete, but now **out of sync** with the fixed page: it still contains "no queue at the till", the Tübingen/Konstanz present-tense example and "what nobody has published yet" |
| 4. Prototype | `04-prototype/index.html`: single-page landing page, inline CSS/SVG, responsive | ✅ Complete after one fix pass. Matches copy apart from the deliberate corrections; demo status disclosed |
| 5. QA | `05-qa-report.md`: 0 🔴, 8 🟡 groups, detailed 🟢 list | ✅ Complete, source review only (no browser or device test). Describes the pre-fix page |

**Status of the QA 🟡 items in the current page:**

| QA item | Current state |
|---|---|
| 1. Secondary CTA missing | ✅ Fixed: "Download the brief" added, with an honest demo hint |
| 2. Pilot CTA does nothing | ⚠️ Still only scrolls to `#pilot-metrics`; acceptable for a demo because the hint says so |
| 3. Tübingen/Konstanz reads as live network | ✅ Fixed: now "Campus A / Campus B, once both take part", in the conditional |
| 4. "No queue at the till" unsupported | ✅ Fixed: heading is now "No app, no cash, just the student card." |
| 5. "Nobody has published yet" overstated | ✅ Fixed: "what we found no public data on for campuses" |
| 6. "Coffee for less" depends on a discount | ✅ Fixed with a qualifier (wording is clumsy, see below) |
| 7. Navigation hidden on mobile | ✅ Fixed: the "Pilot" link stays visible |
| 8. Polish (`id="top"`, meta description, thin nudge section) | ✅ / ✅ / ⚠️ First two fixed; the nudge section is still a sparse two-column block |

## Strengths

1. **Evidence discipline across all five stages.** Each stage states its only input and marks what it does not know. Research separates sourced figures from estimates; strategy carries "insufficient information" into the price, card integration and PPWR reporting; the copy and page turn those into visible caveats (`p.note`) instead of promises. This is the project's biggest quality and the main reason QA found nothing blocking.
2. **A sharp, defensible niche.** Instead of fighting RECUP's ~20,000-outlet city network, the strategy picks the gap between national pools (no campus-card integration) and in-house systems (island solutions), and explicitly says what it will not compete on (off-campus network, food bowls).
3. **Positioning is built from real buyer pain.** Fee resistance (Ulm), app barriers (Vytal/Relevo), the Saarland switch and the Studierendenwerke's cost pressure all map directly to a selling point. "Software without our cups" and "connect, don't replace" answer the most realistic threat: Studierendenwerke building their own system.
4. **The pilot is designed to fill the research gaps.** The KPIs (return rate, cycles per cup against the UBA break-even, cost per cycle) are exactly the numbers the research could not find, and the copy turns this into a sales argument ("results for your board and your next tender").
5. **Faithful execution and honest framing on the page.** Hero, benefits and figures match the copy; the €1 deposit is "proposed", PPWR is "about February 2028", and the footer and demo hints disclose the fictional brand and non-working buttons. The fix pass corrected the claims most likely to mislead a reader without weakening the message.
6. **The QA → fix loop worked.** The CEO sent the page back for two misleading 🟡 items rather than shipping on "no 🔴", which is the right standard for content that names real institutions.

## Areas for Improvement

1. **The first pilot target conflicts with the research.** The strategy names Tübingen as the lead pilot (tax city), but the research table states that Tübingen-Hohenheim has had **no single-use packaging since 2022**. That Studierendenwerk may have no single-use cups left to replace, and its packaging-tax pain may not apply. The strategy never addresses this. Either verify what Tübingen-Hohenheim actually runs today or lead with Konstanz or Freiburg.
2. **Cross-campus return is the headline differentiator but the least evidenced.** The research shows students return to the same buildings daily and that in the Wiesbaden pilot ~78% of cups came back to the same company. Nothing shows demand for returning a cup in another city (Tübingen to Konstanz is ~150 km). Within one Studierendenwerk's several campuses the case is stronger. Meanwhile, clearing between operators adds cost and complexity that pulls against "low per-cup fee". The slogan ("Every CampusLoop campus") and student line ("any CampusLoop campus") still lean on this network idea.
3. **The roadmap misses its own deadline.** Phase 3 is "months 24-36, i.e. before Feb 2028". Starting now (Nov 2026), month 24 is Nov 2028, nine months *after* the PPWR date. Either the phases must be compressed, or the PPWR argument should be reframed around the 2030 10% target.
4. **No cost model behind the core promise.** "Low per-cup fee, no monthly minimum" is the key operator benefit, yet own washing, logistics, cup loss and clearing costs are unknown, and competitors already charge €0.10-0.30 per use. Without even a rough break-even range, the team cannot tell whether a fee that beats in-house systems (which pay no third-party fee) is viable.
5. **Campus-card integration is a single point of failure.** Benefits 1 and the hero depend on it, but the strategy itself calls it "a key technical risk" with no information on which card systems are in use. The page caveat is correct, but the business has no fallback if integration is slow or costly per Studierendenwerk.
6. **The copy document is now stale.** `03-copywriting.md` still contains the three phrasings the fix pass removed, and `02-strategy.md` still uses the Tübingen/Konstanz example in the present tense. If someone reuses the copy for a deck or flyer, the corrected issues return. The copy doc should be updated as the source of truth.
7. **Legal claims are asserted, not checked.** "Discounts ... are legally allowed" and the single-use surcharge rest on one line in the research without a cited legal source; the VerpackG requires that the reusable option not cost more than single-use, so the exact mechanism matters. PPWR dates are flagged as unverified in the research but appear on the page as fact (hedged only by "about").
8. **QA scope was limited.** QA was a source-code review with no browser, mobile or accessibility test, and there was no re-check after the fix pass. Minor page issues remain: both CTA buttons scroll to the same list, the student-line qualifier "(where the Studierendenwerk offers a reusable discount)" reads awkwardly after the quote, and the nudge section looks thin on desktop.
9. **The secondary segment is under-argued.** Munich, Bonn and Saarland already run their own systems with no third-party fees. Why would they pay CampusLoop to connect? The only answer offered (cross-campus return) is the weakest claim (point 2).

## Recommended Next Steps (by priority)

1. **Run Phase 0 discovery before anything else, with sharper questions.** Interview 5-8 catering managers (include Konstanz, Freiburg, Saarland, Munich) and test the two riskiest assumptions directly: (a) Would you pay per cup for a card-integrated system instead of building your own? (b) Do your students actually need to return cups on other campuses, and do you have several campuses yourself? Confirm Tübingen-Hohenheim's current setup before naming it as a pilot.
2. **Map campus-card systems and integration cost.** Identify which card/payment systems the target Studierendenwerke use and what a deposit booking needs. If integration is hard, the core proposition changes.
3. **Build a rough unit-economics model.** Estimate washing, logistics, loss rate and clearing cost per cycle, and compare with the €0.10-0.30 competitor range and with in-house costs. Set a target fee range before any pitch.
4. **Fix the timeline and the PPWR claim.** Verify the PPWR dates in the Official Journal, then either compress the roadmap or reframe the urgency around 2028 readiness plus the 2030 target.
5. **Reconsider the lead differentiator.** If discovery confirms weak demand for inter-city return, lead with "card deposit, no app, pay per cup, your brand", and position cross-campus return as a multi-site benefit within one Studierendenwerk or a later network effect. Adjust the slogan accordingly.
6. **Bring the documents back in sync.** Update `03-copywriting.md` (and the example in `02-strategy.md`) to match the corrected page, so future decks and flyers do not reintroduce the fixed claims.
7. **Get a short legal check** on the surcharge/discount mechanism under VerpackG and on what compliance data PPWR will require, before the "compliance reporting" benefit is sold.
8. **Finish the prototype as a real lead tool.** Replace the anchor CTAs with a stub pilot-request form or `mailto:` and a placeholder brief; tidy the student-line wording and the nudge section; then run a browser, mobile and basic accessibility check on the fixed page.
