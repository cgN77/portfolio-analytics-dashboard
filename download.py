import yfinance as yf
import pandas as pd
# Define the stock ticker
ticker = "AAPL"

# Download historical daily data
data = yf.download(ticker, start="2020-01-01", end="2025-01-01", interval="1d")

# Save it to a CSV file
data.to_csv("AAPL_data.csv")

print("Downloaded data:\n", data.head())

import pandas as pd

# Load the CSV file
df = pd.read_csv("AAPL_data.csv")

# Rename columns
df = df.rename(columns={"Date": "timeline", "Close": "price"})

# Save the modified file
df.to_csv("AAPL_modified.csv", index=False)

print(df.head())


