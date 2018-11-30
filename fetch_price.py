import requests
import requests_cache
import os
import pandas as pd
import io

requests_cache.install_cache()

API_KEY = os.environ.get('QUANDL_API_KEY')
params = {'api_key': API_KEY, 'ticker': 'AAPL'}
url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv'


def fetch():
    r = requests.get(url, params=params)
    # print(json.loads(r.text))
    # print(r.text)
    df = pd.read_csv(io.StringIO(r.text))
    # print(df.head())
    return df.head().to_html(classes='table table-striped', border=0, index=False)

# fetch()
