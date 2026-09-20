# Focal effect sizes — 20 September 2026

Exploratory addition during review. All 91 patient records retained. No imputation, recoding, synthetic participants, or item-level access. Positive values mean higher forensic inpatient scores.

| Dimension | Hedges g | Pointwise bootstrap 95% CI | Raw difference | Games–Howell 95% CI | Holm p across five dimensions |
|---|---:|---|---:|---|---:|
| Depressive | -0.600 | -1.091 to -0.156 | -2.589 | -5.031 to -0.147 | 0.142 |
| Cyclothymic | -0.001 | -0.442 to 0.440 | -0.007 | -2.885 to 2.871 | 1.000 |
| Hyperthymic | 0.457 | -0.013 to 0.951 | 2.275 | -0.719 to 5.270 | 0.493 |
| Irritable | 0.748 | 0.320 to 1.261 | 3.456 | 1.059 to 5.853 | 0.015 |
| Anxious | -0.444 | -0.946 to 0.018 | -2.199 | -5.079 to 0.681 | 0.493 |

Hedges g uses the sample-size-weighted pooled within-group SD and the exact gamma-function small-sample correction (df = 89). It describes a standardized difference; unequal variances limit a common-SD interpretation. Raw differences and their Games–Howell intervals remain the principal interpretable estimates.

Uncertainty for g: percentile nonparametric bootstrap, 20,000 independent within-group row resamples, NumPy default_rng seed 20260920. These intervals are pointwise, exploratory, and not multiplicity-adjusted. Their zero exclusion must not replace the Holm-adjusted inference. Games–Howell intervals account for three pairwise group comparisons within each dimension, not all five dimensions.

The script checks agreement with the previously verified summary statistics and sign reversal on exchanging groups. Bootstrap samples are computational resamples of observed records, not generated study observations. No effect-size thresholds or causal interpretation are assigned.

Methodological background: [Lakens (2013)](https://doi.org/10.3389/fpsyg.2013.00863). This source supports transparent standardized-effect reporting; the bootstrap settings are our explicitly documented review-stage choice.

Source SHA256: `46527ae60ab4a1eb6e99ed0956aad63a81e42a3a9a1a1422ee382ac2364cd44e`. Reproduce: `python analysis/effect_sizes.py`.
