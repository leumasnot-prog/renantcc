"""Atualiza as planilhas corrigidas com a conferência do Formulário de Referência 2026 (20/11/2026).

Parte de um arquivo 'TCC Atual - Cenário N (corrigido).xlsx' (qualquer cenário: a base de dados
é a mesma) e grava 'TCC Atual - Cenário K (final).xlsx' para K = 1, 2 e 3. Edita o XML do .xlsx
(mesmas rotinas de corrigir_planilhas.py), preservando gráficos, fórmulas e formatação.

Alterações:
  F1  aba Cenários: percentuais e composição conferidos no FRE 2026 (dados abertos da CVM)
  F2  Lifemed (LMED) reclassificada: fundador controla ~55% das ON por holdings e preside o CA
      -> familiar nos três cenários (a aba Cenários recalcula a classificação; Dados e
      Classificação leem dela)
  F3  base e aba Análises leem a coluna de classificação do cenário K
  F4  linhas por empresa reordenadas (familiares em cima) e faixas dos testes t e
      Mann-Whitney ajustadas ao novo número de familiares, nas abas Análises e de indicador
  F5  aba Metodologias: "(Cenário N)" -> "(Cenário K)"
  F6  Mann-Whitney: z = MAX(0; |U - n1n2/2| - 0,5) / ..., para o p-valor não passar de 1

Uso:  python3 tcc/auditoria/atualizar_planilhas_fre2026.py "caminho/do/arquivo (corrigido).xlsx"
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from lxml import etree  # noqa: E402
from corrigir_planilhas import ABAS_INDICADOR, BASE, COL_CLASSIF, N, Pacote, split_ref  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DIR = os.path.join(RAIZ, 'tcc', 'arquivos')

FAM = {
    3: ['OFSA', 'DASA', 'HAPV', 'RDOR', 'BALM', 'BLAU', 'LMED', 'PNVL', 'HYPE', 'PFRM', 'RADL'],
    2: ['BLAU', 'DASA', 'BALM', 'OFSA', 'RDOR', 'LMED', 'HAPV', 'PNVL'],
    1: ['BLAU', 'DASA', 'BALM', 'OFSA', 'RDOR', 'LMED'],
}
NAO_FAM_ORDEM = ['HAPV', 'PNVL', 'HYPE', 'PFRM', 'RADL', 'BIOM', 'AALR', 'SAUD', 'FLRY', 'QUAL']

FONTE = ' Conferido no Formulário de Referência 2026 (dados abertos da CVM, 20/11/2026).'
FRE = {  # código: (% ON da família, composição)
    'DASA': (84.95, 'Família Godoy Bueno, bloco de controle: FIP Genoma III 50,58% + FIP Genoma II 14,19% + '
                    'Genoma PG FIA 4,87% + fundos 1122-SF, 2019RV1 e 3921 9,37% + pessoas físicas 5,94%.'),
    'BALM': (89.22, 'Condustil (holding da família) 50,42% + Ruy Salvari Baumer 32,91% + Mônica Salvari '
                    'Baumer 5,89%; Ruy é presidente do CA e diretor-presidente.'),
    'OFSA': (56.72, 'Fundadores em acordo de acionistas: Jardel Massari 28,76% + Norival Bonamichi 27,97%.'),
    'HAPV': (39.73, 'Família Pinheiro (Koren de Lima), bloco de controle: PPAR Pinheiro Participações 34,09% + '
                    'Pedro e Eugenia Part. 1,74% + pessoas físicas 3,91%.'),
    'PNVL': (44.06, 'Famílias Mottin, Weber e Pizzato, bloco de controle por acordo de acionistas: 44,06%.'),
    'RADL': (24.68, 'Famílias Pipponzi, Pires Oliveira Dias/Galvão e Zagottis, bloco de controle por acordo de '
                    'acionistas: 24,68%; familiares no CA.'),
    'PFRM': (27.94, 'BMK Participações (família Birmarcker) 25,57% + Manoel, Sammy e Cacilda Birmarcker 2,37%; '
                    'BPL Brazil (Cencora) 38,18% integra o acordo de acionistas, sem ser controladora.'),
    'LMED': (55.18, 'Fundador Franco Pallamolla: Lifemed Administração e Participações 41,36% + Kumla SP '
                    'Participações 13,82% (ambas controladas por ele); preside o CA.'),
}


def ordem(k):
    f = FAM[k]
    return f, [t for t in NAO_FAM_ORDEM if t not in f]


def atualizar(origem, k):
    p = Pacote(origem)
    fam, nfam = ordem(k)
    nF, seq = len(fam), fam + nfam
    assert len(seq) == 16, seq
    col = COL_CLASSIF[k]
    log = []

    # F1/F2 – aba Cenários (E: classificação inicial, F: %, G: composição, H/I/J: controle, CA, CEO/chairman)
    ce = p.aba('Cenários')
    achados = set()
    for row in ce.data.iterfind(N + 'row'):
        r = int(row.get('r'))
        cod = ce.valor(f'B{r}')
        if cod in FRE:
            pct, comp = FRE[cod]
            c = ce.cell(f'F{r}')
            st = c.get('s')
            for ch in list(c):
                c.remove(ch)
            c.attrib.pop('t', None)
            if st:
                c.set('s', st)

            etree.SubElement(c, N + 'v').text = repr(pct)
            ce.set_texto(f'G{r}', comp + FONTE, ce.estilo(f'G{r}'))
            achados.add(cod)
            if cod == 'LMED':
                ce.set_texto(f'E{r}', 'Familiar', ce.estilo(f'E{r}'))
                for cc in 'HIJ':
                    ce.set_texto(f'{cc}{r}', 'Sim', ce.estilo(f'{cc}{r}'))
    assert achados == set(FRE), set(FRE) - achados
    log.append('F1/F2 Cenários: percentuais do FRE 2026; LMED familiar')

    # F3 – base lê a coluna do cenário K
    base = p.aba(BASE)
    for c in base.data.iter(N + 'c'):
        cc, _ = split_ref(c.get('r'))
        f = c.find(N + 'f')
        if cc == 'B' and f is not None and "'Classificação'!" in (f.text or ''):
            f.text = re.sub(r"'Classificação'!([A-Z]):\1\)$", f"'Classificação'!{col}:{col})", f.text)
            v = c.find(N + 'v')
            if v is not None:
                c.remove(v)

    # F4 – Análises
    an = p.aba('Análises')
    sF, eF, sN, eN = 20, 19 + nF, 20 + nF, 35
    for i, t in enumerate(seq):
        an.set_texto(f'C{20 + i}', t, an.estilo(f'C{20 + i}'))
        c = an.cell(f'D{20 + i}')
        f = c.find(N + 'f')
        if f is not None and f.text:
            f.text = re.sub(r"'Classificação'!([A-Z]):\1", f"'Classificação'!{col}:{col}", f.text)
            v = c.find(N + 'v')
            if v is not None:
                c.remove(v)
    an.set_formula('D38', f'_xlfn.T.TEST(M{sF}:M{eF},M{sN}:M{eN},2,3)', estilo=an.estilo('D38'))
    an.set_formula('D42', f'COUNT(M{sF}:M{eF})', estilo=an.estilo('D42'))
    an.set_formula('D43', f'COUNT(M{sN}:M{eN})', estilo=an.estilo('D43'))
    an.set_formula('D44', f'SUM(N{sF}:N{eF})', estilo=an.estilo('D44'))
    for cc, (cm, cp) in zip('DEF', (('O', 'R'), ('P', 'S'), ('Q', 'T'))):
        an.set_formula(f'{cc}51', f'_xlfn.T.TEST({cm}{sF}:{cm}{eF},{cm}{sN}:{cm}{eN},2,3)', estilo=an.estilo(f'{cc}51'))
        an.set_formula(f'{cc}52', f'COUNT({cm}{sF}:{cm}{eF})', estilo=an.estilo(f'{cc}52'))
        an.set_formula(f'{cc}53', f'COUNT({cm}{sN}:{cm}{eN})', estilo=an.estilo(f'{cc}53'))
        an.set_formula(f'{cc}54', f'SUM({cp}{sF}:{cp}{eF})', estilo=an.estilo(f'{cc}54'))
    log.append(f'F4 Análises: F linhas {sF}-{eF}, NF {sN}-{eN}')

    # F4 – abas de indicador
    sF, eF, sN, eN = 36, 35 + nF, 36 + nF, 51
    for nome in ABAS_INDICADOR:
        a = p.aba(nome)
        for i, t in enumerate(seq):
            a.set_texto(f'A{36 + i}', t, a.estilo(f'A{36 + i}'))
        a.set_formula('D54', f'_xlfn.T.TEST(AH{sF}:AH{eF},AH{sN}:AH{eN},2,3)', estilo=a.estilo('D54'))
        a.set_formula('D58', f'COUNT(AH{sF}:AH{eF})', estilo=a.estilo('D58'))
        a.set_formula('D59', f'COUNT(AH{sN}:AH{eN})', estilo=a.estilo('D59'))
        a.set_formula('D60', f'SUM(AI{sF}:AI{eF})', estilo=a.estilo('D60'))
    log.append(f'F4 abas de indicador: F linhas {sF}-{eF}, NF {sN}-{eN}')

    # F6 – Mann-Whitney: z não pode ser negativo (com U no centro, |U - média| - 0,5 < 0 dava p > 1)
    n_fix = 0
    for nome in ['Análises'] + ABAS_INDICADOR:
        a = p.aba(nome)
        for f in a.data.iter(N + 'f'):
            if f.text and '(ABS(' in f.text and '-0.5)' in f.text and 'MAX(0,' not in f.text:
                f.text = re.sub(r'\(ABS\(([^()]*)\)-0\.5\)', r'MAX(0,ABS(\1)-0.5)', f.text)
                n_fix += 1
    log.append(f'F6 Mann-Whitney: {n_fix} fórmulas de z corrigidas')

    # F5 – Metodologias
    me = p.aba('Metodologias')
    for c in list(me.data.iter(N + 'c')):
        if c.get('t') not in ('s', 'inlineStr'):
            continue
        txt = me.valor(c.get('r'))
        novo = re.sub(r'\(Cenário \d\)', f'(Cenário {k})', txt or '')
        if novo != txt:
            me.set_texto(c.get('r'), novo, c.get('s'))
    log.append('F5 Metodologias')

    destino = os.path.join(DIR, f'TCC Atual - Cenário {k} (final).xlsx')
    p.salvar(destino)
    return destino, log


if __name__ == '__main__':
    origem = sys.argv[1]
    os.makedirs(DIR, exist_ok=True)
    for k in (3, 2, 1):
        d, log = atualizar(origem, k)
        print(os.path.basename(d))
        for linha in log:
            print('   ', linha)
