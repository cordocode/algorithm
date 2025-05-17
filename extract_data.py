import os
from dotenv import load_dotenv
from alpaca.data.live import StockDataStream
from settings import Settings
from alpaca.data.enums import DataFeed 

load_dotenv()                       

class WebSocketMarketData:
    """Connect to Alpaca and print each new 1-minute bar’s close price."""

    #might need to update IEX when main subscription starts.
    def __init__(self, settings: Settings):
        self.ticker = settings.ticker
        self.stream = StockDataStream(
            api_key=os.getenv("ALPACA_API_KEY"),
            secret_key=os.getenv("ALPACA_SECRET"),
            feed=DataFeed.IEX
        )

    async def _handle_bar(self, bar):
        # Alpaca calls this for every new bar
        print(f"{bar.symbol} {bar.timestamp}  close={bar.close}")

    def start(self):
        print(f"Subscribing to {self.ticker} 1-min bars …")
        self.stream.subscribe_bars(self._handle_bar, self.ticker)
        self.stream.run()                 # blocks until you Ctrl-C


if __name__ == "__main__":
    WebSocketMarketData(Settings()).start()
