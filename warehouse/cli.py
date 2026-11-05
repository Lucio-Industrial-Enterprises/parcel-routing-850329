"""Command-line shipping quote."""

import argparse
from .rates import shipping_quote


def main() -> None:
    parser = argparse.ArgumentParser(description="Quote shipping for an order")
    parser.add_argument("weight_kg", type=float)
    parser.add_argument("zone", choices=["local", "regional"])
    args = parser.parse_args()
    print(f"${shipping_quote(args.weight_kg, args.zone):.2f}")


if __name__ == "__main__":
    main()
