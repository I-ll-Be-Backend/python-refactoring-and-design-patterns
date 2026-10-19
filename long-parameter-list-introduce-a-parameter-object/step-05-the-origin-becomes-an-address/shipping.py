from dataclasses import dataclass
from typing import Protocol


class RateTable(Protocol):
    def per_kg(self, from_country: str, to_country: str) -> float: ...


@dataclass(frozen=True)
class Quote:
    from_postal: str
    to_postal: str
    price: float


@dataclass(frozen=True)
class Cart:
    weight_kg: float
    length_cm: float
    width_cm: float
    height_cm: float
    express: bool
    fragile: bool


@dataclass(frozen=True)
class Customer:
    postal_code: str
    country: str

WAREHOUSE_POSTAL = "10115"
WAREHOUSE_COUNTRY = "DE"


@dataclass(frozen=True)
class Address:
    postal: str
    country: str


class ShippingService:
    def __init__(self, rates: RateTable) -> None:
        self.rates = rates

    def quote(self, origin: Address,
              to_postal: str, to_country: str, weight_kg: float,
              length_cm: float, width_cm: float, height_cm: float,
              express: bool) -> Quote:
        price = self._price(origin, to_country, weight_kg, length_cm,
                            width_cm, height_cm, express)
        return Quote(origin.postal, to_postal, price)

    def _price(self, origin: Address, to_country: str,
               weight_kg: float, length_cm: float, width_cm: float,
               height_cm: float, express: bool) -> float:
        volumetric_kg = length_cm * width_cm * height_cm / 5000
        rate = self.rates.per_kg(origin.country, to_country)
        cost = rate * max(weight_kg, volumetric_kg)
        return cost * 1.5 if express else cost


class Checkout:
    def __init__(self, shipping: ShippingService) -> None:
        self.shipping = shipping

    def shipping_for(self, cart: Cart, customer: Customer) -> Quote:
        origin = Address(WAREHOUSE_POSTAL, WAREHOUSE_COUNTRY)
        return self.shipping.quote(
            origin,
            customer.postal_code, customer.country, cart.weight_kg,
            cart.length_cm, cart.width_cm, cart.height_cm,
            cart.express)
