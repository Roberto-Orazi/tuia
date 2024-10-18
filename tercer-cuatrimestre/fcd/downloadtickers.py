import yfinance as yf
import pandas as pd

# Create an empty DataFrame to store daily variations
df = pd.DataFrame()

# List of tickers
tickers = [
    "QQQ",
    "SPY",
    "EEM",
    "EWZ",
    "XLF",
    "BAC",
    "JPM",
    "BRK-B",
    "NU",
    "VALE",
    "VIST",
    "MELI",
    "IEF",
    "EMB",
    "AAAU",
    "BTC-USD",
    "GGAL",
]

# Loop through each ticker
for ticker in tickers:
    # Download historical data
    data = yf.download(ticker, start="2024-01-01", end="2024-10-09")

    # Check if data is not empty
    if not data.empty:
        # Calculate daily price variation (percentage change)
        data["Price Variation"] = data["Adj Close"].pct_change()

        # Rename the 'Price Variation' column to the ticker symbol
        data = data[["Price Variation"]].rename(columns={"Price Variation": ticker})

        # Concatenate the result with the main DataFrame, aligning on dates
        df = pd.concat([df, data], axis=1)

# Save the result to a CSV file if the DataFrame is not empty
if not df.empty:
    df.to_csv("daily_price_variation.csv", index=True)
    print("Data saved to 'daily_price_variation.csv'")
else:
    print("No data to save")
