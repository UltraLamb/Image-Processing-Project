# GitHub Release Draft

DRAFT — DO NOT PUBLISH YET

Publish only after ALL of the following are true:

1. The repository has been renamed to `Image-Processing-Project`.
2. The final IEEE-style report PDF has been compiled successfully (locally or in
   Overleaf) and placed at `final/report/Image_Processing_Project_V2_IEEE_Report.pdf`.
3. All final-facing links are verified.
4. The user explicitly approves publication.

Suggested tag: `v2-final-image-processing-project`
Release title: `V2 Final Submission — Image Processing Project`

## Summary

This draft release describes the final V2 course-facing package for:

**Image Processing Project**

**Feature-Based Image Processing and Reinforcement Learning for CarRacing-v3**

The main contribution is an image-processing-derived compact visual feature
representation. PPO and SAC are downstream evaluation methods for that
representation.

## Included Repository Assets (final-facing paths)

- Final IEEE-style report: [`final/report/Image_Processing_Project_V2_IEEE_Report.pdf`](report/Image_Processing_Project_V2_IEEE_Report.pdf)
- Overleaf / LaTeX package: [`final/overleaf/Image_Processing_Project_Overleaf_Package.zip`](overleaf/Image_Processing_Project_Overleaf_Package.zip)
- Final presentation PDF: [`final/slides/Image_Processing_Project_Final_Presentation.pdf`](slides/Image_Processing_Project_Final_Presentation.pdf)
- Final presentation PPTX: [`final/slides/Image_Processing_Project_Final_Presentation.pptx`](slides/Image_Processing_Project_Final_Presentation.pptx)
- PPO and SAC notebooks with saved output evidence: [`final/notebooks/`](notebooks/)
- Demo videos and video manifest: [`final/videos/`](videos/)

## Demo Videos

The repository includes 12 MP4 videos under [`final/videos/`](videos/). These
videos are qualitative evidence extracted from notebook outputs, not additional
evaluation runs. The final presentation uses poster frames plus links to the
media folder and [`final/videos/video_manifest.csv`](videos/video_manifest.csv)
rather than relying on embedded playable videos.

## Headline Results

| Branch | Status | Validated eval | Best parsed eval |
| ------ | ------ | -------------- | ---------------- |
| PPO completed baseline | Completed 500K baseline | 938.87 +/- 7.86 @ 500,000 | 939.53 +/- 4.09 @ 480,000 |
| SAC fast-result branch | Partial 400K best-checkpoint / fast-result branch | 938.51 +/- 4.88 @ 400,000 | 938.51 +/- 4.88 @ 400,000 |

PPO and SAC share the same 16D base / 64D temporally stacked visual feature
pipeline; only the downstream policy optimization method changes.

## Limitations

- The SAC fast-result branch did not complete 500K.
- SAC is not claimed to beat PPO.
- The PPO/SAC comparison is not compute-equivalent.
- No raw image-input CNN policy was trained in this submission.
- CarRacing-v3 is not claimed to be solved.
