import requests
import yfinance as yf

# Yahoo Finance API URL
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

# Query parameters
querystring = {"symbol":"AAPL"}

# Headers
headers = {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

# Make a request to the Yahoo Finance API
response = requests.request("GET", url, headers=headers, params=querystring)

# Parse the JSON response and get the current price of the stock
data = response.json()
current_price = data["price"]["regularMarketPrice"]["raw"]

# Use yfinance library to get historical prices of the stock
apple_stock = yf.Ticker("AAPL")
historical_prices = apple_stock.history(period="max")

# Print the current price and the historical prices
print("Current price of AAPL: ${:.2f}".format(current_price))
print(historical_prices)