---
name: agentic-product-discovery-video
description: Agentic AI Product Discovery & Product Video Generator. A multi-agent workflow for cross-border e-commerce that goes from market opportunity to customer insight, product knowledge base, digital twin, a 12-scene 120-second 16:9 video storyboard (XLSX) and a quality review. Use when the user names a product (or product idea) and target markets and wants discovery evidence plus a production-ready product video plan.
---

# Agentic AI Product Discovery & Product Video Generator

Discover Market Opportunities → Understand the Product → Build a Digital Twin → Generate Product Videos.

## Input contract
Ask for (or infer and state as assumptions):
- `product`: name + one-line description (real or concept)
- `markets`: 2–4 target countries (cross-border)
- `channel`: e.g. own D2C shop, Amazon, Rakuten, TikTok Shop
- `protagonist`: male or female presenter for the video
- optional facts the user already has (specs, prices, reviews)

## Orchestration (six specialist agents, one shared product story)
Run the agents in this order. Each agent reads the outputs of the agents before it and writes ONE file
into `runs/<product-slug>/`. Prompts for each role are in `agents/`.

| # | Agent | Reads | Writes |
|---|---|---|---|
| 1 | Market Research (`agents/1_market_research.md`) | input | `01_market_research.md` |
| 2 | Customer Insight (`agents/2_customer_insight.md`) | 01 | `02_customer_insight.md` |
| 3 | Product Intelligence (`agents/3_product_intelligence.md`) | input, 01–02 | `03_product_intelligence.md` |
| 4 | Digital Twin (`agents/4_digital_twin.md`) | 01–03 | `04_digital_twin.json` |
| 5 | Product Video (`agents/5_product_video.md`) | 04 | `05_storyboard.json` → `05_storyboard.xlsx`, `05_script.md` |
| 6 | Quality Review (`agents/6_quality_review.md`) | all | `06_quality_review.md` |

Finish with `00_summary.md` (one page: opportunity, target customer, positioning, video idea, open checks).

## Shared output contract
See `references/output_contract.md`. Key rules:
- Every market claim carries a source or is labelled **[assumption]** / **[to verify]**.
- Product facts for a concept product are labelled **[concept spec]**; never present them as tested results.
- No health, medical or performance claims the product cannot prove.
- Everything for the video is written in English.

## Execution
```
python scripts/build_storyboard.py runs/<product-slug>/05_storyboard.json
```
turns the Product Video agent's JSON into the formatted XLSX storyboard
(12 scenes × 10 s = 120 s, 16:9, columns: Scene, Timecode, Shot, Image prompt, Image-to-video prompt,
Voice prompt, Dialogue/voice-over, On-screen caption, Localization notes).

## Human checkpoint
The Quality Review agent ends with a list of items that need human confirmation before anything is published.
