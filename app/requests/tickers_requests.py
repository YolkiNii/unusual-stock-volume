import os

def get_all_tickers():
  # Get path of current file
  current_dir = os.path.dirname(__file__)

  # Read from all_tickers file
  with open(os.path.join(current_dir, "../data/all_tickers.txt")) as f:
    raw_all_tickers = f.read()
    all_tickers = raw_all_tickers.split("\n")

  unwanted_ticker_letters = ["W", "Q", "E", "C"]

  return [ticker for ticker in all_tickers if len(ticker) < 5 or \
          (len(ticker) > 4 and ticker[-1] not in unwanted_ticker_letters)]