#!/usr/bin/env python3
"""Verify an exact-arithmetic model; this does NOT run the Markdown Skill on NAS."""
import json
from fractions import Fraction
from random import Random


def cents(amount, rate='1'):
    exact = Fraction(str(amount)) * Fraction(str(rate)) * 100
    if exact < 0 or Fraction(str(rate)) <= 0:
        raise ValueError('negative expenses or nonpositive rates are unsupported')
    return (2 * exact.numerator + exact.denominator) // (2 * exact.denominator)


def settle(paid):
    if not 2 <= len(paid) <= 8 or any(type(x) is not int or x < 0 for x in paid):
        raise ValueError('2..8 members with nonnegative integer-cent paid amounts required')
    n, total = len(paid), sum(paid)
    base, remainder = divmod(total, n)
    shares = [base + int(i < remainder) for i in range(n)]
    original = [p - s for p, s in zip(paid, shares)]
    residual, transfers = original.copy(), []
    while any(x < 0 for x in residual):
        debtor = min(range(n), key=lambda i: (residual[i], i))
        creditor = min(range(n), key=lambda i: (-residual[i], i))
        amount = min(-residual[debtor], residual[creditor])
        transfers.append([debtor, creditor, amount])
        residual[debtor] += amount
        residual[creditor] -= amount
    return shares, original, transfers


def check(paid, expected_shares=None, expected_transfers=None):
    shares, net, transfers = settle(paid)
    assert sum(paid) == sum(shares) and sum(net) == 0
    ideal = Fraction(sum(paid), len(paid))
    assert all(abs(Fraction(s) - ideal) < 1 for s in shares)
    assert max(shares) - min(shares) <= 1
    assert shares == sorted(shares, reverse=True)
    assert len(transfers) <= len(paid) - 1
    # Independent per-member cash-flow accounting, applied to original liabilities.
    incoming, outgoing = [0] * len(paid), [0] * len(paid)
    for debtor, creditor, amount in transfers:
        assert debtor != creditor and type(amount) is int and amount > 0
        assert net[debtor] < 0 and net[creditor] > 0
        outgoing[debtor] += amount
        incoming[creditor] += amount
    for i in range(len(paid)):
        assert paid[i] + outgoing[i] - incoming[i] == shares[i]
    if expected_shares is not None:
        assert shares == expected_shares, (shares, expected_shares)
    if expected_transfers is not None:
        assert transfers == expected_transfers, (transfers, expected_transfers)


def verify():
    alex = [120, 80, 100, 150, 50]
    jamie = [60, 40, 75, 25, 20, 15, 10, 5, 30, 20]
    assert len(alex) + len(jamie) == 15 and 42 + 87 + 171 == 300
    check([sum(alex) * 100, sum(jamie) * 100, 0, 0], [20000] * 4,
          [[2, 0, 20000], [3, 0, 10000], [3, 1, 10000]])
    mixed = cents('10.00', '1.35') + cents('86.50')
    assert mixed == 10000
    check([mixed, 0, 0], [3334, 3333, 3333], [[1, 0, 3333], [2, 0, 3333]])
    foreign_only = cents('30.00', '1.35')
    assert foreign_only == 4050
    check([foreign_only, 0, 0], [1350] * 3, [[1, 0, 1350], [2, 0, 1350]])
    half_up = cents('0.01', '1.50')
    assert half_up == 2
    check([half_up, 0, 0], [1, 1, 0], [[1, 0, 1]])
    check([0, 0, 0, 0], [0] * 4, [])
    check([1, 0, 0], [1, 0, 0], [])
    # Conversion is per receipt: two half-cent ties round to four cents, not three.
    assert cents('0.01', '1.50') + cents('0.01', '1.50') == 4
    assert cents('0.02', '1.50') == 3
    check([0, 4, 0], [2, 1, 1], [[0, 1, 2], [2, 1, 1]])
    for amount, rate in [('-1', '1'), ('1', '0'), ('1', '-1')]:
        try:
            cents(amount, rate)
        except ValueError:
            pass
        else:
            raise AssertionError('unsupported expense/rate accepted')
    for paid in [[1], [0] * 9, [-1, 1], [1.0, 1]]:
        try:
            settle(paid)
        except ValueError:
            pass
        else:
            raise AssertionError('unsupported member/paid input accepted')
    rng = Random(20261115)
    rates = ['1', '1.35', '1.50', '0.825', '0.01']
    random_cases = 20000
    for _ in range(random_cases):
        paid = [0] * rng.randint(2, 8)
        for _ in range(rng.randint(0, 60)):
            original_cents = rng.randint(0, 1000000)
            amount = f'{original_cents // 100}.{original_cents % 100:02d}'
            paid[rng.randrange(len(paid))] += cents(amount, rng.choice(rates))
        check(paid)
    return {
        'status': 'pass',
        'scope': 'exact-arithmetic model only; not NAS or LLM runtime validation',
        'golden_settlement_cases': 7,
        'conversion_rounding_checks': 'pass',
        'unsupported_input_checks': 'pass',
        'random_trips': random_cases,
        'seed': 20261115,
        'invariants': ['ledger/paid/share conservation', 'equal shares within one cent',
                       'fixed remainder order', 'per-member cash-flow settlement',
                       'positive non-self integer-cent transfers', 'at most n-1 transfers'],
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
