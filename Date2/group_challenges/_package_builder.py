from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import numpy as np
import pandas as pd


GROUPS = {
    "group_01_DO": {
        "number": 1,
        "theme": "Dissolved oxygen data product",
        "question": "Which dissolved-oxygen records form a defensible dataset for temporal and cross-station exploration?",
        "product": "A documented dissolved-oxygen observation product with a justified station-inclusion rule.",
        "available": ["data/do_observations.csv", "data/do_station_coverage.csv", "data/do_metadata.csv", "data/data_dictionary.csv"],
        "tasks": [
            "Confirm how dissolved oxygen is represented and which unit is used.",
            "Quantify available and missing DO values for each station and reporting period.",
            "Define and apply a defensible rule for stations with sufficient DO data. Do not use a cutoff merely because it is convenient.",
            "Check whether gaps are concentrated or scattered through time.",
            "Build an analysis-ready DO observation table without changing environmental values.",
            "Document every exclusion and retain source-PDF provenance fields.",
        ],
        "decisions": [
            "What does sufficient DO coverage mean for your intended comparison?",
            "Should reported missing rows remain in the released observation table or a separate gap table?",
            "Which temporal summary is defensible for weekly report data?",
        ],
        "deliverables": ["do_observations.csv", "do_station_summary.csv", "metadata.csv", "data_dictionary.csv", "README.md", "selection_rules.md"],
        "peer": "Could another team reproduce every included and excluded station from the written rule?",
        "oral": "Why is your sufficiency rule appropriate for DO exploration, and what conclusion would change if the rule were relaxed?",
    },
    "group_02_nutrients": {
        "number": 2,
        "theme": "Nutrient monitoring data product",
        "question": "Can the available nutrient measurements be compared fairly across stations and weeks?",
        "product": "A nutrient-focused observation table with coverage evidence and a clearly bounded scope.",
        "available": ["data/nutrient_observations.csv", "data/nutrient_coverage.csv", "data/indicator_catalog.csv", "data/nutrient_metadata.csv"],
        "tasks": [
            "Use the indicator catalog to identify which nutrient-related indicators actually exist.",
            "Verify units and quantify station and weekly coverage for each retained nutrient indicator.",
            "Identify coverage gaps that could bias station or week comparisons.",
            "Decide whether the available field supports a broad nutrient claim or a narrower ammonia-nitrogen product.",
            "Create a nutrient observation table and coverage summary while preserving source values.",
            "Document absent nutrient fields such as TP or TN as limitations, not zeros.",
        ],
        "decisions": [
            "Which nutrient-related indicators belong in the release, and why?",
            "Which station/week comparisons are sufficiently balanced?",
            "How narrowly should the product be named when only one nutrient-related indicator is available?",
        ],
        "deliverables": ["nutrient_observations.csv", "nutrient_coverage.csv", "metadata.csv", "data_dictionary.csv", "README.md", "scope_decisions.md"],
        "peer": "Does the product title and documentation accurately reflect the indicators that are actually present?",
        "oral": "What comparison would become invalid if missing nutrient weeks were treated as zero?",
    },
    "group_03_station_comparison": {
        "number": 3,
        "theme": "Station comparison data product",
        "question": "When are two monitoring stations sufficiently comparable?",
        "product": "A station-comparison dataset built from explicit indicator and temporal-overlap criteria.",
        "available": ["data/candidate_station_observations.csv", "data/station_indicator_coverage.csv", "data/candidate_station_inventory.csv"],
        "tasks": [
            "Inspect coverage by station and indicator.",
            "Identify indicators shared among candidate stations.",
            "Measure overlap in reporting periods rather than comparing record counts alone.",
            "Propose inclusion criteria for a fair station comparison.",
            "Create a comparison table and document excluded stations and indicators.",
            "Explain why no geographic comparison is attempted without verified coordinates.",
        ],
        "decisions": [
            "How much shared temporal coverage is enough for comparison?",
            "Must all compared stations contain the same indicators?",
            "Should comparability prioritize completeness, continuity, or representativeness?",
        ],
        "deliverables": ["station_comparison_dataset.csv", "comparison_eligibility.csv", "metadata.csv", "data_dictionary.csv", "README.md", "comparison_design.md"],
        "peer": "Would the comparison remain fair if one station had the same record count but different missing weeks?",
        "oral": "Identify the most consequential comparability assumption in your design.",
    },
    "group_04_temporal_coverage": {
        "number": 4,
        "theme": "Temporal coverage and continuity",
        "question": "Which station–indicator records are suitable for temporal analysis?",
        "product": "A verified coverage table and a justified list of temporal-analysis candidates.",
        "available": ["data/availability_metrics.csv", "data/gap_pattern_summary.csv", "data/coverage_field_definitions.csv"],
        "tasks": [
            "Reconstruct at least two availability metrics from observation records and compare them with Date2 values.",
            "Create a station × indicator coverage table.",
            "Distinguish long continuous gaps from scattered missing values.",
            "Compare at least two definitions of good temporal coverage.",
            "Select temporal-analysis candidates and preserve the decision evidence.",
            "Explain why weekly-report availability is not daily or hourly monitoring completeness.",
        ],
        "decisions": [
            "Which metric or metric combination best supports your intended temporal study?",
            "How should a long uninterrupted segment be weighed against overall completeness?",
            "What should happen when the metrics disagree?",
        ],
        "deliverables": ["availability_metrics_verified.csv", "temporal_analysis_candidates.csv", "coverage_summary.csv", "README.md", "metric_verification.md"],
        "peer": "Can the candidate rule distinguish scattered gaps from one long missing interval?",
        "oral": "Why did you prioritize your chosen availability metric over the alternatives?",
    },
    "group_05_high_quality_dataset": {
        "number": 5,
        "theme": "High-quality analysis dataset",
        "question": "How can a smaller dataset improve reliability without hiding selection bias?",
        "product": "A quality-filtered observation product with strict and moderate strategies compared.",
        "available": ["data/quality_selection_input.csv", "data/qc_flag_summary.csv", "data/source_indicator_inventory.csv"],
        "tasks": [
            "Design at least two filtering strategies with different levels of strictness.",
            "Use coverage, continuity, missingness, length, and QC information where relevant.",
            "Apply both strategies and compare retained records, stations, indicators, and weeks.",
            "Choose one strategy for the final product and justify it scientifically.",
            "Describe information lost and potential selection bias.",
            "Export the selected observations and matching metadata with provenance intact.",
        ],
        "decisions": [
            "Which quality dimensions belong in the inclusion rule?",
            "How should strict and moderate strategies differ?",
            "Which loss of representativeness is acceptable for the intended analysis?",
        ],
        "deliverables": ["high_quality_dataset.csv", "selection_rules.md", "selection_summary.csv", "metadata.csv", "data_dictionary.csv", "README.md"],
        "peer": "Could the selected quality rule systematically remove the most impaired or difficult-to-monitor stations?",
        "oral": "What scientific question became more reliable, and what population became less represented?",
    },
    "group_06_multivariate": {
        "number": 6,
        "theme": "Multivariate analysis-ready dataset",
        "question": "How much completeness should be sacrificed to retain more environmental variables?",
        "product": "A documented station–week feature table prepared for later multivariate or ML analysis.",
        "available": ["data/station_week_indicator_matrix.csv", "data/feature_availability.csv", "data/retention_scenarios.csv"],
        "tasks": [
            "Verify the observational unit of the supplied wide table.",
            "Measure overlapping availability for different indicator combinations.",
            "Quantify complete-case loss in rows, stations, and weeks.",
            "Compare at least two feature-retention strategies.",
            "Propose an analysis-ready feature table without running the Date3 machine-learning lesson.",
            "Identify leakage risks, identifiers, outcomes, provenance fields, and inappropriate predictors.",
        ],
        "decisions": [
            "Which variables are essential and which can be omitted?",
            "Is imputation defensible, or should the product use complete cases?",
            "What is the acceptable tradeoff among variables, observations, stations, and temporal coverage?",
        ],
        "deliverables": ["multivariate_dataset.csv", "feature_availability.csv", "retention_summary.csv", "data_dictionary.csv", "README.md", "feature_design.md"],
        "peer": "Does each feature belong to the same observational unit, and could any proposed field leak an outcome?",
        "oral": "Which additional variable costs the most data, and why is that cost acceptable or unacceptable?",
    },
    "group_07_qc_provenance": {
        "number": 7,
        "theme": "Quality-control and provenance audit",
        "question": "Can every released value be traced to its source and processing history?",
        "product": "A provenance audit, QC summary, data-lineage description, and reproducibility-risk register.",
        "available": ["data/provenance_audit_sample.csv", "data/extraction_log.csv", "data/quality_control_report.csv", "data/dataset_validation.csv", "data/data_dictionary.csv"],
        "tasks": [
            "Trace selected observations through source PDF, page, table, row, extraction method, and QC fields.",
            "Compare the extraction log, QC summary, validation report, metadata, and final observation schema.",
            "Identify fields or transformations whose provenance is incomplete or ambiguous.",
            "Record silent assumptions and reproducibility risks without inventing test errors.",
            "Design a provenance table that could support verification five years from now.",
            "Explain which checks require reopening the source PDF and which can be automated.",
        ],
        "decisions": [
            "What is the minimum provenance needed for one observation?",
            "Which risks require correction and which require documentation?",
            "How should a reviewer sample records for source verification?",
        ],
        "deliverables": ["provenance_audit.csv", "qc_summary.csv", "reproducibility_risks.md", "data_lineage.md", "README.md", "audit_protocol.md"],
        "peer": "Can a reviewer trace a chosen value to a precise source location without asking the original analyst?",
        "oral": "Which missing provenance element would most threaten verification five years from now?",
    },
}


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def csv_write(frame: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding="utf-8-sig")


def challenge_brief(group):
    available = "\n".join(f"- `{item}`" for item in group["available"])
    tasks = "\n".join(f"{i}. {item}" for i, item in enumerate(group["tasks"], 1))
    decisions = "\n".join(f"- {item}" for item in group["decisions"])
    deliverables = "\n".join(f"- `{item}`" for item in group["deliverables"])
    return f'''# Group {group['number']} Challenge

## Mission

{group['theme']}.

## Scientific / Data Question

> {group['question']}

## Available Files

{available}

The full common data remain in `../../../outputs/`. Use relative paths. Do not copy the complete classroom dataset into a public repository.

## Required Tasks

{tasks}

## Decisions Your Team Must Make

{decisions}

Record the alternatives considered, the evidence used, and the effect of the final decision. AI-generated thresholds or rules are not evidence by themselves.

## AI Use

**AI tools are allowed.** Document the tool, the task it assisted with, the outputs you manually verified, and the decisions that remained human decisions. Complete `AI_verification_log.md` with at least two consequential examples.

## Deliverables

{deliverables}

Your final data product is: **{group['product']}**

Prepare the local `mock_release/` package. Keep `DOI: Not assigned — classroom mock release`. Do not publish to Zenodo and do not create or reserve a DOI.

## Peer Review

{group['peer']}

Use only these readiness ratings: **Ready for classroom release**, **Minor revision**, or **Major revision**.

## Oral Defense

{group['oral']}
'''


def group_readme(folder_name, group):
    return f'''# Group {group['number']}: {group['theme']}

This package uses a deterministic subset of the common CNEMC-derived Date2 outputs. Environmental measurements were not edited or fabricated.

## Start here

1. Read `challenge_brief.md` and `review_questions.md`.
2. Inspect every file under `data/` and the relevant common files under `../../../outputs/`.
3. Run `python starter_analysis.py` from this group folder.
4. Record analytical decisions and AI checks.
5. Build the required product and complete `mock_release/` locally.

## Reproducibility

The instructor can regenerate all group input files by running:

```bash
python ../prepare_group_datasets.py
```

Use relative paths in code. Do not overwrite files under `../../../outputs/`.

## Data source

China National Environmental Monitoring Centre weekly water-quality reports, extracted and cleaned through the Date2 teaching workflow. See Date2 output provenance fields and documentation.

## AI Assistance

AI tools may assist with code, documentation, and review. Your team remains responsible for scientific choices and verification. Include the completed `AI_verification_log.md` in your repository-ready package.
'''


def expected_outputs(group):
    lines = "\n".join(f"- `{name}`: complete this file with your team’s analysis and decisions." for name in group["deliverables"])
    return f'''# Expected Outputs

{lines}

## Common requirements

- Preserve environmental values and units.
- Use stable identifiers and document keys.
- State the observational unit.
- Use relative paths and reproducible code.
- Document filtering, missing-value handling, metadata, and provenance.
- Include an explicit data-source statement and AI Assistance statement.
- Keep large/full classroom data out of GitHub/Gitee; include code and small derived examples where appropriate.
- Complete the local mock release without publishing it.
'''


def review_questions(group):
    return f'''# Review Questions

## Dataset design

1. Is the observational unit explicit and consistent?
2. Does the final product answer the stated question?
3. {group['peer']}

## Reproducibility and provenance

4. Can the product be rebuilt from relative paths and documented code?
5. Are exclusions, transformations, and source fields traceable?
6. Are missing values distinguished from zeros and unavailable metadata?

## Responsible AI use

7. Which AI-assisted suggestion had the greatest potential to change the product?
8. What independent check supports accepting or rejecting that suggestion?

## Release readiness

9. Are metadata, data dictionary, citation, license status, and limitations consistent?
10. Choose one rating: **Ready for classroom release**, **Minor revision**, or **Major revision**. Give specific evidence.
'''


def starter_script(group_name, group):
    first_file = Path(group["available"][0]).name
    return f'''from pathlib import Path
import pandas as pd

GROUP_DIR = Path(__file__).resolve().parent
DATA_DIR = GROUP_DIR / "data"
OUTPUT_DIR = GROUP_DIR / "work_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

data = pd.read_csv(DATA_DIR / "{first_file}")
print("Rows:", len(data))
print("Columns:", data.columns.tolist())
print(data.head())

# TODO 1: Define the observational unit and primary key.
# TODO 2: Calculate evidence needed for your team decisions.
# TODO 3: Apply and document your chosen rule without changing source measurements.
# TODO 4: Export only your derived result to OUTPUT_DIR.
'''


def ai_log():
    return '''# AI Verification Log

## Entry 1

**AI tool:**

**Task assisted:**

**AI suggestion:**

**How we checked it:**

**Accepted / rejected:**

**Reason:**

**Human decision that remained:**

## Entry 2

**AI tool:**

**Task assisted:**

**AI suggestion:**

**How we checked it:**

**Accepted / rejected:**

**Reason:**

**Human decision that remained:**
'''


def mock_release_files(group_dir: Path, group):
    release = group_dir / "mock_release"
    release.mkdir(parents=True, exist_ok=True)
    title = group["theme"]
    write(release / "README.md", f'''# {title}: classroom mock release

Replace template rows with your final group product. Verify consistency across all release files.

DOI: Not assigned — classroom mock release

This directory is local teaching material. Do not upload it to Zenodo or create a DOI.
''')
    csv_write(pd.DataFrame(columns=["replace_with_final_product_fields"]), release / "dataset_or_data_product.csv")
    csv_write(pd.DataFrame(columns=["MetadataField", "Value", "Source", "Limitation"]), release / "metadata.csv")
    csv_write(pd.DataFrame(columns=["VariableName", "Definition", "DataType", "Unit", "MissingValueConvention", "Source", "QCNotes"]), release / "data_dictionary.csv")
    csv_write(pd.DataFrame(columns=["OutputField", "SourceFile", "SourceField", "Transformation", "Verification"]), release / "provenance.csv")
    write(release / "LICENSE.txt", '''No license selected — classroom mock release only.

The team must discuss reuse rights and source-data conditions before selecting a real license. This file does not grant permission for public redistribution.''')
    write(release / "CITATION.cff", f'''cff-version: 1.2.0
message: "Classroom mock citation only. DOI not assigned."
title: "{title}"
type: dataset
version: "classroom-mock"
date-released: "YYYY-MM-DD"
authors:
  - family-names: "Group {group['number']}"
    given-names: "Student Team"
identifiers:
  - type: other
    value: "DOI: Not assigned — classroom mock release"
''')
    metadata = {
        "title": title,
        "upload_type": "dataset",
        "description": group["product"],
        "creators": [{"name": f"Group {group['number']} Student Team"}],
        "keywords": ["water quality", "CNEMC-derived", "classroom mock release"],
        "license": "not selected - classroom mock",
        "doi": "Not assigned — classroom mock release",
        "publication_status": "local classroom mock only",
    }
    (release / "zenodo_metadata_mock.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_sources(source: Path):
    obs = pd.read_csv(source / "water_quality_dataset.csv")
    metadata = pd.read_csv(source / "water_quality_metadata.csv")
    availability = pd.read_csv(source / "availability_metrics.csv")
    dictionary = pd.read_csv(source / "data_dictionary.csv")
    extraction = pd.read_csv(source / "extraction_log.csv")
    qc = pd.read_csv(source / "quality_control_report.csv")
    validation = pd.read_csv(source / "dataset_validation.csv")
    return obs, metadata, availability, dictionary, extraction, qc, validation


def create_group_data(root: Path, source: Path):
    obs, metadata, availability, dictionary, extraction, qc, validation = load_sources(source)
    results = {}

    # Group 1: all actual dissolved-oxygen rows, including explicitly reported missing rows.
    do = obs[obs["IndicatorsName"].eq("Dissolved oxygen")].copy()
    do_cov = do.groupby(["MonitoringLocationIdentifier", "MonitoringLocationName"], dropna=False).agg(
        ReportingRows=("RecordIdentifier", "size"), AvailableValues=("Value", "count"),
        MissingValues=("Value", lambda s: int(s.isna().sum())),
        FirstPeriod=("ReportPeriodEnd", "min"), LastPeriod=("ReportPeriodEnd", "max"),
        DistinctWeeks=("ReportWeek", "nunique"), QCReviewRows=("QCFlag", lambda s: int((s != "pass").sum())),
    ).reset_index()
    do_cov["MissingPercent"] = do_cov["MissingValues"] / do_cov["ReportingRows"] * 100
    g = root / "group_01_DO" / "data"
    csv_write(do, g / "do_observations.csv")
    csv_write(do_cov, g / "do_station_coverage.csv")
    csv_write(metadata[metadata["IndicatorsName"].eq("Dissolved oxygen")], g / "do_metadata.csv")
    csv_write(dictionary, g / "data_dictionary.csv")
    results["group_01_DO"] = {"rows": len(do), "indicators": ["Dissolved oxygen"]}

    # Group 2: only the nutrient-related indicator that actually exists.
    nutrient_names = [name for name in obs["IndicatorsName"].dropna().unique() if name == "Ammonia nitrogen"]
    nutrients = obs[obs["IndicatorsName"].isin(nutrient_names)].copy()
    nutrient_cov = nutrients.groupby(["MonitoringLocationIdentifier", "MonitoringLocationName", "IndicatorsName", "Unit"], dropna=False).agg(
        ReportingRows=("RecordIdentifier", "size"), AvailableValues=("Value", "count"),
        MissingValues=("Value", lambda s: int(s.isna().sum())), DistinctWeeks=("ReportWeek", "nunique"),
        FirstPeriod=("ReportPeriodEnd", "min"), LastPeriod=("ReportPeriodEnd", "max"),
    ).reset_index()
    indicator_catalog = obs.groupby(["IndicatorsName", "Unit"], dropna=False).agg(
        Rows=("RecordIdentifier", "size"), AvailableValues=("Value", "count"),
        Stations=("MonitoringLocationIdentifier", "nunique"), Weeks=("ReportWeek", "nunique"),
    ).reset_index()
    g = root / "group_02_nutrients" / "data"
    csv_write(nutrients, g / "nutrient_observations.csv")
    csv_write(nutrient_cov, g / "nutrient_coverage.csv")
    csv_write(indicator_catalog, g / "indicator_catalog.csv")
    csv_write(metadata[metadata["IndicatorsName"].isin(nutrient_names)], g / "nutrient_metadata.csv")
    results["group_02_nutrients"] = {"rows": len(nutrients), "indicators": nutrient_names}

    # Group 3: a manageable, deterministic set of the 24 stations with the most available values.
    station_rank = obs.groupby(["MonitoringLocationIdentifier", "MonitoringLocationName"], dropna=False).agg(
        AvailableValues=("Value", "count"), ReportingRows=("RecordIdentifier", "size"),
        Indicators=("IndicatorsName", "nunique"), Weeks=("ReportWeek", "nunique"),
    ).reset_index().sort_values(["AvailableValues", "MonitoringLocationIdentifier"], ascending=[False, True])
    candidates = station_rank.head(24).copy()
    candidate_obs = obs[obs["MonitoringLocationIdentifier"].isin(candidates["MonitoringLocationIdentifier"])].copy()
    station_indicator = metadata.merge(availability, on=["MonitoringLocationIdentifier", "IndicatorsName"], how="left", suffixes=("", "_Recalculated"))
    station_indicator = station_indicator[station_indicator["MonitoringLocationIdentifier"].isin(candidates["MonitoringLocationIdentifier"])]
    g = root / "group_03_station_comparison" / "data"
    csv_write(candidate_obs, g / "candidate_station_observations.csv")
    csv_write(station_indicator, g / "station_indicator_coverage.csv")
    csv_write(candidates, g / "candidate_station_inventory.csv")
    results["group_03_station_comparison"] = {"rows": len(candidate_obs), "indicators": sorted(candidate_obs["IndicatorsName"].unique())}

    # Group 4: coverage metrics plus gap-pattern evidence.
    weeks = sorted(obs["ReportWeek"].dropna().astype(int).unique())
    def gap_stats(group):
        observed = set(group.loc[group["Value"].notna(), "ReportWeek"].astype(int))
        present = [week in observed for week in weeks]
        longest_missing = current = 0
        gap_segments = 0
        previous_missing = False
        for value in present:
            if not value:
                current += 1
                longest_missing = max(longest_missing, current)
                if not previous_missing:
                    gap_segments += 1
                previous_missing = True
            else:
                current = 0
                previous_missing = False
        return pd.Series({"ExpectedWeeks": len(weeks), "ObservedWeeks": sum(present), "MissingWeeks": len(weeks)-sum(present), "LongestMissingRun": longest_missing, "MissingGapSegments": gap_segments})
    gap_summary = obs.groupby(["MonitoringLocationIdentifier", "MonitoringLocationName", "IndicatorsName"], dropna=False).apply(gap_stats, include_groups=False).reset_index()
    coverage_defs = pd.DataFrame([
        ("DataIntensity", "Non-missing reported values divided by extracted reporting periods", "station-indicator"),
        ("OverallAvailability", "Non-missing reported values divided by expected report weeks", "station-indicator"),
        ("LongestAvailability", "Longest consecutive observed run divided by expected report weeks", "station-indicator"),
        ("Continuity", "Longest consecutive observed run divided by observed weeks", "station-indicator"),
    ], columns=["Field", "Date2Definition", "UnitOfAnalysis"])
    g = root / "group_04_temporal_coverage" / "data"
    csv_write(metadata.merge(availability, on=["MonitoringLocationIdentifier", "IndicatorsName"], how="left", suffixes=("", "_AvailabilityFile")), g / "availability_metrics.csv")
    csv_write(gap_summary, g / "gap_pattern_summary.csv")
    csv_write(coverage_defs, g / "coverage_field_definitions.csv")
    results["group_04_temporal_coverage"] = {"rows": len(gap_summary), "indicators": sorted(gap_summary["IndicatorsName"].unique())}

    # Group 5: decision table only; teams choose their own strict/moderate thresholds.
    station_qc = obs.groupby(["MonitoringLocationIdentifier", "MonitoringLocationName", "IndicatorsName"], dropna=False).agg(
        ReportingRows=("RecordIdentifier", "size"), AvailableValues=("Value", "count"),
        MissingValues=("Value", lambda s: int(s.isna().sum())), PassRows=("QCFlag", lambda s: int((s == "pass").sum())),
        ReviewRows=("QCFlag", lambda s: int((s != "pass").sum())), DistinctWeeks=("ReportWeek", "nunique"),
    ).reset_index()
    quality_input = metadata.merge(station_qc, on=["MonitoringLocationIdentifier", "MonitoringLocationName", "IndicatorsName"], how="left")
    source_inventory = obs.groupby(["SourcePDF", "IndicatorsName", "Unit"], dropna=False).agg(Rows=("RecordIdentifier", "size"), AvailableValues=("Value", "count"), ReviewRows=("QCFlag", lambda s: int((s != "pass").sum()))).reset_index()
    g = root / "group_05_high_quality_dataset" / "data"
    csv_write(quality_input, g / "quality_selection_input.csv")
    csv_write(qc, g / "qc_flag_summary.csv")
    csv_write(source_inventory, g / "source_indicator_inventory.csv")
    results["group_05_high_quality_dataset"] = {"rows": len(quality_input), "indicators": sorted(quality_input["IndicatorsName"].unique())}

    # Group 6: station-week matrix. Values remain exact; no imputation is performed.
    identifiers = ["MonitoringLocationIdentifier", "MonitoringLocationName", "ReportWeek", "ReportPeriodStart", "ReportPeriodEnd"]
    # Keep only station-week combinations that occur in the source. dropna=False would
    # construct a Cartesian product across identifier levels and invent empty rows.
    wide = obs.pivot_table(index=identifiers, columns="IndicatorsName", values="Value", aggfunc="first").reset_index()
    wide.columns.name = None
    indicators = sorted(obs["IndicatorsName"].dropna().unique())
    feature_availability = pd.DataFrame({
        "IndicatorsName": indicators,
        "AvailableValues": [int(wide[name].notna().sum()) for name in indicators],
        "MissingValues": [int(wide[name].isna().sum()) for name in indicators],
        "AvailablePercent": [float(wide[name].notna().mean() * 100) for name in indicators],
    })
    scenarios = []
    for count in range(1, len(indicators) + 1):
        for combo in __import__("itertools").combinations(indicators, count):
            mask = wide[list(combo)].notna().all(axis=1)
            scenarios.append({"FeatureSet": " + ".join(combo), "NumberOfFeatures": count, "CompleteRows": int(mask.sum()), "Stations": int(wide.loc[mask, "MonitoringLocationIdentifier"].nunique()), "Weeks": int(wide.loc[mask, "ReportWeek"].nunique())})
    g = root / "group_06_multivariate" / "data"
    csv_write(wide, g / "station_week_indicator_matrix.csv")
    csv_write(feature_availability, g / "feature_availability.csv")
    csv_write(pd.DataFrame(scenarios), g / "retention_scenarios.csv")
    results["group_06_multivariate"] = {"rows": len(wide), "indicators": indicators}

    # Group 7: deterministic audit sample: every QC-review row plus systematic source/indicator samples.
    review_rows = obs[obs["QCFlag"].ne("pass")]
    pass_rows = obs[obs["QCFlag"].eq("pass")].sort_values(["SourcePDF", "IndicatorsName", "MonitoringLocationIdentifier", "ReportWeek"]).groupby(["SourcePDF", "IndicatorsName"], group_keys=False).head(2)
    audit_sample = pd.concat([review_rows, pass_rows], ignore_index=True).drop_duplicates("RecordIdentifier").sort_values("RecordIdentifier")
    g = root / "group_07_qc_provenance" / "data"
    csv_write(audit_sample, g / "provenance_audit_sample.csv")
    csv_write(extraction, g / "extraction_log.csv")
    csv_write(qc, g / "quality_control_report.csv")
    csv_write(validation, g / "dataset_validation.csv")
    csv_write(dictionary, g / "data_dictionary.csv")
    results["group_07_qc_provenance"] = {"rows": len(audit_sample), "indicators": sorted(audit_sample["IndicatorsName"].unique())}

    return results


def common_readme(results):
    rows = []
    for folder, group in GROUPS.items():
        rows.append(f"| {group['number']} | {group['theme']} | {group['question']} | {group['product']} |")
    table = "\n".join(rows)
    return f'''# Date2 Group Challenges

All seven teams use one common CNEMC-derived Date2 dataset. Each team develops a different research-data product and answers a different scientific or data-engineering question.

Environmental values are not fabricated. Missing coordinates, station types, dates, indicators, or metadata must remain unavailable unless supported by Date2 outputs.

AI tools are allowed. Every AI-assisted decision must be documented and manually verified. Code and documentation may be prepared for GitHub or Gitee, but the full classroom dataset does not need to be placed in a remote repository.

Each group prepares a **local mock release**. Do not publish a Zenodo record, create a DOI, reserve a DOI, request credentials, or push a remote repository.

## Group themes

| Group | Theme | Main Question | Final Data Product |
| ----- | ----- | ------------- | ------------------ |
{table}

## Shared source

- `../outputs/water_quality_dataset.csv`
- `../outputs/water_quality_metadata.csv`
- `../outputs/availability_metrics.csv`
- `../outputs/data_dictionary.csv`
- Date2 extraction, QC, and validation reports

## Regenerate group inputs

From this directory:

```bash
python prepare_group_datasets.py
python validate_group_packages.py
```

The preparation script applies deterministic filters and reshaping. It does not edit Date2 source outputs or environmental measurements.
'''


def instructor_files(root: Path):
    instructor = root / "instructor"
    write(instructor / "review_assignment.md", '''# Cross-Group Review Assignment

| Reviewing group | Reviews group |
| ---: | ---: |
| Group 1 | Group 4 |
| Group 4 | Group 7 |
| Group 7 | Group 3 |
| Group 3 | Group 6 |
| Group 6 | Group 2 |
| Group 2 | Group 5 |
| Group 5 | Group 1 |

Review dataset design, documentation, reproducibility, metadata, provenance, assumptions, responsible AI use, and release readiness.

Use only: **Ready for classroom release**, **Minor revision**, or **Major revision**.
''')
    write(instructor / "scoring_rubric.md", '''# Common Scoring Rubric

| Criterion | Points |
| --- | ---: |
| Scientific/data-product design | 20 |
| Reproducibility | 20 |
| Metadata and documentation | 15 |
| Provenance and traceability | 15 |
| Scientific justification of decisions | 10 |
| Peer-review quality | 10 |
| Responsible AI use and verification | 5 |
| Oral defense | 5 |
| **Total** | **100** |

Do not award points for code volume. Evaluate whether the code is necessary, reproducible, and scientifically justified.
''')
    questions = [
        "Why did you exclude this station?", "What happens if you relax your completeness rule?",
        "Where does this column originate?", "Which step was suggested by AI?",
        "How did you verify that suggestion?", "Why is this field metadata rather than observation data?",
        "What information would another researcher need to reproduce this result?",
        "Which assumption is most likely to change your final dataset?",
        "Why should this dataset not automatically be uploaded to a public repository?",
        "What is the tradeoff between completeness and representativeness?",
        "Could your filtering rule introduce selection bias?",
        "What result would change if missing weeks were distributed differently?",
        "Which value can you trace to a PDF page and row?", "What does your observational unit represent?",
    ]
    write(instructor / "instructor_questions.md", "# Instructor Challenge Questions\n\n" + "\n".join(f"- {q}" for q in questions))
    write(instructor / "expected_learning_outcomes.md", '''# Expected Learning Outcomes

Students should be able to:

- define an observational unit and a defensible data product;
- balance completeness, continuity, comparability, and representativeness;
- preserve units, missingness, identifiers, metadata, and provenance;
- build deterministic and reviewable data-preparation code;
- distinguish source observations from transformations and derived summaries;
- supervise AI-assisted analysis and document verification;
- review another team’s release for reproducibility and traceability;
- prepare local research-data release documentation without claiming a DOI or publishing data.
''')
    write(instructor / "overview.md", '''# Instructor Overview

Seven groups share one Date2 source but produce distinct products: indicator-specific, nutrient-focused, station-comparison, temporal-coverage, quality-filtered, multivariate, and provenance-audit products.

## Classroom sequence

1. Introduce the common Date2 source and its limitations.
2. Assign group folders and require teams to inspect their inputs before choosing rules.
3. Require an AI Verification Log during work, not after completion.
4. Conduct oral defenses using randomly assigned questions.
5. Use the review ring and common readiness ratings.
6. Score all groups with the same 100-point rubric.

## Actual-data adaptations

- Only ammonia nitrogen is available as a nutrient-related indicator; TP and TN are absent.
- Verified coordinates and monitoring-location types are unavailable, so no group should invent spatial comparisons.
- Reporting periods are weekly summaries, not exact sampling timestamps.
- Date2 contains four reported indicators: pH, dissolved oxygen, permanganate index, and ammonia nitrogen.

## Instructor checks

Run `python prepare_group_datasets.py` and `python validate_group_packages.py`. The scripts use relative paths and never overwrite Date2 source outputs.
''')


def delivered_prepare_script():
    # A compact wrapper reuses the deterministic builder copied into the package.
    return '''from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent
builder = ROOT / "_package_builder.py"
namespace = runpy.run_path(str(builder))
results = namespace["create_group_data"](ROOT, ROOT.parent / "outputs")
print("Regenerated group data packages:")
for group, summary in results.items():
    print(f"- {group}: {summary['rows']} primary input rows; indicators={summary['indicators']}")
'''


def delivered_validation_script():
    return '''from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parent
required_group_files = [
    "README.md", "challenge_brief.md", "expected_outputs.md", "review_questions.md",
    "AI_verification_log.md", ".gitignore", "requirements.txt", "starter_analysis.py",
]
required_release_files = [
    "README.md", "dataset_or_data_product.csv", "metadata.csv", "data_dictionary.csv",
    "provenance.csv", "LICENSE.txt", "CITATION.cff", "zenodo_metadata_mock.json",
]
errors = []
for group_dir in sorted(ROOT.glob("group_??_*")):
    for name in required_group_files:
        if not (group_dir / name).is_file(): errors.append(f"{group_dir.name}: missing {name}")
    for name in required_release_files:
        if not (group_dir / "mock_release" / name).is_file(): errors.append(f"{group_dir.name}: missing mock_release/{name}")
    csv_files = list((group_dir / "data").glob("*.csv"))
    if not csv_files: errors.append(f"{group_dir.name}: no CSV inputs")
    for csv_file in csv_files:
        try: pd.read_csv(csv_file)
        except Exception as exc: errors.append(f"{csv_file}: {exc}")
    metadata = json.loads((group_dir / "mock_release" / "zenodo_metadata_mock.json").read_text(encoding="utf-8"))
    if metadata.get("doi") != "Not assigned — classroom mock release": errors.append(f"{group_dir.name}: mock DOI text changed")

expected_groups = 7
if len(list(ROOT.glob("group_??_*"))) != expected_groups:
    errors.append("Expected seven group folders")
if errors:
    raise SystemExit("VALIDATION FAILED\\n" + "\\n".join(errors))
print("All seven group packages passed structural and CSV-readability validation.")
print("No upload or DOI operation is performed by this script.")
'''


def build(source: Path, root: Path):
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    results = create_group_data(root, source)

    for folder, group in GROUPS.items():
        group_dir = root / folder
        write(group_dir / "README.md", group_readme(folder, group))
        write(group_dir / "challenge_brief.md", challenge_brief(group))
        write(group_dir / "expected_outputs.md", expected_outputs(group))
        write(group_dir / "review_questions.md", review_questions(group))
        write(group_dir / "AI_verification_log.md", ai_log())
        write(group_dir / ".gitignore", '''work_outputs/
.ipynb_checkpoints/
__pycache__/
*.pyc
.DS_Store
# Keep the full shared Date2 dataset outside a public group repository.
''')
        write(group_dir / "requirements.txt", "pandas>=2.2,<3\nnumpy>=1.26,<3")
        write(group_dir / "starter_analysis.py", starter_script(folder, group))
        mock_release_files(group_dir, group)

    write(root / "README.md", common_readme(results))
    instructor_files(root)
    write(root / "prepare_group_datasets.py", delivered_prepare_script())
    write(root / "validate_group_packages.py", delivered_validation_script())
    # Copy this builder as an implementation module used by the delivered wrapper.
    shutil.copy2(Path(__file__), root / "_package_builder.py")
    (root / "package_manifest.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.source.resolve(), args.output.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
