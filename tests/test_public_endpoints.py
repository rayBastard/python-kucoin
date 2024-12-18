import pytest

def test_spot_status(client):
    response = client.get_status()
    assert response is not None

@pytest.mark.asyncio()
async def test_spot_status_async(asyncClient):
    response = await asyncClient.get_status()
    assert response is not None

def test_futures_status(client):
    response = client.futures_get_status()
    assert response is not None

@pytest.mark.asyncio()
async def test_futures_status_async(asyncClient):
    response = await asyncClient.futures_get_status()
    assert response is not None

def test_announcements(client):
    response = client.get_announcements()
    assert response is not None

@pytest.mark.asyncio()
async def test_announcements_async(asyncClient):
    response = await asyncClient.get_announcements()
    assert response is not None

def test_currencies(client):
    response = client.get_currencies()
    assert response is not None

@pytest.mark.asyncio()
async def test_currencies_async(asyncClient):
    response = await asyncClient.get_currencies()
    assert response is not None

def test_currency(client):
    response = client.get_currency("BTC")
    currency = response["currency"]
    assert currency == "BTC"

# todo: throws TypeError: Invalid variable type: value should be str, int or float, got None of type <class 'NoneType'>
# @pytest.mark.asyncio()
# async def test_currency_async(asyncClient):
#     response = await asyncClient.get_currency("BTC")
#     currency = response["currency"]
#     assert currency == "BTC"

def test_symbols(client):
    response = client.get_symbols()
    assert response is not None

@pytest.mark.asyncio()
async def test_symbols_async(asyncClient):
    response = await asyncClient.get_symbols()
    assert response is not None

def test_symbol(client):
    response = client.get_symbol("ETH-USDT")
    symbol = response["symbol"]
    assert symbol == "ETH-USDT"

@pytest.mark.asyncio()
async def test_symbol_async(asyncClient):
    response = await asyncClient.get_symbol("ETH-USDT")
    symbol = response["symbol"]
    assert symbol == "ETH-USDT"

def test_ticker(client):
    response = client.get_ticker("ETH-USDT")
    assert response is not None

@pytest.mark.asyncio()
async def test_ticker_async(asyncClient):
    response = await asyncClient.get_ticker("ETH-USDT")
    assert response is not None

def test_tickers(client):
    response = client.get_tickers()
    assert response is not None

@pytest.mark.asyncio()
async def test_tickers_async(asyncClient):
    response = await asyncClient.get_tickers()
    assert response is not None

def test_24hr_stats(client):
    response = client.get_24hr_stats("ETH-USDT")
    symbol = response["symbol"]
    assert symbol == "ETH-USDT"

@pytest.mark.asyncio()
async def test_24hr_stats_async(asyncClient):
    response = await asyncClient.get_24hr_stats("ETH-USDT")
    symbol = response["symbol"]
    assert symbol == "ETH-USDT"

def test_markets(client):
    response = client.get_markets()
    assert response is not None

@pytest.mark.asyncio()
async def test_markets_async(asyncClient):
    response = await asyncClient.get_markets()
    assert response is not None

def test_order_book(client):
    response = client.get_order_book("ETH-USDT")
    assert response is not None

@pytest.mark.asyncio()
async def test_order_book_async(asyncClient):
    response = await asyncClient.get_order_book("ETH-USDT")
    assert response is not None

def test_trade_histories(client):
    response = client.get_trade_histories("ETH-USDT")
    assert response is not None

@pytest.mark.asyncio()
async def test_trade_histories_async(asyncClient):
    response = await asyncClient.get_trade_histories("ETH-USDT")
    assert response is not None

def test_klines(client):
    response = client.get_klines("ETH-USDT")
    assert response is not None

@pytest.mark.asyncio()
async def test_klines_async(asyncClient):
    response = await asyncClient.get_klines("ETH-USDT")
    assert response is not None

def test_fiat_prices(client):
    code = "BTC"
    response = client.get_fiat_prices(None, code)
    assert code in response

@pytest.mark.asyncio()
async def test_fiat_prices_async(asyncClient):
    code = "BTC"
    response = await asyncClient.get_fiat_prices(None, code)
    assert code in response

def test_futures_symbol(client):
    response = client.futures_get_symbol("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

@pytest.mark.asyncio()
async def test_futures_symbol_async(asyncClient):
    response = await asyncClient.futures_get_symbol("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

def test_futures_symbols(client):
    response = client.futures_get_symbols()
    assert response is not None

@pytest.mark.asyncio()
async def test_futures_symbols_async(asyncClient):
    response = await asyncClient.futures_get_symbols()
    assert response is not None

def test_futures_tickers(client):
    response = client.futures_get_tickers()
    assert response is not None

@pytest.mark.asyncio()
async def test_futures_tickers_async(asyncClient):
    response = await asyncClient.futures_get_tickers()
    assert response is not None

def test_futures_ticker(client):
    response = client.futures_get_ticker("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

@pytest.mark.asyncio()
async def test_futures_ticker_async(asyncClient):
    response = await asyncClient.futures_get_ticker("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

def test_futures_order_book(client):
    response = client.futures_get_order_book("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

@pytest.mark.asyncio()
async def test_futures_order_book_async(asyncClient):
    response = await asyncClient.futures_get_order_book("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

def test_futures_full_order_book(client):
    response = client.futures_get_full_order_book("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

@pytest.mark.asyncio()
async def test_futures_full_order_book_async(asyncClient):
    response = await asyncClient.futures_get_full_order_book("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

def test_futures_trade_histories(client):
    response = client.futures_get_trade_histories("ETHUSDTM")
    assert response is not None

@pytest.mark.asyncio()
async def test_futures_trade_histories_async(asyncClient):
    response = await asyncClient.futures_get_trade_histories("ETHUSDTM")
    assert response is not None

def test_futures_klines(client):
    response = client.futures_get_klines("ETHUSDTM")
    assert response is not None

@pytest.mark.asyncio()
async def test_futures_klines_async(asyncClient):
    response = await asyncClient.futures_get_klines("ETHUSDTM")
    assert response is not None

def test_futures_interest_rate(client):
    response = client.futures_get_interest_rate(".KXBT")
    assert response is not None

# todo:
# File "/opt/homebrew/lib/python3.11/site-packages/yarl/_url.py", line 946, in _query_var
#     raise TypeError(
# TypeError: Invalid variable type: value should be str, int or float, got True of type <class 'bool'>
# @pytest.mark.asyncio()
# async def test_futures_interest_rate_async(asyncClient):
#     response = await asyncClient.futures_get_interest_rate(".KXBT")
#     assert response is not None

def test_futures_index(client):
    response = client.futures_get_index(".KXBT")
    assert response is not None

# todo:
# File "/opt/homebrew/lib/python3.11/site-packages/yarl/_url.py", line 946, in _query_var
#     raise TypeError(
# TypeError: Invalid variable type: value should be str, int or float, got True of type <class 'bool'>
# @pytest.mark.asyncio()
# async def test_futures_index_async(asyncClient):
#     response = await asyncClient.futures_get_index(".KXBT")
#     assert response is not None

def test_futures_mark_price(client):
    response = client.futures_get_mark_price("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

@pytest.mark.asyncio()
async def test_futures_mark_price_async(asyncClient):
    response = await asyncClient.futures_get_mark_price("ETHUSDTM")
    symbol = response["symbol"]
    assert symbol == "ETHUSDTM"

def test_futures_premium_index(client):
    response = client.futures_get_premium_index("ETHUSDTM")
    assert response is not None

# todo:
# TypeError: Invalid variable type: value should be str, int or float, got True of type <class 'bool'>
# @pytest.mark.asyncio()
# async def test_futures_premium_index_async(asyncClient):
#     response = await asyncClient.futures_get_premium_index("ETHUSDTM")
#     assert response is not None

def test_margin_all_trading_pairs_mark_prices(client):
    response = client.margin_get_all_trading_pairs_mark_prices()
    assert response is not None

@pytest.mark.asyncio()
def test_margin_all_trading_pairs_mark_prices_async(asyncClient):
    response = asyncClient.margin_get_all_trading_pairs_mark_prices()
    assert response is not None

def test_futures_public_funding_history(client):
    response = client.futures_get_public_funding_history('ETHUSDTM', start=1622505600000, end=1622592000000)
    assert response is not None

@pytest.mark.asyncio()
async def test_futures_public_funding_history_async(asyncClient):
    response = await asyncClient.futures_get_public_funding_history('ETHUSDTM', start=1622505600000, end=1622592000000)
    assert response is not None