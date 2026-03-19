from bot.client import client
import logging

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing {order_type} order")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            return {"error": "Invalid order type"}

        logging.info(order)
        return order

    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}