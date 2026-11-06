"""Recálculo independente do Cenário 3 a partir da aba-base (auditoria de 06/11/2026).
Uso: python3 tcc/auditoria/recalculo_c3.py  (requer openpyxl, scipy, numpy)"""
import openpyxl, collections
import os
F=os.path.join(os.path.dirname(__file__),'..','arquivos','TCC Atual - Cenário 3.xlsx')
def load(sheet='Saúde - 1218 à 1225'):
    ws=openpyxl.load_workbook(F,data_only=True,read_only=True)[sheet]
    rows=list(ws.iter_rows(values_only=True))
    hdr=rows[0]; data=collections.defaultdict(list); grp={}
    for r in rows[1:]:
        if len(r)<8 or not r[4]: continue
        vals=[(v if isinstance(v,(int,float)) else None) for v in list(r[7:36])+[None]*(29-len(r[7:36]))]
        data[(r[4],r[6])].append(vals); grp[r[4]]=r[1]
    return hdr,data,grp
from scipy import stats
import numpy as np, math
h,d,g=load()
ANN=[0,4,8,12,16,20,24,28]; YRS=list(range(2018,2026))
def mw_sheet(f,n):
    allv=f+n; r=stats.rankdata(allv); R1=sum(r[:len(f)]); n1,n2=len(f),len(n)
    U=R1-n1*(n1+1)/2; z=(abs(U-n1*n2/2)-0.5)/math.sqrt(n1*n2*(n1+n2+1)/12); return 2*(1-stats.norm.cdf(z))
def run(ind,years=YRS,excl=()):
    idx=[ANN[YRS.index(y)] for y in years]
    F=[];N=[];info={}
    for t,gr in g.items():
        if t in excl: continue
        v=[d[(t,ind)][0][i] for i in idx]; v=[x for x in v if x is not None]
        if not v: continue
        m=np.mean(v); info[t]=(round(m,2),len(v))
        (F if gr=='Familiar' else N).append(m)
    # anos F<NF (média anual por grupo)
    cnt=0
    for i in idx:
        fa=[d[(t,ind)][0][i] for t in g if g[t]=='Familiar' and t not in excl and d[(t,ind)][0][i] is not None]
        na=[d[(t,ind)][0][i] for t in g if g[t]!='Familiar' and t not in excl and d[(t,ind)][0][i] is not None]
        cnt+= np.mean(fa)<np.mean(na)
    pt=stats.ttest_ind(F,N,equal_var=False).pvalue
    pmw=mw_sheet(F,N); pex=stats.mannwhitneyu(F,N,method='exact').pvalue
    return dict(F=np.mean(F),N=np.mean(N),nF=len(F),nN=len(N),cnt=cnt,k=len(idx),pt=pt,pmw=pmw,pex=pex,info=info)
INDS=['Divida Bruta / Atv Tt %','Exigivel Tt / Ativo Tt %','Estr Cap (D/D+Pat Liq) %','Divida liq / Ebitda x','Divida CP / Divida Tt %','Liquidez Corrente x','Exigivel Tt / Pat Liq %','Divida Bruta / Pat Liq %','Divida Liq / Pat Liq %']
def show(title,years=YRS,excl=(),inds=INDS):
    print('\n##',title)
    for ind in inds:
        r=run(ind,years,excl)
        print(f"{ind:28s} F={r['F']:7.2f} NF={r['N']:7.2f} ({r['nF']}x{r['nN']}) F<NF {r['cnt']}/{r['k']}  p_t={r['pt']:.3f} p_MW(planilha)={r['pmw']:.3f} p_MW(exato)={r['pex']:.3f}")
show('Período completo 2018-2025')
show('Pré 2018-2019',[2018,2019],inds=INDS[:5])
show('Pandemia 2020-2021',[2020,2021],inds=INDS[:5])
show('Pós 2022-2025',[2022,2023,2024,2025],inds=INDS[:5])
show('Sem SAUD, completo',excl=('SAUD',),inds=INDS[:5])
for ind in ['Divida liq / Ebitda x','Divida CP / Divida Tt %']:
    print('\n',ind,run(ind)['info'])
