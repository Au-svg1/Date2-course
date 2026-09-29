# Station Comparability Product

## Research/data question

> Which station pairs are comparable, for which indicators and reporting weeks?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Profile shared indicators, overlapping weeks, missingness, and available QC status by station.
2. Define a reproducible station-pair comparability rule.
3. Apply the rule and produce an accepted/rejected pair table with reasons.
4. Test how at least one alternative rule changes the network of comparable pairs.
5. Document unavailable contextual variables that limit scientific interpretation.

## Open-ended decisions

- Which dimensions of overlap are essential for comparability?
- How much imbalance between stations is acceptable?
- Should comparability be indicator-specific or assigned once per station pair?

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

> Does the rule measure comparability, or merely reward stations with more records?

## Short oral-defense question

> Which rejected pair is closest to acceptance, and why?

## Final data product

A station-pair comparability table, supporting metrics, rule specification, decision log, and visual summary.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
