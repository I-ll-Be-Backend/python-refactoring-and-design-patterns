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


@dataclass(frozen=True)
class Parcel:
    weight_kg: float
    length_cm: float
    width_cm: float
    height_cm: float

    def billable_kg(self) -> float:
        volumetric_kg = (self.length_cm * self.width_cm
                         * self.height_cm / 5000)
        return max(self.weight_kg, volumetric_kg)


class ShippingService:
    def __init__(self, rates: RateTable) -> None:
        self.rates = rates

    def quote(self, origin: Address, destination: Address,
              parcel: Parcel, express: bool) -> Quote:
        price = self._price(origin, destination, parcel, express)
        return Quote(origin.postal, destination.postal, price)

    def _price(self, origin: Address, destination: Address,
               parcel: Parcel, express: bool) -> float:
        rate = self.rates.per_kg(origin.country, destination.country)
        cost = rate * parcel.billable_kg()
        return cost * 1.5 if express else cost


class Checkout:
    def __init__(self, shipping: ShippingService) -> None:
        self.shipping = shipping

    def shipping_for(self, cart: Cart, customer: Customer) -> Quote:
        origin = Address(WAREHOUSE_POSTAL, WAREHOUSE_COUNTRY)
        destination = Address(customer.postal_code, customer.country)
        parcel = Parcel(cart.weight_kg, cart.length_cm,
                        cart.width_cm, cart.height_cm)
        return self.shipping.quote(origin, destination, parcel, cart.express)
