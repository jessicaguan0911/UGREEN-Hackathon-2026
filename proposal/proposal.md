# Trip Wrap-Up: Settle Up and Relive Your Trip

**Skill name:** `trip-wrap-up` · **Track:** Open Innovation · **Entrant:** Individual

## 1. What does the Skill do?

It turns receipt photos snapped during a trip into a settle-up report showing exactly who pays whom, then organizes the trip photos into albums.

## 2. Who is the target user and problem?

The target users are roommates and friend groups who share a UGREEN NAS. The real pain isn't the math; it's the awkwardness. People hesitate to ask friends for money they're owed, and those who owe feel uneasy without knowing the exact amount.

## 3. What is your proposed solution?

No one wants to keep score on vacation. Members only snap each receipt and upload their photos to the shared album. Afterwards, one request finds the receipts, reads them locally, asks only what AI cannot know, and saves a neutral, traceable report, so the report does the asking.

## 4. What is the Core User Flow?

1. The user gives dates, members, currency, and the payment mode.
2. The Skill builds a day × place index of the trip photos and finds the receipts.
3. A review table flags gaps such as "Lake Louise: 87 photos, 0 receipts", along with duplicates, payers, personal items and rates.
4. The report is saved, with the final transfers on top.
5. Albums are created from the same index.

## 5. What substantive difference does your idea offer?

ChatGPT can do the math once you've done the work. Trip Wrap-Up does the work: it finds receipts across everyone's uploads, uses photos as reminders for missing receipts, and traces every amount to its source photo. It never guesses, and its data never leaves home.

## 6. Which UGREEN AI NAS capabilities will be used, and at which step?

- **Trip index and receipt search:** photo-agent (`ug-photo` search-picture by capture time, upload time, location and OCR text, plus search-screen).
- **Read receipts:** document-agent (`ug-document` extract, receipt schema, dedupe), with vision-ocr as the fallback.
- **Save the report:** knowledge-agent (`ug-knowledge` save-text).
- **Albums:** photo-agent (create-album).

## 7. What was your technical approach?

A Markdown-only Skill following the Uliya standard: SKILL.md delegates to three registered experts, with no scripts. Photos without a capture time fall back to an upload-time window and are marked for the user to confirm. Writes require platform approval. The settlement uses integer cents, a fixed remainder rule, a zero-sum check, and greedy matching that needs at most n−1 transfers. Everything runs locally.

## 8. What is the current development status?

- **Done:** SKILL.md and two references. The official checker returns static-pass with 0 errors and 0 warnings. The settlement rule was verified on 20,000 simulated trips.
- **Pending NAS validation:** whether extract reads images directly, OCR recall, and location grouping.

## 9. What is your final validation plan?

- **Core test 1:** 4 members, 15 receipts among 300 shared-album photos, claim mode. Expect every receipt found, zero-sum balances, and at most 3 transfers.
- **Core test 2:** one-payer mode with USD and CAD receipts.
- **Edge case:** a duplicate receipt, a blurry receipt, and a forwarded photo with no capture time. All three must be flagged.

## 10. Are there any known limitations?

- Every member must have an account on the same NAS.
- Equal splits only.
- Users supply exchange rates; automatic rates and card-statement reconciliation are future work.
- Excluding receipts from albums depends on photo-agent support.

---

**Third-party components and external services:** None. The Skill uses only UGREEN AI NAS capabilities and its local AI model. No data is sent outside the NAS.
