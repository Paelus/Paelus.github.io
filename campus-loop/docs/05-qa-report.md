# QA Report

*Checked: `04-prototype/index.html` against `02-strategy.md` and `03-copywriting.md` (source code review only, no browser test).*

## 🔴 Must Fix

None found. The HTML is well-formed, every internal link has a matching target, and every claim and figure on the page can be traced to the strategy and copy documents.

## 🟡 Should Fix

1. **The secondary CTA is missing.** `03-copywriting.md` defines a secondary CTA, "Get our short brief on packaging taxes and PPWR deadlines. [Download the brief]", which supports the strategy's "Policy content" channel. It does not appear anywhere in `index.html`: not in the hero `.actions` and not in `section#pilot`. Add it as a `.btn-ghost` next to the pilot button in `.cta-box`, with a demo hint like the existing one.

2. **The pilot CTA does nothing.** In `section#pilot`, `<a class="btn btn-primary" href="#pilot-metrics">Request a pilot call</a>` only scrolls to the metrics list right next to it. The `.demo-hint` is honest about this. Still, a `mailto:` placeholder or a stub form would show the intended flow more clearly. The hero button with the same label (`href="#pilot"`) is fine, because it takes the visitor to the CTA section.

3. **The Tübingen/Konstanz example reads as a live network.** Card 3 (`article.card`, "One return network across campuses") says "A cup borrowed in Tübingen can be returned in Konstanz." The strategy uses this as an example of the target state. In reality CampusLoop has no participating campuses yet, and these are real Studierendenwerk locations, so the present tense could suggest an existing partnership. The footer disclaimer softens this. Suggested wording: "Once both take part, a cup borrowed in Tübingen can be returned in Konstanz."

4. **"No queue at the till" has no source.** The `<h3>` of card 1 (taken from the copy) promises faster checkout. The strategy argues "no app, no cash", but it says nothing about checkout speed or queues. Either drop "no queue at the till" or mark it as a pilot goal.

5. **"What nobody has published yet" overstates the research.** In the `section#pilot` paragraph, the strategy only says the research found **no public data on campus return rates**. It does not say the same for cycles per cup or cost per cycle across all campuses. Suggested wording: "what we found no public data on for campuses".

6. **The student line depends on a discount.** In `p.student-line`, "coffee for less" is only true if the Studierendenwerk switches on the reusable discount. The strategy treats the nudge as a setting the operator chooses, and the page itself offers "a reusable discount *or* a single-use surcharge". Add a qualifier, for example "with the launch-week discount", or make sure every pilot contract includes the discount, as the strategy's risk mitigation suggests.

7. **Navigation disappears on mobile.** `@media (max-width: 760px) { .site-header nav { display: none; } }` hides the navigation and puts nothing in its place. The page is short and the hero CTAs remain, so it is still usable, but a compact menu or a single "Pilot" link would help.

8. **Small polish items:**
   - `id="top"` sits on `<main>`, so the logo link and "Back to top" skip the header. Moving the id to `<body>` or to the header fixes this.
   - There is no `<meta name="description">`.
   - Benefit 5 from the copy is a separate `section#nudges` rather than a fifth card. That works, but the section is a two-column grid holding only one heading and one paragraph, so it looks thin on desktop.

## 🟢 Passed

- **HTML syntax:** the doctype, `lang="en"`, charset and viewport are all present. All tags are closed and properly nested (`header`/`main`/`section`/`article`/`footer`), and the inline SVGs are well-formed.
- **Heading order:** one `h1` (hero), `h2` for each section, and `h3` for the cards. Sections use `aria-labelledby` with matching ids.
- **Internal links:** `#top`, `#benefits`, `#nudges`, `#pilot` and `#pilot-metrics` all exist. No `href="#"` and no empty links.
- **No placeholder text:** there is no lorem ipsum, TODO or unreplaced bracket text.
- **Hero matches the copy word for word:** the headline, subheadline, supporting line and slogan (`p.slogan`).
- **Benefits 1-5 match the copy word for word,** including the italic caveats (`p.note`) on card-system integration and on the per-cup price. These caveats respect the strategy's "insufficient information" points.
- **Figures match the strategy:**
  - the €1 deposit is marked "proposed";
  - PPWR is dated "about February 2028";
  - the 2030 reuse target is named;
  - the pilot covers 2-4 cafeterias;
  - cycles per cup: goal more than 25, UBA break-even about 10.
- **No unsupported promises:**
  - there is no per-cup price;
  - there is no claim of compatibility with any specific campus card system;
  - reporting support is limited to VerpackG and tracking the 2030 target, with no promise about the exact PPWR reporting duties.
- **Positioning matches the strategy:**
  - "a system, not a cup brand";
  - white label;
  - software available without the cups;
  - "we connect it rather than replace it" for Studierendenwerke that already run a system;
  - StuCup is cited as proof that campus-card deposits work.
- **Audience:** the page speaks to Studierendenwerke in a professional tone. The student line is limited to pilot campuses, as the strategy and copy specify.
- **CTA:** the primary action, "Request a pilot call", is clear and appears in both the hero and the CTA section. The two buttons look clearly different (green, then amber on dark).
- **Responsive layout:** grid and flex layouts with breakpoints at 960, 760 and 520 px. Cards go from 4 to 2 to 1 column, the hero, nudge and CTA grids collapse to one column, and buttons become full width on small screens. `h1`/`h2` sizes use `clamp()`. No fixed widths that would cause horizontal scrolling were found.
- **Honesty:** the footer and `.demo-hint` say clearly that the brand is fictional and the page is a demo.

## Summary: Ready to Ship?

**Yes, as a demo prototype.** There are no 🔴 issues: the HTML is valid, nothing links nowhere, and every claim can be traced to the strategy. Before a real handover, fix the 🟡 items in this order:

1. Add the missing "Download the brief" secondary CTA.
2. Rephrase the Tübingen/Konstanz example so it does not read as an existing network.
3. Remove or qualify "no queue at the till", and soften "nobody has published yet".
4. Make the pilot CTA actually lead somewhere (a mailto link or a stub form).
