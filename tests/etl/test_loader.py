"""
Unit Tests for loader.py
Sprint 1 - ETL
"""

import pandas as pd

from src.etl.loader import (
    clean_dataframe,
    HEADER_ROWS,
    FILES
)


# =====================================================
# clean_dataframe()
# =====================================================

def test_remove_duplicate_rows():

    df = pd.DataFrame({
        "id": [1, 2, 3],
        "company_id": ["ABB", "ABB", "TCS"],
        "year": [2020, 2020, 2021]
    })

    cleaned, removed = clean_dataframe(df)

    assert len(cleaned) == 2
    assert removed == 1


def test_no_duplicates():

    df = pd.DataFrame({
        "id": [1, 2],
        "company_id": ["ABB", "TCS"],
        "year": [2020, 2021]
    })

    cleaned, removed = clean_dataframe(df)

    assert len(cleaned) == 2
    assert removed == 0


def test_duplicate_without_id():

    df = pd.DataFrame({
        "company": ["ABB", "ABB"],
        "sales": [100, 100]
    })

    cleaned, removed = clean_dataframe(df)

    assert len(cleaned) == 1
    assert removed == 1


def test_empty_dataframe():

    df = pd.DataFrame()

    cleaned, removed = clean_dataframe(df)

    assert cleaned.empty
    assert removed == 0


def test_single_row():

    df = pd.DataFrame({
        "id": [1],
        "company_id": ["ABB"]
    })

    cleaned, removed = clean_dataframe(df)

    assert len(cleaned) == 1
    assert removed == 0


# =====================================================
# HEADER_ROWS
# =====================================================

def test_header_companies():

    assert HEADER_ROWS["companies.xlsx"] == 1


def test_header_profit():

    assert HEADER_ROWS["profitandloss.xlsx"] == 1


def test_header_market_cap():

    assert HEADER_ROWS["market_cap.xlsx"] == 0


# =====================================================
# FILES
# =====================================================

def test_total_files():

    assert len(FILES) == 12


def test_companies_exists():

    assert "companies.xlsx" in FILES