import os
import requests
from dotenv import load_dotenv
from settings import Settings

#load in the api key from .env
load_dotenv()

#grab env from .env - set as api_key
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

#build the class for customizing pulling news data
class AlphaVantageNews:
    """pull a certain amount of news in realtime relative to a given ticker, return average sentiment"""

    #set up parameter for stock and optional variable for limit of articles
    def __init__(self, settings):
        self.function = "NEWS_SENTIMENT"
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = api_key
        
        #use the settings for specific instance varaibles
        self.settings = settings

    def get_news(self):
        
        #build the dictionary of key/value pairs we want to request 
        params = {
            "function": self.function,
            "tickers": self.settings.ticker,
            "time_from": self.settings.time_from,
            "time_to": self.settings.time_to,
            "limit": self.settings.limit,
            "sort": self.settings.sort,
            "apikey": self.api_key
        }

        #return the news in json in terminal
        self.response = requests.get(self.base_url, params=params) 
        self.news = self.response.json()
        
    def print_news(self):
        #convert the r response into json string
        print(self.news)

    def average_sentiment(self):
        # Get all articles from the feed
        feed = self.news['feed']
    
        # Calculate total sentiment
        total_sentiment = 0
        for article in feed:
            total_sentiment += float(article['overall_sentiment_score'])
    
        # Return the average
        print(total_sentiment / len(feed))
