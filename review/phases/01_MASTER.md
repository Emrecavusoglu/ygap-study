# Phase 1 — Establish the master version

Audit date: 19 September 2026. Status: available versions reconciled; factual provenance queries remain.

## Inputs and hierarchy

The GitHub main branch contains the original Turkish DOCX and SAV. The review branch adds the English master, historical English snapshot, syntax, reproducible aggregate analysis and issue register. At the start of this extension, main was `619e4f6020c946b0b8ea5db70982c8cfe07e4bc5`; the review branch was `843660936cfc6e8f72d9e71f9aefb0fcd1551646`. No newer supervisor version was found in the inspected repository.

| Source | Check | Role |
|---|---|---|
| Turkish DOCX in GitHub and uploaded copy | Exact Git blob match, a49b9b7ac4badbaedde9dc71e60abf858f812c08 | Original narrative, not an authority over contradictory data |
| Repository and uploaded SAV | Binary files differ; all 115 × 13 values and row order agree | Numerical source |
| Earlier English DOCX | Extracted and compared | Historical translation |
| User's pasted translation | Compared as conversation text | Author's wording; not a separately authenticated file |
| OUTPUT2.pdf | 126 image pages OCR'd; key tables reconciled; selected pages visually checked | Saved analysis evidence |
| OUTPUT.pdf | 62 image pages; not completely reconciled | Earlier archive; no claim of exhaustive verification |
| YGAP_analiz.sps | Read and archived | Documents requested procedures; does not establish diagnosis code meanings |

## Version decision

[MASTER.md](../../manuscript/MASTER.md) is the working English document. Corrections are based on the SAV and saved output, while recruitment, ethics, diagnosis labels and institutional facts remain explicit author queries. Neither translation resolves a factual discrepancy merely by repeating it.

Both English versions inherited the reversed depressive-temperament Discussion and causal criminality interpretation. The revised master corrects these and uses affective temperament rather than temperament and character. Original files and the historical translation remain preserved.

## Remaining provenance work

The dataset lacks participant identifiers and categorical value labels. No source questionnaire, item-level responses, enrollment log or ethics approval document has been inspected. Confirm whether a more recent supervisor correction exists outside GitHub. Record its date and author before integrating it.

## Exit condition and handoff

One active master and a traceable issue list exist. Phase 1 document consolidation is complete for available materials; authentication of study facts is not. Authors should return confirmed facts against issue IDs, rather than create another untracked English version.
