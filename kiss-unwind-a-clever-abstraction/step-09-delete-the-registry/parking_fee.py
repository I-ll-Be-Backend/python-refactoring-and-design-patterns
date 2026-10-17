from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Ticket:
    minutes: int
    electric: bool

    def hours(self) -> int:
        return (self.minutes + 59) // 60

def fee(t: Ticket) -> float:
    f = t.hours() * 3.0
    f = min(f, 20.0)
    f = 0.0 if t.minutes <= 15 else f
    return f


def charge(t: Ticket) -> float:
    return fee(t)
