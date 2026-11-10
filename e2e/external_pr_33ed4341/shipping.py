"""Shipping fee rule added by the external PR."""


def shipping_fee(order_total: float) -> float:
    """Orders of 50 or more ship free; smaller orders pay a flat 5."""
    if order_total >= 50:
        return 0.0
    return 5.0
