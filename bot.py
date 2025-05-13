from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        self.logger = logging.getLogger(__name__)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            self.logger.info(f"Market Order Placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Market Order Error: {str(e)}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            self.logger.info(f"Limit Order Placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Limit Order Error: {str(e)}")
            return None
        
    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP,
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            self.logger.info(f"Stop-Limit Order Placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Stop-Limit Order Error: {str(e)}")
            return None

