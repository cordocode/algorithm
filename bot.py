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

        #set up the trading account
        self.account = PaperTradingAccount()

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
        # 1️⃣ wait for 07:25 (or whatever is set in Settings)
        self._wait_until(self.settings.hour,
                        self.settings.minute,
                        self.settings.news_time_zone)

        # 2️⃣ pull sentiment
        self.news_client.get_news()
        avg_score = self.news_client.average_sentiment()

        # 3️⃣ gate: only trade on strong positive news
        if avg_score <= 0.35:
            return

        price = self.market_data.latest_price
        qty   = self._calc_quantity(price)
        if qty == 0:
            return                       

        # 4️⃣ execute
        self.account.buy(self.settings.ticker, qty)
        self.position       = True
        self.purchase_price = price


    # ========== helper methods (all private) =================
    
    def _store_price(self, price: float):
        #helper method for storing incoming data
        self.prices.append(price)
        print(f"{len(self.prices):>4}  |  last price: {price}")

    def _wait_until(self):
        #helper method so news doesnt call itself 24/7
        hour, minute = self.settings.target
        tz = self.settings.news_time_zone

        while True:
            now = datetime.now(tz)
            if (now.hour, now.minute) == (hour, minute):
                return                 
            time.sleep(30)         

    def _calculate_investment(self, price: float):
        dollars_to_deploy = self.settings.investment_size * self.account.cash
        return int(dollars_to_deploy // price)


if __name__ == "__main__":
    settings = Settings()                  
    bot      = VirtualAssistant(settings) 