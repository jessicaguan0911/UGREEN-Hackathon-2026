# UGREEN Hackathon 2026: Trip Wrap-Up

Trip Wrap-Up is a Round 1 AI Skill for roommates and friend groups sharing a UGREEN NAS. It finds candidate receipt photos, uses trip-photo activity to prompt missing-expense review, and saves a source-traceable who-pays-whom report. Optional albums reuse the same confirmed dates and places.

**Status:** Markdown orchestration implemented; actual NAS execution is not yet validated. Equal shares only, 2–8 members, a two-decimal settlement currency and user-confirmed exchange rates. Search completeness, image extraction and album receipt exclusion have explicit limitations and fallbacks.

## Version 0.2.0 review release

- [Skill ZIP](proposal/releases/v0.2.0/trip-wrap-up-v0.2.0.zip)
- [Technical proposal PDF for entrant review](proposal/releases/v0.2.0/trip-wrap-up-proposal-v0.2.0-review.pdf) and [editable source](proposal/proposal-v0.2.0-review.md)
- [Review against the four judging criteria, in Chinese](proposal/criteria-review.md)
- [Official static-check evidence](proposal/releases/v0.2.0/static-check.json)
- [Exact-arithmetic model checks](proposal/releases/v0.2.0/math-check.json)
- [Package limits, hashes and proposal word count](proposal/releases/v0.2.0/package-check.json)

Original Round 1 PDF/ZIP and source remain in `proposal/`; they have not been overwritten. The revised PDF is a technical review draft for the entrant to check in their own submission process. No Devpost submission or Skills Hub publication has been performed.

## Package contents

```text
trip-wrap-up/
├── SKILL.md
└── references/
    ├── capability-boundaries.md
    ├── disclosures.md
    ├── report-template.md
    ├── settlement-math.md
    └── validation-plan.md
```

Every reference is directly linked from SKILL.md. Only these six Markdown files belong in the Skill ZIP. Proposals, local tools, test evidence and the official developer kit stay outside it. AI usage, sources, licenses and the functionality developed for the Hackathon are disclosed in [disclosures.md](trip-wrap-up/references/disclosures.md).

## Validation and reproducibility

Using official kit **0.7.7**, catalog **2.2.0**, the v0.2.0 Skill returns **static-pass**, with **0 errors and 0 warnings**. Seven golden settlement cases and 20,000 seeded synthetic trips pass an exact-arithmetic model's conservation, rounding and cash-flow checks. These results do not validate LLM arithmetic, OCR, installation or NAS execution.

The proposal's ten substantive responses contain **371 whitespace-delimited words**. Dependencies and license information are separately disclosed. Both compressed and uncompressed Skill sizes, per-file limits and ZIP/source equality are recorded in package-check.json.

Local development only:

```text
python tools/verify_settlement.py
python tools/build_release.py --kit /absolute/path/to/uliya-skill-kit
```

The release builder requires the official kit, Node.js, Python and local ReportLab; these are not Skill runtime dependencies. It refuses to overwrite an existing v0.2.0 release. Build only into a fresh version location; preserve any already submitted materials.

The [NAS validation plan](trip-wrap-up/references/validation-plan.md) supplies expected financial results, preview-overflow and single-foreign-currency regressions, interrupted-write/repeat-use checks, setup and safe-removal boundaries. Finalists must collect actual target-device evidence during their assigned testing day.
