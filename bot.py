from news import AlphaVantageNews
from extract_data import WebSocketMarketData
from extract_historical_data import HistoricalMarketData
from paper_trade import PaperTradingAccount
from settings import Settings

class VirtualAssistant:
    """handles the live purchase and sale of stocks"""

    def __init__(self, settings):
        """initialize the unchanging variables"""
        #initiate self as the arguments in settings
        self.settings = settings

        #set up active or incavtive state for while loops
        self.position = False

        #build dynamic list to store incoming data in memory
        self.prices = []
        
    # ───────────────────────────────────────────────
    # STATE 1 : LIVE TRADE
    # ──────────────────────────────────────────────
    def active_position(self):
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

if __name__ == "__main__":
    settings = Settings()                  # uses dates already in settings.py
    bot      = VirtualAssistant(settings)  # prices list already initialised

    HistoricalMarketData(settings, bot._store_price).start()   # run replay

    print(f"Collected {len(bot.prices)} bars.")