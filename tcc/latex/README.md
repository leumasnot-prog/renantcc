# TCC em LaTeX (abnTeX2)

Fonte oficial do texto do TCC a partir de 06/11/2026. O Word (`TCC - Entrega 1_corrigido_Maisa.docx`)
fica como histórico.

## Estrutura

| Arquivo | Conteúdo |
|---|---|
| `main.tex` | Preâmbulo, dados da capa e da folha de rosto, ordem dos capítulos |
| `pretextuais/resumo.tex`, `pretextuais/abstract.tex` | Resumo (NBR 6028) e Abstract |
| `capitulos/01-introducao.tex` … `05-consideracoes.tex` | Um arquivo por capítulo |
| `referencias.bib` | Referências (BibTeX). Os comentários mostram o que foi verificado |
| `figuras/` | Gráficos exportados do Google Planilhas (PDF ou PNG) |
| `build/main.pdf` | PDF gerado (não vai para o Git) |

## Compilar

- **Aqui no Claude Code (nuvem):** o TeX Live já está instalado. Rode `make` dentro de `tcc/latex`.
- **No GitHub:** todo push que altera `tcc/latex/` compila sozinho. O PDF fica em
  *Actions > Compilar TCC > (última execução) > Artifacts > tcc-pdf*.
- **No Overleaf (editor on-line, sem instalar nada):** *New Project > Import from GitHub*, ou envie a
  pasta `tcc/latex` como .zip. Em *Menu*, defina o arquivo principal como `main.tex`. O Overleaf já
  tem o abnTeX2.
- **No seu computador:** instale o TeX Live (Linux/Windows) ou o MacTeX e rode `latexmk` nesta pasta.
  O VS Code com a extensão *LaTeX Workshop* compila ao salvar.

## Comandos que você vai usar

| Para | Escreva |
|---|---|
| Citação entre parênteses: (SANTOS; SILVA, 2018) | `\cite{santos2018}` |
| Citação no texto: Santos e Silva (2018) | `\citeonline{santos2018}` |
| Duas obras: (AMES et al., 2020; SANTOS; SILVA, 2018) | `\cite{ames2020,santos2018}` |
| Página na citação direta: (JENSEN, 1986, p. 324) | `\cite[p.~324]{jensen1986}` |
| Itálico / negrito | `\textit{...}` / `\textbf{...}` |
| Porcentagem | `15\%` (o `%` sozinho inicia um comentário) |
| Referência cruzada | `\autoref{qua:amostra}`, `\autoref{sec:risco}` |
| Pendência no texto (sai em vermelho) | `\verificar{...}` e `\decidir{...}` |

## Versão final

Em `main.tex`, troque `\revisaotrue` por `\revisaofalse`. Os marcadores `[VERIFICAR]` e `[DECIDIR]` e as
notas "Citado na página…" das referências deixam de aparecer. Antes disso, resolva cada marcador
(procure por `\verificar` e `\decidir` nos arquivos).

## Observações de norma

- As citações seguem o abntex2cite (autor-data, sobrenome em maiúsculas entre parênteses), o que atende
  à NBR 10520. A versão de 2023 da norma também aceita maiúsculas e minúsculas; se a orientadora
  preferir esse formato, dá para ajustar depois.
- A lista de ilustrações e a de tabelas estão desligadas em `main.tex` até existirem figuras e tabelas.
- A ficha catalográfica e a folha de aprovação estão comentadas em `main.tex`. Ative-as se o curso exigir.
