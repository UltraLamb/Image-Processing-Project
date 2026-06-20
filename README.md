# CarRacing-v3 PPO with Road-Mask Ray Features

Student: Joe

Student ID: 1103820

## Summary

This project trains a PPO agent for Gymnasium CarRacing-v3 using compact road-mask ray features. The notebook converts each RGB frame into a HSV road mask, casts dynamic ray distances, stacks four 14D observations into a 56D vector, and trains Stable-Baselines3 PPO with MlpPolicy for 500,000 timesteps.

This repository is the final GitHub submission package for the project.

## Main Results

- COMPARE5 mean raw reward: 609.1
- RANDOM10 mean raw reward: 614.1
- Best observed raw reward: 929.7
- Important limitation: some seeds still fail early, so the method is promising but not uniformly robust.

## Repository Contents

- `notebooks/CarRacingV3_PPO_Final_Submission.ipynb`: clean Colab notebook.
- `report/CarRacingV3_PPO_Final_Report.tex`: IEEE-style LaTeX source.
- `report/CarRacingV3_PPO_Final_Report.pdf`: compiled IEEE-format report.
- `slides/CarRacingV3_PPO_Final_Presentation_REBUILT.pptx`: final class presentation.
- `artifacts/CarRacingV3_PPO_Final_Submission.zip`: saved model, VecNormalize statistics, evaluation data, and videos.
- `tables/`: evaluation CSV files.
- `figures/`: reward chart and extracted video evidence frames.
- `DATASET.md`: dataset/environment notes.
- `requirements.txt`: Python dependencies.

## Reproduction Path

Use the notebook for the executable workflow. The artifact zip contains the saved model-related files and videos used for final reporting, so the reported evaluation can be inspected without retraining.

No external dataset is used; see `DATASET.md` for the environment-generated data description.

## Installation

In Google Colab, run the first notebook cell. Locally, install:

```bash
pip install "gymnasium[box2d]" "stable-baselines3>=2.5.0" opencv-python-headless numpy pandas torch matplotlib
```

Linux/Colab may also need `swig`, `build-essential`, and `ffmpeg`.

## GitHub Link

https://github.com/UltraLamb/CarRacingV3-PPO-RayFeatures
