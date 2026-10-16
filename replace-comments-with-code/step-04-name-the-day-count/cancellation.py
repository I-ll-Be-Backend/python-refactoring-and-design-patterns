from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Booking:
    check_in: date
    total: float
    nights: int
    rate: str
    loyal: bool

def fee(b: Booking, today: date) -> float:
    days_before_check_in = (b.check_in - today).days
    # free cancellation 14 days or more before check-in
    if days_before_check_in >= 14:
        return 0
    # non-refundable or under 2 days out: pay in full
    if b.rate == "N" or days_before_check_in < 2:
        return b.total
    # otherwise half the total
    f = b.total * 0.5
    # partner contracts require a one-night minimum
    return max(f, b.total / b.nights)
