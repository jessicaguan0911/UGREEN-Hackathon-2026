# Trip Wrap-Up

UGREEN Hackathon 2026 · Automate Your Workflow

Submitted by: Jiayi Guan

## 1. Skill purpose

Receipt photos become a report showing exactly who pays whom, with optional trip albums.

## 2. Users and problem

Roommates and friends sharing a NAS hesitate to ask for repayment. Those who owe also feel uneasy without a clear amount. After trips, reconstructing expenses from banking screenshots takes time and invites mistakes. Those who owe may forget while waiting for the final calculation.

## 3. Proposed solution

No one wants to keep score on vacation. Members photograph receipts and upload trip photos. Afterwards, the Skill finds candidates, requests missing details and saves a neutral, traceable report, so the report does the asking.

## 4. User flow

1. Confirm dates, members, currency, payment mode and photo scope.
2. Find receipts; review daily and whole-trip place summaries.
3. Confirm gaps, duplicates, unreadable receipts, payers, personal expenses and rates.
4. Save the confirmed report with transfers first.
5. Optionally create albums.

## 5. What makes it different?

A chatbot needs someone to collect its inputs. This Skill searches authorized NAS uploads and uses photos to prompt missing-expense review. Every receipt retains its source. Unknown details require confirmation. If day three has photos but no confirmed receipts, it asks whether anyone spent money that day.

## 6. NAS capabilities

Photo-agent uses ug-photo search-picture for capture dates, locations and OCR text; search-screen for content and upload dates; vision-ocr for eligible fallbacks; create-album for albums. Document-agent extracts receipts through ug-document; knowledge-agent saves reports through ug-knowledge.

## 7. Technical approach

The Markdown Skill follows Uliya and delegates to three experts without NAS scripts. Writes require approval. Settlement uses integer cents, fixed rounding, balance checks and at most n-1 transfers. The intended local-model workflow uses no external services. Photos missing capture dates use an approved upload window and need user confirmation before joining the trip. Checks reconcile ledger totals, paid amounts, shares and balances after transfers.

## 8. Development status

SKILL.md and six references are written. Official checks pass with zero errors or warnings. A separate arithmetic model passes seven known cases and 20,000 synthetic trips. NAS execution, extraction, search coverage and model routing remain untested.

## 9. Validation plan

Core one: four members, fifteen receipts among 300 photos; expect CAD 800 and three transfers. Core two: one payer, USD/CAD receipts; expect CAD 100 with rounding. Edge case: duplicate, blurry and undated images must prompt review.

## 10. Known limitations

Members need NAS accounts and shared access. Equal splits and two-decimal settlement currencies only; users supply rates. Search previews, OCR and location metadata limit coverage. Album receipt exclusion needs device testing.

---

UGREEN kit 0.7.7/catalog 2.2.0 and experts: https://ai.ugreen.com/pages/hackathon-starter-kit (UGREEN terms). No bundled libraries or external runtime services.

Codex assisted drafting, review and validation; OpenAI image generation created covers: https://openai.com/ (OpenAI terms). Document tools: ReportLab (BSD, https://www.reportlab.com/), python-docx (MIT, https://python-docx.readthedocs.io/), Bitstream Vera (font license, https://www.gnome.org/fonts/). Full disclosure: references/disclosures.md.
