# QA Report

*Prepared by: QA Agent | Checked: `04-prototype/index.html` against `02-strategy.md` and `03-copywriting.md` | 20 Nov 2026*

---

## 🔴 Must Fix

None. I found no HTML errors and no content that contradicts the strategy or makes a claim the strategy cannot back up.

## 🟡 Should Fix

1. **The CTA buttons in `<section id="optician">` do nothing.** Both `.cta-actions` buttons ("Find a Sehwerk optician near you" and "Book a fitting appointment") use `href="#optician"`, which links to the section they are already in. The hero primary button, the nav "Opticians" link and the nav `.pill` "Book a fitting" also all lead to this same section, so the page has no real next step. That is fine for a demo, but each button should point to a clearly marked placeholder (for example `#store-locator` / `#booking` with a "coming soon" note), or at least the two buttons should go to different targets. Right now, "find" and "book" behave the same.

2. **The German slogan has no language tag.** In `#benefits .section-head`, the line `<p>Mehr sehen. Nichts filmen.</p>` sits on a page with `<html lang="en">`, so screen readers will pronounce it with English rules. Add `lang="de"` to that `<p>`. Also, `03-copywriting.md` marks the German line as *"German market adaptation for review"*. Publishing it as the benefits subheading goes a little beyond that. Confirm the team has approved it, or remove it until they have.

3. **The slogan appears four times and pushes out a real section heading.** "See more. Film nothing." is the `<title>`, the hero `.eyebrow`, the `#benefits` `<h2 id="benefits-title">` and the footer. As the benefits `<h2>` it does not tell readers what the section contains. Use a descriptive heading such as "Why Sehwerk" (which also matches the hero ghost button) and keep the slogan in the eyebrow and footer.

4. **The CTA heading repeats a button label word for word.** `<h2 id="cta-title">` reads "Find a Sehwerk optician near you", and the `.btn-primary` directly below it says exactly the same. The hero primary button uses the same text again. Consider a different heading for the CTA box, such as "Try Sehwerk at your optician", so the button carries the action.

5. **Varifocals: the page is correct, but the strategy contradicts itself.** Benefit card 2 ("Your glasses, made smarter.") says single-vision lenses are part of the base product and varifocals are *available*. This matches `03-copywriting.md` and `02-strategy.md` §1. However, `02-strategy.md` §3 (the table and selling point 2) says varifocals are *included*. The prototype has picked the safer wording, which is good. The strategy file should be made consistent so later material does not start promising included varifocals.

6. **No Impressum / Datenschutz links in the `<footer>`.** A German-market site legally needs both. For a product whose main promise is GDPR-first data handling, a missing privacy policy link is especially noticeable. The footer disclaimer ("fictional brand… demo prototype") covers the course context, but add placeholder links so the layout is ready for them.

7. **Minor: Safari prefix.** `header` uses `backdrop-filter` without `-webkit-backdrop-filter`. Older Safari versions will show the solid fallback background only. This is cosmetic, not broken.

## 🟢 Passed

- **HTML syntax:** all tags are closed and nested correctly. The document structure is valid (`<!DOCTYPE html>`, `lang`, `charset`, `viewport`, `<title>`, `<meta name="description">`). The landmarks are clear (`header`, `nav aria-label="Main"`, `main`, `section`s with `aria-labelledby`, `footer`).
- **Heading hierarchy:** one `<h1>` (hero), then `<h2>` per section, then `<h3>` per card. No levels are skipped.
- **Copy matches word for word:** the hero headline, subheadline, all four benefit cards (titles and body text), the CTA labels and the CTA supporting line are identical to `03-copywriting.md`.
- **Matches the strategy:** the three core selling points from `02-strategy.md` §3 (no camera, prescription included, data in Europe) plus German-language AI are all present. The tone suits Segment B (meetings, client visits, teleprompter, meeting notes). The page is optician-first, as the GTM plan requires.
- **No unsupported claims:** no price (the €600–900 band is still being validated), no "independently audited" claim, no health, reimbursement or accessibility-aid claims (Segment C on hold), and no battery, weight or display figures. All of the copywriter's "do not publish" notes are followed.
- **No leftover placeholder text** (no "Lorem ipsum", "TODO" or `href="#"`). The footer clearly marks the brand as fictional and the page as a course demo.
- **CTA visibility:** there is a primary/secondary button pair in the hero and in the CTA box, plus a persistent nav `.pill`. The filled vs. outline styles make the order of importance clear.
- **Mobile layout:** the `@media (max-width: 860px)` rule turns `.hero-grid` and `.cards` into one column. `@media (max-width: 560px)` hides the secondary nav links but keeps the "Book a fitting" pill, makes the buttons full width and reduces padding. Headings use `clamp()`, the SVGs scale (`width:100%; height:auto`), and `.hero-actions`/`.cta-actions` wrap. I see no likely overflow.
- **Accessibility basics:** decorative SVGs have `aria-hidden="true"`. The hero illustration has `role="img"` and an `aria-label`. The logo link has an `aria-label`. Text colours are dark on light backgrounds and light on the teal CTA box, all with good contrast. Default focus outlines have not been removed.
- **Anchor offset:** the 72px top padding on sections is larger than the 64px sticky header, so anchor jumps do not hide section headings.

## Summary: Ready to Ship?

**Yes, ready to ship as a course demo prototype.** There are no 🔴 issues. The HTML is valid, the copy matches `03-copywriting.md` exactly, and the page stays within what `02-strategy.md` supports. Before it is presented as a real landing page, fix 🟡 items 1–3: give the CTAs separate placeholder targets, add `lang="de"` (and confirm the German slogan is approved), and replace the slogan in the benefits `<h2>` with a descriptive heading. Also ask the strategy agent to fix the varifocal wording in §3 (item 5).
