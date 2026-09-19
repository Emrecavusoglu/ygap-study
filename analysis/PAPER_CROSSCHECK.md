# Fresh SAV-to-manuscript cross-check

Original Turkish DOCX tables were extracted directly from Word XML and compared with a fresh read of the repository SAV. No data were changed. Group/ordinary demographic labels follow the manuscript provisionally; diagnosis codes are not assigned clinical labels.

## Input provenance

- SAV SHA256: `46527ae60ab4a1eb6e99ed0956aad63a81e42a3a9a1a1422ee382ac2364cd44e`
- DOCX SHA256: `db2726b0b70446bcf4982618b1bd4403f6f8c77f157fb7b86c90ea358f3faf62`
- Runtime versions: numpy=2.3.5, pandas=2.2.3, scipy=1.17.0, pyreadstat=1.3.6
- Rows: 115; columns: 13. Value labels: {}. User-defined missing ranges: {}.

## Every continuous descriptive cell

Expected values use conventional rounding to two decimals and sample SD (denominator n−1). Small differences often reflect truncation; they do not by themselves establish different source data.

| Measure | Group | Original Word table | Fresh mean ± SD | Assessment |
|---|---|---|---|---|
| Age | YGAP | 39.31±10.67 | 39.32±10.68 | Correct displayed value |
| Age | Outpatient | 39.72±8.12 | 39.72±8.32 | Correct displayed value |
| Age | Control | 37.00±7.27 | 37.00±7.27 | Agrees |
| Depressive | YGAP | 10.09±4.27 | 10.09±4.27 | Agrees |
| Depressive | Outpatient | 12.66±4.28 | 12.68±4.29 | Correct displayed value |
| Depressive | Control | 3.79±3.02* | 3.79±3.02 | Agrees |
| Cyclothymic | YGAP | 11.27±5.33 | 11.27±5.34 | Correct displayed value |
| Cyclothymic | Outpatient | 11.28±4.95 | 11.28±4.95 | Agrees |
| Cyclothymic | Control | 4.70±3.91* | 4.71±3.92 | Correct displayed value |
| Hyperthymic | YGAP | 12.51±4.75 | 12.52±4.76 | Correct displayed value |
| Hyperthymic | Outpatient | 10.24±5.40 | 10.24±5.40 | Agrees |
| Hyperthymic | Control | 10.95±3.19 | 10.96±3.20 | Correct displayed value |
| Irritable | YGAP | 11.57±4.75** | 11.58±4.78 | Correct displayed value |
| Irritable | Outpatient | 8.12±4.00 | 8.12±4.00 | Agrees |
| Irritable | Control | 2.29±1.82 | 2.29±1.83 | Correct displayed value |
| Anxious | YGAP | 10.12±4.83 | 10.12±4.83 | Agrees |
| Anxious | Outpatient | 12.32±5.12 | 12.32±5.12 | Agrees |
| Anxious | Control | 3.37±3.89* | 3.38±3.90 | Correct displayed value |

## Omnibus tests, independently checked from sums of squares

| Measure | Original table F / p | Fresh F(2,112) | Fresh p |
|---|---|---|---|
| Age | F=0.626p=0.537 | 0.626 | 0.537 |
| Depressive | 32.126 / 0.000 | 32.126 | <.001 |
| Cyclothymic | 16.413 / 0.000 | 16.418 | <.001 |
| Hyperthymic | 2.568 / 0.810 | 2.568 | 0.081 |
| Irritable | 44.248 / 0.000 | 44.248 | <.001 |
| Anxious | 24.966 / 0.000 | 24.966 | <.001 |

All six manual sums-of-squares F calculations agree with scipy ANOVA. The original narrative gives cyclothymic F=16.126; Table 2 gives 16.413; neither matches the fresh 16.418. A printed .000 p-value should be <.001. Hyperthymic .810 should be .081.

## Every categorical cell in Table 1

Percentages use the full group denominator (66, 25, 24). Labels are based on the manuscript and remain subject to codebook confirmation. Original dashes are interpreted as zero only where the SAV confirms zero.

| Variable/category | Group | Original cell | Fresh n (%) | Check |
|---|---|---|---|---|
| egi, code 1 (İlkokul) | YGAP | 9(%13.6) | 9 (13.6%) | Agrees at printed precision |
| egi, code 1 (İlkokul) | Outpatient | ------ | 0 (0.0%) | Zero confirmed |
| egi, code 1 (İlkokul) | Control | ----- | 0 (0.0%) | Zero confirmed |
| egi, code 2 (Ortaokul) | YGAP | 33(%50) | 33 (50.0%) | Agrees at printed precision |
| egi, code 2 (Ortaokul) | Outpatient | 10(%40) | 10 (40.0%) | Agrees at printed precision |
| egi, code 2 (Ortaokul) | Control | 9(%37.5) | 9 (37.5%) | Agrees at printed precision |
| egi, code 3 (Lise) | YGAP | 18(%27.2) | 18 (27.3%) | Mismatch |
| egi, code 3 (Lise) | Outpatient | 13(%52) | 13 (52.0%) | Agrees at printed precision |
| egi, code 3 (Lise) | Control | 14(%58.3) | 14 (58.3%) | Agrees at printed precision |
| egi, code 4 (Üni-yüksekokul) | YGAP | 6(%9.2) | 6 (9.1%) | Mismatch |
| egi, code 4 (Üni-yüksekokul) | Outpatient | 2(%8) | 2 (8.0%) | Agrees at printed precision |
| egi, code 4 (Üni-yüksekokul) | Control | 1(%4.2) | 1 (4.2%) | Agrees at printed precision |
| med, code 1 (Bekar) | YGAP | 44(%66.7) | 44 (66.7%) | Agrees at printed precision |
| med, code 1 (Bekar) | Outpatient | 13(%52) | 13 (52.0%) | Agrees at printed precision |
| med, code 1 (Bekar) | Control | 3(%12.5) | 3 (12.5%) | Agrees at printed precision |
| med, code 2 (Evli) | YGAP | 15(%22.8) | 15 (22.7%) | Mismatch |
| med, code 2 (Evli) | Outpatient | 10(%40) | 10 (40.0%) | Agrees at printed precision |
| med, code 2 (Evli) | Control | 21(%87.5) | 21 (87.5%) | Agrees at printed precision |
| med, code 3 (Dul-boşanmış) | YGAP | 7(%10.6) | 7 (10.6%) | Agrees at printed precision |
| med, code 3 (Dul-boşanmış) | Outpatient | 2(%8) | 2 (8.0%) | Agrees at printed precision |
| med, code 3 (Dul-boşanmış) | Control | ------ | 0 (0.0%) | Zero confirmed |
| is, code 1 (Çalışıyor) | YGAP | 41(%62.1) | 41 (62.1%) | Agrees at printed precision |
| is, code 1 (Çalışıyor) | Outpatient | 13(%52) | 13 (52.0%) | Agrees at printed precision |
| is, code 1 (Çalışıyor) | Control | 24(%100) | 24 (100.0%) | Agrees at printed precision |
| is, code 2 (Çalışmıyor) | YGAP | 24(%37.4) | 24 (36.4%) | Mismatch |
| is, code 2 (Çalışmıyor) | Outpatient | 12(%48) | 12 (48.0%) | Agrees at printed precision |
| is, code 2 (Çalışmıyor) | Control | ------ | 0 (0.0%) | Zero confirmed |
| varyok, code 1 (Var) | YGAP | 35(%53.03) | 35 (53.0%) | Agrees at printed precision |
| varyok, code 1 (Var) | Outpatient | 15(%60) | 15 (60.0%) | Agrees at printed precision |
| varyok, code 1 (Var) | Control | 24(%100) | 24 (100.0%) | Agrees at printed precision |
| varyok, code 0 (Yok) | YGAP | 31(%46.96) | 31 (47.0%) | Mismatch |
| varyok, code 0 (Yok) | Outpatient | 10(%40) | 10 (40.0%) | Agrees at printed precision |
| varyok, code 0 (Yok) | Control | ------ | 0 (0.0%) | Zero confirmed |

Employment code 3 is absent from the paper: YGAP 1/66 (1.5%), outpatients 0, controls 0. It is not declared missing in the SAV. The 24 unemployed YGAP records represent 36.4%, not 37.4%. Do not omit the third category or relabel it without confirmation.

## Categorical inference

| Variable | Pearson χ² | df | p | Cells expected <5 |
|---|---|---|---|---|
| med | 30.889 | 4 | <.001 | 2/9 |
| is | 15.924 | 4 | 0.003 | 3/9 |
| egi | 13.720 | 6 | 0.033 | 4/12 |
| varyok | 17.188 | 2 | <.001 | 0/6 |
| tanı | 3.793 | 3 | 0.285 | 3/8 |

These are reproduced Pearson results, not final endorsement of sparse-table inference. The employment table as stored has three categories and p=.003. The narrative χ²=15.2 is also inconsistent with Table 1 and the SAV (15.924). Omnibus tests do not identify each patient-control contrast.

## Diagnosis percentages cannot be recovered by relabeling alone

| Group | Code 1 | Code 2 | Code 3 | Code 4 |
|---|---|---|---|---|
| YGAP | 28 (42.4%) | 29 (43.9%) | 7 (10.6%) | 2 (3.0%) |
| Outpatient | 12 (48.0%) | 13 (52.0%) | 0 (0.0%) | 0 (0.0%) |

The original three diagnosis percentages are 29.4/51.5/19.1 for YGAP and 18.4/52.3/29.4 for outpatients. For n=25, percentages must be multiples of 4%: none of the three outpatient percentages can arise from whole-person counts with that denominator. Confirm whether the text used another sample or denominator. Do not infer clinical labels from proportions.

## All temperament pairwise comparisons

Tukey tests reproduce the original equal-variance procedure; differences are first group minus second. Within each dimension p-values account for its three group comparisons, not for all five dimensions.

| Dimension | Comparison | Mean difference | Tukey p | 95% simultaneous CI |
|---|---|---|---|---|
| Depressive | YGAP − Outpatient | -2.589 | 0.020 | -4.849 to -0.329 |
| Depressive | YGAP − Control | 6.299 | <.001 | 4.005 to 8.593 |
| Depressive | Outpatient − Control | 8.888 | <.001 | 6.138 to 11.639 |
| Cyclothymic | YGAP − Outpatient | -0.007 | 1.000 | -2.793 to 2.778 |
| Cyclothymic | YGAP − Control | 6.564 | <.001 | 3.737 to 9.392 |
| Cyclothymic | Outpatient − Control | 6.572 | <.001 | 3.182 to 9.961 |
| Hyperthymic | YGAP − Outpatient | 2.275 | 0.096 | -0.310 to 4.861 |
| Hyperthymic | YGAP − Control | 1.557 | 0.340 | -1.067 to 4.181 |
| Hyperthymic | Outpatient − Control | -0.718 | 0.851 | -3.864 to 2.428 |
| Irritable | YGAP − Outpatient | 3.456 | 0.002 | 1.132 to 5.780 |
| Irritable | YGAP − Control | 9.284 | <.001 | 6.925 to 11.643 |
| Irritable | Outpatient − Control | 5.828 | <.001 | 3.001 to 8.656 |
| Anxious | YGAP − Outpatient | -2.199 | 0.121 | -4.833 to 0.436 |
| Anxious | YGAP − Control | 6.746 | <.001 | 4.072 to 9.420 |
| Anxious | Outpatient − Control | 8.945 | <.001 | 5.739 to 12.151 |

Forensic–outpatient depressive and irritable pooled standard errors are checked below. SE is uncertainty in a contrast, not the magnitude of the group difference.

- depres: pooled contrast SE=0.951575.
- irritable: pooled contrast SE=0.978333.

## Normality recheck

Shapiro–Wilk is a complementary fresh check. The original claim specifically about Kolmogorov–Smirnov is already contradicted by archived OUTPUT2 page 15. A naive KS test against a fitted normal distribution is not substituted here for SPSS Lilliefors-corrected results.

| Variable | YGAP Shapiro p | Outpatient Shapiro p | Control Shapiro p |
|---|---|---|---|
| yas | 0.193 | 0.144 | 0.037 |
| depres | 0.183 | 0.069 | <.001 |
| siklotimi | 0.003 | 0.059 | <.001 |
| hipertimi | 0.034 | 0.024 | 0.021 |
| irritable | <.001 | 0.010 | 0.002 |
| anksiyöz | 0.077 | 0.016 | <.001 |

Normality rejection alone does not establish that a mean comparison is unusable. See the existing Welch/Games–Howell and Kruskal–Wallis sensitivity analyses in [RESULTS.md](generated/RESULTS.md). The exploratory across-dimension Holm adjustment is not part of the original paper and must not be presented as prespecified.

## Data integrity and interpretation

- Fully repeated profiles beyond first occurrences: 13. No participant identifier exists; this is not proof of repeated participants. No rows removed.
- All-empty columns: GELİR. Missing diagnosis entries: 24; all belong to controls.
- No missing values in age or the five temperament scores. All temperament scores lie within the maxima described in the manuscript; item-level scoring cannot be checked.
- Original Results paragraph correctly says depressive scores are higher in outpatients. Original Discussion reverses this direction. Both cannot be retained.
- The original education narrative is also inaccurate for outpatients: high school is the largest category (13/25, 52%), while primary plus middle school is 10/25 (40%).
- Irritable-score elevation is a between-group association. Offense causation, future violence, illness course and medication mechanisms were not tested.
- This cross-check does not add new participants, infer diagnosis labels, or replace unresolved recruitment details.
