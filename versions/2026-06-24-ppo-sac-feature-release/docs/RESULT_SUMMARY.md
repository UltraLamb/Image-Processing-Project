# RESULT_SUMMARY.md

_Evidence-based summary parsed from the training logs on 2026-06-24. No values are
invented; anything absent is marked "not found in provided files."_

Environment: **Gymnasium CarRacing-v3** (randomized).
Perception: **mask / ray / radar visual features** (not raw-pixel CNN).

---

## PPO baseline (V9) - COMPLETED 500K

- Source log: `logs/V9_training_500k_log.txt` (5,666 lines)
- Completion: **COMPLETED 500K baseline** (eval present at 500,000; last observed step 501,760).
- Final eval @500K: **938.87 +/- 7.86**
- Best checkpoint: **939.5 @ step 480,000** (explicit in log)
- Best parsed eval: 939.53 +/- 4.09 @ 480,000
- Throughput: ~40 fps, elapsed 12417s (~3h26m)

### PPO eval checkpoints

| step    | mean reward | +/- std |
| ------: | ----------: | ------: |
| 20,000  | 293.54      | 146.56  |
| 40,000  | 310.22      | 89.79   |
| 60,000  | 236.05      | 79.57   |
| 80,000  | 381.07      | 69.73   |
| 100,000 | 358.19      | 132.66  |
| 120,000 | 467.53      | 211.29  |
| 140,000 | 648.81      | 243.53  |
| 160,000 | 721.70      | 135.85  |
| 180,000 | 505.19      | 296.11  |
| 200,000 | 769.12      | 223.36  |
| 220,000 | 505.04      | 355.49  |
| 240,000 | 335.40      | 109.84  |
| 260,000 | 824.59      | 182.66  |
| 280,000 | 849.36      | 173.34  |
| 300,000 | 832.78      | 204.18  |
| 320,000 | 780.22      | 211.17  |
| 340,000 | 810.58      | 233.17  |
| 360,000 | 768.91      | 211.34  |
| 380,000 | 857.28      | 104.10  |
| 400,000 | 784.98      | 178.68  |
| 420,000 | 780.46      | 317.26  |
| 440,000 | 934.05      | 6.67    |
| 460,000 | 931.94      | 2.33    |
| 480,000 | 939.53      | 4.09    |
| 500,000 | 938.87      | 7.86    |

---

## SAC fast result (V11.1) - 400K BEST CHECKPOINT / PARTIAL RUN

- Source log: `logs/V11_1_training_log.txt` (4,361 lines)
- Completion: **NOT a completed 500K run.** SAC fast-result run reached a best
  evaluation checkpoint at **400K** and is treated as a 400K best-checkpoint /
  partial-run result.
- Last observed training step: **418,697** (~82% of 500K per the log's ETA line).
- Best (and last) eval checkpoint: **938.51 +/- 4.88 @ 400,000**
- Steps beyond 400K have **no eval checkpoint** and are NOT treated as a validated best result.
- Explicit "Best checkpoint:" line in log: not found in provided files
- Throughput: ~36 fps, elapsed 11400s (~3h10m)
- Early stopping reflects Colab runtime limits / fast-result intent.

### SAC eval checkpoints

| step    | mean reward | +/- std |
| ------: | ----------: | ------: |
| 50,000  | 9.67        | 8.98    |
| 100,000 | 179.94      | 28.69   |
| 150,000 | 362.34      | 53.22   |
| 200,000 | 838.10      | 151.24  |
| 250,000 | 924.99      | 4.55    |
| 300,000 | 930.68      | 6.09    |
| 350,000 | 938.33      | 2.42    |
| 400,000 | 938.51      | 4.88    |

---

## Honest comparison note

PPO is a fully completed 500K baseline.

SAC is a strong but **partial** fast-result run whose headline number is the
**400K** checkpoint. Treat SAC only as a 400K checkpoint result. When comparing,
compare PPO@500K (or PPO@best) against SAC@400K-best and disclose the difference
in budget.
