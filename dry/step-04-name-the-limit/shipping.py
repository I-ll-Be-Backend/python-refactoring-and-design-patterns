from dataclasses import dataclass


@dataclass(frozen=True)
class Cart:
    subtotal: float
    member: bool

FREE_SHIPPING_FROM = 50.0


def shipping_fee(cart: Cart) -> float:
    if cart.subtotal >= FREE_SHIPPING_FROM:
        return 0.0
    return 4.99


def banner_message(cart: Cart) -> str:
    if cart.subtotal < FREE_SHIPPING_FROM:
        missing = FREE_SHIPPING_FROM - cart.subtotal
        return f"Add ${missing:.2f} to ship free"
    return "Your order ships free"


def email_line(cart: Cart) -> str:
    free = cart.subtotal >= FREE_SHIPPING_FROM
    return "Shipping: free" if free else "Shipping: $4.99"
