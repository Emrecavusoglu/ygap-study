# Phase 2 — Finalize and cross-check results

Status: numerical reproduction completed; final analysis and source-record gates remain open.

## Verification performed

The existing Python analysis was rerun into a separate temporary directory. Its complete aggregate JSON matched the committed results exactly. All five archived-output assertions passed. These are replication checks, not proof that the chosen model or input records are valid. No observations were removed or recoded.

Source mapping: OUTPUT2 page 15 normality, page 49 variance tests, page 50 ANOVA/Welch, pages 51–54 pairwise comparisons, pages 58–62 categorical results, page 126 Kruskal–Wallis. Page 15 was additionally inspected visually in this extension. The earlier OUTPUT.pdf was not fully reconciled.

[Complete estimates, SDs, tests and confidence intervals](../../analysis/generated/RESULTS.md) and [full-precision JSON](../../analysis/generated/results.json) are the numerical record. Group codes are 1 forensic (66), 2 controls (24), 3 outpatients (25), inferred from manuscript/sample sizes; clinical diagnosis codes remain unknown.

## Corrections to the submitted text

| Finding | Verified result | Required correction |
|---|---|---|
| Sample | 66 + 25 + 24 = 115 | Retain; distinct-person verification pending |
| Depressive scores | Forensic 10.09 ± 4.27; outpatient 12.68 ± 4.29 | Outpatients score higher; reverse the original Discussion |
| Irritable scores | Forensic 11.58 ± 4.78; outpatient 8.12 ± 4.00 | Higher forensic score supported; original SD 4.75 inaccurate |
| Outpatient age SD | 8.32 | Replace table's 8.12 |
| Cyclothymic F | 16.418 | Replace 16.126/16.413 |
| Hyperthymic ANOVA | F(2,112)=2.568, p=.081 | Replace .810; nonsignificance does not prove equivalence |
| Employment | χ²(4)=15.924, p=.003 | Replace <.001; retain unexplained third category |
| Education | χ²(6)=13.720, p=.033 | Sparse cells make asymptotic inference provisional; p does not measure effect size |
| Marital status | χ²(4)=30.889, p<.001 | Overall test does not identify each pairwise difference |
| Social-security proxy | χ²(2)=17.188, p<.001 | Confirm varyok label; do not call this income |
| Zero p-values | No p-value equals zero | Report SPSS .000 as p<.001; never p<.000 |

## Distribution and variance assumptions

The statement that all continuous variables were normally distributed is false according to the archived tests. On page 15, Kolmogorov–Smirnov p<.001 for control depressive, cyclothymic, irritable and anxious scores; forensic hyperthymic p=.003 and irritable p<.001; outpatient hyperthymic p=.010 and anxious p=.015. Normality tests alone should not dictate model selection; inspect distributions, bounded scales, group sizes and variance differences together.

Mean-centered Levene p-values are .041 for age, .309 depressive, .045 cyclothymic, .013 hyperthymic, <.001 irritable and .064 anxious. Welch and Games–Howell address unequal variances; they do not repair dependence, selection bias, confounding or all distributional problems.

Kruskal–Wallis reproduces page 126: age H=1.648, p=.439; depressive 40.310, p<.001; cyclothymic 26.191, p<.001; hyperthymic 4.314, p=.116; irritable 50.496, p<.001; anxious 36.866, p<.001. This supports the overall pattern under a rank-based sensitivity analysis. It is not a verification of each pairwise mean difference and must not automatically be described as a median test.

## Focal comparisons and multiplicity

Forensic minus outpatient irritable mean difference is +3.456; Tukey p=.002; Games–Howell p=.003, simultaneous within-dimension 95% CI 1.059–5.853. Depressive difference is −2.589; Tukey p=.020; Games–Howell p=.036, CI −5.031 to −.147. Other patient-group comparisons are nonsignificant. Both patient groups exceed controls for the four nonhyperthymic dimensions in within-dimension comparisons.

Exploratory Holm correction across five focal Games–Howell comparisons gives irritable p=.015 and depressive p=.142. This conservative additional sensitivity was introduced during review, not prespecified. Its family does not include every demographic test or every patient–control contrast. Authors must specify the primary question and reporting hierarchy without selecting methods to obtain significance.

## Data gates

- Diagnosis codes 1/2/3/4: forensic 28/29/7/2; outpatients 12/13/0/0. Published percentages do not follow these counts. Clinical labels cannot be guessed. The percentages reported for 25 outpatients also do not correspond to whole-person counts.
- Employment: forensic 41/24/1, not 41/24 plus a missing observation. Code 3 needs a label.
- All 115 GELİR entries are missing. Diagnosis is absent in 24 controls. No missing continuous scores were found.
- Thirteen complete profiles repeat earlier profiles. This is a source-record check, not proof of duplicate participants; do not delete them automatically.
- Small expected counts affect marital, employment, education and diagnosis tables. Select exact/Monte Carlo procedures after meanings are confirmed; do not collapse categories for significance.
- Item-level scoring, internal consistency, symptom severity, substance exposure and adjusted diagnosis analyses cannot be audited from these 13 columns.

## Exit condition

Supervisor confirms code meanings, distinct participants and recruitment facts; authors agree the primary/sensitivity analysis hierarchy and sparse-table treatment. Then regenerate the tables and integrate one consistent Methods/Results account. No paid SPSS license is needed for the reproduced analyses.

## Revision checkpoint — 20 September 2026

Effect sizes are now computed from the unchanged SAV: see [report](../../analysis/generated/EFFECT_SIZES.md). Repeated profiles are author-confirmed distinct; this closes the author query, not an independent source-record audit. Diagnosis/employment labels and the final inferential hierarchy remain open.
