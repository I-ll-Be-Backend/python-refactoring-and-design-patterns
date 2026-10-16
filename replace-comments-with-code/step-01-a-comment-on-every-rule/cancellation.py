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
    # days left before check-in
    d = (b.check_in - today).days
    # free cancellation 14 days or more before check-in
    if d >= 14:
        return 0
    # non-refundable or under 2 days out: pay in full
    if b.rate == "N" or d < 2:
        return b.total
    # otherwise half the total
    f = b.total * 0.5
    # partner contracts require a one-night minimum
    return max(f, b.total / b.nights)
