"""
Unit Tests for validator.py
Sprint 1 - ETL
"""

import pandas as pd


# =====================================================
# DQ-01 Duplicate Company IDs
# =====================================================

def test_duplicate_company_id():

    companies = pd.DataFrame({
        "id": ["ABB", "ABB", "TCS"]
    })

    duplicates = companies[
        companies.duplicated(
            subset=["id"],
            keep=False
        )
    ]

    assert len(duplicates) == 2


# =====================================================
# DQ-02 Duplicate Company + Year
# =====================================================

def test_duplicate_company_year():

    profit = pd.DataFrame({
        "company_id": ["ABB", "ABB", "TCS"],
        "year": ["2020", "2020", "2021"]
    })

    duplicates = profit[
        profit.duplicated(
            subset=["company_id", "year"],
            keep=False
        )
    ]

    assert len(duplicates) == 2


# =====================================================
# DQ-03 Foreign Key Check
# =====================================================

def test_invalid_company():

    companies = {"ABB", "TCS"}

    profit = pd.DataFrame({
        "company_id": ["ABB", "INFY"]
    })

    invalid = []

    for _, row in profit.iterrows():

        if row["company_id"] not in companies:

            invalid.append(row["company_id"])

    assert invalid == ["INFY"]


# =====================================================
# DQ-04 Sales Positive
# =====================================================

def test_sales_positive():

    profit = pd.DataFrame({
        "sales": [100, -20]
    })

    invalid = profit[
        profit["sales"] <= 0
    ]

    assert len(invalid) == 1


# =====================================================
# DQ-05 OPM Range
# =====================================================

def test_opm_range():

    profit = pd.DataFrame({
        "opm_percentage": [20, 150]
    })

    invalid = profit[
        (profit["opm_percentage"] > 100)
    ]

    assert len(invalid) == 1


# =====================================================
# DQ-06 Tax Range
# =====================================================

def test_tax_range():

    profit = pd.DataFrame({
        "tax_percentage": [25, 120]
    })

    invalid = profit[
        profit["tax_percentage"] > 100
    ]

    assert len(invalid) == 1


# =====================================================
# DQ-07 Missing EPS
# =====================================================

def test_missing_eps():

    profit = pd.DataFrame({
        "eps": [10, None]
    })

    assert profit["eps"].isna().sum() == 1


# =====================================================
# DQ-08 Duplicate Balance Sheet
# =====================================================

def test_duplicate_balance():

    balance = pd.DataFrame({
        "company_id": ["ABB", "ABB"],
        "year": [2020, 2020]
    })

    duplicates = balance.duplicated(
        subset=["company_id", "year"],
        keep=False
    )

    assert duplicates.sum() == 2


# =====================================================
# DQ-09 Duplicate Cash Flow
# =====================================================

def test_duplicate_cashflow():

    cash = pd.DataFrame({
        "company_id": ["ABB", "ABB"],
        "year": [2020, 2020]
    })

    duplicates = cash.duplicated(
        subset=["company_id", "year"],
        keep=False
    )

    assert duplicates.sum() == 2


# =====================================================
# DQ-10 Missing Year
# =====================================================

def test_missing_year():

    profit = pd.DataFrame({
        "year": ["2020", None]
    })

    assert profit["year"].isna().sum() == 1