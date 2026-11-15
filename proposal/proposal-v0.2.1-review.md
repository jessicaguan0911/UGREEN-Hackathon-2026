# Trip Wrap-Up

UGREEN Hackathon 2026 · Open Innovation · Version 0.2.1

## 1. What does the Skill do?

Trip Wrap-Up finds receipt photos on a shared UGREEN NAS, helps friends settle trip expenses, and optionally organizes their trip albums.

## 2. Who is the target user and problem?

It is for roommates and friends who share a NAS. Asking friends to repay money can feel awkward. After a trip, receipts are scattered among photos, and nobody remembers every purchase.

## 3. What is your proposed solution?

During the trip, members just photograph receipts. Afterwards, the Skill finds them and asks for the details it cannot know, such as who paid. A saved report shows the confirmed expenses and who should pay whom.

## 4. What is the Core User Flow?

The user confirms dates, members, currency and photo scope. The Skill finds receipts, then checks for missing expenses by day and by place. Users confirm amounts, payers and rates before reviewing transfers and approving a report. Albums are optional.

## 5. What substantive difference does your idea offer?

The NAS holds both receipts and trip photos. If day three has photos but no receipts, or a visited place has none, the Skill asks whether anything was spent there. This gives friends a way to remember missing expenses. Each recorded receipt keeps its source path.

## 6. Which UGREEN AI NAS capabilities will be used, and at which step?

Photo-agent uses ug-photo search-picture and search-screen to find photos and receipts, vision-ocr for eligible unreadable images, and create-album for albums. Document-agent uses ug-document extract with receipt schema and dedupe. Knowledge-agent saves the report through ug-knowledge save-text.

## 7. What was your technical approach?

The Markdown Skill delegates to registered experts. Searches stay within the confirmed scope; writes need platform approval. Missing paths, truncated results and unreadable receipts prompt clarification. Settlement uses integer cents, confirmed rates and balance checks. Existing reports are preserved on reruns. The intended workflow uses the NAS-local model without external services.

## 8. What is the current development status?

The workflow, references and local checks are built. The official checker passes. A separate arithmetic model passes seven known examples and 20,000 synthetic trips. The Skill has not run on a NAS; installation, image extraction, search coverage, permissions and local-model settings still need testing.

## 9. What is your final validation plan?

First, test four members and fifteen receipts among 300 photos: expect CAD 800 and three transfers. Second, test one payer with USD/CAD expenses: expect CAD 100 with a rounding remainder. Test duplicate, blurry and undated images together, then check cancelled writes and repeated requests.

## 10. Are there any known limitations?

Members need NAS accounts and shared access. Only equal splits and two-decimal settlement currencies are supported. Users provide rates. Search previews, missing location data and unreadable receipts can limit coverage. Album receipt exclusion and date boundaries need device testing. Missing receipts can change the totals.

---

UGREEN's official kit 0.7.7/catalog 2.2.0 and runtime experts are used under applicable UGREEN terms: https://ai.ugreen.com/pages/hackathon-starter-kit. No third-party libraries are bundled in the Skill, and it uses no external runtime services.

Codex helped write and review the Skill and proposal and prepare validation tools: https://openai.com/codex/, applicable OpenAI terms. Local PDF generation uses ReportLab 4.4.9 (BSD license, https://www.reportlab.com/) and Bitstream Vera (font license, https://www.gnome.org/fonts/). Neither is a Skill dependency. Full tool, license and AI-use details are in the ZIP's linked references/disclosures.md.
