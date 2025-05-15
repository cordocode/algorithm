import os
import asyncio
from collections import deque
from dotenv import load_dotenv
from alpaca.data.live import StockDataStream
from settings import Settings

# load environment variables from .env
load_dotenv()

class WebSocketMarketData:
    """Blueprint for receiving and storing websocket market data."""

    def __init__(self, settings):
        # Setup Alpaca authentication from environment variables
        self.api_key = os.getenv("ALPACA_API_KEY")
        self.secret_key = os.getenv("ALPACA_SECRET")

        # Settings for flexibility
        self.settings = settings
        self.ticker = self.settings.ticker
        self.historical_cache = self.settings.historical_cache

        # WebSocket initialization
        self.stream = StockDataStream(self.api_key, self.secret_key)

        #store the latest price of the bar
        self.latest_price = None

    async def handle_new_data(self, bar):
        """Handle incoming websocket data for close price- method is automatic."""
        #could activate time here later. just chose to take close_price for now
        self.latest_price = bar.close
    
    async def start_stream(self):
        """Starts the websocket stream."""
        print("Subscribing to bar data...")
        self.stream.subscribe_bars(self.handle_new_data, self.ticker)


if __name__ == "__main__":
    settings = Settings()
    ws_market_data = WebSocketMarketData(settings)
    asyncio.get_event_loop().run_until_complete(ws_market_data.start_stream())

