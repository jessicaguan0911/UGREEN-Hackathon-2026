# Capability boundaries

Source: official UGREEN Skill Developer Package 0.7.7, catalog 2.2.0, from https://ai.ugreen.com/pages/hackathon-starter-kit. Examples are synthetic, not verified NAS responses. The parent delegates; registered experts select actual Actions.

| CLI / expert | Actions used | Effect / approval | Required evidence and boundary |
|---|---|---|---|
| `ug-photo` / `photo-agent` | `search-picture`, `search-screen`, `albums`, optionally `meta` | Read / none | Actual totals and references; previews are not exhaustive exports. Only use place candidates established inside the approved scope. |
| `ug-photo` / `photo-agent` | `vision-ocr` | Read / none | Single user-explicit absolute image path or attachment; compact OCR output. A discovered path alone is insufficient. |
| `ug-document` / `document-agent` | `extract`, receipt schema and dedupe | Read / none | Account for exact paths, fields, failures and ambiguity. Receipt schema does not prove image-file support; test on the NAS. |
| `ug-knowledge` / `knowledge-agent` | `save-text` | State change / workflow | Confirmed real folder and full content; verified output path/read-back. Not proof of indexing or group access. |
| `ug-photo` / `photo-agent` | `create-album` | State change / workflow | Confirmed regular-album name and scoped real reference; actual creation and ID. Blocked is not created. |

## Search coverage gate

Photo searches expose matched totals, a result reference and the first 20 previews. Do not invent pagination/export parameters or assume document-agent can read a photo result reference.

1. Keep each query's matched total and individually returned real paths; deduplicate overlaps by picture ID, not filename.
2. Exhaustive candidate access requires uniquely identified returned items to account for the matched total. Missing totals/paths mean unverified coverage. Even exhaustive results do not prove the search recognized every real receipt.
3. If more matched than are individually available, ask for user-confirmed narrower day/time batches within the approved range. Boundaries must cover the range without gaps; deduplicate overlaps. Never set a small limit and call the resulting preview complete.
4. If supported queries cannot expose all required paths, ask for missing files or explicit limited-coverage acceptance. List omissions; never manufacture successful extraction.
5. Activity counts use actual query totals, not inspection of every scenery image. Unknown locations fall back to days; a full place inventory depends on real metadata or a confirmed itinerary.

## Time and scope constraints

- `search-picture` date filters refer to capture time. Sorting by upload time does not change filtering semantics.
- `search-screen` supports a date range with `time-field=create-time` or `time-field=upload-time` and recognized receipt content.
- OCR-text matching is documented on `search-picture`, without an upload-time filter. Do not claim this combination exists. The missing-date fallback uses content search and has a stated recall limitation.
- Structured album/folder selectors on `search-picture` do not have equivalents on `search-screen` in this catalog. Stop searches that cannot enforce a user's narrower restriction; ask before broadening it.
- Validate actual timezone and date endpoints on the assigned NAS. Do not promise exact timezone behavior before testing.

## Albums and privacy

Create albums using real search references, not preview IDs. Automatic query selection freezes the first 1000 IDs; handle larger sets explicitly without implying full inclusion. No general result-set subtraction/filter Action is published. Receipt exclusion is conditional: ask skip/include if it cannot be verified, rather than inventing support. Shared source photos do not establish the created album's audience; report known visibility or mark it unknown.

No external services, payments or access-control changes are included. Verify local-model routing during NAS testing; do not substitute a cloud model or loosen permissions to make a test pass.
