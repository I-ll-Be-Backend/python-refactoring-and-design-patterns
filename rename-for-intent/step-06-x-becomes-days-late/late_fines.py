from dataclasses import dataclass

@dataclass(frozen=True)
class Loan:
    days_out: int
    student: bool


def calc(l: Loan) -> float:
    days_late = l.days_out - 14
    if days_late <= 0:
        return 0.0
    r = 0.10 if l.student else 0.25
    return min(days_late * r, 10.0)


def receipt(l: Loan) -> str:
    return f"Late fine: ${calc(l):.2f}"
