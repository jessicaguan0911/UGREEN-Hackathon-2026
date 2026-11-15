# Trip Wrap-Up: Settle Up and Relive Your Trip

Skill: trip-wrap-up · Track: Open Innovation · Version: 0.2.0
Technical revision for entrant review; original Round 1 materials are preserved.

## 1. What does the Skill do?

It finds receipt photos on a shared UGREEN NAS, helps friends review trip expenses, saves a who-pays-whom report, and optionally organizes trip albums.

## 2. Who is the target user and problem?

Roommates and friend groups sharing a NAS hesitate to request repayment, while friends who owe money lack a clear total. Receipts scattered among trip photos make reconstructing expenses tedious.

## 3. What is your proposed solution?

Members photograph receipts during the trip. Afterwards, the Skill finds candidates, asks for missing financial facts, and creates a neutral report with source references. Photo activity prompts users to remember missing expenses; it never proves a purchase occurred.

## 4. What is the Core User Flow?

Confirm dates, members, currency, payment mode and photo scope; build a photo-activity checklist; find and review receipts; confirm payers, exclusions and rates; preview transfers; approve a saved report; optionally create albums.

## 5. What substantive difference does your idea offer?

The shared NAS connects expense evidence with trip memories. A place with many photos but no receipts prompts a review that an expense ledger alone cannot provide. Albums reuse the same scope. Full source paths make confirmed expenses traceable.

## 6. Which UGREEN AI NAS capabilities will be used, and at which step?

Photo-agent uses ug-photo search-picture and search-screen for activity and receipt discovery, vision-ocr for eligible fallback images, and create-album for albums. Document-agent uses ug-document extract with receipt schema and dedupe. Knowledge-agent uses ug-knowledge save-text for the report.

## 7. What was your technical approach?

A Markdown-only Skill delegates to registered experts. Read scope is confirmed; writes require platform approval. Missing paths, preview truncation and unreadable images trigger clarification. Settlement uses integer cents, confirmed rates, deterministic rounding and balance/transfer checks. The intended model runs locally; external services are excluded. Reruns preserve prior outputs.

## 8. What is the current development status?

Implemented: workflow, report template, settlement rules, capability boundaries, disclosures and test plan. Official static checks pass. An exact-arithmetic model passes seven golden cases and 20,000 synthetic trips. NAS installation, image extraction, search recall, scope enforcement and model routing remain unvalidated.

## 9. What is your final validation plan?

Core one: four members, fifteen receipts among 300 photos; expected CAD 800 total and three specified transfers. Core two: one payer, USD/CAD expenses, CAD 100 total and a rounding remainder. Combined edge case: duplicate, blurry and undated images must trigger review. Test interrupted writes and reruns separately.

## 10. Are there any known limitations?

Members need NAS accounts and authorized shared access. Equal splits only; two-decimal settlement currencies; user-supplied rates. Searches may expose only previews. Image extraction, receipt exclusion from albums, location grouping and timezone behavior need device validation. Missing receipts can change totals.

---

Third-party/runtime dependencies: UGREEN UGOS experts and local model, under applicable UGREEN terms; official kit 0.7.7/catalog 2.2.0, source https://ai.ugreen.com/pages/hackathon-starter-kit. No bundled third-party libraries or external runtime services. Codex assisted review, workflow/document drafting and validation tooling; source https://openai.com/codex/, applicable OpenAI terms. Local PDF generation uses ReportLab 4.4.9, https://www.reportlab.com/, BSD license, and its bundled Bitstream Vera font, https://www.gnome.org/fonts/, Bitstream Vera font license; neither is a Skill dependency. Full disclosure is in the ZIP's directly linked references/disclosures.md. No NAS execution is claimed.
