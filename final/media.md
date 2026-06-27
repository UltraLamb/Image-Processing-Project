# Media Notes

Demo videos are available as standalone MP4 files under
[`videos/`](videos/). They were extracted from the embedded outputs in the PPO
and SAC notebooks.

These videos are visual evidence only. They are not additional evaluation runs.

- PPO demo clips correspond to the **completed 500K PPO baseline**.
- SAC demo clips correspond to the **validated 400K best-checkpoint / partial
  fast-result branch**.

Do not interpret the SAC clips as 500K completion evidence, a PPO victory claim,
or solved-status evidence for CarRacing-v3.

## Video manifest

Machine-readable metadata is in
[`videos/video_manifest.csv`](videos/video_manifest.csv).
The full visual gallery and per-clip details are in
[`videos/README.md`](videos/README.md).

## Naming and traceability

Final-facing video files use neutral names (for example `best_ppo_demo.mp4`,
`sac_demo_best.mp4`, `ppo_demo_limitation_1.mp4`). The mapping from internal
evidence filenames to these neutral names is kept in
`../archive/internal_traceability/ID_MAP.md` for traceability and is not a
main final-submission material.

## Larger media

Larger demo bundles should be attached to GitHub Releases instead of being
committed directly to this repository.
