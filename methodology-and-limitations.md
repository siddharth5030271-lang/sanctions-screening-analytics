# Methodology and limitations

## Objective
Demonstrate how customer-name screening can generate candidate alerts by comparing synthetic customer names with a synthetic sanctions reference list, then evaluate the consolidated output against synthetic ground-truth labels.

## Population
- 500 customer records: 50 labelled `MATCH` and 450 labelled `NO_MATCH`.
- 50 sanctions-reference rows, including one row with a blank screening name and malformed-looking entity number.
- 68 candidate-level alert rows across 49 distinct customer IDs.

## Consolidation logic
The delivered `Final_Screening_Results` sheet contains one row per customer. A customer is flagged when its consolidated candidate count is greater than zero. The status `Potential Match - Review` indicates an alert for investigation, not a confirmed sanctions match.

## Evaluation
The workbook compares the candidate flag with the synthetic `Ground_Truth` field:

| | Predicted alert | No alert |
|---|---:|---:|
| Ground-truth MATCH | 49 (TP) | 1 (FN) |
| Ground-truth NO_MATCH | 0 (FP) | 450 (TN) |

- Precision = TP / (TP + FP) = 49 / 49 = 100%.
- Recall = TP / (TP + FN) = 49 / 50 = 98%.
- Accuracy = (TP + TN) / 500 = 499 / 500 = 99.8%.
- F1 = 2 × Precision × Recall / (Precision + Recall) = 98.99%.

## Exceptions retained
1. `CUST045` has no usable customer name or screening name. The record remains a false negative; no match was fabricated.
2. One sanctions-reference row has a blank `Screening_Name` and malformed-looking `ent_num`. It needs source verification.
3. Embedded Power Query refreshability was not validated. This deliverable is a manually consolidated workbook, not a repaired live-refresh pipeline.

## Operational cautions
- Fuzzy name similarity creates candidate alerts, not legal determinations.
- Production screening requires authoritative, current lists; aliases and transliterations; risk-based tuning; documented thresholds; analyst review; audit trails; and governance.
- Metrics on a small synthetic dataset do not establish production performance.
