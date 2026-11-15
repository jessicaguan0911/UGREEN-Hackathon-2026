# Development and AI disclosure

## Work developed for this Hackathon

Trip Wrap-Up's Skill and supporting documents were developed during this Hackathon. The workflow finds receipt photos, checks for possible missing expenses by day and by place, asks users to confirm financial details, calculates equal shares, and saves a report. Optional albums use the same trip information.

The package contains the Markdown workflow, report template, settlement rules, capability notes and test plan. It does not reuse a previously developed third-party Skill. There are no bundled scripts, libraries, model weights or executables.

## Tools and dependencies

The official UGREEN Skill Developer Package 0.7.7 and catalog 2.2.0 were used for authoring guidance, capability checks and static validation. They are available at https://ai.ugreen.com/pages/hackathon-starter-kit and are subject to UGREEN's applicable agreements and publishing guidelines. No open-source license is claimed for these resources, and the kit is not included in the Skill ZIP.

At runtime, the Skill needs UGREEN's registered photo-agent, document-agent and knowledge-agent, plus a configured NAS-local model, under the platform's applicable terms. Actual device behavior has not yet been tested. The workflow uses no external model, exchange-rate API or payment service.

Local development utilities, which are not Skill runtime dependencies:

| Tool | Source | License or terms |
|---|---|---|
| OpenAI Codex | https://openai.com/codex/ | Applicable OpenAI terms |
| Python | https://www.python.org/ | PSF License |
| Node.js | https://nodejs.org/ | MIT license |
| ReportLab 4.4.9 | https://www.reportlab.com/ | BSD license, as stated in its package metadata |
| Bitstream Vera font, embedded in the separate proposal PDF | https://www.gnome.org/fonts/ | Bitstream Vera font license |

## AI assistance

Codex helped review the idea, write and revise the Skill and proposal, identify edge cases, and prepare the local validation and packaging tools. It also checked word counts and package contents and ran the official checker. The entrant confirmed that Codex and the official UGREEN package were the only AI/Skill-assistance products used. The UGREEN package supplied instructions and capability information; it is not a separate AI model.

Codex is a development tool, not a runtime service for the Skill. It has not run this project on a NAS or submitted the entry.

## Data handling

Development used project files, contest text and public technical documentation. The package contains no real receipts, private photo libraries, credentials or API keys. Test descriptions use invented names and synthetic amounts. Demo data must be synthetic or anonymized, and any images must be authorized for use.

The intended workflow processes authorized NAS content with local capabilities and saves only to a user-confirmed folder. It does not send receipts to an external service. Local-model routing, permissions and indexing still need to be checked on the assigned NAS.
