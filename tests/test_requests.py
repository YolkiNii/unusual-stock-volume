import app.requests.tickers_requests as tickers_requests

class TestRequests:
  def test_get_all_tickers(self):
    tickers = tickers_requests.get_all_tickers()

    # Assert that we have tickers
    assert len(tickers) > 0

    unwantedTickers = []
    unwantedTickerLetters = ["W", "Q", "E", "C"]

    # Add any unwanted tickers in the unwanted list
    for ticker in tickers:
      if len(ticker) > 4 and ticker[-1] in unwantedTickerLetters:
        unwantedTickers.append(ticker)

    # Asset that we have no unwanted tickers
    assert len(unwantedTickers) == 0
