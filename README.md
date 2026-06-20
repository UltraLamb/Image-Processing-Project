# CarRacing-v3 PPO with Road-Mask Ray Features

Student: Joe

Student ID: 1103820

## Summary

This project trains a PPO agent for Gymnasium CarRacing-v3 using compact road-mask ray features. The notebook converts each RGB frame into a HSV road mask, casts dynamic ray distances, stacks four 14D observations into a 56D vector, and trains Stable-Baselines3 PPO with MlpPolicy for 500,000 timesteps.

## Main Results

- COMPARE5 mean raw reward: 609.1
- RANDOM10 mean raw reward: 614.1
- Best observed raw reward: 929.7
- Important limitation: some seeds still fail early, so the method is promising but not uniformly robust.

## Repository Contents

- `notebooks/CarRacingV3_PPO_Final_Submission.ipynb`: clean Colab notebook.
- `report/CarRacingV3_PPO_Final_Report.tex`: IEEE LaTeX source (compile in Overleaf).
- `report/CarRacingV3_PPO_Final_Report.pdf`: compiled IEEE-format report.
- `report/CarRacingV3_PPO_Final_Report.docx`: Word backup copy.
- `slides/CarRacingV3_PPO_Final_Presentation.pptx`: class presentation.
- `tables/`: evaluation CSV files.
- `figures/`: reward chart and extracted video evidence frames.
- `DATASET.md`: dataset/environment notes.
- `requirements.txt`: Python dependencies.

## Installation

In Google Colab, run the first notebook cell. Locally, install:

```bash
pip install "gymnasium[box2d]" "stable-baselines3>=2.5.0" opencv-python-headless numpy pandas torch matplotlib
```

Linux/Colab may also need `swig`, `build-essential`, and `ffmpeg`.

## GitHub Link

https://github.com/UltraLamb/CarRacingV3-PPO-RayFeatures
