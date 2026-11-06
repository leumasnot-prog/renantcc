<!--
Revisão de consistência do TCC (06/11/2026), feita com a skill `academic-paper` (modo `revision`)
do ARS instalado em ars/. Procedimento seguido:
  - roteiro de revisão (seção 1) → patches por trecho (seção 2) → checagem de citações (seção 3);
  - cada patch altera só o trecho indicado; o restante do texto fica igual (regra de "blocos intocados");
  - IRON RULE: nenhuma referência foi incluída sem ser verificada (seção 3 traz a fonte de cada uma);
  - anti-padrão 7 (scope creep): conteúdo NOVO vem marcado [NOVO – APROVAR] e só entra se você aprovar;
  - writing_quality_check.md: termos vagos, terminologia inconsistente e siglas definidas duas vezes.
Os scripts do ARS (anchorize/apply/check_acronyms) não foram executados neste ambiente; a checagem de siglas
foi feita manualmente.
-->

# Revisão de consistência do TCC

**Base:** `TCC - Entrega 1_corrigido_Maisa.docx` (com as alterações controladas aceitas) + nova seção 3
(`03_METODOLOGIA.md`).
**Como aplicar no Word:** primeiro *Revisão > Aceitar todas as alterações* (isso também elimina a lista
apagada "Indicadores a analisar… 👉 Excelente equilíbrio" que ainda está no fim do arquivo). Depois aplique cada
patch abaixo: o texto **ATUAL** é para você localizar (Ctrl+L) e o **NOVO** é para colar no lugar.

---

## 1. Roteiro de revisão

| # | Gravidade | Onde | Inconsistência | Tipo de patch |
|---|---|---|---|---|
| R1 | Alta | Resumo (folha de rosto) | Promete "modelo econométrico" e "dados em painel"; não traz resultados | Substituição |
| R2 | Alta | Introdução, problema de pesquisa | "mesmo após o controle de fatores setoriais e características específicas da firma": a nova Metodologia não tem controles | Substituição |
| R3 | Alta | Introdução, §4 | "isolar o efeito-família", "análise causal mais precisa": o desenho é descritivo-comparativo | Substituição |
| R4 | Alta | Introdução, justificativa | "abordagem capaz de isolar esses fatores" | Substituição |
| R5 | Alta | Seção 3 inteira | System-GMM, Q de Tobin, alavancagem de mercado | Já feito: `03_METODOLOGIA.md` |
| R6 | Alta | Referencial 2.2 | A teoria só fala do *risco dos covenants de longo prazo*, mas o resultado mais forte do TCC é que as familiares têm **menos dívida de curto prazo** (logo, mais longo prazo). Sem um argumento sobre prazo e refinanciamento, a banca vê uma contradição entre teoria e resultado | [NOVO – APROVAR] |
| R7 | Alta | Referencial 2.2 | O referencial não apresenta o argumento contrário (família que prefere dívida para não diluir o controle), mas a Conclusão vai precisar dele para explicar o resultado não significativo | [NOVO – APROVAR] |
| R8 | Média | Introdução, §1 | Frase com erro de concordância após a revisão: "empresas com diferentes estrutural: propriedade e governança" | Correção |
| R9 | Média | Introdução, §2 × 2.1 | A mesma ideia aparece com dois nomes: "Capital Socioemocional (*SEW*)" e "riqueza socioemocional (Socioemotional Wealth – SEW)"; a sigla é definida duas vezes | Padronização |
| R10 | Média | 2.2, §2 | A frase "Essa relação de risco é especialmente associada à(s) dívida(s) de longo prazo…" aparece **duas vezes seguidas** | Exclusão |
| R11 | Média | 2.1, início | Comentário da Maisa: "Exemplos." | Inclusão de exemplos |
| R12 | Média | Citações | "(Pestana et al., 2021)": pela NBR 10520:2023, até três autores são citados todos | Correção |
| R13 | Média | Referências | 6 obras citadas e ausentes da lista; ALMEIDA (2020) e CUNHA, ADAM e BOFF (2024) estão na lista mas não são citadas | Inclusão/exclusão |
| R14 | Baixa | Introdução, §1 | Trade-off e Pecking Order sem citação | Sugestão |
| R15 | Baixa | Elementos pré-textuais | Ano 2025 na capa e na folha de rosto; folha de rosto sem nota de natureza do trabalho; "Lista de Tabelas" com a Tabela 1, que deixou de existir; título "4. REFERÊNCIA" | Correção |

**O que não foi alterado, de propósito:** a **H1** continua como está. Mudar a hipótese depois de ver os
resultados (HARKing) seria um problema metodológico mais grave que o resultado não significativo. O
caminho correto é manter a H1 e discutir na Conclusão por que ela não se confirmou.

---

## 2. Patches

### P1 (R1). Resumo

**ATUAL:**
> Este trabalho investiga se empresas familiares brasileiras de capital aberto se endividam menos que as não familiares. A pesquisa propõe que a aversão à perda de controle e à interferência de credores, visando preservar a riqueza socioemocional, leva à políticas de financiamento mais conservadoras. A hipótese é testada com um modelo econométrico que controla por fatores da firma e do setor, usando dados em painel de companhias listadas na B3.

**NOVO** (NBR 6028:2021: parágrafo único, 150 a 500 palavras; aqui são cerca de 260):
> **RESUMO**
>
> Este trabalho investiga se empresas familiares brasileiras de capital aberto apresentam endividamento diferente do das empresas não familiares. Com base na perspectiva da riqueza socioemocional, a pesquisa parte da hipótese de que a aversão à interferência de credores e à perda de controle leva as famílias controladoras a adotarem políticas de financiamento mais conservadoras. A amostra compreende 16 companhias do setor de saúde da B3, com dados trimestrais da Economática de 2018 a 2025. As empresas foram classificadas como familiares segundo o critério de Santos e Silva (2018), e dois critérios alternativos foram usados como testes de robustez. O endividamento foi medido por indicadores contábeis de nível, de capacidade de pagamento e de composição da dívida, e as diferenças entre os grupos foram avaliadas pelos testes t de Welch e de Mann-Whitney, para o período completo e para os subperíodos anterior, durante e posterior à pandemia de COVID-19. Os resultados indicam que as empresas familiares apresentaram, em todos os exercícios, menor endividamento oneroso e menor participação da dívida de curto prazo que as não familiares, mas essas diferenças não foram estatisticamente significativas no período completo, e o endividamento total dos dois grupos foi semelhante. A exceção é a composição da dívida durante a pandemia, quando a menor participação da dívida de curto prazo nas empresas familiares foi significativa ao nível de 5%. A diferença no endividamento oneroso mostrou-se sensível ao critério de classificação e à presença de uma empresa sem dívida financeira. Conclui-se que a hipótese não pode ser confirmada estatisticamente, embora a evidência descritiva seja compatível com uma postura mais conservadora das famílias em relação ao prazo da dívida.
>
> **Palavras-chave:** empresas familiares; endividamento; estrutura de capital; riqueza socioemocional; setor de saúde.

Observações:
- O resumo deve ficar em página própria, depois da folha de rosto (NBR 14724), e não na folha de rosto.
- Se a orientadora pedir um *abstract*, escreva-o a partir deste resumo, mas sem traduzir palavra por palavra.
- O resumo antecipa os resultados. Depois de corrigir a planilha, confira se os números continuam iguais
  (pela auditoria, nada muda).

### P2 (R15). Nota da folha de rosto (no lugar onde hoje está o resumo)

**NOVO:**
> Trabalho de Conclusão de Curso apresentado ao Departamento de Contabilidade da Faculdade de Economia, Administração e Contabilidade de Ribeirão Preto da Universidade de São Paulo, como requisito parcial para a obtenção do título de Bacharel em Ciências Contábeis.
>
> Orientadora: Profa. Dra. Maisa Ribeiro [VERIFICAR: título e nome completo]

Na capa e na folha de rosto, troque **2025 → 2026** [VERIFICAR: ano da entrega].

### P3 (R8). Introdução, §1, primeira frase

**ATUAL:**
> O ambiente corporativo brasileiro é composto por empresas com diferentes estrutural: propriedade e governança.

**NOVO:**
> O ambiente corporativo brasileiro é composto por empresas com diferentes estruturas de propriedade e de governança.

E, no mesmo parágrafo:

**ATUAL:** "as decisões de estrutura de capital, a combinação entre capital próprio e de terceiros representam um dilema central"
**NOVO:** "as decisões de estrutura de capital, isto é, a combinação entre capital próprio e de terceiros, representam um dilema central"

### P4 (R12). Introdução, §1, citação

**ATUAL:** "(Pestana et al., 2021)" → **NOVO:** "(Pestana; Gomes; Lopes, 2021)"

Atenção: Pestana, Gomes e Lopes (2021) estudam empresas **portuguesas**. A frase cita o trabalho para uma
afirmação geral sobre empresas familiares, o que é aceitável. Na justificativa (P8), o texto cita o trabalho
como parte da literatura sobre empresas familiares; se quiser, acrescente "no contexto português".

### P5 (R9). Introdução, §2: terminologia da SEW

**ATUAL:**
> A literatura sobre governança em firmas familiares introduz o conceito de Capital Socioemocional (*SEW)*, que representa a utilidade não financeira…

**NOVO:**
> A literatura sobre governança em firmas familiares introduz o conceito de riqueza socioemocional (*socioemotional wealth* – SEW), que representa a utilidade não financeira…

Em todo o texto, use **"riqueza socioemocional"** e **"SEW"** (sem itálico na sigla), sempre no mesmo
gênero. O texto usa "o SEW"; mantenha "o SEW" em todas as ocorrências (ou "a SEW" em todas, se a Maisa
preferir). Em 2.1, como a sigla já foi definida na Introdução:

**ATUAL (2.1):** "ganha destaque o conceito da riqueza socioemocional (Socioemotional Wealth – SEW), que abrange…"
**NOVO (2.1):** "ganha destaque o conceito de riqueza socioemocional (SEW), que abrange…"

### P6 (R3). Introdução, §4

**ATUAL:**
> Assim, a aversão à interferência de credores, que ameaça o *SEW*, pode levar a uma política de endividamento mais conservadora, alinhada à Teoria da Agência, que prevê que empresas com muitas oportunidades de crescimento (e, portanto, menor caixa livre ocioso) tendem a usar menos dívida (Jensen, 1986). Para testar essa hipótese de forma robusta, é imperativo isolar o "efeito-família" de fatores setoriais. Nesse sentido, a abordagem de Oliveira e Kayo (2020) torna-se uma referência crucial, pois demonstra como operacionalizar e controlar o efeito de choques idiossincráticos da firma em relação ao seu setor, permitindo uma análise causal mais precisa.

**NOVO:**
> Assim, a aversão à interferência de credores, que ameaça o SEW, pode levar a uma política de endividamento mais conservadora, alinhada à Teoria da Agência, que prevê que empresas com muitas oportunidades de crescimento (e, portanto, menor fluxo de caixa livre ocioso) tendem a usar menos dívida (Jensen, 1986). Como o setor de atuação também influencia a estrutura de capital (Oliveira; Kayo, 2020), a comparação entre empresas familiares e não familiares precisa evitar que diferenças setoriais sejam confundidas com o efeito da estrutura de controle. Por isso, esta pesquisa concentra a análise nas companhias de um único setor, o de saúde da B3.

[VERIFICAR em Oliveira e Kayo (2020) a passagem sobre o efeito do setor; o texto original já atribuía essa
ideia aos autores.]

### P7 (R2). Introdução, problema de pesquisa (e objetivo)

**ATUAL:**
> Diante do exposto, emerge o seguinte problema de pesquisa: a estrutura de controle familiar está associada a diferentes níveis de endividamento quando comparada à estrutura de controle não familiar nas empresas de capital aberto brasileiras, mesmo após o controle de fatores setoriais e características específicas da firma? A resposta a esta questão é crucial para subsidiar investidores, credores e os próprios gestores familiares na formulação de estratégias financeiras alinhadas a seus objetivos multifacetados.

**NOVO:**
> Diante do exposto, emerge o seguinte problema de pesquisa: a estrutura de controle familiar está associada a diferentes níveis de endividamento quando comparada à estrutura de controle não familiar nas companhias abertas brasileiras do setor de saúde? A resposta a esta questão pode subsidiar investidores, credores e os próprios gestores familiares na formulação de estratégias financeiras alinhadas a seus objetivos econômicos e não econômicos.
>
> [NOVO – APROVAR] O objetivo geral deste trabalho é comparar o nível e a composição do endividamento de empresas familiares e não familiares do setor de saúde da B3 no período de 2018 a 2025. Como objetivos específicos, busca-se: (i) classificar as companhias quanto ao controle familiar a partir de critérios da literatura; (ii) comparar os grupos quanto ao endividamento oneroso, ao endividamento total, à capacidade de pagamento e ao prazo da dívida; e (iii) verificar se as diferenças se mantêm em subperíodos e sob critérios alternativos de classificação.

(O parágrafo de objetivos é novo. Ele costuma ser exigido em TCC, mas confirme com a Maisa se o modelo do curso
pede essa parte.)

### P8 (R4). Introdução, justificativa

**ATUAL:**
> Além disso, a literatura nacional ainda apresenta espaço para investigações que considerem simultaneamente características específicas das firmas e fatores setoriais na análise do endividamento corporativo. Nesse contexto, ao aplicar uma abordagem capaz de isolar esses fatores, esta pesquisa busca oferecer uma contribuição empírica adicional para a literatura de finanças corporativas e de governança em empresas familiares.

**NOVO:**
> Além disso, esta pesquisa examina um período recente, que inclui o choque da pandemia de COVID-19, concentra a comparação em um único setor e verifica se os resultados se mantêm sob diferentes critérios de classificação de empresa familiar, aspecto em que os estudos nacionais divergem. Com isso, busca oferecer uma contribuição empírica adicional para a literatura de finanças corporativas e de governança em empresas familiares.

### P9 (R11). 2.1: exemplos (comentário "Exemplos." da Maisa)

Inserir **depois** da frase "…enfatiza o envolvimento da família no controle, propriedade e gestão (Santos; Silva, 2018)."

**NOVO:**
> Entre as companhias analisadas nesta pesquisa, a Baumer ilustra a presença simultânea dessas três dimensões: a família detém cerca de 89% das ações ordinárias, integra o bloco de controle e ocupa a presidência do conselho de administração e a diretoria-presidência. Já a RaiaDrogasil exemplifica um arranjo comum no mercado brasileiro, em que três famílias reunidas em um mesmo bloco de controle detêm, em conjunto, menos da metade das ações ordinárias, mas mantêm membros no conselho de administração.

[VERIFICAR no FRE mais recente: participação e cargos na BALM ("confirmar cargos atuais", pendência da aba
Metodologia) e na RADL.] Se a Maisa quiser exemplos da literatura, e não da amostra, troque por exemplos
citados em Santos e Silva (2018).

### P10 (R10). 2.2, §2: frase duplicada

**ATUAL (as duas frases seguidas):**
> Essa relação de risco é especialmente associada às dívidas de longo prazo, que normalmente apresentam cláusulas restritivas mais rigorosas. Essa relação de risco é especialmente associada à dívida de longo prazo, que geralmente contém os covenants mais rigorosos.

**NOVO (uma só):**
> Essa relação de risco é especialmente associada às dívidas de longo prazo, que normalmente apresentam cláusulas restritivas mais rigorosas.

### P11 (R6). 2.2: prazo da dívida e risco de refinanciamento [NOVO – APROVAR]

Inserir **depois** de P10 e **antes** de "Para as empresas familiares, o risco de violação de covenants…".

**NOVO:**
> O prazo da dívida, contudo, expõe a empresa aos credores de outra forma. Enquanto a dívida de longo prazo concentra as restrições nas cláusulas contratuais, a dívida de curto prazo precisa ser renovada com frequência e sujeita a empresa ao risco de liquidez, isto é, ao risco de que os credores se recusem a refinanciá-la ou o façam em condições desfavoráveis (Diamond, 1991). Esse risco tende a se agravar em períodos de crise, quando o crédito se torna mais escasso. Para uma família que busca preservar a autonomia decisória, depender de renovações frequentes significa submeter-se repetidamente à avaliação dos credores. Assim, além de um menor nível de dívida, a aversão à interferência de credores pode se manifestar na preferência por prazos mais longos.

Por que isso é necessário: a seção 3.4 da Metodologia e o resultado mais forte do TCC (Dívida CP/Dívida total
na pandemia) dependem desse argumento, que hoje não existe no referencial. Sem ele, o texto diz que a dívida de
longo prazo é a mais ameaçadora e depois mostra que as familiares têm mais dívida de longo prazo. Com ele, as
duas coisas se conciliam: a família aceita as cláusulas do longo prazo para não depender de renovações.

### P12 (R7). 2.2: argumento em sentido oposto [NOVO – APROVAR]

Inserir **depois** de "…como forma de reduzir o risco de perda de controle." e **antes** de "Com base no
exposto, formula-se a seguinte hipótese:".

**NOVO:**
> Há, porém, um argumento em sentido oposto. Como a emissão de novas ações dilui a participação da família, a preservação do controle pode levar a família a preferir a dívida ao capital próprio. Poletti-Hughes e Martínez Garcia (2022), em empresas latino-americanas, encontraram empresas familiares mais alavancadas quando a participação da família é menor, como forma de manter o controle, e redução da alavancagem quando essa participação é elevada. No Brasil, Kayo, Brunaldi e Aldrighi (2018) observaram empresas familiares mais endividadas e com ajuste mais lento da estrutura de capital. Essas evidências ajudam a explicar por que a literatura permanece inconclusiva. Ainda assim, considerando a perspectiva da riqueza socioemocional e o papel dos credores discutido nesta seção, adota-se como hipótese a direção de menor endividamento.

[VERIFICAR nos dois artigos: (a) se Poletti-Hughes e Martínez Garcia (2022) formulam o argumento da diluição
nesses termos; (b) o resultado de Kayo, Brunaldi e Aldrighi (2018) sobre alavancagem maior, que vem do resumo
e de um estudo que cita o artigo.] Este parágrafo prepara a Conclusão: forças opostas podem se anular, o que é
coerente com diferenças não significativas.

### P13 (R14). Introdução, §1: Trade-off e Pecking Order sem citação [SUGESTÃO]

As duas teorias são apresentadas sem fonte. Sugestão de referências clássicas (conferir antes de incluir):
Myers (1984), *The capital structure puzzle*, para as duas, e Myers e Majluf (1984) para a Pecking Order.
Uma alternativa já presente no texto é Pestana, Gomes e Lopes (2021), que testam as duas teorias.

### P14 (R15). Lista, sumário e referências

- **Lista de Tabelas → Lista de Quadros:** Quadro 1 (Composição da amostra), Quadro 2 (Critérios de
  classificação na literatura), Quadro 3 (Cenários de classificação), Quadro 4 (Indicadores). As tabelas de
  resultados entram depois, na seção 4.
- **Sumário:** atualize as subseções da seção 3 (3.1 a 3.5) e acrescente 4 Resultados, 5 Considerações
  Finais e Referências. Use *Referências > Atualizar sumário*.
- **"4. REFERÊNCIA" → "REFERÊNCIAS"**, centralizado e **sem número** (NBR 14724, elemento pós-textual).

---

## 3. Checagem de citações (citation-check)

### 3.1 Citadas no texto e ausentes da lista: verificadas na web em 06/11/2026

| Referência (formato ABNT NBR 6023:2018) | Verificação |
|---|---|
| AMES, A. C.; NOLLI, J. G.; BECK, F.; MUCCI, D. M. Preservação da riqueza socioemocional e a profissionalização em empresas familiares. **RACE – Revista de Administração, Contabilidade e Economia**, Joaçaba, v. 19, n. 3, p. 513-536, 2020. DOI: 10.18593/race.23702. | Confirmada (portal da revista e Dialnet). Ao citar no texto: "Ames *et al.*, 2020", porque são 4 autores |
| KAYO, E. K.; BRUNALDI, E. O.; ALDRIGHI, D. M. Capital structure adjustment in Brazilian family firms. **Revista de Administração Contemporânea**, Rio de Janeiro, v. 22, n. 1, p. 92-114, 2018. DOI: 10.1590/1982-7849rac2018170004. | Confirmada (RAC, SciELO, RePEc) |
| WILDNER, R.; ORO, I. M.; PETRY, D. R. Influência da propriedade familiar na estrutura e custo de capital das empresas brasileiras. **Revista Catarinense da Ciência Contábil**, Florianópolis, v. 19, e2913, 2020. DOI: 10.16930/2237-766220202913. | Confirmada (DOAJ, Redalyc) |
| PESTANA, L. J.; GOMES, L. P.; LOPES, C. Testando a estrutura de capital de empresas familiares portuguesas. **Revista Contabilidade & Finanças**, São Paulo, v. 32, n. 87, 2021. DOI: 10.1590/1808-057x202113190. | Título, autores, revista, ano e DOI confirmados. [VERIFICAR: volume, número e páginas] |
| JENSEN, M. C. Agency costs of free cash flow, corporate finance, and takeovers. **The American Economic Review**, v. 76, n. 2, p. 323-329, 1986. | Referência clássica; dados conforme o CONTEXTO_TCC.md |

### 3.2 Novas, introduzidas pela Metodologia e pelos patches P11 e P12

| Referência | Verificação |
|---|---|
| DIAMOND, D. W. Debt maturity structure and liquidity risk. **The Quarterly Journal of Economics**, v. 106, n. 3, p. 709-737, 1991. DOI: 10.2307/2937924. | Confirmada (RePEc, EconBiz). O resumo define risco de liquidez como o risco de perda por incentivos excessivos dos credores à liquidação, o que sustenta P11 |
| POLETTI-HUGHES, J.; MARTÍNEZ GARCIA, B. Leverage in family firms: the moderating role of female directors and board quality. **International Journal of Finance & Economics**, v. 27, n. 1, p. 207-223, 2022. DOI: 10.1002/ijfe.2147. | Confirmada (Liverpool, Navarra, RePEc). Versão online de 2020; use 2022, que é a do fascículo |
| TOMMASETTI, R.; MACEDO, M. A. S.; CONSTANTINO, F. F. S.; SARLO NETO, A. Family control and earnings management in Brazilian listed companies: a relationship mediated by age. **Revista Universo Contábil**, Blumenau, v. 15, n. 1, p. 151-169, 2019. DOI: 10.4270/ruc.2019108. | Confirmada (FURB) |
| VOELCKER, G.; MACAGNAN, C. B.; VANCIN, D. Uma análise da tomada de risco em firmas familiares listadas na B3. **BBR – Brazilian Business Review**, Vitória, v. 17, n. 4, p. 399-418, 2020. DOI: 10.15728/bbr.2020.17.4.3. | Confirmada (SciELO, Redalyc). O estudo conclui que as familiares são mais avessas a risco, o que pode reforçar o referencial |
| WELCH, B. L. The generalization of "Student's" problem when several different population variances are involved. **Biometrika**, v. 34, n. 1-2, p. 28-35, 1947. | Clássica; não verificada na web nesta sessão |
| MANN, H. B.; WHITNEY, D. R. On a test of whether one of two random variables is stochastically larger than the other. **The Annals of Mathematical Statistics**, v. 18, n. 1, p. 50-60, 1947. | Clássica; não verificada na web nesta sessão |
| WASSERSTEIN, R. L.; LAZAR, N. A. The ASA statement on p-values: context, process, and purpose. **The American Statistician**, v. 70, n. 2, p. 129-133, 2016. | Clássica; não verificada na web nesta sessão |
| RIBEIRO, M. J. S.; AZEVEDO, Y. G. P.; PRADO, A. G. S.; PINHEIRO, A. B. Family hands, greener firms? […] **Business Strategy & Development**, v. 9, e70331, 2026. | **Não verificada.** Confira o DOI e os dados no artigo |
| EY; UNIVERSITY OF ST.GALLEN. **Global 500 Family Business Index**. | **Não verificada.** Informe edição, URL e data de acesso |
| BRASIL. **Lei nº 6.404, de 15 de dezembro de 1976**. Dispõe sobre as sociedades por ações. | Usar o link do Planalto e a data de acesso |

### 3.3 Na lista, mas não citadas no texto: retirar

- ALMEIDA (2020), *Revolução tecnológica no mundo dos negócios…*: não aparece no texto.
- CUNHA, ADAM e BOFF (2024), *conflito trabalho-família… auditores*: não aparece no texto e não tem relação com
  o tema.
- BLUNDELL e BOND (1998): não está na lista, mas era citado na seção 3 antiga. Com a nova Metodologia, deixa
  de ser citado.

### 3.4 Siglas (checagem manual, equivalente ao `check_acronyms.py`)

| Sigla | Situação |
|---|---|
| SEW | Definida duas vezes (Introdução e 2.1). Corrigido em P5 |
| B3 | Não é definida em nenhum lugar. Na primeira ocorrência, escreva "B3 S.A. – Brasil, Bolsa, Balcão (B3)" |
| CVM | Definida na seção 3.3 ✓ |
| EBITDA, PL | Definidas no Quadro 4; na primeira menção do texto, escreva "patrimônio líquido (PL)" |
| COVID-19 | Dispensa definição |
