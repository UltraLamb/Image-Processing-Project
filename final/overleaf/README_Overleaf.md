# Overleaf / LaTeX Package

This folder is the self-contained LaTeX source for the IEEE-style report:

**Image Processing Project: Feature-Based Image Processing and Reinforcement
Learning for CarRacing-v3** — Joe / Student ID 1103820.

## Contents

- `main.tex` — report source (IEEEtran, two-column conference style).
- `references.bib` — bibliography (Gymnasium, Stable-Baselines3, PPO, SAC,
  OpenCV).
- `figures/` — figures referenced by `main.tex`
  (`feature_pipeline_cards.png`, `ray_fan_schematic.png`,
  `training_curve_ppo_sac.png`, `generalization_summary.png`).

## How to compile

### Option 1 — Overleaf (recommended)

1. Create a new Overleaf project.
2. Upload the contents of this folder (`main.tex`, `references.bib`, and the
   whole `figures/` directory).
3. Set the compiler to **pdfLaTeX** and the main document to `main.tex`.
4. Click **Recompile**. IEEEtran is built into Overleaf, so no extra class files
   are needed.

### Option 2 — local TeX Live / MiKTeX

The `IEEEtran` package is required; it is included in full TeX Live and MiKTeX
distributions (it is NOT shipped in this package). From this folder run:

```bash
latexmk -pdf main.tex
```

or, if `latexmk` is unavailable:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

This produces `main.pdf`.

## After compilation

Place the compiled PDF at:

```
final/report/Image_Processing_Project_V2_IEEE_Report.pdf
```

That file is the official final report. Do **not** use archived DOCX or PDF
preview material as the official report; those files are kept only for
traceability.

## Notes

- The report uses only verified project content. The base observation is
  16-dimensional (nine rays + three smoothed actions + speed + curvature +
  front-ray change + left-right asymmetry); four observations are stacked into
  a 64-dimensional vector. PPO and SAC share this exact pipeline.
- Headline numbers are parsed from the training logs: PPO completed baseline
  $938.87 \pm 7.86$ at 500{,}000 (best parsed $939.53 \pm 4.09$ at 480{,}000);
  SAC fast-result branch $938.51 \pm 4.88$ at the 400{,}000 best checkpoint.
- The SAC result is partial (no eval after 400{,}000). The PPO/SAC comparison is
  not compute-equivalent, and CarRacing-v3 is not claimed to be solved.
