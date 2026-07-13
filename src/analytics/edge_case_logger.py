"""
Sprint 2 - Day 13
Ratio Edge Case Logger
"""

import sqlite3
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql("""
SELECT
    id AS company_id,
    company_name,
    roce_percentage,
    roe_percentage
FROM companies
""", conn)

engine = pd.read_sql("""
SELECT
    company_id,
    year,
    return_on_equity_pct
FROM financial_ratios_engine
""", conn)

latest = (
    engine
    .sort_values("year")
    .groupby("company_id")
    .tail(1)
)

merged = latest.merge(
    companies,
    on="company_id",
    how="left"
)

log = []

for _, row in merged.iterrows():

    # ROE comparison
    if (
        pd.notna(row["roe_percentage"])
        and pd.notna(row["return_on_equity_pct"])
    ):

        diff = abs(
            row["roe_percentage"]
            - row["return_on_equity_pct"]
        )

        if diff > 5:

            log.append({
                "company_id": row["company_id"],
                "company_name": row["company_name"],
                "metric": "ROE",
                "source_value": row["roe_percentage"],
                "computed_value": row["return_on_equity_pct"],
                "difference": round(diff, 2),
                "category": "Source Data / Version Difference"
            })

log_df = pd.DataFrame(log)

log_df.to_csv(
    "output/ratio_edge_cases.csv",
    index=False
)

with open("output/ratio_edge_cases.log", "w") as f:

    f.write("=" * 60 + "\n")
    f.write("RATIO EDGE CASE LOG\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"Total anomalies: {len(log_df)}\n\n")

    for _, row in log_df.iterrows():

        f.write(
            f"{row['company_id']} | "
            f"{row['metric']} | "
            f"Source={row['source_value']} | "
            f"Computed={row['computed_value']} | "
            f"Diff={row['difference']} | "
            f"{row['category']}\n"
        )

print("=" * 60)
print("Edge Case Log Generated")
print("=" * 60)
print(f"Anomalies Found: {len(log_df)}")

conn.close()