# group_01_DO: package guide

This is a secondary reference. Students should begin with `../START_HERE.md`.

## Working-directory convention

Run commands from the group folder (`group_01_DO/`). Paths below are relative to that folder.

1. Read `challenge_brief.md`.
2. Inspect the unchanged files in `data/`.
3. Run `python starter_analysis.py`.
4. Use `resources/review_questions.md` during peer review.
5. Complete the files under `submission_template/`; place release tables in `submission_template/mock_release/`.

## Reproducibility and source protection

Use relative paths in all submitted code. Do not overwrite `data/`, the original Date2 files under `../../../outputs/`, or any source PDF. The instructor can rebuild group inputs from the challenge root with `python prepare_group_datasets.py`, but students should not regenerate their assigned input during the competition.

## Data source and AI assistance

The group input is derived from China National Environmental Monitoring Centre weekly water-quality reports through the Date2 workflow. Environmental measurements were not edited or fabricated. AI may assist with code or critique, but the team must verify and defend every analytical decision and complete `submission_template/AI_verification_log.md`.
