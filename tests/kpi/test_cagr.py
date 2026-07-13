"""
Unit Tests for CAGR Engine
Sprint 2 - Day 10
"""

from src.analytics.cagr import (
    calculate_cagr,
    revenue_cagr,
    pat_cagr,
    eps_cagr,
    NORMAL,
    DECLINE_TO_LOSS,
    TURNAROUND,
    BOTH_NEGATIVE,
    ZERO_BASE,
    INSUFFICIENT
)


# =====================================================
# Normal CAGR
# =====================================================

def test_normal_cagr():

    value, flag = calculate_cagr(
        100,
        200,
        5
    )

    assert round(value, 2) == 14.87
    assert flag == NORMAL


# =====================================================
# Revenue CAGR
# =====================================================

def test_revenue_cagr():

    value, flag = revenue_cagr(
        500,
        1000,
        5
    )

    assert round(value, 2) == 14.87
    assert flag == NORMAL


# =====================================================
# PAT CAGR
# =====================================================

def test_pat_cagr():

    value, flag = pat_cagr(
        200,
        400,
        5
    )

    assert round(value, 2) == 14.87
    assert flag == NORMAL


# =====================================================
# EPS CAGR
# =====================================================

def test_eps_cagr():

    value, flag = eps_cagr(
        10,
        20,
        5
    )

    assert round(value, 2) == 14.87
    assert flag == NORMAL


# =====================================================
# Positive → Negative
# =====================================================

def test_decline_to_loss():

    value, flag = calculate_cagr(
        100,
        -50,
        5
    )

    assert value is None
    assert flag == DECLINE_TO_LOSS


# =====================================================
# Negative → Positive
# =====================================================

def test_turnaround():

    value, flag = calculate_cagr(
        -100,
        50,
        5
    )

    assert value is None
    assert flag == TURNAROUND


# =====================================================
# Negative → Negative
# =====================================================

def test_both_negative():

    value, flag = calculate_cagr(
        -100,
        -50,
        5
    )

    assert value is None
    assert flag == BOTH_NEGATIVE


# =====================================================
# Zero Base
# =====================================================

def test_zero_base():

    value, flag = calculate_cagr(
        0,
        100,
        5
    )

    assert value is None
    assert flag == ZERO_BASE


# =====================================================
# Insufficient Years
# =====================================================

def test_insufficient_years():

    value, flag = calculate_cagr(
        100,
        200,
        0
    )

    assert value is None
    assert flag == INSUFFICIENT


# =====================================================
# None Values
# =====================================================

def test_none_values():

    value, flag = calculate_cagr(
        None,
        100,
        5
    )

    assert value is None
    assert flag == INSUFFICIENT