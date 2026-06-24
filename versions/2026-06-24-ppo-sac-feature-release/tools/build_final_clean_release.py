#!/usr/bin/env python3
"""
build_final_clean_release.py
============================
Turns the two source CarRacing notebooks + their training logs into a clean,
presentation-ready release under CarRacing_Final_Clean_Release/.

SAFETY: This script NEVER runs training, evaluation, or notebooks. It only
reads/copies files, parses logs, and writes cleaned notebook copies + docs.
Originals are never modified.

Run from anywhere:  python build_final_clean_release.py
"""
import os
import re
import json
import shutil
import datetime

import nbformat

# ----------------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
RELEASE_ROOT = os.path.dirname(HERE)                 # CarRacing_Final_Clean_Release/
REPO_ROOT = os.path.dirname(RELEASE_ROOT)            # project root

SRC_PPO_NB = os.path.join(REPO_ROOT, "completed_run_evidence", "V9_CarRacing_PPO_Colab.ipynb")
SRC_SAC_NB = os.path.join(REPO_ROOT, "completed_run_evidence", "V11_1_CarRacing_SAC_Fast_Result.ipynb")
SRC_PPO_LOG = os.path.join(REPO_ROOT, "evidence_logs", "V9_training_500k_log.txt")
SRC_SAC_LOG = os.path.join(REPO_ROOT, "evidence_logs", "V11.1_training_500k_log.txt")

NB_DIR = os.path.join(RELEASE_ROOT, "notebooks")
LOG_DIR = os.path.join(RELEASE_ROOT, "logs")
DOC_DIR = os.path.join(RELEASE_ROOT, "docs")

OUT_PPO_NB = os.path.join(NB_DIR, "Final_PPO_Baseline_CarRacing_v3.ipynb")
OUT_SAC_NB = os.path.join(NB_DIR, "Final_SAC_Fast_Result_CarRacing_v3.ipynb")
OUT_PPO_LOG = os.path.join(LOG_DIR, "V9_training_500k_log.txt")
OUT_SAC_LOG = os.path.join(LOG_DIR, "V11_1_training_log.txt")

for d in (NB_DIR, LOG_DIR, DOC_DIR):
    os.makedirs(d, exist_ok=True)

TODAY = datetime.date.today().isoformat()


# ----------------------------------------------------------------------------
# 1. Log parsing  (evidence-based, no invention)
# ----------------------------------------------------------------------------
def parse_log(path):
    """Pull eval checkpoints + completion evidence from a training log."""
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()

    evals = []
    for m in re.finditer(r"Eval num_timesteps=(\d+),\s*episode_reward=([\d.]+)\s*\+/-\s*([\d.]+)", text):
        evals.append({"step": int(m.group(1)),
                      "mean": float(m.group(2)),
                      "std": float(m.group(3))})

    # max observed training step
    steps = [int(s) for s in re.findall(r"total_timesteps\s*[|=]\s*(\d+)", text)]
    max_step = max(steps) if steps else None

    # last fps / elapsed
    fps_all = re.findall(r"\bfps\s*[|=]?\s*\|?\s*(\d+)", text)
    elapsed_all = re.findall(r"time_elapsed\s*[|=]?\s*\|?\s*(\d+)", text)
    last_fps = int(fps_all[-1]) if fps_all else None
    last_elapsed = int(elapsed_all[-1]) if elapsed_all else None

    # explicit best line (PPO log has it; SAC may not)
    best_line = re.search(r"Best checkpoint:\s*([\d.]+)\s*at step\s*([\d,]+)", text)
    best_explicit = None
    if best_line:
        best_explicit = {"mean": float(best_line.group(1)),
                         "step": int(best_line.group(2).replace(",", ""))}

    # ETA progress line: "[ETA] X/Y (P%)"
    eta = re.findall(r"\[ETA\]\s*([\d,]+)/([\d,]+)\s*\(([\d.]+)%\)", text)
    last_pct = float(eta[-1][2]) if eta else None

    # best eval among parsed checkpoints
    best_eval = max(evals, key=lambda e: e["mean"]) if evals else None

    # completion: a 500K eval present OR 100% ETA OR max_step >= 500000
    target = 500_000
    reached_500k_eval = any(e["step"] >= target for e in evals)
    completed = bool(reached_500k_eval or (last_pct is not None and last_pct >= 99.9)
                     or (max_step is not None and max_step >= target))

    return {
        "path": path,
        "n_lines": text.count("\n") + 1,
        "evals": evals,
        "best_eval": best_eval,
        "best_explicit": best_explicit,
        "max_step": max_step,
        "last_fps": last_fps,
        "last_elapsed_s": last_elapsed,
        "last_pct": last_pct,
        "completed_500k": completed,
        "target": target,
    }


def fmt_hms(seconds):
    if seconds is None:
        return "not found in provided files"
    h = seconds // 3600
    m = (seconds % 3600) // 60
    return f"{seconds}s (~{h}h{m:02d}m)"


# ----------------------------------------------------------------------------
# 2. Notebook cleaning helpers
# ----------------------------------------------------------------------------
def md(text):
    return nbformat.v4.new_markdown_cell(text)


def first_line(cell):
    src = cell.source if isinstance(cell.source, str) else "".join(cell.source)
    for ln in src.splitlines():
        if ln.strip():
            return ln
    return ""


def cell_src(cell):
    return cell.source if isinstance(cell.source, str) else "".join(cell.source)


# --- second-pass polish: neutralize version-history / crash wording -----------
# Substring replacements applied to every cell. Order matters (longest first).
COMMON_REPLACEMENTS = [
    ("Results are NOT directly comparable to V8.2.",
     "Perception, reward, and training profile were co-designed (no per-change ablation here)."),
    (" (V9 simplified from V8.2's 10)", ""),
    (" (V9: more responsive than V8.2 at 0.65)", ""),
    ("V8.2's ", "the earlier "),  # markdown figure note: drop version label
    ('model.save(f"{CKPT_DIR}/model_crash")',
     'model.save(f"{CKPT_DIR}/model_interrupted")'),
    ('train_vec.save(f"{CKPT_DIR}/vecnorm_crash.pkl")',
     'train_vec.save(f"{CKPT_DIR}/vecnorm_interrupted.pkl")'),
    ("Config audit passed. Ready for RESUME (Appendix).", "Config audit passed."),
]

PPO_REPLACEMENTS = [
    ('RUN_MODE = "OFFICIAL_500K"  # SMOKE_ONLY | RAPID_50K | OFFICIAL_500K | EVAL_ONLY | RESUME',
     'RUN_MODE = "EVAL_ONLY"  # EVAL_ONLY (default: report/eval only) | SMOKE_ONLY | RAPID_50K | OFFICIAL_500K'),
]

SAC_REPLACEMENTS = [
    ('RUN_MODE = "EVAL_ONLY"  # SMOKE_ONLY | RAPID_50K | RAPID_120K | OFFICIAL_300K | OFFICIAL_500K | RESUME | EVAL_ONLY  (V11 default SMOKE_ONLY; do not set a training mode until smoke PASS)',
     'RUN_MODE = "EVAL_ONLY"  # EVAL_ONLY (default: report/eval only) | SMOKE_ONLY | RAPID_50K | OFFICIAL_500K'),
    # path-safety: keep the asserts, neutralize the version-history comments
    ("# V10 SAC: separate output root. NEVER write into V9 dirs or evidence dirs.",
     "# Separate output root for this experiment. NEVER write into other experiment folders or evidence dirs."),
    ("# V10.5 must NOT write into the running V10 official run dirs either:",
     "# Must NOT write into other experiments' run dirs either:"),
    ("# V11 must NOT write into the frozen V10.5 dirs either:",
     "# (other prior experiment dirs are also forbidden write targets):"),
    ("# V11.1 must NOT write into the frozen V11 dirs (it only READS them for resume):",
     "# (this run only READS any prior dirs, it never writes into them):"),
    ("# --- V10 path safety:", "# --- path safety:"),
    ("# V10 root must neither be inside a forbidden dir nor contain it.",
     "# This run's root must neither be inside a forbidden dir nor contain it."),
    ("# V9 root must not equal or nest the V10 root (and vice versa).",
     "# The PPO baseline root must not equal or nest this run's root (and vice versa)."),
    ('print(f"  V11 {_name:13s}= {_p}")', 'print(f"  {_name:13s}= {_p}")'),
    ('print("  [OK] V11 paths do not overwrite V9/V10/V10.5/evidence/output dirs.")',
     'print("  [OK] output paths do not overwrite the PPO baseline, other experiments, evidence, or output dirs.")'),
    ("CONFIGURATION AUDIT (V11 SAC)", "CONFIGURATION AUDIT (SAC)"),
    ("(V11 SAC profile)", "(SAC profile)"),
    # final report: drop version label, reword the misleading "no result" note
    ("CARRACING-V3 SAC V11 -- FINAL REPORT", "CARRACING-V3 SAC -- FINAL REPORT"),
    ("V11 SAC has NO official result until OFFICIAL_500K training + ",
     "SAC headline is the 400K best checkpoint (fast-result, partial run; not a completed 500K run). "),
    ("COMPARE5/RANDOM10 eval complete. Any V9 numbers are the locked PPO baseline.",
     "PPO (V9) remains the completed 500K baseline."),
    ("# V9 numbers are the locked PPO baseline only, never V10 SAC results.",
     "# V9 numbers are the PPO baseline only, never SAC results."),
    ("feature observations (V11)", "feature observations"),
]

_V82_COMMENT = re.compile(r"[ \t]*#[^\n]*V8\.2[^\n]*")


def polish_source(src, extra_replacements, is_code):
    if is_code:
        src = _V82_COMMENT.sub("", src)  # drop leftover "# V8.2: ..." comments
    for find, repl in COMMON_REPLACEMENTS + list(extra_replacements):
        src = src.replace(find, repl)
    return src


def has_learn(cell):
    # ponytail: strip inline/full-line comments before matching so `.learn(`
    # inside a comment (e.g. "# ready for model.learn(...)") is not a false hit.
    if cell.cell_type != "code":
        return False
    for line in cell_src(cell).splitlines():
        code = line.split("#", 1)[0]
        if ".learn(" in code:
            return True
    return False


def guard_training_cell(cell):
    """Wrap a training cell body so it is disabled unless ALLOW_TRAINING=True."""
    body = cell_src(cell)
    header = (
        "# === OPTIONAL TRAINING CELL - DISABLED BY DEFAULT (REPORT_ONLY) ===\n"
        "# This final notebook ships in REPORT_ONLY / EVAL_ONLY mode. Training is\n"
        "# long-running and is NOT required to reproduce the reported results from\n"
        "# the saved artifacts. To actually train, set ALLOW_TRAINING = True in the\n"
        "# Configuration cell, then re-run this cell.\n"
        "if globals().get('ALLOW_TRAINING', False):\n"
    )
    indented = "\n".join(("    " + ln) if ln.strip() else "" for ln in body.splitlines())
    footer = (
        "\nelse:\n"
        "    print('[SKIP] Training disabled (ALLOW_TRAINING=False). "
        "Final notebook is in REPORT_ONLY mode.')\n"
    )
    cell.source = header + indented + footer
    return cell


SAFE_MODE_BLOCK = """

# === FINAL CLEAN RELEASE - SAFE MODE FLAGS (added during cleanup) ===
# This notebook ships report/eval-only. Training cells are guarded by these.
SAFE_MODE     = True    # master safety switch for the final release
REPORT_ONLY   = True    # build figures/tables/report from saved artifacts only
EVAL_ONLY     = True    # run evaluation from saved artifacts only
ALLOW_TRAINING = False  # set True ONLY if you intentionally want to re-train
"""


def clean_notebook(src_path, title, subtitle, overview_md, provenance_md,
                   remove_first_line_substrings, remove_md_header_substrings,
                   extra_replacements=()):
    """Produce a cleaned nbformat notebook from a source notebook."""
    nb = nbformat.read(src_path, as_version=4)
    removed = []
    kept_training = []
    provenance_placed = False

    new_cells = []
    for cell in nb.cells:
        fl = first_line(cell)
        src = cell_src(cell)

        # --- drop clearly dev-only cells ---
        drop = False
        if cell.cell_type == "code":
            for sub in remove_first_line_substrings:
                if sub.lower() in fl.lower():
                    drop = True
                    removed.append(fl.strip()[:70])
                    break
        if cell.cell_type == "markdown" and src.strip():
            hdr = src.strip().splitlines()[0].strip()
            for sub in remove_md_header_substrings:
                if sub.lower() in hdr.lower():
                    drop = True
                    removed.append("MD: " + hdr[:60])
                    break
        if drop:
            continue

        # --- replace original title cell (index-0 style) with clean overview ---
        if cell.cell_type == "markdown" and src.lstrip().startswith("# CarRacing"):
            continue  # original title replaced below; skip it

        # --- rename / repurpose old section headers to clean taxonomy ---
        if cell.cell_type == "markdown":
            stripped = src.strip()
            # Appendix becomes the full Provenance and Limitations section (in place)
            if stripped == "## Appendix" or stripped.startswith("## Appendix\n"):
                cell.source = provenance_md
                provenance_placed = True
            else:
                rename = {
                    "## Training": "## Model and Training Protocol",
                    "## Evaluation & Results": "## Evaluation Protocol",
                    "## Package & Report": "## Release Artifacts",
                }
                for old, new in rename.items():
                    if stripped == old or stripped.startswith(old + "\n"):
                        cell.source = src.replace(old, new, 1)
                        break

        # --- inject SAFE_MODE flags into the central config cell ---
        if cell.cell_type == "code" and "Central configuration" in fl:
            cell.source = cell_src(cell).rstrip() + "\n" + SAFE_MODE_BLOCK

        # --- guard training cells ---
        if has_learn(cell):
            guard_training_cell(cell)
            kept_training.append(fl.strip()[:60])

        new_cells.append(cell)

    # Build clean front matter + section anchors
    title_cell = md(
        f"# {title}\n\n"
        f"**{subtitle}**\n\n"
        f"_Project: Visual Reinforcement Learning for Randomized CarRacing-v3 - "
        f"PPO Baseline, Generalization, and Speed._\n\n"
        f"---\n\n"
        f"> **SAFE MODE / REPORT-ONLY.** This is a cleaned final-release notebook. "
        f"Training cells are disabled by default (`ALLOW_TRAINING=False`). "
        f"It is intended for evaluation, figure/table generation, and the written "
        f"report. See the Configuration cell for the safety flags.\n\n"
        + overview_md
    )

    # Insert lightweight section headers before key cells (content-based, no reorder)
    def insert_before(cells, match_fn, header_md):
        out = []
        inserted = False
        for c in cells:
            if (not inserted) and match_fn(c):
                out.append(md(header_md))
                inserted = True
            out.append(c)
        return out

    cells = new_cells
    cells = insert_before(cells,
                          lambda c: c.cell_type == "code" and "Install dependencies" in first_line(c),
                          "## Setup\n\nInstall dependencies and mount Drive / set output paths. "
                          "In Colab, run the install cell first, then restart the runtime.")
    cells = insert_before(cells,
                          lambda c: c.cell_type == "code" and "Central configuration" in first_line(c),
                          "## Configuration\n\nAll knobs live in one place. The final release adds "
                          "`SAFE_MODE` / `REPORT_ONLY` / `EVAL_ONLY` / `ALLOW_TRAINING` flags so the "
                          "notebook runs report/eval-only by default.")
    cells = insert_before(cells,
                          lambda c: c.cell_type == "code" and "road mask" in cell_src(c).lower(),
                          "## Environment and Perception\n\nGymnasium **CarRacing-v3** with a "
                          "mask/ray/radar visual-feature pipeline (HSV road mask -> morphological "
                          "cleanup -> connected components -> ray casting). This is feature-based "
                          "visual RL, **not** a raw-pixel CNN.")
    cells = insert_before(cells,
                          lambda c: c.cell_type == "markdown" and "## Provenance and Limitations" in cell_src(c),
                          "## Figures and Tables for Report\n\nThe cells above generate the "
                          "diagnostics, COMPARE5 / RANDOM10 evaluation, bootstrap-CI distribution, "
                          "training curve, and failure taxonomy used as figures/tables in the report.")

    if not provenance_placed:
        cells.append(md(provenance_md))
    nb.cells = [title_cell] + cells

    # second-pass polish: neutralize version-history / crash wording everywhere
    for c in nb.cells:
        c.source = polish_source(cell_src(c), extra_replacements, c.cell_type == "code")

    # normalise notebook metadata (minor 5 so new cell ids are valid)
    nb.metadata.setdefault("language_info", {"name": "python"})
    nb.nbformat = 4
    nb.nbformat_minor = max(getattr(nb, "nbformat_minor", 0) or 0, 5)
    for k, c in enumerate(nb.cells):  # minor>=5 requires a cell id on every cell
        if not c.get("id"):
            c["id"] = f"cell{k:03d}"
    nbformat.validate(nb)
    return nb, removed, kept_training


# ----------------------------------------------------------------------------
# 3. Parse logs
# ----------------------------------------------------------------------------
ppo = parse_log(SRC_PPO_LOG)
sac = parse_log(SRC_SAC_LOG)

# ----------------------------------------------------------------------------
# 4. Copy logs (rename SAC -> training_log; evidence shows it did not finish 500k)
# ----------------------------------------------------------------------------
shutil.copyfile(SRC_PPO_LOG, OUT_PPO_LOG)
shutil.copyfile(SRC_SAC_LOG, OUT_SAC_LOG)

# ----------------------------------------------------------------------------
# 5. Clean both notebooks
# ----------------------------------------------------------------------------
ppo_overview = (
    "## Project Overview\n\n"
    "This notebook is the **PPO baseline** for randomized CarRacing-v3. PPO is "
    "trained from scratch with an `MlpPolicy` over engineered visual features "
    "(road mask + radar rays), then evaluated for generalization (COMPARE5 fixed "
    "seeds, RANDOM10 random seeds) with bootstrap confidence intervals on the raw "
    "reward.\n"
)
ppo_provenance = (
    "## Provenance and Limitations\n\n"
    "**Provenance.** Cleaned from source `V9_CarRacing_PPO_Colab.ipynb` "
    f"(release built {TODAY}). Development-history, resume-training, and debug "
    "appendices were removed; training cells were guarded behind `ALLOW_TRAINING`. "
    "Functional setup / perception / evaluation / reporting code is preserved.\n\n"
    "**Result (from `logs/V9_training_500k_log.txt`).** Completed 500K-step PPO "
    f"baseline: eval@500K = {ppo['evals'][-1]['mean']:.2f} +/- {ppo['evals'][-1]['std']:.2f}; "
    f"best checkpoint {ppo['best_explicit']['mean'] if ppo['best_explicit'] else float('nan'):.1f} "
    f"@ step {ppo['best_explicit']['step'] if ppo['best_explicit'] else 'n/a'}.\n\n"
    "**Limitations.** Single training seed for the curve; generalization is "
    "evaluated but per-seed variance exists (see RANDOM10). Numbers are read from "
    "the training log, not re-run here. See `docs/RESULT_SUMMARY.md`.\n"
)

sac_overview = (
    "## Project Overview\n\n"
    "This notebook is the **SAC fast-result branch** for randomized CarRacing-v3 "
    "(speed-first single-env configuration). SAC is trained from scratch over the "
    "same engineered visual features as the PPO baseline and evaluated with the "
    "same COMPARE5 / RANDOM10 / bootstrap-CI protocol.\n\n"
    "> **Status: 400K best-checkpoint / partial run.** This SAC fast-result run "
    "reached a best evaluation checkpoint at **400K** and is **not** treated as a "
    "completed 500K run (the log progresses to ~83% with no eval checkpoint beyond "
    "400K). Early stopping reflects Colab runtime limits / fast-result intent.\n"
)
sac_provenance = (
    "## Provenance and Limitations\n\n"
    "**Provenance.** Cleaned from source `V11_1_CarRacing_SAC_Fast_Result.ipynb` "
    f"(release built {TODAY}). The FAST_RESULT resume cell, speed/fps probes, "
    "emergency-recovery cell, development-history and old-version narrative were "
    "removed; the remaining training cells were guarded behind `ALLOW_TRAINING`. "
    "Functional setup / perception / evaluation / reporting code is preserved.\n\n"
    "**Result (from `logs/V11_1_training_log.txt`).** SAC fast-result run reached a "
    "best evaluation checkpoint at 400K "
    f"({sac['best_eval']['mean']:.2f} +/- {sac['best_eval']['std']:.2f}) and is not "
    "treated as a completed 500K run. Last observed training step ~"
    f"{sac['max_step']:,} (~{sac['last_pct']:.0f}% of 500K) with no eval checkpoint "
    "beyond 400K.\n\n"
    "**Limitations.** Partial run; the 400K checkpoint is the main SAC result. Steps "
    "beyond 400K are NOT a validated best (no later eval). Numbers are read from the "
    "training log, not re-run here. See `docs/RESULT_SUMMARY.md`.\n"
)

ppo_nb, ppo_removed, ppo_train = clean_notebook(
    SRC_PPO_NB,
    title="CarRacing-v3 PPO Baseline - Final Clean Notebook",
    subtitle="PPO (MlpPolicy) on engineered visual features - completed 500K baseline",
    overview_md=ppo_overview,
    provenance_md=ppo_provenance,
    remove_first_line_substrings=["Development History", "RESUME mode"],
    remove_md_header_substrings=[],
    extra_replacements=PPO_REPLACEMENTS,
)

sac_nb, sac_removed, sac_train = clean_notebook(
    SRC_SAC_NB,
    title="CarRacing-v3 SAC Fast Result - Final Clean Notebook",
    subtitle="SAC fast-result branch - 400K best checkpoint (partial run, not 500K)",
    overview_md=sac_overview,
    provenance_md=sac_provenance,
    remove_first_line_substrings=["Development History", "RESUME mode", "RESUME_FAST",
                                  "SPEED PROBE", "ENV-ONLY"],
    remove_md_header_substrings=["resume + probes"],
    extra_replacements=SAC_REPLACEMENTS,
)

nbformat.write(ppo_nb, OUT_PPO_NB)
nbformat.write(sac_nb, OUT_SAC_NB)


# ----------------------------------------------------------------------------
# 6. Docs
# ----------------------------------------------------------------------------
def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def eval_table(rec):
    rows = ["| step | mean reward | +/- std |", "|---:|---:|---:|"]
    for e in rec["evals"]:
        rows.append(f"| {e['step']:,} | {e['mean']:.2f} | {e['std']:.2f} |")
    return "\n".join(rows)


result_summary = f"""# RESULT_SUMMARY.md

_Evidence-based summary parsed from the training logs on {TODAY}. No values are
invented; anything absent is marked "not found in provided files."_

Environment: **Gymnasium CarRacing-v3** (randomized).
Perception: **mask / ray / radar visual features** (not raw-pixel CNN).

---

## PPO baseline (V9) - COMPLETED 500K

- Source log: `logs/V9_training_500k_log.txt` ({ppo['n_lines']:,} lines)
- Completion: **COMPLETED 500K baseline** (eval present at 500,000; last observed step {ppo['max_step']:,}).
- Final eval @500K: **{ppo['evals'][-1]['mean']:.2f} +/- {ppo['evals'][-1]['std']:.2f}**
- Best checkpoint: **{ppo['best_explicit']['mean']:.1f} @ step {ppo['best_explicit']['step']:,}** (explicit in log)
- Best parsed eval: {ppo['best_eval']['mean']:.2f} +/- {ppo['best_eval']['std']:.2f} @ {ppo['best_eval']['step']:,}
- Throughput: ~{ppo['last_fps']} fps, elapsed {fmt_hms(ppo['last_elapsed_s'])}

### PPO eval checkpoints
{eval_table(ppo)}

---

## SAC fast result (V11.1) - 400K BEST CHECKPOINT / PARTIAL RUN

- Source log: `logs/V11_1_training_log.txt` ({sac['n_lines']:,} lines)
- Completion: **NOT a completed 500K run.** SAC fast-result run reached a best
  evaluation checkpoint at **400K** and is treated as a 400K best-checkpoint /
  partial-run result.
- Last observed training step: **{sac['max_step']:,}** (~{sac['last_pct']:.0f}% of 500K per the log's ETA line).
- Best (and last) eval checkpoint: **{sac['best_eval']['mean']:.2f} +/- {sac['best_eval']['std']:.2f} @ {sac['best_eval']['step']:,}**
- Steps beyond 400K have **no eval checkpoint** and are NOT treated as a validated best result.
- Explicit "Best checkpoint:" line in log: {"present" if sac['best_explicit'] else "not found in provided files"}
- Throughput: ~{sac['last_fps']} fps, elapsed {fmt_hms(sac['last_elapsed_s'])}
- Early stopping reflects Colab runtime limits / fast-result intent.

### SAC eval checkpoints
{eval_table(sac)}

---

## Honest comparison note

PPO is a fully completed 500K baseline. SAC is a strong but **partial** fast-result
run whose headline number is the **400K** checkpoint. Do not present SAC as a
completed 500K run. When comparing, compare PPO@500K (or PPO@best) against
SAC@400K-best and disclose the difference in budget.
"""
write(os.path.join(DOC_DIR, "RESULT_SUMMARY.md"), result_summary)

readme = f"""# CarRacing Final Clean Release

Presentation-ready final release for the project
**"Visual Reinforcement Learning for Randomized CarRacing-v3: PPO Baseline,
Generalization, and Speed."**

Two cleaned notebooks (PPO baseline + SAC fast result), the supporting training
logs, an evidence-based result summary, and starter notes for the written report
and slides.

## Layout

```
CarRacing_Final_Clean_Release/
  notebooks/
    Final_PPO_Baseline_CarRacing_v3.ipynb   # PPO baseline, completed 500K
    Final_SAC_Fast_Result_CarRacing_v3.ipynb# SAC fast result, 400K best (partial)
  logs/
    V9_training_500k_log.txt                 # PPO training log (unmodified copy)
    V11_1_training_log.txt                   # SAC training log (unmodified copy)
  docs/
    README.md  RESULT_SUMMARY.md  RUN_INSTRUCTIONS.md
    NOTEBOOK_CLEANUP_CHANGELOG.md  REPORT_AND_PPT_STARTER_NOTES.md
  tools/
    build_final_clean_release.py  validate_final_release.py
  validation/
    validation_report.md
```

## Headline results (see `docs/RESULT_SUMMARY.md`)

- **PPO (V9):** completed 500K baseline. Eval@500K = {ppo['evals'][-1]['mean']:.1f}; best {ppo['best_explicit']['mean']:.1f} @ {ppo['best_explicit']['step']:,}.
- **SAC (V11.1):** 400K best checkpoint = {sac['best_eval']['mean']:.1f} +/- {sac['best_eval']['std']:.1f}. **Partial run (~{sac['last_pct']:.0f}%), not a completed 500K run.**

## Safety

Both notebooks ship in **REPORT_ONLY / EVAL_ONLY** mode. Training cells are
disabled by default (`ALLOW_TRAINING=False`). Nothing here trains automatically.
See `docs/RUN_INSTRUCTIONS.md`.

Regenerate with `python tools/build_final_clean_release.py` then
`python tools/validate_final_release.py`.
"""
write(os.path.join(DOC_DIR, "README.md"), readme)

run_instr = """# RUN_INSTRUCTIONS.md  (safe report / eval-only use)

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
"""
write(os.path.join(DOC_DIR, "RUN_INSTRUCTIONS.md"), run_instr)

changelog = f"""# NOTEBOOK_CLEANUP_CHANGELOG.md

Built {TODAY} by `tools/build_final_clean_release.py`. Originals were **not**
modified; cleaned copies live in `notebooks/`.

## Both notebooks
- Replaced the original title cell with a clean title + Project Overview + a
  SAFE MODE / REPORT-ONLY banner.
- Added `SAFE_MODE / REPORT_ONLY / EVAL_ONLY / ALLOW_TRAINING=False` flags to the
  central Configuration cell.
- Wrapped every `model.learn(...)` training cell in an `if ALLOW_TRAINING:` guard
  (disabled by default; prints a `[SKIP]` message otherwise).
- Renamed section headers to a clean taxonomy: Setup / Configuration /
  Environment and Perception / Model and Training Protocol / Evaluation Protocol /
  Figures and Tables for Report / Release Artifacts / Provenance and Limitations.
- Added a Provenance and Limitations section near the end (source filenames kept
  only there, per the cleanliness rules).
- Preserved all functional code: install/setup, Drive/paths, config, env wrappers,
  HSV mask / radar perception, model-loading + evaluation helpers, COMPARE5,
  RANDOM10, bootstrap-CI, plotting/report and artifact-packaging helpers.

## PPO (Final_PPO_Baseline_CarRacing_v3.ipynb)
- Removed cells: {", ".join(ppo_removed) if ppo_removed else "none"}.
- Guarded training cells: {", ".join(ppo_train) if ppo_train else "none"}.

## SAC (Final_SAC_Fast_Result_CarRacing_v3.ipynb)
- Removed cells: {", ".join(sac_removed) if sac_removed else "none"}.
- Guarded training cells: {", ".join(sac_train) if sac_train else "none"}.
- Removed the FAST_RESULT resume + speed/fps probe + emergency-recovery section
  (development-only; not part of the final PPO/SAC story).
- SAC status is documented as a 400K best-checkpoint / partial run, not 500K.

## Second-pass polish (same build run)
- PPO default `RUN_MODE` changed `OFFICIAL_500K` -> `EVAL_ONLY` (report/eval is now
  the default user-facing mode). SAC already defaulted to `EVAL_ONLY`.
- Dropped `RESUME` from the user-facing `RUN_MODE` option comments (no resume cell ships).
- Renamed crash-save wording `model_crash` / `vecnorm_crash` -> `model_interrupted` /
  `vecnorm_interrupted` (inside the guarded optional-training path; nothing loads these names).
- Neutralized old-version comparison wording (e.g. `# V8.2: ...` inline notes and
  "not directly comparable to V8.2" narrative) into version-neutral phrasing.
- SAC: rewrote V10/V10.5/V11 path-safety *comments* in version-neutral terms
  ("prevent writes into other experiment folders") while keeping all path-safety
  asserts and variable names intact (they prevent overwriting the PPO baseline).
- SAC: relabeled the final-report header/notes to the 400K best-checkpoint framing
  instead of "no official result until OFFICIAL_500K"; kept the FAST_RESULT / UTD
  update-density disclosure (scientifically relevant).
- `MODEL_TO_EVALUATE="best"` and `ALLOW_TRAINING=False` kept in both.
- Emergency runtime-restore cells: none remained to relabel (removed in first pass).

## Not done (deliberately)
- Did not re-run training, evaluation, or video. Numbers come from the logs.
- Did not touch decorative comment banners inside functional code cells.
"""
write(os.path.join(DOC_DIR, "NOTEBOOK_CLEANUP_CHANGELOG.md"), changelog)

ppt_notes = f"""# REPORT_AND_PPT_STARTER_NOTES.md

Starter notes for the written report and the slides. Phrasing avoids overclaiming.

## Storyline (report)

1. **Problem.** Generalization in randomized CarRacing-v3 from compact *visual
   features* (road mask + radar rays), not raw pixels - cheaper, interpretable.
2. **Method.** Shared perception pipeline + `MlpPolicy`. PPO as the baseline;
   SAC as a sample-efficiency / speed-oriented alternative.
3. **Protocol.** From-scratch training; COMPARE5 (fixed seeds) and RANDOM10
   (random seeds) evaluation on **raw reward**, with bootstrap confidence
   intervals; first-frame hashing to confirm seed diversity.
4. **Results.** PPO completed a 500K baseline (eval@500K = {ppo['evals'][-1]['mean']:.0f},
   best {ppo['best_explicit']['mean']:.0f} @ {ppo['best_explicit']['step']:,}).
   SAC fast-result reached a strong **400K** checkpoint
   ({sac['best_eval']['mean']:.0f} +/- {sac['best_eval']['std']:.1f}) but did not
   finish 500K.
5. **Discussion.** SAC reaches high reward by 400K (sample efficiency) but the run
   is partial; PPO is the fully-completed, more reproducible baseline.
6. **Limitations + future work** (below).

## Suggested tables

- **T1. Setup/hyperparameters** (algo, policy, env, N_ENVS, steps budget).
- **T2. Eval checkpoints** - PPO vs SAC mean +/- std per step (from RESULT_SUMMARY).
- **T3. COMPARE5 per-seed** rewards + bootstrap CI (PPO vs SAC@400K).
- **T4. RANDOM10** summary (mean, std, min/max, CI).
- **T5. Compute/budget** - fps, wall-clock, steps reached (PPO 500K vs SAC ~{sac['last_pct']:.0f}%).

## Suggested figures

- **F1.** HSV road-mask (3-seed) - shows the perception input.
- **F2.** Radar/ray overlay + obs table - the feature vector.
- **F3.** Training curve(s) - reward vs steps (mark SAC's 400K stop).
- **F4.** Reward distribution / bootstrap CI.
- **F5.** COMPARE5 bar chart.
- **F6.** Failure / termination taxonomy.
- **F7.** Action-smoothing / reward-breakdown diagnostic.

All of these are produced by the notebooks' diagnostics + evaluation + reporting
cells (Figures and Tables for Report section).

## Honest limitations (state these explicitly)

- **SAC is a partial run** (~{sac['last_pct']:.0f}% of 500K); headline is the 400K
  checkpoint. Not a completed 500K result.
- **Different budgets:** PPO@500K vs SAC@400K - disclose when comparing.
- **Single training seed** for the curve; generalization variance remains across
  eval seeds (see RANDOM10).
- **Feature-based perception** trades raw-pixel generality for speed/interpretability.
- Numbers are from training logs; not independently re-run in this release.

## Suggested presentation structure (~8-10 slides)

1. Title + one-line result. 2. Problem & why visual features. 3. Perception
pipeline (F1/F2). 4. Algorithms & protocol. 5. PPO results (F3/F4). 6. SAC
fast-result + the 400K-vs-500K honesty slide. 7. COMPARE5/RANDOM10
generalization (F5/T3). 8. Compute/budget (T5). 9. Limitations & future work.
10. Conclusion.

## Wording to avoid overclaiming
- Say "SAC fast-result reached a 400K best checkpoint", not "SAC achieved 500K".
- Say "comparable reward at a smaller step budget (partial run)", not "SAC beats PPO".
- Always pair a headline number with its step budget and +/- std.
"""
write(os.path.join(DOC_DIR, "REPORT_AND_PPT_STARTER_NOTES.md"), ppt_notes)

# ----------------------------------------------------------------------------
# 7. Console report
# ----------------------------------------------------------------------------
print("BUILD OK")
print(f"  PPO completed_500k={ppo['completed_500k']} eval@500K={ppo['evals'][-1]['mean']:.2f} "
      f"best={ppo['best_explicit']['mean'] if ppo['best_explicit'] else 'n/a'}")
print(f"  SAC completed_500k={sac['completed_500k']} best_eval={sac['best_eval']['mean']:.2f}@{sac['best_eval']['step']:,} "
      f"max_step={sac['max_step']:,} pct={sac['last_pct']}")
print(f"  PPO removed={ppo_removed} guarded_training={ppo_train}")
print(f"  SAC removed={sac_removed} guarded_training={sac_train}")
print("  wrote notebooks, logs, docs.")
