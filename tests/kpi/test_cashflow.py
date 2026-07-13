"""
Unit Tests for Cash Flow KPIs
Sprint 2 - Day 11
"""

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion,
    capital_allocation_pattern
)


# =====================================================
# Free Cash Flow
# =====================================================

def test_free_cash_flow():

    assert free_cash_flow(
        1000,
        -300
    ) == 700


def test_negative_fcf():

    assert free_cash_flow(
        100,
        -500
    ) == -400


# =====================================================
# CFO Quality
# =====================================================

def test_high_quality():

    assert cfo_quality_score(
        120,
        100
    ) == "High Quality"


def test_moderate_quality():

    assert cfo_quality_score(
        75,
        100
    ) == "Moderate"


def test_accrual_risk():

    assert cfo_quality_score(
        20,
        100
    ) == "Accrual Risk"


def test_pat_zero():

    assert cfo_quality_score(
        100,
        0
    ) is None


# =====================================================
# CapEx Intensity
# =====================================================

def test_asset_light():

    assert capex_intensity(
        -20,
        1000
    ) == "Asset Light"


def test_moderate_capex():

    assert capex_intensity(
        -50,
        1000
    ) == "Moderate"


def test_capital_intensive():

    assert capex_intensity(
        -120,
        1000
    ) == "Capital Intensive"


# =====================================================
# FCF Conversion
# =====================================================

def test_fcf_conversion():

    assert fcf_conversion(
        400,
        500
    ) == 80.00


def test_fcf_conversion_zero():

    assert fcf_conversion(
        400,
        0
    ) is None


# =====================================================
# Capital Allocation Patterns
# =====================================================

def test_reinvestor():

    assert capital_allocation_pattern(
        100,
        -50,
        -20
    ) == "Reinvestor"


def test_shareholder_returns():

    assert capital_allocation_pattern(
        100,
        -50,
        -20,
        "High Quality"
    ) == "Shareholder Returns"


def test_distress():

    assert capital_allocation_pattern(
        -50,
        100,
        80
    ) == "Distress Signal"


def test_growth_debt():

    assert capital_allocation_pattern(
        -50,
        -100,
        120
    ) == "Growth Funded by Debt"


def test_cash_accumulator():

    assert capital_allocation_pattern(
        100,
        20,
        40
    ) == "Cash Accumulator"


def test_pre_revenue():

    assert capital_allocation_pattern(
        -20,
        -50,
        -30
    ) == "Pre-Revenue"


def test_mixed():

    assert capital_allocation_pattern(
        100,
        -20,
        50
    ) == "Mixed"