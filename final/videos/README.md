# Video Gallery

This folder holds 12 qualitative demo clips plus
[`video_manifest.csv`](video_manifest.csv). The clips were extracted from PPO
and SAC notebook outputs; they are visual demonstrations, not extra evaluation
runs.

Quantitative claims must be read from [`../docs/RESULT_SUMMARY.md`](../docs/RESULT_SUMMARY.md)
and the training logs.

## Playback Notes

The original evidence MP4 files remain in this folder. GitHub sometimes fails
to preview MP4s when the MP4 metadata is at the end of the file, so
[`github_playable/`](github_playable/) contains stream-copy playback versions
with the same H.264 video, `yuv420p` pixel format, and faststart metadata.

Use the `playable` links first. If GitHub does not play a video inline, use the
download link.

## Featured Demos

| Clip | Role | Playable | Download |
| ---- | ---- | -------- | -------- |
| `best_ppo_demo.mp4` | PPO completed baseline, raw reward 936.0 | [playable](github_playable/best_ppo_demo.mp4) | [download](github_playable/best_ppo_demo.mp4?raw=1) |
| `sac_demo_best.mp4` | SAC fast-result branch, raw reward 933.7 | [playable](github_playable/sac_demo_best.mp4) | [download](github_playable/sac_demo_best.mp4?raw=1) |

## Full Gallery

### PPO Completed Baseline

| Clip | Seed | Raw reward | Duration | Playable | Download |
| ---- | ---: | ---------: | -------: | -------- | -------- |
| `best_ppo_demo.mp4` | 136505587 | 936.0 | 10.7s | [playable](github_playable/best_ppo_demo.mp4) | [download](github_playable/best_ppo_demo.mp4?raw=1) |
| `ppo_demo_best_3.mp4` | 1181241943 | 933.0 | 11.2s | [playable](github_playable/ppo_demo_best_3.mp4) | [download](github_playable/ppo_demo_best_3.mp4?raw=1) |
| `ppo_demo_best_2.mp4` | 107420369 | 932.9 | 11.2s | [playable](github_playable/ppo_demo_best_2.mp4) | [download](github_playable/ppo_demo_best_2.mp4?raw=1) |
| `ppo_demo_limitation_1.mp4` | 1051802512 | 918.4 | 13.6s | [playable](github_playable/ppo_demo_limitation_1.mp4) | [download](github_playable/ppo_demo_limitation_1.mp4?raw=1) |
| `ppo_demo_limitation_2.mp4` | 123 | 913.4 | 14.5s | [playable](github_playable/ppo_demo_limitation_2.mp4) | [download](github_playable/ppo_demo_limitation_2.mp4?raw=1) |
| `ppo_demo_limitation_3.mp4` | 599310825 | 911.2 | 14.8s | [playable](github_playable/ppo_demo_limitation_3.mp4) | [download](github_playable/ppo_demo_limitation_3.mp4?raw=1) |

### SAC Fast-Result Branch

| Clip | Seed | Raw reward | Duration | Playable | Download |
| ---- | ---: | ---------: | -------: | -------- | -------- |
| `sac_demo_best.mp4` | 136505587 | 933.7 | 5.5s | [playable](github_playable/sac_demo_best.mp4) | [download](github_playable/sac_demo_best.mp4?raw=1) |
| `sac_demo_best_2.mp4` | 107420369 | 933.3 | 5.6s | [playable](github_playable/sac_demo_best_2.mp4) | [download](github_playable/sac_demo_best_2.mp4?raw=1) |
| `sac_demo_best_3.mp4` | 1181241943 | 931.1 | 5.8s | [playable](github_playable/sac_demo_best_3.mp4) | [download](github_playable/sac_demo_best_3.mp4?raw=1) |
| `sac_demo_limitation_1.mp4` | 1051802512 | 914.4 | 7.1s | [playable](github_playable/sac_demo_limitation_1.mp4) | [download](github_playable/sac_demo_limitation_1.mp4?raw=1) |
| `sac_demo_limitation_2.mp4` | 123 | 911.0 | 7.4s | [playable](github_playable/sac_demo_limitation_2.mp4) | [download](github_playable/sac_demo_limitation_2.mp4?raw=1) |
| `sac_demo_limitation_3.mp4` | 599310825 | 908.7 | 7.6s | [playable](github_playable/sac_demo_limitation_3.mp4) | [download](github_playable/sac_demo_limitation_3.mp4?raw=1) |

## Original Evidence Files

The original MP4 files remain beside this README. The `github_playable/` copies
are for GitHub/browser playback only and use stream-copy remuxing, not
retraining, reevaluation, or numerical changes.

## Interpretation

- PPO clips come from the completed 500K baseline.
- SAC clips come from the validated 400K best checkpoint of a partial run; they
  are not evidence of a completed 500K SAC run.
- PPO and SAC are not a compute-equivalent comparison.
- These clips do not show that CarRacing-v3 is solved.
