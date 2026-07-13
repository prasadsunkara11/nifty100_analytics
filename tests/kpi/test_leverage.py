"""
Unit Tests for Leverage & Efficiency Ratios
Sprint 2 - Day 09
"""

from src.analytics.ratios import (
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    icr_warning,
    net_debt,
    asset_turnover
)


# =====================================================
# Debt to Equity
# =====================================================

def test_debt_to_equity():

    assert debt_to_equity(
        500,
        500,
        500
    ) == 0.50


def test_debt_free():

    assert debt_to_equity(
        0,
        500,
        500
    ) == 0


def test_negative_equity():

    assert debt_to_equity(
        100,
        -500,
        100
    ) is None


# =====================================================
# High Leverage Flag
# =====================================================

def test_high_leverage():

    assert high_leverage_flag(
        6,
        "Industrials"
    ) is True


def test_financials_not_flagged():

    assert high_leverage_flag(
        8,
        "Financials"
    ) is False


# =====================================================
# Interest Coverage Ratio
# =====================================================

def test_interest_coverage():

    assert interest_coverage_ratio(
        100,
        20,
        10
    ) == 12.00


def test_interest_zero():

    assert interest_coverage_ratio(
        100,
        20,
        0
    ) is None


# =====================================================
# Debt Free Label
# =====================================================

def test_debt_free_label():

    assert icr_label(None) == "Debt Free"


def test_normal_label():

    assert icr_label(5.2) == ""


# =====================================================
# ICR Warning
# =====================================================

def test_icr_warning():

    assert icr_warning(1.2) is True


def test_icr_safe():

    assert icr_warning(4.8) is False


# =====================================================
# Net Debt
# =====================================================

def test_net_debt():

    assert net_debt(
        500,
        120
    ) == 380


# =====================================================
# Asset Turnover
# =====================================================

def test_asset_turnover():

    assert asset_turnover(
        1000,
        500
    ) == 2.00


def test_asset_turnover_zero():

    assert asset_turnover(
        100,
        0
    ) is None