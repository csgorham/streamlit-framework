import requests
import json

APIKEY = 'RN6CGXIAQ7RMQG9G'
ticker = 'AAPL'
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey={}'.format(ticker, APIKEY)

r = requests.get(url)
data = r.json()

print(data)
