# Leitura dos artigos brasileiros (texto completo)

Data da leitura: 20/11/2026. Ficha de leitura de 7 artigos de acesso aberto pedidos para responder à
banca (referências recentes e crítica de misturar operadoras de planos de saúde com varejo
farmacêutico).

**Como foi feito.** Os PDFs foram baixados das páginas das revistas (ou de repositório
institucional) e salvos em `tcc/referencias/pdfs/`. O texto foi extraído com `pdftotext`. Todas as
citações diretas abaixo foram conferidas por script contra o texto extraído do PDF, página por
página. Os números de página são os **números impressos no artigo**. Onde eles diferem do índice do
PDF, isso está indicado.

**Situação do texto completo**

| # | Artigo | Texto completo lido? | Arquivo |
|---|---|---|---|
| 1 | Monteiro, Gasparetto e Lunkes (2019) | Sim | `pdfs/monteiro2019.pdf` |
| 2 | Moura et al. (2020) | Sim | `pdfs/moura2020.pdf` |
| 3 | Andrietta e Monte-Cardoso (2022) | Sim (PDF da editora, depositado no repositório Pantheon/UFRJ, hdl 11422/19087; o SciELO bloqueou o download automático) | `pdfs/andrietta2022.pdf` |
| 4 | Goulart et al. (2023) | Sim (versão em português; a inglesa também foi baixada) | `pdfs/goulart2023_pt.pdf`, `pdfs/goulart2023_en.pdf` |
| 5 | Valcanover e Sonza (2023) | Sim (PDF do SciELO, versão em inglês) | `pdfs/valcanover2023.pdf` |
| 6 | Marques et al. (2025) | **NÃO.** O servidor da UERJ (e-publicacoes.uerj.br) recusou a conexão em todas as tentativas; não há cópia em repositório nem no Wayback acessível daqui. Só o **resumo** (depositado pela revista no Crossref) foi lido. | — |
| 7 | Quiraque, Sousa e Colauto (2026) | Sim | `pdfs/quiraque2026.pdf` |

Os `.txt` ao lado de cada PDF são a extração com marcadores `=== PDF p.N ===` (índice do PDF, não a
página impressa).

**Resultados do TCC usados para a conexão** (resumo dado pelo autor): sem diferença no endividamento
total entre familiares e não familiares; tendência **não significativa** de menor dívida bruta/ativo
nas familiares; familiares com **menos** dívida de curto prazo / dívida total, significativo a 5% na
pandemia (2020–2021).

> Atenção geral: nenhum dos artigos mede exatamente as mesmas razões do TCC. Antes de escrever "em
> linha com" ou "ao contrário de", confira a definição da variável indicada em cada ficha.

---

## 1. Monteiro, Gasparetto e Lunkes (2019)

**Referência (ABNT NBR 6023)**
MONTEIRO, Januário José; GASPARETTO, Valdirene; LUNKES, Rogério João. Influência da gestão familiar
na estrutura de capital. **Revista Pensamento Contemporâneo em Administração**, Rio de Janeiro,
v. 13, n. 2, p. 1-17, abr./jun. 2019. DOI: https://doi.org/10.12712/rpca.v13i2.28146.

- Páginas confirmadas no PDF: o rodapé traz "RPCA | Rio de Janeiro | v. 13 | n. 2 | abr. – jun. 2019"
  e a numeração vai de 1 a 17 (referências nas p. 14-17).

**Amostra, período e método** (p. 6-9)
- 266 empresas não financeiras da B3, 2013–2017; dados contábeis da Economatica e dados de família
  do Formulário de Referência (p. 6).
- A amostra inclui 9 empresas de "Serviços médicos Hospitalares, Análises e Diagnósticos" e 4 de
  "Medicamentos e Outros Produtos" (Tabela 1, p. 7).
- 38% da amostra foi classificada como familiar (p. 8). A classificação é **uma única dummy** (GF),
  baseada em Pérez-González (2006), que junta propriedade, fundador executivo e parentes na gestão
  (Quadro 2, p. 9). Correção para `NOVAS_REFERENCIAS.md`: o artigo não estima efeitos separados de
  propriedade, controle e gestão; ele os reúne numa só variável.
- Variáveis dependentes (Quadro 2, p. 9): ECP = PC/AT (passivo circulante / ativo total);
  ELP = PNC/AT; ET = (PC+PNC)/AT. São razões de **passivo total** sobre ativo, não de dívida onerosa.
- Regressão em painel com efeitos fixos (Hausman, p. 9).

**Achados principais**
- Gestão familiar associada **positivamente** ao endividamento de curto prazo, só a 10%
  (coef. 0,140; p = 0,10; Tabela 2, p. 10).
- Sem associação com endividamento de longo prazo (coef. -0,040; p = 0,74; Tabela 3, p. 11) nem com
  endividamento total (coef. 0,021; p = 0,87; Tabela 4, p. 11).
- R² within de 0,09 nos modelos de curto e longo prazo e de 0,32 no total (p. 10-12).
- Os autores leem o resultado como preferência das familiares por dívida de curto prazo e por
  capital próprio no longo prazo (p. 12-14).

**Trechos citáveis**
1. "Os achados evidenciam que empresas com estrutura de gestão familiar exercem influência sobre o
   endividamento de curto prazo." (p. 1)
2. "ao nível de significância de 10% constatou-se uma associação positiva entre a estrutura de
   gestão familiar e endividamento a curto prazo." (p. 13)
3. "a estrutura de gestão familiar não influencia no endividamento de longo prazo nem no
   endividamento total" (p. 13)

**Conexão com o TCC**
- **Endividamento total:** converge com o TCC (sem diferença). É o apoio brasileiro mais direto ao
  resultado nulo.
- **Curto prazo:** aponta na direção **oposta** à do TCC. Monteiro et al. acham familiares com mais
  passivo circulante/ativo (fraco, a 10%); o TCC acha familiares com menos dívida de curto prazo /
  dívida total (5%, pandemia). Mas as medidas são diferentes: PC/AT (todo o passivo circulante,
  incluindo fornecedores, sobre o ativo) contra a composição da dívida onerosa. Vale dizer isso
  explicitamente na Discussão em vez de tratar como contradição direta.
- Período (2013–2017) anterior ao do TCC; não cobre a pandemia.

---

## 2. Moura, Lanzarin, Mazzioni e Macêdo (2020)

**Referência (ABNT)**
MOURA, Geovanne Dias de; LANZARIN, Jovani; MAZZIONI, Sady; MACÊDO, Francisca Francivânia Rodrigues
Ribeiro. Qual a influência da gestão familiar no custo de financiamento da dívida? Análise em
companhias com estrutura de propriedade familiar. **Revista Contemporânea de Contabilidade**,
Florianópolis, v. 17, n. 43, p. 71-87, abr./jun. 2020. DOI:
https://doi.org/10.5007/2175-8069.2020v17n43p71.

- Páginas confirmadas no rodapé do PDF ("v. 17, n. 43, p. 71-87, abr./jun., 2020"). Na lista abaixo,
  as páginas são as impressas (a p. 71 é a 1ª página do PDF).

**Amostra, período e método** (p. 76-78)
- **Só companhias familiares** da B3 (não financeiras): 113 em 2012 a 125 em 2016 (p. 76). Familiar =
  último acionista controlador é família ou indivíduo, com pelo menos 10% dos votos (p. 76).
- A comparação é **gestão familiar × gestão não familiar dentro de empresas de propriedade familiar**
  (CEO familiar, presidente do conselho familiar, ambos), com dados de gestão em t-1 (p. 76-77).
- Custo da dívida = despesas financeiras / passivo oneroso médio (empréstimos, financiamentos e
  debêntures de curto e longo prazo) (Quadro 2, p. 77).
- Teste t (variâncias desiguais quando Levene significativo) e MQO com erro-padrão robusto (p. 78).

**Achados principais**
- CEO familiar: custo médio da dívida 0,38 contra 0,62 no período 2012–2016 (t = -3,15; p = 0,00;
  Tabela 2, p. 80).
- Presidente do conselho familiar: 0,43 contra 0,77 (Tabela 3, p. 80). CEO e presidente familiares:
  0,38 contra 0,59 (Tabela 4, p. 81).
- Na regressão, as três dummies de gestão familiar têm coeficiente negativo e significativo
  (DirPres_Fam -0,37***; PresCA_Fam -0,33***; ambos -0,23***), e o endividamento (controle) não é
  significativo (Tabela 5, p. 81).
- Interpretação: prevalece o efeito alinhamento (problema de agência principal-agente) (p. 82).
- Limitação apontada pelos autores: corte de 10% para propriedade familiar; sugerem 20% ou 50%
  (p. 83).

**Trechos citáveis**
1. "As companhias foram classificadas como familiares quando o último acionista controlador era uma
   família." (p. 71, resumo)
2. "dentre as empresas familiares, àquelas com diretor presidente familiar possuem menor custo de
   financiamento da dívida." (p. 80)
3. "a gestão familiar influenciava para redução do custo de financiamento da dívida" (p. 71, resumo;
   a mesma frase reaparece nas considerações finais, p. 83)

**Conexão com o TCC**
- Não mede nível nem composição da dívida; mede **custo**. Serve como canal teórico: se as
  familiares (com gestão familiar) pagam menos pela dívida, isso pode ajudar a explicar por que
  usam menos dívida de curto prazo (que tende a ser mais cara e mais arriscada) num choque como a
  pandemia. Isso é uma hipótese de discussão, **não** um resultado do artigo.
- Cuidado: a comparação do artigo é entre tipos de gestão dentro de empresas de propriedade
  familiar, não entre familiares e não familiares como no TCC.
- Útil na Metodologia como exemplo brasileiro de classificação pelo controlador último no
  Formulário de Referência (seções 12.6 e 12.9; p. 76-77).

---

## 3. Andrietta e Monte-Cardoso (2022)

**Referência (ABNT)**
ANDRIETTA, Lucas Salvador; MONTE-CARDOSO, Artur. Análise de demonstrações financeiras de empresas do
setor de saúde brasileiro (2009-2015): concentração, centralização de capital e expressões da
financeirização. **Cadernos de Saúde Pública**, Rio de Janeiro, v. 38, supl. 2, e00006020, 2022.
DOI: https://doi.org/10.1590/0102-311X00006020.

- O cabeçalho do PDF traz "Cad. Saúde Pública 2022; 38 Sup 2:e00006020". O artigo tem 16 páginas
  numeradas (1-16) dentro do número eletrônico; em ABNT, para citação direta use a página interna
  (ex.: p. 10). Recebido em 14/jan/2020, aprovado em 03/jun/2020.

**Amostra, período e método** (p. 1, 3-6)
- 43 empresas em cinco subsetores: planos de saúde, hospitais, varejo farmacêutico, indústria
  farmacêutica e serviços de apoio diagnóstico e terapêutico (SADT); 2009–2015 (p. 1).
- Banco BDES-B (demonstrações coletadas da CVM, sites, jornais e diários oficiais), comparado com
  empresas de capital aberto (Economatica, sem finanças e fundos) e com as 500 maiores da Exame
  (p. 4). Inclui empresas de capital fechado.
- Estudo descritivo, com medianas por subsetor. Endividamento medido por PCT = (PC+PNC)/PL
  (Quadro 1, p. 5; p. 6). Não há teste estatístico.

**Achados principais**
- O capital próprio pesava mais no setor de saúde que nas abertas: 41,2% contra 31,3% do ativo em
  2015 (p. 6).
- PCT mediana: setor de saúde de 119% (2009) para 101% (2015), abaixo das abertas (121%) e das Exame
  (154%) em 2015 (p. 10; Tabela 3, p. 11).
- Forte heterogeneidade entre subsetores: farmácias com a maior PCT (154% em 2015); queda clara nos
  hospitais e nos planos de saúde (planos: 161% em 2009 para 94% em 2015) (p. 10; Tabela 3, p. 11).
- Planos de saúde têm disponibilidades/ativo muito acima dos demais (sempre acima de 25%; 28% em
  2015), enquanto varejo e indústria farmacêutica ficam abaixo de 10% (p. 11; Tabela 4, p. 12). Os
  autores ligam isso à natureza do negócio e a motivos regulatórios (p. 13).
- Giro do ativo do varejo farmacêutico muito superior (309% em 2009; 227% em 2015) (p. 10).

**Trechos citáveis**
1. "o setor de farmácias registrou a maior mediana do indicador frente ao demais subsetores e aos
   outros dois conjuntos de empresas: 154% em 2015." (p. 10)
2. "Houve uma clara tendência ao desendividamento nos hospitais e nos planos de saúde, já o sentido
   não foi claro para outros três subsetores." (p. 10)
3. "foi relevante apenas no setor de planos e seguros de saúde, exatamente pela natureza do negócio"
   (p. 13; o sujeito da frase é "a importância da geração de receitas financeiras por meio de ativos
   muito líquidos")

**Conexão com o TCC**
- É a melhor referência para **responder à crítica da banca**: mostra, com dados contábeis, que
  operadoras de planos e varejo farmacêutico têm estruturas patrimoniais muito diferentes
  (endividamento, liquidez, giro). Justifica controlar por subsetor, analisar por subsetor ou
  rodar robustez sem as operadoras.
- O período (2009–2015) é anterior ao do TCC e a amostra inclui empresas fechadas; use como
  evidência de heterogeneidade estrutural, não como comparação direta de níveis.
- A PCT (passivo/PL) não é a mesma medida de dívida bruta/ativo do TCC.

---

## 4. Goulart, Oliveira, Santos, Paranaiba e Ferreira Neto (2023)

**Referência (ABNT)**
GOULART, Selma Querino Cruvinel; OLIVEIRA, Elis Regina de; SANTOS, Geovane Camilo dos; PARANAIBA,
Alexandre de Carvalho; FERREIRA NETO, Brasilino José. COVID-19: como a pandemia afetou o desempenho
econômico-financeiro das empresas do setor de saúde listadas na B3? **Contextus – Revista
Contemporânea de Economia e Gestão**, Fortaleza, v. 21, e81813, 2023. DOI:
https://doi.org/10.19094/contextus.2023.81813.

- O PDF em português tem páginas numeradas 1-13 dentro do e81813 (texto e referências até a p. 12;
  p. 13 é o expediente). Submetido em 11/10/2022; aceito em 10/12/2022; publicado on-line em
  28/03/2023 (p. 1).
- Correções para `NOVAS_REFERENCIAS.md`: o artigo tem título em português (usado acima, pois o TCC é
  em português) e o terceiro autor é "Geovane Camilo dos Santos" (p. 1).

**Amostra, período e método** (p. 6-7)
- 22 empresas dos subsetores de saúde da B3 (após excluir Kora Saúde e Mater Dei por falta de dados);
  2018–2019 (antes) contra 2020–2021 (pandemia); dados da Economatica (p. 6).
- Teste de Wilcoxon com 44 observações anuais por período (p. 6), por subsetor e para a amostra
  toda; depois, painel trimestral com efeitos aleatórios (191 observações), usando o log de óbitos
  por Covid-19 como variável explicativa (p. 6-7).
- Endividamento medido por PCT (capital de terceiros / capital próprio) (Tabela 1, p. 4).
- Classificação de subsetores da B3 usada pelos autores (Tabela 3, p. 6): Odontoprev, Qualicorp e
  Hapvida aparecem em "Serviços médicos"; Hypera e Blau aparecem em "Comércio e distribuição", junto
  com Raia Drogasil, Pague Menos, Dimed, D1000, Profarma e CM Hospitalar.

**Achados principais**
- Setor com "elevada dependência de capital de terceiros" antes e durante a pandemia; PCT média de
  152,40 (2018–2019) e 160,50 (2020–2021) (Tabela 4, p. 7).
- Amostra toda: a mediana da PCT subiu de 121,23 para 159,34, **sem significância** (p = 0,3505)
  (Tabela 7, p. 9).
- Serviços médicos: PCT subiu de 120,47 para 166,37 (p = 0,0475), com queda de margem líquida, ROA e
  ROE (Tabela 6, p. 8; texto, p. 9). Comércio e distribuição: PCT de 178,23 para 167,65, sem
  significância (p = 0,3011) (Tabela 6, p. 8).
- No painel, óbitos não afetam a PCT (coef. -0,000) (Tabela 8, p. 10).
- Inconsistência interna a registrar: na p. 9 o texto diz que houve "aumento significativo da
  mediana para LC, LS, ME e ROA", mas a Tabela 7 (p. 9) mostra queda das medianas de ME (17,57 para
  16,08) e ROA (5,73 para 4,55), e as considerações finais (p. 11) falam em "redução de ME e ROA".
  Não cite a frase da p. 9 sobre ME e ROA.

**Trechos citáveis**
1. "Trata-se de setor com elevada dependência de capital de terceiros nos dois períodos" (p. 7)
2. "Já o Subsetor de Serviços médico-hospitalares, análise e diagnósticos foi o mais afetado
   negativamente pela pandemia entre os quatro Subsetores, pois houve aumento estatisticamente
   significativo da dependência de capital" (p. 9)
3. "esse desempenho é heterogêneo dentro do subsetor e entre subsetores do setor de saúde" (p. 10)

**Conexão com o TCC**
- É o estudo mais próximo do recorte do TCC (empresas de saúde da B3, 2018–2021, antes e durante a
  pandemia) e usa teste não paramétrico, como o TCC. Serve para contextualizar o subperíodo
  2020–2021, em que o TCC encontra a diferença significativa na composição da dívida.
- Mostra que o choque da pandemia foi **desigual entre subsetores**: reforça a resposta à banca e
  sugere que o efeito "familiar" do TCC na pandemia pode estar misturado com efeito de subsetor
  (por exemplo, se familiares se concentram no varejo farmacêutico e não familiares em serviços
  médicos). Vale checar a distribuição familiar/não familiar por subsetor.
- A própria Tabela 3 do artigo mostra como a classificação setorial da B3 junta operadoras
  (Hapvida, Odontoprev) e corretora (Qualicorp) com hospitais e laboratórios. É um argumento a mais
  para o TCC não depender só do rótulo da B3.
- Não separa familiares de não familiares nem mede composição curto/longo prazo.

---

## 5. Valcanover e Sonza (2023)

**Referência (ABNT)**
VALCANOVER, Vanessa M.; SONZA, Igor B. "Family business": does the family structure affect the
performance of listed companies? **RAM. Revista de Administração Mackenzie**, São Paulo, v. 24,
n. 3, eRAMF230028, 2023. DOI: https://doi.org/10.1590/1678-6971/eRAMF230028.en.

- O PDF (versão em inglês) tem 26 páginas numeradas; a seção "To cite this paper" da p. 1 indica
  "24(3), 1–26". O número eletrônico no PDF é **eRAMF230028** (o Crossref registra eRAMD230028;
  prevalece o do PDF). Submetido em 08/02/2021; aprovado em 23/03/2022 (p. 1). Seção "Strategic
  Finance".

**Amostra, período e método** (p. 9-13)
- **Só empresas familiares** da B3: 753 observações de 112 empresas, 2010–2017 (p. 9). Dados de
  família dos formulários de referência da CVM e dos sites das empresas; dados financeiros da
  Economatica (p. 9).
- Familiar = pelo menos um fundador/descendente no conselho, fundador/descendente como CEO, ou pelo
  menos 5% das ações com fundador/herdeiro/família (Zhou et al., 2017) (p. 11).
- Variáveis dependentes de desempenho: ROA, ROE, Q de Tobin e market-to-book (Tabela 1, p. 10).
  Alavancagem (dívida de curto e longo prazo / patrimônio) entra como **controle** (Tabela 3, p. 12).
- GMM-Sys em duas etapas (p. 12-13).

**Achados principais**
- Efeito da estrutura familiar sobre o desempenho é ambíguo (p. 2). Fundador no conselho e fundador
  como CEO reduzem ROA e ROE; descendente como CEO reduz ROA e Q (Tabela 5, p. 15; texto, p. 17-18).
- Propriedade familiar (FOC) eleva o ROE (0,085, a 1%) (Tabela 5, p. 15; texto, p. 18).
- Alavancagem média de 0,862 (mediana 0,611) por unidade de patrimônio (Tabela 4 e texto, p. 14).
- Alavancagem positiva e significativa no ROA (0,034, a 1%), lida pelos autores como apoio à teoria
  do trade-off (p. 18).
- Observação de leitura: na Tabela 5 (p. 15) o coeficiente de FOC só é significativo no ROE (no MB
  é 0,042, não significativo), mas o texto da p. 19 conclui por efeito sobre "ROE e MB". Ao citar,
  prefira a tabela.

**Trechos citáveis**
1. "The impact of family structure on performance was ambiguous." (p. 2) / em português, no resumo:
   "O impacto da estrutura familiar no desempenho foi ambíguo." (p. 3)
2. "variables in Table 2 were used to classify the companies as family businesses" (p. 11)
3. "The increase of 1% in companies’ leverage led to an increase of 0.034% in ROA, with a
   significance of 1%." (p. 18)

**Conexão com o TCC**
- Não compara familiares com não familiares e não tem o endividamento como variável dependente. O
  uso principal é **conceitual/metodológico**: critério brasileiro recente de classificação de
  empresa familiar (p. 11) e evidência de que a família não é um bloco único (fundador ×
  descendente; propriedade × gestão), o que ajuda a explicar resultados nulos ou fracos no
  endividamento total quando se usa uma dummy única, como no TCC.
- Referência recente (2023) em periódico A2/SciELO, o que atende ao pedido da banca.

---

## 6. Marques, Lugoboni, Zittei e Araújo (2025) — TEXTO COMPLETO NÃO OBTIDO

**Referência (ABNT; dados do Crossref, páginas NÃO conferidas no PDF)**
MARQUES, Sandro Rios; LUGOBONI, Leonardo Fabris; ZITTEI, Marcus Vinicius Moreira; ARAÚJO, Juliano
Augusto Orsi de. Impacto das práticas de governança corporativa (RN 518/22) na solvência das
operadoras de planos de saúde de médio porte no Brasil. **Revista de Contabilidade do Mestrado em
Ciências Contábeis da UERJ**, Rio de Janeiro, v. 30, n. 1, p. 38-57, 2025. DOI:
https://doi.org/10.12957/rcmccuerj.2025.87849.

- **Situação:** não foi possível baixar o PDF. O servidor e-publicacoes.uerj.br derrubou todas as
  conexões (curl e WebFetch, várias tentativas); OpenAlex não lista cópia em repositório; o Wayback
  Machine não está acessível desta sessão. O PDF da revista está em
  https://www.e-publicacoes.uerj.br/rcmccuerj/article/download/87849/55474 — o autor pode baixá-lo
  pelo navegador e salvar em `tcc/referencias/pdfs/marques2025.pdf` para completar esta ficha.
- As páginas 38-57 e o fascículo vêm do Crossref; publicado on-line em 11/08/2025 (Crossref).

**O que se sabe pelo resumo (depositado pela revista no Crossref)**
- 38 operadoras de planos de saúde de médio porte obrigadas a reportar à ANS as práticas da RN
  518/2022 (data-base 31/12/2022); dados contábeis da ANS de 2014 a 2022.
- Estatística descritiva, teste de Mann-Whitney (por operadora e para o grupo) e agrupamento
  K-Means.
- Melhora geral da solvência e dos indicadores econômico-financeiros após a norma; relação positiva
  na solvência em 15 das 38 operadoras (cerca de 40%).

**Trecho do resumo** (sem página confirmada; não usar como citação direta com página até conferir
no PDF): "A contribuição do estudo indica que práticas de governança corporativa contribuem com a
solvência e desempenho financeiro das operadoras de planos de saúde."

**Conexão com o TCC**
- Mostra que as operadoras de planos têm **regime próprio de solvência e governança definido pela
  ANS** (RN 443/2019, substituída pela RN 518/2022). Isso reforça a crítica da banca: a estrutura de
  capital das operadoras é condicionada por regulação prudencial que não se aplica ao varejo
  farmacêutico. Bom para a Metodologia (justificar separação ou robustez sem operadoras).
- Achados detalhados, tabelas e páginas: **pendentes** até a leitura do PDF.

---

## 7. Quiraque, Sousa e Colauto (2026)

**Referência (ABNT)**
QUIRAQUE, Elcídio Henriques; SOUSA, Allison Manoel de; COLAUTO, Romualdo Douglas. Profitability and
leverage in family-managed and non-family firms. **Journal of Globalization, Competitiveness and
Governability**, [S. l.], v. 20, n. 1, p. 65-80, jan./abr. 2026. DOI:
https://doi.org/10.58416/gcg.2026.v20.n1.04.

- Páginas confirmadas no PDF: rodapé "pp: 65-80", "Enero - Abril 2026, Vol. 20 Num. 1". O PDF tem 16
  páginas; a p. 65 é a 1ª. Recebido em 14/02/2025; aceito em 13/04/2025 (p. 65). O local de
  publicação não aparece no PDF (o cabeçalho diz "GCG - LALP Georgetown University"); confira a
  norma do curso para referência sem local ([S. l.]).
- O PDF traz também títulos em espanhol e português ("Rentabilidade e endividamento em empresas de
  gestão familiar e não familiares").

**Amostra, período e método** (p. 69-71)
- Empresas não financeiras da B3, 2011–2024; de 376 empresas, ficaram 191 com pelo menos 50% das
  observações; 2.606 observações empresa-ano; excluídas empresas com PL negativo; winsorização a
  1%/99% (p. 69-70). Dados da Refinitiv Eikon e do Formulário de Referência (p. 70).
- Propriedade familiar: pelo menos 10% das ações votantes com a mesma família (Shyu, 2011); gestão
  familiar segundo Villalonga e Amit (2006): CEO, executivos ou presidente/conselheiros da família
  (p. 70).
- Alavancagem = dívida total / ativo total × 100 (Tabela 2, p. 70).
- Mann-Whitney para comparar grupos e GMM-Sys em duas etapas com interação ROA × gestão familiar
  (p. 71-72).

**Achados principais**
- Alavancagem média de 33,30% nas empresas de gestão familiar e 32,19% nas demais (p. 72).
- 88 empresas sempre com gestão familiar, 104 com gestão não familiar e 1 mista (p. 72).
- ROA reduz a alavancagem em todas as especificações (Modelo 1: -0,2500***; familiares:
  -0,3189**; não familiares: -0,2202***) (Tabela 4, p. 73).
- A interação ROA × gestão familiar não é significativa (0,0184), ou seja, a gestão familiar não
  intensifica a relação; H2 rejeitada (p. 74-75).
- **Inconsistência interna a registrar:** na p. 72 o texto do Mann-Whitney diz que o nível de dívida
  difere significativamente entre os grupos (Z = -2,757; p < 0,005), com a frase truncada "does is
  significantly differ"; na discussão (p. 74) os autores afirmam que as empresas de gestão familiar
  "do not exhibit differences" na dívida. Não cite o resultado do Mann-Whitney sem mencionar essa
  contradição. A Tabela 3 (p. 71-72) também tem rótulos de linha trocados (ROA/MB no bloco da LEV).
- Limitação declarada: só dívida total, sem separar curto e longo prazo (p. 76).

**Trechos citáveis**
1. "Brazilian firms tend to reduce their debt levels as they become more profitable. However, the
   findings also suggest that family management does not intensify this relationship." (p. 65) /
   em português, no resumo: "Os resultados indicam que as empresas brasileiras tendem a reduzir o
   endividamento à medida que se tornam mais rentáveis." (p. 65)
2. "firms with family members in top executive positions do not exhibit differences in third-party
   debt levels compared to firms managed by non-family executives." (p. 74)
3. "this research only analyzed overall debt, without distinguishing between short- and long-term
   liabilities." (p. 76)

**Conexão com o TCC**
- É a evidência brasileira mais recente e cobre todo o período do TCC (2018–2025 dentro de
  2011–2024). A conclusão da discussão (p. 74) apoia o resultado nulo do TCC para o endividamento
  total; a média descritiva (33,30% × 32,19%) é praticamente igual entre os grupos.
- A limitação declarada na p. 76 (não separar curto e longo prazo) é exatamente a lacuna que o
  resultado de composição da dívida do TCC ocupa. Bom argumento de contribuição na Introdução e na
  Discussão.
- Atenção: usa gestão familiar (não propriedade) e amostra de todos os setores; o TCC é setorial.

---

## Síntese para o texto do TCC

| Ponto do TCC | Artigos que apoiam | Artigos que contrastam ou qualificam |
|---|---|---|
| Sem diferença no endividamento total | Monteiro et al. (2019, p. 11-13); Quiraque et al. (2026, p. 72, 74) | Mann-Whitney de Quiraque et al. (p. 72) aponta diferença, mas contradiz a própria discussão |
| Menos dívida de curto prazo / dívida total nas familiares (pandemia) | Lacuna declarada por Quiraque et al. (2026, p. 76); canal de custo da dívida em Moura et al. (2020, p. 80-81) | Monteiro et al. (2019, p. 10, 13): familiares com **mais** PC/AT (a 10%; medida diferente) |
| Pandemia como subperíodo relevante | Goulart et al. (2023, p. 8-11): choque desigual entre subsetores da saúde na B3 | Goulart et al. não separam familiares de não familiares |
| Resposta à banca (operadoras × varejo) | Andrietta e Monte-Cardoso (2022, p. 10-13); Goulart et al. (2023, p. 6, 8-9); Marques et al. (2025, resumo — regulação ANS) | — |
| Definição de empresa familiar | Valcanover e Sonza (2023, p. 11); Moura et al. (2020, p. 76); Quiraque et al. (2026, p. 70); Monteiro et al. (2019, p. 7-9) | Cada um usa critério diferente (5%, 10%, gestão × propriedade) |

## Pendências

1. **Marques et al. (2025):** baixar o PDF pelo navegador, conferir as páginas 38-57 e extrair
   achados e citações com página.
2. Ao levar para o `referencias.bib`, use os dados confirmados acima. Há três correções em relação a
   `NOVAS_REFERENCIAS.md`: páginas de Monteiro (p. 1-17) e de Quiraque (p. 65-80); título em
   português e nome "Geovane Camilo dos Santos" em Goulart et al.; a dummy única de Monteiro et al.
3. Antes de afirmar convergência ou divergência na Discussão, confira as definições de variável
   (PC/AT, PCT = passivo/PL, dívida total/ativo, custo da dívida) contra as do TCC.
