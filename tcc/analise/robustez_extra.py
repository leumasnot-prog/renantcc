"""Análises complementares pedidas na revisão simulada (roteiro RR-24, 25, 28, 30, 41, 45).

Usa as funções de resultados_c3.py e a mesma base. Gera:
  tcc/analise/saidas/robustez_extra.md
  tcc/latex/tabelas/tab-efeito.tex, tab-loo.tex, tab-tamanho.tex, tab-secundarios.tex

Uso: python3 tcc/analise/robustez_extra.py
"""
import math
import os
import sys

import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import resultados_c3 as R

BR, CP, EX = 'Divida Bruta / Atv Tt %', 'Divida CP / Divida Tt %', 'Exigivel Tt / Ativo Tt %'
PAND = [2020, 2021]
COMERCIO = ('RADL', 'PNVL', 'PFRM')


def grupos(dados, grupo, ind, anos=R.ANOS, excluir=()):
    m = R.medias_empresa(dados, [t for t in grupo if t not in excluir], ind, anos)
    f = [m[t][0] for t in m if grupo[t] == 'F']
    n = [m[t][0] for t in m if grupo[t] == 'NF']
    return f, n


def efeito(f, n):
    """Diferença F - NF, IC 95% de Welch e g de Hedges."""
    f, n = np.array(f), np.array(n)
    d = f.mean() - n.mean()
    vf, vn = f.var(ddof=1) / len(f), n.var(ddof=1) / len(n)
    ep = math.sqrt(vf + vn)
    gl = (vf + vn) ** 2 / (vf ** 2 / (len(f) - 1) + vn ** 2 / (len(n) - 1))
    tc = stats.t.ppf(0.975, gl)
    sp = math.sqrt(((len(f) - 1) * f.var(ddof=1) + (len(n) - 1) * n.var(ddof=1)) / (len(f) + len(n) - 2))
    g = d / sp * (1 - 3 / (4 * (len(f) + len(n)) - 9))
    return d, d - tc * ep, d + tc * ep, g


def main():
    dados, grupo, _ = R.carregar()
    md = ['# Análises complementares (revisão simulada)\n']

    # 1. Tamanho de efeito e IC ------------------------------------------------
    md.append('## 1. Diferença F − NF, IC 95% (Welch) e g de Hedges\n')
    linhas = []
    casos = [(i, r, u, R.ANOS, '2018--2025') for i, r, u in R.INDICADORES] + \
            [(CP, 'Dívida CP / Dívida total', '%', PAND, '2020--2021')]
    for ind, rot, un, anos, per in casos:
        f, n = grupos(dados, grupo, ind, anos)
        d, lo, hi, g = efeito(f, n)
        suf = ' p.p.' if un == '%' else 'x'
        md.append(f'- {rot} ({per}): dif = {d:.2f}; IC95% [{lo:.2f}; {hi:.2f}]; g = {g:.2f}')
        linhas.append([rot, per, R.br(d) + suf, f'[{R.br(lo)}; {R.br(hi)}]', R.br(g, 2)])
    R.tabela_latex('tab-efeito.tex', 'Diferença entre os grupos, intervalo de confiança e tamanho de efeito',
                   'tab:efeito', ['Indicador', 'Período', 'F $-$ NF', 'IC 95\\%', 'g de Hedges'], linhas,
                   'Diferença entre as médias das familiares e das não familiares (p.p.: pontos percentuais), '
                   'com intervalo de confiança de 95\\% pela aproximação de Welch. g de Hedges: diferença '
                   'padronizada, com correção para amostras pequenas; por convenção, valores em torno de 0,2, '
                   '0,5 e 0,8 indicam efeitos pequeno, médio e grande.', 'llrcc')

    # 2. Retirada de uma empresa por vez --------------------------------------
    md.append('\n## 2. Retirada de uma empresa por vez (faixa de p-valores)\n')
    linhas = []
    for ind, rot, anos, per in [(BR, 'Dív. bruta / Ativo', R.ANOS, '2018--2025'),
                                (CP, 'Dív. CP / Dív. total', R.ANOS, '2018--2025'),
                                (CP, 'Dív. CP / Dív. total', PAND, '2020--2021')]:
        res = {}
        for t in grupo:
            r = R.comparar(dados, grupo, ind, anos, excluir=(t,))
            res[t] = (r['p_t'], r['p_mw'], r['F'] < r['NF'])
        pts = sorted(res.items(), key=lambda kv: kv[1][0])
        pms = sorted(res.items(), key=lambda kv: kv[1][1])
        n5t = sum(v[0] < 0.05 for v in res.values()); n5m = sum(v[1] < 0.05 for v in res.values())
        sinal = sum(v[2] for v in res.values())
        md.append(f'- {rot} ({per}): p(t) de {pts[0][1][0]:.3f} (sem {pts[0][0]}) a {pts[-1][1][0]:.3f} (sem {pts[-1][0]}); '
                  f'p(MW) de {pms[0][1][1]:.3f} (sem {pms[0][0]}) a {pms[-1][1][1]:.3f} (sem {pms[-1][0]}); '
                  f'p<0,05: t em {n5t}/16, MW em {n5m}/16; F<NF em {sinal}/16')
        linhas.append([rot, per, f'{R.br(pts[0][1][0], 3)} a {R.br(pts[-1][1][0], 3)}', f'{n5t} de 16',
                       f'{R.br(pms[0][1][1], 3)} a {R.br(pms[-1][1][1], 3)}', f'{n5m} de 16', f'{sinal} de 16'])
    R.tabela_latex('tab-loo.tex', 'Sensibilidade à retirada de uma empresa por vez', 'tab:loo',
                   ['Indicador', 'Período', 'p (t): faixa', 'p $<$ 0,05', 'p (MW): faixa', 'p $<$ 0,05', 'F $<$ NF'],
                   linhas,
                   'Cada teste foi repetido 16 vezes, retirando uma empresa de cada vez. Faixa: menor e maior '
                   'p-valor obtidos. F $<$ NF: número de repetições em que a média das familiares ficou abaixo '
                   'da média das não familiares.', 'llccccc')

    # 3. Sem Comércio e Distribuição ------------------------------------------
    md.append('\n## 3. Sem o subsetor de Comércio e Distribuição (RADL, PNVL, PFRM)\n')
    sem = {}
    for ind, rot, anos, per in [(CP, 'Dív. CP / Dív. total', R.ANOS, '2018-2025'), (CP, 'Dív. CP / Dív. total', PAND, '2020-2021'),
                                (BR, 'Dív. bruta / Ativo', R.ANOS, '2018-2025')]:
        r = R.comparar(dados, grupo, ind, anos, excluir=COMERCIO)
        sem[(ind, per)] = r
        md.append(f"- {rot} ({per}): F = {r['F']:.1f} · NF = {r['NF']:.1f} ({r['nF']}×{r['nNF']}); p(t) = {r['p_t']:.3f}; p(MW) = {r['p_mw']:.3f}")

    # 4. Holm ------------------------------------------------------------------
    md.append('\n## 4. Testes múltiplos (Holm) na análise por subperíodos\n')
    ps = []
    for ind in (BR, EX, CP):
        for nome, anos in R.SUBPERIODOS.items():
            r = R.comparar(dados, grupo, ind, anos)
            ps += [(r['p_t'], ind, nome, 't'), (r['p_mw'], ind, nome, 'MW')]
    ps.sort()
    m = len(ps)
    md.append(f'- família: {m} testes (3 indicadores × 3 subperíodos × 2 testes); menor p = {ps[0][0]:.3f} '
              f'({ps[0][1]}, {ps[0][2]}, {ps[0][3]}); p ajustado (Holm) = {min(1, ps[0][0] * m):.3f}')

    # 5. Tamanho ---------------------------------------------------------------
    md.append('\n## 5. Tamanho (Capital Employed médio 2018–2025, R$ milhões)\n')
    ce = R.medias_empresa(dados, grupo, 'Capital Employed $', R.ANOS)
    linhas = []
    for gg, nome in (('F', 'Familiares'), ('NF', 'Não familiares')):
        v = np.array([ce[t][0] for t in ce if grupo[t] == gg]) / 1e6
        pond = {}
        for ind in (BR, EX):
            mm = R.medias_empresa(dados, grupo, ind, R.ANOS)
            ts = [t for t in mm if grupo[t] == gg]
            w = np.array([ce[t][0] for t in ts]); x = np.array([mm[t][0] for t in ts])
            pond[ind] = (x.mean(), (w * x).sum() / w.sum())
        md.append(f'- {nome}: mediana {np.median(v):,.0f}; mín {v.min():,.0f}; máx {v.max():,.0f}; '
                  f'Dív bruta/Ativo simples {pond[BR][0]:.1f} ponderada {pond[BR][1]:.1f}; '
                  f'Exigível/Ativo simples {pond[EX][0]:.1f} ponderada {pond[EX][1]:.1f}')
        fm = lambda x: f'{x:,.0f}'.replace(',', '.')
        linhas.append([nome, str(len(v)), fm(np.median(v)), fm(v.min()), fm(v.max()),
                       R.br(pond[BR][0]) + '\\%', R.br(pond[BR][1]) + '\\%'])
    R.tabela_latex('tab-tamanho.tex', 'Tamanho das empresas e endividamento oneroso ponderado pelo tamanho',
                   'tab:tamanho',
                   ['Grupo', 'n', 'Mediana', 'Mínimo', 'Máximo', 'Média simples', 'Média ponderada'], linhas,
                   'Tamanho: capital empregado (\\textit{Capital Employed}, Economática), média de 2018 a 2025, em '
                   'R\\$ milhões. Médias simples e ponderada (pelo capital empregado) da Dívida bruta / Ativo total.',
                   'lcrrrcc')

    # 6. Indicadores secundários (apêndice) -------------------------------------
    linhas = []
    for ind, rot, un in R.SECUNDARIOS:
        r = R.comparar(dados, grupo, ind)
        linhas.append([rot, R.fmt_val(r['F'], un), R.fmt_val(r['NF'], un), f"{r['nF']} $\\times$ {r['nNF']}",
                       R.fmt_p(r['p_t']), R.fmt_p(r['p_mw'])])
    R.tabela_latex('tab-secundarios.tex', 'Indicadores secundários e liquidez corrente, 2018--2025', 'tab:secundarios',
                   ['Indicador', 'F', 'NF', 'n', 'p (t)', 'p (MW)'], linhas,
                   R.NOTA_P + ' Os indicadores sobre o patrimônio líquido (PL) incluem a Alliar em 2025, quando o PL '
                   'da empresa foi negativo.', 'lrrccc')

    out = os.path.join(R.RAIZ, 'tcc', 'analise', 'saidas', 'robustez_extra.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print('\n'.join(md))


if __name__ == '__main__':
    main()
