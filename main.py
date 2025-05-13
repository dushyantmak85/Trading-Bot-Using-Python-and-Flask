from bot import BasicBot
from cli import get_order_details
from logger import setup_logger
import os

if __name__ == "__main__":
    setup_logger()

    # Replace with your Testnet API credentials
    API_KEY = os.getenv('BINANCE_TESTNET_KEY')
    API_SECRET = os.getenv('BINANCE_TESTNET_SECRET')

    bot = BasicBot(API_KEY, API_SECRET, testnet=True)

    order_data = get_order_details()

    if order_data['order_type'] == 'market':
        result = bot.place_market_order(
            order_data['symbol'],
            order_data['side'],
            order_data['quantity']
        )
    elif order_data['order_type'] == 'limit':
        result = bot.place_limit_order(
            order_data['symbol'],
            order_data['side'],
            order_data['quantity'],
            order_data['price']
        )
    elif order_data['order_type'] == 'stop-limit':
        result = bot.place_stop_limit_order(
        order_data['symbol'],
        order_data['side'],
        order_data['quantity'],
        order_data['stop_price'],
        order_data['price']
        )

    else:
        print("Invalid order type.")
        result = None

    if result:
        print("Order executed:", result)
    else:
        print("Order failed. Check logs for details.")
