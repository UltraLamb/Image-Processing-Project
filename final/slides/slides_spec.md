# Image Processing Project — Final Presentation (15 slides)

**Feature-Based Image Processing and Reinforcement Learning for CarRacing-v3**

Joe — Student ID 1103820

---

## How to use this file

This is the authoritative 15-slide deck specification and presenter handout.
Each block below is one slide: the **Title**, the **bullet** content to place on
the slide, and the **Visual** asset to use. Build the PPTX from this spec (the
local machine has no PowerPoint/PDF export toolchain), then export a PDF. Use
**real figures/screenshots only** (paths below are relative to `final/`).
**Do not embed videos** — use poster frames plus links.

Slide count target: 15 (split slide 15 into 15+16 if it gets dense). The
original 12-slide deck is archived at
`archive/legacy_versions/original_slides_12/` as a starting template.

Visual asset paths (relative to `final/`):

- Pipeline: `figures/feature_pipeline_schematic.png`
- Training curves: `figures/training_curve_ppo_sac.png`
- Generalization (secondary): `figures/generalization_summary.png`
- Best PPO poster: `figures/best_ppo_demo_poster.png`
- Posters folder: `posters/` (PPO/SAC best + limitation posters)

---

## Slide 1 — Title

- **Image Processing Project**
- Feature-Based Image Processing and Reinforcement Learning for CarRacing-v3
- Joe — Student ID 1103820
- Visual: `figures/feature_pipeline_schematic.png` (as banner)

## Slide 2 — Motivation and Project Goal

- CarRacing-v3 is a visual continuous-control task: 96x96 RGB in, 3D action out.
- Training directly on pixels is expensive (perception + control learned together).
- Goal: move perception into a deterministic image-processing wrapper; keep the
  RL algorithm standard.
- The contribution is the visual representation; PPO/SAC are evaluation tools.
- Visual: small CarRacing-v3 screenshot or pipeline banner.

## Slide 3 — CarRacing-v3 Environment

- Randomized, procedurally generated tracks (must generalize, not memorize).
- Observation: 96x96 top-down RGB frame.
- Action: [steer in -1..1, gas in 0..1, brake in 0..1].
- Reward: track progress (reduced for off-order tiles / time outs).
- Hard cases: sudden failure after sharp turns or off-road drift.
- Visual: environment frame or screenshot.

## Slide 4 — Why Image Processing Features?

- Raw pixels force the policy to learn perception from scratch.
- A compact, inspectable road description trains faster and audits cleanly.
- Smaller observation → MLP policy instead of a CNN.
- Thresholds, ray geometry, and shaping are all explicit and reproducible.
- Visual: contrast "raw pixel stack" vs "compact feature vector" (simple diagram).

## Slide 5 — Visual Preprocessing Pipeline

- RGB frame → crop driving-relevant region → convert to HSV.
- HSV separates road/grass by color, robust to brightness.
- Road mask = bitwise complement of grass band.
- Clean with 3x3 morphological opening; optional connected-component cleanup.
- Visual: `figures/feature_pipeline_schematic.png`.

## Slide 6 — Road-Mask and Ray/Radar Feature Extraction

- Grass HSV band removed → road mask.
- Nine distance rays cast across a calibrated angular fan:
  [-70, -52.5, -35, -17.5, 0, 17.5, 35, 52.5, 70] degrees.
- Each ray returns normalized distance to first non-road pixel.
- Fan is speed-adaptive (tighter when fast, wider when slow).
- Visual: mask + ray fan diagram (from screenshots or pipeline schematic).

## Slide 7 — Observation Vector Anatomy (16D)

- Base observation = 16 dimensions:
  - 9 ray distances (indices 0–8)
  - 3 smoothed previous actions (9–11)
  - speed (12)
  - curvature proxy (13)
  - front-ray change (14)
  - left-right asymmetry (15)
- Curvature active only when forward road is detected.
- Visual: simple table or labeled 16-slot bar (build from this spec).

## Slide 8 — Shared 16D → 64D Pipeline Across PPO and SAC

- Four consecutive 16D observations are stacked → 64D.
- Key point: PPO and SAC see the **same** feature stream.
- Perception layer held constant; only the policy optimizer changes.
- This isolates the image-processing contribution.
- Visual: two-box diagram "shared perception → PPO" and "→ SAC".

## Slide 9 — PPO Completed Baseline Setup

- Off-the-shelf Stable-Baselines3 PPO, MLP policy (not modified).
- VecNormalize observation normalization.
- Completed 500,000-step run.
- Artifact-driven eval: restore checkpoint, reload VecNormalize, fixed seeds.
- Visual: PPO icon / curve start.

## Slide 10 — SAC Fast-Result Branch Setup

- Off-the-shelf Stable-Baselines3 SAC, MLP policy (not modified).
- Same shared 16D→64D feature pipeline as PPO.
- Partial run; validated at the 400,000-step best checkpoint.
- Early stop reflects Colab/runtime limits and fast-result intent.
- Visual: SAC icon.

## Slide 11 — Training and Evaluation Protocol

- Headline metrics parsed from training logs + validated best checkpoints.
- Secondary evidence: fixed multi-seed set, randomized multi-seed set,
  bootstrap confidence interval (clearly labeled secondary).
- Notebooks in safe report/eval mode (training disabled by default).
- No retraining required to inspect evidence.
- Visual: simple protocol flow (train → checkpoint → reload → eval).

## Slide 12 — Primary Results

- PPO completed baseline: **938.87 ± 7.86 @ 500,000** (best parsed
  **939.53 ± 4.09 @ 480,000**; last step 501,760).
- SAC fast-result branch: **938.51 ± 4.88 @ 400,000** (last step 418,697; no
  eval after 400K).
- Both reach the low-930s to low-940s band on the same representation.
- Visual: `figures/training_curve_ppo_sac.png`.

## Slide 13 — Secondary Generalization Evidence

- Saved notebook outputs on fixed + randomized multi-seed sets.
- PPO: ~925–926 ± ~7; SAC: ~923–925 ± ~8 (bootstrap CIs overlap).
- Explicitly secondary — distinct from log-validated headline numbers.
- Quantitative claims come from logs/tables, not from clips alone.
- Visual: `figures/generalization_summary.png`.

## Slide 14 — Limitations and Future Work

- SAC is a partial 400K fast-result, not a completed 500K matched-budget run.
- PPO/SAC comparison is **not** compute-equivalent; SAC not claimed to beat PPO.
- Engineered visual features used, not a raw-pixel CNN baseline.
- CarRacing-v3 is not claimed to be solved.
- Future work: matched-budget multi-seed runs, raw-pixel baseline, systematic
  ablation of perception stages.

## Slide 15 — Reproducibility / GitHub / Final Takeaways

- Compact road-mask ray-feature representation supports strong driving.
- PPO and SAC share one 16D→64D pipeline; only the optimizer differs.
- Repo structure: `final/` (public) + `archive/` (history).
  - `final/report/`, `final/overleaf/`, `final/slides/`, `final/notebooks/`,
    `final/figures/`, `final/tables/`, `final/videos/`, `final/logs/`,
    `final/docs/`.
- Best demo: `final/videos/best_ppo_demo.mp4` (poster:
  `final/figures/best_ppo_demo_poster.png`).
- Takeaway: image processing is the contribution; the method is
  sample-efficient and promising, not uniformly robust.

_(If slide 15 is too dense, split into: 15 Reproducibility & GitHub Structure,
16 Final Takeaways.)_

---

## Manual export steps (no local toolchain)

1. Open PowerPoint (or Keynote/Google Slides).
2. Create 15 slides from the spec above, one block per slide.
3. Insert the listed visual assets (real figures/posters only).
4. Do **not** embed videos — use poster images and text links to
   `final/videos/`.
5. Save as `Image_Processing_Project_Final_Presentation.pptx`.
6. Export/Print to PDF as `Image_Processing_Project_Final_Presentation.pdf`.
7. Place both files in `final/slides/`.

The archived 12-slide deck at
`archive/legacy_versions/original_slides_12/Image_Processing_Project_Final_Presentation_12slide.pptx`
can be opened as a style template, then expanded to 15 slides per this spec.
