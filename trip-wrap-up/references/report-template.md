# Report template

Fill every section with confirmed values only. Leave out a section only where this file says it is optional. Amounts are shown in the settlement currency with two decimals.

## Layout

```text
# Trip Wrap-Up: [trip name]
[first day] to [last day] · Members: [names in the order the user gave] · Settlement currency: [code]

## 💸 Final transfers
[debtor] → [creditor]: [currency] [amount]
(one line per transfer; if nobody owes anything, write "Everyone is already even.")

## Balances
| Member | Paid | Share | Net |
Self-check: sum of net balances = 0.00 ✔
Rounding: [r] cent(s) of remainder assigned to [names], following the member order.

## Shared receipts
| # | Date | Merchant | Original amount | Rate | Amount in settlement currency | Paid by | Source photo |

## Personal receipts (not split)
| # | Date | Merchant | Amount | Paid by | Source photo |
(optional: include only if the user marked any receipt as personal)

## Exchange rates used
[foreign currency] → [settlement currency]: [rate], provided by the user
(optional: include only if more than one currency appeared)

## Notes
- Values the user corrected by hand: [list]
- Suspected duplicates the user dropped: [list]
- Receipts that could not be read and were typed in by the user: [list]
- This report says who should pay whom. It does not move any money.
```

## Rules

- Put the final transfers first, so that someone who reads only the top lines still knows what to pay.
- The source photo column shows the file name returned by photo-agent, so anyone can open the original receipt.
- Never fill a cell with a guessed value. If a value is unknown, the workflow must stop before this report is built.
