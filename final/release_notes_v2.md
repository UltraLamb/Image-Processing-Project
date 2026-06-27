# Release Notes — V2 Final Submission

## Purpose

This V2 final submission publishes the feature-based CarRacing-v3 update as the
public-facing final version of the Image Processing Project. The original
PPO-only submission is preserved under `archive/` for traceability.

## Final materials (in `final/`)

- Final report (IEEE-style) in [`report/`](report/).
- Overleaf / LaTeX package in [`overleaf/`](overleaf/).
- Final presentation (PPTX/PDF) in [`slides/`](slides/).
- PPO and SAC notebooks (saved outputs) in [`notebooks/`](notebooks/).
- Training logs in [`logs/`](logs/).
- Figures in [`figures/`](figures/).
- CSV tables in [`tables/`](tables/).
- Standalone demo MP4 videos in [`videos/`](videos/).
- Video metadata in [`videos/video_manifest.csv`](videos/video_manifest.csv).
- Documentation in [`docs/`](docs/).
- Static validation report in [`validation/`](validation/).

## Headline Results

| Branch | Result |
| ------ | ------ |
| PPO completed baseline | Completed 500K baseline; final eval 938.87 +/- 7.86 @ 500,000; best parsed eval 939.53 +/- 4.09 @ 480,000 |
| SAC fast-result branch | Validated 400K best-checkpoint / partial fast-result branch; checkpoint 938.51 +/- 4.88 @ 400,000 |

PPO and SAC share the same 16D base / 64D temporally stacked visual feature
pipeline; only the downstream policy optimization method changes.

## Limitations

- The SAC fast-result branch did not complete 500K.
- SAC is not claimed to beat PPO.
- The PPO/SAC comparison is not compute-equivalent.
- No raw image-input CNN policy was trained.
- CarRacing-v3 is not claimed to be solved.
