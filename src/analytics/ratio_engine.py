"""
Financial Ratio Engine
Sprint 2 - Day 12
"""

import sqlite3
import pandas as pd

from ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover
)

from cashflow_kpis import (
    free_cash_flow
)

from cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr
)


DB = "db/nifty100.db"

conn = sqlite3.connect(DB)


profit = pd.read_sql(
    "SELECT * FROM profitandloss",
    conn
)

balance = pd.read_sql(
    "SELECT * FROM balancesheet",
    conn
)

cash = (
    pd.read_sql(
        "SELECT * FROM cashflow",
        conn
    )
    .drop_duplicates(
        subset=["company_id", "year"],
        keep="first"
    )
)

companies = pd.read_sql(
    "SELECT * FROM companies",
    conn
)

df = (
    profit
    .merge(
        balance,
        on=["company_id","year"],
        how="left"
    )
    .merge(
        cash,
        on=["company_id","year"],
        how="left"
    )
)

results = []

for company in df["company_id"].unique():

    company_df = (
        df[
            df.company_id==company
        ]
        .sort_values("year")
        .reset_index(drop=True)
    )

    for i,row in company_df.iterrows():

        npm = net_profit_margin(
            row.net_profit,
            row.sales
        )

        opm = operating_profit_margin(
            row.operating_profit,
            row.sales
        )

        roe = return_on_equity(
            row.net_profit,
            row.equity_capital,
            row.reserves
        )

        de = debt_to_equity(
            row.borrowings,
            row.equity_capital,
            row.reserves
        )

        icr = interest_coverage_ratio(
            row.operating_profit,
            row.other_income,
            row.interest
        )

        turnover = asset_turnover(
            row.sales,
            row.total_assets
        )

        fcf = free_cash_flow(
            row.operating_activity,
            row.investing_activity
        )

        revenue5 = None
        pat5 = None
        eps5 = None

        if i >= 5:

            revenue5,_ = revenue_cagr(
                company_df.iloc[i-5]["sales"],
                row.sales,
                5
            )

            pat5,_ = pat_cagr(
                company_df.iloc[i-5]["net_profit"],
                row.net_profit,
                5
            )

            eps5,_ = eps_cagr(
                company_df.iloc[i-5]["eps"],
                row.eps,
                5
            )

        results.append({

            "company_id":row.company_id,
            "year":row.year,

            "net_profit_margin_pct":npm,
            "operating_profit_margin_pct":opm,
            "return_on_equity_pct":roe,

            "debt_to_equity":de,
            "interest_coverage":icr,
            "asset_turnover":turnover,

            "free_cash_flow_cr":fcf,

            "revenue_cagr_5yr":revenue5,
            "pat_cagr_5yr":pat5,
            "eps_cagr_5yr":eps5

        })


ratio_df = pd.DataFrame(results)

ratio_df.to_sql(
    "financial_ratios_engine",
    conn,
    if_exists="replace",
    index=False
)

print("="*60)
print("Ratio Engine Complete")
print("="*60)

print(ratio_df.head())

print()

print("Rows:",len(ratio_df))

conn.close()