# Flask UI Server

from flask import Flask, render_template, request
from bot import BasicBot
from logger import setup_logger
import os

setup_logger()

app = Flask(__name__)

# Replace with your testnet API key/Secret,I am not able to provide my credentials due to security reasons
API_KEY =  "your_api_key_here"
API_SECRET =  "your_api_secret_here"

bot = BasicBot(API_KEY, API_SECRET, testnet=True) # Configuring the bot using api credentials

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        side = request.form.get("side").upper()
        order_type = request.form.get("order_type").lower()
        quantity = float(request.form.get("quantity"))

        if order_type == "market":
            result = bot.place_market_order(symbol, side, quantity)
        elif order_type == "limit":
            price = request.form.get("price")
            result = bot.place_limit_order(symbol, side, quantity, price)
        elif order_type == "stop-limit":
            stop_price = request.form.get("stop_price")
            price = request.form.get("price")
            result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, price)
        else:
            result = {"error": "Unsupported order type."}

    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
