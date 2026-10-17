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
    "ev": lambda t, f: max(0.0, f - 6.0) if t.electric else f,
    "cap": lambda t, f: min(f, 20.0),
    "grace": lambda t, f: 0.0 if t.minutes <= 15 else f,
}


def fee(t: Ticket, plan: list[str]) -> float:
    f = 0.0
    for name in plan:
        f = RULES[name](t, f)
    return f


def charge(t: Ticket) -> float:
    return fee(t, ["base", "ev", "cap", "grace"])
