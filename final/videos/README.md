# Video Gallery

This folder holds the 12 standalone demo MP4 clips plus the machine-readable
[`video_manifest.csv`](video_manifest.csv). The clips were extracted from the
embedded outputs of the PPO and SAC notebooks. They are **qualitative evidence
only** — they are not additional evaluation runs.

Quantitative claims must be read from [`docs/RESULT_SUMMARY.md`](../docs/RESULT_SUMMARY.md)
and the training logs, not from these clips.

## Featured demos

| Clip | Role | Link |
| ---- | ---- | ---- |
| `best_ppo_demo.mp4` | Highest-reward PPO baseline clip (raw reward 936) | [`best_ppo_demo.mp4`](best_ppo_demo.mp4) |
| `sac_demo_best.mp4` | Highest-reward SAC fast-result clip (raw reward 933.7) | [`sac_demo_best.mp4`](sac_demo_best.mp4) |

## Full gallery (12 clips)

Sorted by branch, then best-to-limitation.

### PPO completed baseline (completed 500K)

| Clip | Seed | Raw reward | Duration | Link |
| ---- | ---: | ---------: | -------: | ---- |
| best_ppo_demo.mp4 | 136505587 | 936.0 | 10.7s | [`best_ppo_demo.mp4`](best_ppo_demo.mp4) |
| ppo_demo_best_3.mp4 | 1181241943 | 933.0 | 11.2s | [`ppo_demo_best_3.mp4`](ppo_demo_best_3.mp4) |
| ppo_demo_best_2.mp4 | 107420369 | 932.9 | 11.2s | [`ppo_demo_best_2.mp4`](ppo_demo_best_2.mp4) |
| ppo_demo_limitation_1.mp4 | 1051802512 | 918.4 | 13.6s | [`ppo_demo_limitation_1.mp4`](ppo_demo_limitation_1.mp4) |
| ppo_demo_limitation_2.mp4 | 123 | 913.4 | 14.5s | [`ppo_demo_limitation_2.mp4`](ppo_demo_limitation_2.mp4) |
| ppo_demo_limitation_3.mp4 | 599310825 | 911.2 | 14.8s | [`ppo_demo_limitation_3.mp4`](ppo_demo_limitation_3.mp4) |

### SAC fast-result branch (validated 400K best checkpoint, partial run)

| Clip | Seed | Raw reward | Duration | Link |
| ---- | ---: | ---------: | -------: | ---- |
| sac_demo_best.mp4 | 136505587 | 933.7 | 5.5s | [`sac_demo_best.mp4`](sac_demo_best.mp4) |
| sac_demo_best_2.mp4 | 107420369 | 933.3 | 5.6s | [`sac_demo_best_2.mp4`](sac_demo_best_2.mp4) |
| sac_demo_best_3.mp4 | 1181241943 | 931.1 | 5.8s | [`sac_demo_best_3.mp4`](sac_demo_best_3.mp4) |
| sac_demo_limitation_1.mp4 | 1051802512 | 914.4 | 7.1s | [`sac_demo_limitation_1.mp4`](sac_demo_limitation_1.mp4) |
| sac_demo_limitation_2.mp4 | 123 | 911.0 | 7.4s | [`sac_demo_limitation_2.mp4`](sac_demo_limitation_2.mp4) |
| sac_demo_limitation_3.mp4 | 599310825 | 908.7 | 7.6s | [`sac_demo_limitation_3.mp4`](sac_demo_limitation_3.mp4) |

## Posters

Static poster frames for the featured demos are in
[`../posters/`](../posters/) (e.g. `best_ppo_demo_poster.png`).

## Interpretation

- PPO clips come from the completed 500K baseline.
- SAC clips come from the validated 400K best checkpoint of a partial run; they
  are **not** evidence of a completed 500K SAC run.
- PPO and SAC are **not** a compute-equivalent comparison.
- These clips do **not** show that CarRacing-v3 is solved.
