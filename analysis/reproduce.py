"""Reproduce aggregate YGAP results without modifying or exporting participant rows.

Run from repository root: python analysis/reproduce.py
Group labels inferred from unique sample sizes and manuscript tables; categorical
code meanings are not invented. This is an audit, not an approved analysis plan.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import itertools
import json
import numpy as np
import pandas as pd
import pyreadstat
from scipy import stats
from statsmodels.stats.oneway import anova_oneway
from statsmodels.stats.multitest import multipletests

ROOT = Path(__file__).resolve().parents[1]
NAMES = {1: 'Forensic inpatients', 3: 'Psychiatric outpatients', 2: 'Controls'}
VARIABLES = {'yas': 'Age', 'depres': 'Depressive temperament',
             'siklotimi': 'Cyclothymic temperament', 'hipertimi': 'Hyperthymic temperament',
             'irritable': 'Irritable temperament', 'anksiyöz': 'Anxious temperament'}

def run(path, out):
    d, meta = pyreadstat.read_sav(path)
    out.mkdir(parents=True, exist_ok=True)
    if set(d.grup.unique()) != {1, 2, 3}:
        raise ValueError('Unexpected group codes: review mapping before analysis')
    groups = [1, 3, 2]
    r = {'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
         'versions': {k: importlib.metadata.version(k) for k in ['numpy','pandas','scipy','statsmodels','pyreadstat']},
         'n': len(d), 'groups': {str(g): int((d.grup == g).sum()) for g in groups},
         'missing': {c: int(d[c].isna().sum()) for c in d},
         'value_labels': meta.variable_value_labels,
         'repeated_rows_beyond_first': int(d.duplicated().sum()),
         'continuous': {}, 'categorical': {}}
    for v, label in VARIABLES.items():
        a = [d.loc[d.grup == g, v].dropna().to_numpy() for g in groups]
        desc = [{'group': g, 'n': len(x), 'mean': float(x.mean()), 'sd': float(x.std(ddof=1)),
                 'min': float(x.min()), 'max': float(x.max())} for g,x in zip(groups,a)]
        f,p = stats.f_oneway(*a)
        w = anova_oneway(a, use_var='unequal')
        lv = stats.levene(*a, center='mean')
        kw = stats.kruskal(*a)
        tk = stats.tukey_hsd(*a)
        ci = tk.confidence_interval()
        pairs = []
        for i,j in itertools.combinations(range(3),2):
            x,y = a[i],a[j]
            vx,vy = x.var(ddof=1)/len(x),y.var(ddof=1)/len(y)
            se = np.sqrt(vx+vy)
            df = (vx+vy)**2/(vx**2/(len(x)-1)+vy**2/(len(y)-1))
            diff = x.mean()-y.mean()
            q = abs(diff)/se*np.sqrt(2)
            gp = stats.studentized_range.sf(q,3,df)
            margin = stats.studentized_range.ppf(.95,3,df)*se/np.sqrt(2)
            pairs.append({'groups': [groups[i],groups[j]], 'difference_first_minus_second': float(diff),
                          'tukey_p': float(tk.pvalue[i,j]), 'tukey_ci95': [float(ci.low[i,j]),float(ci.high[i,j])],
                          'games_howell_p': float(gp), 'games_howell_df': float(df),
                          'games_howell_ci95': [float(diff-margin),float(diff+margin)]})
        r['continuous'][v] = {'label':label, 'descriptives':desc,
          'anova': {'F':float(f),'df':[2,sum(map(len,a))-3],'p':float(p)},
          'welch': {'F':float(w.statistic),'df':[float(z) for z in w.df],'p':float(w.pvalue)},
          'levene_mean': {'F':float(lv.statistic),'p':float(lv.pvalue)},
          'kruskal_wallis': {'H':float(kw.statistic),'p':float(kw.pvalue)}, 'pairs':pairs}
    for v in ['med','is','egi','varyok','tanı']:
        t = pd.crosstab(d.grup,d[v])
        chi,p,df,expected = stats.chi2_contingency(t, correction=False)
        r['categorical'][v] = {'groups': [int(x) for x in t.index], 'codes':[int(x) for x in t.columns],
          'counts':t.values.tolist(), 'chi2':float(chi),'df':int(df),'p':float(p),
          'minimum_expected':float(expected.min()), 'fraction_expected_below_5':float((expected<5).mean())}
    temperaments = [v for v in VARIABLES if v != 'yas']
    # Explicit exploratory sensitivity across the five focal forensic/outpatient comparisons.
    gh = [r['continuous'][v]['pairs'][0]['games_howell_p'] for v in temperaments]
    r['exploratory_holm_across_five_focal_dimensions'] = dict(zip(temperaments,map(float,multipletests(gh,method='holm')[1])))
    # Verify rounded values from OUTPUT2, pp 50, 51, 53, 59 (not source manuscript typos).
    checks = [abs(r['continuous']['depres']['anova']['F']-32.126)<.0005,
              abs(r['continuous']['siklotimi']['anova']['F']-16.418)<.0005,
              abs(r['continuous']['hipertimi']['anova']['p']-.081)<.0005,
              abs(r['continuous']['irritable']['pairs'][0]['games_howell_p']-.003)<.0005,
              abs(r['categorical']['is']['chi2']-15.924)<.0005]
    if not all(checks): raise AssertionError('Dataset differs from archived SPSS output; inspect before reporting')
    (out/'results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    def ptext(p): return '<.001' if p<.001 else f'{p:.3f}'
    lines = ['# Reproduced aggregate results','',
      'Source: repository SAV; generated by analysis/reproduce.py. No rows removed or recoded.',
      'Group labels inferred from manuscript and sample sizes. Numeric categorical codes require confirmation.',
      'Classical results reproduce the saved analysis; Welch/Games–Howell are reported as sensitivity results pending an agreed reporting plan.', '',
      '| Measure | Forensic n=66 mean ± SD | Outpatients n=25 mean ± SD | Controls n=24 mean ± SD | Classical F | Classical p | Welch F | Welch p |',
      '|---|---|---|---|---|---|---|---|']
    for v,c in r['continuous'].items():
        ds = [f"{z['mean']:.2f} ± {z['sd']:.2f}" for z in c['descriptives']]
        lines.append('| '+' | '.join([c['label'],*ds,f"{c['anova']['F']:.3f}",ptext(c['anova']['p']),f"{c['welch']['F']:.3f}",ptext(c['welch']['p'])])+' |')
    lines += ['', '## Focal forensic minus outpatient comparisons', '',
      '| Dimension | Mean difference | Tukey p | Games–Howell p | Games–Howell 95% CI | Exploratory Holm p across five dimensions |',
      '|---|---|---|---|---|---|']
    for v in temperaments:
        c=r['continuous'][v];z=c['pairs'][0]
        lines.append(f"| {c['label']} | {z['difference_first_minus_second']:.3f} | {ptext(z['tukey_p'])} | {ptext(z['games_howell_p'])} | {z['games_howell_ci95'][0]:.3f} to {z['games_howell_ci95'][1]:.3f} | {ptext(r['exploratory_holm_across_five_focal_dimensions'][v])} |")
    lines += ['', 'Within-dimension adjusted pairwise p-values do not control multiplicity across all five dimensions. The additional Holm sensitivity is exploratory and must not be described as prespecified.', '', '## Categorical audit', '',
      '| Variable | Codes | Groups in count rows | Counts | Pearson chi-square | df | p | Minimum expected | Fraction of cells below 5 |',
      '|---|---|---|---|---|---|---|---|---|']
    for v,c in r['categorical'].items():
        lines.append(f"| {v} | {c['codes']} | {c['groups']} | {c['counts']} | {c['chi2']:.3f} | {c['df']} | {ptext(c['p'])} | {c['minimum_expected']:.3f} | {c['fraction_expected_below_5']:.1%} |")
    lines += ['', 'Pearson results are reproduced, not endorsed as final for sparse tables. Resolve category meanings before choosing an exact/Monte Carlo procedure or any clinically justified grouping.', '',
      f"Repeated complete rows beyond the first: {r['repeated_rows_beyond_first']}. No participant identifier exists in this file; identical recorded profiles are not proof of duplicate participants. Check source records; do not automatically deduplicate.", '',
      'Missing diagnosis: 24 controls. GELİR is entirely missing and cannot support income analyses.', '',
      'All five saved-output reproduction checks passed. Aggregate JSON contains complete precision, all pairwise contrasts, degrees of freedom and package versions.']
    (out/'RESULTS.md').write_text('\n'.join(lines)+'\n')
    print('Aggregate audit written; five archived-output checks passed.')

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--sav',type=Path,default=ROOT/'SOSYODEMOGRAFİ YGAP.sav')
    p.add_argument('--out',type=Path,default=ROOT/'analysis'/'generated')
    a=p.parse_args();run(a.sav,a.out)
