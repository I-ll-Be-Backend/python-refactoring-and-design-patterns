from dataclasses import dataclass


@dataclass(frozen=True)
class Cart:
    subtotal: float
    member: bool

def shipping_fee(cart: Cart) -> float:
    free_from = 25.0 if cart.member else 50.0
    if cart.subtotal >= free_from:
        return 0.0
    return 4.99


def banner_message(cart: Cart) -> str:
    limit = 25.0 if cart.member else 50.0
    if cart.subtotal < limit:
        missing = limit - cart.subtotal
        return f"Add ${missing:.2f} to ship free"
    return "Your order ships free"


def email_line(cart: Cart) -> str:
    free = cart.subtotal >= 50.0
    return "Shipping: free" if free else "Shipping: $4.99"
