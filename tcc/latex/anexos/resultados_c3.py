"""Resultados do TCC recalculados a partir da base da Economática (Cenário 3 e robustez).

Lê a aba-base 'Saúde - 1218 à 1225' de 'TCC Atual - Cenário 3.xlsx' e reproduz, de forma
independente da planilha, todas as tabelas do Capítulo 4:

  - médias anuais (31/12) por grupo e número de anos em que F < NF;
  - testes por empresa (média das 8 datas de 31/12): t de Welch e Mann-Whitney
    (aproximação normal com correção de continuidade, como na planilha, e p exato);
  - subperíodos (2018-19, 2020-21, 2022-25);
  - robustez: Cenários 1 e 2 (classificação do CONTEXTO_TCC.md, tabela 4.2) e sem SAUD;
  - tamanho das empresas (Capital Employed) e médias ponderadas por tamanho.

Saídas:
  tcc/analise/saidas/resultados.md        relatório completo (conferência)
  tcc/latex/tabelas/*.tex                 tabelas inseridas no Capítulo 4

Uso (na raiz do repositório):  python3 tcc/analise/resultados_c3.py
Requer: openpyxl, numpy, scipy.
"""
from __future__ import annotations

import collections
import math
import os

import numpy as np
import openpyxl
from scipy import stats

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PLANILHA = os.path.join(RAIZ, 'tcc', 'arquivos', 'TCC Atual - Cenário 3.xlsx')
ABA = 'Saúde - 1218 à 1225'
SAIDA_MD = os.path.join(RAIZ, 'tcc', 'analise', 'saidas', 'resultados.md')
DIR_TAB = os.path.join(RAIZ, 'tcc', 'latex', 'tabelas')

ANOS = list(range(2018, 2026))
COL_ANO = {a: 4 * i for i, a in enumerate(ANOS)}  # índice da coluna de 31/12 nas 29 datas
SUBPERIODOS = {'2018--2019': [2018, 2019], '2020--2021': [2020, 2021], '2022--2025': [2022, 2023, 2024, 2025]}

# Classificação dos cenários alternativos (CONTEXTO_TCC.md, tabela 4.2).
# O arquivo "Cenário 1" está com a classificação do C2 (erro 1), por isso as listas ficam aqui.
FAMILIARES = {
    'C1': {'BLAU', 'DASA', 'BALM', 'OFSA', 'RDOR'},
    'C2': {'BLAU', 'DASA', 'BALM', 'OFSA', 'RDOR', 'HAPV', 'PNVL'},
}

INDICADORES = [  # (nome na Economática, rótulo, unidade)
    ('Divida Bruta / Atv Tt %', 'Dívida bruta / Ativo total', '%'),
    ('Exigivel Tt / Ativo Tt %', 'Exigível total / Ativo total', '%'),
    ('Estr Cap (D/D+Pat Liq) %', 'Dívida bruta / (Dívida bruta + PL)', '%'),
    ('Divida liq / Ebitda x', 'Dívida líquida / EBITDA', 'x'),
    ('Divida CP / Divida Tt %', 'Dívida CP / Dívida total', '%'),
]
CURTO = {'Dívida bruta / Ativo total': 'Dív. bruta / Ativo', 'Exigível total / Ativo total': 'Exigível / Ativo',
         'Dívida CP / Dívida total': 'Dív. CP / Dív. total'}
SECUNDARIOS = [
    ('Exigivel Tt / Pat Liq %', 'Exigível total / PL', '%'),
    ('Divida Bruta / Pat Liq %', 'Dívida bruta / PL', '%'),
    ('Divida Liq / Pat Liq %', 'Dívida líquida / PL', '%'),
    ('Liquidez Corrente x', 'Liquidez corrente', 'x'),
]


# ---------------------------------------------------------------------------- dados
def carregar():
    ws = openpyxl.load_workbook(PLANILHA, data_only=True, read_only=True)[ABA]
    dados, grupo, nome = {}, {}, {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        if len(r) < 8 or not r[4]:
            continue
        vals = list(r[7:36]) + [None] * (29 - len(r[7:36]))
        vals = [v if isinstance(v, (int, float)) else None for v in vals]
        chave = (r[4], r[6])
        if chave in dados:
            raise ValueError(f'linha duplicada na base: {chave}')
        dados[chave] = vals
        grupo[r[4]] = 'F' if r[1] == 'Familiar' else 'NF'
        nome[r[4]] = r[3]
    return dados, grupo, nome


# ---------------------------------------------------------------------------- testes
def mw_planilha(f, n):
    """Mann-Whitney como na planilha: postos médios, U das familiares, z com correção de continuidade."""
    postos = stats.rankdata(list(f) + list(n))
    n1, n2 = len(f), len(n)
    u = sum(postos[:n1]) - n1 * (n1 + 1) / 2
    z = (abs(u - n1 * n2 / 2) - 0.5) / math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    return 2 * (1 - stats.norm.cdf(z))


def medias_empresa(dados, empresas, ind, anos):
    out = {}
    for t in empresas:
        v = [dados[(t, ind)][COL_ANO[a]] for a in anos]
        v = [x for x in v if x is not None]
        if v:
            out[t] = (float(np.mean(v)), len(v))
    return out


def comparar(dados, grupo, ind, anos=ANOS, excluir=()):
    emp = [t for t in grupo if t not in excluir]
    m = medias_empresa(dados, emp, ind, anos)
    f = [m[t][0] for t in m if grupo[t] == 'F']
    n = [m[t][0] for t in m if grupo[t] == 'NF']
    anos_menor = 0
    for a in anos:
        fa = [dados[(t, ind)][COL_ANO[a]] for t in emp if grupo[t] == 'F' and dados[(t, ind)][COL_ANO[a]] is not None]
        na = [dados[(t, ind)][COL_ANO[a]] for t in emp if grupo[t] == 'NF' and dados[(t, ind)][COL_ANO[a]] is not None]
        anos_menor += np.mean(fa) < np.mean(na)
    return dict(
        F=np.mean(f), NF=np.mean(n), medF=np.median(f), medNF=np.median(n), nF=len(f), nNF=len(n),
        anos_menor=int(anos_menor), k=len(anos),
        p_t=stats.ttest_ind(f, n, equal_var=False).pvalue,
        p_mw=mw_planilha(f, n),
        p_mw_exato=stats.mannwhitneyu(f, n, method='exact').pvalue,
        incompletas={t: m[t][1] for t in m if m[t][1] < len(anos)},
    )


def medias_anuais(dados, grupo, ind):
    linhas = []
    for a in ANOS:
        fa = [dados[(t, ind)][COL_ANO[a]] for t in grupo if grupo[t] == 'F' and dados[(t, ind)][COL_ANO[a]] is not None]
        na = [dados[(t, ind)][COL_ANO[a]] for t in grupo if grupo[t] == 'NF' and dados[(t, ind)][COL_ANO[a]] is not None]
        linhas.append((a, np.mean(fa), np.mean(na)))
    return linhas


# ---------------------------------------------------------------------------- formatação
def br(x, casas=1):
    return f'{x:.{casas}f}'.replace('.', ',')


def fmt_val(x, unidade):
    return f'{br(x)}\\%' if unidade == '%' else f'{br(x)}x'


def fmt_p(p):
    s = br(p, 3)
    if p < 0.01:
        return f'\\textbf{{{s}}}$^{{***}}$'
    if p < 0.05:
        return f'\\textbf{{{s}}}$^{{**}}$'
    if p < 0.10:
        return f'{s}$^{{*}}$'
    return s


NOTA_P = ('Testes bicaudais sobre a média de cada empresa nas datas de 31/12 do período. '
          'p (MW): teste de Mann-Whitney, aproximação normal com correção de continuidade. '
          '$^{***}$, $^{**}$ e $^{*}$: significativo a 1\\%, 5\\% e 10\\%.')


def tabela_latex(arquivo, legenda, rotulo, cabecalho, linhas, nota, especificacao):
    corpo = '\n'.join(' & '.join(l) + r' \\' for l in linhas)
    tex = rf"""% Gerado por tcc/analise/resultados_c3.py -- não edite à mão; rode o script de novo.
\begin{{table}}[htb]
\caption{{{legenda}}}\label{{{rotulo}}}
\centering\footnotesize\setlength{{\tabcolsep}}{{4pt}}
\begin{{tabular}}{{{especificacao}}}
\toprule
{' & '.join(cabecalho)} \\
\midrule
{corpo}
\bottomrule
\end{{tabular}}
\fonte{{Elaborado pelo autor (2026), com dados da Economática.}}
\nota{{{nota}}}
\end{{table}}
"""
    with open(os.path.join(DIR_TAB, arquivo), 'w', encoding='utf-8') as fh:
        fh.write(tex)


# ---------------------------------------------------------------------------- principal
def main():
    os.makedirs(DIR_TAB, exist_ok=True)
    os.makedirs(os.path.dirname(SAIDA_MD), exist_ok=True)
    dados, grupo, nome = carregar()
    md = ['# Resultados recalculados (Cenário 3)\n',
          f'Base: `{ABA}` · {sum(1 for g in grupo.values() if g == "F")} familiares × '
          f'{sum(1 for g in grupo.values() if g == "NF")} não familiares\n']

    # 1. Período completo -------------------------------------------------------
    md.append('\n## 1. Período completo 2018–2025\n\n| Indicador | F | NF | n | F<NF | p t | p MW | p MW exato | mediana F | mediana NF |\n|---|---|---|---|---|---|---|---|---|---|')
    linhas_tex = []
    for ind, rot, un in INDICADORES + SECUNDARIOS:
        r = comparar(dados, grupo, ind)
        md.append(f"| {rot} | {r['F']:.2f} | {r['NF']:.2f} | {r['nF']}×{r['nNF']} | {r['anos_menor']}/{r['k']} | "
                  f"{r['p_t']:.3f} | {r['p_mw']:.3f} | {r['p_mw_exato']:.3f} | {r['medF']:.2f} | {r['medNF']:.2f} |")
        if r['incompletas']:
            md.append(f"|  ↳ empresas com menos de {r['k']} anos: {r['incompletas']} |||||||||| ")
        if (ind, rot, un) in INDICADORES:
            linhas_tex.append([rot, fmt_val(r['F'], un), fmt_val(r['NF'], un), f"{r['nF']} $\\times$ {r['nNF']}",
                               f"{r['anos_menor']} de {r['k']}", fmt_p(r['p_t']), fmt_p(r['p_mw'])])
    tabela_latex('tab-periodo-completo.tex',
                 'Endividamento das empresas familiares (F) e não familiares (NF), 2018--2025',
                 'tab:completo',
                 ['Indicador', 'F', 'NF', 'n', 'Anos F $<$ NF', 'p (t)', 'p (MW)'], linhas_tex,
                 NOTA_P + ' Valores: média simples das médias por empresa. '
                 'Na Dívida CP / Dívida total, a Bradsaúde é excluída por não ter dívida financeira; '
                 'na Dívida líquida / EBITDA, a Biomm tem um único ano com EBITDA positivo (2025). '
                 'Na Dívida bruta / (Dívida bruta + PL), o valor da Alliar em 2025 supera 100\\% porque o PL da empresa '
                 'foi negativo nesse ano.',
                 'lrrcccc')

    # 2. Médias anuais ------------------------------------------------------------
    md.append('\n## 2. Médias anuais por grupo (31/12)\n')
    anuais_tex = []
    sel = [INDICADORES[0], INDICADORES[1], INDICADORES[4]]
    series = {ind: medias_anuais(dados, grupo, ind) for ind, _, _ in sel}
    md.append('| Ano | ' + ' | '.join(f'{rot} F | {rot} NF' for _, rot, _ in sel) + ' |\n|' + '---|' * (1 + 2 * len(sel)))
    for i, a in enumerate(ANOS):
        md.append(f'| {a} | ' + ' | '.join(f'{series[ind][i][1]:.1f} | {series[ind][i][2]:.1f}' for ind, _, _ in sel) + ' |')
        anuais_tex.append([str(a)] + [x for ind, _, _ in sel for x in (br(series[ind][i][1]), br(series[ind][i][2]))])
    tabela_latex('tab-medias-anuais.tex',
                 'Médias anuais por grupo em 31 de dezembro (\\%)', 'tab:anuais',
                 ['Ano', '\\multicolumn{2}{c}{Dívida bruta / Ativo}', '\\multicolumn{2}{c}{Exigível / Ativo}',
                  '\\multicolumn{2}{c}{Dívida CP / Dívida total}'] ,
                 [['', 'F', 'NF', 'F', 'NF', 'F', 'NF']] + anuais_tex,
                 'F: familiares (10 empresas); NF: não familiares (6 empresas; 5 na Dívida CP / Dívida total). '
                 'Média simples entre as empresas de cada grupo.',
                 'lrrrrrr')

    # 3. Subperíodos --------------------------------------------------------------
    md.append('\n## 3. Subperíodos\n\n| Indicador | Período | F | NF | p t | p MW | p MW exato |\n|---|---|---|---|---|---|---|')
    sub_tex = []
    for ind, rot, un in [INDICADORES[0], INDICADORES[1], INDICADORES[4]]:
        for nome_p, anos in SUBPERIODOS.items():
            r = comparar(dados, grupo, ind, anos)
            md.append(f"| {rot} | {nome_p} | {r['F']:.2f} | {r['NF']:.2f} | {r['p_t']:.3f} | {r['p_mw']:.3f} | {r['p_mw_exato']:.3f} |")
            sub_tex.append([CURTO.get(rot, rot) if nome_p == '2018--2019' else '', nome_p, fmt_val(r['F'], un), fmt_val(r['NF'], un),
                            fmt_p(r['p_t']), fmt_p(r['p_mw'])])
    tabela_latex('tab-subperiodos.tex', 'Comparação entre os grupos por subperíodo', 'tab:subperiodos',
                 ['Indicador', 'Subperíodo', 'F', 'NF', 'p (t)', 'p (MW)'], sub_tex,
                 NOTA_P + ' Subperíodos: pré-pandemia (2018--2019), pandemia (2020--2021) e pós-pandemia (2022--2025).',
                 'llrrcc')

    # 4. Robustez -----------------------------------------------------------------
    md.append('\n## 4. Robustez\n\n| Especificação | Indicador | F | NF | n | p t | p MW |\n|---|---|---|---|---|---|---|')
    rob_tex = []
    especs = [('C3 (principal)', grupo, ()),
              ('C3 sem Bradsaúde', grupo, ('SAUD',)),
              ('C2', {t: ('F' if t in FAMILIARES['C2'] else 'NF') for t in grupo}, ()),
              ('C1', {t: ('F' if t in FAMILIARES['C1'] else 'NF') for t in grupo}, ())]
    for nome_e, gr, excl in especs:
        for ind, rot, un in [INDICADORES[0], INDICADORES[1], INDICADORES[4]]:
            r = comparar(dados, gr, ind, excluir=excl)
            md.append(f"| {nome_e} | {rot} | {r['F']:.2f} | {r['NF']:.2f} | {r['nF']}×{r['nNF']} | {r['p_t']:.3f} | {r['p_mw']:.3f} |")
            rob_tex.append([nome_e if ind == INDICADORES[0][0] else '', CURTO.get(rot, rot), fmt_val(r['F'], un), fmt_val(r['NF'], un),
                            f"{r['nF']} $\\times$ {r['nNF']}", fmt_p(r['p_t']), fmt_p(r['p_mw'])])
    tabela_latex('tab-robustez.tex', 'Análises de robustez', 'tab:robustez',
                 ['Especificação', 'Indicador', 'F', 'NF', 'n', 'p (t)', 'p (MW)'], rob_tex,
                 NOTA_P + ' C1, C2 e C3: Cenários 1, 2 e 3; C1 e C2 são classificações alternativas de empresa familiar (\\autoref{qua:cenarios}).',
                 'llrrccc')

    # 5. DL/EBITDA: sensibilidade à Biomm -----------------------------------------
    r_all = comparar(dados, grupo, 'Divida liq / Ebitda x')
    r_sem = comparar(dados, grupo, 'Divida liq / Ebitda x', excluir=('BIOM',))
    md.append(f"\n## 5. Dívida líquida / EBITDA sem a Biomm\n\nCom BIOM: F={r_all['F']:.2f} NF={r_all['NF']:.2f} "
              f"(p t={r_all['p_t']:.3f}, MW={r_all['p_mw']:.3f}); medianas {r_all['medF']:.2f} × {r_all['medNF']:.2f}.  \n"
              f"Sem BIOM: F={r_sem['F']:.2f} NF={r_sem['NF']:.2f} (p t={r_sem['p_t']:.3f}, MW={r_sem['p_mw']:.3f}).")

    # 6. Tamanho ------------------------------------------------------------------
    md.append('\n## 6. Tamanho (Capital Employed, média 2018–2025, em R$)\n')
    ce = medias_empresa(dados, grupo, 'Capital Employed $', ANOS)
    for t in sorted(ce, key=lambda t: -ce[t][0]):
        md.append(f'- {t} ({grupo[t]}): {ce[t][0]:,.0f}')
    lf = [math.log(ce[t][0]) for t in ce if grupo[t] == 'F' and ce[t][0] > 0]
    ln = [math.log(ce[t][0]) for t in ce if grupo[t] == 'NF' and ce[t][0] > 0]
    md.append(f"\nMediana F = {np.median([ce[t][0] for t in ce if grupo[t]=='F']):,.0f}; "
              f"mediana NF = {np.median([ce[t][0] for t in ce if grupo[t]=='NF']):,.0f}; "
              f"t (log) p = {stats.ttest_ind(lf, ln, equal_var=False).pvalue:.3f}; MW p = {mw_planilha(lf, ln):.3f}")
    # médias ponderadas por tamanho (ilustração)
    for ind, rot, _ in [INDICADORES[0], INDICADORES[1]]:
        m = medias_empresa(dados, grupo, ind, ANOS)
        def pond(gg):
            ts = [t for t in m if grupo[t] == gg and t in ce]
            w = np.array([ce[t][0] for t in ts]); v = np.array([m[t][0] for t in ts])
            return float((w * v).sum() / w.sum())
        md.append(f'- {rot}, média ponderada por Capital Employed: F = {pond("F"):.1f}% · NF = {pond("NF"):.1f}%')

    with open(SAIDA_MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(md) + '\n')
    print('\n'.join(md))


if __name__ == '__main__':
    main()
