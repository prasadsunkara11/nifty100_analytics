"""
Unit Tests for normaliser.py
Sprint 1 - ETL
"""

import pytest

from src.etl.normaliser import (
    normalize_year,
    normalize_ticker
)


# =====================================================
# normalize_year()
# =====================================================

def test_year_dec_2012():
    assert normalize_year("Dec 2012") == 2012


def test_year_mar_2014():
    assert normalize_year("Mar 2014") == 2014


def test_year_integer():
    assert normalize_year(2020) == 2020


def test_year_string():
    assert normalize_year("2021") == 2021


def test_year_with_spaces():
    assert normalize_year("  Mar 2018  ") == 2018


def test_year_none():
    assert normalize_year(None) is None


def test_year_invalid():
    assert normalize_year("ABC") is None


def test_year_ttm():
    assert normalize_year("TTM") is None


def test_year_empty():
    assert normalize_year("") is None


def test_year_special():
    assert normalize_year("FY 2019-20") == 2019


# =====================================================
# normalize_ticker()
# =====================================================

def test_ticker_uppercase():
    assert normalize_ticker("ABB") == "ABB"


def test_ticker_lowercase():
    assert normalize_ticker("abb") == "ABB"


def test_ticker_spaces():
    assert normalize_ticker(" ABB ") == "ABB"


def test_ticker_multiple_spaces():
    assert normalize_ticker("A B B") == "ABB"


def test_ticker_mixed():
    assert normalize_ticker("TcS") == "TCS"


def test_ticker_numbers():
    assert normalize_ticker("ABC123") == "ABC123"


def test_ticker_none():
    assert normalize_ticker(None) is None


def test_ticker_empty():
    assert normalize_ticker("") == ""


def test_ticker_special():
    assert normalize_ticker(" M&M ") == "M&M"


def test_ticker_zomato():
    assert normalize_ticker("zomato") == "ZOMATO"