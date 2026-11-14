"""Converte o TCC (LaTeX/abnTeX2) para .docx no padrão ABNT.

Resolve citações (autor-data), referências cruzadas e tabelas geradas antes de chamar o
pandoc, e depois ajusta o Word (Times 12, 1,5, recuo 1,25 cm, margens 3/2 cm, número da
página no canto superior direito, títulos de capítulo em 14 pt).

Uso (em tcc/latex, depois de compilar o PDF com `make`):
    python3 ferramentas/para_docx.py   ->  build/TCC_Renan_Ribeiro.docx
"""
import os, re, subprocess, sys

AQUI = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
B = os.path.join(AQUI, 'build')

def ler(p): return open(os.path.join(AQUI, p), encoding='utf-8').read()

# ---------------------------------------------------------------- bib -> citações
def parse_bib(txt):
    ent = {}
    for m in re.finditer(r'@\w+\{([^,]+),(.*?)\n\}', txt, re.S):
        k, body = m.group(1).strip(), m.group(2)
        def campo(n):
            mm = re.search(n + r'\s*=\s*\{(.*?)\},?\s*\n', body, re.S)
            return mm.group(1) if mm else ''
        ent[k] = (campo('author'), campo('year'))
    return ent

def sobrenomes(autor):
    out = []
    for a in re.split(r'\s+and\s+', autor):
        a = a.strip()
        if a.startswith('{{') or (a.startswith('{') and ',' not in a):
            out.append(('corp', a.strip('{}')))
        else:
            s = a.split(',')[0].strip().strip('{}')
            out.append(('pes', s))
    return out

def cit_par(ent, k):
    a, y = ent[k]; s = sobrenomes(a)
    if s[0][0] == 'corp':
        nomes = '; '.join(n.upper() for _, n in s)
    elif len(s) > 3:
        nomes = s[0][1].upper() + ' et al.'
    else:
        nomes = '; '.join(n.upper() for _, n in s)
    return f'{nomes}, {y}'

def cit_txt(ent, k):
    a, y = ent[k]; s = sobrenomes(a)
    if s[0][0] == 'corp':
        nomes = ' e '.join(n for _, n in s)
    elif len(s) > 3:
        nomes = s[0][1] + ' et al.'
    elif len(s) == 3:
        nomes = f'{s[0][1]}, {s[1][1]} e {s[2][1]}'
    else:
        nomes = ' e '.join(n for _, n in s)
    return f'{nomes} ({y})'

# ---------------------------------------------------------------- rótulos
def labels():
    lab = {}
    for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}', open(os.path.join(B, 'main.aux'), encoding='utf-8').read()):
        lab[m.group(1)] = m.group(2)
    return lab

PREF = {'cap': 'Capítulo', 'sec': 'seção', 'qua': 'Quadro', 'tab': 'Tabela', 'fig': 'Figura', 'an': 'Anexo'}

# ---------------------------------------------------------------- utilidades
def remover_cmd(s, cmd):
    while True:
        i = s.find('\\' + cmd + '{')
        if i < 0: return s
        j, d = i + len(cmd) + 2, 1
        while d:
            d += {'{': 1, '}': -1}.get(s[j], 0); j += 1
        s = s[:i] + s[j:]

def arg(s, i):
    """devolve (conteúdo, fim) do grupo {...} que começa em s[i]=='{'"""
    j, d = i + 1, 1
    while d:
        d += {'{': 1, '}': -1}.get(s[j], 0); j += 1
    return s[i + 1:j - 1], j

def inline_inputs(s):
    def rep(m):
        p = m.group(1)
        if not p.endswith('.tex'): p += '.tex'
        return inline_inputs(ler(p))
    return re.sub(r'\\input\{([^}]+)\}', rep, s)

def esc(t):
    for c in '\\&%_#$~^{}':
        t = t.replace(c, '\\' + c if c not in '\\~^' else {'\\': '\\textbackslash{}', '~': '\\textasciitilde{}', '^': '\\textasciicircum{}'}[c])
    return t

def sem_comentarios(s):
    return '\n'.join(re.sub(r'(?<!\\)%.*$', '', l) for l in s.split('\n'))

# ---------------------------------------------------------------- floats
def floats(s, lab):
    out, i = [], 0
    pat = re.compile(r'\\begin\{(quadro|table|figure)\}(\[[^\]]*\])?')
    while True:
        m = pat.search(s, i)
        if not m: out.append(s[i:]); break
        out.append(s[i:m.start()])
        env = m.group(1); fim = s.index('\\end{' + env + '}', m.end())
        corpo = s[m.end():fim]; i = fim + len('\\end{' + env + '}')
        cap_i = corpo.find('\\caption{'); cap, _ = arg(corpo, cap_i + 8)
        lm = re.search(r'\\label\{([^}]+)\}', corpo); num = lab.get(lm.group(1), '?') if lm else '?'
        nome = {'quadro': 'Quadro', 'table': 'Tabela', 'figure': 'Figura'}[env]
        partes = [f'\n\n\\begin{{center}}\\textbf{{{nome} {num} -- {cap}}}\\end{{center}}\n\n']
        tb = re.search(r'\\begin\{(tabularx|tabular)\}(\{\\textwidth\})?\{([^\n]*?)\}\n(.*?)\\end\{\1\}', corpo, re.S)
        if tb:
            spec = re.sub(r'P\{[^}]*\}|L|p\{[^}]*\}|X', 'l', tb.group(3))
            linhas = tb.group(4)
            linhas = linhas.replace('\\toprule', '\\hline').replace('\\midrule', '\\hline').replace('\\bottomrule', '\\hline')
            linhas = re.sub(r'\\multicolumn\{\d+\}\{[^}]*\}\{([^}]*)\}', r'\1 &', linhas)
            partes.append(f'\\begin{{tabular}}{{{spec}}}\n{linhas}\\end{{tabular}}\n\n')
        g = re.search(r'\\includegraphics(\[[^\]]*\])?\{([^}]+)\}', corpo)
        if g:
            png = g.group(2).replace('.pdf', '.png')
            subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', os.path.join(AQUI, g.group(2)),
                            os.path.join(AQUI, png[:-4])], check=True)
            partes.append(f'\\includegraphics{{{png}}}\n\n')
        for cmd, rot in (('fonte', 'Fonte'), ('nota', 'Nota')):
            k = corpo.find('\\' + cmd + '{')
            if k >= 0:
                txt, _ = arg(corpo, k + len(cmd) + 1)
                txt = txt.strip()
                if cmd == 'fonte' and txt.lower().startswith('fonte'): pass
                partes.append(f'\\begin{{center}}{{\\small {rot}: {txt}}}\\end{{center}}\n\n')
        out.append(''.join(partes))
    return ''.join(out)

# ---------------------------------------------------------------- principal
def main():
    ent = parse_bib(ler('referencias.bib')); lab = labels()
    corpo = ''
    caps = ['01-introducao', '02-referencial', '03-metodologia', '04-resultados', '05-consideracoes']
    for c in caps:
        corpo += ler(f'capitulos/{c}.tex') + '\n\n'
    corpo = sem_comentarios(inline_inputs(sem_comentarios(corpo)))
    for c in ('verificar', 'decidir'): corpo = remover_cmd(corpo, c)
    corpo = floats(corpo, lab)

    def rcite(m):
        pre, ks = m.group(1), [k.strip() for k in m.group(2).split(',')]
        return '(' + '; '.join(cit_par(ent, k) for k in ks) + (', ' + pre if pre else '') + ')'
    corpo = re.sub(r'\\cite(?:\[([^\]]*)\])?\{([^}]+)\}', rcite, corpo)
    corpo = re.sub(r'\\citeonline\{([^}]+)\}', lambda m: '; '.join(cit_txt(ent, k.strip()) for k in m.group(1).split(',')), corpo)

    def rauto(m):
        k = m.group(1); p = k.split(':')[0]
        return f'{PREF.get(p, "")} {lab.get(k, "?")}'.strip()
    corpo = re.sub(r'\\autoref\{([^}]+)\}', rauto, corpo)
    corpo = re.sub(r'\\ref\{([^}]+)\}', lambda m: lab.get(m.group(1), '?'), corpo)
    corpo = corpo.replace('\\begin{alineas}', '\\begin{itemize}').replace('\\end{alineas}', '\\end{itemize}')
    corpo = re.sub(r'\\label\{[^}]+\}', '', corpo)

    # numeração manual dos títulos (ABNT: capítulo em caixa alta)
    n = [0, 0]
    def rcap(m):
        n[0] += 1; n[1] = 0
        return f'\\chapter*{{{n[0]} {m.group(1).upper()}}}'
    def rsec(m):
        n[1] += 1
        return f'\\section*{{{n[0]}.{n[1]} {m.group(1)}}}'
    corpo = re.sub(r'\\chapter\{([^}]*)\}', rcap, corpo)
    corpo = re.sub(r'\\section\{([^}]*)\}', rsec, corpo)

    # resumo e abstract
    def bloco(p, titulo):
        t = sem_comentarios(ler(p))
        t = re.sub(r'\\begin\{resumo\}(\[[^\]]*\])?|\\end\{resumo\}|\\begin\{otherlanguage\*\}\{english\}|\\end\{otherlanguage\*\}|\\vspace\{[^}]*\}|\\noindent', '', t)
        t = re.sub(r'\\citeonline\{([^}]+)\}', lambda m: cit_txt(ent, m.group(1)), t)
        return f'\\chapter*{{{titulo}}}\n{t}\n'
    pre = bloco('pretextuais/resumo.tex', 'RESUMO') + bloco('pretextuais/abstract.tex', 'ABSTRACT')

    # referências: texto do PDF já formatado pelo abntex2cite
    txt = subprocess.run(['pdftotext', os.path.join(B, 'main.pdf'), '-'], capture_output=True, text=True).stdout
    i = txt.rfind('\nREFERÊNCIAS\n'); f = txt.find('\nANEXOS', i)
    refs = re.sub(r'\n\d+\n', '\n', txt[i + 13:f]).strip()
    refs = [re.sub(r'\s*\n\s*', ' ', r).strip() for r in re.split(r'\n\s*\n', refs) if r.strip()]
    refs = [r for r in refs if not re.fullmatch(r'\d+', r)]
    reftex = '\\chapter*{REFERÊNCIAS}\n' + '\n\n'.join(esc(r) for r in refs)

    # anexos
    an = sem_comentarios(ler('capitulos/anexos.tex'))
    an = an.replace('\\begin{alineas}', '\\begin{itemize}').replace('\\end{alineas}', '\\end{itemize}')
    an = re.sub(r'\\autoref\{([^}]+)\}', rauto, an)
    an = re.sub(r'\\label\{[^}]+\}', '', an)
    letras = iter('AB')
    an = re.sub(r'\\chapter\{([^}]*)\}', lambda m: f'\\chapter*{{ANEXO {next(letras)} -- {m.group(1).upper()}}}', an)
    an = re.sub(r'\\section\*\{[^}]*\}\s*\\lstinputlisting\{anexos/([^}]+)\}', lambda m: '\\begin{itemize}\\item ' + m.group(1).replace('_', '\\_') + '\\end{itemize}', an)
    an += '\n\nO código completo de cada programa está nos arquivos acima, entregues em formato eletrônico junto com a planilha.\n'

    doc = ('\\documentclass{report}\n\\begin{document}\n' + pre + corpo + reftex + '\n' + an + '\n\\end{document}\n')
    tmp = os.path.join(B, 'tcc_docx.tex'); open(tmp, 'w', encoding='utf-8').write(doc)
    saida = os.path.join(B, 'TCC_Renan_Ribeiro.docx')
    subprocess.run(['pandoc', tmp, '-f', 'latex', '-o', saida, '--resource-path', AQUI,
                    '--reference-doc', os.path.join(AQUI, 'ferramentas', 'referencia.docx')], check=True)
    ajustar(saida)
    print(saida)

# ---------------------------------------------------------------- formatação Word
def ajustar(caminho):
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
    d = Document(caminho)
    for s in d.sections:
        s.top_margin = s.left_margin = Cm(3); s.bottom_margin = s.right_margin = Cm(2)
        s.header_distance = Cm(2)
        p = s.header.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run()
        for t, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
            if t:
                el = OxmlElement('w:fldChar'); el.set(qn('w:fldCharType'), t); r._r.append(el)
            else:
                el = OxmlElement('w:instrText'); el.text = txt; r._r.append(el)
        r.font.name = 'Times New Roman'; r.font.size = Pt(10)
    for p in d.paragraphs:
        st = p.style.name
        f = p.paragraph_format
        if st.startswith('Heading'):
            lvl = 14 if st == 'Heading 1' else 12
            for r in p.runs:
                r.font.size = Pt(lvl); r.font.bold = True; r.font.name = 'Times New Roman'
                r.font.color.rgb = RGBColor(0, 0, 0)
            f.space_before = Pt(12 if st == 'Heading 1' else 18); f.space_after = Pt(12)
            if st == 'Heading 1': f.page_break_before = True
            continue
        if st in ('Source Code',):
            for r in p.runs: r.font.size = Pt(7)
            continue
        f.line_spacing = 1.5; f.space_before = Pt(0); f.space_after = Pt(0)
        if p.alignment is None and st in ('Body Text', 'First Paragraph', 'Normal'):
            f.first_line_indent = Cm(1.25); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p.runs:
            r.font.name = 'Times New Roman'
            if r.font.size is None: r.font.size = Pt(12)
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    p.paragraph_format.line_spacing = 1.0; p.paragraph_format.first_line_indent = None
                    for r in p.runs: r.font.size = Pt(10); r.font.name = 'Times New Roman'
    capa(d)
    d.save(caminho)


def capa(d):
    """Insere capa e folha de rosto antes do primeiro parágrafo."""
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.shared import Pt
    primeiro = d.paragraphs[0]
    def linha(txt, tam=12, negrito=False, antes=0, quebra=False):
        p = primeiro.insert_paragraph_before()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(antes); p.paragraph_format.first_line_indent = None
        p.paragraph_format.line_spacing = 1.5
        if txt:
            r = p.add_run(txt); r.font.size = Pt(tam); r.bold = negrito; r.font.name = 'Times New Roman'
        if quebra:
            p.add_run().add_break(WD_BREAK.PAGE)
        return p
    inst = ['UNIVERSIDADE DE SÃO PAULO', 'FACULDADE DE ECONOMIA, ADMINISTRAÇÃO E CONTABILIDADE', 'DE RIBEIRÃO PRETO', 'DEPARTAMENTO DE CONTABILIDADE']
    titulo = 'EMPRESAS FAMILIARES VS. NÃO FAMILIARES: COMPORTAMENTOS DE ENDIVIDAMENTO'
    for t in inst: linha(t, negrito=True)
    linha('RENAN DO AMARAL RIBEIRO', antes=80)
    linha(titulo, 14, True, antes=110)
    linha('Ribeirão Preto', antes=140); linha('2026', quebra=True)
    linha('RENAN DO AMARAL RIBEIRO')
    linha(titulo, 14, True, antes=150)
    p = linha('', antes=60)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Pt(226); p.paragraph_format.line_spacing = 1.0
    r = p.add_run('Trabalho de Conclusão de Curso apresentado ao Departamento de Contabilidade da Faculdade de '
                  'Economia, Administração e Contabilidade de Ribeirão Preto da Universidade de São Paulo, como '
                  'requisito parcial para a obtenção do título de Bacharel em Ciências Contábeis.')
    r.font.size = Pt(10); r.font.name = 'Times New Roman'
    linha('Orientadora: Profa. Dra. Maisa Ribeiro', antes=40)
    linha('Ribeirão Preto', antes=110); linha('2026')


if __name__ == '__main__':
    main()
