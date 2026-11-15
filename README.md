# Trip Wrap-Up

A Skill for settling shared trip expenses on UGREEN AI NAS.

During a trip, everyone takes photos of their receipts and uploads them with the other trip photos. Back home, Trip Wrap-Up finds the receipts, asks who paid, and prepares a report showing who owes whom.

Before calculating, it checks expenses in two ways: by day, and by place across the whole trip. If there are photos from the third day but no confirmed receipts, it asks whether anyone spent money that day. The same check works for a place the group visited. This helps people remember missing expenses without having to recall every purchase. Albums can be created afterwards from the same dates and places.

## Files

The latest version is 0.2.1:

- [Skill ZIP](proposal/releases/v0.2.1/trip-wrap-up-v0.2.1.zip)
- [Proposal PDF](proposal/releases/v0.2.1/trip-wrap-up-proposal-v0.2.1-review.pdf), [Word copy](proposal/releases/v0.2.1/trip-wrap-up-proposal.docx) and [editable text](proposal/proposal-v0.2.1-review.md)
- [Review against the judging criteria, in Chinese](proposal/criteria-review.md)

The ZIP contains `SKILL.md` and six Markdown references, including a [usage README](trip-wrap-up/references/README.md). The [AI and dependency disclosure](trip-wrap-up/references/disclosures.md) is included in the package. Original proposal files and earlier releases remain in `proposal/`.

## Current limits and checks

The Skill supports 2–8 people, equal shares, and a settlement currency with two decimal places. Everyone needs a NAS account and access to the shared content. Exchange rates and payers are confirmed by the user. No payments are made.

Official kit 0.7.7, catalog 2.2.0, returns `static-pass` with no errors or warnings. A separate arithmetic model passes seven known examples and 20,000 synthetic trips. The ten proposal answers total fewer than 500 words. Results, file sizes and hashes are in [the release folder](proposal/releases/v0.2.1/).

The Skill has not yet run on a NAS. Image extraction, receipt discovery, location metadata, local-model settings and album behavior still need device testing. The [test plan](trip-wrap-up/references/validation-plan.md) gives the expected results and cases to check.

## Local development

The scripts in `tools/` run on the development machine and stay outside the Skill ZIP. They require Python, Node.js, ReportLab, python-docx and the official UGREEN kit.

```text
python tools/verify_settlement.py
python tools/build_release.py --kit /path/to/uliya-skill-kit --version 0.2.1
```

Build into a new version directory. The builder preserves existing releases rather than overwriting them. Updating the repository does not submit an entry to Devpost or publish the Skill to Skills Hub.
