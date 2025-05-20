import os
import asyncio
import requests
from alpaca.data.live import StockDataStream
from dotenv import load_dotenv
from settings import Settings

load_dotenv()


class WebSocketMarketData:
    """Live market-data feed using Alpaca’s WebSocket."""

    def __init__(self, settings: Settings, on_price):
        # 1. auth
        self.api_key    = os.getenv("ALPACA_API_KEY")
        self.secret_key = os.getenv("ALPACA_SECRET")

        # 2. config
        self.ticker = settings.ticker

        # 3. Alpaca stream client
        self.stream = StockDataStream(self.api_key, self.secret_key)

        # 4. Define Key data point - price as VB
        self.on_price  = on_price

    # ---------- common output ---------- #
    def _forward_price(self, price: float):
        """
        Send the latest price to whatever logic you write later.
        Replace the print with storage, indicators, etc.
        """
        self.on_price(price) 
    # ----------------------------------- #

    async def _handle_bar(self, bar):
        """Called automatically by Alpaca for every new bar."""
        price = bar.close
        self._forward_price(price)

    async def start(self):
        """Begin live streaming."""
        self.stream.subscribe_bars(self._handle_bar, self.ticker)
        await self.stream._run_forever()

    # --------- retrieve single latest price---------- #
    def snap_price(self):
        url = f"https://data.alpaca.markets/v2/stocks/{self.ticker}/trades/latest"
        headers = {
            "APCA-API-KEY-ID":     self.api_key,
            "APCA-API-SECRET-KEY": self.secret_key,
        }
        return requests.get(url, headers=headers, timeout=3).json()["trade"]["p"]