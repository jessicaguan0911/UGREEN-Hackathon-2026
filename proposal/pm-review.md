# PM review: decisions log

These are the answers to the 30 critical PM questions. Each decision will be applied to SKILL.md and the proposal once the review is finished.

## Q6: Receipts spread across several phones
- **Decision:** for every receipt, at least one person takes a photo; whoever paid takes it. After the trip, everyone uploads their photos to the NAS shared album.
- **SKILL.md changes:**
  - Step 1 searches both the personal and the shared space.
  - Duplicate receipts become a core check: the same receipt photographed twice must be flagged and confirmed by the user.
- **User guide tip:** agree on the rule before the trip. Friends without NAS accounts send their photos to the NAS owner, who uploads them.

## Q6b: Capture time lost when photos are forwarded through chat apps
- **Decision:**
  - Main rule: upload original photos through the NAS app, which keeps the capture time.
  - Fallback: also search by upload time, from the first trip day to one week after the trip. Mark photos that have no capture time as "date uncertain" and ask the user to confirm them.

## Q14: A missed receipt silently breaks the totals
- **Decision:** list receipts by day and by place, next to the number of trip photos taken at that place on that day. Example: "Oct 4 · Lake Louise: 87 photos, 0 receipts ⚠️". The photos act as the memory checklist that users do not have.
- **Fallback:** if photos have no location data, group by day only.
- **Future plan:** reconcile against a credit-card statement PDF that the user downloads and saves to the NAS. No bank connection is needed.
- **Pitch value:** only the NAS holds both the photos and the receipts, which strengthens the answer to Q21 ("why not ChatGPT?").

## Q18: Is the album feature just filler?
- **Decision:** keep the albums (option A). Money and memories together tell the complete "trip wrap-up" story.
- **Framing to avoid looking stapled on:** the Skill builds one day × place index of the trip. It serves two purposes:
  1. Spotting missing receipts (Q14).
  2. Creating the albums.
- One engine produces two outputs, so the albums reuse the work the settle-up already needs.

## Q19: Receipts leaking into the albums
- **Decision:** option B. If photo-agent cannot leave receipt photos out of an album, stop and ask the user, for example: "The Lake Louise album would include 3 receipts. Create it anyway?"
- **Status:** SKILL.md Step 6 already does this. No change needed.

## Q21: Why not just use ChatGPT?
- **Headline:** "ChatGPT can do the math once you've done the work. Trip Wrap-Up does the work."
- **Supporting points:**
  1. Finding the receipts: they are scattered across 300 photos and four phones, and the NAS finds them in the shared album.
  2. Photos as reminders: "87 photos at Lake Louise, 0 receipts" can only be noticed by a NAS that holds both.
  3. Traceability: every amount links to its source photo, and balances pass a zero-sum check.
  4. Privacy: receipts with card digits never leave home.
  5. Albums come free: the same day × place index builds the trip albums.
- **PDF:** lead Q5 with the headline, then compress the points into one sentence.

## Q23: Where does the Finalist test data come from?
- **Decision:** options A and B.
  - Use the entrant's own real trip photos, only on the test NAS. Mask card digits and other personal details in the demo video.
  - Start collecting a small "test trip" now: receipts plus photos taken at the same places, including at least one duplicate receipt photo and one blurry receipt for the edge case.
- **Follow-ups:**
  - Friends who appear in photos must agree to be shown in the public video.
  - Upload all test data at the very start of the testing day, so that photo indexing (faces, places, OCR) has time to finish.

## Q1: Is the pain real?
- **Answer:** yes, from the entrant's own experience and from friends. The real pain is social, not arithmetic:
  - People hesitate to ask friends for money they are owed.
  - People who owe money feel uneasy because they cannot easily work out the exact amount.
- **Repositioning:** "The report does the asking, so friends don't have to." A neutral, fully traceable report removes the awkwardness.
- **PDF Q2 draft:** "The real pain isn't the math. It's the awkwardness: people hesitate to ask friends for money they're owed, and those who owe feel uneasy without knowing the exact amount."
- **Rejected:** a ready-to-send group-chat message in the report. The entrant declined it.

## Q2 and Q3: Who is the real user?
- **Decision:** B and C.
  - **B:** roommates or housemates who share one NAS. Everyone has an account, uploads to the shared album, and can open the report.
  - **C:** friend groups where one person owns the NAS. Friends send their photos to the owner, who uploads them. The owner shares the report with the group manually, for example with a screenshot. The Skill itself never shares anything.
- **Out of scope:** families. "Families don't split bills."
- **Q3 (overlap between NAS owners and people who split trip costs):** answered by this. The target is NAS owners who live or travel with peers, not households of parents and children.
- **Update (assumption):** every trip member has an account on the same NAS. The owner creates accounts for friends if needed. Everyone uploads to the shared album and can open the saved report on the NAS, so no screenshots are needed. List this assumption under Known limitations.
