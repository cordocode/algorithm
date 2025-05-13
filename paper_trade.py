import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

load_dotenv()

api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET")

class PaperTradingAccount:
    """initialize the user - alpaca access // boy and sell methods"""

    def __init__(self):
        self.api_key = api_key
        self.secret_key = secret_key
        paper = True

        #settup actual client
        self.client = TradingClient(self.api_key, 
                    self.secret_key, paper=paper)
        
    def buy(self, symbol, qty):
        
        #market order purchase - setup parameters
        market_order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        
        #submit the order
        market_order = self.client.submit_order(
            order_data=market_order_data
        )
        return market_order

    def sell(self, symbol, qty):
        
        #market order sell - setup parameters
        market_order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
        )
        
        #submit the order
        market_order = self.client.submit_order(
            order_data=market_order_data
        )
        return market_order
    

#example instance
investment = PaperTradingAccount()
investment.buy("AAPL", 5)