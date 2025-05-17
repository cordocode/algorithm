import os, time
from dotenv import load_dotenv
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests   import StockBarsRequest
from alpaca.data.timeframe  import TimeFrame
from settings import Settings

load_dotenv()


class HistoricalMarketData:
    """Replay minute bars from Alpaca and stream them to a callback."""

    def __init__(self, settings: Settings, on_price):
        # 1. high-level config
        self.ticker       = settings.ticker
        self.start_date   = settings.historical_start   # "YYYY-MM-DD"
        self.end_date     = settings.historical_end
        self.speed        = settings.replay_speed       # 1 = real-time, 10 = 10× faster

        # 2. data client
        self.client = StockHistoricalDataClient(
            os.getenv("ALPACA_API_KEY"),
            os.getenv("ALPACA_SECRET"),
        )

        # 3. callback (identical signature to live feed)
        self.on_price = on_price

    # ---------- common output ---------- #
    def _forward_price(self, price: float):
        """Uniform interface so the bot never cares which feed is active."""
        self.on_price(price)
    # ----------------------------------- #

    def start(self):
        """Pull bars once, then drip them out at replay speed."""
        req = StockBarsRequest(
            symbol_or_symbols=self.ticker,
            timeframe=TimeFrame.Minute,
            start=self.start_date,
            end=self.end_date,
        )
        bars_df = self.client.get_stock_bars(req).df

        for _, row in bars_df.iterrows():
            self._forward_price(row.close)
            time.sleep(60 / self.speed)   # ↓ sleep less for faster replay


# quick smoke-test
if __name__ == "__main__":
    def _debug(price):   # simple print handler
        print(price)

    settings = Settings()
    HistoricalMarketData(settings, _debug).start()
