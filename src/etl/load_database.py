"""
Load all cleaned datasets into SQLite
"""

import sqlite3
import pandas as pd
import os

DB_PATH = "db/nifty100.db"
DATA_PATH = "data/processed"

TABLES = {
    "companies_clean.xlsx": "companies",
    "profitandloss_clean.xlsx": "profitandloss",
    "balancesheet_clean.xlsx": "balancesheet",
    "cashflow_clean.xlsx": "cashflow",
    "analysis_clean.xlsx": "analysis",
    "documents_clean.xlsx": "documents",
    "financial_ratios_clean.xlsx": "financial_ratios",
    "market_cap_clean.xlsx": "market_cap",
    "peer_groups_clean.xlsx": "peer_groups",
    "prosandcons_clean.xlsx": "prosandcons",
    "sectors_clean.xlsx": "sectors",
    "stock_prices_clean.xlsx": "stock_prices"
}

conn = sqlite3.connect(DB_PATH)

load_audit = []

for file, table in TABLES.items():

    path = os.path.join(DATA_PATH, file)

    df = pd.read_excel(path)

    print(f"Loading {table}...")

    try:

        df.to_sql(
            table,
            conn,
            if_exists="append",
            index=False
        )

        load_audit.append(
            {
                "table": table,
                "rows_loaded": len(df),
                "status": "SUCCESS"
            }
        )

    except Exception as e:

        print(e)

        load_audit.append(
            {
                "table": table,
                "rows_loaded": 0,
                "status": str(e)
            }
        )

audit = pd.DataFrame(load_audit)

os.makedirs("output", exist_ok=True)

audit.to_csv(
    "output/load_audit.csv",
    index=False
)

conn.commit()
conn.close()

print("=" * 60)
print("DATABASE LOAD COMPLETE")
print("=" * 60)
print(audit)