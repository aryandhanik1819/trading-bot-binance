import argparse
import logging

from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        if args.type == "LIMIT" and not args.price:
            raise ValueError("Price is required for LIMIT orders")

        client = get_client()

        print("\n📌 Order Request Summary")
        print(vars(args))

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Success")
        print("\n🔍 Full Order Response:")
        print(order)

        print("\n📊 Important Fields:")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Average Price:", order.get("avgPrice"))


    except Exception as e:
        print("\n❌ Order Failed:", e)
        logging.error(str(e))

if __name__ == "__main__":
    main()
