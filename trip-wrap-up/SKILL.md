---
name: trip-wrap-up
description: Group-trip wrap-up from photos already on the NAS. Receipt photos hidden among trip pictures become a settle-up report that names exactly who pays whom and how much, with every amount traced to its source photo, plus trip albums by place, group photos, and scenery. Use when the user says things like "split the costs from our Banff trip", "who owes whom from last month's trip", "settle up our road trip", or "wrap up our trip photos and expenses".
---

# Goal

After a trip with friends or family, give the user two results with as little typing as possible:

1. **A settle-up report.** The first section lists only the final transfers, for example "Ben → Alex: CAD 200.00". Below it, the report shows one row per receipt with its source photo path, each person's balance, the exchange rates used, and a zero-sum self-check, so anyone in the group can verify the result.
2. **Trip albums.** One album per recognized place, one "Group Photos" album, and one "Scenery" album.

Supported scope:

- Receipts that were photographed and stored in the NAS photo library during the trip dates.
- Shared costs split equally among all trip members. Receipts the user marks as personal are listed but left out of the split.
- One settlement currency. Foreign-currency receipts are converted with a rate the user provides.

Not supported in this version: splits among only part of the group, live exchange-rate lookup, and payment or messaging to other people. The Skill never sends money and never shares anything outside the NAS.

# Required input

Ask for these before the first delegation, in one short message:

- **Trip dates**: the first and last day as YYYY-MM-DD. Required; stop and ask if missing.
- **Trip members**: the display names of everyone who shares costs (2 to 8 people). Required.
- **Trip name**: a short label for albums and the report, such as "Banff 2026". If the user gives none, use the main place name and year.
- **Settlement currency**: the single currency everyone will pay back in. If the user does not say, ask; do not assume one.
- **Payment mode**: ask "Did one person pay for everything?"
  - Yes → **one-payer mode**: record that person's name; every other member pays their share to that person.
  - No → **claim mode**: members claim the receipts they paid for during the review step.

The following are collected later, only when the workflow needs them: who paid each receipt (claim mode), which receipts are personal, corrections to low-confidence values, and exchange rates.

# Generation-time capability evidence

- `ug-photo` → `photo-agent`
- `ug-document` → `document-agent`
- `ug-knowledge` → `knowledge-agent`

# Orchestration

This is the expert orchestration workflow. Run the steps in order. Each step uses only the real results returned by the step before it. Never pass a guessed path, ID, amount, payer, or rate downstream.

## Step 1: Find receipt photos (read only)

```text
delegate --target photo-agent --instruction 'Find receipt photos in the photo library whose capture time falls within the trip dates the user confirmed. Use capture time, not upload time. Combine two searches: recognized picture content matching receipt, and OCR text containing any of TOTAL, SUBTOTAL, GST, HST, PST, TIP, VISA, MASTERCARD, DEBIT. Merge the results without duplicates. For each photo return the exact file path, the picture ID, and the capture time. If nothing matches, say explicitly that no receipt photos were found in that date range.'
```

- If photo-agent explicitly reports no matches, tell the user no receipt photos were found for those dates and stop the settle-up part. Offer to continue with albums only (Step 6). Do not widen the dates or search elsewhere on your own.
- Show the user a numbered list of what was found (capture time and file name) and ask them to remove anything that is not a receipt. Continue with only the paths the user kept.

## Step 2: Read the receipts (read only)

```text
delegate --target document-agent --instruction 'Extract receipt data from exactly these image files, which the user confirmed as trip receipts: the confirmed paths returned by photo-agent in Step 1. Use the receipt schema with dedupe on. For each file return: merchant name, transaction date, final amount paid including tax and tip, the currency symbol or code exactly as printed, the last four card digits if printed, and the payment method if printed. Flag low-confidence values and suspected duplicate receipts. Report coverage and list every file that could not be read.'
```

When this step runs, replace the phrase about confirmed paths with the actual list of paths. If a required path is missing, stop and ask the user; never rebuild a path from a file name.

Fallback for unreadable images: for each file that document-agent lists as unreadable, run one delegation per file:

```text
delegate --target photo-agent --instruction 'Run vision OCR on this single receipt image path from the confirmed trip receipt list and return the full recognized text unchanged.'
```

Read the merchant, date, total, and currency from the returned text and mark all of them as low confidence for the user to confirm. If OCR also fails, keep the receipt in the table as "unread" and ask the user to type the amount or remove the receipt.

## Step 3: Review with the user (conversation only)

Show one table: number, merchant, date, amount, currency, card last four digits, low-confidence flag, duplicate flag, and source file name. Then ask, in one message:

1. **Corrections**: fix any flagged amount or currency, and keep or drop each suspected duplicate.
2. **Personal receipts**: "Were any of these paid by one person just for themselves?" Personal receipts stay in the report but are left out of the split. Everything else, including shared meals, lodging, gas, and activities, is shared equally by all members.
3. **Payers (claim mode only)**: "Who paid for each receipt?" Show the card last four digits as a memory aid. Ask once whether the group wants to match card digits to names. Never assign a payer the user has not confirmed.
4. **Exchange rates (only if more than one currency appears)**: for each foreign currency, ask "1 [foreign currency] = ? [settlement currency]". Suggest the rate shown on the card statement, because that is what was actually charged on the transaction date. Record each rate in the report. Never invent or estimate a rate.

Do not compute anything until every shared receipt has a confirmed amount, currency, and payer.

## Step 4: Settle up (computed by the parent)

Follow [settlement math](references/settlement-math.md) exactly: convert currencies, compute each member's share and balance, round to cents with a fixed remainder rule, check that balances sum to zero, and generate transfers with the greedy matching rule, which needs at most one fewer transfer than the number of members. In one-payer mode, every other member pays their share directly to the payer.

If the zero-sum check fails, stop. Report the mismatch to the user instead of saving the report.

## Step 5: Save the report (write; requires approval)

Build the report from [report template](references/report-template.md), then:

```text
delegate --target knowledge-agent --instruction 'Save this Markdown settle-up report as a new text file on the NAS with the filename hint trip-wrap-up followed by the trip name and start date. Save it to the folder the user named; if the user named none, ask the user where to save it. Return the verified output file path.'
```

When this step runs, include the full report text as the content. Tell the user the verified file path only after save-text confirms it.

## Step 6: Build trip albums (write; requires approval)

```text
delegate --target photo-agent --instruction 'For photos captured within the trip dates the user confirmed, report which recognized places they were taken at and how many photos each place has. Also count photos whose content shows a group of people and photos whose content shows scenery such as mountains, lakes, or landscapes. Read only; create nothing yet.'
```

Show the proposed albums to the user: one per place, named with the trip name and the place (for example "Banff 2026 · Lake Louise"), plus "Banff 2026 · Group Photos" and "Banff 2026 · Scenery". Ask the user to confirm the names. Then:

```text
delegate --target photo-agent --instruction 'Create these regular albums from photos captured within the trip dates the user confirmed, one search per album: the place albums by recognized location, the Group Photos album by picture content showing a group of people, and the Scenery album by picture content showing landscapes. Leave out the picture IDs the user confirmed as receipts. If receipt photos cannot be left out of a search result, report which albums would include them and wait for the user to decide. Return each created album name, album ID, and photo count.'
```

When this step runs, replace the album list with the names the user confirmed and the receipt picture IDs from Step 1.

# Completion and failure

Treat every delegation result by its public status:

- **completed**: continue only if the result contains the real facts the next step needs (paths, picture IDs, amounts, the saved file path, album IDs). If a needed value is missing, say the step finished but its result cannot be verified, and stop the steps that depend on it.
- **failed**: stop the dependent steps. Tell the user which step failed and which expert ran it, and keep every result already confirmed. Example: if album creation fails, the saved report is still valid.
- **cancelled**: report the step as not done. Do not retry automatically, because a retry could create a duplicate report file or album. Ask the user first.
- **waiting_user**: wait for the user's answer and let the same delegation resume. Do not start a parallel copy.
- **waiting_approval**: wait for platform approval. Approval in the conversation is not a substitute. After resuming, check the final status before reporting success.

Empty results:

- **No receipt photos found**: say so and stop the settle-up part.
- **No recognized places**: create only the Group Photos and Scenery albums, and say why no place albums were made.
- **Zero photos for a proposed album**: do not create that album.

Partial completion: end with a short summary that lists the steps completed, the steps failed or cancelled, and the steps still waiting. For example: "Report saved; two of three albums created; Scenery album failed."

Never invent receipts, amounts, payers, exchange rates, file paths, or album contents. Never claim the transfers were paid; the Skill only tells people what to pay.
