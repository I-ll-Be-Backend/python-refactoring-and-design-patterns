from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Order:
    id: str
    total: float
    postal_code: str


class OrderRepo(Protocol):
    def today(self) -> list[Order]: ...


class Warehouse(Protocol):
    def upload_csv(self, csv: str) -> None: ...

# config.toml


def export_orders(orders: list[Order]) -> str:
    lines = ["id,total,postal_code"]
    for o in orders:
        row = f"{o.id},{o.total},{o.postal_code}"
        lines.append(row)
    return "\n".join(lines) + "\n"


@dataclass
class NightlyJob:
    orders: OrderRepo
    warehouse: Warehouse

    def run(self) -> None:
        csv = export_orders(self.orders.today())
        self.warehouse.upload_csv(csv)
