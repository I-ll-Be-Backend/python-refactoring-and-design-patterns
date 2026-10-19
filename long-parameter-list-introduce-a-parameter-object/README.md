# Long parameter list: introduce a parameter object, in Python

> Group the values that travel together, so a new one stops touching every signature.

[Watch the video](https://www.youtube.com/watch?v=DXzTifBc-bY) · [Step through it interactively](https://illbebackend.dev/lessons/long-parameter-list-introduce-a-parameter-object/python/)

## The problem

The carrier charges 20% more for fragile parcels. A fragile flag joins both signatures, both calls and a new check in price.

## Steps

Each folder holds the complete `shipping.py` after that step, and every one compiles. Diff two neighbouring folders to see a single refactoring.

| Step | What changes | Move |
|---|---|---|
| [01](step-01-a-quote-with-nine-parameters/) | A quote with nine parameters: Checkout passes two warehouse constants, the customer's address and five cart values to quote. Quote hands seven of them to the price method. | Before |
| [02](step-02-one-flag-five-edits/) | One flag, five edits: The carrier charges 20% more for fragile parcels. A fragile flag joins both signatures, both calls and a new check in price. | Code smell |
| [03](step-03-two-booleans-side-by-side/) | Two booleans side by side: Four signature and call edits came before the one check that uses fragile. Express and fragile now sit next to each other in every list. | Code smell |
| [04](step-04-back-it-out-then-group/) | Back it out, then group: Fragile comes out again. Three groups of values travel together through every list, and each one becomes a type first. | Plan |
| [05](step-05-the-origin-becomes-an-address/) | The origin becomes an Address: A frozen dataclass Address holds a postal code and a country. Quote and price take one origin, and checkout builds it from the warehouse constants. | Introduce Parameter Object |
| [06](step-06-the-destination-is-an-address-too/) | The destination is an Address too: The customer's postal code and country become a second Address. Both methods take origin and destination. | Introduce Parameter Object |
| [07](step-07-four-floats-become-a-parcel/) | Four floats become a Parcel: A frozen dataclass Parcel holds the weight and the three box sizes. Quote and price take four parameters each, and checkout builds the parcel from the cart. | Introduce Parameter Object |
| [08](step-08-name-the-weight-rule/) | Name the weight rule: The volumetric weight and the larger-of-two rule move into billable_kg. Price multiplies the rate by it. | Extract Method |
| [09](step-09-the-rule-moves-onto-parcel/) | The rule moves onto Parcel: billable_kg moves into Parcel and reads its own fields. Price asks the parcel for it. | Move Method |
| [10](step-10-fragile-in-three-edits/) | Fragile, in three edits: Fragile joins Parcel, checkout passes the cart's flag, and price adds the surcharge. Both signatures and the call inside quote didn't change. | Payoff |
| [11](step-11-why-the-clumps-paid-off/) | Why the clumps paid off: Each clump is one type, so a new parcel fact joins Parcel. Express is a parameter and fragile lives in the parcel. | Payoff |
| [12](step-12-four-floats-by-position/) | Four floats by position: Checkout fills Parcel by position: four floats and a flag in a row. | Code smell |
| [13](step-13-checkout-names-every-value/) | Checkout names every value: kw_only=True makes every Parcel field keyword-only. Checkout writes each name next to its value. | Keyword-only fields |

## Takeaways

- **Use it when:** The same group of values goes, in the same order, through several methods.
- **Skip it when:** A method takes three or four unrelated values used only there, like a log call with a level, a message and an error.
- **Spot it by:** The same names repeated across signatures, runs of same-typed arguments, a method that only passes its parameters on.
- **Already in Python:** datetime hands you one date where older code passed year, month and day.
