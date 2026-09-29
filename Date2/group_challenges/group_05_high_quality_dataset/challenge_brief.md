# High-Quality Dataset Strategies

## Research/data question

> Does a cleaner dataset necessarily produce a better scientific dataset?

## Input

Use only the CSV file(s) in `data/`. These are transparently derived from the existing Date2 outputs. Inspect the actual columns before choosing methods.

## Required analytical tasks

1. Design at least two defensible strategies: one stricter and one more inclusive; choose and justify your own criteria.
2. Apply both strategies without changing the underlying environmental values.
3. Compare retained stations, observations, indicators, and temporal coverage.
4. Evaluate representativeness and possible selection bias introduced by each strategy.
5. Recommend a strategy for a stated scientific purpose and document rejected alternatives.

## Open-ended decisions

- Which quality dimensions belong in each strategy, and why?
- When is retaining an uncertain record preferable to excluding it?
- Which scientific use case justifies the strict or inclusive product?

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

> Does the stricter strategy remove difficult evidence in a way that changes the population represented?

## Short oral-defense question

> Which conclusion is least robust to switching strategies?

## Final data product

Two analysis-ready candidate datasets, a side-by-side retention/bias audit, decision log, data dictionaries, and a recommendation memo.

## Competition Rules

- AI tools are allowed; teams may use ChatGPT, Codex, or similar tools.
- Every analytical decision must be defendable with evidence from the supplied data.
- Teams may be asked to modify one assumption during the oral defense.
- Unexplained AI-generated output receives no credit.
- Reproducibility and reasoning matter more than code complexity.
