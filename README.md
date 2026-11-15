# UGREEN Hackathon 2026: Trip Wrap-Up

`trip-wrap-up` is an AI Skill for UGREEN AI NAS. It turns the receipt photos in a group's trip pictures into a settle-up report that says exactly who pays whom, and it organizes the trip photos into albums by place, group photos, and scenery.

## Repository layout

```text
trip-wrap-up/                     The Skill package: zip this folder for submission
├── SKILL.md                      Required entry point (Uliya Skill Development Standard)
└── references/
    ├── settlement-math.md        Integer-cent split, remainder rule, greedy transfers
    └── report-template.md        Layout of the saved settle-up report
proposal/
├── proposal.md                   Source of the Round 1 PDF (10 answers, under 500 words)
├── trip-wrap-up-proposal.pdf     Round 1 PDF
└── trip-wrap-up.zip              Round 1 Initial Skill Package
```

Only `SKILL.md` and `references/*.md` belong in the Skill ZIP. The proposal files stay outside the package.

## Checks

- Official UGOS Skill Creation Tool checker (kit v0.7.7, catalog 2.2.0): `static-pass`, with 0 errors and 0 warnings (re-run after the PM-review update).
- The settlement rule was simulated on 20,000 random trips. Balances always summed to zero, and no trip needed more than n − 1 transfers.

A static pass does not prove the Skill runs on a NAS. Runtime validation is planned for the Finalist testing day.
