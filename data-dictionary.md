# Data dictionary

## Customer input / final results

| Field | Meaning |
|---|---|
| `Customer_ID` | Synthetic customer identifier |
| `Customer_Name` | Customer's supplied name |
| `Customer_DOB` | Synthetic date of birth |
| `Customer_Nationality` | Synthetic nationality field |
| `Ground_Truth` | Synthetic evaluation label (`MATCH` / `NO_MATCH`) |
| `Variation_Type` | Synthetic test-case category |
| `Screening_Name` | Name string used for screening |
| `Candidate_Count` | Number of candidate rows consolidated for the customer |
| `ent_num` | Reference entity number where a candidate is present |
| `Sanctions_Matched_Name` | Name from the reference candidate output |
| `Name_Source` | Reference-name source/type |
| `Candidate_Flag` | 1 when one or more candidate rows exist; otherwise 0 |
| `Final_Screening_Status` | `Potential Match - Review` or `No Match` |
| `Evaluation_Result` | TP, FP, TN, or FN classification against synthetic ground truth |

## Sanctions reference

| Field | Meaning |
|---|---|
| `ent_num` | Synthetic/reference entity identifier as supplied in workbook |
| `Screening_Name` | Reference name used for comparison |
| `Name_Source` | Source/type label associated with the name |

## Interpretation
A `Potential Match - Review` is not a confirmed sanctions hit. `Ground_Truth` exists for synthetic evaluation only and would not be available as an operational screening input.
