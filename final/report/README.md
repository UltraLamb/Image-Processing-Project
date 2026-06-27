# Final report

The official final report is:

```
Image_Processing_Project_V2_IEEE_Report.pdf
```

This is the compiled IEEE-style technical report (two-column, conference format),
built from the LaTeX source in [`../overleaf/`](../overleaf/). It covers the
environment and problem, the full road-mask ray-feature pipeline (HSV road-mask
extraction, morphological opening, connected components, and the nine-ray
geometry), the shared 16-dimensional base / 64-dimensional temporally stacked
observation, the PPO completed baseline and SAC fast-result branch, the primary
versus secondary evidence hierarchy, and limitations / failure modes. The full
per-checkpoint evaluation tables are in the appendix.

## Files in this folder

- `Image_Processing_Project_V2_IEEE_Report.pdf` — the final compiled report.
- `Image_Processing_Project_V2_IEEE_Report.docx` — DOCX writing material /
  editable reference (not the official compiled PDF).

To rebuild the PDF, compile
[`../overleaf/Image_Processing_Project_Overleaf_Package.zip`](../overleaf/Image_Processing_Project_Overleaf_Package.zip)
in Overleaf (pdfLaTeX, main document `main.tex`; IEEEtran is built in).

_This is an IEEE-style / conference-format technical report — not a published,
accepted, or official IEEE publication._
