import requests
import os
import pandas as pd

API_KEY = os.environ.get('QUANDL_API_KEY')
params = {'api_key': API_KEY, 'ticker': 'AAPL'}
url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv'
r = requests.get(url, params=params)
# print(json.loads(r.text))
# print(r.text)
df = pd.DataFrame(r.text)
print(df.head())
