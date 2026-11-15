# Components, originality and AI-use disclosure

## Principal functionality developed for this Hackathon

This project defines a new Markdown orchestration workflow for post-trip expense review: discover receipt candidates in authorized NAS photo spaces; use day/place photo activity to prompt missing-expense review; confirm duplicates, payers, personal exclusions and rates; calculate equal-share transfers with integer-cent checks; save a source-traceable report; and optionally create albums from the same trip scope. Supporting documents define report format, settlement rules, capability boundaries and validation scenarios. No custom application, trained model or executable NAS code is bundled.

Repository history records the initial Skill during this Hackathon. The entrant retains responsibility for originality and rights to submitted work/data; no pre-existing third-party Skill is claimed. Development scope is not proof of NAS runtime execution.

## Third-party resources and dependencies

| Resource | Source | Terms/license and use |
|---|---|---|
| Official UGREEN Skill Developer Package 0.7.7, catalog 2.2.0 | https://ai.ugreen.com/pages/hackathon-starter-kit | UGREEN-provided resource subject to its applicable agreement, privacy policy and Skill publishing guidelines; no open-source license is asserted. Used for guidance, capability lookup and local static checks. Tool/checker/catalog not redistributed in the Skill ZIP. |
| UGOS photo-agent, document-agent, knowledge-agent and configured NAS-local model | Official Starter Kit and assigned UGREEN AI NAS | Platform runtime dependencies under applicable UGREEN service/license terms. No SDK or model weights bundled; device behavior not yet tested. |
| OpenAI Codex | https://openai.com/codex/ | AI development assistance under applicable OpenAI terms; not a Skill runtime dependency. Principal uses below. |
| ReportLab 4.4.9 (local PDF review draft only) | https://www.reportlab.com/ | BSD license per installed package metadata. Its bundled Bitstream Vera font is embedded in the separate PDF under the Bitstream Vera font license (source: https://www.gnome.org/fonts/). Neither library nor font is in the Skill ZIP or a NAS dependency. |
| Python and Node.js (local validation/build only) | https://www.python.org/ and https://nodejs.org/ | PSF License and MIT license respectively; not redistributed in the Skill ZIP. Node.js runs the official checker; Python runs synthetic arithmetic checks and packaging. |

**Bundled third-party components and open-source libraries: none.** The ZIP contains only project Markdown. Local packaging and mathematical verification utilities stay outside the ZIP and are not runtime dependencies. No additional external APIs, live-rate service or external data feed is used.

## AI tools and principal uses

The entrant confirmed that **Codex and the official UGREEN package are the only AI/Skill-assistance products used**. Codex assisted PM/idea review, drafting and revising the Skill workflow and supporting documentation, identifying limitations and edge cases, checking proposal word count and package consistency, invoking the official checker, and developing local arithmetic verification and packaging utilities. Codex also drafted the version 0.2.0 technical proposal revision; the original proposal files are preserved. The entrant must review final submission authorship and any separate FAQ requirements. This assistance must not be described as proofreading only.

The UGREEN package supplied authoring instructions, capability facts and static validation; it is a development resource, not another AI model. Codex did not access a test NAS, execute the Skill on a NAS, move money, message trip members or submit the entry. No runtime Codex/OpenAI connection is required by the workflow.

## Data and external flows

Codex reviewed project files, supplied contest text and public technical documentation in the development workspace. No real trip receipts, credentials or personal photo libraries are bundled. Fixtures use invented labels and synthetic descriptions; no real card digits, personal data, access tokens or API keys are included.

The intended deployed workflow uses local NAS capabilities and a user-confirmed destination, with no added external inference or transmission. This is a design constraint: local-model routing, storage permissions, indexing and actual device behavior remain to be validated. Public demo data must be synthetic/anonymized and images authorized.
