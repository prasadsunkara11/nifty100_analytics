"""
Excel Loader & Cleaner
Sprint 1 - Day 2
"""

import os
import pandas as pd

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

# -----------------------------
# Source Files
# -----------------------------
FILES = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx",
    "sectors.xlsx",
    "stock_prices.xlsx",
    "financial_ratios.xlsx",
    "peer_groups.xlsx",
    "market_cap.xlsx"
]

# -----------------------------
# Header Row for each file
# -----------------------------
HEADER_ROWS = {
    "companies.xlsx": 1,
    "profitandloss.xlsx": 1,
    "balancesheet.xlsx": 1,
    "cashflow.xlsx": 1,
    "analysis.xlsx": 1,
    "documents.xlsx": 1,
    "prosandcons.xlsx": 1,

    "sectors.xlsx": 0,
    "stock_prices.xlsx": 0,
    "financial_ratios.xlsx": 0,
    "peer_groups.xlsx": 0,
    "market_cap.xlsx": 0,
}

# -----------------------------
# Remove duplicates
# -----------------------------
def clean_dataframe(df):

    original_rows = len(df)

    if "id" in df.columns:
        duplicate_cols = [c for c in df.columns if c != "id"]
        df = df.drop_duplicates(subset=duplicate_cols)
    else:
        df = df.drop_duplicates()

    removed = original_rows - len(df)

    return df, removed


# -----------------------------
# Load one excel file
# -----------------------------
def load_excel(filename):

    path = os.path.join(RAW_PATH, filename)

    header = HEADER_ROWS.get(filename, 0)

    df = pd.read_excel(
        path,
        header=header
    )

    df, removed = clean_dataframe(df)

    output_file = os.path.join(
        PROCESSED_PATH,
        filename.replace(".xlsx", "_clean.xlsx")
    )

    df.to_excel(
        output_file,
        index=False
    )

    print(
        f"{filename:<30}"
        f"Rows: {len(df):<6}"
        f"Removed: {removed}"
    )

    return df


# -----------------------------
# Load all datasets
# -----------------------------
def load_all():

    datasets = {}

    print("=" * 70)
    print("LOADING DATASETS")
    print("=" * 70)

    for file in FILES:

        try:

            datasets[file] = load_excel(file)

        except Exception as e:

            print(f"Error loading {file}")
            print(e)

    print("=" * 70)
    print("ALL FILES PROCESSED")
    print("=" * 70)

    return datasets


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":

    load_all()