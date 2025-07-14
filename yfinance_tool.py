import yfinance as yf

ticker = "ONGC.NS"

stock = yf.Ticker(ticker)

response =stock.info

#print(stock.info)

summary=stock.info['longBusinessSummary'] #Summary of company
ind=stock.info['industryDisp'] #Industry of company
beta=stock.info['beta'] #Beta value
pe=stock.info['trailingPE'] #PE Ratio
div_yield=(stock.info['trailingAnnualDividendYield'])*100 #Dividend Yield
book_value = stock.info['bookValue'] #Book value of comapny 
pb = stock.info['priceToBook'] #P/B Ratio
earnings_q=stock.info['earningsQuarterlyGrowth'] #Earnings Quarterly Growth
eps = stock.info['trailingEps'] #Earnings Per Share 
y_change = stock.info['fiftyTwoWeekChangePercent'] #52W Change percent 
current_price = stock.info['currentPrice'] #Current Market Price
roe = (stock.info['returnOnEquity'])*100 #Return On Equity
currency =stock.info['financialCurrency'] #Currency
exchange=stock.info['fullExchangeName'] #Stock Exchange Name
name = stock.info['longName'] #Name of the company
market_cap=stock.info['marketCap']



