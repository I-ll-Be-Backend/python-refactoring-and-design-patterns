from dataclasses import dataclass


@dataclass(frozen=True)
class Cart:
    subtotal: float
    member: bool

FREE_SHIPPING_FROM = 50.0
MEMBER_FREE_SHIPPING_FROM = 25.0
SHIPPING_FEE = 4.99


def _free_from(cart: Cart) -> float:
    return MEMBER_FREE_SHIPPING_FROM if cart.member else FREE_SHIPPING_FROM


def ships_free(cart: Cart) -> bool:
    return cart.subtotal >= _free_from(cart)


def amount_to_free_shipping(cart: Cart) -> float:
    return _free_from(cart) - cart.subtotal


def shipping_fee(cart: Cart) -> float:
    if ships_free(cart):
        return 0.0
    return SHIPPING_FEE


def banner_message(cart: Cart) -> str:
    if not ships_free(cart):
        missing = amount_to_free_shipping(cart)
        return f"Add ${missing:.2f} to ship free"
    return "Your order ships free"


def email_line(cart: Cart) -> str:
    free = ships_free(cart)
    return "Shipping: free" if free else f"Shipping: ${SHIPPING_FEE}"
