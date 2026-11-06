<!--
RASCUNHO da nova seção 3 – Metodologia (06/11/2026).
Substitui integralmente a seção 3 da "Entrega 1". Marcadores:
  [DECIDIR: ...]   = escolha pendente sua/da orientadora (ver notas no fim)
  [VERIFICAR: ...] = dado a confirmar na fonte antes da entrega
Números conferidos na auditoria de 06/11 (tcc/auditoria/AUDITORIA_CENARIO3.md).
-->

## 3. METODOLOGIA

Esta seção descreve o delineamento da pesquisa, a amostra e as fontes de dados, o critério de classificação das empresas familiares, os indicadores de endividamento e os procedimentos estatísticos empregados para avaliar a hipótese H1.

### 3.1 Abordagem e Estratégia da Pesquisa

A pesquisa adota abordagem quantitativa, de natureza descritiva e comparativa, com uso de dados secundários de companhias abertas. O objetivo é verificar se empresas de controle familiar e não familiar diferem quanto ao nível e à composição do endividamento, e não estimar uma relação causal entre a estrutura de controle e a estrutura de capital.

A proposta inicial previa um modelo de painel dinâmico estimado por System-GMM, aplicado a todas as companhias não financeiras da B3. Ao longo da coleta, a classificação manual das empresas a partir dos Formulários de Referência levou à delimitação de um único setor (seção 3.2), o que resultou em uma amostra de 16 companhias. Com esse número de unidades, estimadores de painel dinâmico baseados em instrumentos internos não são adequados, pois exigem um número de empresas consideravelmente maior que o de instrumentos. Optou-se, por isso, pela comparação entre grupos por meio de estatística descritiva e de testes de diferença entre grupos, complementados por análises de subperíodos e de robustez.

[DECIDIR: se a Maisa preferir não mencionar a proposta anterior, apague o segundo parágrafo a partir de "A proposta inicial" e mantenha apenas a última frase, adaptada.]

### 3.2 Definição da Amostra e Fontes de Dados

A população do estudo compreende as companhias abertas classificadas pela B3 no setor econômico de Saúde. A restrição a um único setor tem duas finalidades: reduzir a influência de diferenças setoriais na estrutura de capital, que a literatura aponta como determinante relevante do endividamento (Oliveira; Kayo, 2020), e viabilizar a classificação manual de cada companhia quanto ao controle familiar, que exige a leitura individual dos Formulários de Referência. [VERIFICAR: se houve outro motivo para a escolha do setor de saúde, por exemplo, a sugestão da orientadora ou a relevância do setor durante a pandemia, inclua aqui.]

Os dados contábeis foram extraídos da base Economática, em valores consolidados, com frequência trimestral, de 31/12/2018 a 31/12/2025 (29 datas-base). Os indicadores de fluxo, como EBITDA e despesa financeira, correspondem aos últimos 12 meses de cada data-base. Das 22 companhias do setor com dados na base, foram mantidas apenas as que possuem informações em todo o intervalo, para que os dois grupos sejam comparados no mesmo período. Foram excluídas seis empresas que abriram capital ou passaram a ter dados durante o período: D1000 (DMVF, dados a partir de 12/2019), Eurofarma (EUFA), Oncoclínicas (ONCO) e Viveo (VVEO), a partir de 12/2020, Mater Dei (MATD), a partir de 09/2021, e Pague Menos (PGMN), a partir de 09/2022. A amostra final é composta por 16 companhias, distribuídas em quatro subsetores da B3 (Quadro 1).

**Quadro 1 – Composição da amostra por subsetor e classificação (Cenário 3)**

| Subsetor (B3) | Familiares | Não familiares |
|---|---|---|
| Comércio e Distribuição | Dimed/Panvel (PNVL), Profarma (PFRM), RaiaDrogasil (RADL) | — |
| Medicamentos e Outros Produtos | Blau (BLAU), Hypera (HYPE), Ourofino (OFSA) | Biomm (BIOM) |
| Serviços Médico-Hospitalares, Análises e Diagnósticos | Dasa (DASA), Hapvida (HAPV), Rede D'Or (RDOR) | Alliar (AALR), Bradsaúde (SAUD), Fleury (FLRY), Qualicorp (QUAL) |
| Equipamentos | Baumer (BALM) | Lifemed (LMED) |
| **Total** | **10** | **6** |

Fonte: Elaborado pelo autor (2026), com base na classificação setorial da B3 e nos Formulários de Referência (CVM).

A série da Bradsaúde (SAUD) corresponde, no período analisado, à antiga Odontoprev (ODPV3), cuja denominação e código de negociação foram alterados. A companhia não apresenta dívida financeira em nenhuma das datas-base e foi mantida na amostra principal, com análise de robustez que a exclui (seção 3.5). [VERIFICAR: confirmar na DFP a ausência de empréstimos e financiamentos da SAUD e a dívida bruta nula da HAPV em 31/12/2018.]

### 3.3 Classificação das Empresas Familiares

Não há definição única de empresa familiar na literatura, e os estudos brasileiros combinam, de formas diferentes, critérios de propriedade, de controle e de participação da família na administração. Para esta pesquisa, foram reunidos os critérios de seis trabalhos (Quadro 2), e a partir deles foram construídos três cenários de classificação, que diferem principalmente no percentual mínimo de ações ordinárias detido pela família.

**Quadro 2 – Critérios de classificação de empresa familiar na literatura**

| Estudo | Participação mínima | Envolvimento na administração | Amostra |
|---|---|---|---|
| Santos e Silva (2018) | Mais de 15% das ações ordinárias, com a família no controle | Familiar no conselho de administração | 110 empresas da B3, 2010–2016 |
| Tommasetti et al. (2019) | Mais de 50% dos votos | Familiar como diretor-presidente ou presidente do conselho | 151 empresas da B3, 2012–2016 |
| Voelcker, Macagnan e Vancin (2020) | Família como acionista controladora declarada | Membro indicado pelo controlador ao conselho | 1.188 observações da B3, 2010–2017 |
| Poletti-Hughes e Martínez Garcia (2022) | Pelo menos 20% das ações | Familiar conselheiro, diretor-presidente ou presidente do conselho | 187 empresas da América Latina, 2005–2016 |
| Ribeiro et al. (2026) | Pelo menos 10% das ações ordinárias | Familiar na administração (dimensões tratadas separadamente) | 105 empresas da B3, 2010–2024 |
| EY e University of St.Gallen | Pelo menos 32% dos votos (companhia aberta) | Não exige | 500 maiores empresas familiares do mundo |

Fonte: Elaborado pelo autor (2026), com base nos estudos citados.

Em todos os cenários, a empresa é classificada como familiar somente se atender, simultaneamente, a três condições: (i) a família detém um percentual mínimo das ações ordinárias, somando a participação direta e a indireta; (ii) a família integra o controle declarado da companhia; e (iii) há membro da família na administração. A empresa que deixa de atender a pelo menos uma condição é classificada como não familiar. O Quadro 3 apresenta os três cenários.

**Quadro 3 – Cenários de classificação adotados**

| Cenário | Ações ordinárias da família | Controle | Administração | Base | Familiares × não familiares |
|---|---|---|---|---|---|
| Cenário 1 | Mais de 50% | Família integra o controle | Familiar como diretor-presidente ou presidente do conselho | Tommasetti et al. (2019) | 5 × 11 |
| Cenário 2 | Pelo menos 32% | Família integra o controle | Familiar no conselho de administração | EY e University of St.Gallen; Voelcker, Macagnan e Vancin (2020) | 7 × 9 |
| **Cenário 3 (principal)** | **Mais de 15%** | **Família integra o controle** | **Familiar no conselho de administração** | **Santos e Silva (2018)** | **10 × 6** |

Fonte: Elaborado pelo autor (2026).

O Cenário 3, que reproduz o critério de Santos e Silva (2018), foi adotado como classificação principal por três razões de método: trata-se de critério de estudo brasileiro que utiliza a mesma fonte de informação desta pesquisa (Formulário de Referência) e a mesma base de participação (ações ordinárias); capta o controle exercido por blocos familiares com participação inferior a 50%, frequentemente organizados por acordo de acionistas, situação comum entre as companhias da B3; e produz grupos de tamanho mais equilibrado, o que é relevante em uma amostra pequena. Os Cenários 1 e 2 são utilizados como testes de robustez, para verificar se os resultados se mantêm quando se exige uma participação familiar maior.

Para aplicar as condições, adotaram-se as seguintes regras, comuns aos três cenários:

a) **Base de participação:** considera-se o percentual das ações ordinárias, isto é, das ações com direito a voto, e não do capital total;

b) **Grupo familiar:** a "família" pode corresponder a uma ou mais famílias que integram o mesmo bloco de controle, inclusive por acordo de acionistas (art. 116 da Lei nº 6.404/1976). É o caso da RaiaDrogasil (RADL), controlada por um bloco formado por três famílias que, em conjunto, detêm cerca de 28% das ações ordinárias e têm membros no conselho de administração, o que a classifica como familiar no Cenário 3, mas não nos Cenários 1 e 2;

c) **Participação indireta:** soma-se a participação detida por meio de holdings, fundos de investimento em participações ou outras pessoas jurídicas controladas pela família, seguindo a cadeia societária até as pessoas físicas. Na Dasa (DASA), por exemplo, a participação da família Bueno, de cerca de 57% das ações ordinárias, é detida por meio de um fundo de investimento em participações;

d) **Família no controle:** a participação relevante não basta se a família não integra o controle declarado. Na Fleury (FLRY), a família Pardini detém cerca de 20% das ações ordinárias desde a incorporação do Instituto Hermes Pardini, mas não faz parte do bloco de controle, e por isso a companhia é classificada como não familiar em todos os cenários. Também são não familiares as companhias de capital disperso ou controladas por instituições, como a Bradsaúde (SAUD), controlada pelo Banco Bradesco;

e) **Fonte e data de referência:** as informações foram obtidas no Formulário de Referência mais recente disponível no site da Comissão de Valores Mobiliários (CVM), nos itens de controle e composição acionária (itens 15.1 e 15.2 até 2022 e itens 6.1 e 6.2 a partir de 2023) e de administração, complementadas pelos sites de relações com investidores. A classificação é mantida fixa em todo o período, como em Tommasetti et al. (2019). Mudanças relevantes de controle ao longo do período, como as reorganizações de Hapvida, Rede D'Or e Fleury em 2021–2022, são reconhecidas como limitação.

[VERIFICAR: percentuais de RADL (28,3%), DASA (56,7%) e FLRY (19,73%) no FRE mais recente, e a citação correta da Lei 6.404/1976 na lista de referências.]

### 3.4 Indicadores de Endividamento

Na ausência de dados de valor de mercado e de um modelo de regressão, o endividamento foi medido por indicadores contábeis calculados pela Economática, organizados em três níveis de prioridade conforme a sua relação com a hipótese (Quadro 4).

**Quadro 4 – Indicadores de endividamento**

| Prioridade | Indicador | Cálculo | O que mede |
|---|---|---|---|
| Principal | Dívida bruta / Ativo total | (Empréstimos, financiamentos e debêntures de curto e longo prazo) ÷ Ativo total | Endividamento oneroso: parcela do ativo financiada por credores financeiros, que impõem *covenants* e monitoramento |
| Principal | Exigível total / Ativo total | (Passivo circulante + Passivo não circulante) ÷ Ativo total | Endividamento geral, incluindo obrigações operacionais (fornecedores, salários, tributos, provisões) |
| Complementar | Dívida bruta / (Dívida bruta + PL) | Dívida bruta ÷ (Dívida bruta + Patrimônio líquido) | Estrutura de capital: proporção de dívida no capital investido |
| Complementar | Dívida líquida / EBITDA | (Dívida bruta − Caixa e aplicações) ÷ EBITDA dos últimos 12 meses | Capacidade de pagamento; principal métrica utilizada em *covenants* financeiros |
| Complementar | Dívida de curto prazo / Dívida total | Dívida onerosa de curto prazo ÷ Dívida onerosa total | Composição da dívida por prazo e exposição ao risco de refinanciamento |
| Secundário | Exigível total / PL; Dívida bruta / PL; Dívida líquida / PL | Passivo ou dívida ÷ Patrimônio líquido | Grau de endividamento em relação ao capital próprio |

Fonte: Elaborado pelo autor (2026), com base nas definições da Economática.

A Dívida bruta / Ativo total é o indicador mais diretamente ligado à hipótese, pois mede a dívida financeira, que traz os credores e as cláusulas restritivas discutidos na seção 2.2. O Exigível total / Ativo total permite verificar se uma eventual diferença se restringe à dívida financeira ou alcança o passivo como um todo. A composição da dívida por prazo foi incluída porque a dívida de curto prazo exige renovações frequentes com os credores e, portanto, aumenta a exposição da empresa à sua interferência.

Alguns indicadores não podem ser calculados em determinadas situações, e esses casos foram tratados da seguinte forma: a Dívida de curto prazo / Dívida total não é definida para a Bradsaúde, que não possui dívida financeira, e essa empresa é excluída apenas desse indicador; a Dívida líquida / EBITDA não é informada pela base quando o EBITDA é negativo, o que ocorre com a Biomm de 2018 a 2024. [DECIDIR: (a) manter a Biomm com o único valor disponível, de 2025, e informar isso em nota; (b) excluir a Biomm desse indicador; ou (c) reportar também a mediana dos grupos.] Os indicadores calculados sobre o patrimônio líquido são tratados como secundários, por se tornarem instáveis quando o PL é pequeno ou negativo, como ocorre com a Alliar em 2025.

### 3.5 Procedimentos de Análise

A análise foi realizada em quatro etapas, com uso do Google Planilhas. A planilha de apoio, com a base de dados, a classificação das empresas e todas as fórmulas, acompanha este trabalho. [VERIFICAR: como a planilha será disponibilizada à banca (anexo, apêndice ou link).]

**a) Análise descritiva.** Para cada indicador, calculou-se a média de cada grupo em cada data-base, como média simples entre as empresas, de modo que todas as companhias tenham o mesmo peso. A evolução dos grupos é apresentada em gráficos com as 29 datas trimestrais, e as tabelas registram os valores de 31 de dezembro de cada exercício, bem como o número de exercícios em que a média das familiares ficou abaixo da média das não familiares.

**b) Testes de diferença entre os grupos.** A unidade de análise dos testes é a empresa: para cada companhia, calculou-se a média do indicador nas oito datas de encerramento de exercício (31/12/2018 a 31/12/2025), obtendo-se uma observação por empresa. Esse procedimento foi adotado porque as observações de uma mesma empresa em trimestres ou anos consecutivos não são independentes entre si, e tratá-las como observações distintas superestimaria a significância das diferenças. Sobre essas médias, aplicaram-se dois testes bicaudais:

- o **teste t de Welch** (Welch, 1947), que compara as médias dos dois grupos sem exigir variâncias iguais nem grupos de mesmo tamanho; e
- o **teste U de Mann-Whitney** (Mann; Whitney, 1947), não paramétrico, que compara as posições (postos) das empresas de cada grupo e é menos sensível a valores extremos e à ausência de normalidade, comuns em indicadores contábeis de amostras pequenas. O p-valor foi obtido pela aproximação normal com correção de continuidade. [DECIDIR: se a opção for pelo p exato, troque esta frase por "O p-valor foi calculado de forma exata".]

Adotaram-se como referência os níveis de significância de 1%, 5% e 10%, e um p-valor entre 5% e 10% é interpretado como evidência fraca. Embora a hipótese H1 seja direcional, os testes bicaudais foram mantidos por serem mais conservadores e por a literatura apresentar argumentos nos dois sentidos (seção 2). Dado o número reduzido de empresas, que limita o poder dos testes, os resultados não significativos são interpretados como ausência de evidência estatística de diferença, e não como evidência de que os grupos são iguais (Wasserstein; Lazar, 2016).

**c) Análise por subperíodos.** Para verificar se o comportamento dos grupos se alterou diante de um choque externo, o período foi dividido em três subperíodos: pré-pandemia (2018–2019), pandemia de COVID-19 (2020–2021) e pós-pandemia (2022–2025). A pandemia exigiu decisões de financiamento rápidas e fora do planejamento das empresas, situação em que a aversão da família à exposição a credores, prevista pela perspectiva da riqueza socioemocional, deveria se manifestar com mais clareza. Os testes da etapa (b) foram repetidos com a média de cada empresa em cada subperíodo. Por ter sido definida durante a análise, essa divisão tem caráter exploratório, e os resultados dos três subperíodos são reportados integralmente, inclusive os não significativos.

**d) Análises de robustez.** Os testes foram repetidos (i) com as classificações dos Cenários 1 e 2, para verificar a sensibilidade dos resultados ao critério de empresa familiar; e (ii) excluindo a Bradsaúde, única companhia da amostra sem dívida financeira, cujos valores nulos reduzem a média das não familiares nos indicadores de dívida onerosa.

Como foram realizados diversos testes (vários indicadores, dois testes, subperíodos e cenários), um resultado significativo isolado deve ser interpretado com cautela, e as conclusões consideram o conjunto dos resultados, e não testes individuais.

<!--
[OPCIONAL – só incluir se a regressão for refeita com o subsetor corrigido e um script reprodutível (R):]
**e) Análise exploratória multivariada.** Como complemento, estimou-se uma regressão linear com dados empilhados (pooled), tendo como variável dependente a Dívida bruta / Ativo total e como variável de interesse uma variável binária para empresa familiar, controlando por tamanho (logaritmo do capital empregado), rentabilidade do ativo, liquidez corrente, imobilização do patrimônio líquido e efeitos de ano, com erros-padrão agrupados por empresa. Dado o número de empresas, os resultados dessa etapa são tratados como exploratórios.
-->

---

<!--
NOTAS PARA O AUTOR (apagar antes de colar no Word)

1. O que saiu em relação à Entrega 1: System-GMM, Blundell e Bond (1998), alavancagem de mercado,
   Q de Tobin, alavancagem média do setor, winsorização 1%/99% e a Tabela 1 de variáveis.
   Se a regressão exploratória não entrar, Blundell e Bond (1998) também sai das Referências.

2. Comentário da Maisa "exemplifique" (fim do 1º parágrafo da antiga 3.2): está atendido pelos
   exemplos das alíneas b) a d) da seção 3.3 (RADL, DASA, FLRY, SAUD).

3. Outras partes do Word que ficam incoerentes com esta Metodologia e precisam de ajuste:
   - Resumo: "testada com um modelo econométrico que controla por fatores da firma e do setor,
     usando dados em painel de companhias listadas na B3".
   - Introdução, problema de pesquisa: "mesmo após o controle de fatores setoriais e
     características específicas da firma".
   - Introdução, parágrafo de Oliveira e Kayo (2020): "permitindo uma análise causal mais precisa".
   - Introdução, justificativa: "ao aplicar uma abordagem capaz de isolar esses fatores".
   - Lista de Tabelas (Tabela 1 deixa de existir; agora há os Quadros 1 a 4).
   - Capa e folha de rosto: ano 2025.

4. Referências novas citadas nesta seção (incluir na lista e conferir os dados):
   - TOMMASETTI et al. (2019); VOELCKER; MACAGNAN; VANCIN (2020); POLETTI-HUGHES;
     MARTÍNEZ GARCIA (2022); RIBEIRO et al. (2026); EY; UNIVERSITY OF ST.GALLEN (edição e acesso).
   - WELCH, B. L. The generalization of "Student's" problem when several different population
     variances are involved. Biometrika, v. 34, n. 1-2, p. 28-35, 1947.
   - MANN, H. B.; WHITNEY, D. R. On a test of whether one of two random variables is
     stochastically larger than the other. The Annals of Mathematical Statistics, v. 18, n. 1,
     p. 50-60, 1947.
   - WASSERSTEIN, R. L.; LAZAR, N. A. The ASA statement on p-values: context, process, and
     purpose. The American Statistician, v. 70, n. 2, p. 129-133, 2016.
   - BRASIL. Lei nº 6.404, de 15 de dezembro de 1976 (Lei das Sociedades por Ações).
   - Fontes de dados: Economática; CVM (Formulários de Referência); B3 (classificação setorial).
-->
