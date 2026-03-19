--------Welcome-------
Trading Bot - Binance Futures Testnet

Overview
This is a Python CLI trading bot to place MARKET and LIMIT orders on Binance Futures Testnet.

Setup
pip install -r requirements.txt

Run

MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

LIMIT Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.006 --price 20000

Features
1.BUY and SELL support
2.MARKET and LIMIT orders
3.CLI input
4.Logging
5.Error handling

Folder Structure
trading_bot/
  bot/
    client.py
    orders.py
    logging_config.py
  cli.py
  requirements.txt
