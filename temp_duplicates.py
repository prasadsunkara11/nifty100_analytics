import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow"
]

for table in tables:

    print("=" * 60)
    print(table.upper())
    print("=" * 60)

    query = f"""
    SELECT
        company_id,
        year,
        COUNT(*) AS total
    FROM {table}
    GROUP BY company_id, year
    HAVING COUNT(*) > 1
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("No duplicates found.\n")
    else:
        print(df)
        print(f"\nTotal Duplicate Groups: {len(df)}\n")

conn.close()