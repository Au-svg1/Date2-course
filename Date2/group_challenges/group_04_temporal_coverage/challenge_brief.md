# Temporal Coverage and Continuity

## Research/data question

> Which stations are suitable for trend, event, or cross-sectional analysis given their temporal coverage?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Reconstruct and audit OverallAvailability and continuity-related evidence from the supplied records.
2. Measure gaps and distinguish scattered observations from uninterrupted sequences.
3. Compare at least two availability definitions and identify stations whose classification changes.
4. Contrast stations with similar overall availability but different continuity.
5. Recommend candidates separately for trend, event, and cross-sectional analyses.

## Open-ended decisions

- Which availability metric fits each intended analysis?
- When should continuity outweigh overall completeness?
- How should a station with high coverage but a strategically placed gap be classified?

Do not treat these as fill-in-the-blank questions: state alternatives, evidence, and consequences.

## Required evidence

- Keep the supplied `data/` files unchanged and write products inside `submission_template/mock_release/`.
- Provide runnable code with relative paths and a short environment note.
- Complete `submission_template/AI_verification_log.md`, including at least one AI suggestion you checked and rejected or revised.
- Provide a data dictionary and provenance statement that names the supplied input file and documents each transformation.
- Do not invent coordinates, station types, dates, indicators, units, metadata, or measurements.

## Reproducibility check

Another team must be able to recreate the main product from the unchanged `data/` file using only your submitted code and documentation.

## AI-verification requirement

For at least one AI-assisted transformation or interpretation, independently inspect rows or recompute a result, document the check, and explain whether you accepted, revised, or rejected the suggestion.

## Peer-review question

> Would your recommendation change if the scientific goal changed from trend detection to event analysis?

## Short oral-defense question

> Why is a single availability percentage insufficient?

## Final data product

A temporal-coverage dataset, metric-sensitivity table, use-case recommendations, decision log, and coverage visualization.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
