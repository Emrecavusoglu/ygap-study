"""Exploratory standardized focal contrasts; never exports participant rows.
Run from repository root: python analysis/effect_sizes.py
Bootstrap resamples existing observations within each group; it creates no study records.
"""
from pathlib import Path
import hashlib, json, importlib.metadata
import numpy as np
import pyreadstat
from scipy.special import gammaln
ROOT=Path(__file__).resolve().parents[1]
V={'depres':'Depressive','siklotimi':'Cyclothymic','hipertimi':'Hyperthymic','irritable':'Irritable','anksiyöz':'Anxious'}
SEED=20260920
B=20000

def g(x,y):
    nx,ny=x.shape[-1],y.shape[-1]
    df=nx+ny-2
    j=np.exp(gammaln(df/2)-.5*np.log(df/2)-gammaln((df-1)/2))
    pooled=np.sqrt(((nx-1)*x.var(axis=-1,ddof=1)+(ny-1)*y.var(axis=-1,ddof=1))/df)
    return j*(x.mean(axis=-1)-y.mean(axis=-1))/pooled

def run():
    path=next(ROOT.glob('*.sav'))
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    expected=json.loads((ROOT/'analysis/generated/results.json').read_text())
    assert sha==expected['source_sha256'], 'Source changed; repeat audit first'
    data,_=pyreadstat.read_sav(path)
    x=data.loc[data.grup==1,list(V)].to_numpy()
    y=data.loc[data.grup==3,list(V)].to_numpy()
    assert x.shape==(66,5) and y.shape==(25,5) and np.isfinite(x).all() and np.isfinite(y).all()
    rng=np.random.default_rng(SEED)
    # Same row draws across dimensions preserve the observed within-person dependence.
    ix=rng.integers(0,len(x),(B,len(x)))
    iy=rng.integers(0,len(y),(B,len(y)))
    rows=[]
    for k,(v,label) in enumerate(V.items()):
        a,b=x[:,k],y[:,k]
        estimate=float(g(a,b))
        assert np.isclose(estimate,-g(b,a))
        desc=expected['continuous'][v]['descriptives']
        df=len(a)+len(b)-2
        j=np.exp(gammaln(df/2)-.5*np.log(df/2)-gammaln((df-1)/2))
        from_summary=j*(desc[0]['mean']-desc[1]['mean'])/np.sqrt(((len(a)-1)*desc[0]['sd']**2+(len(b)-1)*desc[1]['sd']**2)/df)
        assert np.isclose(estimate,from_summary)
        boot=g(a[ix],b[iy])
        assert np.isfinite(boot).all()
        lo,hi=np.quantile(boot,[.025,.975])
        pair=expected['continuous'][v]['pairs'][0]
        rows.append(dict(variable=v,label=label,n_forensic=len(a),n_outpatient=len(b),hedges_g=estimate,bootstrap_percentile_ci95=[float(lo),float(hi)],raw_difference=pair['difference_first_minus_second'],games_howell_ci95=pair['games_howell_ci95'],games_howell_p=pair['games_howell_p'],holm_five_p=expected['exploratory_holm_across_five_focal_dimensions'][v]))
    result=dict(source_sha256=sha,seed=SEED,bootstrap_replicates=B,direction='Forensic minus outpatient',versions={k:importlib.metadata.version(k) for k in ['numpy','scipy','pyreadstat']},contrasts=rows)
    out=ROOT/'analysis/generated'
    (out/'effect_sizes.json').write_text(json.dumps(result,indent=2)+'\n')
    lines=['# Focal effect sizes — 20 September 2026','','Exploratory addition during review. All 91 patient records retained. No imputation, recoding, synthetic participants, or item-level access. Positive values mean higher forensic inpatient scores.','', '| Dimension | Hedges g | Pointwise bootstrap 95% CI | Raw difference | Games–Howell 95% CI | Holm p across five dimensions |','|---|---:|---|---:|---|---:|']
    for r in rows:
        lo,hi=r['bootstrap_percentile_ci95']; rl,rh=r['games_howell_ci95']
        lines.append(f"| {r['label']} | {r['hedges_g']:.3f} | {lo:.3f} to {hi:.3f} | {r['raw_difference']:.3f} | {rl:.3f} to {rh:.3f} | {r['holm_five_p']:.3f} |")
    lines += ['', 'Hedges g uses the sample-size-weighted pooled within-group SD and the exact gamma-function small-sample correction (df = 89). It describes a standardized difference; unequal variances limit a common-SD interpretation. Raw differences and their Games–Howell intervals remain the principal interpretable estimates.', '',f'Uncertainty for g: percentile nonparametric bootstrap, {B:,} independent within-group row resamples, NumPy default_rng seed {SEED}. These intervals are pointwise, exploratory, and not multiplicity-adjusted. Their zero exclusion must not replace the Holm-adjusted inference. Games–Howell intervals account for three pairwise group comparisons within each dimension, not all five dimensions.', '', 'The script checks agreement with the previously verified summary statistics and sign reversal on exchanging groups. Bootstrap samples are computational resamples of observed records, not generated study observations. No effect-size thresholds or causal interpretation are assigned.', '', 'Methodological background: [Lakens (2013)](https://doi.org/10.3389/fpsyg.2013.00863). This source supports transparent standardized-effect reporting; the bootstrap settings are our explicitly documented review-stage choice.', '',f'Source SHA256: `{sha}`. Reproduce: `python analysis/effect_sizes.py`.']
    (out/'EFFECT_SIZES.md').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines[:12]))
if __name__=='__main__': run()
