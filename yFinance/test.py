import yfinance as yf

start_date = '2020-01-01'
end_date = '2023-08-01'
ticker = 'AAPL'
data = yf.download(ticker, start_date, end_date)
print(data.tail())

# Export data to a CSV file
data.to_csv("AAPL.csv")