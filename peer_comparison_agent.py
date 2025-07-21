import sqlite3

# Connect to the same DB file
conn = sqlite3.connect("nse_stocks.db")
cursor = conn.cursor()

# Run the query
cursor.execute("""
SELECT symbol, longName, marketCap, currentPrice
FROM stocks
WHERE sector = 'Energy' AND marketCap > 10000
ORDER BY marketCap DESC
""")

# Fetch and print results
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
