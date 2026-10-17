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
EV_FREE_HOURS = 2


def charge(t: Ticket) -> float:
    if t.minutes <= GRACE_MINUTES:
        return 0.0
    hours = t.hours()
    if t.electric:
        hours = max(0, hours - EV_FREE_HOURS)
    return min(hours * HOURLY_RATE, DAILY_CAP)
