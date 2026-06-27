# Deployment and Rename Guide

Manual steps to publish the cleaned repository and submit the course link. None of
this is automated — run it yourself after reviewing the working tree.

The local folder `github_repo/` is already a git working tree with a remote at
`origin/main` (the current repo name is `CarRacingV3-PPO-RayFeatures`). The
restructure into `final/` + `archive/` is currently **uncommitted**.

## 1. Review the changes

```bash
cd github_repo
git status
git add -A
git status            # confirm final/, archive/, README.md, etc. are staged
```

## 2. Commit and push

```bash
git commit -m "Restructure into final/ + archive/; 15-slide deck; neutral labels"
git push origin main
```

If you prefer a clean slate instead of pushing local history:

- **Option A (web UI):** on GitHub, delete the old top-level folders and upload
  the cleaned `final/`, `archive/`, `README.md`, `requirements.txt`, `DATASET.md`.
- **Option B (fresh clone):** `git clone` the remote into a new folder, copy the
  cleaned `github_repo/` contents over it, then `git add -A && commit && push`.

## 3. Rename the repository (required before sharing the link)

GitHub → repository **Settings** → **Repository name** → rename to:

```
Image-Processing-Project
```

Then update your local remote:

```bash
git remote set-url origin https://github.com/UltraLamb/Image-Processing-Project.git
```

## 4. Polish the GitHub "About" panel (portfolio quality)

- Description: `Feature-based image processing + RL (PPO/SAC) for CarRacing-v3`
- Topics: `image-processing`, `reinforcement-learning`, `ppo`, `sac`,
  `carracing`, `gymnasium`, `opencv`, `feature-engineering`
- No website needed.

## 5. Compile the report PDF (pending)

`pdflatex` is not available locally, so the IEEE PDF must be compiled in Overleaf:

1. Upload the contents of `final/overleaf/Image_Processing_Project_Overleaf_Package.zip`
   to a new Overleaf project (compiler: pdfLaTeX, main file: `main.tex`).
2. Download the PDF and save it as
   `final/report/Image_Processing_Project_V2_IEEE_Report.pdf` **and** into the
   upload package folder.
3. Commit and push the report PDF.

## 6. Submit to the course

1. Confirm `https://github.com/UltraLamb/Image-Processing-Project` opens.
2. Upload the final presentation (`Image_Processing_Project_Final_Presentation.pptx`
   / `.pdf`) and the GitHub link to the course platform.

## 7. (Optional) Release / tag — do NOT publish until approved

See `final/github_release_draft.md`. Only after the rename, the compiled report
PDF, verified links, and your approval:

```bash
git tag v2-final-image-processing-project
git push origin v2-final-image-processing-project
```
