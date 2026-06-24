# V2 PPO/SAC Feature Release

GitHub-ready V2 release for the project **"Visual Reinforcement Learning for
Randomized CarRacing-v3: PPO Baseline, Generalization, and Speed."**

This folder contains two cleaned notebooks (PPO baseline + SAC fast result), the
supporting training logs, an evidence-based result summary, final report assets,
and validation notes.

## Layout

```
versions/2026-06-24-ppo-sac-feature-release/
  README.md
  report/
    CarRacing_v3_RL_Report_1103820_REVISED.docx
  notebooks/
    Final_PPO_Baseline_CarRacing_v3.ipynb   # PPO baseline, completed 500K
    Final_SAC_Fast_Result_CarRacing_v3.ipynb # SAC fast result, 400K best (partial)
  logs/
    V9_training_500k_log.txt
    V11_1_training_log.txt
  figures/
    checkpoint_comparison.png
    feature_pipeline_schematic.png
    generalization_summary.png
    training_curve_ppo_sac.png
  tables/
    compute_budget.csv
    headline_comparison.csv
    notebook_output_generalization_summary.csv
    ppo_eval_checkpoints.csv
    sac_eval_checkpoints.csv
  docs/
    README.md
    RESULT_SUMMARY.md
    RUN_INSTRUCTIONS.md
    ASSET_EXPORT_MANIFEST.md
  tools/
    build_final_clean_release.py
    validate_final_release.py
  validation/
    validation_report.md
```

## Headline results (see `docs/RESULT_SUMMARY.md`)

- **PPO (V9):** completed 500K baseline. Eval@500K = 938.9; best 939.5 @ 480,000.
- **SAC (V11.1):** 400K best checkpoint = 938.5 +/- 4.9. **Partial run (~82%), not a completed 500K run.**

## Safety

Both notebooks ship in **REPORT_ONLY / EVAL_ONLY** mode. Training cells are
disabled by default (`ALLOW_TRAINING=False`). Nothing here trains automatically.
See [`RUN_INSTRUCTIONS.md`](RUN_INSTRUCTIONS.md).

Validate this V2 folder from the version root with:

```bash
python tools/validate_final_release.py
```
