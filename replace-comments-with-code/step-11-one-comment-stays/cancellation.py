from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Booking:
    check_in: date
    total: float
    nights: int
    rate: str
    loyal: bool

FREE_CANCELLATION_DAYS = 14
LAST_MINUTE_DAYS = 2
NON_REFUNDABLE = "N"


def fee(b: Booking, today: date) -> float:
    days_before_check_in = (b.check_in - today).days
    if _is_free_cancellation(days_before_check_in):
        return 0
    if _pays_in_full(b, days_before_check_in):
        return b.total
    half_total = b.total * 0.5
    # partner contracts require a one-night minimum
    return max(half_total, _nightly_price(b))


def _is_free_cancellation(days: int) -> bool:
    return days >= FREE_CANCELLATION_DAYS


def _pays_in_full(b: Booking, days: int) -> bool:
    return b.rate == NON_REFUNDABLE or days < LAST_MINUTE_DAYS


def _nightly_price(b: Booking) -> float:
    return b.total / b.nights
