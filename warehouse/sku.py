"""SKU normalization."""


def normalize_sku(value: str) -> str:
    """Return a canonical SKU suitable for labels and lookup."""
    if not value or not value.strip():
        raise ValueError("SKU must not be blank")
    return value.strip().upper()
