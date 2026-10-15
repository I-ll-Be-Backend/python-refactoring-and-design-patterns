from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    price: float
    qty: int


@dataclass(frozen=True)
class Order:
    items: list[Item]
    express: bool
    member: bool

def confirm(order: Order) -> str:
    require_items(order)
    goods = subtotal(order)
    total = goods
    if goods < 50.0:
        total += 4.99
    if order.express:
        total += 7.50
    return f"{len(order.items)} items, ${total:.2f}"


def require_items(order: Order) -> None:
    if not order.items:
        raise ValueError("No items")


def subtotal(order: Order) -> float:
    cost = 0.0
    for item in order.items:
        cost += item.price * item.qty
    return cost
