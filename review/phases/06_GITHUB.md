> **Status superseded on 21 September 2026:** see [current full review](../FULL_REVIEW_2026-09-21.md). The original paper is now the author-selected numerical source. Older SAV analyses are historical and not verified results for that paper. Resolved methods questions in the current review must not be re-asked from historical lists below.

# Phase 6 — Reproducibility and GitHub package

Status: review checkpoint; final release is dependent on phases 2–5.

## Repository inspection

Repository: Emrecavusoglu/ygap-study, verified private at the initial audit. The initial default branch contained the Turkish DOCX and SAV. Authenticated GitHub API access works; shell cloning lacked credentials. No existing Actions workflow failure was identified. This is a manuscript/data audit, not a repair of a failed CI pipeline.

Review branch: `review/manuscript-audit-2026-09-19`. This extension builds on `843660936cfc6e8f72d9e71f9aefb0fcd1551646`; original main was `619e4f6020c946b0b8ea5db70982c8cfe07e4bc5`.

## Deliverables

- One working English master and corrected aggregate tables.
- Reproducible analysis script, recorded package versions, original syntax and aggregate JSON/Markdown.
- Source manifest, historical translation and issue register.
- Six phase reports, full original-reference triage and claim audit.
- Updated report index linking these materials.

Only review documents and the working master are changed in this extension. Original data are preserved. Participant-level records already present in the private repository are not duplicated in reports; no identifiers or source enrollment records are added.

## Validation

A rerun in the audit environment passed five saved-output assertions and produced JSON identical to the prior committed output. These checks cover computation with the supplied dataset; they do not validate categorical labels, participant independence or all original scale items. A clean installation on a different machine has not been independently tested. The requirements file records the audit environment; dependency availability must be checked if recreating it elsewhere.

Markdown local links are checked before committing. The branch head is re-read before updating, and the pushed commit is verified afterward. The final commit hash is available in GitHub history and the delivery message rather than embedded recursively in this report.

## Release policy

The review branch is a concrete reviewable checkpoint, not a declaration of author approval. Finalize source facts and scientific decisions before merging a submission release. A private repository containing research data should not be made public as part of routine manuscript packaging; any public code release needs a separate data-sharing decision.

## Revision checkpoint — 20 September 2026

The 20 September revision adds author-confirmation provenance, reproducible focal effect sizes, essential source follow-up and submission structure. This is a review-branch checkpoint, not author approval or submission.
