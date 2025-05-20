
import time
import asyncio
from news import AlphaVantageNews
from extract_data import WebSocketMarketData
from extract_historical_data import HistoricalMarketData
from paper_trade import PaperTradingAccount
from settings import Settings
from datetime import datetime

class VirtualAssistant:
    """handles the live purchase and sale of stocks"""

    def __init__(self, settings):
        """initialize the unchanging variables"""
        #initiate self as the arguments in settings
        self.settings = settings

        self.news_client  = AlphaVantageNews(settings)

        self.market = WebSocketMarketData(settings, lambda _: None)

        #set up the trading account
        self.account = PaperTradingAccount()

        #set up active or incavtive state for while loops
        self.position = False

        #build dynamic list to store incoming data in memory
        self.prices = []
        self.latest_price = None 

    # ───────────────────────────────────────────────
    # STATE 1 : LIVE TRADE
    # ──────────────────────────────────────────────
    def active_position(self):
        # Initialize peak price with the purchase price
        peak_price = self.purchase_price
        
        # Clear any existing price data
        self.prices = [self.purchase_price]
        
        # Set up websocket with a price handler
        self.market.on_price = self._store_price
        
        # Start the websocket in a non-blocking way
        asyncio.create_task(self.market.start())
        
        # Main trading loop
        while self.position:
            # Check for trailing stop condition if we have prices
            if len(self.prices) > 0:
                current_price = self.prices[-1]
                
                # Update peak price if we have a new high
                if current_price > peak_price:
                    peak_price = current_price
                    print(f"New peak: {peak_price}")
                
                # Calculate drawdown ratio
                drawdown_ratio = current_price / peak_price
                
                # Execute trailing stop if drawdown exceeds threshold
                if drawdown_ratio <= 0.80:
                    print(f"Trailing stop triggered: {current_price} is {drawdown_ratio:.2%} of peak {peak_price}")
                    
                    # Get position size from account
                    position = self.account.client.get_position(self.settings.ticker)
                    qty = int(position.qty)
                    
                    # Execute sell
                    self.account.sell(self.settings.ticker, qty)
                    
                    # Reset state
                    self.position = False
                    self.prices = []  # Clear price data
                    print(f"Position closed, memory cleared")
                    break
            
            # Prevent tight loop, check every second
            time.sleep(1)
    # ───────────────────────────────────────────────
    # STATE 2 : NO ACTIVE TRADES
    # ───────────────────────────────────────────────
    def inactive_position(self):
       
       while self.position == False:
        # 1️ wait for 07:25 (or whatever is set in Settings)
        self._wait_until(self.settings.hour,
                        self.settings.minute,
                        self.settings.news_time_zone)

        # 2️ pull sentiment
        self.news_client.get_news()
        avg_score = self.news_client.average_sentiment()

        # 3️ gate: only trade on strong positive news
        if avg_score <= 0.35:
            return

        price = self.market.snap_price()
        qty   = int(self._calculate_investment(price))
        if qty == 0:
            return                       

        # 4️ execute
        self.account.buy(self.settings.ticker, qty)
        self.position       = True
        self.purchase_price = price


    # ========== helper methods (all private) =================
    
    def _store_price(self, price: float):
        #helper method for storing incoming data
        self.latest_price = price
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