# Internal-to-Neutral Filename Map

_Non-prominent traceability file. Maps internal evidence filenames to neutral final-facing names._
_This file is NOT a main final-submission material and is not linked from the README._

## Videos (`final/videos/`)

| internal filename (archive/raw) | neutral filename (`final/videos/`) | role | seed | reward |
|---|---|---|---|---|
| `PPO_V9_worst_seed599310825_r911_clean.mp4` | `ppo_demo_limitation_3.mp4` | PPO completed baseline | 599310825 | 911.2 |
| `PPO_V9_worst_seed123_r913_clean.mp4` | `ppo_demo_limitation_2.mp4` | PPO completed baseline | 123 | 913.4 |
| `PPO_V9_worst_seed1051802512_r918_clean.mp4` | `ppo_demo_limitation_1.mp4` | PPO completed baseline | 1051802512 | 918.4 |
| `PPO_V9_best_seed107420369_r933_clean.mp4` | `ppo_demo_best_2.mp4` | PPO completed baseline | 107420369 | 932.9 |
| `PPO_V9_best_seed1181241943_r933_clean.mp4` | `ppo_demo_best_3.mp4` | PPO completed baseline | 1181241943 | 933.0 |
| `PPO_V9_best_seed136505587_r936_clean.mp4` | `best_ppo_demo.mp4` | PPO completed baseline | 136505587 | 936.0 |
| `SAC_V11_1_worst_seed599310825_r909_clean.mp4` | `sac_demo_limitation_3.mp4` | SAC fast-result branch | 599310825 | 908.7 |
| `SAC_V11_1_worst_seed123_r911_clean.mp4` | `sac_demo_limitation_2.mp4` | SAC fast-result branch | 123 | 911.0 |
| `SAC_V11_1_worst_seed1051802512_r914_clean.mp4` | `sac_demo_limitation_1.mp4` | SAC fast-result branch | 1051802512 | 914.4 |
| `SAC_V11_1_best_seed1181241943_r931_clean.mp4` | `sac_demo_best_3.mp4` | SAC fast-result branch | 1181241943 | 931.1 |
| `SAC_V11_1_best_seed107420369_r933_clean.mp4` | `sac_demo_best_2.mp4` | SAC fast-result branch | 107420369 | 933.3 |
| `SAC_V11_1_best_seed136505587_r934_clean.mp4` | `sac_demo_best.mp4` | SAC fast-result branch | 136505587 | 933.7 |

## Posters (`final/posters/`)

| internal filename (local_sources) | neutral filename (`final/posters/` + `final/figures/`) | role |
|---|---|---|
| `PPO_V9_best_seed136505587_r936_clean.png` | `best_ppo_demo_poster.png` | PPO best demo poster (README hero) |
| `PPO_V9_worst_seed599310825_r911_clean.png` | `ppo_limitation_poster.png` | PPO limitation poster |
| `SAC_V11_1_best_seed136505587_r934_clean.png` | `sac_demo_best_poster.png` | SAC best demo poster |
| `SAC_V11_1_worst_seed599310825_r909_clean.png` | `sac_limitation_poster.png` | SAC limitation poster |

## Logs (`final/logs/`, raw filenames preserved)

_Raw log files keep their original names (allowed raw-evidence location). Final-facing
docs cite them by neutral description; this table preserves the mapping._

| raw filename (`final/logs/`) | neutral citation (final-facing docs) |
|---|---|
| `V9_training_500k_log.txt` | "PPO completed-baseline training log" |
| `V11_1_training_log.txt` | "SAC fast-result training log" |

## Internal labels -> neutral terminology (final-facing narrative)

| internal label | neutral term (used in all final-facing docs) |
|---|---|
| `v6_full_mask` (perception mode) | "full road-mask ray-feature pipeline" |
| `V9` (PPO branch) | "PPO completed baseline" |
| `V11.1` (SAC branch) | "SAC fast-result branch" |
| `INVARIANT vs V9` | "shared 16D→64D pipeline across PPO and SAC" |
| `COMPARE5` (fixed seed set) | "fixed multi-seed evaluation set" |
| `RANDOM10` (randomized seed set) | "randomized multi-seed evaluation set" |
| 14D / 56D (V1) | NOT used — V2 real values are 16D base / 64D stacked |
