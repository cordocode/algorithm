import os

class Settings:
    """central configuration"""
        
    def __init__(self):
        #trading symbold
        self.ticker = "NVDA"

        #data input
        self.interval = "60min"
        self.extended_hours = True

        self.data_frequency = 60

        #new input
        self.news_frequency = 5 # minutes
        self.sort = "LATEST"
        self.limit = 1

        #trading settings
        self.trade_amount = 20