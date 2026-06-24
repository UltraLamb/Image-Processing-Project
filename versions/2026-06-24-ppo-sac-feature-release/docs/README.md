# CarRacing Final Clean Release

Presentation-ready final release for the project
**"Visual Reinforcement Learning for Randomized CarRacing-v3: PPO Baseline,
Generalization, and Speed."**

Two cleaned notebooks (PPO baseline + SAC fast result), the supporting training
logs, an evidence-based result summary, and starter notes for the written report
and slides.

## Layout

```
CarRacing_Final_Clean_Release/
  notebooks/
    Final_PPO_Baseline_CarRacing_v3.ipynb   # PPO baseline, completed 500K
    Final_SAC_Fast_Result_CarRacing_v3.ipynb# SAC fast result, 400K best (partial)
  logs/
    V9_training_500k_log.txt                 # PPO training log (unmodified copy)
    V11_1_training_log.txt                   # SAC training log (unmodified copy)
  docs/
    README.md  RESULT_SUMMARY.md  RUN_INSTRUCTIONS.md
    NOTEBOOK_CLEANUP_CHANGELOG.md  REPORT_AND_PPT_STARTER_NOTES.md
  tools/
    build_final_clean_release.py  validate_final_release.py
  validation/
    validation_report.md
```

## Headline results (see `docs/RESULT_SUMMARY.md`)

- **PPO (V9):** completed 500K baseline. Eval@500K = 938.9; best 939.5 @ 480,000.
- **SAC (V11.1):** 400K best checkpoint = 938.5 +/- 4.9. **Partial run (~82%), not a completed 500K run.**

## Safety

Both notebooks ship in **REPORT_ONLY / EVAL_ONLY** mode. Training cells are
disabled by default (`ALLOW_TRAINING=False`). Nothing here trains automatically.
See `docs/RUN_INSTRUCTIONS.md`.

Regenerate with `python tools/build_final_clean_release.py` then
`python tools/validate_final_release.py`.
