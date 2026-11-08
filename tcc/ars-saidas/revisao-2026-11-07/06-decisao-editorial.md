# Decisão editorial: painel simulado de revisão (Fase 2, `editorial_synthesizer_agent`)

*ARS `academic-paper-reviewer`, modo `full`, 08/11/2026. Síntese dos cinco pareceres da Fase 1
(07/11/2026). O sintetizador não é um sexto revisor: todo ponto abaixo remete a um achado de um
assento, citado pelo código do parecer (EIC = Revisor de Adequação/banca; R1 = Metodologia;
R2 = Domínio; R3 = Prática e setor; DA = Advogado do Diabo). "W" = fraqueza; "S" = ponto forte;
"M"/"m" = problema MAIOR/MENOR do DA.*

## Calibração e condições deste run

`calibration_status: NOT_CALIBRATED`. Nenhum perfil de calibração foi aplicado; os graus de
confiança dos pareceres (1–5) são autodeclarações de escopo e não pesam na decisão.

`criteria_binding_unavailable`: a banca não forneceu seus critérios. Esta decisão não afirma
aderência a critérios institucionais da FEA-RP/USP. Os cinco pareceres declaram o mesmo estado.

- **Sem contrato de sprint.** A decisão segue o protocolo de síntese qualitativo e a matriz de
  recomendações de `references/editorial_decision_standards.md` (caminho sem contrato), e não o
  protocolo mecânico v3.6.2.
- **Sem verificação cross-model.** `ARS_CROSS_MODEL` não foi usado; não houve checagem cega da decisão
  por outro modelo.
- **Verificações automáticas que não rodaram:**
  - `check_panel_synthesis.py`: não executado (não há contrato de sprint para recomputar).
  - `check_acronyms.py`: não executado; não há anexo de verificação de siglas.
  - `verify_panel_recommendations.py`: não executado; as referências sugeridas por R2 e R3 **não**
    foram conferidas nos índices bibliográficos por este sintetizador.
  - `audit_panel_claims.py`: não executado; no lugar dele, o sintetizador conferiu manualmente
    contra `manuscrito.txt` as afirmações factuais dos revisores (Parte D).
- **Público.** A carta é dirigida à banca de TCC (orientadora e dois professores, que avaliam só o
  texto). "Revisão maior" deve ser lida como "o que falta para entregar", e não como decisão de
  periódico.

## Proveniência do painel

Não há artefato tipado `review-panel-provenance/1.0` para este run. Por isso, os eixos formais ficam
como `unknown`. Ao lado, transcrevo o que o orquestrador declarou e o que os próprios pareceres
registram, sem inferir nada a partir das personas.

| Eixo de proveniência | Status formal | Declaração do orquestrador / registro nos pareceres |
|---|---|---|
| Separação de papéis | `unknown` (sem artefato) | Cinco assentos com papéis distintos (cartões n.º 1–4 + DA fixo) |
| Separação de contexto de invocação no painel | `unknown` (sem artefato) | Cinco subagentes em contextos separados |
| Cego às saídas dos pares | `unknown` (sem artefato) | Instrução de não ler os outros pareceres; R2, R3 e DA registram isso no parecer; EIC e R1 não registram |
| Família de modelo distinta | `unknown` (sem artefato) | Declarado: **mesma família** (Claude) em todos os assentos |
| Provedor distinto | `unknown` (sem artefato) | Declarado: mesmo provedor |
| Revisor humano distinto | `unknown` (sem artefato) | Nenhum revisor humano |

- **Afirmação binária de independência:** não calculada. Separação de papéis não é independência de
  erros.
- **Divulgação de erro correlacionado:** os cinco assentos rodaram no mesmo modelo, da mesma família.
  Erros de leitura, vieses e pontos cegos podem se repetir entre eles. Um consenso deste painel indica
  que o problema é provável, mas não substitui a leitura da orientadora e da banca.
- **Falha registrada:** artefato de proveniência ausente. Os eixos não foram verificados por script.

---

# Parte A — Carta de decisão editorial

À banca e ao autor do TCC "Empresas familiares vs. não familiares: comportamentos de endividamento"
(Ciências Contábeis, FEA-RP/USP),

O texto foi examinado por cinco assentos com papéis separados: adequação a um TCC (EIC), metodologia
(R1), domínio de empresas familiares (R2), prática de crédito e setor (R3) e Advogado do Diabo (DA). A
proveniência está descrita acima e não deve ser lida como prova de independência.

## Decisão: **Revisão maior**

Na linguagem de banca: **trabalho aprovável depois de ajustes substanciais, sem necessidade de refazer
a pesquisa nem de coletar uma nova base.** Nenhum assento recomenda rejeição, e o DA não registrou
nenhum problema CRÍTICO.

## Recomendações dos assentos

| Assento | Papel | Recomendação | Confiança (autodeclarada) |
|---|---|---|---|
| EIC | Professor de Contabilidade Financeira, avaliador de TCC | Revisão maior: "reescrita substancial [...] não exige novos dados nem nova análise" | 4 |
| R1 | Finanças empíricas e estatística em amostras pequenas | Revisão maior: reescrita e "poucas análises que o script já consegue produzir" | 4 |
| R2 | Governança e empresas familiares no Brasil | Revisão maior: "essencialmente de texto", com uma checagem manual da classificação | 4 |
| R3 | Crédito corporativo e setor de saúde | Revisão maior: "maior no conteúdo, não no esforço"; dados que o autor já tem | 4 |
| DA | Assento adversarial fixo | Sem recomendação (só achados); 0 CRÍTICOS, 7 MAIORES, 8 MENORES | por achado |

## Fundamentação da decisão

Os quatro assentos com recomendação concordam em "revisão maior". Pela matriz de decisão, quatro
"Major" levam a Revisão maior. Não há divergência de recomendação a arbitrar.

A decisão não é mais branda (Revisão menor) porque três grupos de problemas que pesam na decisão
seguem abertos e exigem mais que ajustes de frase:

1. **A leitura do prazo da dívida vai além da evidência e do enquadramento.** Este é o único ponto com
   os quatro assentos de acordo (CONSENSUS-4, SC-05): a menor participação da dívida de curto prazo
   é atribuída à preferência da família sem que as explicações concorrentes sejam discutidas. Os
   assentos citam tamanho e acesso a crédito (R2-W3, R3-W2, DA-M2), subsetor (EIC-W2, R3-W1),
   vencimentos e reclassificações (R1-W3, R3-W4) e oferta de crédito (R2-W3). Além disso, o prazo não
   estava na H1 (EIC-W1, R1, R2-W3a; CONSENSUS-3).
2. **O referencial teórico não sustenta a hipótese.** A SEW se apoia em fonte secundária, e faltam as
   obras seminais e a literatura empírica sobre família e endividamento (EIC-W3, R2-W1, R2-W5, DA-M7).
   O argumento sobre o prazo é ambíguo: os *covenants* pesam no longo prazo e o refinanciamento, no
   curto (EIC-W2, R2-W3b, DA-M1).
3. **Afirmações de síntese contradizem as tabelas do próprio trabalho, e falta reporte estatístico.**
   Há contradições confirmadas na Parte D: "único significativo a 5%", "tendência que se acentuou",
   26,4% contra 26,3% (EIC-W4–W6, R1-W2, R1-W6, DA-m1, DA-m2). A pandemia é lida além do teste
   (R1-W1), não há intervalos de confiança nem tamanhos de efeito (R1-W4), e o texto descreve a
   procedência dos números de um jeito que não confere com o material (R1-W5).

A decisão também não é mais dura (Rejeitar). Todos os assentos afirmam que a conclusão principal, de
que **a H1 não pode ser confirmada**, está correta e bem defendida (EIC-S1, R1, R2, R3 e a abertura da
lista do DA). Os problemas atingem a interpretação secundária e o enquadramento, e todos têm reparo
com a base que o autor já tem.

**Sobre a extensão do trabalho, houve uma divergência entre os assentos.** O EIC diz que a revisão não
exige nova análise; R1 e R3 pedem análises curtas sobre a base existente; R2 pede uma releitura
manual dos Formulários de Referência de 2018. Arbitragem na Parte B, Divergência 1. O roteiro marca,
item por item, o que exige nova análise ou coleta e o que é só reescrita.

## Questões que sustentam a decisão (ordem de origem, não ordem de execução)

| Ref. | Questão | Assentos | Âncora | Itens do roteiro |
|---|---|---|---|---|
| B1 | Prazo da dívida promovido a achado principal sem hipótese e sem explicações concorrentes | EIC, R1, R2, R3, DA | `text: §4.5 "a aversão à interferência de credores parece se manifestar mais na escolha do prazo do que na quantidade de dívida"` | RR-01, RR-02, RR-23, RR-25–RR-29, RR-38, RR-41, RR-42 |
| B2 | Referencial teórico sem as fontes do conceito central e da literatura empírica | EIC, R2, DA | `absence: Cap. 2 — fonte seminal da SEW, trade-off/pecking order e estudos de família × dívida` | RR-03–RR-05, RR-14, RR-37 |
| B3 | Afirmações de síntese em conflito com as Tabelas 1 e 4; reporte e procedência incompletos | EIC, R1, R3, DA | `text: §4.3 "o resultado da pandemia é o único significativo a 5% entre os testes realizados"` | RR-06–RR-09, RR-24, RR-30, RR-31 |

A ordem B1–B3 segue a origem dos achados, e não a importância nem a ordem de trabalho. A ordem de
execução é decisão do autor com a orientadora.

## Itens CRÍTICOS do Advogado do Diabo

`da_critical_adjudications: []`. Li o parecer do DA: a tabela "CRÍTICO" está vazia, e o DA afirma que
"Nenhum problema foi classificado como CRÍTICO. A conclusão principal [...] se sustenta diante de
todos os contra-argumentos". Nada bloqueia por essa via. Os sete MAIORES estão adjudicados na Parte C.

## Fechamento

Recomendamos ao autor revisar o texto com base no roteiro (Parte E), respondendo item por item:
"vou tratar", "não vou tratar, porque..." ou "não se aplica". O roteiro não fixa ordem nem prazo; isso
é decisão do autor com a orientadora. Depois da revisão, cabe uma re-revisão (modo `re-review`).

Lembretes de integridade:
- Nenhuma referência sugerida pelo painel deve entrar no TCC sem que o autor a localize e leia. R2
  diz ter conferido os metadados das suas por busca na web; R3 marca as suas como **[NÃO
  VERIFICADO]**; este sintetizador não conferiu nenhuma.
- Os números calculados por R1 fora das tabelas (IC, *leave-one-out*, interação, 29 datas, sem
  Comércio e Distribuição, Alliar 245%) são cálculos do revisor e devem ser refeitos pelo autor antes
  de qualquer uso.
- O texto é do autor. Confira as regras da FEA-RP/USP sobre uso de IA e declare esse uso, se exigido
  (`/ars-disclosure`), como lembram o EIC (pergunta 4) e os demais assentos.

---

# Parte B — Quadro de consenso e divergências

## B.1 Inventário de subafirmações (resumido)

Contagem sobre os 4 assentos com recomendação (EIC, R1, R2, R3). O DA é contado à parte. "Silêncio"
não é discordância. A gravidade é a do parecer de origem; quando dois assentos dão gravidades
diferentes, as duas aparecem.

| SC | Subafirmação | EIC | R1 | R2 | R3 | DA | Disposição |
|---|---|---|---|---|---|---|---|
| SC-01 | O prazo não está na H1, mas vira o achado central do Resumo e do Cap. 5 | W1 (MAIOR) | coment. "Pergunta e hipótese"; W1(i) (Major) | W3a (Maior) | — | M4 | **CONSENSUS-3** (R3 em silêncio) |
| SC-02 | Ambiguidade *covenants* × refinanciamento na previsão sobre o prazo | W2 (MAIOR) | — | W3b (Maior) | — | M1 | Corroborado 2/4 + DA |
| SC-03 | SEW sem fonte seminal; apoio em estudo sobre remuneração | W3 (MAIOR) | — | W1 (Maior) | — | M7 | Corroborado 2/4 + DA |
| SC-04 | *Trade-off*/*pecking order* sem citação | W3(ii) (MAIOR) | — | W5 (Maior) | — | — | Corroborado 2/4 |
| SC-05 | A interpretação do prazo como preferência familiar não é distinguida de explicações concorrentes | W2 sugestão (subsetor) | W3 (Major: vencimento/reclassificação) | W3c (Maior: oferta, tamanho) | W1, W2, W4 (Major) | M2, M6 | **CONSENSUS-4** |
| SC-06 | "Tendência que se acentuou a partir da pandemia" contradiz a Tabela 1 na dívida onerosa | W4 (MENOR) | W2 (Minor) | — | — | m1 | Corroborado 2/4 + DA |
| SC-07 | "Único significativo a 5%" contradiz a Tabela 4 (p = 0,027) | W5 (MENOR) | W6 (Minor) | — | — | M4 (âncora) | Corroborado 2/4 + DA |
| SC-08 | 26,4% no texto × 26,3% na Tabela 4 (C1) | W6 (MENOR) | quest. menor | — | quest. menor | m2 | **CONSENSUS-3** (R2 em silêncio) |
| SC-09 | A exclusão da Bradsaúde é tratada como valor extremo, mas dívida zero é característica legítima (escolha, modelo de negócio ou tipo de controlador) | W7 (MENOR) | W7 (Minor) | W8 (Menor) | W8 (Minor) | m5 | **CONSENSUS-4** |
| SC-10 | Uso de Jensen (1986) desconectado do argumento | W8 (MENOR) | — | W6 (Menor) | — | m3 | Corroborado 2/4 + DA |
| SC-11 | "Setor pouco explorado" sem suporte | W11 (MENOR) | — | W9 (Menor) | — (usa a frase como âncora de MEETS, sem contestar a falta de suporte) | m4 | Corroborado 2/4 + DA |
| SC-12 | A literatura empírica sobre família × dívida é enumerativa; Wildner aparece só numa lista; Pestana (Portugal) é usada para o Brasil | W12 (MENOR) | — | W5 (Maior) | — | — | Corroborado 2/4, com divergência de gravidade (Div. 4) |
| SC-13 | "Alavancagem financeira" na H1 × indicador principal | W10 (MENOR) | — | W10 (Menor) | — | — | Corroborado 2/4 |
| SC-14 | Lacunas de ABNT nas referências | W14 (MENOR) | — | quest. menores | — | — | Corroborado 2/4 |
| SC-15 | Classificação fixa pelo FRE mais recente coincide com as reorganizações de 2021–2022 | — | W10(ii) (Minor) | W4 (Maior) | W3 (Major) | M6 | **CONSENSUS-3** (EIC em silêncio), com divergência de gravidade (Div. 3) |
| SC-16 | Falta um quadro por empresa (classificação, controlador, subsetor, tamanho) | coment. ([VERIFICAR] da planilha) | — | W4(2), W8 | W1(a) | M2 | **CONSENSUS-3** (R1 em silêncio) |
| SC-17 | Resultado da pandemia lido além do teste; motivação de 3.5(c) escrita como previsão | W1, W5 (rótulo "exploratório") | W1 (Major) | — | — | M4; alternativa 2 (Selic) | Corroborado 2/4 + DA |
| SC-18 | Faltam IC, tamanho de efeito e poder | — | W4 (Major) | — | — | — | Achado de um assento |
| SC-19 | A procedência descrita (Google Planilhas) não confere com o script; a planilha do Cenário 1 está com a classificação do C2 | coment. (link da planilha e do script) | W5 (Major) | — | — | — | Achado de um assento (EIC corrobora só a disponibilização) |
| SC-20 | Multiplicidade não quantificada | — | W1, W6 | — | — | M4 | Achado de um assento + DA |
| SC-21 | O "resultado mais estável" (Dívida CP) é frágil a empresas individuais e à mensuração | — | W3 (Major) | — | W4 (Major) | M4, m8 | Corroborado 2/4 + DA |
| SC-22 | Tamanho e médias ponderadas existem no material de apoio e não aparecem no texto | — | — | W3c (cita tamanho) | W2 (Major) | M2, M5 | Corroborado 2/4 + DA |
| SC-23 | Leitura de Diamond (1991) simplificada (qualidade de crédito) | — | — | W3c (Maior) | W5 (Minor) | M2 | Corroborado 2/4 + DA, com divergência de gravidade |
| SC-24 | Fusões, aquisições e IPOs como descontinuidades de balanço | — | — | W4 (financiamento de operações) | W3 (Major) | M6 | Corroborado 2/4 + DA |
| SC-25 | Indicadores calculados e omitidos (sobre o PL, liquidez corrente, média ponderada) | — | — | — | W11 (Minor) | M5 (MAIOR) | Achado de um assento + DA |
| SC-26 | "Natureza do passivo" apresentada como achado | — | — | **S4 (elogia)** | **S3 (elogia)** | M3 | **SPLIT** entre DA e R2/R3 (Div. 5) |
| SC-27 | Seleção por painel completo (sobrevivência, empresas excluídas) | — | W10(i) (Minor) | — | W10 (Minor) | — | Corroborado 2/4 |
| SC-28 | Grupo não familiar heterogêneo | — | — | W8 (Menor) | W1 (Major) | alternativa 6 | Corroborado 2/4 + DA |
| SC-29 | Implicações práticas genéricas | — | — | — | W9 (Minor) | m6 | Achado de um assento + DA |
| SC-30 | "Duas forças" opõe SEW a controle, quando o controle é dimensão da própria SEW | — | — | W2 (Maior) | — | M1 (parcial: "menos dívida é SEW, mais dívida é diluição") | Achado de um assento + DA |

Os achados restantes de um único assento (EIC-W9, W13, W15; R1-W8, W9; R2-W7; R3-W6, W7; DA-m7) não
têm conflito e entram direto no roteiro, avaliados pela âncora de cada um.

## B.2 Consenso

**[CONSENSUS-4]**
1. **SC-05: a leitura do prazo não se distingue das explicações concorrentes.** EIC-W2 (perfil de
   dívida do subsetor), R1-W3 ("uma dívida de curto prazo alta é consequência de vencimento ou de
   dificuldade financeira, e não escolha"), R2-W3c (oferta de crédito, tamanho, qualidade de crédito)
   e R3-W1/W2/W4 (subsetor, tamanho, causas mecânicas). O DA chega ao mesmo ponto por outro caminho
   (M2, M6). É o achado com mais corroboração no painel.
2. **SC-09: a exclusão da Bradsaúde precisa de outra justificativa.** Os quatro assentos dizem que a
   dívida zero é um traço legítimo, e não um erro de dado: escolha conservadora (EIC-W7, R1-W7), tipo
   de controlador (R2-W8) e modelo de operadora (R3-W8). O DA soma a assimetria da robustez (m5). As
   correções sugeridas são compatíveis entre si (ver RR-09 e RR-25).

**[CONSENSUS-3]**
1. **SC-01: o prazo não estava na H1** (EIC, R1, R2; R3 em silêncio; DA-M4 concorda).
2. **SC-08: 26,4% × 26,3%** (EIC, R1, R3; R2 em silêncio; DA-m2 concorda).
3. **SC-15: a classificação fixa coincide com as reorganizações** (R1, R2, R3; EIC em silêncio; DA-M6
   concorda). A gravidade diverge (Div. 3).
4. **SC-16: falta um quadro por empresa** (EIC, R2, R3; R1 em silêncio; DA-M2 pede "o prazo por
   empresa").

Não há outro consenso de 3 ou 4 assentos. Os demais itens são corroborados por 2 assentos ou vêm de
um só, e entram no roteiro pelo mérito da âncora, sem rótulo de consenso.

## B.3 Divergências e arbitragem

**Divergência 1: a revisão exige nova análise?**
- **EIC:** "Não exige novos dados nem nova análise" (Recomendação).
- **R1:** pede IC, tamanho de efeito, *leave-one-out*, teste de variação entre subperíodos e
  sensibilidade às 29 datas (W1, W3, W4, W7), "que o script já consegue produzir".
- **R2:** pede a releitura dos FREs de 2018/2019 (W4).
- **R3:** pede tabelas descritivas (subsetor, tamanho, eventos) e consulta às notas explicativas
  (W1–W4).
- **Tipo:** divergência de direção sobre o escopo do remédio.
- **Resolução:** cada assento decide dentro da sua área. Em reporte estatístico e robustez vale R1;
  em classificação, R2; na leitura de crédito, R3. O EIC declara que esses pontos estão fora do seu
  foco ("detalhes estatísticos [...] fora do meu foco"; "Rigor estatístico: NOT_ASSESSED"). O
  roteiro registra as análises pedidas como tais. Onde o próprio assento ofereceu um caminho só de
  reescrita (R1-W9, R1-W10, R3-W6), os dois caminhos ficam visíveis e a escolha é do autor.
- **Justificativa:** prioridade da competência (princípio 2). Todas as análises usam a base e o
  script existentes, de modo que nenhuma exige coletar uma base nova. As exceções são consultas
  documentais pontuais: FRE 2018, notas explicativas e fatos relevantes.

**Divergência 2: o subsetor de Comércio e Distribuição explica o resultado do prazo?**
- **R3-W1 e DA (alternativa 3):** o subsetor pode explicar o padrão, e o exame feito para o nível
  (§4.4) não foi repetido para o prazo.
- **R1-W3(4):** pelos cálculos do revisor, retirar Comércio e Distribuição *fortalece* a diferença no
  prazo (Mann-Whitney p ≈ 0,035), "o que afasta essa explicação alternativa".
- **R3-W1(c)** reconhece que os Cenários 1 e 2, que levam RADL e PFRM para o grupo não familiar e
  mantêm a direção, "já são um bom indício contra o confundimento pelo varejo".
- **Tipo:** divergência de existência, só para o prazo. Para o nível, todos concordam que o subsetor
  pesa (EIC-S5, R2-S5, R3-S2).
- **Resolução:** **dissenso parcialmente resolvido.** A evidência de R1 (cálculo do revisor, a
  confirmar) e o argumento de R3-W1(c) apontam na mesma direção: Comércio e Distribuição não explica
  o prazo. O que continua em aberto é a composição *dentro* de Serviços e de Medicamentos (operadora
  sem dívida, administradora, biotecnologia com EBITDA negativo; R3-W1). A ação é a mesma para todos:
  reportar a robustez sem Comércio e Distribuição e usá-la a favor do autor (RR-28).
- **Justificativa:** evidência primeiro (princípio 1). Os assentos concordam na ação; só a força da
  explicação ficou em aberto.

**Divergência 3: gravidade da classificação fixa (SC-15)**
- **R1-W10(ii) (Minor):** o erro de classificação tende a atenuar as diferenças em direção a zero;
  basta registrar isso nas limitações.
- **R2-W4 (Maior) e R3-W3 (Major):** a classificação feita com informação do fim do período e as
  operações societárias coincidem com a abertura da diferença em 2021–2022, e podem fazê-las parecer
  efeito da estrutura familiar.
- **Tipo:** divergência de gravidade, com remédios diferentes mas compatíveis.
- **Resolução:** **prevalece a gravidade MAIOR** para a classificação (domínio de R2) e para os
  eventos de balanço (domínio de R3). A observação de R1 sobre a atenuação entra no texto como parte
  da limitação. Os dois argumentos podem valer ao mesmo tempo: o erro de classificação atenua a
  diferença, e o efeito mecânico de balanço pode criá-la.
- **Justificativa:** prioridade da competência (princípio 2); a questão de classificação é de domínio.

**Divergência 4: gravidade da literatura empírica (SC-12)**
- **EIC-W12 (MENOR):** a Discussão dialoga pouco com Wildner et al.
- **R2-W5 (Maior):** a afirmação "literatura inconclusiva", que sustenta a leitura do nulo, não está
  demonstrada.
- **Resolução:** **MAIOR**, por competência de domínio (R2). O próprio EIC classifica o referencial
  como MAIOR em W3.

**Divergência 5: "natureza do passivo" (SC-26): achado ou leitura excessiva?**
- **R2-S4 e R3-S3:** separar dívida onerosa de passivo total é "conceitualmente correto" e é "a leitura
  que interessa ao credor".
- **DA-M3:** apresentar isso como achado é uma generalização excessiva, porque a diferença na dívida
  onerosa não é significativa, inverte o sinal em C1 e C2 e se confunde com o subsetor.
- **Tipo:** divergência de existência sobre o *status* da afirmação.
- **Resolução:** **os dois lados têm razão em planos diferentes.** A distinção conceitual é correta
  (R2, R3). A frase do Cap. 5 ("a diferença observada está na natureza do passivo"), porém, afirma
  como resultado algo que, pela Tabela 2 (p = 0,556/0,255) e pela Tabela 4 (sinal invertido em C1 e
  C2), é só descritivo (Parte D, V9). Recomendação: manter a distinção como leitura descritiva e
  retirar o tom de achado (RR-46).
- **Justificativa:** evidência primeiro; a frase foi conferida contra as tabelas.

**Divergência 6: severidade de Diamond (1991) (SC-23)**
- **R2-W3 (Maior, no conjunto do W3)** e **R3-W5 (Minor):** os dois dizem que o modelo liga o prazo à
  qualidade de crédito.
- **Resolução:** a subafirmação "leitura simplificada de Diamond" é MENOR quando isolada (R3). Ela
  ganha peso como parte da questão B1, que é MAIOR por consenso. As duas gravidades ficam registradas
  (RR-38).

**Não são divergências** (posições compatíveis):
- R3-S1 elogia a preocupação com o setor na mesma frase em que EIC-W9 critica o verbo "evitar".
- R2 chama de "questão de estilo" a localização dos exemplos (Baumer, RaiaDrogasil) que EIC-W15 aponta.
- R1-W6 conta "cerca de 40" p-valores e DA-M4, "cerca de 45". As duas contagens conferem (V18): 3
  p-valores abaixo de 5%, em 2 comparações distintas.

---

# Parte C — Adjudicação dos itens do Advogado do Diabo

**CRÍTICOS:** nenhum. Lido e confirmado (seção "Lista de problemas" do DA, tabela CRÍTICO vazia).
`da_critical_adjudications: []`.

**Contra-argumento mais forte do DA** (o tamanho e o acesso ao mercado de capitais explicam o prazo
melhor que a SEW): **validado como explicação concorrente a ser discutida**, e não como explicação
demonstrada. R2-W3c e R3-W2 o corroboram de forma independente. O DA não mostrou que o tamanho
*explica melhor*: para isso seriam necessários os dados por faixa de tamanho que ele mesmo pede. O
autor deve apresentá-lo como rival na §4.5.

| DA | Argumento | Corroborado por | Avaliação do sintetizador | Exigência ao autor |
|---|---|---|---|---|
| M1 | Arcabouço não falseável: *covenants* (longo prazo) × refinanciamento (curto prazo); SEW × diluição | EIC-W2, R2-W3b; parcialmente R2-W2 | **VALIDADO.** Texto conferido (V5): §2.2 traz as duas previsões, e a frase sobre os *covenants* do longo prazo não tem citação. O "não falseável" é forte demais para o nível, porque a H1 é direcional e foi testada; vale plenamente para o prazo | RR-02, RR-37 |
| M2 | Tamanho e acesso a crédito explicam o prazo; Diamond liga prazo à qualidade de crédito | R2-W3c, R3-W2, R3-W5 | **VALIDADO como explicação concorrente.** Dados de tamanho conferidos no material de apoio (V19). O conteúdo de Diamond (1991) não foi conferido por ninguém no painel além da leitura dos revisores; o autor deve conferir | RR-38, RR-41 |
| M3 | "Natureza do passivo" como achado, quando é subsetor e não é significativa | Divergente: R2-S4 e R3-S3 elogiam a distinção | **PARCIALMENTE VALIDADO** (Div. 5). Frase e tabelas conferidas (V9) | RR-46 |
| M4 | O achado do prazo pesa mais do que a evidência permite (fora da H1, subperíodo *a posteriori*, cerca de 45 p-valores, cenários aninhados) | EIC-W1, R1-W1, R1-W3, R1-W6, R2-W3a | **VALIDADO.** Contagem de p-valores conferida (V18). O aninhamento dos cenários (as 5 familiares de C1 estão entre as 10 de C3) é afirmação só do DA; ela é compatível com o Quadro 3, mas não foi recontada empresa por empresa | RR-01, RR-24, RR-29 |
| M5 | Resultados do material de apoio ausentes do texto, em sua maioria desfavoráveis à H1; o Resumo não menciona a inversão de sinal | R3-W11 (liquidez), R3-W2 (média ponderada) | **VALIDADO.** Valores conferidos em `resultados.md` (V19). O Resumo menciona a sensibilidade ao critério, mas não a inversão (V8: parcialmente confirmada). O próprio DA registra que a omissão não vai num sentido só (a liquidez favorece as familiares) | RR-45 |
| M6 | A janela em que a diferença se abre coincide com eventos societários e com a classificação fixa | R2-W4, R3-W3, R1-W10(ii) | **VALIDADO como questão a examinar.** Tabela 1 conferida (2021: 26,0% × 35,4%). As datas de IPO e de fusões são conhecimento externo marcado [VERIFICAR] pelo DA e por R3, e não foram conferidas | RR-35, RR-42 |
| M7 | O mecanismo central não tem apoio direto nas fontes citadas | EIC-W3, R2-W1 | **VALIDADO.** Os títulos das referências confirmam o tema das fontes (remuneração de executivos; qualidade dos lucros) (V12). Que Kayo et al. e Poletti-Hughes apontam mais dívida nas familiares vem da descrição do próprio autor, com [VERIFICAR] em aberto | RR-03, RR-18 |

**MENORES do DA** (adjudicados resumidamente): m1 validado (V3) → RR-06; m2 validado (V2) → RR-08;
m3 validado com EIC-W8 e R2-W6 → RR-10; m4 validado com EIC-W11 e R2-W9 → RR-13; m5 validado,
corroborado por R1-W7 e R3-W8 → RR-09, RR-25; m6 validado com R3-W9 → RR-44; m7 validado (V10) →
RR-47; m8 validado como hipótese, corroborado por R1-W3 e R3-W4, com a causa a confirmar nas notas
explicativas → RR-27.

---

# Parte D — Conferência das afirmações factuais contra o manuscrito

Feita manualmente sobre `manuscrito.txt`, as tabelas nele contidas e, quando o revisor citou o
material de apoio, `tcc/analise/saidas/resultados.md` e `tcc/analise/resultados_c3.py`. Não executei
scripts.

| V | Afirmação do revisor | Assentos | Resultado | O que o texto mostra |
|---|---|---|---|---|
| V1 | A §4.3 diz que a pandemia é "o único significativo a 5%", mas a Tabela 4 tem p = 0,027 | EIC-W5, R1-W6, DA-M4 | **Confirmada** | §4.3: "o resultado da pandemia é o único significativo a 5% entre os testes realizados"; Tabela 4, "C3 sem Bradsaúde", Dív. bruta/Ativo: p (t) = 0,027** |
| V2 | A §4.4 dá 26,4% para NF em C1; a Tabela 4 dá 26,3% | EIC-W6, R1, R3, DA-m2 | **Confirmada** | §4.4: "30,9% contra 26,4% no Cenário 1"; Tabela 4, linha C1: 26,3% |
| V3 | "Tendência que se acentuou a partir da pandemia" contradiz a Tabela 1 na dívida onerosa | EIC-W4, R1-W2, DA-m1 | **Confirmada** (dívida onerosa) | Tabela 1: diferença de 0,9 p.p. (2020), 9,4 (2021), 11,2 (2022), 0,5 (2025: 26,4% × 26,9%). No prazo, a distância é maior depois de 2021, como os próprios revisores ressalvam |
| V4 | O texto atribui a análise ao Google Planilhas e não menciona o script; a planilha do Cenário 1 está com a classificação do C2 | R1-W5 | **Parcialmente confirmada** | §3.5: "com uso do Google Planilhas"; o manuscrito não menciona script nem Python. O script registra: "O arquivo 'Cenário 1' está com a classificação do C2 (erro 1)". Não conferi as cópias "(corrigido)", e o R1 também não conseguiu ler a coluna de classificação delas |
| V5 | A §2.2 associa *covenants* mais rigorosos ao longo prazo, sem citação, e depois argumenta a favor do longo prazo | EIC-W2, R2-W3b, DA-M1 | **Confirmada** | "Essa relação de risco é especialmente associada às dívidas de longo prazo, que normalmente apresentam cláusulas restritivas mais rigorosas." (sem citação na frase); o parágrafo seguinte conclui pela "preferência por prazos mais longos" |
| V6 | "Sem ela, passa a ser" exagera, porque o Mann-Whitney fica a 10% | R1-W7 | **Parcialmente confirmada** | A frase anterior da §4.4 é precisa ("significativa a 5% no teste t [...] e a 10% no teste de Mann-Whitney"); o exagero está só na frase de síntese |
| V7 | O Cap. 5 diz que a diferença "dependeu da presença" da Bradsaúde | EIC-W7 | **Confirmada** (texto); a ambiguidade de leitura é julgamento do EIC | Cap. 5, 3.º parágrafo: "dependeu da presença de uma única empresa sem dívida financeira" |
| V8 | O Resumo diz "em todos os exercícios, menor endividamento oneroso" sem mencionar a inversão de sinal | DA-M5 | **Parcialmente confirmada** | O Resumo traz a frase, mas acrescenta que a diferença "mostrou-se sensível ao critério de classificação"; não diz que o sinal se inverte |
| V9 | "Natureza do passivo" é afirmada como achado, mas a diferença na dívida onerosa não é significativa e inverte o sinal em C1 e C2 | DA-M3 | **Confirmada** | Cap. 5: "a diferença observada está na natureza do passivo"; Tabela 2: p = 0,556/0,255; Tabela 4: C1 30,9% × 26,3%, C2 28,7% × 27,0% |
| V10 | "As familiares concentram-se em comércio e distribuição" é impreciso (3 de 10) | DA-m7 | **Confirmada** | Quadro 1: PNVL, PFRM e RADL entre 10 familiares; nenhuma não familiar no subsetor |
| V11 | Wildner, Oro e Petry (2020) aparecem uma única vez, numa lista da Introdução | EIC-W12, R2-W5 | **Confirmada** | Referência: "Citado na página 7"; não reaparece na §4.5 |
| V12 | Pestana et al. tratam de empresas portuguesas e são usados para o "ambiente corporativo brasileiro"; Santos e Silva (2018) é estudo sobre remuneração | EIC-W12, R2-W1, R2-W5, DA-M7 | **Confirmada** (pelos títulos das referências) | "Testando a estrutura de capital de empresas familiares portuguesas"; "Análise da remuneração dos executivos [...]"; Cap. 1, 1.º parágrafo cita Pestana para o Brasil |
| V13 | Falta Lista de tabelas e de ilustrações | EIC-W13 | **Confirmada** no texto extraído | Só aparecem "Lista de quadros" e "Sumário" |
| V14 | Há 11 marcadores [VERIFICAR]/[DECIDIR] | EIC | **Confirmada** | 11 ocorrências em `manuscrito.txt` |
| V15 | "Martínez García" em caixa mista; "s.d." na EY; documentos *on-line* sem "Acesso em" | EIC-W14, R2 | **Confirmada** | "POLETTI-HUGHES; Martínez García"; "EY [...] s.d."; Lei 6.404 sem "Acesso em" |
| V16 | Números da Tabela 1 citados pelos revisores (2021: 26,0 × 35,4; Dív. CP NF 25,8 → 47,0 → 54,3; Exigível 50,2 → 56,1 e 47,8 → 53,3) | R1-W2, R3-W4, R3-W6, DA-M6, DA-m8 | **Confirmada** | Valores idênticos na Tabela 1 |
| V17 | Lifemed com 66% da dívida no curto prazo | R3-W4, DA-M2 | **Confirmada** | §4.2 |
| V18 | Contagem de p-valores (R1 cerca de 40; DA cerca de 45, com 3 abaixo de 5%) | R1-W6, DA-M4 | **Confirmada**; as contagens se reconciliam | Tabela 2: 10; Tabela 3: 18; Tabela 4: 16 novos; mais 1 (sem a Biomm) = 45. Abaixo de 5%: 0,040 e 0,043 (pandemia) e 0,027 (sem a Bradsaúde): 3 p-valores, 2 comparações |
| V19 | Material de apoio: mediana do capital empregado F R$ 6,5 bi × NF R$ 1,7 bi; média ponderada 32,5% × 34,5%; Exigível/PL 153,6% × 116,7%; liquidez corrente 2,18 × 1,48 (p = 0,064) | R3-W2, R3-W11, DA-M2, DA-M5 | **Confirmada** em `resultados.md` (fora do manuscrito) | Linhas 17, 20, 90–91 |
| V20 | §3.5(c) formula a motivação da pandemia como previsão | R1-W1 | **Confirmada** | "deveria se manifestar com mais clareza" |
| V21 | Introdução: "precisa evitar" | EIC-W9 | **Confirmada** | Cap. 1, 4.º parágrafo |
| V22 | Cálculos próprios de R1 (IC, *g*, poder, *leave-one-out*, interação p ≈ 0,13, 29 datas, sem Comércio e Distribuição p ≈ 0,035, Alliar 245,2%) | R1-W1, W3, W4, W7, W8 | **Não confirmada** pelo sintetizador | Não aparecem no manuscrito; o R1 pede ao autor que os confira |
| V23 | Fatos externos (datas de IPO e fusões, Selic, ANS, IFRS 16 na Economática, conteúdo de Diamond, 1991) | R3-W3, W6; DA-M2, M6, alternativas | **Não confirmada** | Marcados como "a confirmar" ou [VERIFICAR] pelos próprios revisores |

Nenhuma afirmação factual dos revisores sobre o manuscrito foi desmentida pela conferência.

---

# Parte E — Roteiro de Revisão (*Revision Roadmap*)

**Leia antes de usar.** O roteiro **não é ranqueado**. A numeração segue a ordem de origem: os achados
do EIC (W1 → W15 e comentários), depois os de R1, R2, R3 e DA que ainda não estavam cobertos. Ela
não indica importância nem ordem de execução, que são decisões do autor com a orientadora. A
gravidade é a do parecer de origem; quando há duas, as duas aparecem.

**Tipo de trabalho**:
- **R**: só reescrita, o que inclui localizar e ler fontes;
- **RC**: reportar resultados que já estão calculados no material de apoio ou nos dados já coletados;
- **NA**: nova análise sobre a base e o script existentes;
- **NC**: nova consulta documental (FRE, notas explicativas, fatos relevantes, definição da
  Economática);
- **R/NA**: o assento ofereceu os dois caminhos, e a escolha é do autor.

| ID | Origem | Disposição | Gravidade | Local | O que fazer | Tipo |
|---|---|---|---|---|---|---|
| RR-01 | EIC-W1; R1-W1(i) e "Pergunta e hipótese"; R2-W3a, W3(1); DA-M4 | CONSENSUS-3 + DA | MAIOR | Resumo (última frase), §2.2, §3.5(c), §4.5 (3.º par.), Cap. 5 (2.º e 4.º par.) | Tratar o prazo explicitamente como questão complementar exploratória (ou como expectativa secundária, dizendo quando foi formulada), e marcar no Resumo e no Cap. 5 que o resultado é "exploratório, sem correção para múltiplos testes". A escolha entre os caminhos depende da resposta honesta à pergunta 1 do EIC e à pergunta 3 do R1 | R |
| RR-02 | EIC-W2; R2-W3b; DA-M1 | Corroborado 2/4 + DA | MAIOR | §2.2 (2.º–3.º par.), §4.5 | Pesar os dois canais (*covenants* no longo prazo × refinanciamento no curto); citar fonte para a frase sobre cláusulas do longo prazo ou retirá-la; reconhecer que a previsão sobre o prazo é ambígua | R |
| RR-03 | EIC-W3(i); R2-W1; DA-M7 | Corroborado 2/4 + DA | MAIOR | Cap. 1, §2.1, §2.2 | Citar a origem do conceito de SEW e suas dimensões (sugestões de R2 a ler e verificar); reservar Santos e Silva (2018) ao que o estudo mostra; usar "apud" quando a fonte for indireta (NBR 10520) | R (fontes) |
| RR-04 | EIC-W3(ii); R2-W5 | Corroborado 2/4 | MAIOR | Cap. 1, 1.º par., §2 | Citar *trade-off* e *pecking order* na fonte (resolver o [VERIFICAR] de Myers e de Myers e Majluf) e ligar a *pecking order* com aversão à diluição ao argumento da §2.2 | R (fontes) |
| RR-05 | EIC-W3(iii); R2-W6 | Corroborado 2/4 | MAIOR (EIC) / Menor (R2) | §2.1 (título e conteúdo) | Incluir o conflito controlador × minoritários e a visão do credor sobre o controle familiar, ou retirar "Conflitos de agência" do título | R (fontes) |
| RR-06 | EIC-W4; R1-W2; DA-m1, DA-M4 | Corroborado 2/4 + DA | MENOR | Cap. 5, 2.º par.; §4.1; nota da Tabela 2 | Separar os indicadores: na dívida onerosa, a diferença se ampliou em 2021–2022 e quase desapareceu em 2025; no prazo, ficou maior desde 2021; nenhuma variação foi testada. Dizer em 4.1 que a abertura de 2021 reflete sobretudo Qualicorp e Fleury (dado do R1, a conferir). Avisar que "8 de 8 anos" é contagem descritiva, e não 8 observações independentes | R |
| RR-07 | EIC-W5; R1-W6; DA-M4 | Corroborado 2/4 + DA | MENOR | §4.3, último par.; Resumo; Cap. 5 ("a exceção") | Corrigir "único significativo a 5%": é um dos dois resultados a 5%, ambos em análises complementares (o outro é a exclusão da Bradsaúde) | R |
| RR-08 | EIC-W6; R1 (q. menores); R3 (q. menores); DA-m2 | CONSENSUS-3 + DA | MENOR | §4.4 | Corrigir 26,4% para 26,3% e conferir todos os números do texto contra as Tabelas 1–4 | R |
| RR-09 | EIC-W7; R1-W7; R2-W8; R3-W8; DA-m5 | CONSENSUS-4 + DA | MENOR | §3.5(d), §4.4, Cap. 5 (3.º par.) | Reescrever: "a significância dependeu da *exclusão* da Bradsaúde"; justificar a exclusão como análise de influência e/ou pelo modelo de operadora e pelo tipo de controlador, e não pelo efeito sobre a média; dizer que dívida zero é escolha de financiamento legítima; trocar "sem ela, passa a ser" por "significativa a 5% no teste t e a 10% no Mann-Whitney" | R |
| RR-10 | EIC-W8; R2-W6; DA-m3 | Corroborado 2/4 + DA | MENOR | Cap. 1, 4.º par. | Retirar a frase com Jensen (1986) ou reescrevê-la conforme o que Jensen sustenta (fluxo de caixa livre, gestores × acionistas) | R |
| RR-11 | EIC-W9 | Um assento | MENOR | Cap. 1, 4.º par. | Trocar "evitar" por "reduzir", como já está na §3.2 | R |
| RR-12 | EIC-W10; R2-W10 | Corroborado 2/4 | MENOR | §2.2 (H1), Cap. 5, 1.º par. | Reformular a H1 com o termo do indicador ("menor endividamento oneroso") ou dizer, logo depois da H1, qual indicador a operacionaliza | R |
| RR-13 | EIC-W11; R2-W9; DA-m4 | Corroborado 2/4 + DA | MENOR | Cap. 5, 5.º par.; §3.2 ([VERIFICAR]) | Apoiar "setor pouco explorado" na busca feita ("nenhum dos estudos revisados analisa o setor isoladamente") ou retirar a frase | R |
| RR-14 | EIC-W12; R2-W5 | Corroborado 2/4 (gravidade: Div. 4) | MAIOR (arbitrada) / MENOR (EIC) | Cap. 1, 1.º e 5.º par.; §2.2 ou nova §2.3; §4.5 | Quadro-síntese dos estudos empíricos sobre família × endividamento (autor, país, amostra, critério, sinal); comparar os resultados com Wildner et al. (2020) na §4.5, depois de lê-lo; usar uma fonte brasileira para caracterizar o Brasil, ou dizer que Pestana et al. estudam Portugal | R (fontes) |
| RR-15 | EIC-W13 | Um assento | MENOR | Pré-textuais (`main.tex`) | Incluir Lista de tabelas e Lista de ilustrações; avaliar uma lista de siglas; conferir no modelo do curso a folha de aprovação e a ficha catalográfica | R |
| RR-16 | EIC-W14; R2 (q. menores) | Corroborado 2/4 | MENOR | Referências (`referencias.bib`) | Completar Pestana et al. (volume, número, páginas, DOI) com dados conferidos na fonte; caixa alta em MARTÍNEZ GARCÍA; "Acesso em:" nos documentos *on-line*; trocar "s.d." da EY por data provável entre colchetes e indicar a edição | R |
| RR-17 | EIC-W15; R2 (coment. Metodologia, "questão de estilo") | Corroborado 2/4 | MENOR | §2.1 → §3.3 | Levar os exemplos da Baumer e da RaiaDrogasil para a §3.3 | R |
| RR-18 | EIC (Pendências); R2-W5 e Referências; DA (Observações) | Corroborado | Sem gravidade própria (condição de integridade) | 11 marcadores no texto; `.bib` | Resolver todos os [VERIFICAR]/[DECIDIR] antes da entrega. Antes de tudo, os de Kayo et al. (2018) e de Poletti-Hughes e Martínez García (2022), dos quais depende o argumento das "duas forças" (R2-W5, DA). Conferir Ribeiro et al. (2026), marcado como não verificado no `.bib` (R2). [DECIDIR] do System-GMM: EIC e DA sugerem manter uma versão curta | R (fontes) |
| RR-19 | EIC (Pendências: apêndice da classificação); R2-W4(2), W8; R3-W1(a); DA-M2 | CONSENSUS-3 + DA | MAIOR (R2-W4, R3-W1) | Novo apêndice; Quadro 1 | Quadro por empresa: % de ações ordinárias da família (direta + indireta), bloco de controle e acordo de acionistas, cargo do familiar, versão e item do FRE, classificação em C1/C2/C3, tipo de controlador das não familiares, subsetor e modelo de negócio, tamanho, Dívida/Ativo médio e Dívida CP média | RC |
| RR-20 | EIC (Apresentação); R1 (q. menores); R3 (q. menores) | CONSENSUS-3 | Questão menor | §4.1, Figuras 1–2 | O autor refaz os gráficos (pendência já registrada), incluindo o da Dívida CP / Dívida total e, se quiser, marcas das datas dos eventos societários (R3) | RC |
| RR-21 | EIC (Coerência estrutural); R2 (Título e resumo) | Corroborado 2/4 | Questão menor | Título | Avaliar um título que informe o recorte (setor de saúde da B3, 2018–2025), se o curso permitir | R |
| RR-22 | EIC (q. menores); R1 (q. menores); R2 (q. menores) | Vários | Questão menor | §4.1, §4.2, §3.3, notas das Tabelas 2–4, Cap. 2 | "As Figuras 1 e 2"; itálico uniforme em termos estrangeiros; Quadro 3 fora do meio da lista (b)–(e); dizer que as medianas da §4.2 incluem a Biomm; n de cada linha também na Tabela 3; anos que entram na média das empresas com dados incompletos; frase de abertura do Cap. 2 | R |
| RR-23 | R1-W1(ii)–(iii); DA (alternativa 2) | Um assento + DA | Major | §3.5(c), §4.3 | Reescrever a motivação da pandemia como pergunta exploratória ("examinar se a diferença se altera"), e não como previsão; não ler "tornou-se/reduziu-se a significância" como mudança de comportamento | R |
| RR-24 | R1-W1(3)–(4), W6; DA-M4 | Um assento + DA | Major (W1) / Minor (W6) | §4.3, §3.5 | Testar a diferença entre grupos na variação por empresa entre subperíodos (pandemia − pré, pós − pré) e reportar o resultado; informar o número de testes e o p ajustado (Holm) do resultado da pandemia dentro da sua família | NA |
| RR-25 | R1-W3(1), W7; R3-W3(c); DA-m5 | Corroborado 2/4 + DA | Major (R1-W3) / Minor (R1-W7) | §4.4 ou apêndice | Retirar uma empresa por vez, nas 16, para a dívida onerosa e para a Dívida CP (período completo e pandemia), e reportar a faixa de p-valores | NA |
| RR-26 | R1-W3(2) | Um assento | Major | §4.4 | Reportar a Dívida CP com as 29 datas trimestrais, ou com a mediana por empresa, como sensibilidade à mensuração | NA |
| RR-27 | R1-W3(3); R3-W4; DA-m8 | Corroborado 2/4 + DA | Major | §4.2, §4.5 | Consultar as notas explicativas (Alliar 2025; Qualicorp 2018 e 2021; não familiares que puxam 2021 e 2025) para saber se houve vencimento único, reclassificação por *covenant* ou *waiver*, e relatar em uma ou duas frases | NC |
| RR-28 | R1-W3(4); R3-W1(b)–(c) | Corroborado 2/4 (Div. 2) | Major | §4.4 | Reportar a robustez da Dívida CP sem Comércio e Distribuição e, de forma descritiva, a comparação dentro de Serviços (3 × 4); usar o resultado e os Cenários 1 e 2 como argumento a favor do autor | NA |
| RR-29 | R1-W3(5); R2-W3(4); DA-M4 | Corroborado 2/4 + DA | Major / Maior | Cap. 5, 3.º par. e sugestões de pesquisa; §4.4 | Trocar "resultado mais estável" e "aspecto mais promissor" por "o único cujo sinal se manteve em todas as especificações, com significância frágil"; dizer que os cenários compartilham empresas e não são replicações independentes; trocar "parece se manifestar" por formulação descritiva | R |
| RR-30 | R1-W4 | Um assento | Major | Tabelas 2–4; §3.5(b); Cap. 5 | Acrescentar diferença com IC 95% e um tamanho de efeito (g de Hedges ou delta de Cliff); uma frase sobre o efeito mínimo detectável; trocar "resultado nulo" por "ausência de evidência, com estimativas imprecisas" | NA |
| RR-31 | R1-W5; EIC (Pendências: link da planilha e do script) | Um assento (EIC corrobora a disponibilização) | Major | §3.5, 1.º par. | Dizer qual ferramenta gerou os números das tabelas (planilha e/ou script em Python) e disponibilizar os dois; garantir que a planilha entregue tenha, em cada cenário, a classificação do Quadro 3; se planilha e script divergirem, dizer qual versão é a oficial | R (conferência de arquivos) |
| RR-32 | R1-W8 | Um assento | Minor | Tabela 2 e nota | Tratar a Alliar 2025 na Dívida bruta / (Dívida bruta + PL), que passa de 100% (dado do R1, a conferir), com a mesma regra dos indicadores sobre o PL, e registrar na nota | NA |
| RR-33 | R1-W9; EIC (Pendências) | Um assento | Minor | §3.5(b), notas das Tabelas 2–4 | Adotar o p exato do Mann-Whitney (o script já calcula) e regerar as tabelas, **ou** manter a aproximação e dizer em nota que o p exato não altera nenhuma conclusão. Resolve o [DECIDIR] | R/NA |
| RR-34 | R1-W10(i); R3-W10 | Corroborado 2/4 | Minor | §3.2; limitações | No mínimo, explicar a inclusão de empresas com IPO no período (RDOR, BLAU, a confirmar) e registrar o possível viés de sobrevivência; opcionalmente (R1), uma sensibilidade 2022–2025 com as empresas excluídas | R/NA |
| RR-35 | R2-W4(1), (3); R1-W10(ii); DA-M6 | CONSENSUS-3 + DA (gravidade: Div. 3) | MAIOR (arbitrada) / Minor (R1) | §3.3(e); limitações | Reler os itens 15.1/15.2 dos FREs de 2018 (ou 2019) das 16 empresas e informar quantas mudariam de grupo em cada cenário; se alguma mudar, reportar o teste com a classificação inicial; conferir se Tommasetti et al. (2019) mantêm a classificação fixa; dizer nas limitações que o erro de classificação tende a atenuar as diferenças (R1) | NC |
| RR-36 | R1 (Métodos de análise); R3-W7 | Corroborado 2/4 | Minor | Quadro 4; §4.2 | Citar fonte para "principal métrica em *covenants*" ou suavizá-la; mencionar que a ausência da Biomm nos anos de EBITDA negativo não é aleatória; opcionalmente (R3), apresentar a distribuição por faixas | R/NA |
| RR-37 | R2-W2; DA-M1 (parcial) | Um assento + DA | Maior | §2.2, último par.; §4.5, 2.º par.; Cap. 5 | Reenquadrar as "duas forças" como pressões que nascem do mesmo motivo (preservar o controle): evitar a diluição, o que favorece dívida, e evitar o risco de falência e a intervenção de credores, o que favorece menos dívida; apoiar em literatura que testa esse dilema (sugestões de R2, a ler) | R (fontes) |
| RR-38 | R2-W3c, W3(3); R3-W2 (discussão), W5; EIC-W2 (sugestão); DA-M2 e "Premissa não examinada" | **CONSENSUS-4 (SC-05)** + DA | Maior (R2) / Major (R3-W2) / Minor (R3-W5) | §2.2; §4.5; Cap. 5, 4.º par.; Resumo | Na §4.5, um parágrafo com as explicações concorrentes do prazo: tamanho e acesso ao mercado de capitais, oferta e qualidade de crédito (inclusive a leitura de Diamond, 1991, a conferir), subsetor e causas mecânicas; reformular para "o padrão é compatível com [...], mas também com [...]", também no Resumo e no Cap. 5 | R (fontes) |
| RR-39 | R2-W7 | Um assento | Menor | §3.3 (escolha do C3), Quadros 2–3 | Justificar o C3 por validade conceitual, deixando o equilíbrio dos grupos como vantagem secundária; apresentar o C2 como construção do autor; dizer como a participação indireta é calculada (multiplicada ou elo mais fraco); registrar que a proxy não distingue o tipo de envolvimento familiar | R |
| RR-40 | R2-W8; R3-W1; DA (alternativa 6) | Corroborado 2/4 + DA | Menor (R2) / Major (R3-W1) | Quadro 1; §4.4 | Caracterizar o tipo de controlador de cada não familiar (disperso, instituição financeira, fundo etc.) e ligar o resultado sem a Bradsaúde ao tipo de controlador | R (consulta ao FRE) |
| RR-41 | R3-W2; DA-M2, M5 | Corroborado 2/4 + DA | Major | Cap. 4 (nova tabela curta); §4.5 | Tabela de tamanho por grupo (mediana, mínimo, máximo) e médias ponderadas da Dívida bruta/Ativo e do Exigível/Ativo, já calculadas em `resultados.md`; opcionalmente, separar descritivamente empresas grandes e pequenas | RC |
| RR-42 | R3-W3; DA-M6; R2-W4 | Corroborado 2/4 + DA | Major | Novo quadro; §4.1, §4.3 | Linha do tempo dos eventos societários (fusões, IPOs, aquisições), com empresa, data e efeito esperado no balanço; confirmar as datas nos fatos relevantes e FREs; dizer se a abertura da diferença em 2021 é explicada por empresas específicas | NC |
| RR-43 | R3-W6 | Um assento | Minor | Quadro 4; limitações | Informar se a "Dívida bruta" da Economática inclui arrendamentos (IFRS 16/CPC 06) e mencionar a quebra de 2019 como limitação, ou mostrar que os resultados não mudam a partir de 2019 | NC (definição) + R/NA |
| RR-44 | R3-W9; DA-m6 | Um assento + DA | Minor | Cap. 5, 5.º par. | Tornar as implicações para credores, investidores e gestores específicas e cautelosas (exemplos em R3-W9), ou reduzir a promessa da Introdução | R |
| RR-45 | R3-W11; DA-M5 | Um assento + DA | Minor (R3) / MAIOR (DA) | Apêndice; Resumo | Reportar em apêndice todos os indicadores do Quadro 4 já calculados (os sobre o PL e a liquidez corrente) e a média ponderada, ou explicar por que ficaram de fora; mencionar no Resumo a inversão de sinal nos Cenários 1 e 2 | RC |
| RR-46 | DA-M3 (× R2-S4, R3-S3) | SPLIT arbitrado (Div. 5) | MAIOR (DA) | Cap. 5, 2.º par. | Manter a distinção entre dívida financeira e passivo total como leitura descritiva, e retirar o tom de achado de "a diferença observada está na natureza do passivo", já que a diferença não é significativa e inverte o sinal em C1 e C2 | R |
| RR-47 | DA-m7 | Um assento (DA) | MENOR | Cap. 5, limitações | Trocar "as familiares concentram-se no subsetor de comércio e distribuição" por "não há não familiares no subsetor de comércio e distribuição" (3 de 10 familiares) | R |

**Contagem por tipo de trabalho (47 itens)**

| Tipo | Itens | Quantidade |
|---|---|---|
| R: só reescrita (inclui ler fontes e conferir arquivos) | RR-01–18, 21–23, 29, 31, 37–40, 44, 46, 47 | 30 |
| RC: reportar o que já está calculado ou coletado | RR-19, 20, 41, 45 | 4 |
| NA: nova análise sobre a base e o script existentes | RR-24, 25, 26, 28, 30, 32 | 6 |
| NC: nova consulta documental | RR-27, 35, 42, 43 | 4 |
| R/NA: escolha do autor | RR-33, 34, 36 | 3 |

Nenhum item exige coletar uma base nova na Economática nem trocar o método. Para responder, use
`templates/revision_response_template.md`, item por item ("vou tratar" / "não vou tratar, porque..."
/ "não se aplica"). A recusa de um item fica registrada e é reavaliada na re-revisão.

---

# Parte F — Méritos reconhecidos pelo painel

- **O resultado nulo é tratado com honestidade.** A conclusão responde ao problema sem confirmar o que
  não foi confirmado, e distingue "ausência de evidência" de "igualdade" (EIC-S1, S2; R1-S2; DA, "O que
  o trabalho faz bem"). É o ponto em que muitos TCCs erram.
- **A unidade de análise está correta e justificada.** Uma média por empresa, sem tratar
  empresa-trimestre como observação independente (EIC-S4, R1-S1, DA).
- **A classificação das empresas é transparente e auditável.** Três condições cumulativas, regras
  para blocos de controle, participação indireta e participação relevante sem controle, e casos
  concretos (Fleury/Pardini, RaiaDrogasil, Dasa). EIC-S3 a considera "a contribuição metodológica mais
  sólida"; R2-S1 e R3-S4 concordam.
- **A robustez é reportada mesmo quando contraria a hipótese.** A inversão de sinal em C1 e C2 aparece
  e é explicada (EIC-S5, R1-S4, R2-S2, R3-S2). O DA e o EIC sugerem que essa sensibilidade ao critério
  de empresa familiar ganhe mais destaque como contribuição.
- **A análise exploratória é declarada.** Os subperíodos aparecem como exploratórios, todos os
  resultados são reportados e há alerta para a multiplicidade (R1-S3, DA). A crítica do painel é que
  o Resumo e o Cap. 5 não mantêm esse tom (DA, "Observações").
- **Mudança de desenho justificada.** O abandono do System-GMM é explicado pelo tamanho da amostra
  (EIC-S6, R1-S2).
- **Números fiéis e reprodutíveis.** R1 conferiu as Tabelas 1–4 contra `resultados.md` e registrou
  que o script regera as tabelas sem diferença (R1-S5). A única divergência é a de RR-08.
- **Leituras contábeis corretas.** A distinção entre dívida financeira e passivo total (R2-S4, R3-S3),
  com a ressalva de RR-46, e o tratamento prudente da Dívida líquida/EBITDA com e sem a Biomm (R3-S5).
- **Escopo adequado a um TCC**, com coleta manual verificável nos Formulários de Referência (EIC,
  "Adequação a um TCC de graduação"; R2-S5).

---

## Apêndice — Síntese por assento

- **EIC (adequação/banca):** Revisão maior | confiança 4. O enquadramento (hipótese só sobre o nível,
  conclusão sobre o prazo) e o referencial curto pesam mais que os dados, que se sustentam.
- **R1 (metodologia):** Revisão maior | confiança 4. O Resumo e o Cap. 5 leem a pandemia e o prazo com
  mais força do que os testes permitem; faltam IC e tamanho de efeito; a procedência descrita não
  confere com o script.
- **R2 (domínio):** Revisão maior | confiança 4. A SEW está sem as fontes seminais, as "duas forças"
  estão mal enquadradas, o prazo não tem hipótese nem explicações concorrentes e a classificação fixa
  coincide com as reorganizações.
- **R3 (prática e setor):** Revisão maior | confiança 4. Subsetor, tamanho e fusões ou IPOs não foram
  examinados como explicações do prazo, embora os dados existam.
- **DA:** sem recomendação | **nenhum problema CRÍTICO**. Contra-argumento central: tamanho e acesso ao
  mercado de capitais explicam o prazo sem recorrer à SEW; a contribuição mais defensável é a
  sensibilidade ao critério de empresa familiar.

*Este documento foi gerado por IA numa simulação de banca. Ele não substitui a avaliação da
orientadora nem da banca, e as decisões sobre o texto são do autor. Nenhum arquivo do TCC nem dos
pareceres foi alterado nesta etapa.*
