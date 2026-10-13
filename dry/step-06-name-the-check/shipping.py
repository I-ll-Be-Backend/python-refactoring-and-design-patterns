from dataclasses import dataclass


@dataclass(frozen=True)
class Cart:
    subtotal: float
    member: bool

FREE_SHIPPING_FROM = 50.0
SHIPPING_FEE = 4.99


def ships_free(cart: Cart) -> bool:
    return cart.subtotal >= FREE_SHIPPING_FROM


def shipping_fee(cart: Cart) -> float:
    if ships_free(cart):
        return 0.0
    return SHIPPING_FEE


def banner_message(cart: Cart) -> str:
    if cart.subtotal < FREE_SHIPPING_FROM:
        missing = FREE_SHIPPING_FROM - cart.subtotal
        return f"Add ${missing:.2f} to ship free"
    return "Your order ships free"


def email_line(cart: Cart) -> str:
    free = cart.subtotal >= FREE_SHIPPING_FROM
    return "Shipping: free" if free else f"Shipping: ${SHIPPING_FEE}"
