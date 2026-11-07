#!/usr/bin/env python3
"""Validate workbook structure and the reported portfolio metrics."""
from pathlib import Path
from openpyxl import load_workbook

WORKBOOK = Path(__file__).resolve().parents[1] / "workbook" / "Sanctions_Screening_Project_Final_Manually_Repaired.xlsx"

def main():
    if not WORKBOOK.exists():
        raise FileNotFoundError(WORKBOOK)
    wb = load_workbook(WORKBOOK, data_only=True, read_only=True)
    required = {"Project_Overview", "Dashboard", "Final_Screening_Results",
                "Candidate_Alerts", "Customer_Input", "Sanctions_Reference",
                "Data_Quality_Exceptions", "Methodology"}
    missing = required.difference(wb.sheetnames)
    if missing:
        raise AssertionError(f"Missing worksheets: {sorted(missing)}")
    dashboard = wb["Dashboard"]
    metrics = {dashboard.cell(r, 1).value: dashboard.cell(r, 2).value for r in range(4, 12)}
    expected = {"True Positive": 49, "False Positive": 0,
                "True Negative": 450, "False Negative": 1}
    for key, value in expected.items():
        if metrics.get(key) != value:
            raise AssertionError(f"{key}: expected {value}, found {metrics.get(key)}")
    if wb["Final_Screening_Results"].max_row - 1 != 500:
        raise AssertionError("Expected 500 customer rows")
    if wb["Candidate_Alerts"].max_row - 1 != 68:
        raise AssertionError("Expected 68 candidate rows")
    print("Workbook structure and reported outputs validated.")
    print("500 customers | 68 candidate rows | TP 49 | FP 0 | TN 450 | FN 1")
    print("This script does not validate embedded Power Query refreshability.")

if __name__ == "__main__":
    main()
