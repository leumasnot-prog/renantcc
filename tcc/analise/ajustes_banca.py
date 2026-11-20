"""Ajustes pedidos pela orientadora (20/11/2026).

1. Amostra comparável: operadoras de planos de saúde (reguladas pela ANS) e o varejo/
   distribuição farmacêutica têm estruturas de financiamento próprias. Recalcula tudo
   (a) com a amostra completa, (b) sem as operadoras, (c) sem Comércio e Distribuição e
   (d) sem os dois grupos.
2. PL e resultado negativos: exclui as observações empresa-ano com PL <= 0 ou prejuízo
   (ROA < 0). O sinal do PL é lido no indicador Exigível total / PL (negativo quando o PL
   é negativo); o do resultado, no ROA.
3. Sem "média de médias": em vez de tirar a média de cada empresa nos 8 anos e depois a
   média do grupo, os grupos são comparados ANO A ANO (cada empresa é uma observação
   independente em 31/12) e, de forma descritiva, pela média de todas as observações
   empresa-ano do grupo (média ponderada pelo número de anos válidos de cada empresa).

Usa as funções e a base de resultados_c3.py. Gera:
  tcc/analise/saidas/ajustes_banca.md
  tcc/latex/tabelas/tab-banca-amostras.tex   (comparação empresa-ano por amostra)
  tcc/latex/tabelas/tab-banca-anual.tex      (testes ano a ano, amostra recomendada)

Uso (na raiz do repositório):  python3 tcc/analise/ajustes_banca.py [planilha.xlsx]
A base é igual nos arquivos dos três cenários; a classificação usada é sempre a do Cenário 3
(lista FAMILIARES_C3 abaixo), e não a coluna B do arquivo.
"""
import os
import sys

import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import resultados_c3 as R

OPERADORAS = ('HAPV', 'QUAL', 'SAUD')     # planos de saúde / administradora de benefícios (ANS)
COMERCIO = ('RADL', 'PNVL', 'PFRM')       # Comércio e Distribuição (B3)
AMOSTRAS = [
    ('Completa', ()),
    ('Sem operadoras', OPERADORAS),
    ('Sem comércio', COMERCIO),
    ('Sem operadoras e sem comércio', OPERADORAS + COMERCIO),
]
FAMILIARES_C3 = R.FAMILIARES['C3']
PL_IND, ROA_IND = 'Exigivel Tt / Pat Liq %', 'ROA Rentab do Ativo %'
PRINCIPAIS = [R.INDICADORES[0], R.INDICADORES[1], R.INDICADORES[4]]  # Dív/Ativo, Exig/Ativo, CP/Total
SAIDA_MD = os.path.join(R.RAIZ, 'tcc', 'analise', 'saidas', 'ajustes_banca.md')


def filtrar(dados, grupo, prejuizo=True):
    """Anula as observações empresa-ano com PL < 0 (e, se prejuizo=True, com ROA < 0). Retorna (dados filtrados, lista de exclusões)."""
    for ind in (PL_IND, ROA_IND):
        if not any(k[1] == ind for k in dados):
            raise KeyError(f'indicador "{ind}" não encontrado na base')
    excl = []
    novo = {k: list(v) for k, v in dados.items()}
    for t in grupo:
        for a in R.ANOS:
            c = R.COL_ANO[a]
            pl, roa = dados[(t, PL_IND)][c], dados[(t, ROA_IND)][c]
            motivo = []
            if pl is not None and pl < 0:
                motivo.append('PL negativo')
            if prejuizo and roa is not None and roa < 0:
                motivo.append('prejuízo')
            if motivo:
                excl.append((t, a, ', '.join(motivo)))
                for (tt, ind), v in novo.items():
                    if tt == t:
                        v[c] = None
    return novo, excl


def obs(dados, grupo, ind, anos, excluir, g):
    """Todas as observações empresa-ano válidas do grupo g."""
    return [dados[(t, ind)][R.COL_ANO[a]] for t in grupo if grupo[t] == g and t not in excluir
            for a in anos if dados[(t, ind)][R.COL_ANO[a]] is not None]


def por_ano(dados, grupo, ind, excluir):
    linhas = []
    for a in R.ANOS:
        c = R.COL_ANO[a]
        f = [dados[(t, ind)][c] for t in grupo if grupo[t] == 'F' and t not in excluir and dados[(t, ind)][c] is not None]
        n = [dados[(t, ind)][c] for t in grupo if grupo[t] == 'NF' and t not in excluir and dados[(t, ind)][c] is not None]
        if len(f) >= 2 and len(n) >= 2:
            pt = stats.ttest_ind(f, n, equal_var=False).pvalue
            pm = stats.mannwhitneyu(f, n, method='exact').pvalue
        else:
            pt = pm = float('nan')
        linhas.append(dict(ano=a, F=np.mean(f) if f else float('nan'), NF=np.mean(n) if n else float('nan'),
                           nF=len(f), nNF=len(n), p_t=pt, p_mw=pm))
    return linhas


def resumo_anual(linhas):
    validas = [l for l in linhas if not np.isnan(l['p_t'])]
    return dict(menor=sum(l['F'] < l['NF'] for l in validas), k=len(validas),
                sig5=sum(min(l['p_t'], l['p_mw']) < 0.05 for l in validas),
                sig10=sum(min(l['p_t'], l['p_mw']) < 0.10 for l in validas))


def fp(p):
    return '--' if np.isnan(p) else R.fmt_p(p)


CURTA = {'Completa': 'Completa', 'Sem operadoras': 'Sem operadoras', 'Sem comércio': 'Sem comércio',
         'Sem operadoras e sem comércio': 'Sem ambos'}
FILTROS = [('Só PL negativo', False), ('PL negativo ou prejuízo', True)]  # o primeiro é o principal


def bloco_amostras(dados, grupo):
    linhas, tex = [], []
    for nome_a, ex in AMOSTRAS:
        nF = sum(1 for t in grupo if grupo[t] == 'F' and t not in ex)
        nN = sum(1 for t in grupo if grupo[t] == 'NF' and t not in ex)
        for ind, rot, un in PRINCIPAIS:
            f, n = obs(dados, grupo, ind, R.ANOS, ex, 'F'), obs(dados, grupo, ind, R.ANOS, ex, 'NF')
            ra = resumo_anual(por_ano(dados, grupo, ind, ex))
            linhas.append(f"| {nome_a} ({nF}F×{nN}NF) | {rot} | {np.mean(f):.2f} | {np.mean(n):.2f} | {len(f)} | {len(n)} | "
                          f"{ra['menor']}/{ra['k']} | {ra['sig5']} | {ra['sig10']} | {np.median(f):.2f} | {np.median(n):.2f} |")
            tex.append([f'{CURTA[nome_a]} ({nF} $\\times$ {nN})' if ind == PRINCIPAIS[0][0] else '', R.CURTO.get(rot, rot),
                        R.fmt_val(np.mean(f), un), R.fmt_val(np.mean(n), un), f'{len(f)}/{len(n)}',
                        f"{ra['menor']} de {ra['k']}", str(ra['sig5']), str(ra['sig10'])])
    return linhas, tex


def tabela_anual(dados, grupo, ex, arquivo, legenda, rotulo, nota):
    linhas_tex = []
    for ind, rot, un in PRINCIPAIS:
        for l in por_ano(dados, grupo, ind, ex):
            linhas_tex.append([R.CURTO.get(rot, rot) if l['ano'] == R.ANOS[0] else '', str(l['ano']),
                               R.fmt_val(l['F'], un) if l['nF'] else '--', R.fmt_val(l['NF'], un) if l['nNF'] else '--',
                               f"{l['nF']} $\\times$ {l['nNF']}", fp(l['p_t']), fp(l['p_mw'])])
    R.tabela_latex(arquivo, legenda, rotulo, ['Indicador', 'Ano', 'F', 'NF', 'n', 'p (t)', 'p (MW)'], linhas_tex,
                   nota, 'llrrccc')


CAB = ('| Amostra | Indicador | F | NF | obs F | obs NF | anos F<NF | anos p<5% | anos p<10% | mediana F | mediana NF |\n'
       '|---|---|---|---|---|---|---|---|---|---|---|')
CAB_TEX = ['Amostra (F $\\times$ NF)', 'Indicador', 'F', 'NF', 'Obs.', 'F $<$ NF',
           'p $<$ 5\\%', 'p $<$ 10\\%']
NOTA_ANUAL = ('Cada empresa é uma observação em 31/12 de cada ano; {filtro}. Testes aplicados só quando há ao menos '
              'duas empresas em cada grupo. p (MW): Mann-Whitney exato. $^{{***}}$, $^{{**}}$ e $^{{*}}$: '
              'significativo a 1\\%, 5\\% e 10\\%.')
OPER_TXT = ('Obs.: observações empresa-ano (F/NF). Colunas F $<$ NF, p $<$ 5\\% e p $<$ 10\\%: número de anos. '
            'Sem ambos: sem operadoras e sem comércio. Operadoras: Hapvida, Qualicorp e Bradsaúde; Comércio: RaiaDrogasil, Panvel e Profarma.')


def main():
    dados0, grupo, _ = R.carregar()
    grupo = {t: ('F' if t in FAMILIARES_C3 else 'NF') for t in grupo}
    assert sum(g == 'F' for g in grupo.values()) == 11 and len(grupo) == 16, grupo
    md = ['# Ajustes pedidos pela orientadora\n',
          'Classificação: Cenário 3. Médias = média de todas as observações empresa-ano válidas do grupo; '
          'testes t de Welch e Mann-Whitney exato aplicados ano a ano (31/12).\n']
    dados_sem_filtro = dados0
    for nome_f, prej in FILTROS:
        dados, excl = filtrar(dados0, grupo, prej)
        md.append(f'\n# Filtro: {nome_f}\n\n## Observações excluídas\n')
        md += [f'- {t} {a}: {m} ({grupo[t]})' for t, a, m in excl] or ['- nenhuma']
        md.append('\n## Comparação por amostra\n\n' + CAB)
        linhas, tex = bloco_amostras(dados, grupo)
        md += linhas
        for nome_a, ex in AMOSTRAS:
            md.append(f'\n### Ano a ano — {nome_a}\n\n| Indicador | Ano | F | NF | n | p t | p MW exato |\n|---|---|---|---|---|---|---|')
            for ind, rot, un in PRINCIPAIS:
                for l in por_ano(dados, grupo, ind, ex):
                    md.append(f"| {rot} | {l['ano']} | {l['F']:.2f} | {l['NF']:.2f} | {l['nF']}×{l['nNF']} | {l['p_t']:.3f} | {l['p_mw']:.3f} |")
        if not prej:
            R.tabela_latex('tab-banca-amostras.tex',
                           'Comparação entre os grupos por composição da amostra (observações empresa-ano)',
                           'tab:banca-amostras', CAB_TEX, tex,
                           'F e NF: média de todas as observações empresa-ano válidas do grupo (31/12, 2018--2025), '
                           'excluídas as observações com PL negativo. Testes t de Welch e de Mann-Whitney '
                           '(exato) aplicados a cada ano separadamente; contam-se os anos com ao menos duas empresas por grupo '
                           'e aqueles em que pelo menos um dos testes é significativo. ' + OPER_TXT, 'llrrcccc')
            for nome_a, ex in (AMOSTRAS[0], AMOSTRAS[-1]):
                suf = 'completa' if not ex else 'homogenea'
                tabela_anual(dados, grupo, ex, f'tab-banca-anual-{suf}.tex',
                             f'Comparação ano a ano -- amostra {nome_a.lower()}', f'tab:banca-anual-{suf}',
                             NOTA_ANUAL.format(filtro='excluídas as observações com PL negativo')
                             + ('' if not ex else ' ' + OPER_TXT))
        else:
            R.tabela_latex('tab-banca-prejuizo.tex',
                           'Sensibilidade: exclusão também dos exercícios com prejuízo',
                           'tab:banca-prejuizo', CAB_TEX, tex,
                           'Mesmo procedimento da \\autoref{tab:banca-amostras}, excluindo também as observações '
                           'com prejuízo no exercício (ROA negativo). ' + OPER_TXT, 'llrrcccc')

    os.makedirs(os.path.dirname(SAIDA_MD), exist_ok=True)
    with open(SAIDA_MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(md) + '\n')
    print(f'ok: {SAIDA_MD}')


if __name__ == '__main__':
    main()
