# Settlement math

The parent Skill does this arithmetic itself after the user confirms every shared receipt. Work in **integer cents** of the settlement currency so that rounding never makes money appear or disappear.

## 1. Convert to the settlement currency

For each shared receipt in a foreign currency, multiply the amount by the rate the user confirmed (1 foreign unit = rate settlement units) and round to the nearest cent, with half a cent rounding up. Record the original amount, the rate, and the converted amount in the report. If a rate is missing, stop and ask the user. Never estimate a rate.

## 2. Each member's share

- Let **S** be the total of all shared receipts, in cents.
- Let **n** be the number of trip members.
- Base share: **b = floor(S / n)**. Remainder: **r = S − b × n**, where 0 ≤ r < n.
- In the order the user listed the members, the first **r** members owe **b + 1** cents and everyone else owes **b** cents. The shares then add up to exactly S. The report states that the rounding remainder was assigned this way.

Personal receipts are not part of S.

## 3. Balances

For each member i:

- **paid(i)**: the sum of the shared receipts that member i paid, in cents.
- **net(i) = paid(i) − share(i)**.

A positive net means the group owes this member money. A negative net means this member owes the group.

**Zero-sum self-check:** the sum of net(i) over all members must equal exactly 0. If it does not, stop and report the mismatch. Do not save a report.

## 4. Transfers (greedy matching)

1. Make two lists: creditors (net > 0) and debtors (net < 0).
2. Take the debtor who owes the most and the creditor who is owed the most. Break ties by the member order the user gave.
3. The debtor pays the creditor **min(amount owed, amount due)**. Record "debtor → creditor: amount".
4. Subtract that amount from both balances. Anyone whose balance reaches 0 leaves the lists.
5. Repeat until both lists are empty.

Every round settles at least one person, and the last round settles two. So there are **at most n − 1 transfers**. This rule does not always find the smallest possible number of transfers. Finding that minimum is NP-hard in general, so the report says "at most n − 1 transfers", never "the fewest possible".

**One-payer mode** is a special case. The payer is the only creditor, so every other member pays their own share to the payer. That makes exactly n − 1 transfers when everyone else owes something.

## Worked example

Four members, shared total CAD 800.00, so S = 80000 cents, n = 4, b = 20000, r = 0.

| Member | Paid | Share | Net |
|---|---|---|---|
| Alex | 500.00 | 200.00 | +300.00 |
| Jamie | 300.00 | 200.00 | +100.00 |
| Ben | 0.00 | 200.00 | −200.00 |
| Cindy | 0.00 | 200.00 | −200.00 |

Self-check: 300 + 100 − 200 − 200 = 0.

Ben and Cindy are tied as the largest debtors. Ben is listed first, so Ben goes first.

1. Ben → Alex: 200.00. Alex is still owed 100.00, and Ben is settled.
2. Cindy → Alex: 100.00. Alex is settled, and Cindy still owes 100.00.
3. Cindy → Jamie: 100.00. Everyone is settled.

That is three transfers, which is n − 1 = 3.

Rounding example: S = 10000 cents (CAD 100.00) split among 3 members gives b = 3333 and r = 1. The first member listed owes 33.34, and the other two owe 33.33 each. The total is exactly 100.00.
