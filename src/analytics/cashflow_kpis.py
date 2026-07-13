"""
Cash Flow KPI Engine
Sprint 2 - Day 11
"""


# ==========================================================
# Free Cash Flow
# ==========================================================

def free_cash_flow(
        operating_activity,
        investing_activity):
    """
    FCF = CFO + CFI
    """

    return operating_activity + investing_activity


# ==========================================================
# CFO Quality Score
# ==========================================================

def cfo_quality_score(
        cfo,
        pat):
    """
    CFO / PAT
    """

    if pat == 0:
        return None

    ratio = cfo / pat

    if ratio > 1:

        return "High Quality"

    elif ratio >= 0.5:

        return "Moderate"

    else:

        return "Accrual Risk"


# ==========================================================
# CapEx Intensity
# ==========================================================

def capex_intensity(
        investing_activity,
        sales):

    if sales == 0:
        return None

    ratio = abs(investing_activity) / sales * 100

    if ratio < 3:

        return "Asset Light"

    elif ratio <= 8:

        return "Moderate"

    else:

        return "Capital Intensive"


# ==========================================================
# FCF Conversion
# ==========================================================

def fcf_conversion(
        fcf,
        operating_profit):

    if operating_profit == 0:

        return None

    return round(
        fcf / operating_profit * 100,
        2
    )


# ==========================================================
# Capital Allocation Pattern
# ==========================================================

def capital_allocation_pattern(
        cfo,
        cfi,
        cff,
        quality=None):

    signs = (
        cfo > 0,
        cfi > 0,
        cff > 0
    )

    if signs == (True, False, False):

        if quality == "High Quality":

            return "Shareholder Returns"

        return "Reinvestor"

    if signs == (True, True, False):

        return "Liquidating Assets"

    if signs == (False, True, True):

        return "Distress Signal"

    if signs == (False, False, True):

        return "Growth Funded by Debt"

    if signs == (True, True, True):

        return "Cash Accumulator"

    if signs == (False, False, False):

        return "Pre-Revenue"

    if signs == (True, False, True):

        return "Mixed"

    return "Unknown"