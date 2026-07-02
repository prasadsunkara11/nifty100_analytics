"""
Utility functions for data normalization.
"""

import re


def normalize_year(year):
    """
    Convert year values to integer.
    """

    if year is None:
        return None

    year = str(year).strip()

    match = re.search(r"\d{4}", year)

    if match:
        return int(match.group())

    return None


def normalize_ticker(ticker):
    """
    Normalize stock ticker symbols.
    """

    if ticker is None:
        return None

    ticker = str(ticker).upper().strip()

    ticker = ticker.replace(" ", "")

    return ticker