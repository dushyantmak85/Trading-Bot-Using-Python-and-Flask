def get_order_details():
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    order_type = input("Enter order type (market/limit/stop-limit): ").lower()
    side = input("Enter side (buy/sell): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    stop_price = None

    if order_type == "limit":
        price = float(input("Enter limit price: "))
    elif order_type == "stop-limit":
        stop_price = float(input("Enter stop price (trigger): "))
        price = float(input("Enter limit price (actual): "))

    return {
        "symbol": symbol,
        "order_type": order_type,
        "side": side,
        "quantity": quantity,
        "price": price,
        "stop_price": stop_price
    }
