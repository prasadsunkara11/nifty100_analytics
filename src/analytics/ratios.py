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