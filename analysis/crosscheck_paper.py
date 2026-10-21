"""Read original SAV and DOCX; generate aggregate cell-by-cell paper comparison.
Run from repository root: python analysis/crosscheck_paper.py
No participant records are exported, removed or recoded.
"""
from pathlib import Path
import json, re, hashlib, zipfile, importlib.metadata, xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import pyreadstat
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
sav=next(ROOT.glob('*.sav')); doc=next(ROOT.glob('*.docx'))
d,meta=pyreadstat.read_sav(sav)
xml=ET.fromstring(zipfile.ZipFile(doc).read('word/document.xml'))
tables=[[[ ''.join(t.text or '' for t in c.findall('.//w:t',ns)) for c in row.findall('w:tc',ns)] for row in table.findall('w:tr',ns)] for table in xml.findall('.//w:tbl',ns)]
groups=[1,3,2]; names={1:'YGAP',3:'Outpatient',2:'Control'}
variables=['yas','depres','siklotimi','hipertimi','irritable','anksiyöz']
labels=['Age','Depressive','Cyclothymic','Hyperthymic','Irritable','Anxious']
fmt=lambda p:'<.001' if p<.001 else f'{p:.3f}'
lines=['# Fresh SAV-to-manuscript cross-check','',
'Original Turkish DOCX tables were extracted directly from Word XML and compared with a fresh read of the repository SAV. No data were changed. Group/ordinary demographic labels follow the manuscript provisionally; diagnosis codes are not assigned clinical labels.','',
'## Input provenance','',f'- SAV SHA256: `{hashlib.sha256(sav.read_bytes()).hexdigest()}`',f'- DOCX SHA256: `{hashlib.sha256(doc.read_bytes()).hexdigest()}`',
'- Runtime versions: '+', '.join(f'{k}={importlib.metadata.version(k)}' for k in ['numpy','pandas','scipy','pyreadstat']),f'- Rows: {len(d)}; columns: {len(d.columns)}. Value labels: {meta.variable_value_labels}. User-defined missing ranges: {meta.missing_ranges}.','',
'## Every continuous descriptive cell','',
'Expected values use conventional rounding to two decimals and sample SD (denominator n−1). Small differences often reflect truncation; they do not by themselves establish different source data.','',
'| Measure | Group | Original Word table | Fresh mean ± SD | Assessment |','|---|---|---|---|---|']
manual_checks=[]
for i,(v,label) in enumerate(zip(variables,labels)):
 arrays=[d.loc[d.grup==g,v].dropna().to_numpy() for g in groups]
 row=tables[0][1] if i==0 else tables[1][i]
 for j,(g,a) in enumerate(zip(groups,arrays)):
  original=row[j+1]; expected=f'{a.mean():.2f}±{a.std(ddof=1):.2f}'
  clean=original.replace('*','').replace(' ','')
  lines.append(f'| {label} | {names[g]} | {original} | {expected} | {"Agrees" if clean==expected else "Correct displayed value"} |')
 # Independently compute classical F from sums of squares.
 allx=np.concatenate(arrays);grand=allx.mean()
 ssb=sum(len(a)*(a.mean()-grand)**2 for a in arrays);ssw=sum(((a-a.mean())**2).sum() for a in arrays)
 f=(ssb/2)/(ssw/(len(allx)-3));p=stats.f.sf(f,2,len(allx)-3)
 sf,sp=stats.f_oneway(*arrays)
 assert np.isclose(f,sf,rtol=1e-12) and np.isclose(p,sp,rtol=1e-10)
 manual_checks.append((label,f,p))
lines+=['','## Omnibus tests, independently checked from sums of squares','','| Measure | Original table F / p | Fresh F(2,112) | Fresh p |','|---|---|---|---|']
for i,(label,f,p) in enumerate(manual_checks):
 orig=tables[0][1][4] if i==0 else ' / '.join(tables[1][i][4:6])
 lines.append(f'| {label} | {orig} | {f:.3f} | {fmt(p)} |')
lines+=['','All six manual sums-of-squares F calculations agree with scipy ANOVA. The original narrative gives cyclothymic F=16.126; Table 2 gives 16.413; neither matches the fresh 16.418. A printed .000 p-value should be <.001. Hyperthymic .810 should be .081.','','## Every categorical cell in Table 1','','Percentages use the full group denominator (66, 25, 24). Labels are based on the manuscript and remain subject to codebook confirmation. Original dashes are interpreted as zero only where the SAV confirms zero.','','| Variable/category | Group | Original cell | Fresh n (%) | Check |','|---|---|---|---|---|']
mapping=[('egi',1,3),('egi',2,4),('egi',3,5),('egi',4,6),('med',1,8),('med',2,9),('med',3,10),('is',1,12),('is',2,13),('varyok',1,15),('varyok',0,16)]
for v,c,idx in mapping:
 for j,g in enumerate(groups):
  n=int(((d.grup==g)&(d[v]==c)).sum());den=int((d.grup==g).sum());pct=100*n/den;orig=tables[0][idx][j+1]
  found=re.fullmatch(r'(\d+)\(%([\d.]+)\)',orig)
  status='Zero confirmed' if n==0 and not found else 'Review format'
  if found:
   count,perc=found.groups(); decimals=len(perc.split('.')[1]) if '.' in perc else 0
   status='Agrees at printed precision' if int(count)==n and abs(float(perc)-round(pct,decimals))<1e-8 else 'Mismatch'
  lines.append(f'| {v}, code {c} ({tables[0][idx][0]}) | {names[g]} | {orig} | {n} ({pct:.1f}%) | {status} |')
lines+=['','Employment code 3 is absent from the paper: YGAP 1/66 (1.5%), outpatients 0, controls 0. It is not declared missing in the SAV. The 24 unemployed YGAP records represent 36.4%, not 37.4%. Do not omit the third category or relabel it without confirmation.','','## Categorical inference','','| Variable | Pearson χ² | df | p | Cells expected <5 |','|---|---|---|---|---|']
for v in ['med','is','egi','varyok','tanı']:
 t=pd.crosstab(d.grup,d[v]);chi,p,df,e=stats.chi2_contingency(t,correction=False)
 lines.append(f'| {v} | {chi:.3f} | {df} | {fmt(p)} | {(e<5).sum()}/{e.size} |')
lines+=['','These are reproduced Pearson results, not final endorsement of sparse-table inference. The employment table as stored has three categories and p=.003. The narrative χ²=15.2 is also inconsistent with Table 1 and the SAV (15.924). Omnibus tests do not identify each patient-control contrast.','','## Diagnosis percentages cannot be recovered by relabeling alone','','| Group | Code 1 | Code 2 | Code 3 | Code 4 |','|---|---|---|---|---|']
for g in [1,3]:
 den=int((d.grup==g).sum()); vals=[int(((d.grup==g)&(d['tanı']==c)).sum()) for c in [1,2,3,4]]
 lines.append('| '+names[g]+' | '+' | '.join(f'{n} ({100*n/den:.1f}%)' for n in vals)+' |')
lines+=['','The original three diagnosis percentages are 29.4/51.5/19.1 for YGAP and 18.4/52.3/29.4 for outpatients. For n=25, percentages must be multiples of 4%: none of the three outpatient percentages can arise from whole-person counts with that denominator. Confirm whether the text used another sample or denominator. Do not infer clinical labels from proportions.','','## All temperament pairwise comparisons','','Tukey tests reproduce the original equal-variance procedure; differences are first group minus second. Within each dimension p-values account for its three group comparisons, not for all five dimensions.','','| Dimension | Comparison | Mean difference | Tukey p | 95% simultaneous CI |','|---|---|---|---|---|']
for v,label in zip(variables[1:],labels[1:]):
 arrays=[d.loc[d.grup==g,v].to_numpy() for g in groups];res=stats.tukey_hsd(*arrays);ci=res.confidence_interval()
 for i,j in [(0,1),(0,2),(1,2)]:
  lines.append(f'| {label} | {names[groups[i]]} − {names[groups[j]]} | {arrays[i].mean()-arrays[j].mean():.3f} | {fmt(res.pvalue[i,j])} | {ci.low[i,j]:.3f} to {ci.high[i,j]:.3f} |')
lines+=['','Forensic–outpatient depressive and irritable pooled standard errors are checked below. SE is uncertainty in a contrast, not the magnitude of the group difference.','']
for v in ['depres','irritable']:
 a=[d.loc[d.grup==g,v].to_numpy() for g in groups];mse=sum(((x-x.mean())**2).sum() for x in a)/(len(d)-3);se=np.sqrt(mse*(1/len(a[0])+1/len(a[1])))
 lines.append(f'- {v}: pooled contrast SE={se:.6f}.')
lines+=['','## Normality recheck','','Shapiro–Wilk is a complementary fresh check. The original claim specifically about Kolmogorov–Smirnov is already contradicted by archived OUTPUT2 page 15. A naive KS test against a fitted normal distribution is not substituted here for SPSS Lilliefors-corrected results.','','| Variable | YGAP Shapiro p | Outpatient Shapiro p | Control Shapiro p |','|---|---|---|---|']
for v in variables:lines.append('| '+v+' | '+' | '.join(fmt(stats.shapiro(d.loc[d.grup==g,v]).pvalue) for g in groups)+' |')
lines+=['','Normality rejection alone does not establish that a mean comparison is unusable. See the existing Welch/Games–Howell and Kruskal–Wallis sensitivity analyses in [RESULTS.md](generated/RESULTS.md). The exploratory across-dimension Holm adjustment is not part of the original paper and must not be presented as prespecified.','','## Data integrity and interpretation','',f'- Fully repeated profiles beyond first occurrences: {int(d.duplicated().sum())}. No participant identifier exists; this is not proof of repeated participants. No rows removed.',
f'- All-empty columns: {", ".join(d.columns[d.isna().all()])}. Missing diagnosis entries: {int(d["tanı"].isna().sum())}; all belong to controls.',
'- No missing values in age or the five temperament scores. All temperament scores lie within the maxima described in the manuscript; item-level scoring cannot be checked.',
'- Original Results paragraph correctly says depressive scores are higher in outpatients. Original Discussion reverses this direction. Both cannot be retained.',
'- The original education narrative is also inaccurate for outpatients: high school is the largest category (13/25, 52%), while primary plus middle school is 10/25 (40%).',
'- Irritable-score elevation is a between-group association. Offense causation, future violence, illness course and medication mechanisms were not tested.',
'- This cross-check does not add new participants, infer diagnosis labels, or replace unresolved recruitment details.','']
assert all(d[v].between(0,m).all() for v,m in zip(variables[1:],[18,19,20,18,24]))
(ROOT/'analysis/PAPER_CROSSCHECK.md').write_text('\n'.join(lines))
print('Wrote analysis/PAPER_CROSSCHECK.md; six independent F checks passed; 18 descriptive cells, 33 categorical cells and 15 temperament contrasts compared.')
