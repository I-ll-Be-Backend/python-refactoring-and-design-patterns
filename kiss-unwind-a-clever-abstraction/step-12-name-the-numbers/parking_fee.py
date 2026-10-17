from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Ticket:
    minutes: int
    electric: bool

    def hours(self) -> int:
        return (self.minutes + 59) // 60

HOURLY_RATE = 3.0
DAILY_CAP = 20.0
GRACE_MINUTES = 15


def charge(t: Ticket) -> float:
    if t.minutes <= GRACE_MINUTES:
        return 0.0
    return min(t.hours() * HOURLY_RATE, DAILY_CAP)
