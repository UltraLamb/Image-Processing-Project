# validation_report.md

_Static validation of the `final/` package, run 2026-06-27. No notebooks,
training, or result generation were executed._

## Overall: PASS (structure, links, manifest, terms) · report PDF pending Overleaf

| status | check | detail |
| ------ | ----- | ------ |
| PASS | final/ folder map complete | report, overleaf, slides, notebooks, figures, tables, videos, logs, docs |
| PASS | root README.md / requirements.txt and final/docs/dataset.md exist | |
| PASS | final presentation PPTX exists | 15 slides |
| PASS | final presentation PDF exists | 15 pages |
| PASS | Overleaf package zip exists | main.tex + references.bib + README_Overleaf.md + 3 figures |
| PASS | PPO notebook valid JSON (nbformat) | |
| PASS | SAC notebook valid JSON (nbformat) | |
| PASS | exactly 12 demo MP4 videos exist | |
| PASS | video_manifest.csv maps 1:1 to MP4 files | 12 rows |
| PASS | all relative Markdown links resolve | except report PDF (pending) |
| PASS | no forbidden internal labels in final-facing docs/figures | neutral terminology throughout |
| PASS | no unsupported claims | limitations stated as negations only |
| PASS | report figures use neutral legends/labels | training curve + generalization regenerated |
| PENDING | official report PDF | compile Overleaf package -> place at report/Image_Processing_Project_V2_IEEE_Report.pdf |

## Notes

- Headline metrics are parsed from the training logs and validated best
  checkpoints; nothing was re-run.
- The official IEEE report PDF is produced in Overleaf (no local LaTeX toolchain);
  see `report/README.md`.
- Full classification (AUTO-PASS / MANUAL-REQUIRED / BLOCKER) is in
  `FINAL_VALIDATION_REPORT.md` at the submission root.
