# Demo Video Gallery

This folder contains the qualitative demo clips for the final Image Processing
Project package. The clips were extracted from saved PPO and SAC notebook
outputs; they are visual demonstrations, not new evaluation runs.

For the main presentation view, open the GitHub Pages demo:

<p align="center">
  <a href="https://ultralamb.github.io/CarRacingV3-PPO-RayFeatures/"><strong>Open PPO + SAC demo page</strong></a>
</p>

Quantitative claims should be read from [`../docs/RESULT_SUMMARY.md`](../docs/RESULT_SUMMARY.md)
and the training logs.

## Featured Clips

| Branch | Status | Validated eval | Featured clip | Open | Download |
| ------ | ------ | -------------- | ------------- | ---- | -------- |
| PPO completed baseline | Completed 500K baseline | 938.87 +/- 7.86 @ 500,000 | `best_ppo_demo.mp4` | [open MP4](github_playable/best_ppo_demo.mp4) | [download](github_playable/best_ppo_demo.mp4?raw=1) |
| SAC fast-result branch | Partial 400K best-checkpoint | 938.51 +/- 4.88 @ 400,000 | `sac_demo_best.mp4` | [open MP4](github_playable/sac_demo_best.mp4) | [download](github_playable/sac_demo_best.mp4?raw=1) |

## Playback Notes

The original evidence MP4 files remain in this folder. GitHub sometimes fails
to preview MP4s when metadata is at the end of the file, so
[`github_playable/`](github_playable/) contains browser-friendly playback
copies with H.264 video, `yuv420p` pixel format, and faststart metadata.
[`previews/`](previews/) contains short preview clips used for project display.

Use the `open MP4` links first. If GitHub does not play a video inline, use the
download link.

## Full PPO Set

| Clip | Seed | Raw reward | Duration | Open | Download |
| ---- | ---: | ---------: | -------: | ---- | -------- |
| `best_ppo_demo.mp4` | 136505587 | 936.0 | 10.7s | [open MP4](github_playable/best_ppo_demo.mp4) | [download](github_playable/best_ppo_demo.mp4?raw=1) |
| `ppo_demo_best_3.mp4` | 1181241943 | 933.0 | 11.2s | [open MP4](github_playable/ppo_demo_best_3.mp4) | [download](github_playable/ppo_demo_best_3.mp4?raw=1) |
| `ppo_demo_best_2.mp4` | 107420369 | 932.9 | 11.2s | [open MP4](github_playable/ppo_demo_best_2.mp4) | [download](github_playable/ppo_demo_best_2.mp4?raw=1) |
| `ppo_demo_limitation_1.mp4` | 1051802512 | 918.4 | 13.6s | [open MP4](github_playable/ppo_demo_limitation_1.mp4) | [download](github_playable/ppo_demo_limitation_1.mp4?raw=1) |
| `ppo_demo_limitation_2.mp4` | 123 | 913.4 | 14.5s | [open MP4](github_playable/ppo_demo_limitation_2.mp4) | [download](github_playable/ppo_demo_limitation_2.mp4?raw=1) |
| `ppo_demo_limitation_3.mp4` | 599310825 | 911.2 | 14.8s | [open MP4](github_playable/ppo_demo_limitation_3.mp4) | [download](github_playable/ppo_demo_limitation_3.mp4?raw=1) |

## Full SAC Set

| Clip | Seed | Raw reward | Duration | Open | Download |
| ---- | ---: | ---------: | -------: | ---- | -------- |
| `sac_demo_best.mp4` | 136505587 | 933.7 | 5.5s | [open MP4](github_playable/sac_demo_best.mp4) | [download](github_playable/sac_demo_best.mp4?raw=1) |
| `sac_demo_best_2.mp4` | 107420369 | 933.3 | 5.6s | [open MP4](github_playable/sac_demo_best_2.mp4) | [download](github_playable/sac_demo_best_2.mp4?raw=1) |
| `sac_demo_best_3.mp4` | 1181241943 | 931.1 | 5.8s | [open MP4](github_playable/sac_demo_best_3.mp4) | [download](github_playable/sac_demo_best_3.mp4?raw=1) |
| `sac_demo_limitation_1.mp4` | 1051802512 | 914.4 | 7.1s | [open MP4](github_playable/sac_demo_limitation_1.mp4) | [download](github_playable/sac_demo_limitation_1.mp4?raw=1) |
| `sac_demo_limitation_2.mp4` | 123 | 911.0 | 7.4s | [open MP4](github_playable/sac_demo_limitation_2.mp4) | [download](github_playable/sac_demo_limitation_2.mp4?raw=1) |
| `sac_demo_limitation_3.mp4` | 599310825 | 908.7 | 7.6s | [open MP4](github_playable/sac_demo_limitation_3.mp4) | [download](github_playable/sac_demo_limitation_3.mp4?raw=1) |

## Interpretation

- PPO clips come from the completed 500K baseline.
- SAC clips come from the validated 400K best checkpoint of a partial run; they
  are not evidence of a completed 500K SAC run.
- PPO and SAC are not a compute-equivalent comparison.
- These clips are not a solved-status claim for CarRacing-v3.
- Playback copies are presentation assets only; they do not change numerical evidence.
