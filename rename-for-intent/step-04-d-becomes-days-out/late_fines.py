from dataclasses import dataclass

@dataclass(frozen=True)
class Loan:
    days_out: int
    f: bool


def calc(l: Loan) -> float:
    x = l.days_out - 14
    if x <= 0:
        return 0.0
    r = 0.10 if l.f else 0.25
    return min(x * r, 10.0)


def receipt(l: Loan) -> str:
    return f"Late fine: ${calc(l):.2f}"
