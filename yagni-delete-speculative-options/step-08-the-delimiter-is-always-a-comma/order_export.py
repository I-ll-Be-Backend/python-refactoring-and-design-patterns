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
# [export]
# header = true

@dataclass(frozen=True)
class ExportConfig:
    header: bool


class OrderExport:
    def __init__(self, cfg: ExportConfig) -> None:
        self.header = cfg.header

    def export(self, orders: list[Order]) -> str:
        lines: list[str] = []
        if self.header:
            lines.append("id,total")
        for o in orders:
            row = f"{o.id},{o.total}"
            lines.append(row)
        return "\n".join(lines) + "\n"


@dataclass
class NightlyJob:
    config: ExportConfig
    orders: OrderRepo
    warehouse: Warehouse

    def run(self) -> None:
        csv = OrderExport(self.config).export(self.orders.today())
        self.warehouse.upload_csv(csv)
