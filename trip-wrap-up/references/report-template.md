# Report template

Use confirmed financial fields only. Unknown optional date/place/merchant may say "unknown". Manual expenses say "user entry; no source photo". Never invent sources or links. Exclude card digits, account details, unrelated private photos and raw OCR text.

```text
# Trip Wrap-Up: [confirmed trip label]
Skill 0.2.1 · Report revision: [revision]
[first day] to [last day] · Trip timezone: [timezone]
Members in rounding order: [labels] · Settlement currency: [ISO code]
Scope: [confirmed spaces and enforced album/folder restrictions]
Coverage: [confirmed inputs only / limited coverage and specific reasons]
Omitted costs can change this result. Photo activity is a memory checklist, not proof of complete expense coverage.
Supersedes: [prior verified report path, if applicable]

## Final transfers
[debtor] → [creditor]: [currency] [amount]
[If none: Everyone is even for the confirmed shared expenses.]

## Balances and arithmetic checks
| Member | Paid | Equal share | Net (paid minus share) |
Shared ledger total: [amount]
Total paid = total shares = [amount]
Sum of original net balances = 0.00
All residual balances after transfers = 0.00
Transfer count: [count], at most [n-1]; no self/zero/negative transfers
Rounding: [r] minor unit(s) assigned to [labels] in confirmed member order

## Expenses by day
| Day | Matched photos | Unique receipt candidates | Unreadable/pending | Confirmed shared receipts | Spending decision |
Include every trip day, including days with no photos. Keep unknown receipt dates in a separate row.

## Expenses by place
| Place across the whole trip | Dates visited if known | Matched photos | Unique receipt candidates | Unreadable/pending | Confirmed shared receipts | Spending decision |
Use one row per known place even when visited on several days. Unknown places stay separate.

For both views, unknown counts stay unknown. Count a duplicated transaction once after review. Never sum overlapping place searches as unique photos. Explain whether zero confirmed receipts means none found, unreadable candidates, or pending confirmation. Keep any search coverage limitation beside the count. A free activity may have no receipts; record the user's answer. A group with receipts may still have missing expenses.

## Confirmed shared receipts
| ID | Date | Place | Merchant | Original amount and ISO currency | Rate ID | Converted amount | Payer | Full source path and picture ID, or manual entry |

## Personal entries and exclusions
| ID/source | Reason (personal, unrelated, duplicate of ID, unreadable or other explicit exclusion) | Known amount/currency | User decision |
Record known omissions and any unknown cost that could change the result. Do not include card digits.

## Exchange rates
| Rate ID | 1 foreign unit = X settlement units | Applicable receipt IDs | User-supplied basis/date if given |
Round each converted receipt once to the nearest settlement cent, half up.

## Search and extraction coverage
| Query scope | Matched total | Individually returned candidates | Exhaustive access or specific gap |
Candidates merged by picture ID: [count]
Confirmed input images: [count]; extracted: [count]; unreadable/failed: [count]
Upload-window check: [confirmed window and limits, or not performed]
Currency, tip, payer and duplicate decisions: [confirmed decisions]
Manual corrections/added expenses: [IDs and changes]
Date-uncertain photos: [IDs and user's decisions]
Known omissions: [specific list, or none among reviewed candidates]

## Notes
These are amounts to settle; the Skill does not make payments or send messages.
Confirm that members can open the saved report.
The totals cover the confirmed expenses listed here.
```

Omit the supersedes line, personal/exclusion table or exchange-rate table only when inapplicable. Keep coverage and arithmetic checks even with no shared expenses. The verified saved path belongs in the final conversation; do not guess it before saving.
