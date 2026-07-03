import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT DISTINCT company_id
FROM balancesheet
WHERE company_id NOT IN (
    SELECT id
    FROM companies
)

UNION

SELECT DISTINCT company_id
FROM cashflow
WHERE company_id NOT IN (
    SELECT id
    FROM companies
)

UNION

SELECT DISTINCT company_id
FROM profitandloss
WHERE company_id NOT IN (
    SELECT id
    FROM companies
)

ORDER BY company_id;
"""

missing = pd.read_sql(query, conn)

print("=" * 50)
print("Missing Companies")
print("=" * 50)

print(missing)

print("\nTotal Missing:", len(missing))

conn.close()