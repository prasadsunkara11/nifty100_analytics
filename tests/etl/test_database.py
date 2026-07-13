"""
Unit Tests for SQLite Database
Sprint 1 - ETL
"""

import sqlite3
import os
import pandas as pd

DB_PATH = "db/nifty100.db"


# =====================================================
# Database Exists
# =====================================================

def test_database_exists():

    assert os.path.exists(DB_PATH)


# =====================================================
# Database Connection
# =====================================================

def test_database_connection():

    conn = sqlite3.connect(DB_PATH)

    assert conn is not None

    conn.close()


# =====================================================
# Companies Table Exists
# =====================================================

def test_companies_table():

    conn = sqlite3.connect(DB_PATH)

    tables = pd.read_sql(
        "SELECT name FROM sqlite_master WHERE type='table';",
        conn
    )

    conn.close()

    assert "companies" in tables["name"].values


# =====================================================
# Total Tables
# =====================================================

def test_total_tables():

    conn = sqlite3.connect(DB_PATH)

    tables = pd.read_sql(
        "SELECT name FROM sqlite_master WHERE type='table';",
        conn
    )

    conn.close()

    assert len(tables) >= 12


# =====================================================
# Companies Row Count
# =====================================================

def test_companies_rows():

    conn = sqlite3.connect(DB_PATH)

    count = pd.read_sql(
        "SELECT COUNT(*) AS total FROM companies",
        conn
    )

    conn.close()

    assert count.iloc[0]["total"] == 92


# =====================================================
# Profit Table Not Empty
# =====================================================

def test_profit_rows():

    conn = sqlite3.connect(DB_PATH)

    count = pd.read_sql(
        "SELECT COUNT(*) AS total FROM profitandloss",
        conn
    )

    conn.close()

    assert count.iloc[0]["total"] > 0


# =====================================================
# Stock Price Rows
# =====================================================

def test_stock_price_rows():

    conn = sqlite3.connect(DB_PATH)

    count = pd.read_sql(
        "SELECT COUNT(*) AS total FROM stock_prices",
        conn
    )

    conn.close()

    assert count.iloc[0]["total"] == 5520


# =====================================================
# Company ID Column Exists
# =====================================================

def test_company_column():

    conn = sqlite3.connect(DB_PATH)

    columns = pd.read_sql(
        "PRAGMA table_info(companies);",
        conn
    )

    conn.close()

    assert "id" in columns["name"].values


# =====================================================
# Database Read Query
# =====================================================

def test_select_query():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        "SELECT * FROM companies LIMIT 5;",
        conn
    )

    conn.close()

    assert len(df) == 5


# =====================================================
# Foreign Key Check Executes
# =====================================================

def test_foreign_key_check_runs():

    conn = sqlite3.connect(DB_PATH)

    fk = pd.read_sql(
        "PRAGMA foreign_key_check;",
        conn
    )

    conn.close()

    assert isinstance(fk, pd.DataFrame)