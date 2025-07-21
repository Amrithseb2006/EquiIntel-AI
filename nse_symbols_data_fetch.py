from nsetools import Nse
import yfinance as yf
import sqlite3
import time

# Initialize NSE and DB
nse = Nse()
stock_list = nse.get_stock_codes()


# Connect to SQLite
conn = sqlite3.connect("nse_stocks.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    symbol TEXT PRIMARY KEY,
    sector TEXT,
    typeDisp TEXT,
    industryDisp TEXT,
    beta REAL,
    trailingPE REAL,
    trailingAnnualDividendYield REAL,
    bookValue REAL,
    priceToBook REAL,
    earningsQuarterlyGrowth REAL,
    trailingEPS REAL,
    fiftyTwoWeekChangePercent REAL,
    currentPrice REAL,
    returnOnEquity REAL,
    longName TEXT,
    marketCap INTEGER
);
''')

# Iterate over symbols
for i, symbol in enumerate(stock_list):
    try:
        ticker = f"{symbol}.NS"
        print(f"[{i+1}/{len(stock_list)}] Fetching: {ticker}")
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Insert into DB
        cursor.execute('''
        INSERT OR REPLACE INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            symbol,
            info.get("sector"),
            info.get("quoteType"),
            info.get("industry"),
            info.get("beta"),
            info.get("trailingPE"),
            info.get("trailingAnnualDividendYield"),
            info.get("bookValue"),
            info.get("priceToBook"),
            info.get("earningsQuarterlyGrowth"),
            info.get("trailingEps"),
            info.get("52WeekChange"),
            info.get("currentPrice"),
            info.get("returnOnEquity"),
            info.get("longName"),
            info.get("marketCap")
        ))

        conn.commit()
        time.sleep(1)  # Be nice to Yahoo Finance

    except Exception as e:
        print(f"Error fetching {symbol}: {e}")

conn.close()
print("✅ Done storing all stock info into nse_stocks.db")
