# Trip Wrap-Up

Trip Wrap-Up helps friends review shared trip expenses using receipt photos on their UGREEN NAS. It prepares a report showing who should pay whom and can also organize trip albums.

## Before you start

Use the platform's supported Skill installation flow and confirm that the NAS-local model and registered photo-agent, document-agent and knowledge-agent are available. Device installation and the full workflow still need NAS testing.

Members need accounts on the same NAS and access to the shared photos and report destination. This version supports 2–8 people, equal shares and settlement currencies with two decimal places. Members photograph receipts during the trip and upload them with their other photos. Original uploads are preferable because forwarded images can lose their capture dates.

## Start a review

For example: "Wrap up our Banff trip from 2026-10-04 to 2026-10-05. Members are Alex, Jamie, Ben and Cindy. Settle in CAD and use the shared photo space."

The Skill asks for missing dates, timezone, member order, currency, payment mode and search scope. It does not infer permission to read other members' private libraries. An upload-date fallback needs a confirmed window.

Review the daily and whole-trip place summaries for possible missing expenses. Confirm receipt amounts, payers, duplicates, personal items and any exchange rates. A day with no receipts may have had no spending; a receipt already found at a place does not prove that all expenses are accounted for. Unreadable or unconfirmed receipts stay visible.

Check the proposed transfers, choose the report folder and approve the save. Albums are optional and require separate approval. The report gives payment instructions; it does not transfer money or message anyone.

## Source, dependencies and configuration

SKILL.md is the entry point and includes the name and description frontmatter. Together with its directly linked Markdown references, it is the source of this orchestration Skill. Do not add a separate manifest.

The runtime dependencies are the supported UGREEN platform capabilities and configured NAS-local model. There are no bundled libraries, scripts, API keys or external runtime services. Inputs are collected in conversation, so no separate configuration template is needed. Sources, applicable terms, local development tools and AI use are listed in disclosures.md, linked directly from SKILL.md.

## If something fails

Missing paths, unreadable receipts, truncated search previews and unknown permissions are reported rather than guessed. Platform approvals remain required. A failed album does not erase a saved report; an interrupted write is not retried automatically. Previous report revisions and source photos are preserved. Use the linked validation plan for test cases and safe removal guidance.
