# Sanctions Screening Analytics | Excel & Power Query

A portfolio project demonstrating a sanctions-name screening workflow using **synthetic customer data**, a sanctions reference list, candidate-alert consolidation, data-quality review, and classification metrics.

> **Important:** This repository contains a manually consolidated analytical workbook. The embedded Power Query refresh process has not been validated. Potential matches are alerts for human review, not confirmed sanctions hits.

## Project at a glance

| Item | Result |
|---|---:|
| Synthetic customer records | 500 |
| Synthetic sanctions-reference rows | 50 |
| Candidate-level alert rows | 68 |
| Customers with at least one candidate | 49 |
| True positives | 49 |
| False positives | 0 |
| True negatives | 450 |
| False negatives | 1 |

## Evaluation metrics

| Metric | Result |
|---|---:|
| Precision | 100.00% |
| Recall | 98.00% |
| Accuracy | 99.80% |
| F1 score | 98.99% |

These are results calculated against the workbook's **synthetic ground-truth labels** and its consolidated candidate outputs. They are not evidence of real-world sanctions-screening effectiveness. The single false negative is retained and documented rather than being manually converted into a match.

## Workflow demonstrated

1. Prepare customer and sanctions-reference tables.
2. Inspect and clean name fields for screening.
3. Use fuzzy name-matching concepts to identify candidate records.
4. Consolidate candidate-level results to one row per customer.
5. Classify each customer as a potential-match alert or no candidate.
6. Compare the alert flag with synthetic ground-truth labels.
7. Document data-quality exceptions and workflow limitations.

## Workbook contents

Open `workbook/Sanctions_Screening_Project_Final_Manually_Repaired.xlsx`.

| Worksheet | Description |
|---|---|
| `Project_Overview` | Project scope and status |
| `Dashboard` | Confusion matrix and performance metrics |
| `Final_Screening_Results` | One row per customer (500 rows) |
| `Candidate_Alerts` | Candidate-level alert output (68 rows) |
| `Customer_Input` | Synthetic customer input |
| `Sanctions_Reference` | Synthetic sanctions reference data |
| `Data_Quality_Exceptions` | Known source and workflow issues |
| `Methodology` | Consolidation and evaluation notes |

## Key data-quality findings

- `CUST045` has a blank customer name and blank screening name. It is retained as the one missed seeded positive; no name or match was invented.
- One sanctions-reference row has a blank `Screening_Name` and a malformed-looking entity number. It requires validation against an authoritative source before any operational use.
- The workbook's embedded Power Query queries include duplicate/output artifacts and a query error. The delivered workbook consolidates worksheet outputs; it does **not** claim that live Power Query refresh is repaired or reproducible.

## Repository structure

```text
sanctions-screening-analytics/
├── README.md
├── LICENSE
├── .gitignore
├── linkedin/
│   └── LINKEDIN_PROJECT_POST.md
├── workbook/
│   └── Sanctions_Screening_Project_Final_Manually_Repaired.xlsx
├── docs/
│   ├── methodology-and-limitations.md
│   └── data-dictionary.md
└── scripts/
    └── validate_workbook.py
```

## How to review

1. Download the workbook from `workbook/`.
2. Start with `Dashboard`.
3. Review `Final_Screening_Results` and `Candidate_Alerts`.
4. Read `Data_Quality_Exceptions` and `Methodology` before interpreting the metrics.

## Skills demonstrated

Excel • Power Query concepts • fuzzy matching • data cleaning • data quality assessment • candidate-alert analysis • confusion matrix • precision • recall • F1 score • compliance analytics

## Disclaimer

All records are synthetic and intended solely for educational and portfolio demonstration. This project is not a production screening solution, legal advice, or a substitute for authoritative sanctions-list data, validated screening software, human investigation, or compliance controls.
