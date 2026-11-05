"""Shipping rate calculations."""


def shipping_quote(weight_kg: float, zone: str) -> float:
    """Quote standard shipping in dollars."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    base = 5.0 if zone == "local" else 8.0
    return round(base + 1.5 * weight_kg, 2)
