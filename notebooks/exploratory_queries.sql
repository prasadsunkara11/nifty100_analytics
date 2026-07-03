-- Query 1
SELECT COUNT(*) FROM companies;

-- Query 2
SELECT company_name, roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- Query 3
SELECT company_id, MAX(net_profit) AS max_profit
FROM profitandloss
GROUP BY company_id
ORDER BY max_profit DESC
LIMIT 10;

-- Query 4
SELECT company_id, AVG(opm_percentage) AS avg_opm
FROM profitandloss
GROUP BY company_id
ORDER BY avg_opm DESC
LIMIT 10;

-- Query 5
SELECT broad_sector, COUNT(*)
FROM sectors
GROUP BY broad_sector;

-- Query 6
SELECT company_id, MAX(close_price)
FROM stock_prices
GROUP BY company_id
ORDER BY MAX(close_price) DESC
LIMIT 10;

-- Query 7
SELECT company_id, AVG(pe_ratio)
FROM market_cap
GROUP BY company_id
ORDER BY AVG(pe_ratio) DESC
LIMIT 10;

-- Query 8
SELECT company_id, AVG(return_on_equity_pct)
FROM financial_ratios
GROUP BY company_id
ORDER BY AVG(return_on_equity_pct) DESC
LIMIT 10;

-- Query 9
SELECT company_id, COUNT(*)
FROM documents
GROUP BY company_id
ORDER BY COUNT(*) DESC;

-- Query 10
SELECT company_id, SUM(net_profit)
FROM profitandloss
GROUP BY company_id
ORDER BY SUM(net_profit) DESC
LIMIT 10;