import os
import requests
from dotenv import load_dotenv

#load in the api key from .env
load_dotenv()

#grab env from .env - set as api_key
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

#build the class for customizing pulling news data
class AlphaVantageNews:
    """pull a certain amount of news in realtime 
    relative to a given ticker, return average sentiment"""

    #set up parameter for stock and optional variable for limit of articles
    def __init__(self):
        self.function = "NEWS_SENTIMENT"
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = api_key

    def get_news(self, ticker, limit=1, sort = "LATEST"):
        
        #build the dictionary of key/value pairs we want to request 
        params = {
            "function": self.function,
            "tickers": ticker,
            "limit": limit,
            "sort": sort,
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

#test instance for apple
news = AlphaVantageNews()
news.get_news("NVDA")
news.average_sentiment()