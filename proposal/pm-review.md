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
