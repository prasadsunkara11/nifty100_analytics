"""
Data Quality Validator
Sprint 1 - Day 3
"""

import os
import pandas as pd

# ----------------------------
# Create output folder
# ----------------------------
os.makedirs("output", exist_ok=True)

# ----------------------------
# Load datasets
# ----------------------------
companies = pd.read_excel(
    "data/processed/companies_clean.xlsx",
)

profit = pd.read_excel(
    "data/processed/profitandloss_clean.xlsx"
)

balance = pd.read_excel(
    "data/processed/balancesheet_clean.xlsx",
)

cashflow = pd.read_excel(
    "data/processed/cashflow_clean.xlsx",
)

failures = []

# ==========================================================
# DQ-01
# Duplicate Company IDs
# ==========================================================

duplicates = companies[
    companies.duplicated(
        subset=["id"],
        keep=False
    )
]

for _, row in duplicates.iterrows():

    failures.append([
        "DQ-01",
        "CRITICAL",
        "Duplicate Company ID",
        row["id"]
    ])


# ==========================================================
# DQ-02
# Duplicate Company + Year
# ==========================================================

duplicate_cols = [
    c for c in profit.columns
    if c != "id"
]

duplicates = profit[
    profit.duplicated(
        subset=duplicate_cols,
        keep=False
    )
]

for _, row in duplicates.iterrows():

    failures.append([
        "DQ-02",
        "CRITICAL",
        "Duplicate Company-Year",
        f'{row["company_id"]} - {row["year"]}'
    ])


# ==========================================================
# DQ-03
# Foreign Key Integrity
# ==========================================================

company_ids = set(
    companies["id"].astype(str).str.strip()
)

for _, row in profit.iterrows():

    company = str(row["company_id"]).strip()

    if company not in company_ids:

        failures.append([
            "DQ-03",
            "CRITICAL",
            "Invalid Company ID",
            company
        ])


# ==========================================================
# DQ-04
# Sales must be positive
# ==========================================================

profit["sales"] = pd.to_numeric(
    profit["sales"],
    errors="coerce"
)

invalid_sales = profit[
    profit["sales"] <= 0
]

for _, row in invalid_sales.iterrows():

    failures.append([
        "DQ-04",
        "WARNING",
        "Sales <= 0",
        row["company_id"]
    ])


# ==========================================================
# DQ-05
# OPM Range
# ==========================================================

profit["opm_percentage"] = pd.to_numeric(
    profit["opm_percentage"],
    errors="coerce"
)

invalid_opm = profit[
    (profit["opm_percentage"] < -100)
    |
    (profit["opm_percentage"] > 100)
]

for _, row in invalid_opm.iterrows():

    failures.append([
        "DQ-05",
        "WARNING",
        "Invalid OPM %",
        row["company_id"]
    ])


# ==========================================================
# DQ-06
# Tax Percentage
# ==========================================================

profit["tax_percentage"] = pd.to_numeric(
    profit["tax_percentage"],
    errors="coerce"
)

invalid_tax = profit[
    (profit["tax_percentage"] < 0)
    |
    (profit["tax_percentage"] > 100)
]

for _, row in invalid_tax.iterrows():

    failures.append([
        "DQ-06",
        "WARNING",
        "Invalid Tax %",
        row["company_id"]
    ])


# ==========================================================
# DQ-07
# EPS Missing
# ==========================================================

missing_eps = profit[
    profit["eps"].isna()
]

for _, row in missing_eps.iterrows():

    failures.append([
        "DQ-07",
        "WARNING",
        "Missing EPS",
        row["company_id"]
    ])


# ==========================================================
# DQ-08
# Duplicate Balance Sheet Records
# ==========================================================

duplicates = balance[
    balance.duplicated(
        subset=["company_id", "year"],
        keep=False
    )
]

for _, row in duplicates.iterrows():

    failures.append([
        "DQ-08",
        "CRITICAL",
        "Duplicate Balance Sheet",
        row["company_id"]
    ])


# ==========================================================
# DQ-09
# Duplicate Cash Flow Records
# ==========================================================

duplicates = cashflow[
    cashflow.duplicated(
        subset=["company_id", "year"],
        keep=False
    )
]

for _, row in duplicates.iterrows():

    failures.append([
        "DQ-09",
        "CRITICAL",
        "Duplicate Cash Flow",
        row["company_id"]
    ])


# ==========================================================
# DQ-10
# Missing Years
# ==========================================================

missing_year = profit[
    profit["year"].isna()
]

for _, row in missing_year.iterrows():

    failures.append([
        "DQ-10",
        "WARNING",
        "Missing Year",
        row["company_id"]
    ])


# ==========================================================
# Save Report
# ==========================================================

result = pd.DataFrame(

    failures,

    columns=[
        "Rule",
        "Severity",
        "Message",
        "Value"
    ]
)

result.to_csv(
    "output/validation_failures.csv",
    index=False
)

print("=" * 50)
print("DATA QUALITY VALIDATION COMPLETE")
print("=" * 50)

print(f"Total Failures : {len(result)}")

print()

if len(result) == 0:
    print("No Data Quality Issues Found.")
else:
    print(result.head(20))

print()

print("Validation report saved to:")
print("output/validation_failures.csv")