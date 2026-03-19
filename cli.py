import argparse
from bot.orders import place_order
import bot.logging_config  # initialize logging

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

print("------ Order Request ------")
print(f"Symbol: {args.symbol}")
print(f"Side: {args.side}")
print(f"Type: {args.type}")
print(f"Quantity: {args.quantity}")
print(f"Price: {args.price}")

result = place_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

print("\n------ Response ------")
print("Order ID:", result.get("orderId"))
print("Status:", result.get("status"))
print("Executed Qty:", result.get("executedQty"))
print("Full Response:", result)

if not result or "error" in result:
    print(" Order Failed..!")
else:
    print("Order Successful..!")