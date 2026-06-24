#!/usr/bin/env python3
"""
Static validation for versions/2026-06-24-ppo-sac-feature-release/.

This script does not execute notebooks, train models, or regenerate results.
"""
import datetime as _dt
import json
import re
from pathlib import Path

try:
    import nbformat
except Exception:  # pragma: no cover - optional local dependency
    nbformat = None


ROOT = Path(__file__).resolve().parents[1]
RESULTS = []

REQUIRED_FILES = [
    "README.md",
    "report/CarRacing_v3_RL_Report_1103820_REVISED.docx",
    "notebooks/Final_PPO_Baseline_CarRacing_v3.ipynb",
    "notebooks/Final_SAC_Fast_Result_CarRacing_v3.ipynb",
    "logs/V9_training_500k_log.txt",
    "logs/V11_1_training_log.txt",
    "figures/checkpoint_comparison.png",
    "figures/feature_pipeline_schematic.png",
    "figures/generalization_summary.png",
    "figures/training_curve_ppo_sac.png",
    "tables/compute_budget.csv",
    "tables/headline_comparison.csv",
    "tables/notebook_output_generalization_summary.csv",
    "tables/ppo_eval_checkpoints.csv",
    "tables/sac_eval_checkpoints.csv",
    "docs/README.md",
    "docs/RESULT_SUMMARY.md",
    "docs/RUN_INSTRUCTIONS.md",
    "docs/ASSET_EXPORT_MANIFEST.md",
    "validation/validation_report.md",
    "tools/build_final_clean_release.py",
    "tools/validate_final_release.py",
]

NOTEBOOKS = {
    "PPO": ROOT / "notebooks" / "Final_PPO_Baseline_CarRacing_v3.ipynb",
    "SAC": ROOT / "notebooks" / "Final_SAC_Fast_Result_CarRacing_v3.ipynb",
}


def record(ok, label, detail_ok="", detail_fail="", severity="FAIL"):
    RESULTS.append(("PASS" if ok else severity, label, detail_ok if ok else detail_fail))


def read_text(path):
    return path.read_text(encoding="utf-8", errors="replace")


def markdown_files():
    return [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]


def has_negation(line):
    return bool(re.search(r"\b(not|no|never|without|isn't|doesn't|do not|NOT)\b", line, re.I))


def unsupported_claims():
    bad = []
    checks = [
        ("SAC completed 500K", lambda s: re.search(r"sac.{0,60}completed 500k", s) and not has_negation(s)),
        ("SAC beats PPO", lambda s: "sac" in s and re.search(r"\b(beats?|beating|outperforms?)\b", s) and "ppo" in s and not has_negation(s)),
        ("compute-equivalent comparison", lambda s: "compute-equivalent" in s and not has_negation(s)),
        ("raw-pixel CNN training", lambda s: "raw-pixel cnn" in s and re.search(r"\b(train|trained|training)\b", s) and not has_negation(s)),
        ("CarRacing-v3 is solved", lambda s: "carracing-v3" in s and "solved" in s and not has_negation(s)),
    ]
    for md in markdown_files():
        for line_no, line in enumerate(read_text(md).splitlines(), 1):
            lowered = line.lower()
            for label, predicate in checks:
                if predicate(lowered):
                    bad.append(f"{md.relative_to(ROOT)}:{line_no}: {label}")
    return bad


def broken_markdown_links():
    broken = []
    for md in markdown_files():
        text = read_text(md)
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            link = match.group(1)
            if re.match(r"^[a-z]+:", link) or link.startswith("#"):
                continue
            rel = link.split("#", 1)[0]
            if rel and not (md.parent / rel).resolve().exists():
                broken.append(f"{md.relative_to(ROOT)} -> {link}")
    return broken


def validate_notebooks():
    for name, path in NOTEBOOKS.items():
        try:
            with path.open(encoding="utf-8") as handle:
                json.load(handle)
            record(True, f"{name} notebook valid JSON")
        except Exception as exc:
            record(False, f"{name} notebook valid JSON", detail_fail=str(exc))
            continue

        if nbformat is None:
            record(False, f"{name} notebook nbformat validation", detail_fail="nbformat not installed", severity="NON-BLOCKING")
            continue

        try:
            nb = nbformat.read(path, as_version=4)
            nbformat.validate(nb)
            record(True, f"{name} notebook passes nbformat.validate")
        except Exception as exc:
            record(False, f"{name} notebook passes nbformat.validate", detail_fail=str(exc))


def validate_size_limits():
    over_50 = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and p.stat().st_size > 50 * 1024 * 1024]
    over_90 = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and p.stat().st_size > 90 * 1024 * 1024]
    record(not over_50, "no file exceeds 50 MiB", detail_fail=", ".join(over_50))
    record(not over_90, "no file exceeds 90 MiB", detail_fail=", ".join(over_90))


def write_report():
    n_pass = sum(1 for status, _, _ in RESULTS if status == "PASS")
    n_fail = sum(1 for status, _, _ in RESULTS if status == "FAIL")
    n_nb = sum(1 for status, _, _ in RESULTS if status == "NON-BLOCKING")
    overall = "FAIL" if n_fail else "PASS"

    lines = [
        "# validation_report.md",
        "",
        f"_Static validation run {_dt.date.today().isoformat()} by `tools/validate_final_release.py`._",
        "",
        "No notebooks, training, or result generation were executed.",
        "",
        f"## Overall: **{overall}** ({n_pass} PASS, {n_fail} FAIL, {n_nb} NON-BLOCKING)",
        "",
        "| status | check | detail |",
        "|---|---|---|",
    ]
    for status, label, detail in RESULTS:
        lines.append(f"| {status} | {label} | {detail} |")
    lines.extend([
        "",
        "## Notes",
        "",
        "- This validates the V2 GitHub package structure only.",
        "- Notebook execution, training stability, and live evaluation still require the intended Colab/GPU runtime.",
    ])

    report = "\n".join(lines) + "\n"
    (ROOT / "validation").mkdir(exist_ok=True)
    (ROOT / "validation" / "validation_report.md").write_text(report, encoding="utf-8")
    print(f"VALIDATION {overall}: {n_pass} PASS / {n_fail} FAIL / {n_nb} NON-BLOCKING")
    return n_fail


def main():
    for rel in REQUIRED_FILES:
        record((ROOT / rel).is_file(), f"exists: {rel}", detail_fail="missing")

    validate_notebooks()
    bad_claims = unsupported_claims()
    record(not bad_claims, "V2 README/docs avoid unsupported PPO/SAC claims", detail_fail="; ".join(bad_claims))

    broken = broken_markdown_links()
    record(not broken, "relative Markdown links resolve", detail_fail="; ".join(broken))

    validate_size_limits()
    raise SystemExit(1 if write_report() else 0)


if __name__ == "__main__":
    main()
