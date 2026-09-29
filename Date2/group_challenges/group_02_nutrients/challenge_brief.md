# Ammonia-Nitrogen Comparability

## Research/data question

> Can ammonia-nitrogen measurements be compared fairly across stations and reporting weeks?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Verify that ammonia nitrogen is the only nutrient-related indicator supplied; do not imply a multi-nutrient dataset.
2. Profile station coverage, temporal overlap, reported missingness, and units.
3. Define a defensible comparison set of stations and weeks before ranking stations.
4. Compare apparent station rankings under at least two reasonable inclusion rules.
5. Explain how incomplete or uneven monitoring could bias the apparent differences.

## Open-ended decisions

- What minimum temporal overlap is necessary for a fair comparison?
- Which inclusion rule best balances coverage and representativeness?
- Is any station ranking stable enough to report, and how should uncertainty be communicated?

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

> Could uneven monitoring alone explain part of the reported station ordering?

## Short oral-defense question

> Under what change to your inclusion rule would you withdraw the ranking?

## Final data product

A defensible ammonia-nitrogen comparison dataset, coverage/overlap evidence, ranking-sensitivity table, decision log, and data dictionary.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
