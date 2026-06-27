#!/usr/bin/env python3
"""
Static validation for final/.

This script does not execute notebooks, train models, or regenerate results.
"""
import csv
import datetime as _dt
import json
import re
from pathlib import Path

try:
    import nbformat
except Exception:  # pragma: no cover - optional local dependency
    nbformat = None


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
RESULTS = []

REQUIRED_FILES = [
    "README.md",
    "media.md",
    "release_notes_v2.md",
    "report/MANUAL_OVERLEAF_EXPORT_REQUIRED.md",
    "overleaf/Image_Processing_Project_Overleaf_Package.zip",
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
    "videos/video_manifest.csv",
    "docs/README.md",
    "docs/RESULT_SUMMARY.md",
    "docs/RUN_INSTRUCTIONS.md",
    "docs/ASSET_EXPORT_MANIFEST.md",
    "validation/validation_report.md",
    "tools/validate_final_release.py",
]

NOTEBOOKS = {
    "PPO": ROOT / "notebooks" / "Final_PPO_Baseline_CarRacing_v3.ipynb",
    "SAC": ROOT / "notebooks" / "Final_SAC_Fast_Result_CarRacing_v3.ipynb",
}

STALE_PATTERNS = [
    "CarRacing_Final" + "_Clean_Release",
    "NOTEBOOK_CLEANUP" + "_CHANGELOG",
    "REPORT_AND_PPT" + "_STARTER_NOTES",
    "starter " + "notes",
]


def record(ok, label, detail_ok="", detail_fail="", severity="FAIL"):
    RESULTS.append(("PASS" if ok else severity, label, detail_ok if ok else detail_fail))


def read_text(path):
    return path.read_text(encoding="utf-8", errors="replace")


def markdown_files():
    return [REPO / "README.md", *sorted(ROOT.rglob("*.md"))]


def has_negation(line):
    return bool(re.search(r"\b(not|no|never|without|isn't|doesn't|do not|did not|is not|does not|not claimed|not presented|no claim)\b", line, re.I))


def unsupported_claims():
    bad = []
    checks = [
        ("partial-run completion claim", lambda s: ("s" + "ac") in s and re.search(r"\bsac\b.{0,40}\bcompleted\s+500k\b", s) and not has_negation(s)),
        ("PPO victory claim", lambda s: ("s" + "ac") in s and "ppo" in s and re.search(r"\b(beats?|beating|outperforms?)\b", s) and not has_negation(s)),
        ("compute-equivalent comparison", lambda s: "compute-equivalent" in s and not has_negation(s)),
        ("raw pixel CNN training claim", lambda s: ("raw-pixel cnn policy " + "was trained") in s and not has_negation(s)),
        ("CarRacing solved claim", lambda s: ("carracing-v3 is " + "solved") in s and not has_negation(s)),
    ]
    for md in markdown_files():
        for line_no, line in enumerate(read_text(md).splitlines(), 1):
            lowered = line.lower()
            for label, predicate in checks:
                if predicate(lowered):
                    bad.append(f"{md.relative_to(REPO)}:{line_no}: {label}")
    return bad


def stale_paths():
    hits = []
    for md in markdown_files():
        for line_no, line in enumerate(read_text(md).splitlines(), 1):
            if any(pattern in line for pattern in STALE_PATTERNS):
                hits.append(f"{md.relative_to(REPO)}:{line_no}")
    return hits


def broken_markdown_links():
    broken = []
    for md in markdown_files():
        text = read_text(md)
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            link = match.group(1).strip()
            if re.match(r"^[a-z]+:", link) or link.startswith("#"):
                continue
            rel = link.split("#", 1)[0]
            if rel and not (md.parent / rel).resolve().exists():
                broken.append(f"{md.relative_to(REPO)} -> {link}")
    return broken


def markdown_tables_ok():
    broken = []
    for md in markdown_files():
        lines = read_text(md).splitlines()
        index = 0
        while index < len(lines):
            line = lines[index].strip()
            if line.startswith("|") and line.endswith("|"):
                start = index + 1
                block = []
                while index < len(lines) and lines[index].strip().startswith("|") and lines[index].strip().endswith("|"):
                    block.append(lines[index])
                    index += 1
                if len(block) < 2 or not re.match(r"^\|[\s:|-]+\|$", block[1].strip()):
                    broken.append(f"{md.relative_to(REPO)} table near line {start}")
            else:
                index += 1
    return broken


def has_real_line_breaks(path):
    lines = read_text(path).splitlines()
    return len(lines) >= 20 and max((len(line) for line in lines), default=0) < 220


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


def validate_videos():
    video_dir = ROOT / "videos" / "github_playable"
    videos = sorted(video_dir.glob("*.mp4")) if video_dir.is_dir() else []
    record(video_dir.is_dir(), "videos/github_playable/ exists", detail_fail="missing")
    record(len(videos) == 12, "exactly 12 final MP4 videos exist", detail_ok=f"{len(videos)} videos", detail_fail=f"{len(videos)} videos")

    manifest = ROOT / "videos" / "video_manifest.csv"
    if manifest.is_file():
        with manifest.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        record(len(rows) == 12, "video manifest has 12 rows", detail_ok="12 rows", detail_fail=f"{len(rows)} rows")
        missing = [row.get("filename", "") for row in rows if not (ROOT / "videos" / row.get("filename", "")).is_file()]
        record(not missing, "video manifest filenames exist", detail_fail=", ".join(missing))
    else:
        record(False, "media/video_manifest.csv exists", detail_fail="missing")


def validate_size_limits():
    files = [p for p in REPO.rglob("*") if p.is_file() and ".git" not in p.parts]
    over_50 = [p.relative_to(REPO).as_posix() for p in files if p.stat().st_size > 50 * 1024 * 1024]
    over_90 = [p.relative_to(REPO).as_posix() for p in files if p.stat().st_size > 90 * 1024 * 1024]
    record(not over_50, "no file exceeds 50 MiB", detail_fail=", ".join(over_50))
    record(not over_90, "no file exceeds 90 MiB", detail_fail=", ".join(over_90))


def write_report():
    n_pass = sum(1 for status, _, _ in RESULTS if status == "PASS")
    n_fail = sum(1 for status, _, _ in RESULTS if status == "FAIL")
    n_nb = sum(1 for status, _, _ in RESULTS if status == "NON-BLOCKING")
    n_manual = sum(1 for status, _, _ in RESULTS if status == "MANUAL-REQUIRED")
    overall = "FAIL" if n_fail else "PASS"

    lines = [
        "# validation_report.md",
        "",
        f"_Static validation run {_dt.date.today().isoformat()} by `tools/validate_final_release.py`._",
        "",
        "No notebooks, training, or result generation were executed.",
        "",
        f"## Overall: **{overall}** ({n_pass} PASS, {n_fail} FAIL, {n_nb} NON-BLOCKING, {n_manual} MANUAL-REQUIRED)",
        "",
        "| status | check | detail |",
        "| ------ | ----- | ------ |",
    ]
    for status, label, detail in RESULTS:
        lines.append(f"| {status} | {label} | {detail} |")
    lines.extend([
        "",
        "## Notes",
        "",
        "- This validates the public V2 GitHub package structure only.",
        "- Notebook execution, training stability, and live evaluation still require the intended Colab/GPU runtime.",
    ])

    report = "\n".join(lines) + "\n"
    (ROOT / "validation").mkdir(exist_ok=True)
    (ROOT / "validation" / "validation_report.md").write_text(report, encoding="utf-8")
    print(f"VALIDATION {overall}: {n_pass} PASS / {n_fail} FAIL / {n_nb} NON-BLOCKING / {n_manual} MANUAL-REQUIRED")
    return n_fail


def main():
    record((REPO / "README.md").is_file(), "root README.md exists")
    record(has_real_line_breaks(REPO / "README.md"), "root README.md has real Markdown line breaks", detail_fail="line-break heuristic failed")

    for rel in REQUIRED_FILES:
        record((ROOT / rel).is_file(), f"exists: {rel}", detail_fail="missing")
    record(
        (ROOT / "report" / "Image_Processing_Project_V2_IEEE_Report.pdf").is_file(),
        "official report PDF exported from Overleaf",
        detail_fail="pending manual Overleaf export; see report/MANUAL_OVERLEAF_EXPORT_REQUIRED.md",
        severity="MANUAL-REQUIRED",
    )

    record(has_real_line_breaks(ROOT / "README.md"), "V2 README.md has real Markdown line breaks", detail_fail="line-break heuristic failed")
    table_issues = markdown_tables_ok()
    record(not table_issues, "Markdown tables have separator rows", detail_fail="; ".join(table_issues))

    validate_notebooks()
    validate_videos()

    stale = stale_paths()
    record(not stale, "no stale local paths remain", detail_fail="; ".join(stale))

    bad_claims = unsupported_claims()
    record(not bad_claims, "no unsupported claims remain", detail_fail="; ".join(bad_claims))

    broken = broken_markdown_links()
    record(not broken, "all relative Markdown links resolve", detail_fail="; ".join(broken))

    validate_size_limits()
    raise SystemExit(1 if write_report() else 0)


if __name__ == "__main__":
    main()
