from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Ticket:
    minutes: int
    electric: bool

    def hours(self) -> int:
        return (self.minutes + 59) // 60

Rule = Callable[[Ticket, float], float]

RULES: dict[str, Rule] = {
    "base": lambda t, f: t.hours() * 3.0,
    "cap": lambda t, f: min(f, 20.0),
    "grace": lambda t, f: 0.0 if t.minutes <= 15 else f,
}


def fee(t: Ticket) -> float:
    f = t.hours() * 3.0
    f = RULES["cap"](t, f)
    f = RULES["grace"](t, f)
    return f


def charge(t: Ticket) -> float:
    return fee(t)
