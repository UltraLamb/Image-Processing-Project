# PPO/SAC Feature-Based CarRacing-v3 Release

This folder is the later V2 release of the CarRacing-v3 project. It preserves the
original PPO-only course submission in the repository root and adds the newer
PPO/SAC feature-based result package as a separate version.

## Version Summary

- **PPO V9:** completed 500K baseline.
- **SAC V11.1:** partial fast-result branch with validated 400K best checkpoint.
- **Environment:** Gymnasium `CarRacing-v3`.
- **Policy type:** Stable-Baselines3 `MlpPolicy`.
- **Input representation:** compact mask/ray/radar features, not raw-pixel CNN.
- **Observation size:** 16D base observation, stacked to 64D with 4 frames.

## Headline Results

| Branch | Status | Validated eval | Best eval | Last observed step |
|---|---|---:|---:|---:|
| PPO V9 | completed 500K baseline | 938.87 +/- 7.86 @ 500,000 | 939.53 +/- 4.09 @ 480,000 | 501,760 |
| SAC V11.1 | 400K best-checkpoint / partial-run fast result | 938.51 +/- 4.88 @ 400,000 | 938.51 +/- 4.88 @ 400,000 | 418,697 |

The SAC result is not a completed 500K run and is not presented as beating PPO.
It is evidence that the same compact feature pipeline can support a strong
off-policy fast-result branch under the provided Colab/runtime constraints.

## Contents

- [`report/`](report/) - revised V2 DOCX report.
- [`notebooks/`](notebooks/) - PPO and SAC notebooks with output evidence kept.
- [`logs/`](logs/) - original PPO/SAC training logs used for headline metrics.
- [`figures/`](figures/) - final report figures generated from provided evidence.
- [`tables/`](tables/) - CSV summaries and checkpoint tables.
- [`docs/`](docs/) - result summary, run instructions, and asset manifest.
- [`validation/`](validation/) - static validation report.
- [`tools/`](tools/) - release build and validation scripts referenced by docs.

## How To Read The Evidence

Use [`docs/RESULT_SUMMARY.md`](docs/RESULT_SUMMARY.md) as the main source for
headline metrics. It is backed by the logs in [`logs/`](logs/). Notebook output
tables are secondary evidence for tested-seed generalization and bootstrap
summaries.

## Reproduction Notes

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
- PPO and SAC are not a perfectly compute-equivalent ablation.
- No raw-pixel CNN policy was trained in this V2 package.
- The results do not prove that CarRacing-v3 is solved.
