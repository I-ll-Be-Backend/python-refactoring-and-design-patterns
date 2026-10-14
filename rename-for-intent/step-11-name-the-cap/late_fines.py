from dataclasses import dataclass

@dataclass(frozen=True)
class Loan:
    days_out: int
    student: bool


LOAN_DAYS = 14
STUDENT_RATE = 0.10
STANDARD_RATE = 0.25
MAX_FINE = 10.0


def calc(loan: Loan) -> float:
    days_late = loan.days_out - LOAN_DAYS
    if days_late <= 0:
        return 0.0
    daily_rate = STUDENT_RATE if loan.student else STANDARD_RATE
    return min(days_late * daily_rate, MAX_FINE)


def receipt(loan: Loan) -> str:
    return f"Late fine: ${calc(loan):.2f}"
