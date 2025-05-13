import os
import requests
from dotenv import load_dotenv
from pathlib import Path

#load in the api key from .env
load_dotenv()

#grab env from .env - set as api_key
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

class AlphaVantageMarketData:
    """pull live data from the markets, return most recent close_data"""

    def __init__(self):
        self.function = "TIME_SERIES_INTRADAY"
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = api_key

    def get_market_data(self, symbol, interval = "60min", extended_hours = "true"):

        #defining these variables so we can access them elsewhere
        self.interval = interval 
        self.symbol = symbol

        #the actual formatted call to the API
        params = {
        "function": self.function,
        "symbol": symbol,                 
        "interval": interval,            
        "extended_hours": extended_hours, 
        "apikey": self.api_key
    }
        
        #pull the data from the market for a single stock
        self.response = requests.get(self.base_url, params = params)

    def extract_close_value(self):
    # Make sure we are working with the raw json
        self.data = self.response.json()
        print(self.data)
    
    # Get the time series data with the correct interval
        time_series = self.data[f'Time Series ({self.interval})']
    
    # Get the first (most recent) timestamp
        most_recent_timestamp = list(time_series.keys())[0]
    
    # Get the close price for this timestamp
        close_price = time_series[most_recent_timestamp]['4. close']
    
    # Return both timestamp and close price as a tuple
        return most_recent_timestamp, close_price

    def update_close_value(self):
    #get timestamps and close price
        most_recent_timestamp, close_price = self.extract_close_value()
        path = Path('market_data.json')
        string = f"{most_recent_timestamp}: {close_price}"
        path.write_text(string)


#test instance for apple
data = AlphaVantageMarketData()
data.get_market_data("NVDA", "1min")
data.update_close_value()
