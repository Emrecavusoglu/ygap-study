* Encoding: UTF-8.
* Analiz ayarları.
FILTER OFF.
USE ALL.
WEIGHT OFF.
SPLIT FILE OFF.

* Değişken türleri.
VARIABLE LEVEL yas depres siklotimi hipertimi irritable anksiyöz (SCALE).
VARIABLE LEVEL grup (NOMINAL).

* Kodların ve eksik verilerin kontrolü.
FREQUENCIES VARIABLES=grup med is tanı egi varyok.

* Dağılımlar, uç değerler ve normallik kontrolleri.
EXAMINE VARIABLES=yas depres siklotimi hipertimi irritable anksiyöz BY grup
 /PLOT BOXPLOT HISTOGRAM NPPLOT
 /STATISTICS DESCRIPTIVES EXTREME
 /CINTERVAL 95
 /MISSING PAIRWISE
 /NOTOTAL.

* Klasik ve Welch ANOVA ile ikili karşılaştırmalar.
ONEWAY yas depres siklotimi hipertimi irritable anksiyöz BY grup
 /STATISTICS DESCRIPTIVES HOMOGENEITY WELCH
 /MISSING ANALYSIS
 /POSTHOC=TUKEY GH ALPHA(0.05).

* Demografik karşılaştırmalar.
CROSSTABS
 /TABLES=grup BY med is egi varyok tanı
 /STATISTICS=CHISQ PHI
 /CELLS=COUNT ROW EXPECTED.
NPAR TESTS
 /K-W=yas depres siklotimi hipertimi irritable anksiyöz BY grup(1 3)
 /MISSING ANALYSIS.
