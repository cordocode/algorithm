from news import AlphaVantageNews
from extract_data import WebSocketMarketData
from paper_trade import PaperTradingAccount
from settings import Settings

class VirtualAssistant:
    """handles the live purchase and sale of stocks"""

    def __init__(self, settings):
        """initialize the unchanging variables"""

        self.position = False

        #import the main variable instances from settings
        self.settings = settings
        
        #import the extract news functionality
        self.news = AlphaVantageNews(settings)
        self.market_data = WebSocketMarketData()
        self.trader = PaperTradingAccount()

    def active_position(self):
        #store the purchase price from inactive position close
        #initiate websocket
        #store all future data after purchase price assuming purchase price is baseline
        #run simple 100% down to 80% drop algorithm
        #run simple else if negative 5% sell immediatly
        #sell 100% of portfolio
        #initiate inactive position
        #close active position

    def inactive_position(self):
        #initiate news method
        #initiate time method - wait for 7:25am
        #send news API request at 7:25
        #if news returns good sentiment then buy 100% portfolio
        #return purchase price
        #initiate active position
        #close inactive position
    

if __name__ == "__main__":
    # This code only runs when bot.py is executed directly
    settings = Settings()
    example = VirtualAssistant(settings)
    example._news()