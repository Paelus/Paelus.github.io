# Output contract (shared by all six agents)

1. **One file per agent**, Markdown unless stated otherwise, max ~1 page, headings in the order given in the agent prompt.
2. **Evidence labels** on every non-trivial claim:
   - `[source: <publisher, year>]` – published data or reporting
   - `[assumption]` – reasoned estimate, shows the reasoning
   - `[to verify]` – plausible but must be checked before use
   - `[concept spec]` – product property of a concept product (not tested)
3. **Hand-off block** at the end of each file: 3–5 bullet points the next agent must use.
4. **Markets** are always compared side by side (table), never merged into one "global" view.
5. **Language**: analysis in English; localization notes may quote local wording.
6. **Video JSON** (`05_storyboard.json`): list of 12 objects with keys
   `scene, timecode, shot, image_prompt, i2v_prompt, voice_prompt, dialogue, caption, localization`.
7. **No exaggeration**: no "best", "#1", medical or guaranteed-result claims unless sourced.
