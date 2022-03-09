import requests
import json
from datetime import datetime
import pandas as pd


url = 'https://lirarate.org/wp-json/lirarate/v2/rates?currency=LBP&_ver=t20223710'


# When we call an api endpoint, we get a response object.
response = requests.get(url)

# If the response is successful, we receive <Response [200]> code which means the request was successful.
print(response) 

# If the request was successfull, we can get the response body.
# You can convert the content of the response to a python object using the .json() method.
#print(response.json())

# In this case the response body is a json object with 2 sub-objects:
# - buy: the buying rate
# - sell: the selling rate
# - And each of these objects has a property called timestamp and rate.


# Get erach section seperately
result_buy = response.json()['buy']
result_sell = response.json()['sell']

# Create lirarate (buy) pandas dataframe
lirarate_buy = pd.DataFrame(result_buy)

# Rename the columns
lirarate_buy = lirarate_buy.rename(columns={0: 'date', 1: 'buy'})

# Convert the date column to datetime
lirarate_buy['date'] = pd.to_datetime(lirarate_buy['date'] / 1000 ,unit='s')
print(lirarate_buy)

# Create lirarate (sell) dataframe
lirarate_sell = pd.DataFrame(result_sell)

# Rename the columns
lirarate_sell = lirarate_sell.rename(columns={0: 'date', 1: 'sell'})

# Convert the date column to datetime
lirarate_sell['date'] = pd.to_datetime(lirarate_sell['date'] / 1000 ,unit='s')
print(lirarate_sell)

