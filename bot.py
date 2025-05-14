from news import AlphaVantageNews
from extract_data import AlphaVantageMarketData
from paper_trade import PaperTradingAccount
from settings import Settings

class VirtualAssistant:
    """handles the live purchase and sale of stocks"""

    def __init__(self, settings):
        """initialize the unchanging variables"""

        self.active_position = False

        #import the main variable instances from settings
        self.settings = settings
        
        #import the extract news functionality
        self.news = AlphaVantageNews(settings)
        self.market_data = AlphaVantageMarketData()
        self.trader = PaperTradingAccount()

    def check_news_sentiment(self):
        """Check the news and return sentiment"""
        # Get the news
        self.news.get_news()
    
        # Get and return the sentiment
        sentiment = self.news.average_sentiment()
        print(sentiment)

    def update_stock_price(self):
        """check the current value of the stock"""
    

if __name__ == "__main__":
        # This code only runs when bot.py is executed directly
    settings = Settings()
    assistant = VirtualAssistant(settings)
    assistant._news()