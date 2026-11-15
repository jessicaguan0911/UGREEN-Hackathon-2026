# Trip Wrap-Up

UGREEN Hackathon 2026 · Automate Your Workflow

## 1. What does the Skill do?

It turns receipt photos snapped during a trip into a report showing exactly who pays whom, then optionally organizes the trip photos into albums.

## 2. Who is the target user and problem?

The target users are roommates and friend groups who share a UGREEN NAS. The real pain is the awkwardness: people hesitate to ask friends for money they are owed, and those who owe feel uneasy without knowing the exact amount.

## 3. What is your proposed solution?

No one wants to keep score on vacation. Members snap receipts and upload their photos to the shared NAS. Afterwards, the Skill finds receipts, asks for missing details, and saves a neutral, traceable report, so the report does the asking.

## 4. What is the Core User Flow?

1. Confirm dates, members, currency, payment mode and photo scope.
2. Find receipts and build separate daily and whole-trip place summaries.
3. Review gaps such as "Lake Louise: 87 photos, 0 confirmed receipts", unreadable receipts, duplicates, payers, personal expenses and rates.
4. Confirm and save the report, with transfers on top.
5. Optionally create albums from the same trip information.

## 5. What substantive difference does your idea offer?

A chatbot can split bills once someone has collected the inputs. Trip Wrap-Up searches authorized NAS uploads, uses photos to prompt missing-expense review, and retains each receipt's source. Unknown details require confirmation. A day or place with no receipts prompts a question, not an invented expense.

## 6. Which UGREEN AI NAS capabilities will be used, and at which step?

Photo-agent uses ug-photo search-picture for capture dates, locations and OCR text; search-screen for content and upload-time filtering; vision-ocr for eligible fallback images; and create-album for albums. Document-agent uses ug-document extract with receipt schema and dedupe. Knowledge-agent uses ug-knowledge save-text for the report.

## 7. What was your technical approach?

A Markdown-only Skill follows Uliya and delegates to three registered experts, without NAS scripts. Missing capture times use an approved upload window. Writes require platform approval. Settlement uses integer cents, fixed remainder allocation, total and balance checks, and greedy matching with at most n-1 transfers. The intended workflow uses the NAS-local model without external services.

## 8. What is the current development status?

SKILL.md and five references are written; official checks return static-pass with zero errors or warnings. A separate arithmetic model passes seven known cases and 20,000 synthetic trips. NAS installation, image extraction, search coverage, location grouping and local-model routing remain untested.

## 9. What is your final validation plan?

Core one: four members, fifteen receipts among 300 photos; expect CAD 800, three transfers and missing-expense review. Core two: one payer, USD/CAD receipts; expect CAD 100 with a rounding remainder. Edge case: duplicate, blurry and forwarded undated images must prompt review without double counting or invented values.

## 10. Are there any known limitations?

Members need NAS accounts and shared access. Equal splits and two-decimal settlement currencies only; users supply rates. Search previews, OCR and location metadata can limit coverage. Excluding receipts from albums depends on supported operations. Missing expenses can change totals.

---

UGREEN's official kit 0.7.7/catalog 2.2.0 and runtime experts are used under applicable UGREEN terms: https://ai.ugreen.com/pages/hackathon-starter-kit. No third-party libraries are bundled in the Skill, and it uses no external runtime services.

Codex helped write and review the Skill and proposal and prepare validation tools: https://openai.com/codex/, applicable OpenAI terms. Local document generation uses ReportLab 4.4.9 (BSD license, https://www.reportlab.com/), Bitstream Vera (font license, https://www.gnome.org/fonts/) and python-docx (MIT license, https://python-docx.readthedocs.io/). These are not Skill dependencies. Full tool, license and AI-use details are in the ZIP's linked references/disclosures.md.
