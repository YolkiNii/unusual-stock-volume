import pytest
from app.stock_list import StockList

class TestStockList:
  @pytest.fixture
  def stock_list(self):
    return StockList()
  
  def test_initialized(self, stock_list):
    assert stock_list

  def test_stocks_exist(self, stock_list):
    assert not stock_list.bars_df.empty
