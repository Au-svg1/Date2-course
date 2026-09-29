# Teaching-Quality Audit Report

## Overall finding

The seven packages are suitable for a three-hour, AI-assisted graduate competition after refinement. Workload is balanced by intellectual demands rather than row counts. All teams must make at least three genuine decisions, build a reproducible data product, document metadata/provenance, verify AI-assisted work, review peers, and defend an assumption change live.

| Group | Difficulty | Main Reasoning Task | Main Practical Task | Live Challenge |
|---|---|---|---|---|
| 1 DO | Moderate | Define sufficient station coverage | Build DO product and coverage evidence | Relax coverage rule |
| 2 Ammonia nitrogen | Moderate–high | Establish fair station/week comparison | Test ranking sensitivity | Remove lowest-coverage weeks |
| 3 Station comparison | High | Define pairwise comparability | Produce accepted/rejected pair table | Change comparability definition |
| 4 Temporal coverage | Moderate–high | Separate completeness from continuity | Build metric-sensitivity product | Equal availability, different continuity |
| 5 Quality strategies | Very high | Balance cleanliness and representativeness | Build and compare two datasets | Compare changed conclusions |
| 6 Multivariate | High | Trade variable breadth against usable sample | Build Date3-ready table | Add a required variable |
| 7 QC/provenance | High | Decide what counts as independent traceability | Trace actual records and register gaps | Trace a random record |

## Changes made

- Added a one-page `START_HERE.md`, explicit competition rules, assessment expectations, and an instructor-only live challenge for every group.
- Reduced starter scripts to loading and structural inspection only.
- Strengthened Group 2 around the single available nutrient-related indicator, fair comparison sets, temporal overlap, and ranking sensitivity.
- Strengthened Group 4 with metric sensitivity and explicit completeness-versus-continuity reasoning.
- Made Group 5 the most decision-intensive challenge by requiring strict and inclusive strategies and a representativeness/selection-bias audit.
- Required Group 7 to trace actual final records backward as far as existing evidence permits and to report where traceability stops.
- Clarified that Group 6 ends Date2 with a trustworthy analysis-ready dataset; Date3 begins pattern discovery. No clustering or Random Forest is requested here.
- Moved secondary student materials into `resources/` and submission artifacts into `submission_template/` without deleting useful content.

## Approximate three-hour workload and bottlenecks

- **0:00–0:25:** inspect data and define roles; bottleneck: premature use of AI-generated code before understanding columns.
- **0:25–1:20:** profile evidence and compare candidate rules; bottleneck: translating a scientific claim into an executable rule.
- **1:20–2:10:** build products and metadata; bottleneck: preserving provenance while reshaping data.
- **2:10–2:40:** peer review and revision; bottleneck: testing reproducibility from another team’s documentation.
- **2:40–3:00:** oral defense and live assumption change; bottleneck: explaining sensitivity without rerunning an entire workflow manually.

## Group-specific limitations

- Group 1 is narrower in indicator scope; its difficulty comes from defending sufficiency and temporal interpretation.
- Group 2 cannot support claims about nutrients generally because only ammonia nitrogen is present.
- Group 3 lacks verified station context such as type or coordinates, so comparability is measurement-coverage based.
- Group 4 availability metrics depend on the reporting calendar represented in Date2, not continuous sensor time.
- Group 5 can reveal selection bias but cannot fully quantify representativeness without external station metadata.
- Group 6 prepares data for later pattern discovery but does not establish causal or predictive validity.
- Group 7 traceability is limited by the provenance already retained; reaching a stopping point is a valid audit finding.

## Balance conclusion

Group 5 remains the most demanding because it requires two complete defensible strategies plus a selection-bias comparison. Group 1 is the least demanding overall because it has one indicator and a narrower product, but it is not trivial: coverage, missingness, temporal meaning, provenance, and sensitivity still require judgment. No group is substantially out of balance for the planned session when roles are divided among team members.
