from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Ticket:
    minutes: int
    electric: bool

    def hours(self) -> int:
        return (self.minutes + 59) // 60

def charge(t: Ticket) -> float:
    if t.minutes <= 15:
        return 0.0
    return min(t.hours() * 3.0, 20.0)
