"""Shipping rate calculations."""


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars; express adds $7 to the standard quote."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in {"standard", "express"}:
        raise ValueError("unknown service")
    base = 5.0 if zone == "local" else 8.0
    standard_quote = round(base + 1.5 * weight_kg, 2)
    return round(standard_quote + 7.0, 2) if service == "express" else standard_quote
