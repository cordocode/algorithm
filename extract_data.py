import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from settings import Settings
from alpaca.data.live import StockDataStream

#load in the api key from .env
load_dotenv()

#grab env from .env - set as api_key
api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET")

class AlphaVantageMarketData:
    """pull live data from the markets, return most recent close_data"""

    def __init__(self, settings):
        self.function = "TIME_SERIES_INTRADAY"
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = api_key

        #initialize the settings instance
        self.settings = settings

    def get_market_data(self):

        #the actual formatted call to the API
        params = {
        "function": self.function,
        "symbol": self.settings.ticker,                 
        "interval": self.settings.interval,            
        "extended_hours": self.settings.extended_hours, 
        "apikey": self.api_key
    }
        
        #pull the data from the market for a single stock
        self.response = requests.get(self.base_url, params = params)

    def extract_close_value(self):
    # Make sure we are working with the raw json
        self.data = self.response.json()
        print(self.data)
    
    # Get the time series data with the correct interval
        time_series = self.data[f'Time Series ({self.settings.interval})']
    
    # Get the first (most recent) timestamp
        most_recent_timestamp = list(time_series.keys())[0]
    
    # Get the close price for this timestamp
        close_price = time_series[most_recent_timestamp]['4. close']
    
    # Return both timestamp and close price as a tuple
        return most_recent_timestamp, close_price

    def update_close_value(self):
        # Get timestamps and close price
        most_recent_timestamp, close_price = self.extract_close_value()
        file = os.getenv('LOCAL_DATA_FILE')
        path = Path(file)
        
        # Create the string to append
        new_data = f"{most_recent_timestamp}: {close_price}\n"
        
        # Append to file instead of overwriting
        with open(path, 'a') as f:
            f.write(new_data)


settings = Settings()
thing = AlphaVantageMarketData(settings)
thing.get_market_data()
timestamp, price = thing.extract_close_value()
print(f"The current price of {settings.ticker} is {price}")