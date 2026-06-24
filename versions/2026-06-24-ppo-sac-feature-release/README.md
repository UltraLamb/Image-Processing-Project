# V2 PPO/SAC Feature-Based CarRacing-v3 Release

This folder is the later V2 release of the CarRacing-v3 project. It keeps the
original PPO-only course submission in the repository root and adds a newer
feature-based PPO/SAC result package as a separate version.

## What Changed From V1

| Area | V1 root package | V2 feature release |
| ---- | --------------- | ------------------ |
| Algorithms | PPO only | PPO V9 baseline plus SAC V11.1 fast-result branch |
| Observation | 14D base observation, 56D stacked input | 16D base observation, 64D stacked input |
| Report format | IEEE-style PDF and LaTeX source | Revised DOCX report |
| Main evidence | V1 report, CSV tables, artifact zip, videos in artifact zip | V2 report, notebooks, logs, figures, tables, validation report |

V2 should be read as a later update, not as a replacement for the original V1
course submission.

## Version Summary

- **PPO V9:** completed 500K baseline.
- **SAC V11.1:** partial fast-result branch with validated 400K best checkpoint.
- **Environment:** Gymnasium `CarRacing-v3`.
- **Policy type:** Stable-Baselines3 `MlpPolicy`.
- **Input representation:** compact mask/ray/radar features, not raw-pixel CNN.
- **Observation size:** 16D base observation, stacked to 64D with 4 frames.

## Headline Results

| Branch    | Status                                         | Validated eval            | Best eval                 | Last observed step |
| --------- | ---------------------------------------------- | ------------------------: | ------------------------: | -----------------: |
| PPO V9    | completed 500K baseline                        | 938.87 +/- 7.86 @ 500,000 | 939.53 +/- 4.09 @ 480,000 | 501,760            |
| SAC V11.1 | 400K best-checkpoint / partial-run fast result | 938.51 +/- 4.88 @ 400,000 | 938.51 +/- 4.88 @ 400,000 | 418,697            |

The SAC result is not a completed 500K run and is not presented as beating PPO.
It is evidence that the same compact feature pipeline can support a strong
off-policy fast-result branch under the provided Colab/runtime constraints.

## Evidence Map

| Evidence | Path | Purpose |
| -------- | ---- | ------- |
| V2 report DOCX | [`report/CarRacing_v3_RL_Report_1103820_REVISED.docx`](report/CarRacing_v3_RL_Report_1103820_REVISED.docx) | Main written report for the V2 update |
| PPO notebook | [`notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb`](notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb) | Completed PPO V9 baseline notebook with output evidence |
| SAC notebook | [`notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb`](notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb) | SAC V11.1 fast-result notebook with output evidence |
| Logs | [`logs/`](logs/) | Training logs used for headline metrics |
| Figures | [`figures/`](figures/) | Report-facing plots and feature schematic |
| Tables | [`tables/`](tables/) | CSV checkpoint and summary tables |
| Result summary | [`docs/RESULT_SUMMARY.md`](docs/RESULT_SUMMARY.md) | Main text summary of validated results |
| Validation report | [`validation/validation_report.md`](validation/validation_report.md) | Static package validation |
| Media notes | [`MEDIA.md`](MEDIA.md) | Explains available visual evidence and video policy |
| Release notes | [`RELEASE_NOTES_V2.md`](RELEASE_NOTES_V2.md) | Summary of this V2 package |

## Reproduction / Safe-Run Notes

The notebooks ship in report/evaluation mode by default:

```python
SAFE_MODE = True
REPORT_ONLY = True
EVAL_ONLY = True
ALLOW_TRAINING = False
```

See [`docs/RUN_INSTRUCTIONS.md`](docs/RUN_INSTRUCTIONS.md). Local static checks
can validate notebook structure, but real training or live evaluation is meant
for a Colab/GPU-style runtime.

## Media / Videos

Standalone demo videos are not included in this V2 folder. The available visual
evidence is in [`figures/`](figures/) and the notebook outputs.

The V1 artifact zip in the repository root includes video files for the original
PPO-only package. Larger or future demo videos should be published as GitHub
Release assets instead of being committed directly to the repository.

## Limitations

- SAC V11.1 is a validated 400K best-checkpoint / partial-run result, not a
  completed 500K run.
- PPO and SAC are not a perfectly compute-equivalent ablation.
- No raw-pixel CNN policy was trained in this V2 package.
- The results do not prove that CarRacing-v3 is solved.
