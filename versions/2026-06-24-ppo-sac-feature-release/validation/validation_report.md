# validation_report.md

_Static validation run 2026-06-24 by `tools/validate_final_release.py` (no notebooks/training executed)._

## Overall: **PASS**  (26 PASS, 0 FAIL, 0 NON-BLOCKING)

| status | check | detail |
|---|---|---|
| PASS | exists: notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb |  |
| PASS | exists: notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb |  |
| PASS | exists: logs/V9_training_500k_log.txt |  |
| PASS | exists: logs/V11_1_training_log.txt |  |
| PASS | exists: docs/README.md |  |
| PASS | exists: docs/RESULT_SUMMARY.md |  |
| PASS | exists: docs/RUN_INSTRUCTIONS.md |  |
| PASS | exists: docs/NOTEBOOK_CLEANUP_CHANGELOG.md |  |
| PASS | exists: docs/REPORT_AND_PPT_STARTER_NOTES.md |  |
| PASS | exists: tools/build_final_clean_release.py |  |
| PASS | exists: tools/validate_final_release.py |  |
| PASS | exists: validation/ |  |
| PASS | PPO valid JSON |  |
| PASS | PPO passes nbformat.validate |  |
| PASS | SAC valid JSON |  |
| PASS | SAC passes nbformat.validate |  |
| PASS | PPO headings clean (no old-version clutter) | 12 headings clean |
| PASS | SAC headings clean (no old-version clutter) | 18 headings clean |
| PASS | PPO no unguarded model.learn( | all .learn() calls inside ALLOW_TRAINING guard |
| PASS | PPO ships ALLOW_TRAINING=False (training disabled by default) |  |
| PASS | SAC no unguarded model.learn( | all .learn() calls inside ALLOW_TRAINING guard |
| PASS | SAC ships ALLOW_TRAINING=False (training disabled by default) |  |
| PASS | RESULT_SUMMARY marks PPO completed 500K baseline |  |
| PASS | RESULT_SUMMARY marks SAC 400K best-checkpoint / partial run |  |
| PASS | original preserved: V9_CarRacing_PPO_Colab.ipynb |  |
| PASS | original preserved: V11_1_CarRacing_SAC_Fast_Result.ipynb |  |

## Notes
- Static checks only: AST/JSON/nbformat validity, heading cleanliness, training-guard presence, and result-summary honesty.
- Seed isolation, eval correctness, and training stability can only be verified by running the notebooks in Colab (per project rule 2).
