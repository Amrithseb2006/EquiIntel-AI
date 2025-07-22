import sqlite3
from yfinance_tool import sector

conn = sqlite3.connect("nse_stocks.db")
cursor = conn.cursor()

sector_value = sector  # Assume 'sector' is a variable holding the desired sector name

cursor.execute("""
    SELECT symbol, longName, marketCap, currentPrice ,beta , trailingPE,trailingAnnualDividendYield,bookValue,priceToBook,earningsQuarterlyGrowth,trailingEps,returnOnEquity
    FROM stocks
    WHERE sector = ? AND marketCap > 10000
    ORDER BY marketCap DESC
""", (sector_value,))

rows = cursor.fetchall()
print(rows)

conn.close()
