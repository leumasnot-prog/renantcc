# Repositório do TCC — instruções para o Claude

> **Leia primeiro `tcc/CONTEXTO_TCC.md`**: resumo do projeto (tema, amostra, cenários,
> resultados, erros conhecidos nas planilhas e regras de trabalho com o autor). As regras
> da seção 14 dele valem para todas as tarefas deste repositório, inclusive para as skills ARS.

Este repositório é usado para desenvolver o TCC do autor. Ele traz instalado o
plugin **Academic Research Skills (ARS)**, uma adaptação em pt-BR de
[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
(licença CC BY-NC 4.0). O código do plugin fica em `ars/` e é ativado por
`.claude/settings.json`.

## Idioma
- Responda sempre em **português do Brasil**, inclusive dentro das skills ARS.
- Termos técnicos sem tradução consolidada podem aparecer entre parênteses em inglês
  na primeira ocorrência (ex.: "revisão de escopo (*scoping review*)").
- No resumo bilíngue (modo `abstract-only` ou etapa final), use **Resumo em
  português + Abstract em inglês**. O padrão do ARS é zh-TW + EN; não use chinês.

## Normas acadêmicas (Brasil)
- O ARS formata nativamente em APA 7, Chicago, MLA, IEEE e Vancouver. Ele **não**
  tem ABNT embutido.
- Para o TCC, o padrão é **ABNT**: NBR 6023 (referências), NBR 10520 (citações),
  NBR 14724 (trabalhos acadêmicos), NBR 6028 (resumo), NBR 6027 (sumário). Trabalhe
  internamente em APA 7 (autor-data, que é o mais próximo do sistema autor-data da
  ABNT) e, na entrega, converta citações e referências para ABNT, salvo se o
  usuário pedir outra norma ou se o manual da instituição disser outra coisa.
- Estrutura padrão do TCC: Introdução, Referencial Teórico, Metodologia,
  Resultados e Discussão, Considerações Finais e Referências. Adapte ao modelo do
  curso quando o usuário informar.

## Regras de integridade (não negociáveis)
- Nunca invente referências, DOIs, páginas ou citações. Toda fonte precisa ser
  verificável. Se não der para verificar, marque claramente como não verificada.
- O texto do TCC é do autor. As skills orientam, revisam e estruturam; o autor
  decide e assume a autoria. Lembre o usuário de conferir as regras da instituição
  sobre uso de IA e de declarar esse uso quando for exigido (`/ars-disclosure`).

## Texto do TCC: LaTeX (abnTeX2)
- A fonte oficial do texto é `tcc/latex/` (desde 06/11/2026). Edite os capítulos em
  `tcc/latex/capitulos/*.tex` e as referências em `tcc/latex/referencias.bib`.
  `tcc/redacao/*.md` e o Word são histórico: não edite.
- Compile com `make` em `tcc/latex` e confira que não há erros (`grep '^!' build/main.log`).
  Se o TeX Live não estiver instalado na sessão, instale com:
  `apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-publishers texlive-lang-portuguese texlive-fonts-recommended lmodern latexmk`.
- Citações com `\cite{}` / `\citeonline{}`; pendências com `\verificar{}` e `\decidir{}`.
  Detalhes em `tcc/latex/README.md`.

## Planilhas
- Em 07/11/2026 os erros da seção 10 do `tcc/CONTEXTO_TCC.md` foram corrigidos nas cópias
  `tcc/arquivos/TCC Atual - Cenário N (corrigido).xlsx` (script `tcc/auditoria/corrigir_planilhas.py`;
  detalhes e o que ficou pendente em `tcc/auditoria/ROTEIRO_CORRECAO_PLANILHAS.md`).
- Os números do TCC saem de `tcc/analise/resultados_c3.py`, que lê a base e gera `tcc/latex/tabelas/`.
- Os gráficos do Cap. 4 saem de `tcc/analise/graficos.py` (PDF em `tcc/latex/figuras/`), a pedido do autor em 11/11/2026.

## Organização sugerida
- `tcc/latex/` — texto do TCC em LaTeX.
- `tcc/referencias/` — BibTeX/RIS exportados do Zotero/Mendeley e PDFs de apoio.
- `tcc/ars-saidas/` — relatórios gerados pelas skills (Material Passport,
  pareceres, relatórios de integridade).

Guia completo de uso em português: `GUIA-ARS.md`.
