"""
Excel Loader
Loads all Excel files into pandas DataFrames.
"""

import os
import pandas as pd

RAW_PATH = "data/raw"

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
    "market_cap.xlsx",
]


def load_excel(filename):
    """
    Load a single Excel file.
    """

    path = os.path.join(RAW_PATH, filename)

    return pd.read_excel(path)


def load_all():
    """
    Load all project datasets.
    """

    datasets = {}

    for file in FILES:

        datasets[file] = load_excel(file)

        print(
            f"{file} loaded "
            f"({datasets[file].shape[0]} rows)"
        )

    return datasets


if __name__ == "__main__":

    load_all()