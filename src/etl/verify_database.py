import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "financial_ratios",
    "market_cap",
    "peer_groups",
    "prosandcons",
    "sectors",
    "stock_prices"
]

print("="*60)
print("DATABASE VERIFICATION")
print("="*60)

audit = []

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM {table}",
        conn
    )

    rows = int(count.iloc[0,0])

    print(f"{table:<25}{rows}")

    audit.append({
        "table":table,
        "rows":rows
    })

audit = pd.DataFrame(audit)

audit.to_csv(
    "output/database_row_counts.csv",
    index=False
)

fk = pd.read_sql(
    "PRAGMA foreign_key_check;",
    conn
)

print("\nForeign Key Errors")

if len(fk)==0:

    print("No Foreign Key Errors")

else:

    print(fk)

conn.close()

print("\nDatabase verification completed.")