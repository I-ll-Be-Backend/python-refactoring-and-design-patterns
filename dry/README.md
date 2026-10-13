# DRY: one rule, one place, in Python

> Change a business rule once and have every feature pick it up.

[Watch the video](https://www.youtube.com/watch?v=JoxpOg_EUKk) · [Step through it interactively](https://illbebackend.dev/lessons/dry/python/)

## The problem

The member limit is added to shipping_fee and banner_message by hand. email_line is missed and still uses 50.0.

## Steps

Each folder holds the complete `shipping.py` after that step, and every one compiles. Diff two neighbouring folders to see a single refactoring.

| Step | What changes | Move |
|---|---|---|
| [01](step-01-three-features-one-rule/) | Three features, one rule: shipping_fee, banner_message and email_line each test subtotal >= 50.0 on their own. The fee 4.99 is typed twice. | Before |
| [02](step-02-members-ship-free-from-25/) | Members ship free from 25: The member limit is added to shipping_fee and banner_message by hand. email_line is missed and still uses 50.0. | Code smell |
| [03](step-03-undo-then-give-it-a-home/) | Undo, then give it a home: Back the member change out. Gather the limit, the fee and the check at the top of the module, then add members again. | Plan |
| [04](step-04-name-the-limit/) | Name the limit: The four copies of 50.0 become FREE_SHIPPING_FROM at the top of the module. | Replace Magic Number with Constant |
| [05](step-05-name-the-fee/) | Name the fee: The two copies of 4.99 become SHIPPING_FEE. | Replace Magic Number with Constant |
| [06](step-06-name-the-check/) | Name the check: The comparison moves into ships_free(cart). shipping_fee calls it. | Extract Function |
| [07](step-07-the-banner-asks-too/) | The banner asks too: banner_message's hand-written check becomes not ships_free(cart). | Replace Inline Code with Function Call |
| [08](step-08-the-email-asks-too/) | The email asks too: email_line calls ships_free(cart). The comparison now exists once. | Replace Inline Code with Function Call |
| [09](step-09-name-the-gap/) | Name the gap: The banner's subtraction moves into amount_to_free_shipping(cart), next to ships_free. | Extract Function |
| [10](step-10-members-in-one-helper/) | Members, in one helper: The member limit is a new constant and a private helper, _free_from. The three feature functions don't change. | Payoff |

## Takeaways

- **Use it when:** One business rule, number or decision shows up in more than one feature.
- **Skip it when:** Two lines look alike but follow different rules, like a shipping fee and a gift wrap fee that both cost 4.99.
- **Spot it by:** The same literal or condition in several functions, and changes that start with a search.
