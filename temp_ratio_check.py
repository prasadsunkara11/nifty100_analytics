import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("""
SELECT company_id,
       year,
       COUNT(*) AS total
FROM financial_ratios_engine
GROUP BY company_id, year
HAVING COUNT(*) > 1
""", conn)

print(df)

conn.close()