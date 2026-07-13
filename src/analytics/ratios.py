"""
Financial Ratio Engine
Sprint 2 - Day 08

Profitability Ratios
"""

import math


# ==========================================================
# Net Profit Margin
# ==========================================================

def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin (%)

    Formula:
    Net Profit / Sales * 100
    """

    if sales is None or sales == 0:
        return None

    return round((net_profit / sales) * 100, 2)


# ==========================================================
# Operating Profit Margin
# ==========================================================

def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin (%)
    """

    if sales is None or sales == 0:
        return None

    return round((operating_profit / sales) * 100, 2)


# ==========================================================
# OPM Cross Check
# ==========================================================

def opm_cross_check(calculated_opm, source_opm):

    if calculated_opm is None or source_opm is None:
        return False

    difference = abs(calculated_opm - source_opm)

    return difference > 1


# ==========================================================
# Return on Equity
# ==========================================================

def return_on_equity(net_profit,
                     equity_capital,
                     reserves):

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)


# ==========================================================
# Return on Capital Employed
# ==========================================================

def return_on_capital_employed(
        ebit,
        equity_capital,
        reserves,
        borrowings):

    capital = equity_capital + reserves + borrowings

    if capital <= 0:
        return None

    return round((ebit / capital) * 100, 2)


# ==========================================================
# Return on Assets
# ==========================================================

def return_on_assets(net_profit,
                     total_assets):

    if total_assets is None or total_assets <= 0:
        return None

    return round((net_profit / total_assets) * 100, 2)

# ==========================================================
# Debt to Equity Ratio
# ==========================================================

def debt_to_equity(
        borrowings,
        equity_capital,
        reserves):
    """
    Debt to Equity Ratio

    Return:
        0 if borrowings = 0
        None if equity <= 0
    """

    if borrowings == 0:
        return 0

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round(
        borrowings / equity,
        2
    )


# ==========================================================
# High Leverage Flag
# ==========================================================

def high_leverage_flag(
        debt_equity,
        broad_sector):
    """
    High leverage if D/E > 5
    Ignore Financials sector.
    """

    if debt_equity is None:
        return False

    if broad_sector == "Financials":
        return False

    return debt_equity > 5


# ==========================================================
# Interest Coverage Ratio
# ==========================================================

def interest_coverage_ratio(
        operating_profit,
        other_income,
        interest):
    """
    Interest Coverage Ratio
    """

    if interest == 0:
        return None

    return round(
        (operating_profit + other_income)
        / interest,
        2
    )


# ==========================================================
# ICR Label
# ==========================================================

def icr_label(icr):

    if icr is None:
        return "Debt Free"

    return ""


# ==========================================================
# ICR Warning Flag
# ==========================================================

def icr_warning(icr):

    if icr is None:
        return False

    return icr < 1.5


# ==========================================================
# Net Debt
# ==========================================================

def net_debt(
        borrowings,
        investments):
    """
    Net Debt
    """

    return borrowings - investments


# ==========================================================
# Asset Turnover
# ==========================================================

def asset_turnover(
        sales,
        total_assets):
    """
    Asset Turnover Ratio
    """

    if total_assets == 0:
        return None

    return round(
        sales / total_assets,
        2
    )