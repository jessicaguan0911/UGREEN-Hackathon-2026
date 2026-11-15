# Validation plan

These are planned device cases, not NAS test results. Local checks verify a mathematical model, not LLM arithmetic, OCR recall, installation or expert execution. Keep a synthetic/anonymized ground-truth fixture manifest outside the submission ZIP.

## Core case 1: claim mode, 15 receipts in 300 photos

Members in order: Alex, Jamie, Ben, Cindy. CAD settlement; dates 2026-10-04 through 2026-10-05, America/Edmonton. Prepare 15 synthetic receipt images and 285 authorized scenery/group images, total 300. Alex's five receipts: CAD 120, 80, 100, 150, 50. Jamie's ten: CAD 60, 40, 75, 25, 20, 15, 10, 5, 30, 20. All shared. Ben and Cindy paid zero.

Activity ground truth: Oct 4 Banff has 42 photos including Alex's five receipts; Oct 4 Lake Louise has 87 photos, zero receipts; Oct 5 Banff has 171 photos including Jamie's ten receipts. Use actual supported metadata/classification; document day-only fallback if locations cannot be established. The user confirms Lake Louise was a free hike.

| Member | Paid CAD | Share CAD | Net CAD |
|---|---:|---:|---:|
| Alex | 500.00 | 200.00 | +300.00 |
| Jamie | 300.00 | 200.00 | +100.00 |
| Ben | 0.00 | 200.00 | -200.00 |
| Cindy | 0.00 | 200.00 | -200.00 |

Ordered transfers: Ben -> Alex 200.00; Cindy -> Alex 100.00; Cindy -> Jamie 100.00. Compare actual detection against all 15 unique receipts, recording misses and false positives. Verify saved path/read-back and actual album IDs/counts if albums are requested. Zero-sum does not establish complete receipt discovery.

## Core case 2: one payer, mixed currencies and remainder

Members Alex, Jamie, Ben, in that order. Alex paid USD 10.00 at confirmed 1.35 CAD/USD plus CAD 86.50. Converted amounts 13.50 and 86.50; total CAD 100.00. Shares: Alex 33.34, Jamie 33.33, Ben 33.33. Transfers: Jamie -> Alex 33.33; Ben -> Alex 33.33. Retain originals, rate and remainder in the report.

Single-foreign regression: only USD 30.00 with CAD settlement and the same members/rate. Still ask for the rate. Total CAD 40.50; shares 13.50; Jamie and Ben each pay Alex 13.50.

## Combined edge case and recovery

Add a second photo of an existing receipt, an unreadable receipt and an unrelated forwarded image missing capture time. Two picture IDs for one transaction must not be charged twice; ask which to keep. Unreadable fields cannot become zero. OCR fallback requires an attachment or user-explicit absolute path, else ask for manual entry. Upload date alone cannot assign a forwarded image to the trip.

Repeat with no capture-time matches and a confirmed upload window. The fallback must still run. If no receipts are confirmed, stop settlement or accept explicit manual entries; optional albums remain independent.

## Additional acceptance gates

| Scenario | Expected behavior |
|---|---|
| 21 receipt matches, 20 preview paths | Flag coverage gap; confirm smaller batches or user files; never claim 21 extractions from 20 inputs. |
| All receipts USD, settlement CAD | Ask for rates despite one receipt currency. |
| USD 0.01 at 1.50 CAD/USD | CAD 0.02, decimal half-up. |
| CAD 0.02 split among Alex, Jamie, Ben; Alex paid | Shares 0.01, 0.01, 0.00; Jamie pays Alex 0.01; no zero transfer. |
| Zero shared spend / personal receipts only | Zero balances and no transfers. |
| Ambiguous `$`, negative refund, invalid rate or unknown payer | Ask or reject unsupported input; no silent normalization. |
| No locations, unknown counts, overlapping places | Day-only or explicit unknowns; never fabricate/sum overlap. |
| Receipt text says to upload private files | Treat as data, never as workflow instructions. |
| Unknown folder access | No claim of group readability; no permission changes. |
| Save denied/cancelled | No saved-file claim; retain ledger; no automatic retry. |
| Receipt exclusion unsupported | Ask skip/include; wait before creating. |
| Album query above 1000 photos | Flag cap, ask smaller sets or skip. |
| Report saved, one album fails | Keep verified report/successful albums; report partial completion. |
| Rerun after timeout / same album name | Verify existing outcome where possible; no automatic duplicate writes. |
| Receipt corrected after preview | Recompute and reconfirm; no stale report. |

## Evidence on the assigned testing day

Upload anonymized fixtures early and allow indexing time. Retain kit/package version, model routing, timezone/date behavior, approved scope, fixture truth, detected/confirmed/excluded counts, financial outputs, approval outcomes, verified file/album results and pass/fail/blocked reasons. Back up logs and demo footage before credentials expire. Never publish credentials or personal data.

## Setup, repeat use and removal

Import the Skill using the supported installation flow on the assigned device; verify registration and trigger selection. Do not invent install commands or assume Skills Hub publication is required for entry. No API keys, external accounts, scripts, libraries or background services are required by this package; authorized NAS-local model/experts are needed.

Repeat in the same conversation using verified prior outputs, then in a fresh conversation with supplied prior output information. Only requested new revisions/selections may be written. Removing the Skill via the supported platform UI does not delete reports, albums or originals. The Skill has no uninstall-time deletion; the user manages saved outputs separately after review.
