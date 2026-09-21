"""Reproduce current aggregate tables without modifying/exporting participant records.
Usage: python analysis/reconcile_current.py /path/to/current.sav
The uploaded SAV is retained by the author; it is not newly published by this script.
"""
from pathlib import Path
import sys,json,hashlib,importlib.metadata
import numpy as np
import pandas as pd
import pyreadstat
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
EXPECTED='c9847b403a1b834662ff16c6b7ddb0b0f04bc3dbbdde381c72ef889dae4f1998'
G=[1,3,2]
V={'yas':'Age, years','depres':'Depressive','siklotimi':'Cyclothymic','hipertimi':'Hyperthymic','irritable':'Irritable','anksiyöz':'Anxious'}
def pstr(p):return '<.001' if p<.001 else f'{p:.3f}'.lstrip('0')
def run(path):
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==EXPECTED,'Unrecognized source version'
 d,_=pyreadstat.read_sav(path)
 assert len(d)==115 and [(d.grup==g).sum() for g in G]==[66,25,24]
 assert pd.crosstab(d.grup,d['tanı']).loc[[1,3]].values.tolist()==[[28,29,9],[9,13,3]]
 assert pd.crosstab(d.grup,d['is']).loc[[1,3,2]].values.tolist()==[[41,25],[13,12],[24,0]]
 out={'source_sha256':EXPECTED,'versions':{k:importlib.metadata.version(k) for k in ['numpy','pandas','scipy','pyreadstat']},'continuous':{},'categorical':{}}
 for v in V:
  a=[d.loc[d.grup==g,v].to_numpy() for g in G];assert all(np.isfinite(x).all() for x in a)
  f,p=stats.f_oneway(*a);t=stats.tukey_hsd(*a);ci=t.confidence_interval()
  out['continuous'][v]={'means':[float(x.mean()) for x in a],'sds':[float(x.std(ddof=1)) for x in a],'F':float(f),'p':float(p),'df':[2,112],'tukey_p':t.pvalue.tolist(),'tukey_differences':t.statistic.tolist(),'tukey_ci95_low':ci.low.tolist(),'tukey_ci95_high':ci.high.tolist()}
 for v in ['egi','med','is','varyok','tanı']:
  groups=[1,3] if v=='tanı' else G
  tab=pd.crosstab(d.grup,d[v]).loc[groups];c,p,df,e=stats.chi2_contingency(tab,correction=False)
  out['categorical'][v]={'groups':groups,'codes':list(map(int,tab.columns)),'counts':tab.values.tolist(),'chi2':float(c),'p':float(p),'df':int(df),'expected_below_5':int((e<5).sum()),'cells':int(e.size),'minimum_expected':float(e.min())}
 dest=ROOT/'analysis/generated';(dest/'current_results.json').write_text(json.dumps(out,indent=2)+'\n')
 lines=['# Tables — reconciled current dataset','','Group order throughout: forensic inpatients (n=66), psychiatric outpatients (n=25), healthy controls (n=24). Values are n (%) unless otherwise stated. Percentages use each group denominator; rounding may prevent sums of exactly 100%.','','## Table 1. Participant characteristics','','| Characteristic | Forensic inpatients | Outpatients | Controls | Test | p |','|---|---:|---:|---:|---|---:|']
 a=out['continuous']['yas'];vals=[f'{m:.2f} ± {s:.2f}' for m,s in zip(a['means'],a['sds'])];lines.append('| Age, mean ± SD | '+' | '.join(vals)+f" | F(2,112)={a['F']:.3f} | {pstr(a['p'])} |")
 labels={'egi':['Primary school','Middle school','High school','College/university'],'med':['Single','Married','Widowed/divorced'],'is':['Employed','Not employed'],'varyok':['No coverage','Coverage']}
 headers={'egi':'Education','med':'Marital status','is':'Employment','varyok':'Social security coverage'}
 for v in labels:
  x=out['categorical'][v];lines.append(f"| **{headers[v]}** | | | | χ²({x['df']})={x['chi2']:.3f} | {pstr(x['p'])} |")
  for j,l in enumerate(labels[v]):
   vals=[f'{row[j]} ({100*row[j]/n:.1f})' for row,n in zip(x['counts'],[66,25,24])];lines.append('| '+l+' | '+' | '.join(vals)+' | | |')
 lines+=['','Pearson chi-square tests are omnibus, not pairwise. Education: 4/12 expected cells <5; marital status: 2/9 <5; minimum expected count 1.88 in both. These p-values are approximate and interpreted cautiously. Employment and social-security tables have no expected count <5. No Monte Carlo test was performed. Employment concerns pre-admission/stable-period status, not work during forensic hospitalization.','','## Table 2. Diagnostic distribution in patient groups','','| Diagnosis | Forensic inpatients, n (%) | Outpatients, n (%) |','|---|---:|---:|']
 x=out['categorical']['tanı']
 for j,l in enumerate(['Paranoid schizophrenia','Other schizophrenia subtypes and atypical psychosis','Bipolar affective disorder']):
  lines.append('| '+l+' | '+' | '.join(f'{row[j]} ({100*row[j]/n:.1f})' for row,n in zip(x['counts'],[66,25]))+' |')
 lines+=['','Diagnosis codes follow the supervisor-provided definitions. Combined patient counts are 37, 42 and 12, matching the supplied frequency screenshot. Controls are not included in diagnostic denominators. No formal equivalence or diagnostic matching is inferred from these distributions.','','## Table 3. TEMPS-A subscale scores and group comparisons','','| Dimension | Forensic, mean ± SD | Outpatient, mean ± SD | Control, mean ± SD | F(2,112) | Omnibus p | Tukey p: forensic–outpatient |','|---|---:|---:|---:|---:|---:|---:|']
 for v,l in V.items():
  if v=='yas':continue
  x=out['continuous'][v];vals=[f'{m:.2f} ± {s:.2f}' for m,s in zip(x['means'],x['sds'])]
  lines.append('| '+l+' | '+' | '.join(vals)+f" | {x['F']:.3f} | {pstr(x['p'])} | {pstr(x['tukey_p'][0][1])} |")
 lines+=['','Both patient groups score higher than controls in depressive, cyclothymic, irritable and anxious dimensions (each Tukey p<.001). No hyperthymic pairwise contrast is significant. Tukey adjustment covers the three group comparisons within each dimension; there is no adjustment across all five dimensions.','','## Table 4. Focal raw-score differences with Tukey 95% confidence intervals','','| Dimension | Forensic minus outpatient | Tukey 95% CI |','|---|---:|---|']
 for v,l in V.items():
  if v=='yas':continue
  x=out['continuous'][v];lines.append(f"| {l} | {x['tukey_differences'][0][1]:.2f} | {x['tukey_ci95_low'][0][1]:.2f} to {x['tukey_ci95_high'][0][1]:.2f} |")
 lines+=['','Confidence intervals were calculated during manuscript revision from the current supplied dataset using the same classical ANOVA/Tukey framework; they are not presented as copied from the original SPSS output. No standardized effect size or additional sensitivity analysis is included in the primary report.']
 (ROOT/'manuscript/TABLES.md').write_text('\n'.join(lines)+'\n')
 print('Current aggregate results and tables generated; source unchanged:',hashlib.sha256(path.read_bytes()).hexdigest()==EXPECTED)
if __name__=='__main__':run(Path(sys.argv[1]))
