# Demo Video Gallery

This page is the compact public gallery for the final Image Processing Project
demo clips. The videos were extracted from saved PPO and SAC notebook outputs;
they are visual demonstrations, not new evaluation runs.

<p align="center">
  <a href="https://ultralamb.github.io/Image-Processing-Project/"><strong>Open PPO + SAC demo page</strong></a>
</p>

Use the demo page for the clean playback view. Use the tables below when you
need to open a specific clip.

Quantitative claims should be read from [`../docs/RESULT_SUMMARY.md`](../docs/RESULT_SUMMARY.md)
and the training logs.

## Featured Clips

| Branch | Status | Validated eval | Clip |
| ------ | ------ | -------------- | ---- |
| PPO completed baseline | Completed 500K baseline | 938.87 +/- 7.86 @ 500,000 | [best_ppo_demo.mp4](github_playable/best_ppo_demo.mp4) |
| SAC fast-result branch | Partial 400K best-checkpoint | 938.51 +/- 4.88 @ 400,000 | [sac_demo_best.mp4](github_playable/sac_demo_best.mp4) |

## Playback Notes

The original evidence MP4 files remain in this folder. GitHub sometimes fails
to preview MP4s when metadata is at the end of the file, so
[`github_playable/`](github_playable/) contains browser-friendly playback
copies with H.264 video, `yuv420p` pixel format, and faststart metadata.
[`previews/`](previews/) contains short preview clips used for project display.

Open the MP4 links directly for browser playback. If you need a local copy,
open the MP4 page and use GitHub's **Download** button or your browser's save
command.

## Full PPO Set

| Clip | Seed | Raw reward | Duration |
| ---- | ---: | ---------: | -------: |
| [best_ppo_demo.mp4](github_playable/best_ppo_demo.mp4) | 136505587 | 936.0 | 10.7s |
| [ppo_demo_best_3.mp4](github_playable/ppo_demo_best_3.mp4) | 1181241943 | 933.0 | 11.2s |
| [ppo_demo_best_2.mp4](github_playable/ppo_demo_best_2.mp4) | 107420369 | 932.9 | 11.2s |
| [ppo_demo_limitation_1.mp4](github_playable/ppo_demo_limitation_1.mp4) | 1051802512 | 918.4 | 13.6s |
| [ppo_demo_limitation_2.mp4](github_playable/ppo_demo_limitation_2.mp4) | 123 | 913.4 | 14.5s |
| [ppo_demo_limitation_3.mp4](github_playable/ppo_demo_limitation_3.mp4) | 599310825 | 911.2 | 14.8s |

## Full SAC Set

| Clip | Seed | Raw reward | Duration |
| ---- | ---: | ---------: | -------: |
| [sac_demo_best.mp4](github_playable/sac_demo_best.mp4) | 136505587 | 933.7 | 5.5s |
| [sac_demo_best_2.mp4](github_playable/sac_demo_best_2.mp4) | 107420369 | 933.3 | 5.6s |
| [sac_demo_best_3.mp4](github_playable/sac_demo_best_3.mp4) | 1181241943 | 931.1 | 5.8s |
| [sac_demo_limitation_1.mp4](github_playable/sac_demo_limitation_1.mp4) | 1051802512 | 914.4 | 7.1s |
| [sac_demo_limitation_2.mp4](github_playable/sac_demo_limitation_2.mp4) | 123 | 911.0 | 7.4s |
| [sac_demo_limitation_3.mp4](github_playable/sac_demo_limitation_3.mp4) | 599310825 | 908.7 | 7.6s |

## Interpretation

- PPO clips come from the completed 500K baseline.
- SAC clips come from the validated 400K best checkpoint of a partial run; they
  are not evidence of a full-length SAC run.
- PPO and SAC are not a compute-equivalent comparison.
- These clips are not an environment-completion claim for CarRacing-v3.
- The limitation clips are qualitative examples and are not all
  catastrophic-failure episodes; raw rewards are reported from the saved video
  metadata when available.
- Playback copies are presentation assets only; they do not change numerical evidence.
