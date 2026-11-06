# Guia do ARS (Academic Research Skills) para o TCC

Este guia explica como funcionam as skills instaladas neste repositório e como
usá-las em cada fase do TCC. As skills são uma adaptação em pt-BR de
[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
v3.24.2, de Cheng-I Wu, sob licença CC BY-NC 4.0. Detalhes da adaptação estão em
`TRADUCAO.md`.

---

## 1. Como a instalação funciona

- O código completo do plugin fica em `ars/` (skills, agentes, protocolos em
  `ars/shared/`, scripts Python de verificação em `ars/scripts/`).
- O arquivo `.claude/settings.json` registra `ars/` como um *marketplace* local
  (`ars-ptbr`) e ativa o plugin `academic-research-skills@ars-ptbr`.
- Ao abrir o repositório no Claude Code (terminal, desktop ou web), o Claude
  pergunta se você confia nas configurações do projeto. **Aceite**: só então o
  plugin é carregado. Se não carregar, rode no terminal, a partir da raiz do
  repositório:

```bash
claude plugin marketplace add ./ars --scope project
```

```bash
claude plugin install academic-research-skills@ars-ptbr --scope project
```

- Para conferir se carregou: digite `/` no Claude Code e procure os comandos
  `/ars-...`, ou rode `claude plugin details academic-research-skills@ars-ptbr`.

O que vem com o plugin:

| Componente | Quantidade | Para que serve |
|---|---|---|
| Skills | 5 | `deep-research`, `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `sr-screener` |
| Modos | 35 | Variações de cada skill (ver seção 3) |
| Comandos `/ars-*` | 16 | Atalhos que abrem uma skill direto em um modo |
| Agentes de plugin | 4 | Síntese, arquitetura metodológica, compilação de relatório, revisor de triagem |
| Hooks | 2 | Aviso ao iniciar a sessão + guarda que impede agentes de gravar fora do escopo |

---

## 2. Ideia central: como as skills "pensam"

1. **Você não precisa decorar comandos.** Basta descrever o que quer em
   português ("me ajude a definir o problema de pesquisa do meu TCC") e o Claude
   escolhe a skill e o modo pelas palavras-gatilho. Os comandos `/ars-*` servem
   para forçar um modo específico.
2. **Roteamento com pergunta de esclarecimento.** Se você entregar material de
   várias fases ao mesmo tempo (por exemplo, rascunho + pareceres + bibliografia)
   sem dizer o que quer, a skill **pergunta** qual fluxo seguir (opções a–d), em
   vez de adivinhar. Para pular essa pergunta, comece a mensagem com
   `[direct-mode]` e diga exatamente a skill e o modo.
3. **Equipes de agentes.** Cada skill é uma equipe de papéis (por exemplo, 13
   agentes em `deep-research` e 12 em `academic-paper`): quem busca literatura,
   quem verifica fontes, quem sintetiza, quem escreve, quem faz o papel de
   advogado do diabo. A maioria roda dentro da própria conversa.
4. **Espectro e supervisão.** Cada modo tem um "espectro":
   - *Originalidade* (socratic, plan, guided): a skill **pergunta** em vez de
     responder; quem pensa é você. São os modos mais indicados para o TCC.
   - *Equilibrado* (full, outline-only): a skill propõe e você confirma as
     decisões-chave.
   - *Fidelidade* (citation-check, format-convert, etc.): tarefas mecânicas.
   O nível de supervisão (baixo → muito alto) diz quantas vezes ela vai parar para
   pedir sua confirmação.
5. **Integridade acima de tudo.** Há regras marcadas como *IRON RULE*: não
   inventar referências; verificar se cada citação existe (Crossref, OpenAlex,
   Semantic Scholar, arXiv); conferir se a fonte realmente sustenta a afirmação;
   marcar lacunas como `[MATERIAL GAP]` em vez de "enfeitar" o texto. No pipeline
   completo, as etapas 2.5 e 4.5 de integridade são **obrigatórias** e bloqueiam o
   avanço se algo falhar.
6. **Material Passport.** Ao longo do pipeline, a skill mantém um "passaporte" do
   material (YAML) que registra o que foi produzido, as fontes
   (`literature_corpus[]`), as verificações feitas e o estado de cada etapa. Ele
   permite retomar o trabalho depois e auditar o processo.
7. **Declaração de leitura.** As citações recebem marcas como
   `<!--ref:slug LOW-WARN-->` enquanto você não declarar que leu a fonte. Use
   `/ars-mark-read` para registrar que leu (texto completo, seções, só o resumo...).
   Isso não prova a leitura; é uma declaração sua, registrada para a auditoria.

---

## 3. As 5 skills e seus modos

### 3.1 `deep-research`: pesquisa e revisão de literatura
| Modo | O que entrega | Quando usar no TCC |
|---|---|---|
| `socratic` | Plano de pesquisa + coleção de insights, por diálogo | **Começo do TCC**: tema vago → problema, objetivos e pergunta de pesquisa |
| `quick` | Resumo de 500–1.500 palavras | Visão rápida de um assunto |
| `full` | Relatório de 3.000–8.000 palavras (APA 7) | Base para o referencial teórico |
| `lit-review` | Bibliografia anotada + síntese | Mapear autores e obras do referencial |
| `three-way-scan` | Artigos comparados por POR QUÊ / COMO / O QUÊ | Comparar rapidamente estudos parecidos (`/ars-3w`) |
| `fact-check` | Verificação afirmação por afirmação | Conferir dados e afirmações do texto |
| `review` | Parecer sobre um texto fornecido | Avaliar um artigo que você vai usar |
| `systematic-review` | Relatório PRISMA 2020, com meta-análise opcional | TCC que é uma revisão sistemática |

### 3.2 `academic-paper`: escrita do trabalho
| Modo | Comando | O que entrega |
|---|---|---|
| `plan` | `/ars-plan` | Planejamento socrático capítulo a capítulo (**recomendado para TCC**) |
| `outline-only` | `/ars-outline` | Sumário detalhado + mapa de evidências |
| `full` | — | Rascunho completo (você revisa e reescreve) |
| `lit-review` | `/ars-lit-review` | Seção de revisão de literatura a partir das suas fontes |
| `abstract-only` | `/ars-abstract` | Resumo + abstract + palavras-chave |
| `revision` | `/ars-revision` | Texto revisado + resposta ponto a ponto aos comentários |
| `revision-coach` | `/ars-revision-coach` | Roteiro de revisão a partir dos comentários do orientador/banca, sem reescrever por você |
| `rebuttal-audit` | `/ars-rebuttal-audit` | Confere se sua resposta aos comentários cobriu tudo |
| `citation-check` | `/ars-citation-check` | Relatório de citações ausentes, divergentes ou mal formatadas |
| `format-convert` | `/ars-format-convert` | Converte para DOCX/LaTeX/PDF/Markdown e troca o estilo de citação |
| `disclosure` | `/ars-disclosure` | Texto de declaração de uso de IA |

Configuração inicial (entrevista do `intake_agent`): tipo de trabalho, área,
formato de citação, formato de saída, idioma e número de palavras. Responda:
**idioma pt-BR, resumo pt-BR + EN e citação autor-data**; a conversão para ABNT
fica para o final (ver seção 5).

### 3.3 `academic-paper-reviewer`: simular a banca
Painel com 5 papéis: revisor de adequação ao veículo, revisor de metodologia,
revisor da área, revisor de outra perspectiva e advogado do diabo. Gera 5
pareceres, uma decisão editorial e um roteiro de revisão.
| Modo | Uso |
|---|---|
| `full` (`/ars-reviewer`) | Simulação completa antes de entregar ao orientador/banca |
| `quick` | Olhada rápida com os principais problemas |
| `methodology-focus` | Só a metodologia |
| `guided` | Diálogo socrático, problema por problema (**ótimo para aprender**) |
| `re-review` | Confere se a versão revisada resolveu os problemas apontados |
| `calibration` | Mede a precisão do revisor (uso avançado) |

O revisor mostra os "cartões de configuração" dos revisores e **espera sua
confirmação** antes de começar.

### 3.4 `academic-pipeline`: do zero ao trabalho final (`/ars-full`)
| Etapa | Nome | O que acontece |
|---|---|---|
| 1 | Pesquisa | `deep-research` (socratic, full ou quick) |
| 2 | Escrita | `academic-paper` (plan ou full) |
| 2.5 | Integridade | Verificação obrigatória de referências e afirmações |
| 3 | Revisão | Painel de 5 revisores |
| 4 | Revisão do texto | Você revisa com apoio do `revision` |
| 3′ | Re-revisão | Confere as correções |
| 4′ | Segunda revisão | Se ainda necessário |
| 4.5 | Integridade final | Todas as checagens declaradas precisam passar |
| 5 | Finalização | Markdown → DOCX/PDF/LaTeX |
| 6 | Resumo do processo | Registro de como o trabalho foi construído (opcional) |

O pipeline **para em cada etapa** e pede confirmação. Dá para entrar no meio
(por exemplo, já com um rascunho pronto): ele detecta o material e começa da etapa
certa. O custo estimado de API pelo autor original é de US$ 3–7 por execução
completa, e o trabalho colaborativo leva de horas a dias.

### 3.5 `sr-screener`: triagem para revisão sistemática
Só é necessário se o seu TCC for uma revisão sistemática, de escopo ou rápida.
Transforma seu protocolo em critérios de elegibilidade confirmados (`protocol`),
faz um piloto (`pilot`), triagem de títulos/resumos (`ta-screen`) e de texto
completo (`ft-screen`) com dois revisores de IA "cegos" e um adjudicador, e gera as
contagens PRISMA 2020 e a seção de métodos (`report`). Lê exportações RIS, PubMed,
Web of Science e CSV (por exemplo, do Zotero ou do Rayyan).

---

## 4. Roteiro recomendado para o TCC

1. **Definir o tema e o problema.** Peça em português: *"Tenho uma ideia vaga
   sobre X para meu TCC. Me guie para definir problema, objetivos e pergunta de
   pesquisa."* → `deep-research` modo `socratic`.
2. **Levantar a literatura.** *"Faça uma revisão de literatura sobre X, com
   fontes de 2015 a 2026."* → `deep-research` `lit-review`/`full`. Exporte as
   fontes que você vai usar para o Zotero e salve em `tcc/referencias/`.
3. **Planejar os capítulos.** `/ars-plan` → plano capítulo a capítulo, adaptado
   à estrutura do seu curso.
4. **Escrever.** Escreva você mesmo cada capítulo em `tcc/` e use a skill como
   coautora crítica (peça sugestões, contra-argumentos e pontos fracos). Use
   `/ars-outline` se precisar de um esqueleto com mapa de evidências.
5. **Checar citações.** `/ars-citation-check` em cada capítulo. Use
   `/ars-mark-read` nas fontes que você leu de fato.
6. **Simular a banca.** `/ars-reviewer` (ou modo `guided` para discutir item a
   item).
7. **Revisar.** Com os comentários do orientador ou do painel:
   `/ars-revision-coach` (roteiro) → você revisa → `/ars-rebuttal-audit` para
   conferir se respondeu a tudo.
8. **Resumo/Abstract.** `/ars-abstract` pedindo "Resumo em português (NBR 6028,
   150–500 palavras) + Abstract em inglês + 3 a 5 palavras-chave".
9. **Formatar e entregar.** `/ars-format-convert` para DOCX, depois ajuste ao
   modelo da instituição e à ABNT (seção 5).
10. **Declarar o uso de IA**, se a instituição exigir: `/ars-disclosure`.

Alternativa: `/ars-full` executa o fluxo inteiro com paradas em cada etapa.

---

## 5. Limitações importantes (leia antes de usar)

- **ABNT não é nativa.** O ARS formata em APA 7 / Chicago / MLA / IEEE /
  Vancouver. O `CLAUDE.md` deste repositório instrui o Claude a converter para
  ABNT (NBR 6023/10520/14724) na entrega, mas **confira manualmente** ou use o
  estilo ABNT do Zotero (CSL "ABNT").
- **Idioma.** As skills seguem o idioma do usuário e mantêm alguns termos
  técnicos em inglês. O resumo bilíngue tem padrão interno zh-TW + EN; peça
  sempre **pt-BR + EN**.
- **Os protocolos internos continuam em inglês** (ver `TRADUCAO.md`). Isso não
  afeta as respostas, que saem em português.
- **Verificação de referências** depende de acesso à internet (Crossref,
  OpenAlex, Semantic Scholar, arXiv). Obras brasileiras sem DOI (livros,
  dissertações em repositórios institucionais) podem sair como "não
  verificáveis": confira pela biblioteca, pelo Google Acadêmico ou pelo
  Catálogo de Teses da CAPES.
- **Scripts Python** (`ars/scripts/`) exigem Python 3. Algumas checagens
  opcionais precisam de pacotes extras: `pip install -r ars/requirements-dev.txt`.
  A conversão para DOCX usa o Pandoc, e o PDF usa LaTeX.
- **Autoria.** A IA não substitui sua leitura, sua análise nem a orientação. Use
  os modos socráticos para aprender e mantenha o texto final como seu.

---

## 6. Exemplos de pedidos (em português)

- "Me ajude a pensar no problema de pesquisa do meu TCC sobre evasão no ensino
  superior. Não me dê respostas prontas, me faça perguntas."
- "Compare estes 5 artigos por POR QUÊ, COMO e O QUÊ." (`/ars-3w`)
- "Verifique as citações do capítulo 2 em `tcc/cap2-referencial.md`."
- "Simule uma banca avaliando meu TCC em `tcc/tcc-completo.md`, com foco na
  metodologia."
- "Recebi estes comentários da minha orientadora; monte um roteiro de revisão."
- "Converta o TCC para Word com referências em ABNT."
