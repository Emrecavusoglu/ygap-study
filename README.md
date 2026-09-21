> **Latest review: 21 September 2026.** [Full article/reference review](review/FULL_REVIEW_2026-09-21.md) · [Current paper-based master](manuscript/MASTER.md). Original manuscript values take priority by author instruction; old SAV analyses are historical. The paper has unresolved internal numerical conflicts and is not submission-ready.

# YGAP affective temperament study

Working materials for the comparison of high-security forensic psychiatric inpatients, psychiatric outpatients and healthy controls. Target journal: International Journal of Law and Psychiatry.

## Current status

Implementation checkpoint dated 19 September 2026. The manuscript is **not ready for submission**: diagnosis and employment codes, source-record verification and several recruitment details remain unresolved. See [failure diagnosis](review/FAILURE_DIAGNOSIS.md).

- [Master English manuscript](manuscript/MASTER.md): the only active English draft, with explicit author queries.
- [Fresh cell-by-cell paper comparison](analysis/PAPER_CROSSCHECK.md): all original table values and 15 temperament contrasts; regenerate with `python analysis/crosscheck_paper.py`.
- [Reproduced results](analysis/generated/RESULTS.md): aggregate results and sensitivity analyses.
- [Six detailed phase reports](review/PHASES.md): evidence, corrections, remaining gates and next actions.
- [Source-by-source audit](references/SOURCE_AUDIT.md): all 17 original references plus five priority additions, with reading limitations.
- [Claim audit](review/CLAIM_AUDIT.md): manuscript assertions checked against data and sources.
- [Reference evidence map](references/EVIDENCE_MAP.md): proposed sources and claim-specific uses.
- [Source manifest](review/source_manifest.json): hashes for the reviewed inputs.
- Original Turkish DOCX and SAV remain unchanged at repository root.

## Reproduce the numerical audit

```bash
python -m pip install -r analysis/requirements.txt
python analysis/reproduce.py
```

The script reads the existing SAV and writes aggregate Markdown and JSON. It checks selected results against archived SPSS output. It does not modify observations, infer diagnosis labels, or remove repeated rows. Statistical reproduction is possible without a paid SPSS license.

The archived syntax is in `analysis/YGAP_analiz.sps`; it assumes the dataset is already open in SPSS. The original PDF outputs were inspected locally and identified by hash; they are not required to execute the Python audit.

## Version policy

Edit `manuscript/MASTER.md` rather than the historical English snapshot. Mark factual queries until the authors resolve them. Keep the reference evidence map separate from final reference selection. This repository already contains participant-level data and was verified private at this checkpoint; any wider sharing requires a separate data-sharing decision.
