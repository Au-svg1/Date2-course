from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
GROUPS = sorted(path for path in ROOT.glob("group_*") if path.is_dir())
errors: list[str] = []

required = [
    "START_HERE.md",
    "challenge_brief.md",
    "starter_analysis.py",
    "data",
    "submission_template/README.md",
    "submission_template/AI_verification_log.md",
    "submission_template/expected_outputs.md",
    "submission_template/mock_release",
    "resources/package_guide.md",
    "resources/review_questions.md",
]

for group in GROUPS:
    for rel in required:
        if not (group / rel).exists():
            errors.append(f"{group.name}: missing {rel}")

    brief_path = group / "challenge_brief.md"
    if brief_path.exists():
        text = brief_path.read_text(encoding="utf-8")
        for heading in ["## Open-ended decisions", "## Competition Rules", "## Peer-review question", "## Short oral-defense question"]:
            if heading not in text:
                errors.append(f"{group.name}: missing heading {heading}")
        match = re.search(r"## Open-ended decisions\n(.*?)(?:\n## |\nDo not treat)", text, re.S)
        decisions = re.findall(r"^- ", match.group(1), re.M) if match else []
        if len(decisions) < 2:
            errors.append(f"{group.name}: fewer than two open-ended decisions")

    for csv_path in sorted((group / "data").glob("*.csv")):
        try:
            data = pd.read_csv(csv_path)
            if data.empty:
                errors.append(f"{group.name}: empty data file {csv_path.name}")
        except Exception as exc:
            errors.append(f"{group.name}: unreadable {csv_path.name}: {exc}")

    starter = group / "starter_analysis.py"
    if starter.exists():
        source = starter.read_text(encoding="utf-8")
        try:
            compile(source, str(starter), "exec")
        except SyntaxError as exc:
            errors.append(f"{group.name}: starter syntax error: {exc}")
        if "to_csv" in source or "groupby(" in source or ".plot(" in source:
            errors.append(f"{group.name}: starter appears over-scaffolded")

if len(GROUPS) != 7:
    errors.append(f"Expected 7 groups, found {len(GROUPS)}")
for rel in ["instructor/live_challenges.md", "instructor/challenge_audit_report.md"]:
    if not (ROOT / rel).exists():
        errors.append(f"Missing {rel}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Groups checked: {len(GROUPS)}")
print("All required paths exist, CSV inputs are readable, starters compile and remain minimal, and every brief has at least two decisions plus competition/review/defense sections.")
