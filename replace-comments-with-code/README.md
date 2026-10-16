# Clean code: replace comments with code, in Python

> Let the code say what it does, so no comment can drift into a lie.

[Watch the video](https://www.youtube.com/watch?v=-XIp7QVCOd0) · [Step through it interactively](https://illbebackend.dev/lessons/replace-comments-with-code/python/)

## The problem

Loyalty members now cancel free from 7 days. The if changed, and the comment above it didn't.

## Steps

Each folder holds the complete `cancellation.py` after that step, and every one compiles. Diff two neighbouring folders to see a single refactoring.

| Step | What changes | Move |
|---|---|---|
| [01](step-01-a-comment-on-every-rule/) | A comment on every rule: fee works out what a guest pays to cancel. Each rule has a comment above it that says what the line does. | Before |
| [02](step-02-the-comment-still-says-14/) | The comment still says 14: Loyalty members now cancel free from 7 days. The if changed, and the comment above it didn't. | Code smell |
| [03](step-03-back-it-out-then-name-things/) | Back it out, then name things: The loyalty rule comes out. Each comment that says what becomes a name, and then the comment goes. | Plan |
| [04](step-04-name-the-day-count/) | Name the day count: d becomes days_before_check_in, and the comment that explained d is gone. | Rename Variable |
| [05](step-05-name-the-fourteen/) | Name the fourteen: 14 becomes the module constant FREE_CANCELLATION_DAYS. | Replace Magic Number |
| [06](step-06-name-the-two-and-the-n/) | Name the two and the N: 2 becomes LAST_MINUTE_DAYS and "N" becomes NON_REFUNDABLE. | Replace Magic Number |
| [07](step-07-the-free-rule-gets-a-name/) | The free rule gets a name: _is_free_cancellation(days) holds the 14-day check. Its comment is gone. | Extract Function |
| [08](step-08-full-pay-gets-a-name/) | Full pay gets a name: _pays_in_full(b, days) holds the rate and last-minute check. Its comment is gone. | Extract Function |
| [09](step-09-name-the-half/) | Name the half: f becomes half_total, and the comment that said so is gone. | Rename Variable |
| [10](step-10-name-one-night-s-price/) | Name one night's price: total divided by nights moves into _nightly_price(b). | Extract Function |
| [11](step-11-one-comment-stays/) | One comment stays: The contract comment gives a reason the code can't show, so it stays. | Keep the why |
| [12](step-12-loyalty-in-one-place/) | Loyalty, in one place: _is_free_cancellation takes the booking and checks LOYALTY_FREE_DAYS for loyal guests. _pays_in_full and _nightly_price didn't change. | Payoff |

## Takeaways

- **Use it when:** A comment tells you what the next line or block does.
- **Skip it when:** The comment explains why, like a contract, a bug workaround or a law, or it's a docstring on a public API.
- **Spot it by:** A comment above a short block, a one-letter variable, or a bare number in a condition.
- **Already in Python:** timedelta takes its unit as a keyword, so fourteen days needs no comment.
