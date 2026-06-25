# GitHub Release Draft

Suggested tag: `v2-ppo-sac-feature-release`

Release title: `V2 PPO/SAC Feature-Based CarRacing-v3 Release`

## Summary

This release packages the V2 feature-based CarRacing-v3 update. It includes a
completed PPO V9 500K baseline and a SAC V11.1 validated 400K best-checkpoint /
partial fast-result branch.

## Included Repository Assets

- Revised V2 report DOCX.
- PPO and SAC notebooks with output evidence.
- Training logs.
- Figures and CSV tables.
- Static validation report.
- Media notes and release notes.

## Included Media Videos

The repository includes 12 MP4 videos under [`media/videos/`](media/videos/).
These videos were extracted from embedded notebook outputs and are visual
evidence only, not additional evaluation runs.

## Optional Release Asset Suggestion

If a smaller download package is desired, attach a ZIP of `media/videos/` as a
GitHub Release asset instead of adding larger future media files directly to the
repository.

## Limitations

- SAC V11.1 did not complete 500K.
- SAC is not claimed to beat PPO.
- The PPO/SAC comparison is not compute-equivalent.
- No raw image-input CNN policy was trained.
- CarRacing-v3 is not claimed solved.
