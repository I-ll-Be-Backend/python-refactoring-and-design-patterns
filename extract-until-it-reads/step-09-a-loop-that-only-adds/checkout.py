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
    discount = member_discount(order, goods)
    total = goods - discount + delivery_fee(order, goods)
    return f"{len(order.items)} items, ${total:.2f}"


def require_items(order: Order) -> None:
    if not order.items:
        raise ValueError("No items")


def subtotal(order: Order) -> float:
    cost = 0.0
    for item in order.items:
        cost += item.price * item.qty
    return cost


def member_discount(order: Order, goods: float) -> float:
    return goods * 0.10 if order.member else 0.0


def delivery_fee(order: Order, goods: float) -> float:
    fee = 0.0
    if goods < 50.0:
        fee += 4.99
    if order.express:
        fee += 7.50
    return fee
