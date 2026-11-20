# Leitura de artigos internacionais recentes (20/11/2026)

Resposta ao pedido da banca por referências recentes. Seis artigos sobre endividamento de empresas
familiares, definição de empresa familiar e tratamento de PL negativo.

**Como foi feito.** Os dados bibliográficos vêm dos metadados oficiais do DOI (API do Crossref).
Os PDFs foram baixados de fontes abertas (site da editora ou repositório institucional) e estão em
`tcc/referencias/pdfs/`. O texto foi extraído com `pdftotext`/`pdfplumber`. **Todos os trechos
entre aspas foram conferidos por script contra o texto do PDF, na página indicada** (a numeração é
a da revista, não a do arquivo). As traduções e os resumos em português são meus; confira antes de
usar. Onde só li o resumo, digo isso.

| # | Artigo | Leitura | PDF salvo |
|---|---|---|---|
| 1 | Hansen e Block (2021) | **Texto completo** (versão publicada, CC BY-NC, via EconStor) | `hansen_block_2021.pdf` |
| 2 | Bennedsen, Lu e Mehrotra (2027) | **Só resumo da versão publicada** + texto completo de uma **versão anterior (working paper, jan. 2025)** | `bennedsen_lu_mehrotra_2025_wp_sioe.pdf` (WP) |
| 3 | Muñoz-Bullón, Sanchez-Bueno e Velasco (2024) | **Texto completo** (versão publicada, CC BY, Springer) | `munoz_bullon_2024.pdf` |
| 4 | Blanco-Mazagatos et al. (2024) | **Texto completo** (versão publicada, CC BY, Springer) | `blanco_mazagatos_2024.pdf` |
| 5 | Luo, Liu e Tripathy (2021) | **Só resumo** (acesso fechado; nenhuma versão aberta encontrada) | — |
| 6 | Voordeckers et al. (2026) | **Texto completo** (versão publicada, acesso aberto, CC BY-NC-SA) | `voordeckers_2026.pdf` |

Sobre os resultados do TCC citados abaixo (seção 7 do `CONTEXTO_TCC.md`): sem diferença no
endividamento total; tendência não significativa de menor dívida bruta/ativo nas familiares;
familiares com menor dívida de curto prazo/dívida total, significativa a 5% na pandemia; resultado
sensível à definição de empresa familiar (C1, C2, C3).

---

## 1. Hansen e Block (2021): meta-análise

**Referência ABNT**

HANSEN, Christopher; BLOCK, Joern. Public family firms and capital structure: a meta-analysis.
**Corporate Governance: An International Review**, [s. l.], v. 29, n. 3, p. 297-319, 2021.
DOI: https://doi.org/10.1111/corg.12354.

> Publicado on-line em 11/01/2021 (o PDF traz "© 2020"). Use 2021, o ano do volume.

**Leitura:** texto completo (versão publicada, baixada do repositório EconStor, handle 10419/233738).

**Amostra e método.** Meta-análise de 869 tamanhos de efeito (correlações de Pearson) de 613 estudos
primários, cerca de 436.886 empresas de capital aberto em 48 países. Usa HOMA (meta-análise
univariada de Hedges e Olkin) e meta-regressão hierárquica com moderadores. Os moderadores são os
direitos de acionistas e credores (índices do *Doing Business*/Banco Mundial), a definição de empresa
familiar, a medida de alavancagem e o porte (p. 297-303).

**Principais achados**
- Relação geral levemente negativa e significativa entre ser empresa familiar e alavancagem:
  r = −0,017, p ≤ 0,001 (p. 303, Tabela 1). Cerca de 57% dos efeitos são negativos e 41% positivos
  (p. 304). Há grande heterogeneidade: I² acima de 56% (p. 304).
- **A definição de empresa familiar muda o resultado.** Propriedade familiar como variável contínua:
  r = −0,029. Gestão familiar: r = −0,024. *Dummy* de propriedade familiar: r = 0,002 (p = 0,69,
  não significativo). Presença da família no conselho: r = 0,006 (n.s.). A diferença entre propriedade
  contínua e *dummy* é significativa (p. 303-304, Tabela 1).
- **A medida de dívida importa.** Efeito mais negativo para dívida de longo prazo/ativo
  (r = −0,034). Para dívida total/ativo, r = −0,012. Para dívida de longo prazo/PL, r = −0,003, n.s.
  (p. 303-304).
- **Brasil:** um dos sete países com efeito **positivo** e significativo, ou seja, familiares mais
  endividadas: 19 tamanhos de efeito, 12 estudos, 5.442 empresas, r = 0,030, significativo a 5%
  (p. 305, Tabela 2; p. 304, 311).
- Direitos de acionistas mais fortes aumentam a alavancagem das familiares. Direitos de credores mais
  fortes a reduzem (p. 311). Segundo os autores, a visão de aversão ao risco e a de preservação do
  controle se conciliam, e qual prevalece depende do ambiente institucional (p. 311).
- Agenda de pesquisa: heterogeneidade entre familiares e composição da dívida (maturidade, dívida
  bancária ou pública) (p. 311-312).

**Trechos citáveis (conferidos)**
- "The findings show that, on average, listed family firms have a lower leverage ratio than listed nonfamily firms (r = −0.017, p ≤ 0.001)." (p. 303)
- "the mean effect sizes are positive and significant for Brazil, Kuwait, Pakistan, Poland, Sri Lanka, Taiwan, and Turkey" (p. 304)
- "we note the importance of family firm definitions used in studies on capital structure and its potential influence on study outcomes" (p. 311)

**Conexão com o TCC**
- Explica a ausência de diferença no endividamento total. O efeito médio mundial é muito pequeno
  (r = −0,017), e no Brasil o sinal é o oposto (r = +0,030). Com 16 empresas, um efeito desse tamanho
  dificilmente seria detectado. *Esta leitura sobre o poder do teste é minha; não está no artigo.*
- Apoia a sensibilidade aos cenários C1/C2/C3. Só a troca da definição (*dummy* ou contínua, gestão
  ou conselho) já altera o efeito na meta-análise. O TCC usa classificação binária (*dummy*), o grupo
  em que o efeito médio foi nulo.
- Os autores apontam a maturidade da dívida como lacuna (p. 312), o que reforça a relevância do
  achado sobre dívida de curto prazo/dívida total.

---

## 2. Bennedsen, Lu e Mehrotra (2027): definições de empresa familiar

**Referência ABNT (versão publicada)**

BENNEDSEN, Morten; LU, Yi-Chun; MEHROTRA, Vikas. Defining family firms: a survey of empirical
criteria. **Journal of Corporate Finance**, [s. l.], v. 102, 103075, jan. 2027.
DOI: https://doi.org/10.1016/j.jcorpfin.2026.103075.

**Referência ABNT (versão lida: working paper)**

BENNEDSEN, Morten; LU, Yi-Chun; MEHROTRA, Vikas. **What is a family firm and why does it matter?**
A survey of family firm definitions. [S. l.: s. n.], 20 jan. 2025. Working paper apresentado na
conferência da SIOE 2025. Disponível em:
https://extranet.sioe.org/uploads/sioe2025/lu-2025-01-31_3374.pdf. Acesso em: 20 nov. 2026.

**Leitura.** O texto completo da versão publicada **não foi lido**. O ScienceDirect bloqueou o
acesso desta sessão (erro 403/Cloudflare), embora o artigo conste como acesso aberto (CC BY). Li:
(a) o resumo da versão publicada, só por fonte secundária, porque o Crossref não traz o resumo. A
fonte foi a página do INSEAD, lida por ferramenta que parafraseia, portanto **sem texto literal
verificado**; (b) o **texto completo do working paper de jan. 2025**, uma versão anterior com números
diferentes.

**Versão publicada (resumo; não verificado literalmente).** Os autores revisam 153 estudos empíricos e
encontram 192 definições operacionais, agrupadas em 25 tipos. Reduzem tudo a cinco dimensões
(propriedade, gestão, conselho, enraizamento da família no negócio e sucessão). Mostram que definições
diferentes selecionam populações diferentes e produzem estimativas diferentes de desempenho e inovação.
Recomendam reportar os resultados sob regras de classificação alternativas. **Antes de citar esses
números, confira no PDF da revista** (https://doi.org/10.1016/j.jcorpfin.2026.103075).

**Working paper (texto completo lido, 45 p.)**
- Amostra: 122 artigos empíricos; 29 definições binárias diferentes (p. 1).
- A propriedade é critério único ou suficiente em 47% das definições, e a gestão familiar em só 15%.
  Os limiares de propriedade vão de 1 ação a mais de 50%, sendo 10% um limiar comum (p. 4).
- Exemplos de erro de classificação: Microsoft (fundador sem sucessão familiar) e Suzuki (controle
  dinástico com menos de 1% das ações) (p. 4-6). Em Villalonga e Amit (2006), a fração de empresas
  familiares na Fortune 500 cai de 37% para 19% e depois para 7% conforme os critérios ficam mais
  restritivos (p. 7-8).
- Conclusão: não propõem uma definição rígida. Recomendam análises de robustez com várias definições
  e incluir sucessão e enraizamento da família no negócio (p. 25-27).

**Trechos citáveis (conferidos no working paper; NÃO usar como citação da versão de 2027 sem conferir)**
- "the definition of family firms significantly influences key outcomes, such as their prevalence, performance relative to non-family firms, and innovation activity" (WP, p. 1)
- "We conclude by recommending that future research in family business prioritize robustness analyses using multiple definitions of family firms." (WP, p. 1)
- "the non-unified threshold from 5% to 50% resulted in a dramatic variation in studying the pools of “family firms”, hence raise questionable empirical findings" (WP, p. 25)

**Conexão com o TCC.** É a referência mais direta para justificar os três cenários. O TCC fez o que os
autores recomendam: testou mais de uma definição e reportou todas. O fato de o resultado variar entre
C1, C2 e C3 confirma o argumento do artigo e não é falha do trabalho. No TCC, o C1 (propriedade acima
de 50%) é o critério mais restritivo e o C3 o mais amplo. **Sugestão:** cite a versão publicada (2027)
só depois de conferir o texto. Se for citar trecho literal, use o working paper e identifique-o como tal.

---

## 3. Muñoz-Bullón, Sanchez-Bueno e Velasco (2024)

**Referência ABNT**

MUÑOZ-BULLÓN, Fernando; SANCHEZ-BUENO, Maria J.; VELASCO, Pilar. Exploring the link between family
ownership and leverage: a mediating pathway through socioemotional wealth objectives. **Review of
Managerial Science**, [s. l.], v. 18, n. 11, p. 3203-3252, 2024.
DOI: https://doi.org/10.1007/s11846-023-00713-1.

> Publicado on-line em 05/12/2023; volume de 2024.

**Leitura:** texto completo (versão publicada, CC BY).

**Amostra e método.** Empresas abertas de 15 países europeus, 2011-2018. Os dados vêm do ORBIS e do
Refinitiv Eikon (ESG). Foram excluídas as financeiras e as observações com **PL (common equity),
vendas ou dívida negativos**. A amostra final tem 3.713 observações empresa-ano (758 empresas)
(p. 3211-3212). A alavancagem é medida como dívida financeira de curto e longo prazo sobre ativo
contábil. A empresa familiar é definida por *dummy* (FAMILY20: último controlador com 20% ou mais é
pessoa ou família) e pela % de ações da maior família (FAMILYOWN) (p. 3213-3214). O método é GMM
sistêmico em dois estágios, com análise de mediação pelas dimensões de SEW: controle familiar,
horizonte de longo prazo e reputação (p. 3214-3216).

**Principais achados**
- Propriedade familiar reduz a alavancagem: FAMILY20 negativo (p < 0,05), alavancagem 0,45 p.p. menor
  nas familiares. FAMILYOWN também é negativo (p < 0,01) (p. 3218; Tabela 4, p. 3220).
- **Por maturidade (Tabela 13, p. 3241):** o efeito negativo é significativo para a **dívida de curto
  prazo** e não para a de longo prazo. FAMILY20 = −0,0103 (5%) na dívida de curto prazo e −0,0031
  (n.s.) na de longo prazo (p. 3219, 3241). *O texto não traz a definição exata de STDEBT/LTDEBT; a
  Tabela 10 só define LEVERAGE.*
- CEO da família reduz a dívida total e a de longo prazo, mas não a de curto prazo (p. 3221).
- A relação é mediada pelos objetivos de SEW. Desempenho abaixo da aspiração enfraquece essa mediação
  (p. 3230-3231, 3235).
- Agenda de pesquisa: estudar o papel da SEW na crise da COVID e considerar a maturidade da dívida
  (p. 3233-3234).

**Trechos citáveis (conferidos)**
- "The leverage ratio is 0.45 percentage points lower in FFs compared to NFFs." (p. 3218)
- "FFs’ reluctance to leverage remains statistically significant for short-term but not long-term debt." (p. 3219)
- "short-term borrowings pose the greatest threat to family control as a result of their greater financing risk, greater bankruptcy risk, and closer monitoring" (p. 3219)

**Conexão com o TCC**
- É o achado internacional mais próximo do resultado sobre composição da dívida. Familiares evitam
  sobretudo a dívida de curto prazo, porque ela ameaça o controle (risco de refinanciamento,
  falência e monitoramento). A medida é diferente da do TCC: lá é a dívida de curto prazo em nível
  (provavelmente escalada pelo ativo, ponto não confirmado no texto); no TCC é a participação do
  curto prazo na dívida total. Mesmo assim, a direção e o argumento teórico coincidem.
- Os próprios autores sugerem estudar a SEW na COVID (p. 3233). O resultado do TCC, significativo
  justamente na pandemia, responde a essa sugestão no contexto brasileiro.
- Excluir observações com PL negativo é prática citada (p. 3212). Serve como precedente para decidir
  o tratamento da Alliar (PL negativo em 2025).

---

## 4. Blanco-Mazagatos et al. (2024)

**Referência ABNT**

BLANCO-MAZAGATOS, Virginia; ROMERO-MERINO, M. Elena; SANTAMARÍA-MARISCAL, Marcos;
DELGADO-GARCÍA, Juan Bautista. One more piece of the family firm debt puzzle: the influence of
socioemotional wealth dimensions. **Small Business Economics**, [s. l.], v. 63, n. 2, p. 831-849, 2024.
DOI: https://doi.org/10.1007/s11187-024-00881-8.

> Pela NBR 6023:2018, com quatro autores ou mais pode-se usar "BLANCO-MAZAGATOS, Virginia *et al.*".

**Leitura:** texto completo (versão publicada, CC BY).

**Amostra e método.** Questionário enviado em fevereiro de 2019 aos CEOs familiares de uma amostra
estratificada de 1.000 empresas espanholas **fechadas** (base SABI). Empresa familiar: família com
mais de 50% da propriedade e envolvida na gestão e no conselho. Foram 155 respostas e 126 empresas na
amostra final (p. 838). A variável dependente é dívida financeira total sobre ativo contábil
(p. 838). As dimensões de SEWi (continuidade, proeminência, enriquecimento) seguem a escala de Debicki
et al. (2016). O método é OLS hierárquico, com robustez por Tobit, GLM e subamostras de alta e baixa
dívida (p. 838-841).

**Principais achados**
- A importância dada à **continuidade** da família no negócio **aumenta** a dívida. Proeminência e
  enriquecimento não têm efeito significativo (p. 841).
- Na subamostra de baixa dívida, a proeminência (reputação) reduz a dívida (p. 841).
- Os autores interpretam o resultado assim: o receio de perder o controle com a entrada de sócios
  externos leva as familiares a usar dívida (p. 845).
- A comparação familiar × não familiar segue inconclusiva na literatura, e a heterogeneidade entre
  familiares ajuda a explicar isso (p. 831, 834).
- Observação: na seção de robustez, o texto diz que CONTINUITY é "significant and negative" nas duas
  subamostras, mas logo em seguida interpreta o efeito como positivo (p. 841). Parece erro de
  redação; confira a Tabela 4 (p. 844) antes de citar esse ponto.

**Trechos citáveis (conferidos)**
- "The literature on debt financing in family firms is still inconclusive." (p. 831)
- "as argued by Michiels and Molly (2017), findings remain inconclusive" (p. 834)
- "Thus, the greater the importance attributed to CONTINUITY, the greater the company’s debt." (p. 841)

**Conexão com o TCC**
- Sustenta que diferenças entre familiares (objetivos da família) podem anular a diferença média
  familiar × não familiar. Isso é coerente com a ausência de diferença no endividamento total.
- A definição de empresa familiar (mais de 50% da propriedade e envolvimento na gestão) é próxima do
  cenário C1 do TCC.
- Limitação para a comparação: a amostra é de empresas **fechadas** espanholas, e o TCC estuda
  empresas abertas.

---

## 5. Luo, Liu e Tripathy (2021): PL negativo

**Referência ABNT**

LUO, Haowen; LIU, Ian; TRIPATHY, Niranjan. A study on firms with negative book value of equity.
**International Review of Finance**, [s. l.], v. 21, n. 1, p. 145-182, 2021.
DOI: https://doi.org/10.1111/irfi.12260.

> Publicado on-line em 18/03/2019; volume de 2021.

**Leitura: só o resumo.** O artigo é de acesso fechado (Unpaywall/OpenAlex: "closed"), e não achei
versão aberta (SSRN, repositório ou página dos autores). Sem trechos literais.

**Resumo (Crossref).** Estudo sobre empresas abertas dos EUA com PL contábil negativo. Essas empresas
são heterogêneas. Grande parte delas, mesmo com alavancagem acima de 100%, é financeira e
operacionalmente saudável. As saudáveis aumentam a dívida para financiar investimentos. Ativos
intangíveis fora do balanço, e a qualidade deles, ajudam a explicar a real capacidade de
endividamento dessas empresas.

**Informação não verificada.** Uma pré-visualização parcial no vLex (p. 145-147), resumida por
ferramenta automática, menciona cerca de 51% das empresas com PL negativo com lucro positivo e baixo
risco de insolvência, e passivo/ativo médio de cerca de 1,2. **Não use esses números sem ler o
artigo** (acesso pelo Portal de Periódicos CAPES/CAFe da USP).

**Conexão com o TCC.** Ajuda a fundamentar o tratamento da **Alliar (PL negativo em 2025)**:
- Indicadores com PL no denominador (Exigível/PL, DL/PL, D/(D+PL)) perdem significado ou ficam
  instáveis com PL negativo. Isso justifica priorizar medidas sobre o ativo (dívida bruta/ativo,
  passivo/ativo).
- PL negativo não significa necessariamente insolvência. Excluir a empresa precisa de justificativa
  e de um teste de robustez com e sem a Alliar. Muñoz-Bullón et al. (2024, p. 3212) servem de
  precedente para a exclusão, e Luo et al. (2021) para o cuidado ao interpretar.

---

## 6. Voordeckers et al. (2026): alavancagem zero

**Referência ABNT**

VOORDECKERS, Wim; MICHIELS, Anneleen; STEIJVERS, Tensie; JANSEN, Katrien. The influence of family
firm heterogeneity on a zero-leverage ratio. **European Journal of Family Business**, [s. l.], v. 16,
n. 1, p. 50-66, 2026. DOI: https://doi.org/10.24310/ejfb.16.1.2026.21412.

**Leitura:** texto completo (versão publicada, acesso aberto). A p. 57 tem camadas de texto
sobrepostas no PDF; os dados dessa página foram lidos com cuidado e só cito o que confere.

**Amostra e método.** Survey com CEOs de empresas **fechadas** da região de Flandres (Bélgica), com
10 a 500 empregados, combinado com dados contábeis da base Bel-First. Empresa familiar: família com
50% ou mais das ações e/ou empresa percebida como familiar (p. 57-58). Das respostas saíram 414
familiares, e a amostra final é de 248 (p. 58). As variáveis dependentes são dívida total zero (ZL)
e dívida de longo prazo zero (ZLTL) em 2019 (p. 58). O método é probit bivariado aparentemente não
relacionado (*seemingly unrelated bivariate probit*), com SEWi e variáveis de governança (p. 58).

**Principais achados**
- 25,4% das empresas da amostra têm alavancagem zero (p. 59).
- A literatura anterior concluiu que familiares são mais propensas a não ter dívida do que
  não familiares (p. 51-52).
- Proeminência (reputação) aumenta a probabilidade de não ter dívida de longo prazo (+3,97 p.p., 10%).
  Enriquecimento reduz essa probabilidade (−6,6 p.p., 1%). Continuidade não tem efeito (p. 59-60).
- CEO não familiar aumenta a probabilidade de não ter dívida de longo prazo (+18,2 p.p.). O mesmo vale
  para sócios familiares passivos. Os efeitos dependem um do outro (p. 61-62).
- Distinguir dívida total zero de dívida de longo prazo zero revela determinantes diferentes, ou seja,
  a maturidade importa (p. 58; resumo, p. 50).

**Trechos citáveis (conferidos)**
- "differences within family firms may be as substantial as, or even greater, than those between family and non-family firms" (p. 51)
- "They conclude that family firms are more likely to follow a zero-leverage policy than non-family firms" (p. 52)
- "passive family owners seem to have an aversion towards (long-term) debt, specifically when they cannot personally supervise how the borrowed funds are used" (p. 62)

**Conexão com o TCC**
- Caso **Bradsaúde (SAUD), dívida bruta zero.** A literatura de alavancagem zero mostra que não ter
  dívida é comum (25% da amostra belga) e não é uma anomalia. Ela também associa esse comportamento
  mais às familiares, mas no TCC a empresa sem dívida é **não familiar**. Isso reforça a decisão de
  manter a SAUD e fazer robustez sem ela.
- A heterogeneidade dentro do grupo familiar, que pode superar a diferença entre grupos (p. 51),
  ajuda a explicar a falta de significância com grupos pequenos e a sensibilidade à definição.
- Limitação: as empresas são fechadas, pequenas e médias, belgas, com dados de corte transversal
  (2019).

---

## Síntese para o texto do TCC

| Resultado do TCC | Artigos que dialogam |
|---|---|
| Sem diferença no endividamento total | Hansen e Block (2021): efeito médio pequeno e positivo no Brasil; Blanco-Mazagatos et al. (2024) e Voordeckers et al. (2026): heterogeneidade entre familiares |
| Tendência (n.s.) de menor dívida bruta/ativo nas familiares | Hansen e Block (2021): r = −0,017 no mundo; Muñoz-Bullón et al. (2024): −0,45 p.p. na Europa |
| Menor dívida de curto prazo nas familiares; significativa na pandemia | Muñoz-Bullón et al. (2024): efeito concentrado no curto prazo e sugestão de estudar a COVID; Hansen e Block (2021): maturidade como lacuna |
| Sensibilidade à definição (C1/C2/C3) | Bennedsen, Lu e Mehrotra (2027; WP 2025); Hansen e Block (2021): a definição muda o efeito |
| SAUD sem dívida; Alliar com PL negativo | Voordeckers et al. (2026); Luo, Liu e Tripathy (2021); Muñoz-Bullón et al. (2024, exclusão de PL negativo) |

**Pendências**
1. Ler o texto completo da versão publicada de Bennedsen, Lu e Mehrotra (2027) (acesso aberto no
   ScienceDirect, bloqueado nesta sessão) e conferir números e páginas.
2. Ler Luo, Liu e Tripathy (2021) pelo acesso CAPES/USP antes de citar qualquer número.
3. Conferir a Tabela 4 de Blanco-Mazagatos et al. (2024, p. 844), por causa da inconsistência de sinal
   no texto.
4. Converter as entradas para o `referencias.bib` quando o autor decidir quais usar.
