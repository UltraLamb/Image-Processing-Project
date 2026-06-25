# V2 Media Notes

V2 demo videos are available as standalone MP4 files under
[`media/videos/`](media/videos/). They were extracted from the embedded outputs
in the PPO and SAC notebooks.

These videos are visual evidence only. They are not additional evaluation runs.
PPO V9 videos correspond to the completed 500K PPO baseline.
SAC V11.1 videos correspond to the validated 400K best-checkpoint / partial
fast-result branch.

Do not interpret the SAC videos as 500K completion evidence, a PPO victory
claim, or solved-status evidence for CarRacing-v3.

## Video Manifest

Machine-readable metadata is available in
[`media/video_manifest.csv`](media/video_manifest.csv).

| Algorithm | Label | Seed | Reward | FPS | Frames | Duration | Video |
| --------- | ----- | ---: | -----: | --: | -----: | -------: | ----- |
| PPO V9 | worst | 599310825 | 911.2 | 15 | 222 | 14.8s | [`PPO_V9_worst_seed599310825_r911_clean.mp4`](media/videos/PPO_V9_worst_seed599310825_r911_clean.mp4) |
| PPO V9 | worst | 123 | 913.4 | 15 | 217 | 14.5s | [`PPO_V9_worst_seed123_r913_clean.mp4`](media/videos/PPO_V9_worst_seed123_r913_clean.mp4) |
| PPO V9 | worst | 1051802512 | 918.4 | 15 | 204 | 13.6s | [`PPO_V9_worst_seed1051802512_r918_clean.mp4`](media/videos/PPO_V9_worst_seed1051802512_r918_clean.mp4) |
| PPO V9 | best | 107420369 | 932.9 | 15 | 168 | 11.2s | [`PPO_V9_best_seed107420369_r933_clean.mp4`](media/videos/PPO_V9_best_seed107420369_r933_clean.mp4) |
| PPO V9 | best | 1181241943 | 933.0 | 15 | 168 | 11.2s | [`PPO_V9_best_seed1181241943_r933_clean.mp4`](media/videos/PPO_V9_best_seed1181241943_r933_clean.mp4) |
| PPO V9 | best | 136505587 | 936.0 | 15 | 160 | 10.7s | [`PPO_V9_best_seed136505587_r936_clean.mp4`](media/videos/PPO_V9_best_seed136505587_r936_clean.mp4) |
| SAC V11.1 | worst | 599310825 | 908.7 | 30 | 229 | 7.6s | [`SAC_V11_1_worst_seed599310825_r909_clean.mp4`](media/videos/SAC_V11_1_worst_seed599310825_r909_clean.mp4) |
| SAC V11.1 | worst | 123 | 911.0 | 30 | 223 | 7.4s | [`SAC_V11_1_worst_seed123_r911_clean.mp4`](media/videos/SAC_V11_1_worst_seed123_r911_clean.mp4) |
| SAC V11.1 | worst | 1051802512 | 914.4 | 30 | 214 | 7.1s | [`SAC_V11_1_worst_seed1051802512_r914_clean.mp4`](media/videos/SAC_V11_1_worst_seed1051802512_r914_clean.mp4) |
| SAC V11.1 | best | 1181241943 | 931.1 | 30 | 173 | 5.8s | [`SAC_V11_1_best_seed1181241943_r931_clean.mp4`](media/videos/SAC_V11_1_best_seed1181241943_r931_clean.mp4) |
| SAC V11.1 | best | 107420369 | 933.3 | 30 | 167 | 5.6s | [`SAC_V11_1_best_seed107420369_r933_clean.mp4`](media/videos/SAC_V11_1_best_seed107420369_r933_clean.mp4) |
| SAC V11.1 | best | 136505587 | 933.7 | 30 | 166 | 5.5s | [`SAC_V11_1_best_seed136505587_r934_clean.mp4`](media/videos/SAC_V11_1_best_seed136505587_r934_clean.mp4) |

## V1 Media

The original V1 artifact package
[`../../artifacts/CarRacingV3_PPO_Final_Submission.zip`](../../artifacts/CarRacingV3_PPO_Final_Submission.zip)
contains MP4 video files for the V1 PPO-only submission.

## Future Larger Media

Larger demo bundles should be attached to GitHub Releases instead of committed
directly to this repository.
