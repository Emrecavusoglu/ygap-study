# YGAP data verification and variables to collect

## Final language revision checkpoint

21 October 2026. The manuscript has been edited for clear, natural academic English. All numerical tokens and all 31 reference entries are unchanged from the verified numerical version. Table cells are unchanged; the explanatory footnote has been clarified. There are no em dashes in the manuscript.

Matching Word and Markdown versions are prepared for the existing GitHub review branch. Original forms and datasets remain unchanged and are not included. This editorial checkpoint is not source-form verification or final author approval. See review/FINAL_LANGUAGE_REVIEW_2026-10-21.md in the repository for the remaining author checks. Earlier statements below about whether GitHub was changed refer to the dated audit or correction step, not to this new packaging step.

### Language-edited file fingerprints

- 01_IJLP_Manuscript.docx SHA256: `1020cecf7b627c2b993ce54670354ab5f6f814127d2271e0115467940a34db42`
- 02_IJLP_Tables.docx SHA256: `cd13128b7e9cfa4a70c704778643521373eab7686dc145436fad4df5d0ed843c`

## Update after applying the verified SAV results

21 October 2026. The current Library manuscript and matching three tables have now been aligned to the verified author-supplied SAV. The earlier FAIL findings below describe the pre-correction Word version and are retained as the correction history, not the status of the revised files.

- **Dataset-to-manuscript numerical alignment: PASS.** All 373 saved numerical aggregate values reproduce; the abstract, Results, diagnostic counts/percentages and all affected table cells now use the same dataset version.
- Corrected items include outpatient age SD 8.32; outpatient depressive score 12.68 ± 4.29; forensic irritable score 11.58 ± 4.78; cyclothymic F=16.418; hyperthymic p=.081; forensic employment counts 41/25 with χ²(2)=15.238; and diagnostic counts 28/29/9 (forensic) and 9/13/3 (outpatient).
- The 31-reference bibliography and the cautious interpretation are unchanged. The original SPSS analysis and the Python revision check are distinguished in Methods.
- **Original paper forms and source datasets: unchanged. Source-form verification: NOT COMPLETED.** These corrections establish numerical agreement with the supplied SAV, not independent validation against original clinical or participant records.
- The missing-variable inventory remains valid. No missing clinical data, questionnaire item responses or measurements were invented. Income remains entirely missing; missing control diagnoses were not imputed.
- The current article still requires author approval, completion of declarations and factual publication details, and the remaining source-record checks. Numerical agreement alone does not mean submission approval.
- No GitHub files were changed or pushed in this correction. Older review/checklist documents predating this update should be treated as historical for their numerical status.

### Corrected file fingerprints

- Revised manuscript SHA256: `30d2035ad42e7abc323fd6151151b6c510dafd72681fd96dbac629a9f5409a12`
- Revised tables SHA256: `e873250ee86e964007afdb10942f747b2fa674a0964a6c6caf08423990174bb6`
- Numerical source SAV SHA256: `c9847b403a1b834662ff16c6b7ddb0b0f04bc3dbbdde381c72ef889dae4f1998`

## Historical audit before the correction

Audit date: 21 October 2026. Scope: read-only comparison of the corrected SAV, the original Turkish manuscript, the open English Word manuscript, and the pinned GitHub review branch. No participant-level data or questionnaire item responses are exported in this report.

## Findings

- Numerical reproduction: **PASS**, 373 saved numerical scalar values reproduce within rtol=1e-10/atol=1e-12 (package-version metadata excluded). This checks calculations against the saved aggregate output, not clinical source truth.
- Dataset: **115 records × 13 columns**; forensic 66, outpatient 25, control 24. Twelve columns contain some data; the income column contains none.
- Form-to-dataset transcription: **NOT VERIFIED**. No participant paper forms, enrollment register, source-record linkage key or item-level forms are available in the inspected repository/workspace. The Turkish research manuscript and SPSS PDFs are not participant source forms.
- Manuscript consistency: **FAIL** for selected numerical claims. The open Word manuscript contains the restored original numbers; the GitHub review master/tables instead use the corrected SAV. The two numerical editions must not be combined.
- Sources unchanged: **PASS**. Input hashes were checked before and after. The verification script ran only in a scratch copy; it did not overwrite the active manuscript, source datasets or repository results.

## Repository state and code behavior

- Review branch: `review/manuscript-audit-2026-09-19`, pinned commit `304d6ccaa664fbd9d34c281674ceacbf71a4cf05`. Default `main` commit: `63e18a31e59d9eedd9cb700eb5d8763a1acb77da`.
- `main` contains the original Turkish DOCX and `.gitignore`; the analysis scripts are on the review branch.
- No `.sav`, participant source forms, `AGENTS.md` or GitHub Actions workflow files occur in either inspected current branch tree. The GitHub Actions API reports zero workflow runs. This does not rule out commands running locally or in another environment, and is not a scan of every historical commit.
- `analysis/reconcile_current.py` reproduces aggregates from the locally retained corrected SAV. It writes `analysis/generated/current_results.json` and `manuscript/TABLES.md` when run normally; this audit isolated those writes.
- `analysis/reproduce.py` defaults to a root SAV that is no longer in the branch. Its archived employment check expects χ²=15.924 from the older three-category file, so it is not the corrected-data verification route.
- `analysis/crosscheck_paper.py` selects the first root SAV/DOCX through globbing. It also contains fixed narrative claims about legacy codes 3/4 and employment p=.003. Those statements are not dynamically valid for the corrected SAV. A script finishing successfully is not proof those static sentences are correct.
- The README has conflicting historical banners and a stale statement that a SAV remains at root. No repository files were edited or pushed during this check.

## Available variables

| SAV column | Meaning based on manuscript/team mapping | Nonmissing | Missing |
|---|---|---:|---:|
| `yas` | Age | 115 | 0 |
| `med` | Marital status | 115 | 0 |
| `is` | Employment | 115 | 0 |
| `tanı` | Diagnosis | 91 | 24 |
| `egi` | Education | 115 | 0 |
| `GELİR` | Income (empty) | 0 | 115 |
| `varyok` | Social security coverage, not income | 115 | 0 |
| `depres` | Depressive temperament total | 115 | 0 |
| `siklotimi` | Cyclothymic temperament total | 115 | 0 |
| `hipertimi` | Hyperthymic temperament total | 115 | 0 |
| `irritable` | Irritable temperament total | 115 | 0 |
| `anksiyöz` | Anxious temperament total | 115 | 0 |
| `grup` | Study group | 115 | 0 |

Diagnosis is absent in all 24 controls, consistent with the study structure; do not impute a patient diagnosis to controls. None of the columns has an embedded SPSS value-label/code dictionary, so clinical code meanings still rely on the documented team mapping.

## Current Word versus corrected dataset

The table below shows the important differences, not a replacement analysis plan.

| Item | Open Word manuscript | Corrected SAV recomputation |
|---|---|---|
| Forensic age, mean ± SD | 39.31 ± 10.67 | 39.32 ± 10.68 |
| Outpatient age SD | 8.12 | 8.32 |
| Outpatient depressive mean ± SD | 12.66 ± 4.28 | 12.68 ± 4.29 |
| Forensic irritable mean ± SD | 11.57 ± 4.75 | 11.58 ± 4.78 |
| Cyclothymic F | 16.413 | 16.418 |
| Hyperthymic p | .810 | .081 |
| Employment χ² | 15.924 | 15.238, df=2, p<.001 |
| Forensic diagnoses, codes 1/2/3 | 29.4% / 51.5% / 19.1% | 28/29/9 = 42.4% / 43.9% / 13.6% |
| Outpatient diagnoses, codes 1/2/3 | 18.4% / 52.3% / 29.4% | 9/13/3 = 36.0% / 52.0% / 12.0% |

The original Turkish employment table lists 41 employed and 24 unemployed forensic participants, totaling 65 rather than 66. The corrected SAV has 41 and 25. The original table’s χ²=15.924 is reproduced by the older three-code file, but its p is approximately .003 with df=4, not <.001. The corrected two-category file gives χ²=15.238. Simply restoring the old χ² while keeping the newer p mixes versions.

5 of the six original diagnosis percentages are not attainable to one decimal place with the stated group sizes of 66/25. For the outpatient n=25, percentages must be multiples of 4%. The forensic 51.5% alone is compatible with 34/66, but that is not the corrected SAV count and does not validate the full distribution. A source form or original output with the correct denominator is needed; diagnostic counts must not be invented from these percentages.

## Original Turkish table comparison

All 36 mean/SD scalar entries were checked: 19 agree at two decimals and 17 differ. All 33 categorical count/percentage cells were checked: 5 have a count or printed-percentage discrepancy.

| Variable | Group | Statistic | Original table | Corrected SAV rounded |
|---|---|---|---:|---:|
| yas | Forensic | mean | 39.31 | 39.32 |
| yas | Forensic | SD | 10.67 | 10.68 |
| yas | Outpatient | SD | 8.12 | 8.32 |
| depres | Outpatient | mean | 12.66 | 12.68 |
| depres | Outpatient | SD | 4.28 | 4.29 |
| siklotimi | Forensic | SD | 5.33 | 5.34 |
| siklotimi | Control | mean | 4.70 | 4.71 |
| siklotimi | Control | SD | 3.91 | 3.92 |
| hipertimi | Forensic | mean | 12.51 | 12.52 |
| hipertimi | Forensic | SD | 4.75 | 4.76 |
| hipertimi | Control | mean | 10.95 | 10.96 |
| hipertimi | Control | SD | 3.19 | 3.20 |
| irritable | Forensic | mean | 11.57 | 11.58 |
| irritable | Forensic | SD | 4.75 | 4.78 |
| irritable | Control | SD | 1.82 | 1.83 |
| anksiyöz | Control | mean | 3.37 | 3.38 |
| anksiyöz | Control | SD | 3.89 | 3.90 |

| Variable and category | Group | Original cell | Corrected count and percentage |
|---|---|---|---|
| egi code 3 | Forensic | 18(%27.2) | 18 (27.27%) |
| egi code 4 | Forensic | 6(%9.2) | 6 (9.09%) |
| med code 2 | Forensic | 15(%22.8) | 15 (22.73%) |
| is code 2 | Forensic | 24(%37.4) | 25 (37.88%) |
| varyok code 0 | Forensic | 31(%46.96) | 31 (46.97%) |

The corrected and older locally supplied SAVs differ in 15 diagnosis cells and one employment cell when compared in the supplied row order. Age and all five temperament totals are unchanged. With no participant identifier, this is a positional comparison, not independently verified person-level linkage. Repeated anonymous profiles are not proof of duplicate enrollment and must not be removed automatically.

## Variables missing from the SAV and how to collect them

“Absent” means absent from this SAV, not proof that a field was collected on paper. Availability in original records must be established locally before abstraction. Do not retrospectively create observations that were never recorded.

### Priority 1 Source verification and reproducibility

| Field to obtain locally | Status | Source and recording rule |
|---|---|---|
| Pseudonymous study ID and row-to-form linkage | Absent | Create a local study code only after checking the enrollment register. Keep names, hospital IDs and the linkage key off GitHub and out of shared reports. |
| Source form locator and source version | Absent | Retain an authorized local locator; record which original form and corrected SAV version each audit covers. |
| Diagnostic coding system/version, diagnosis date and confirmation source | Absent beyond diagnosis category | Abstract from the original clinical diagnosis/record; do not translate legacy subtypes into a modern classification without evidence. |
| Original employment answer, reference period and correction evidence | Reference period/audit trail absent | Check the disputed forensic record and retain the existing answer unless the form supports a correction. Preserve a change log with reason and reviewer. |
| TEMPS-A form/version and scoring key | Not embedded in SAV | Confirm locally which 99-item form/key was actually administered. Total-score ranges alone do not verify scoring. |
| Item completeness, scoring verification and reliability results | Only five totals available | The team should inspect item forms locally and report aggregate checks. Do not share item responses with an LLM. |
| Sex | Absent; all-male status already author-confirmed | Confirm against the enrollment record once. It is not an unknown study fact and adds no adjustable variation if all are men. |

### Priority 2 Methods documentation already described in the manuscript

| Field to check | Status | Source and recording rule |
|---|---|---|
| Assessment date and admission date | Absent | Record the original dates locally; derive hospitalization length only if both dates are valid. |
| Psychiatrist-rated clinical stability and date | Absent | Use contemporaneous documentation. Do not invent a numerical symptom score from narrative notes. |
| Offense category and violent/nonviolent classification | Absent | Use authorized forensic records and a prespecified coding definition; a forensic-group code alone is not a violence measure. |
| Outpatient offense-history assessment | Absent | Record what was checked and when; do not call outpatients “non-offenders” without supporting assessment. |
| Independent versus reading-assisted completion | Absent | Recover from administration logs only if documented; otherwise record “not documented.” |
| Control screening and recruitment source | Absent | Retain the procedure and any contemporaneous screening record; do not invent a screening score. |
| Screening/enrollment/exclusions by reason | Absent; aggregate process data | Check the recruitment log. “Approximately 90” minus 66 is not a verified exclusion count. |
| Consent/capacity assessment documentation | Absent from analytic SAV | Check locally for all enrolled participants; do not export signatures, names or consent documents. |

### Priority 3 Optional covariates only if contemporaneous records exist

| Candidate field | Why useful | Collection boundary |
|---|---|---|
| Alcohol/substance use with time window | Potential confounding/context | Distinguish documented absence, presence and unknown; distinguish past from assessment-period use. |
| Illness onset and duration | Diagnostic/course differences | Derive duration only from a documented onset/reference date; do not guess. |
| Medication class, dose, duration and adherence | Clinical/treatment differences | Capture the regimen at the assessment date, not the current regimen; standard-dose conversion would be derived and documented separately. |
| Prior hospitalizations and psychiatric comorbidity | Clinical severity/history | Use the available record and explicit definitions; absence of a note is not confirmed absence. |
| Prior violence/offense history | Distinguishes history from current forensic status | Abstract only authorized, relevant historical information with a defined time window. |
| Income | Existing `GELİR` column is 115/115 missing | Recover only if actually recorded on original forms; social security coverage is not a substitute for income. |

Standardized PANSS/depression/mania/insight/aggression scores were not administered according to the confirmed Methods. They cannot be backfilled as if measured at the original visit. A new assessment now would be a separate time point and might require a revised protocol/ethics review; it is not a repair of the original dataset. Character traits were not measured by TEMPS-A and cannot be inferred from its five totals.

No new model, subgroup analysis, Monte Carlo test or additional clinical measurement is necessary merely to perform this verification. These are missing-data/source-documentation opportunities, not permission to expand the analysis until results look stronger.

## Local source-form verification protocol

1. Freeze the selected SAV and its hash. Keep an immutable original and a separate local working copy.
2. Have an authorized team member create the study-ID-to-form linkage locally; do not infer identity from row order or matching temperament scores.
3. Check every available original-form field against the corresponding SAV column for all 115 records. Verify the 16 changed cells first, then the remaining fields; do not disclose their person-level details here.
4. Use a discrepancy log with fields: study ID, variable, source value, SAV value, resolution, reason, original-record locator and reviewer/date. Record UNKNOWN/NOT RECORDED/NOT APPLICABLE separately from zero or no.
5. Inspect the 99-item forms and scoring locally, honoring the existing restriction against LLM access. Return only aggregate scoring, missingness and reliability results.
6. After resolving discrepancies, freeze the audited dataset and regenerate one selected numerical manuscript/table version. Retain the original and the correction log; all authors should approve the final numerical source.

## What can be completed now

The computational check and missing-variable inventory are complete. True source-form validation and recovery of absent clinical variables remain with the authorized study team because the forms/clinical records have not been supplied and item-level responses must remain local. No paper-form values were fabricated or inferred.

## Provenance

- `upload/01-SOSYODEMOGRAFI-sspsdYGAP.sav` SHA256 `c9847b403a1b834662ff16c6b7ddb0b0f04bc3dbbdde381c72ef889dae4f1998`
- `upload/02-SOSYODEMOGRAFI-YGAP.sav` SHA256 `8460c3a6cd647852db1ae6fea78c0792ab49d47d4d4e429aa33a90c840b22026`
- `upload/01-YGAP-C-ALIS-MA-SON.docx` SHA256 `db2726b0b70446bcf4982618b1bd4403f6f8c77f157fb7b86c90ea358f3faf62`
- `upload/01_IJLP_Manuscript.docx` SHA256 `46865a1bfe2e521e75fc4ec8feb4103c60f4e063a8f310a9415435e82d869614`

- GitHub review source: https://github.com/Emrecavusoglu/ygap-study/tree/304d6ccaa664fbd9d34c281674ceacbf71a4cf05
- Verified code: https://github.com/Emrecavusoglu/ygap-study/blob/304d6ccaa664fbd9d34c281674ceacbf71a4cf05/analysis/reconcile_current.py
- Saved aggregates: https://github.com/Emrecavusoglu/ygap-study/blob/304d6ccaa664fbd9d34c281674ceacbf71a4cf05/analysis/generated/current_results.json
