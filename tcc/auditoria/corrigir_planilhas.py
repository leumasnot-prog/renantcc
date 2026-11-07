"""Aplica as correções da auditoria às planilhas 'TCC Atual - Cenário N.xlsx'.

Edita diretamente o XML de dentro do .xlsx (sem openpyxl), para preservar os gráficos,
as fórmulas de matriz do Google Planilhas e a formatação. Grava cópias
'TCC Atual - Cenário N (corrigido).xlsx' ao lado dos originais, que não são alterados.

Correções (numeração de tcc/auditoria/ROTEIRO_CORRECAO_PLANILHAS.md):
  C1  base do Cenário 1 passa a ler a coluna do Cenário 1 (I) da aba Classificação
  C2  aba Análises dos Cenários 1 e 2 passa a ler a coluna do próprio cenário
  C3  linhas por empresa reordenadas (familiares em cima) e faixas dos testes ajustadas ao cenário
  C4  testes das abas de indicador passam a usar a média anual (31/12) por empresa
  C5  testes com observações não independentes (empresa-trimestre e empresa-ano) removidos
  C6  aba Div Liq x Pl: média da empresa no período completo (era só 2021-2023)
  C7  rótulos "(10 F × 5 NF)" passam a ser calculados
  C8  aba Análises ganha os testes por subperíodo (pré, pandemia, pós)
  C9  aba Classificação: subsetor de BLAU, HYPE e EUFA; PGMN familiar nos Cenários 1 e 2
  C10 aba Metodologias: referências de células e cenário atualizados

Uso: python3 tcc/auditoria/corrigir_planilhas.py
"""
from __future__ import annotations

import os
import re
import shutil
import zipfile

from lxml import etree

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DIR = os.path.join(RAIZ, 'tcc', 'arquivos')
NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
N = '{%s}' % NS
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

ABAS_INDICADOR = ['Div Bruta x Atv t', 'Exigivel T x Atv t', 'Estr de Cap', 'Div Liq x Ebitda',
                  'Exig T x Pat Liq', 'Div Brut x Pl', 'Div Liq x Pl']
BASE = 'Saúde - 1218 à 1225'

FAM = {
    3: ['OFSA', 'DASA', 'HAPV', 'RDOR', 'BALM', 'BLAU', 'PNVL', 'HYPE', 'PFRM', 'RADL'],
    2: ['BLAU', 'DASA', 'BALM', 'OFSA', 'RDOR', 'HAPV', 'PNVL'],
    1: ['BLAU', 'DASA', 'BALM', 'OFSA', 'RDOR'],
}
NAO_FAM_ORDEM = ['HAPV', 'PNVL', 'HYPE', 'PFRM', 'RADL', 'BIOM', 'AALR', 'SAUD', 'FLRY', 'QUAL', 'LMED']
COL_CLASSIF = {1: 'I', 2: 'J', 3: 'K'}


# ------------------------------------------------------------------ utilitários de célula
def col_num(letras):
    n = 0
    for ch in letras:
        n = n * 26 + ord(ch) - 64
    return n


def split_ref(ref):
    m = re.match(r'([A-Z]+)(\d+)$', ref)
    return m.group(1), int(m.group(2))


class Aba:
    def __init__(self, xml_bytes, shared):
        self.tree = etree.fromstring(xml_bytes)
        self.data = self.tree.find(N + 'sheetData')
        self.shared = shared

    def row(self, r, criar=True):
        for el in self.data.iterfind(N + 'row'):
            rr = int(el.get('r'))
            if rr == r:
                return el
            if rr > r:
                if not criar:
                    return None
                novo = etree.Element(N + 'row', r=str(r))
                el.addprevious(novo)
                return novo
        if not criar:
            return None
        novo = etree.SubElement(self.data, N + 'row', r=str(r))
        return novo

    def cell(self, ref, criar=True):
        col, r = split_ref(ref)
        row = self.row(r, criar)
        if row is None:
            return None
        for c in row.iterfind(N + 'c'):
            cc, _ = split_ref(c.get('r'))
            if cc == col:
                return c
            if col_num(cc) > col_num(col):
                if not criar:
                    return None
                novo = etree.Element(N + 'c', r=ref)
                c.addprevious(novo)
                return novo
        if not criar:
            return None
        return etree.SubElement(row, N + 'c', r=ref)

    def valor(self, ref):
        c = self.cell(ref, criar=False)
        if c is None:
            return None
        t = c.get('t')
        if t == 's':
            return self.shared[int(c.find(N + 'v').text)]
        if t == 'inlineStr':
            return ''.join(c.find(N + 'is').itertext())
        v = c.find(N + 'v')
        return v.text if v is not None else None

    def formula(self, ref):
        c = self.cell(ref, criar=False)
        f = c.find(N + 'f') if c is not None else None
        return f.text if f is not None else None

    def _limpar(self, c, estilo, forcar=False):
        f = c.find(N + 'f')
        if not forcar and f is not None and f.get('t') == 'shared' and f.get('ref') and ':' in f.get('ref'):
            raise RuntimeError(f'{c.get("r")} é mestre de fórmula compartilhada {f.get("ref")}')
        for ch in list(c):
            c.remove(ch)
        for a in ('t',):
            if a in c.attrib:
                del c.attrib[a]
        if estilo is not None:
            c.set('s', estilo)

    def set_formula(self, ref, texto, texto_resultado=False, estilo=None, forcar=False):
        """forcar=True: sobrescreve o mestre de uma fórmula compartilhada (só quando as células
        dependentes também são removidas ou reescritas)."""
        c = self.cell(ref)
        self._limpar(c, estilo, forcar)
        if texto_resultado:
            c.set('t', 'str')
        etree.SubElement(c, N + 'f').text = texto

    def set_texto(self, ref, texto, estilo=None):
        c = self.cell(ref)
        self._limpar(c, estilo)
        c.set('t', 'inlineStr')
        etree.SubElement(etree.SubElement(c, N + 'is'), N + 't').text = texto

    def apagar(self, ref):
        c = self.cell(ref, criar=False)
        if c is not None:
            c.getparent().remove(c)

    def estilo(self, ref):
        c = self.cell(ref, criar=False)
        return c.get('s') if c is not None else None

    def xml(self):
        return etree.tostring(self.tree, xml_declaration=True, encoding='UTF-8', standalone=True)


# ------------------------------------------------------------------ pacote xlsx
class Pacote:
    def __init__(self, caminho):
        self.z = zipfile.ZipFile(caminho)
        self.arquivos = {n: self.z.read(n) for n in self.z.namelist()}
        self.ordem = self.z.namelist()
        self.shared = self._ler_shared()
        self.mapa = self._mapa_abas()
        self.abertas = {}

    def _ler_shared(self):
        if 'xl/sharedStrings.xml' not in self.arquivos:
            return []
        t = etree.fromstring(self.arquivos['xl/sharedStrings.xml'])
        return [''.join(si.itertext()) for si in t.iterfind(N + 'si')]

    def _mapa_abas(self):
        wb = etree.fromstring(self.arquivos['xl/workbook.xml'])
        rels = etree.fromstring(self.arquivos['xl/_rels/workbook.xml.rels'])
        alvo = {r.get('Id'): r.get('Target') for r in rels}
        mapa = {}
        for s in wb.iter(N + 'sheet'):
            t = alvo[s.get('{%s}id' % RNS)]
            mapa[s.get('name')] = 'xl/' + t.lstrip('/').replace('xl/', '') if not t.startswith('xl/') else t
        return mapa

    def aba(self, nome):
        if nome not in self.abertas:
            self.abertas[nome] = Aba(self.arquivos[self.mapa[nome]], self.shared)
        return self.abertas[nome]

    def salvar(self, destino):
        for nome, aba in self.abertas.items():
            self.arquivos[self.mapa[nome]] = aba.xml()
        wb = self.arquivos['xl/workbook.xml'].decode('utf-8')
        wb = re.sub(r'<calcPr[^>]*/>', '<calcPr fullCalcOnLoad="1"/>', wb)
        self.arquivos['xl/workbook.xml'] = wb.encode('utf-8')
        with zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as out:
            for n in self.ordem:
                out.writestr(n, self.arquivos[n])


# ------------------------------------------------------------------ correções
def ordem_cenario(k):
    f = FAM[k]
    nf = [t for t in NAO_FAM_ORDEM if t not in f]
    return f, nf


def corrigir(k):
    origem = os.path.join(DIR, f'TCC Atual - Cenário {k}.xlsx')
    destino = os.path.join(DIR, f'TCC Atual - Cenário {k} (corrigido).xlsx')
    p = Pacote(origem)
    fam, nfam = ordem_cenario(k)
    nF = len(fam)
    log = []

    # C1 – base do cenário lê a coluna certa da aba Classificação
    base = p.aba(BASE)
    col = COL_CLASSIF[k]
    for c in base.data.iter(N + 'c'):
        cc, _ = split_ref(c.get('r'))
        f = c.find(N + 'f')
        if cc == 'B' and f is not None and "'Classificação'!" in (f.text or ''):
            novo = re.sub(r"'Classificação'!([A-Z]):\1\)$", f"'Classificação'!{col}:{col})", f.text)
            if novo != f.text:
                f.text = novo
                v = c.find(N + 'v')
                if v is not None:
                    c.remove(v)
    log.append(f'C1 base col. B -> Classificação!{col}')

    # Análises
    an = p.aba('Análises')
    ordem = fam + nfam
    sF, eF, sN, eN = 20, 19 + nF, 20 + nF, 35
    for i, t in enumerate(ordem):
        an.set_texto(f'C{20 + i}', t, an.estilo(f'C{20 + i}'))
        c = an.cell(f'D{20 + i}')                              # C2 – grupo do próprio cenário
        f = c.find(N + 'f')
        f.text = re.sub(r"'Classificação'!([A-Z]):\1", f"'Classificação'!{col}:{col}", f.text)
        v = c.find(N + 'v')
        if v is not None:
            c.remove(v)
    an.set_formula('D38', f'_xlfn.T.TEST(M{sF}:M{eF},M{sN}:M{eN},2,3)', estilo=an.estilo('D38'))
    an.set_formula('C38', '"p-valor – médias anuais por empresa ("&D42&" F × "&D43&" NF)"', True, an.estilo('C38'))
    for ref in ('D39', 'E39', 'F39'):                       # C5 (E39 dependia de E38)
        an.apagar(ref)
    an.set_formula('E38', 'IF(D38<0.05,"Significativo a 5%",IF(D38<0.1,"Significativo a 10%","Não significativo"))',
                   True, an.estilo('E38'), forcar=True)
    an.set_texto('C39', 'Teste com observações empresa-ano removido: os anos de uma mesma empresa não são '
                 'independentes e inflam a significância.', an.estilo('C39'))
    an.set_formula('D42', f'COUNT(M{sF}:M{eF})', estilo=an.estilo('D42'))
    an.set_formula('D43', f'COUNT(M{sN}:M{eN})', estilo=an.estilo('D43'))
    an.set_formula('D44', f'SUM(N{sF}:N{eF})', estilo=an.estilo('D44'))
    log.append(f'C3 Análises: F linhas {sF}-{eF}, NF {sN}-{eN}')

    # C8 – subperíodos na aba Análises (colunas E..L = 2018..2025)
    st_h, st_n, st_r, st_lbl, st_p = an.estilo('M19'), an.estilo('M20'), an.estilo('N20'), an.estilo('C42'), an.estilo('D38')
    cab = {'O': 'Pré (2018–2019)', 'P': 'Pandemia (2020–2021)', 'Q': 'Pós (2022–2025)',
           'R': 'Posto – pré', 'S': 'Posto – pandemia', 'T': 'Posto – pós'}
    for c_, txt in cab.items():
        an.set_texto(f'{c_}19', txt, st_h)
    faixas = {'O': 'E{r}:F{r}', 'P': 'G{r}:H{r}', 'Q': 'I{r}:L{r}'}
    for r in range(20, 36):
        for c_, fx in faixas.items():
            an.set_formula(f'{c_}{r}', f'IFERROR(AVERAGE({fx.format(r=r)}),"")', estilo=st_n)
        for c_m, c_p in (('O', 'R'), ('P', 'S'), ('Q', 'T')):
            an.set_formula(f'{c_p}{r}', f'IF({c_m}{r}="","",_xlfn.RANK.AVG({c_m}{r},{c_m}$20:{c_m}$35,1))', estilo=st_r)
    an.set_texto('B49', 'Testes por subperíodo (média de cada empresa nas datas de 31/12 do subperíodo)', an.estilo('B41'))
    rotulos = {50: 'Subperíodo', 51: 'p-valor – teste t de Welch (bicaudal)', 52: 'n – familiares',
               53: 'n – não familiares', 54: 'Soma dos postos – familiares', 55: 'Estatística U',
               56: 'z (aproximação normal)', 57: 'p-valor – Mann-Whitney (bicaudal)', 58: 'Resultado – teste t',
               59: 'Resultado – Mann-Whitney'}
    for r, txt in rotulos.items():
        an.set_texto(f'C{r}', txt, st_lbl)
    for cc, (cm, cp, nome) in zip('DEF', (('O', 'R', 'Pré (2018–2019)'), ('P', 'S', 'Pandemia (2020–2021)'),
                                          ('Q', 'T', 'Pós (2022–2025)'))):
        an.set_texto(f'{cc}50', nome, st_h)
        an.set_formula(f'{cc}51', f'_xlfn.T.TEST({cm}{sF}:{cm}{eF},{cm}{sN}:{cm}{eN},2,3)', estilo=st_p)
        an.set_formula(f'{cc}52', f'COUNT({cm}{sF}:{cm}{eF})', estilo=st_r)
        an.set_formula(f'{cc}53', f'COUNT({cm}{sN}:{cm}{eN})', estilo=st_r)
        an.set_formula(f'{cc}54', f'SUM({cp}{sF}:{cp}{eF})', estilo=st_r)
        an.set_formula(f'{cc}55', f'{cc}54-{cc}52*({cc}52+1)/2', estilo=st_r)
        an.set_formula(f'{cc}56', f'(ABS({cc}55-{cc}52*{cc}53/2)-0.5)/SQRT({cc}52*{cc}53*({cc}52+{cc}53+1)/12)', estilo=st_n)
        an.set_formula(f'{cc}57', f'2*(1-_xlfn.NORM.S.DIST({cc}56,1))', estilo=st_p)
        for rr, pr in ((58, 51), (59, 57)):
            an.set_formula(f'{cc}{rr}', f'IF({cc}{pr}<0.01,"Significativo a 1%",IF({cc}{pr}<0.05,"Significativo a 5%",'
                           f'IF({cc}{pr}<0.1,"Significativo a 10%","Não significativo")))', True, an.estilo('E47'))
    log.append('C8 subperíodos em Análises!O19:T35 e testes em C49:F59')

    # Abas de indicador
    sF, eF, sN, eN = 36, 35 + nF, 36 + nF, 51
    for nome in ABAS_INDICADOR:
        a = p.aba(nome)
        for i, t in enumerate(ordem):
            a.set_texto(f'A{36 + i}', t, a.estilo(f'A{36 + i}'))
        if nome == 'Div Liq x Pl':                              # C6
            f = a.cell('AF36').find(N + 'f')
            f.text = 'IFERROR(AVERAGE(C36:AE36),"")'
        a.set_texto('AF35', 'Média trimestral (só descritiva)', a.estilo('AF35'))
        a.set_texto('AG35', 'Posto trimestral (não usado)', a.estilo('AG35'))
        a.set_texto('AH35', 'Média anual 31/12 (base dos testes)', a.estilo('AF35'))
        a.set_texto('AI35', 'Posto (Mann-Whitney)', a.estilo('AG35'))
        for r in range(36, 52):                                 # C4 – colunas de 31/12: C,G,K,O,S,W,AA,AE
            a.set_formula(f'AH{r}', f'IFERROR(AVERAGE(C{r},G{r},K{r},O{r},S{r},W{r},AA{r},AE{r}),"")',
                          estilo=a.estilo('AF36'))
            a.set_formula(f'AI{r}', f'IF(AH{r}="","",_xlfn.RANK.AVG(AH{r},$AH$36:$AH$51,1))', estilo=a.estilo('AG36'))
        a.set_formula('D54', f'_xlfn.T.TEST(AH{sF}:AH{eF},AH{sN}:AH{eN},2,3)', estilo=a.estilo('D54'))
        a.set_formula('C54', '"p-valor – médias anuais por empresa ("&D58&" F × "&D59&" NF)"', True, a.estilo('C54'))
        for ref in ('D55', 'E55', 'F55'):                   # C5 (E55 dependia de E54)
            a.apagar(ref)
        a.set_formula('E54', 'IF(D54<0.05,"Significativo a 5%",IF(D54<0.1,"Significativo a 10%","Não significativo"))',
                      True, a.estilo('E54'), forcar=True)
        a.set_texto('C55', 'Teste com observações empresa-trimestre removido: observações não independentes '
                    'inflam a significância.', a.estilo('C55'))
        a.set_formula('D58', f'COUNT(AH{sF}:AH{eF})', estilo=a.estilo('D58'))
        a.set_formula('D59', f'COUNT(AH{sN}:AH{eN})', estilo=a.estilo('D59'))
        a.set_formula('D60', f'SUM(AI{sF}:AI{eF})', estilo=a.estilo('D60'))
    log.append(f'C3/C4/C5/C7 abas de indicador: F linhas {sF}-{eF}, NF {sN}-{eN}, testes na coluna AH')

    # C9 – Classificação
    cl = p.aba('Classificação')
    for row in cl.data.iterfind(N + 'row'):
        r = int(row.get('r'))
        cod = cl.valor(f'F{r}')
        if cod in ('BLAU', 'HYPE', 'EUFA'):
            cl.set_texto(f'C{r}', 'Medicamentos e Outros Produtos', cl.estilo(f'C{r}'))
        if cod == 'PGMN':
            cl.set_texto(f'I{r}', 'Familiar', cl.estilo(f'I{r}'))
            cl.set_texto(f'J{r}', 'Familiar', cl.estilo(f'J{r}'))
    log.append('C9 Classificação: subsetor BLAU/HYPE/EUFA; PGMN familiar em C1/C2')

    # C10 – Metodologias
    me = p.aba('Metodologias')
    for c in list(me.data.iter(N + 'c')):
        ref = c.get('r')
        txt = me.valor(ref) if c.get('t') in ('s', 'inlineStr') else None
        if not txt:
            continue
        novo = txt
        if 'C37 (principal)' in novo:
            novo = ('Análises!D38 (principal): uma observação por empresa (média das oito datas de 31/12 de '
                    '2018 a 2025), garantindo independência entre as observações. Nas abas de indicador, o mesmo '
                    'teste está em D54, sobre a coluna AH. Os testes com observações empresa-ano e '
                    'empresa-trimestre foram removidos, pois as observações de uma mesma empresa não são '
                    'independentes e inflam a significância.')
        novo = novo.replace('(Cenário 3)', f'(Cenário {k})')
        novo = novo.replace('conforme sua média 2018–2025', 'conforme sua média das datas de 31/12 de 2018–2025')
        if novo != txt:
            me.set_texto(ref, novo, c.get('s'))
    log.append('C10 Metodologias atualizada')

    p.salvar(destino)
    return destino, log


if __name__ == '__main__':
    for k in (3, 2, 1):
        d, log = corrigir(k)
        print(os.path.basename(d))
        for linha in log:
            print('   ', linha)
