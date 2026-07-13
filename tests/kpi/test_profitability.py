"""
Unit Tests for Profitability Ratios
Sprint 2 - Day 08
"""

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    opm_cross_check,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets
)


# =====================================================
# Net Profit Margin
# =====================================================

def test_net_profit_margin():

    assert net_profit_margin(100, 1000) == 10.00


def test_net_profit_margin_zero_sales():

    assert net_profit_margin(100, 0) is None


# =====================================================
# Operating Profit Margin
# =====================================================

def test_operating_profit_margin():

    assert operating_profit_margin(250, 1000) == 25.00


def test_operating_profit_margin_zero_sales():

    assert operating_profit_margin(250, 0) is None


# =====================================================
# OPM Cross Check
# =====================================================

def test_opm_crosscheck_match():

    assert opm_cross_check(25.0, 25.5) is False


def test_opm_crosscheck_mismatch():

    assert opm_cross_check(25.0, 27.5) is True


# =====================================================
# Return on Equity
# =====================================================

def test_return_on_equity():

    assert return_on_equity(
        100,
        400,
        600
    ) == 10.00


def test_return_on_equity_negative():

    assert return_on_equity(
        100,
        -500,
        100
    ) is None


# =====================================================
# Return on Capital Employed
# =====================================================

def test_roce():

    assert return_on_capital_employed(
        150,
        500,
        300,
        200
    ) == 15.00


def test_roce_zero_capital():

    assert return_on_capital_employed(
        150,
        -100,
        -100,
        0
    ) is None


# =====================================================
# Return on Assets
# =====================================================

def test_roa():

    assert return_on_assets(
        200,
        4000
    ) == 5.00


def test_roa_zero_assets():

    assert return_on_assets(
        200,
        0
    ) is None