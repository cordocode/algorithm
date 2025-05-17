import os

class Settings:
    """central configuration"""
        
    def __init__(self):
        #trading symbold
        self.ticker = "NVDA"

        #news input
        self.news_frequency = 5 # minutes
        self.sort = "LATEST"
        self.limit = 1

        #trading settings
        self.trade_amount = 20

        #historical data extraction
        #format = YYYY-MM-DD
        #time defaults to begining of day - use RFC-3339 for more specific time
        self.historical_start = "2024-10-01"
        self.historical_end = "2024-10-02"
        self.replay_speed = 60

        #historical news extraction
        #format looks like 20220410T0130 - YYYYMMDDTHHMM
        self.time_from = "20241001T0700"
        self.time_to = "20241001T1100"