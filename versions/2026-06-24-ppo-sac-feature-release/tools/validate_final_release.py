#!/usr/bin/env python3
"""
validate_final_release.py
=========================
Static checks on the built CarRacing_Final_Clean_Release/. Does NOT run notebooks
or training. Writes validation/validation_report.md with PASS/FAIL/NON-BLOCKING.
"""
import os
import json
import datetime

import nbformat

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

NB = {
    "PPO": os.path.join(ROOT, "notebooks", "Final_PPO_Baseline_CarRacing_v3.ipynb"),
    "SAC": os.path.join(ROOT, "notebooks", "Final_SAC_Fast_Result_CarRacing_v3.ipynb"),
}
REQUIRED = [
    "notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb",
    "notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb",
    "logs/V9_training_500k_log.txt",
    "logs/V11_1_training_log.txt",
    "docs/README.md",
    "docs/RESULT_SUMMARY.md",
    "docs/RUN_INSTRUCTIONS.md",
    "docs/NOTEBOOK_CLEANUP_CHANGELOG.md",
    "docs/REPORT_AND_PPT_STARTER_NOTES.md",
    "tools/build_final_clean_release.py",
    "tools/validate_final_release.py",
]

# old-version / scratchpad clutter that must not appear in MAJOR headings
CLUTTER = ["V6", "V7", "V8", "V10", "V10.5", "panic", "emergency", "recovery",
           "crash", "debug", "probe", "resume + probes", "Development History"]

results = []  # (severity, label, detail)  severity in PASS/FAIL/NON-BLOCKING


def check(cond, label, detail_ok="", detail_fail="", nonblocking=False):
    if cond:
        results.append(("PASS", label, detail_ok))
    else:
        results.append(("NON-BLOCKING" if nonblocking else "FAIL", label, detail_fail))
    return cond


def cell_src(c):
    return c.source if isinstance(c.source, str) else "".join(c.source)


def headings(nb):
    out = []
    for c in nb.cells:
        if c.cell_type == "markdown":
            for ln in cell_src(c).splitlines():
                if ln.strip().startswith("#"):
                    out.append(ln.strip())
    return out


def real_learn_lines(nb):
    """Top-level (non-comment, non-indented) model.learn calls = unguarded."""
    bad = []
    for c in nb.cells:
        if c.cell_type != "code":
            continue
        src = cell_src(c)
        guarded = "ALLOW_TRAINING" in src
        for ln in src.splitlines():
            code = ln.split("#", 1)[0]
            if ".learn(" not in code:
                continue
            indented = ln[:1].isspace()  # inside the if-guard block
            if not (guarded and indented):
                bad.append((cell_src(c).splitlines()[0][:50], ln.strip()[:50]))
    return bad


# 1. folder structure + required files
for rel in REQUIRED:
    check(os.path.isfile(os.path.join(ROOT, rel)), f"exists: {rel}",
          detail_fail="missing")
check(os.path.isdir(os.path.join(ROOT, "validation")), "exists: validation/")

# 2-4. notebooks valid JSON + nbformat
loaded = {}
for name, path in NB.items():
    if not os.path.isfile(path):
        results.append(("FAIL", f"{name} notebook present", "file missing"))
        continue
    try:
        with open(path, encoding="utf-8") as f:
            json.load(f)
        check(True, f"{name} valid JSON")
    except Exception as e:
        check(False, f"{name} valid JSON", detail_fail=str(e))
        continue
    try:
        nb = nbformat.read(path, as_version=4)
        nbformat.validate(nb)
        loaded[name] = nb
        check(True, f"{name} passes nbformat.validate")
    except Exception as e:
        check(False, f"{name} passes nbformat.validate", detail_fail=str(e))

# 8. no old-version clutter in major headings
for name, nb in loaded.items():
    hs = headings(nb)
    dirty = [h for h in hs if any(k.lower() in h.lower() for k in CLUTTER)]
    check(not dirty, f"{name} headings clean (no old-version clutter)",
          detail_ok=f"{len(hs)} headings clean",
          detail_fail="dirty headings: " + " | ".join(dirty[:5]))

# 9-10. no unguarded model.learn; remaining training cells guarded+disabled
for name, nb in loaded.items():
    bad = real_learn_lines(nb)
    check(not bad, f"{name} no unguarded model.learn(",
          detail_ok="all .learn() calls inside ALLOW_TRAINING guard",
          detail_fail="unguarded: " + " | ".join(f"{a}:{b}" for a, b in bad[:3]))
    # ALLOW_TRAINING default False present in a config cell
    has_flag = any("ALLOW_TRAINING = False" in cell_src(c) or
                   "ALLOW_TRAINING=False" in cell_src(c)
                   for c in nb.cells if c.cell_type == "code")
    check(has_flag, f"{name} ships ALLOW_TRAINING=False (training disabled by default)",
          detail_fail="ALLOW_TRAINING=False not found")

# 11. result summary distinguishes PPO-completed vs SAC-partial
rs_path = os.path.join(ROOT, "docs", "RESULT_SUMMARY.md")
if os.path.isfile(rs_path):
    rs = open(rs_path, encoding="utf-8").read()
    check("COMPLETED 500K" in rs and "938.87" in rs,
          "RESULT_SUMMARY marks PPO completed 500K baseline",
          detail_fail="PPO completion/number missing")
    check(("NOT a completed 500K" in rs or "not\n  treated as a completed 500K" in rs
           or "not treated as a completed 500K" in rs)
          and "400K" in rs,
          "RESULT_SUMMARY marks SAC 400K best-checkpoint / partial run",
          detail_fail="SAC partial-run status missing")
else:
    check(False, "RESULT_SUMMARY.md present", detail_fail="missing")

# originals untouched (sanity)
for orig in [os.path.join(os.path.dirname(ROOT), "completed_run_evidence", "V9_CarRacing_PPO_Colab.ipynb"),
             os.path.join(os.path.dirname(ROOT), "completed_run_evidence", "V11_1_CarRacing_SAC_Fast_Result.ipynb")]:
    check(os.path.isfile(orig), f"original preserved: {os.path.basename(orig)}",
          nonblocking=True, detail_fail="original not found (cannot confirm)")

# ----------------------------------------------------------------------------
# write report
# ----------------------------------------------------------------------------
n_fail = sum(1 for s, _, _ in results if s == "FAIL")
n_nb = sum(1 for s, _, _ in results if s == "NON-BLOCKING")
n_pass = sum(1 for s, _, _ in results if s == "PASS")
overall = "FAIL" if n_fail else "PASS"

lines = [
    "# validation_report.md",
    "",
    f"_Static validation run {datetime.date.today().isoformat()} by "
    "`tools/validate_final_release.py` (no notebooks/training executed)._",
    "",
    f"## Overall: **{overall}**  ({n_pass} PASS, {n_fail} FAIL, {n_nb} NON-BLOCKING)",
    "",
    "| status | check | detail |",
    "|---|---|---|",
]
for sev, label, detail in results:
    lines.append(f"| {sev} | {label} | {detail} |")
lines += [
    "",
    "## Notes",
    "- Static checks only: AST/JSON/nbformat validity, heading cleanliness, "
    "training-guard presence, and result-summary honesty.",
    "- Seed isolation, eval correctness, and training stability can only be "
    "verified by running the notebooks in Colab (per project rule 2).",
]
report = "\n".join(lines) + "\n"

os.makedirs(os.path.join(ROOT, "validation"), exist_ok=True)
with open(os.path.join(ROOT, "validation", "validation_report.md"), "w", encoding="utf-8") as f:
    f.write(report)

print(f"VALIDATION {overall}: {n_pass} PASS / {n_fail} FAIL / {n_nb} NON-BLOCKING")
for sev, label, detail in results:
    if sev != "PASS":
        print(f"  [{sev}] {label} -- {detail}")
raise SystemExit(1 if n_fail else 0)
