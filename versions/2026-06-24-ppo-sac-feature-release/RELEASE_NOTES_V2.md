# RELEASE_NOTES_V2.md

## Purpose

This V2 release publishes the later PPO/SAC feature-based CarRacing-v3 update
without replacing the original PPO-only course submission in the repository
root.

## Included Files

- Revised V2 report DOCX in [`report/`](report/).
- PPO and SAC notebooks in [`notebooks/`](notebooks/).
- Training logs in [`logs/`](logs/).
- Figures in [`figures/`](figures/).
- CSV tables in [`tables/`](tables/).
- Standalone MP4 demo videos in [`media/videos/`](media/videos/).
- Video metadata in [`media/video_manifest.csv`](media/video_manifest.csv).
- Documentation in [`docs/`](docs/).
- Static validation report in [`validation/`](validation/).

## Headline Results

| Branch | Result |
| ------ | ------ |
| PPO V9 | Completed 500K baseline; final eval 938.87 +/- 7.86 @ 500,000; best parsed eval 939.53 +/- 4.09 @ 480,000 |
| SAC V11.1 | Validated 400K best-checkpoint / partial fast-result branch; checkpoint 938.51 +/- 4.88 @ 400,000 |

## Limitations

- SAC V11.1 did not complete 500K.
- SAC is not claimed to beat PPO.
- The PPO/SAC comparison is not compute-equivalent.
- No raw image-input CNN policy was trained.
- CarRacing-v3 is not claimed solved.
