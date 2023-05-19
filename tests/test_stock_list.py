import pytest
from app.stock_list import StockList

class TestStockList:
  @pytest.fixture
  def stock_list(self):
    return StockList()
  
  def test_initialized(self, stock_list):
    assert stock_list

  def test_stocks_bars_exist(self, stock_list):
    bars_df = stock_list.request_all_30_day_history_bars()

    assert not bars_df.empty
