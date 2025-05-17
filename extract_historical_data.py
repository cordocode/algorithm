import os, time
from dotenv import load_dotenv
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests   import StockBarsRequest
from alpaca.data.timeframe  import TimeFrame
from settings import Settings

load_dotenv()


class HistoricalMarketData:
    """Offline replay of historical bars."""

    def __init__(self, settings: Settings):
        self.ticker  = settings.ticker
        self.start_date   = settings.historical_start      # e.g. "2024-10-01"
        self.end_date     = settings.historical_end        # e.g. "2024-10-02"
        self.speed   = settings.replay_speed    # 1.0 = real-time, 10 = 10× faster

        self.client = StockHistoricalDataClient(
            os.getenv("ALPACA_API_KEY"),
            os.getenv("ALPACA_SECRET"),
        )

    # ---------- common output ---------- #
    def _forward_price(self, price: float):
        """Identical interface to the live class."""
        print(price)
    # ----------------------------------- #

    def start(self):
        """Pull bars, then replay them one by one."""
        req = StockBarsRequest(
            symbol_or_symbols=self.ticker,
            timeframe=TimeFrame.Minute,
            start=self.start_date,
            end=self.end_date,
        )
        bars_df = self.client.get_stock_bars(req).df

        for _, row in bars_df.iterrows():
            price = row.close
            self._forward_price(price)
            time.sleep(60 / self.speed)

if __name__ == "__main__":
    # basic Settings instance
    settings = Settings()

    HistoricalMarketData(settings).start()      
