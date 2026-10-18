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
# format = "csv"
# delimiter = ","
# header = true

@dataclass(frozen=True)
class ExportConfig:
    format: str
    delimiter: str
    header: bool


class OrderExport:
    def __init__(self, cfg: ExportConfig) -> None:
        self.format = cfg.format
        self.delimiter = cfg.delimiter
        self.header = cfg.header

    def export(self, orders: list[Order]) -> str:
        lines: list[str] = []
        if self.header and self.format == "csv":
            lines.append(f"id{self.delimiter}total")
        for o in orders:
            match self.format:
                case "csv":
                    row = f"{o.id}{self.delimiter}{o.total}"
                case "json":
                    row = f'{{"id":"{o.id}","total":{o.total}}}'
                case "xml":
                    row = f'<order id="{o.id}" total="{o.total}"/>'
                case _:
                    raise ValueError(self.format)
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
