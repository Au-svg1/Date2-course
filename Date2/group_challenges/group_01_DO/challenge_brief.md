# Dissolved Oxygen Data Product

## Research/data question

> Which stations and weeks support a scientifically defensible dissolved-oxygen comparison?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Confirm how dissolved oxygen is represented, including units and the meaning of the reporting date.
2. Quantify station coverage, missing values, and temporal gaps.
3. Define and apply a defensible sufficiency rule; show who is included and excluded.
4. Produce an analysis-ready DO table and a compact coverage summary.
5. Document every filter and preserve links to available provenance fields.

## Open-ended decisions

- What evidence is sufficient for a station to support comparison?
- Should reported-missing rows remain explicit or be removed from the analysis table?
- Which temporal summary is least misleading for these reporting weeks?

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

> Would another team reach the same inclusion set from your written rule alone?

## Short oral-defense question

> Which single assumption has the greatest effect on station inclusion?

## Final data product

An analysis-ready DO dataset, station-coverage table, decision log, data dictionary, and one defensible visualization.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
