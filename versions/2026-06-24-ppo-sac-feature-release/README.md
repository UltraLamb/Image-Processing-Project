# V2 PPO/SAC Feature-Based CarRacing-v3 Release

This V2 release publishes the later feature-based PPO/SAC CarRacing-v3 update
without replacing the original PPO-only course submission in the repository
root.

## What This V2 Release Is

V2 packages a completed PPO V9 500K baseline and a SAC V11.1 partial
fast-result branch using compact mask/ray/radar features with
Stable-Baselines3 `MlpPolicy`. The notebooks keep their output evidence, and
the embedded demo videos have been extracted as standalone MP4 files under
[`media/videos/`](media/videos/).

## What Changed From V1

| Area          | V1 root package                                      | V2 feature release                                               |
| ------------- | ---------------------------------------------------- | ---------------------------------------------------------------- |
| Algorithms    | PPO only                                             | PPO V9 baseline plus SAC V11.1 fast-result branch                |
| Observation   | 14D base observation, 56D stacked input              | 16D base observation, 64D stacked input                          |
| Report format | IEEE-style PDF and LaTeX source                      | Revised DOCX report                                              |
| Media         | videos packaged inside the V1 artifact zip           | 12 standalone MP4 videos extracted from notebook outputs         |
| Main evidence | V1 report, CSV tables, artifact zip, videos in zip   | V2 report, notebooks, logs, figures, tables, videos, validation  |

V2 should be read as a later update, not as a replacement for the original V1
course submission.

## Headline Results

| Branch    | Status                                         | Validated eval            | Best eval                 | Last observed step |
| --------- | ---------------------------------------------- | ------------------------: | ------------------------: | -----------------: |
| PPO V9    | completed 500K baseline                        | 938.87 +/- 7.86 @ 500,000 | 939.53 +/- 4.09 @ 480,000 | 501,760            |
| SAC V11.1 | 400K best-checkpoint / partial-run fast result | 938.51 +/- 4.88 @ 400,000 | 938.51 +/- 4.88 @ 400,000 | 418,697            |

The SAC result is a partial 400K checkpoint result and is not presented as
outperforming PPO. It is evidence that the same compact feature pipeline can
support a strong off-policy fast-result branch under the provided Colab/runtime
constraints.

## Evidence Map

| Evidence | Path | Purpose |
| -------- | ---- | ------- |
| V2 report DOCX | [`report/CarRacing_v3_RL_Report_1103820_REVISED.docx`](report/CarRacing_v3_RL_Report_1103820_REVISED.docx) | Main written report for the V2 update |
| PPO notebook | [`notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb`](notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb) | Completed PPO V9 baseline notebook with output evidence |
| SAC notebook | [`notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb`](notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb) | SAC V11.1 fast-result notebook with output evidence |
| Logs | [`logs/`](logs/) | Training logs used for headline metrics |
| Figures | [`figures/`](figures/) | Report-facing plots and feature schematic |
| Tables | [`tables/`](tables/) | CSV checkpoint and summary tables |
| Demo videos | [`media/videos/`](media/videos/) | Standalone MP4 clips extracted from notebook outputs |
| Video manifest | [`media/video_manifest.csv`](media/video_manifest.csv) | Metadata for all 12 extracted videos |
| Result summary | [`docs/RESULT_SUMMARY.md`](docs/RESULT_SUMMARY.md) | Main text summary of validated results |
| Media notes | [`MEDIA.md`](MEDIA.md) | Explains visual evidence and video policy |
| Release notes | [`RELEASE_NOTES_V2.md`](RELEASE_NOTES_V2.md) | Summary of this V2 package |
| GitHub release draft | [`GITHUB_RELEASE_DRAFT.md`](GITHUB_RELEASE_DRAFT.md) | Draft release text; not published automatically |
| Validation report | [`validation/validation_report.md`](validation/validation_report.md) | Static package validation |

## Media And Demo Videos

The 12 standalone MP4 videos in [`media/videos/`](media/videos/) were extracted
from the embedded notebook outputs. They are visual evidence only, not
additional evaluation runs.

See [`MEDIA.md`](MEDIA.md) for the full video table and
[`media/video_manifest.csv`](media/video_manifest.csv) for machine-readable
metadata.

## How To Read The Evidence

Use [`docs/RESULT_SUMMARY.md`](docs/RESULT_SUMMARY.md) as the main source for
headline metrics. It is backed by the logs in [`logs/`](logs/). Notebook output
tables and videos are secondary evidence for tested-seed behavior and visual
inspection.

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

## Limitations

- SAC V11.1 is a validated 400K best-checkpoint / partial-run result, not a
  completed 500K run.
- SAC is not claimed to beat PPO.
- PPO and SAC are not a compute-equivalent comparison.
- No raw image-input CNN policy was trained in this V2 package.
- The results do not prove a solved CarRacing-v3 environment.
