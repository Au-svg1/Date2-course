# QC and Provenance Audit

## Research/data question

> Can another researcher explain where selected final values came from and which transformations affected them?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Select at least three actual final records, including contrasting QC states when available.
2. Trace each record backward through supplied fields and artifacts to report/PDF, page, table, and row as far as evidence permits.
3. Record transformations, flags, ambiguities, and the exact point where traceability stops.
4. Judge whether each record is independently verifiable; do not invent missing provenance.
5. Propose a minimal provenance schema and prioritized improvements for a future release.

## Open-ended decisions

- Which records provide the most informative stress test of the provenance chain?
- What evidence is sufficient to call a record independently verifiable?
- Which missing provenance field creates the greatest scientific risk?

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

> Could a reviewer reproduce each trace without relying on your verbal explanation?

## Short oral-defense question

> Where does the strongest trace end, and what evidence is still missing?

## Final data product

A record-level trace table, evidence map, gap register, verification verdicts, proposed provenance schema, and audit memo.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
