---
name: trip-wrap-up
description: Trip wrap-up for roommates and friend groups who share a NAS. Receipt photos snapped during a trip and uploaded to the shared album become a settle-up report that names exactly who pays whom and how much, with every amount traced to its source photo and a day-by-place view that reveals missing receipts, plus trip albums by place, group photos, and scenery. Use when the user says things like "split the costs from our Banff trip", "who owes whom from last month's trip", "settle up our road trip", or "wrap up our trip photos and expenses".
---

# Goal

Splitting trip costs is awkward. People hesitate to ask friends for money they are owed, and people who owe money feel uneasy without knowing the exact amount. During the trip, members only need to snap each receipt. Afterwards, this Skill lets a neutral, fully traceable report do the asking. It gives the user two results:

1. **A settle-up report.** The first section lists only the final transfers, for example "Ben → Alex: CAD 200.00". Below that come:
   - a day-by-place coverage view showing how many trip photos and receipts each place has, so missing receipts stand out;
   - one row per receipt with its source photo;
   - each member's balance;
   - the exchange rates used;
   - a zero-sum self-check, so anyone in the group can verify the result.
2. **Trip albums.** One album per recognized place, plus "Group Photos" and "Scenery" albums. They are built from the same trip index the report uses.

Supported scope:

- Every trip member has an account on the same NAS. Members upload their trip photos, including receipt photos, to the shared photo space. Each receipt needs to be photographed by at least one person, normally whoever paid.
- Shared costs are split equally among all trip members. Receipts the user marks as personal are listed but not split.
- One settlement currency. Foreign-currency receipts are converted with a rate the user provides.

Not supported in this version:

- Splits among only part of the group.
- Live exchange-rate lookup.
- Reconciliation against card statements.
- Payments, or messaging other people.

The Skill never moves money and never shares anything outside the NAS.

# Required input

Ask for these before the first delegation, in one short message:

- **Trip dates**: the first and last day, as YYYY-MM-DD. Required; stop and ask if missing.
- **Trip members**: the display names of everyone who shares costs (2 to 8 people). Required.
- **Trip name**: a short label for the albums and the report, such as "Banff 2026". If the user gives none, use the main place name and the year.
- **Settlement currency**: the single currency everyone pays back in. If the user does not say, ask. Do not assume one.
- **Payment mode**: ask "Did one person pay for everything?"
  - Yes → **one-payer mode**: record that person's name. Every other member pays their share to that person.
  - No → **claim mode**: members say which receipts they paid during the review step.

Collect the rest later, only when the workflow needs it:

- who paid each receipt (claim mode only);
- which receipts are personal;
- corrections to low-confidence values;
- exchange rates.

# Generation-time capability evidence

- `ug-photo` → `photo-agent`
- `ug-document` → `document-agent`
- `ug-knowledge` → `knowledge-agent`

# Orchestration

This is the expert orchestration workflow. Run the steps in order. Each step uses only the real results returned by the steps before it. Never pass a guessed path, ID, amount, payer, or rate downstream.

## Step 1: Build the trip index (read only)

```text
delegate --target photo-agent --instruction 'Search both the personal and the shared photo space for photos captured within the trip dates the user confirmed, using capture time. For each trip day, report the recognized places and the number of photos taken at each place. Also count photos whose content shows a group of people and photos whose content shows scenery such as mountains, lakes, or landscapes. Read only; create nothing. If no photos match the trip dates, say so explicitly.'
```

Keep the day × place counts and the place names. The report (Step 4) and the albums (Step 7) both use them. If photos have no location data, group them by day only. If photo-agent explicitly reports no trip photos, tell the user and stop. Do not widen the dates on your own.

## Step 2: Find receipt photos (read only)

```text
delegate --target photo-agent --instruction 'In both the personal and the shared photo space, find receipt photos for the trip dates the user confirmed. First search by capture time within the trip dates. Combine two searches: picture content matching receipt, and OCR text containing any of TOTAL, SUBTOTAL, GST, HST, PST, TIP, VISA, MASTERCARD, DEBIT. Then run the same two searches by upload time, from the first trip day to seven days after the last trip day, and keep only photos that have no capture time; mark these as date uncertain. Merge all results without duplicates. For each photo return the exact file path, the picture ID, the capture time if any, the recognized place if any, and whether it is date uncertain. If nothing matches, say explicitly that no receipt photos were found.'
```

- If photo-agent explicitly reports no matches, tell the user that no receipt photos were found for those dates and stop the settle-up part. Offer albums only (Step 7).
- Show the user a numbered list of what was found, with time, place, file name, and a date-uncertain mark where it applies. Ask the user to remove anything that is not a receipt and to confirm the date-uncertain photos. Continue only with the paths the user kept.

## Step 3: Read the receipts (read only)

```text
delegate --target document-agent --instruction 'Extract receipt data from exactly these image files, which the user confirmed as trip receipts: the confirmed receipt paths returned by photo-agent. Use the receipt schema with dedupe on. For each file return: merchant name, transaction date, final amount paid including tax and tip, the currency symbol or code exactly as printed, the last four card digits if printed, and the payment method if printed. Flag low-confidence values and suspected duplicates, including the same receipt photographed by two people. Report coverage and list every file that could not be read.'
```

When this step runs, replace the phrase about confirmed paths with the actual list of paths. If a required path is missing, stop and ask the user. Never rebuild a path from a file name.

Fallback for unreadable images: for each file that document-agent lists as unreadable, run one delegation per file:

```text
delegate --target photo-agent --instruction 'Run vision OCR on this single receipt image path from the confirmed trip receipt list and return the full recognized text unchanged.'
```

Read the merchant, date, total, and currency from the returned text, and mark them all as low confidence for the user to confirm. If OCR also fails, keep the receipt as "unread" and ask the user to type the amount or remove the receipt.

## Step 4: Review with the user (conversation only)

Show the receipts grouped **by day, then by place**. Next to each place, show the number of trip photos from Step 1. For example:

```text
Oct 4 · Banff town      42 photos · 3 receipts
Oct 4 · Lake Louise     87 photos · 0 receipts  ⚠️ did anyone pay for anything here?
```

For each receipt, show: merchant, amount, currency, card last four digits, low-confidence flag, duplicate flag, and source file name. Then ask, in one message:

1. **Gaps**: for every place with many photos and no receipts, ask whether anything was paid there. If yes, ask for the photo, or let the user type the amount and payer and mark it "entered by hand".
2. **Duplicates and corrections**: keep or drop each suspected duplicate. Fix any flagged amount or currency. A receipt photographed twice must count only once.
3. **Personal receipts**: "Were any of these paid by one person just for themselves?" Personal receipts stay in the report but are not split. Everything else, including shared meals, lodging, gas, and activities, is shared equally by all members.
4. **Payers (claim mode only)**: "Who paid for each receipt?" Show the card last four digits as a memory aid. Never assign a payer the user has not confirmed.
5. **Exchange rates (only if more than one currency appears)**: for each foreign currency, ask "1 [foreign currency] = ? [settlement currency]". Suggest the rate on the card statement, because that is what was actually charged on the transaction date. Never invent or estimate a rate.

Do not compute anything until every shared receipt has a confirmed amount, currency, and payer.

## Step 5: Settle up (computed by the parent)

Follow [settlement math](references/settlement-math.md) exactly:

- convert currencies;
- compute each member's share and balance in integer cents;
- assign the rounding remainder by member order;
- check that the balances sum to zero;
- generate transfers by greedy matching, which needs at most one fewer transfer than the number of members.

In one-payer mode, every other member pays their share directly to the payer. If the zero-sum check fails, stop and report the mismatch instead of saving a report.

## Step 6: Save the report (write; requires approval)

Build the report from the [report template](references/report-template.md), then:

```text
delegate --target knowledge-agent --instruction 'Save this Markdown settle-up report as a new text file in the shared space of the NAS, so every trip member can open it, with the filename hint trip-wrap-up followed by the trip name and start date. Save it to the folder the user named; if the user named none, ask the user where to save it. Return the verified output file path.'
```

When this step runs, include the full report text as the content. Tell the user the verified file path only after save-text confirms it.

## Step 7: Build trip albums (write; requires approval)

Propose albums from the Step 1 index:

- one album per place, named with the trip name and the place, for example "Banff 2026 · Lake Louise";
- "Banff 2026 · Group Photos";
- "Banff 2026 · Scenery".

Leave out any proposed album with zero photos. Ask the user to confirm the names, then:

```text
delegate --target photo-agent --instruction 'Create these regular albums from photos captured within the trip dates the user confirmed, one search per album: the place albums by recognized location, the Group Photos album by picture content showing a group of people, and the Scenery album by picture content showing landscapes. Leave out the picture IDs the user confirmed as receipts. If receipt photos cannot be left out of a search result, report which albums would include them and wait for the user to decide. Return each created album name, album ID, and photo count.'
```

When this step runs, replace the album list with the names the user confirmed and the receipt picture IDs from Step 2.

# Completion and failure

Treat every delegation result by its public status:

- **completed**: continue only if the result contains the real facts the next step needs: paths, picture IDs, place counts, amounts, the saved file path, or album IDs. If a needed value is missing, say the step finished but its result cannot be verified, and stop the steps that depend on it.
- **failed**: stop the dependent steps. Tell the user which step failed and which expert ran it, and keep every confirmed result. For example, if album creation fails, the saved report is still valid.
- **cancelled**: report the step as not done. Do not retry automatically, because a retry could create a duplicate report file or album. Ask the user first.
- **waiting_user**: wait for the user's answer and let the same delegation resume. Do not start a parallel copy.
- **waiting_approval**: wait for platform approval. Approval given in the conversation does not replace it. After resuming, check the final status before reporting success.

Empty results:

- **No trip photos or no receipt photos found**: say so and stop the dependent part. Do not widen the search.
- **No recognized places**: group by day only, create only the Group Photos and Scenery albums, and say why no place albums were made.
- **Zero photos for a proposed album**: do not create that album.

Partial completion: end with a short summary that lists the steps completed, the steps failed or cancelled, and the steps still waiting. For example: "Report saved; two of three albums created; Scenery album failed."

Never invent receipts, amounts, payers, exchange rates, file paths, or album contents. Never claim that transfers were paid. The Skill only tells people what to pay.
