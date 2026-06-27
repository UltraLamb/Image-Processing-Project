# Image Processing Project — Final Package

Feature-Based Image Processing and Reinforcement Learning for CarRacing-v3

This folder is the final-facing package. The main contribution is an
image-processing-derived compact visual feature representation. PPO and SAC are
used as downstream evaluation methods on Gymnasium `CarRacing-v3`.

## Final report and presentation

- Final IEEE-style report PDF: [`report/Image_Processing_Project_V2_IEEE_Report.pdf`](report/Image_Processing_Project_V2_IEEE_Report.pdf)
  _(final compiled IEEE-style two-column report; LaTeX source in `overleaf/`.)_
- [Final IEEE-style report DOCX (writing material)](report/Image_Processing_Project_V2_IEEE_Report.docx)
- [Overleaf / LaTeX package](overleaf/Image_Processing_Project_Overleaf_Package.zip)
- [Final presentation PDF](slides/Image_Processing_Project_Final_Presentation.pdf)
- [Final presentation PPTX](slides/Image_Processing_Project_Final_Presentation.pptx)

## What this package contains

- a completed PPO **500K baseline**;
- a SAC **partial 400K best-checkpoint / fast-result branch**;
- a compact full road-mask ray/radar visual-feature representation;
- notebooks, logs, tables, figures, and demo videos used as evidence.

The reinforcement-learning algorithms are not new algorithms here. They are used
to evaluate whether the compact visual features can support strong driving
behavior. PPO and SAC share the same 16D base / 64D temporally stacked visual
feature pipeline; only the downstream policy optimization method changes.

## Headline Results

| Branch | Status | Validated eval | Best parsed eval | Last observed step |
| ------ | ------ | -------------- | ---------------- | ------------------ |
| PPO completed baseline | Completed 500K baseline | 938.87 +/- 7.86 @ 500,000 | 939.53 +/- 4.09 @ 480,000 | 501,760 |
| SAC fast-result branch | Partial 400K best-checkpoint / fast-result branch | 938.51 +/- 4.88 @ 400,000 | 938.51 +/- 4.88 @ 400,000 | 418,697 |

SAC is not presented as completing 500K, outperforming PPO, or providing a
compute-equivalent comparison.

## Image Processing Pipeline

```text
RGB frame -> crop/preprocess -> HSV road mask -> ray/radar features -> stacked observation -> PPO/SAC policy
```

The compact representation makes the visual input smaller and easier to inspect
than raw image tensors. No raw image-input CNN policy was trained in this
submission.

## Evidence Map

| Evidence | Path | Purpose |
| -------- | ---- | ------- |
| Final report | [`report/`](report/) | Course-facing technical report |
| Overleaf package | [`overleaf/`](overleaf/) | LaTeX source for the IEEE-style report |
| Final slides | [`slides/`](slides/) | Course-facing presentation |
| PPO notebook | [`notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb`](notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb) | Completed PPO baseline notebook with saved outputs |
| SAC notebook | [`notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb`](notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb) | SAC fast-result notebook with saved outputs |
| Logs | [`logs/`](logs/) | Training and evaluation logs used for headline metrics |
| Figures | [`figures/`](figures/) | Report-facing plots and feature schematic |
| Tables | [`tables/`](tables/) | CSV checkpoint and summary evidence |
| Demo videos | [`videos/`](videos/) | Standalone qualitative clips extracted from notebook outputs |
| Video gallery | [`videos/README.md`](videos/README.md) | Full 12-clip gallery |
| Video manifest | [`videos/video_manifest.csv`](videos/video_manifest.csv) | Machine-readable metadata for all demo clips |
| Result summary | [`docs/RESULT_SUMMARY.md`](docs/RESULT_SUMMARY.md) | Main text summary of validated results |
| Run instructions | [`docs/RUN_INSTRUCTIONS.md`](docs/RUN_INSTRUCTIONS.md) | Reading and inspection guidance |
| Media notes | [`media.md`](media.md) | Explains visual evidence and video policy |
| Release draft | [`github_release_draft.md`](github_release_draft.md) | Draft release text only |
| Validation report | [`validation/validation_report.md`](validation/validation_report.md) | Static package validation |

## Media and demo videos

The 12 MP4 files in [`videos/`](videos/) are qualitative evidence only. They
were extracted from notebook outputs and are not additional evaluation runs. The
final presentation uses poster frames plus media links so the PDF remains
understandable without playable videos.

## Safe-run notes

The notebooks are intended to remain in report/evaluation mode:

```python
SAFE_MODE = True
REPORT_ONLY = True
EVAL_ONLY = True
ALLOW_TRAINING = False
```

Use [`docs/RUN_INSTRUCTIONS.md`](docs/RUN_INSTRUCTIONS.md) for reading and
inspection guidance. This final package does not require retraining.

## Limitations

- The SAC fast-result branch is a partial 400K checkpoint, not a completed 500K run.
- SAC is not presented as outperforming PPO.
- PPO and SAC are not compute-equivalent.
- No raw image-input CNN policy was trained in this submission.
- The project makes no environment-completion claim for CarRacing-v3.
- HSV-style preprocessing can be sensitive to visual rendering changes.
