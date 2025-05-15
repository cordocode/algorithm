import os

class Settings:
    """central configuration"""
        
    def __init__(self):
        #trading symbold
        self.ticker = "NVDA"

        #market data entry
        self.historical_cache = 1000

        #news input
        self.news_frequency = 5 # minutes
        self.sort = "LATEST"
        self.limit = 1

        #trading settings
        self.trade_amount = 20