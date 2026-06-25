# validation_report.md

_Static validation run 2026-06-25 by `tools/validate_final_release.py`._

No notebooks, training, or result generation were executed.

## Overall: **PASS** (40 PASS, 0 FAIL, 2 NON-BLOCKING)

| status | check | detail |
| ------ | ----- | ------ |
| PASS | root README.md exists |  |
| PASS | root README.md has real Markdown line breaks |  |
| PASS | exists: README.md |  |
| PASS | exists: MEDIA.md |  |
| PASS | exists: RELEASE_NOTES_V2.md |  |
| PASS | exists: GITHUB_RELEASE_DRAFT.md |  |
| PASS | exists: report/CarRacing_v3_RL_Report_1103820_REVISED.docx |  |
| PASS | exists: notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb |  |
| PASS | exists: notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb |  |
| PASS | exists: logs/V9_training_500k_log.txt |  |
| PASS | exists: logs/V11_1_training_log.txt |  |
| PASS | exists: figures/checkpoint_comparison.png |  |
| PASS | exists: figures/feature_pipeline_schematic.png |  |
| PASS | exists: figures/generalization_summary.png |  |
| PASS | exists: figures/training_curve_ppo_sac.png |  |
| PASS | exists: tables/compute_budget.csv |  |
| PASS | exists: tables/headline_comparison.csv |  |
| PASS | exists: tables/notebook_output_generalization_summary.csv |  |
| PASS | exists: tables/ppo_eval_checkpoints.csv |  |
| PASS | exists: tables/sac_eval_checkpoints.csv |  |
| PASS | exists: media/video_manifest.csv |  |
| PASS | exists: docs/README.md |  |
| PASS | exists: docs/RESULT_SUMMARY.md |  |
| PASS | exists: docs/RUN_INSTRUCTIONS.md |  |
| PASS | exists: docs/ASSET_EXPORT_MANIFEST.md |  |
| PASS | exists: validation/validation_report.md |  |
| PASS | exists: tools/validate_final_release.py |  |
| PASS | V2 README.md has real Markdown line breaks |  |
| PASS | Markdown tables have separator rows |  |
| PASS | PPO notebook valid JSON |  |
| NON-BLOCKING | PPO notebook nbformat validation | nbformat not installed |
| PASS | SAC notebook valid JSON |  |
| NON-BLOCKING | SAC notebook nbformat validation | nbformat not installed |
| PASS | media/videos/ exists |  |
| PASS | exactly 12 V2 MP4 videos exist | 12 videos |
| PASS | video manifest has 12 rows | 12 rows |
| PASS | video manifest filenames exist |  |
| PASS | no stale local paths remain |  |
| PASS | no unsupported claims remain |  |
| PASS | all relative Markdown links resolve |  |
| PASS | no file exceeds 50 MiB |  |
| PASS | no file exceeds 90 MiB |  |

## Notes

- This validates the public V2 GitHub package structure only.
- Notebook execution, training stability, and live evaluation still require the intended Colab/GPU runtime.
