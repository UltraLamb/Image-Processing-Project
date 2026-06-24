# RUN_INSTRUCTIONS.md  (safe report / eval-only use)

These notebooks are cleaned for the report. **They do not train by default.**

## What runs safely

Both notebooks ship with these flags in the Configuration cell:

```python
SAFE_MODE      = True
REPORT_ONLY    = True
EVAL_ONLY      = True
ALLOW_TRAINING = False   # training cells are skipped while this is False
```

Run order in Google Colab:

1. **Setup** - run the install cell, then *Runtime > Restart runtime* (Colab quirk).
2. **Setup** - run the Drive mount / output-path cell.
3. **Configuration** - run it. Leave `ALLOW_TRAINING = False`.
4. **Environment and Perception / Diagnostics** - safe; renders mask/radar/obs figures.
5. **Smoke Tests** - safe; quick sanity checks, no training.
6. **Model and Training Protocol** - the training cells here are guarded and will
   print `[SKIP] ...` while `ALLOW_TRAINING=False`. This is expected.
7. **Evaluation Protocol / Results** - loads saved artifacts and runs COMPARE5,
   RANDOM10, bootstrap-CI, training curve, failure taxonomy from disk.
8. **Figures and Tables for Report / Release Artifacts** - regenerate report assets.

> Evaluation / video cells use `PPO.load(path)` (no `env=`) so each eval seed is
> isolated. Do not add `env=` to eval cells.

## If you intentionally want to re-train (NOT needed for the report)

Set `ALLOW_TRAINING = True` in the Configuration cell, then run the training cell.
Training is long-running (hours on Colab GPU) and is not required to reproduce the
reported numbers, which come from the saved artifacts + logs.

## Local machine

Local shells have no Colab runtime / Drive / GPU. Use them only for static checks
(JSON/nbformat validation). Real eval/seed-isolation must be verified in Colab.
