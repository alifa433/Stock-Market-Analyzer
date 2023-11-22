import requests

def fetch_stock_data(symbol):
    # URL for the stock data API
    url = f"https://api.example.com/stock/{symbol}"

    # Make a request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch stock data")
