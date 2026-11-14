# Trip Wrap-Up: Settle Up and Relive Your Trip

**Skill name:** `trip-wrap-up` · **Track:** Open Innovation · **Entrant:** Individual

## 1. What does the Skill do?

It turns receipt photos already in the NAS photo library into a settle-up report showing exactly who pays whom, then organizes the trip photos into albums.

## 2. Who is the target user and problem?

Friends, roommates and families who travel together and keep photos on a UGREEN NAS. After a trip, receipts are buried among hundreds of photos. Someone spends an evening typing them into a spreadsheet and arguing over rounding and currency, while the photos stay unsorted.

## 3. What is your proposed solution?

One request, such as "settle up our Banff trip, Oct 3–7", finds the receipts, reads them locally, and asks only what AI cannot know: who paid, personal items, exchange rates. It computes balances with an auditable rule, saves the report, and builds trip albums.

## 4. What is the Core User Flow?

1. The user gives dates, members, currency, and whether one person paid everything.
2. The Skill lists detected receipts; the user removes false hits.
3. In a review table, the user confirms flagged values, duplicates, payers, personal receipts and rates.
4. The report is saved, with the final transfers on top.
5. Albums are proposed, confirmed and created.

## 5. What substantive difference does your idea offer?

Splitting apps need manual entry. Chatbots cannot see your photos and may guess silently. Trip Wrap-Up reads receipts where they already live and traces every number to a source photo. It never invents payers or rates, and it checks that all balances sum to zero. Money and memories are wrapped up together.

## 6. Which UGREEN AI NAS capabilities will be used, and at which step?

- **Find receipts:** photo-agent (`ug-photo` search-picture with OCR-text and capture-date filters, plus search-screen).
- **Read receipts:** document-agent (`ug-document` extract, receipt schema, dedupe), with photo-agent vision-ocr as the fallback.
- **Save the report:** knowledge-agent (`ug-knowledge` save-text).
- **Build albums:** photo-agent (location search, create-album).

## 7. What was your technical approach?

A Markdown-only Skill following the Uliya standard: SKILL.md delegates to three registered experts, with no scripts. Writes (the report and the albums) require platform approval. The settlement math uses integer cents, a fixed remainder rule, and greedy matching that needs at most n−1 transfers. It runs on the NAS local AI only, so trip data never leaves the NAS.

## 8. What is the current development status?

- **Done:** SKILL.md and two references. The official checker returns static-pass with 0 errors and 0 warnings. The settlement rule was verified on 20,000 simulated trips.
- **Pending NAS validation:** whether extract reads receipt images directly, OCR recall on real receipts, and the quality of location albums.

## 9. What is your final validation plan?

- **Core test 1:** 4 members, 15 receipts among 300 photos, claim mode. Expect every receipt found, zero-sum balances, and at most 3 transfers.
- **Core test 2:** one-payer mode with USD and CAD receipts, using a rate the user supplies.
- **Edge case:** a blurry receipt plus a duplicate photo of another receipt. Both must be flagged, never guessed or double-counted.

## 10. Are there any known limitations?

- Equal splits only; splits among part of the group are not supported yet.
- Receipts must have been photographed.
- There is no exchange-rate lookup capability, so users supply rates. In the future, the Skill could fetch the rate for the transaction date if UGREEN exposes one.
- Leaving receipts out of albums depends on photo-agent support.

---

**Third-party components and external services:** None. The Skill uses only UGREEN AI NAS capabilities and its local AI model. No data is sent outside the NAS.
