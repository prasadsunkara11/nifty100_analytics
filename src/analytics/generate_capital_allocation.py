"""
Generate Capital Allocation Report
Sprint 2 - Day 11
"""

import sqlite3
import pandas as pd

from cashflow_kpis import (
    cfo_quality_score,
    capital_allocation_pattern
)

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    c.company_id,
    c.year,
    c.operating_activity,
    c.investing_activity,
    c.financing_activity,
    p.net_profit
FROM cashflow c
LEFT JOIN profitandloss p
ON c.company_id = p.company_id
AND c.year = p.year
"""

df = pd.read_sql(query, conn)

records = []

for _, row in df.iterrows():

    quality = cfo_quality_score(
        row["operating_activity"],
        row["net_profit"] if pd.notna(row["net_profit"]) else 0
    )

    pattern = capital_allocation_pattern(
        row["operating_activity"],
        row["investing_activity"],
        row["financing_activity"],
        quality
    )

    records.append({
        "company_id": row["company_id"],
        "year": row["year"],
        "cfo_sign": "+" if row["operating_activity"] > 0 else "-",
        "cfi_sign": "+" if row["investing_activity"] > 0 else "-",
        "cff_sign": "+" if row["financing_activity"] > 0 else "-",
        "pattern_label": pattern
    })

output = pd.DataFrame(records)

output.to_csv(
    "output/capital_allocation.csv",
    index=False
)

print(output.head())

print()
print("Generated:", len(output), "rows")

conn.close()