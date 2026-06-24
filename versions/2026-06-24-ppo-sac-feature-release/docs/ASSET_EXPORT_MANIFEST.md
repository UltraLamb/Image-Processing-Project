# ASSET_EXPORT_MANIFEST.md

Assets in this V2 folder were copied from the final clean-release evidence
package. No training was rerun and no notebook outputs were regenerated during
this GitHub packaging step.

## Source-of-truth hierarchy

1. `docs/RESULT_SUMMARY.md` and the logs in `logs/` for headline metrics.
2. Notebook embedded outputs for COMPARE5/RANDOM10/bootstrap evidence.
3. Figures and CSV files in this V2 folder for report-facing summaries.

## Included assets

| path | source evidence | use |
|---|---|---|
| `figures/checkpoint_comparison.png` | `docs/RESULT_SUMMARY.md`; training logs | PPO/SAC headline checkpoint comparison |
| `figures/feature_pipeline_schematic.png` | project method description | compact feature pipeline schematic |
| `figures/generalization_summary.png` | `tables/notebook_output_generalization_summary.csv` | tested-seed summary |
| `figures/training_curve_ppo_sac.png` | checkpoint CSV tables | PPO/SAC learning curve |
| `tables/compute_budget.csv` | `docs/RESULT_SUMMARY.md`; training logs | budget/status disclosure |
| `tables/headline_comparison.csv` | `docs/RESULT_SUMMARY.md`; training logs | headline comparison |
| `tables/notebook_output_generalization_summary.csv` | notebook embedded outputs | secondary generalization evidence |
| `tables/ppo_eval_checkpoints.csv` | `logs/V9_training_500k_log.txt` | PPO checkpoint curve |
| `tables/sac_eval_checkpoints.csv` | `logs/V11_1_training_log.txt` | SAC checkpoint curve |

## Missing or intentionally excluded

- Standalone source video files are not included in this V2 GitHub folder.
- SAC 500K final artifacts are not available or validated in the provided
  evidence.
- Draft reports, review notes, and temporary build files are excluded.
