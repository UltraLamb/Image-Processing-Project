# validation_report.md

_Static validation run 2026-06-25 by `tools/validate_final_release.py`._

No notebooks, training, or result generation were executed.

## Overall: **PASS** (28 PASS, 0 FAIL, 2 NON-BLOCKING)

| status | check | detail |
|---|---|---|
| PASS | exists: README.md |  |
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
| PASS | exists: docs/README.md |  |
| PASS | exists: docs/RESULT_SUMMARY.md |  |
| PASS | exists: docs/RUN_INSTRUCTIONS.md |  |
| PASS | exists: docs/ASSET_EXPORT_MANIFEST.md |  |
| PASS | exists: validation/validation_report.md |  |
| PASS | exists: tools/build_final_clean_release.py |  |
| PASS | exists: tools/validate_final_release.py |  |
| PASS | PPO notebook valid JSON |  |
| NON-BLOCKING | PPO notebook nbformat validation | nbformat not installed |
| PASS | SAC notebook valid JSON |  |
| NON-BLOCKING | SAC notebook nbformat validation | nbformat not installed |
| PASS | V2 README/docs avoid unsupported PPO/SAC claims |  |
| PASS | relative Markdown links resolve |  |
| PASS | no file exceeds 50 MiB |  |
| PASS | no file exceeds 90 MiB |  |

## Notes

- This validates the V2 GitHub package structure only.
- Notebook execution, training stability, and live evaluation still require the intended Colab/GPU runtime.
