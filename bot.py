from news import AlphaVantageNews
from extract_data import WebSocketMarketData
from extract_historical_data import HistoricalMarketData
from paper_trade import PaperTradingAccount
from settings import Settings
from datetime import datetime
import time

class VirtualAssistant:
    """handles the live purchase and sale of stocks"""

    def __init__(self, settings):
        """initialize the unchanging variables"""
        #initiate self as the arguments in settings
        self.settings = settings
        self.news_client  = AlphaVantageNews(settings)

        #set up active or incavtive state for while loops
        self.position = False

        #build dynamic list to store incoming data in memory
        self.prices = []

    # ───────────────────────────────────────────────
    # STATE 1 : LIVE TRADE
    # ──────────────────────────────────────────────
    def active_position(self):

        while self.position == True:
        #store the purchase price from inactive position close
        #initiate websocket
        #store all future data after purchase price assuming purchase price is baseline
        #run simple 100% down to 80% drop algorithm
        #run simple else if negative 5% sell immediatly
        #sell 100% of portfolio
        #initiate inactive position
        #close active position
        return None
    # ───────────────────────────────────────────────
    # STATE 2 : NO ACTIVE TRADES
    # ───────────────────────────────────────────────
    def inactive_position(self):

        while self.position == False:
           self._wait_until()
            sentiment_data = self.news_client.get_news()
            avg_score      = self.news_client.average_sentiment()
            
            if avg_score > .35
                
        #initiate news method
        #initiate time method - wait for 7:25am
        #send news API request at 7:25
        #if news returns good sentiment then buy 100% portfolio
        #return purchase price
        #initiate active position
        #close inactive position
        return None

    # ========== helper methods (all private) =================
    
    def _store_price(self, price: float):
        self.prices.append(price)
        print(f"{len(self.prices):>4}  |  last price: {price}")

    def _wait_until(self):
        hour, minute = self.settings.target
        tz = self.settings.news_time_zone

        while True:
            now = datetime.now(tz)
            if (now.hour, now.minute) == (hour, minute):
                return                 
            time.sleep(30)         

if __name__ == "__main__":
    settings = Settings()                  
    bot      = VirtualAssistant(settings) 