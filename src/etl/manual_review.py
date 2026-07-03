import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

companies = [
    "ABB",
    "TCS",
    "RELIANCE",
    "HDFCBANK",
    "INFY"
]

for company in companies:

    print("=" * 60)
    print(company)
    print("=" * 60)

    profit = pd.read_sql(
        f"""
        SELECT year, sales, net_profit
        FROM profitandloss
        WHERE company_id='{company}'
        ORDER BY year
        """,
        conn
    )

    print(profit)

conn.close()