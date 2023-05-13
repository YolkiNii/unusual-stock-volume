import os
import datetime
import pytz
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from dotenv import load_dotenv
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET = os.getenv("ALPACA_SECRET")

class StockList:
  US_BUISNESS_DAY = CustomBusinessDay(calendar=USFederalHolidayCalendar())
  MARKET_SESSION_END_TIME = datetime.time(20, 20, 0, tzinfo=pytz.timezone("US/Eastern"))
  ALPACA_STOCK_CLIENT = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET)

  def __init__(self):
    self.bars_df = self.request_all_30_day_history_bars()

  def request_all_30_day_history_bars(self):
    # Get list of all symbols
    symbols = self.get_all_symbols()

    # Get end date
    end_date = self.get_end_date()

    # Get start date
    start_date = self.get_n_business_days_before(end_date, 30)

    # Format request parameters
    request_params = StockBarsRequest(
                          symbol_or_symbols=symbols,
                          timeframe=TimeFrame.Day,
                          start=start_date,
                          end=end_date
                      )
    
    bars = self.ALPACA_STOCK_CLIENT.get_stock_bars(request_params)

    return bars.df

  def get_n_business_days_before(self, date, n):
    return datetime.datetime.combine((date - n * self.US_BUISNESS_DAY).date(), \
                                      datetime.time(0, 0, 0), \
                                      pytz.timezone("US/Eastern"))

  def get_end_date(self):
    # Get current datetime in US/Eastern timezone
    today = datetime.datetime.now(pytz.timezone("US/Eastern"))

    # Return last business day if today is a weekend or holiday or today's
    # business day session has not ended
    if (today != pd.Timestamp(today - 0 * self.US_BUISNESS_DAY) or \
        today.time() < self.MARKET_SESSION_END_TIME):
      return datetime.datetime.combine((today - 1 * self.US_BUISNESS_DAY).date(), \
                                        datetime.time(20, 20, 0), \
                                        pytz.timezone("US/Eastern"))
    
    return today

  def get_all_symbols(self):
    # Get path of current file
    current_dir = os.path.dirname(__file__)

    # Read from all_tickers file
    with open(os.path.join(current_dir, "./data/all_tickers.txt")) as f:
      raw_all_tickers = f.read()
      all_tickers = raw_all_tickers.split("\n")

    unwanted_ticker_letters = ["W", "Q", "E", "C"]

    return [ticker for ticker in all_tickers if len(ticker) < 5 or \
          (len(ticker) > 4 and ticker[-1] not in unwanted_ticker_letters)]
  
  class Stock:
    def __init__(self, symbol, bars):
      self.symbol = symbol
      self.bars = bars