# Multivariate Analysis-Ready Dataset

## Research/data question

> Which variables and station-weeks can form a defensible multivariate analysis-ready dataset?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Audit variable availability, units, missingness, and complete-case loss.
2. Choose a multivariate variable set and define the observational unit.
3. Compare at least two missing-data or inclusion strategies without fabricating measurements.
4. Produce a machine-readable table and explain how preprocessing choices affect later pattern discovery.
5. Create a readiness note for Date3; do not run clustering or Random Forest.

## Open-ended decisions

- Which indicators are essential enough to justify sample-size loss?
- Which missing-data strategy is scientifically defensible for the intended later analysis?
- Should values be transformed or standardized later, and what evidence would justify that choice?

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

> Does the chosen table preserve enough observations and station diversity for later pattern discovery?

## Short oral-defense question

> Which added variable would cause the largest defensibility-versus-sample-size conflict?

## Final data product

A multivariate station-week dataset, completeness comparison, data dictionary, decision log, and Date3 readiness note.

## Date2 → Date3 boundary

Date2 ends with **building a trustworthy analysis-ready dataset**. Date3 begins with **discovering patterns from that dataset**. Stop before clustering, Random Forest, or other predictive/pattern-discovery methods.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
