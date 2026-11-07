# Parecer do Advogado do Diabo (assento fixo)

*ARS `academic-paper-reviewer`, modo `full`, 07/11/2026. Assento 5 de 5, sem cartão de configuração.
Manuscrito avaliado: `manuscrito.txt` (texto extraído de `tcc/latex/build/main.pdf`). Material de apoio
consultado: `tcc/analise/saidas/resultados.md`, que a banca também terá. Revisão feita sem ler os
pareceres dos outros assentos. Nenhum script foi executado.*

## Estado de calibração

`NOT_CALIBRATED`

`criteria_binding_unavailable`: os critérios da banca não foram fornecidos. Este parecer não afirma
aderência a critérios da instituição. Os juízos abaixo usam apenas as dimensões de contestação do
próprio agente.

## Juízos por critério

| Dimensão / critério | Fonte do critério | Juízo | Âncoras | Justificativa | Incerteza ou limite | Pesa na decisão? |
|---|---|---|---|---|---|---|
| 1. Tese central | agente DA, dimensão 1 | PARTLY_MEETS | §4.5; §5 | A conclusão principal (H1 não confirmada) se sustenta. A tese secundária (a aversão a credores aparece no prazo) é mais fraca que uma explicação alternativa mais simples (tamanho e acesso ao mercado de capitais) | Não há dados por empresa do prazo da dívida no manuscrito | sim: é a mensagem que o resumo e as considerações levam |
| 2. Escolha seletiva | agente DA, dimensão 2 | PARTLY_MEETS | Quadro 4; Tabela 2; `resultados.md` §1 e §6 | Os indicadores secundários sobre PL e a média ponderada estão no material de apoio, mas não no texto, e vão contra H1 ou são neutros. A omissão não é toda num sentido só: a liquidez corrente, também omitida, favorece as familiares | A exclusão dos indicadores sobre PL tem justificativa declarada (§3.4) | sim |
| 3. Viés de confirmação | agente DA, dimensão 3 | PARTLY_MEETS | §2.2; §4.5 | O referencial deixa as duas direções abertas, tanto para o nível quanto para o prazo, e por isso qualquer resultado fica "compatível" | — | sim |
| 4. Cadeia lógica | agente DA, dimensão 4 | PARTLY_MEETS | §2.1; §2.2; §4.5 | O mecanismo central (a família evita interferência de credores) não tem evidência direta nas fontes citadas. O prazo não estava na H1 | — | sim |
| 5. Generalização excessiva | agente DA, dimensão 5 | PARTLY_MEETS | §5, 2.º parágrafo | "Natureza do passivo" é apresentada como achado, embora seja confundida com o subsetor | — | sim |
| 6. Caminhos alternativos | agente DA, dimensão 6 | DOES_NOT_MEET | §4.4; §4.5; §5 | Tamanho, subsetor, regulação da ANS, ciclo da Selic, reclassificação contábil da parcela corrente e eventos societários (IPO, fusões) não são discutidos como rivais do prazo; só subsetor e tamanho aparecem, nas limitações | Confiança média nos fatos externos, que o autor deve conferir | sim |
| 7. Partes interessadas | agente DA, dimensão 7 | PARTLY_MEETS | §1; §5 | Credores aparecem só como ameaça, não como quem oferta crédito; o regulador setorial e os minoritários não aparecem | — | não |
| 8. Teste do "e daí?" | agente DA, dimensão 8 | PARTLY_MEETS | §5, 4.º parágrafo | A implicação prática é óbvia para analistas de crédito; a contribuição real é metodológica (sensibilidade ao critério) | Nível de exigência de TCC de graduação | não |
| 9. Calibração por norma da área | agente DA, dimensão 9 | MEETS | — | Nenhum achado MAIOR depende de uma norma externa não verificável; o de testes múltiplos se apoia em fonte que o próprio TCC cita | — | não |

Estes juízos não são somados, ponderados nem convertidos em gravidade.

## O que o trabalho faz bem (genuíno)

- Relata um resultado nulo como nulo, sem forçar significância, e diz por escrito que a diferença na
  dívida onerosa "depende de uma única observação" (§4.4). É raro e correto.
- A unidade de análise é a empresa (média por companhia), e não a observação empresa-ano, o que evita
  significância artificial (§3.5 b).
- Os subperíodos aparecem rotulados como exploratórios, e todos os resultados são reportados, inclusive
  os não significativos (§3.5 c).

## Contra-argumento mais forte

O TCC conclui que, embora H1 não se confirme, "a aversão à interferência de credores parece se
manifestar mais na escolha do prazo do que na quantidade de dívida" (§4.5). Esse é o único achado
positivo que o resumo e as considerações levam ao leitor. Há uma explicação mais simples e que se ajusta
melhor aos dados: **o prazo da dívida reflete o tamanho e o acesso ao mercado de capitais, não o
controle familiar**. O grupo familiar reúne as maiores companhias da amostra (Rede D'Or, Hapvida, Hypera,
Dasa, RaiaDrogasil; mediana de capital empregado de R$ 6,5 bi contra R$ 1,7 bi nas não familiares,
`resultados.md` §6). Essas empresas emitem debêntures longas. O grupo não familiar contém as duas menores
(Lifemed e Biomm), e é justamente a Lifemed, com 66% da dívida no curto prazo, que o próprio texto aponta
como responsável pela dispersão. O próprio Diamond (1991), citado como apoio, liga o prazo da dívida à
qualidade de crédito da empresa, e não às preferências de quem a controla. A significância durante a
pandemia (2020–2021) também tem leitura rival: foi o período de Selic mínima e de forte emissão de
debêntures, de que se beneficiaram as empresas com acesso ao mercado. Some-se a isso que o prazo não
consta da H1, que o subperíodo foi definido depois de ver os dados, que há cerca de 45 p-valores com
apenas três abaixo de 5%, e que a "estabilidade entre cenários" vem de grupos familiares aninhados, que
compartilham as mesmas empresas. Fica, assim, um padrão descritivo que o tamanho explica sem recorrer à
riqueza socioemocional. Por fim, o referencial foi montado de modo que qualquer resultado seria
"compatível": a dívida longa traz *covenants*, a curta traz risco de refinanciamento; menos dívida é
preservação da SEW, mais dívida é preservação contra a diluição. Uma hipótese que nenhum dado pode
contrariar não está sendo testada. O valor que resta ao trabalho é real, mas é outro: mostrar que, nesta
amostra, a conclusão muda conforme o critério de empresa familiar.

## Lista de problemas

Nenhum problema foi classificado como CRÍTICO. A conclusão principal do trabalho (H1 não confirmada,
ausência de evidência estatística de diferença no nível de endividamento) se sustenta diante de todos os
contra-argumentos abaixo. Os problemas atingem a interpretação secundária (o prazo) e o enquadramento,
que podem ser corrigidos com reescrita e, no máximo, com tabelas adicionais feitas com dados que o autor
já tem. Nenhum deles, isoladamente, invalida a conclusão.

#### CRÍTICO

| # | Dimensão | Descrição | Evidence Anchor | Confiança | Fronteira da norma da área | Por que a evidência cruza a fronteira |
|---|---|---|---|---|---|---|

#### MAIOR

| # | Dimensão | Descrição | Evidence Anchor | Confiança | Fronteira da norma da área | Por que a evidência cruza a fronteira |
|---|---|---|---|---|---|---|
| M1 | 4. Cadeia lógica / 3. Viés de confirmação | **O arcabouço não é falseável.** A §2.2 atribui ameaça de interferência tanto à dívida longa (*covenants* mais rigorosos) quanto à curta (renovação frequente) e, para o nível, opõe a SEW (menos dívida) ao medo de diluição (mais dívida). Com isso, qualquer resultado, de nível ou de prazo, é declarado "compatível" (§4.5: "coerente com a literatura inconclusiva"). A preferência por prazos longos não é deduzida da teoria; é escolhida. Correção: dizer *ex ante* por que a ameaça do refinanciamento domina a dos *covenants* para famílias, ou apresentar o prazo como questão aberta e não como confirmação do mecanismo. | text: §2.2 "Essa relação de risco é especialmente associada às dívidas de longo prazo, que normalmente apresentam cláusulas restritivas mais rigorosas." | 4 (leitura direta do texto) | — | — |
| M2 | 6. Caminhos alternativos / 1. Tese central | **Tamanho e acesso a crédito explicam o prazo melhor que a SEW.** As familiares são maiores (mediana do capital empregado de R$ 6,5 bi contra R$ 1,7 bi) e as menores empresas da amostra (LMED, BIOM) são não familiares. A Lifemed, com 66% da dívida no curto prazo, é citada como fonte da dispersão. Diamond (1991) relaciona prazo à qualidade de crédito do tomador; usá-lo como apoio à preferência da família inverte o argumento do autor citado. Chamar de "postura mais conservadora" um prazo mais longo também é carregado de valor. Correção mínima: discutir o tamanho como explicação rival na §4.5 (não só nas limitações) e mostrar o prazo por empresa ou por faixa de tamanho. [VERIFICAR com o autor: conferir em Diamond (1991) a relação entre prazo e *rating*.] | text: §4.2 "a Lifemed concentrou 66% de sua dívida no curto prazo" | 4 (dados do próprio trabalho e do material de apoio; leitura de Diamond a conferir) | — | — |
| M3 | 5. Generalização excessiva | **"Natureza do passivo" como achado, quando é subsetor.** As considerações afirmam que a diferença "está na natureza do passivo, com menos dívida financeira nas familiares". Mas comércio e distribuição (PNVL, PFRM, RADL) é 100% familiar na amostra, e o próprio texto (§4.4) reconhece que RADL e PFRM estão entre as menos endividadas pelo modelo de negócio, que se financia com fornecedores. Além disso, a diferença na dívida onerosa não é significativa e inverte o sinal em C1 e C2. Não há achado de composição para explicar. Correção: retirar a frase das considerações ou reformulá-la como hipótese ligada ao subsetor. | text: §5 "a diferença observada está na natureza do passivo, com menos dívida financeira nas familiares, e não no seu tamanho." | 5 (contradição interna verificável) | — | — |
| M4 | 3. Viés de confirmação / 4. Cadeia lógica | **O achado do prazo pesa mais do que a evidência permite.** O prazo não está na H1 (que trata só do nível); o subperíodo foi definido durante a análise; o manuscrito traz cerca de 45 p-valores (Tabelas 2 a 4 e o teste sem a Biomm), dos quais 3 ficam abaixo de 5%. Sob a hipótese nula e com testes independentes, seriam esperados cerca de 2; como t e Mann-Whitney usam os mesmos dados, o número efetivo é menor, mas a ordem de grandeza não está longe do acaso. A "direção mantida nos três cenários" e os "8 de 8 exercícios" não são replicações independentes: os cenários são praticamente aninhados (as 5 familiares de C1 estão nas 10 de C3) e os exercícios repetem as mesmas empresas. O texto reconhece a cautela (§4.3, §4.5), mas o resumo e as considerações ("resultado mais estável", "aspecto mais promissor") voltam a reforçá-lo. Correção: manter o tom da §4.3 também no resumo e nas considerações e dizer explicitamente que os cenários compartilham empresas. | text: §4.3 "o resultado da pandemia é o único significativo a 5% entre os testes realizados" | 4 (contagem feita sobre as tabelas do manuscrito) | Wasserstein e Lazar (2016), citado no próprio TCC: p-valor isolado, sem considerar quantas análises foram feitas, não sustenta conclusão | O resultado de prazo é selecionado entre cerca de 45 testes e promovido a achado no resumo |
| M5 | 2. Escolha seletiva | **Resultados disponíveis à banca e ausentes do texto, em sua maioria desfavoráveis a H1.** O Quadro 4 define indicadores secundários sobre PL, mas nenhum resultado deles é reportado. No material de apoio, Exigível total / PL é maior nas familiares (153,6% contra 116,7%; F < NF em 2 de 8 anos), e Dívida bruta / PL e Dívida líquida / PL ficam em 4 de 8. A média ponderada pelo capital empregado reduz a diferença da dívida onerosa para 2 p.p. (32,5% contra 34,5%), indicando que as familiares pequenas puxam a média simples para baixo. O resumo diz "em todos os exercícios, menor endividamento oneroso" sem dizer que o sinal se inverte em C1 e C2. Por equilíbrio: a liquidez corrente, também omitida, favorece as familiares (p = 0,064). Correção: uma tabela em apêndice com todos os indicadores do Quadro 4 e a média ponderada, e no resumo a menção à inversão de sinal. | dataset: tcc/analise/saidas/resultados.md §1 linha "Exigível total / PL" e §6 "média ponderada por Capital Employed" | 5 (comparação direta entre o material de apoio e o texto) | — | — |
| M6 | 6. Caminhos alternativos | **A janela em que a diferença se abre coincide com eventos societários e com a classificação fixa.** As diferenças se abrem em 2021–2022 (Tabela 1: dívida onerosa de 26,0% contra 35,4% em 2021), justamente quando ocorreram as reorganizações de Hapvida, Rede D'Or e Fleury citadas na §3.3 e, segundo o conhecimento público, o IPO da Rede D'Or (dez./2020). Ofertas de ações reduzem a alavancagem de forma mecânica. A classificação pelo FRE mais recente, aplicada desde 2018, pode ainda pôr no grupo familiar empresas cuja estrutura de controle mudou no meio do período. O texto cita as mudanças de controle como limitação, mas não discute que elas coincidem com o "efeito pandemia". Correção: discutir esses eventos na §4.3 e/ou repetir os testes de prazo sem as empresas afetadas. [VERIFICAR: datas de IPO e de *follow-on* das empresas da amostra.] | text: §3.3 e) "A classificação é mantida fixa em todo o período, como em Tommasetti et al. (2019)." | 3 (as datas dos eventos vêm de conhecimento geral e precisam ser conferidas) | — | — |
| M7 | 4. Cadeia lógica (lacuna de evidência) | **O mecanismo central não tem apoio direto nas fontes.** A premissa de que famílias controladoras evitam dívida por medo de interferência dos credores, base da H1 e da leitura do prazo, é sustentada por Santos e Silva (2018), um estudo sobre remuneração de executivos, e por Costa, Matte e Monte-Mor (2018), sobre gerenciamento de resultados, sem foco em familiares. Nenhuma fonte citada testa a relação entre SEW e dívida. As duas fontes que tratam de família e dívida (Kayo, Brunaldi e Aldrighi, 2018; Poletti-Hughes e Martínez García, 2022) apontam, pela descrição do próprio autor, para mais dívida nas familiares e ainda estão marcadas [VERIFICAR]. Correção: apoiar a premissa em literatura que relacione SEW e risco ou dívida, e não só em fontes sobre outros temas. [Sugestão a conferir: Gómez-Mejía et al. (2007), *Administrative Science Quarterly*, origem do conceito de SEW.] | text: §2.1 "a prevalência do SEW gera um conflito latente com os credores" | 3 (o conteúdo das fontes foi avaliado pela descrição do autor, não pelos originais) | — | — |


#### MENOR

| # | Dimensão | Descrição | Âncora | Confiança |
|---|---|---|---|---|
| m1 | 5. Generalização | As considerações dizem que o menor endividamento oneroso é uma "tendência que se acentuou a partir da pandemia", mas a Tabela 1 e a §4.1 mostram a diferença quase desaparecendo em 2025 (26,4% contra 26,9%). A afirmação só vale para o prazo. | text: §5 "tendência que se acentuou a partir da pandemia" | 5 |
| m2 | Consistência interna | A média das não familiares no Cenário 1 aparece como 26,4% no texto e 26,3% na Tabela 4 (no material de apoio, 26,35). | text: §4.4 "30,9% contra 26,4% no Cenário 1" | 5 |
| m3 | 4. Cadeia lógica | Jensen (1986) é usado para dizer que a aversão a credores está "alinhada à Teoria da Agência" por um argumento sobre oportunidades de crescimento, sem mostrar que as familiares têm mais oportunidades. É um salto lógico. | text: §1 "alinhada à Teoria da Agência, que prevê que empresas com muitas oportunidades de crescimento" | 4 |
| m4 | 8. "E daí?" | A afirmação de novidade ("setor ainda pouco explorado") não vem acompanhada de busca ou de citação que a sustente. | absence: §5, 4.º parágrafo — expected evidência de busca ou citação que sustente a lacuna setorial; checked §1, §2, §5 e lista de referências | 4 |
| m5 | 2. Escolha seletiva | A robustez é assimétrica: retira-se a única não familiar sem dívida (SAUD), mas não as familiares extremas (RADL e PFRM, com 12,8% e 16,5%) nem a HAPV, com dívida nula em 2018. Um teste deixando uma empresa de fora por vez, em ambos os grupos, mostraria quão frágil é cada resultado. | text: §3.5 d) "excluindo a Bradsaúde, única companhia da amostra sem dívida financeira" | 4 |
| m6 | 8. "E daí?" | A implicação prática ("considerar a composição da dívida por prazo") é prática corrente na análise de crédito e não decorre especificamente dos resultados. | text: §5 "deve considerar a composição da dívida por prazo, e não apenas o seu nível" | 3 |
| m7 | Precisão | "As familiares concentram-se no subsetor de comércio e distribuição" é impreciso: são 3 de 10. O ponto relevante é que não há nenhuma não familiar nesse subsetor. | text: §5 "As familiares concentram-se no subsetor de comércio e distribuição" | 5 |
| m8 | 6. Caminhos alternativos | A participação da dívida de curto prazo das não familiares sobe para 54,3% em 2025 com apenas 5 empresas. A transferência mecânica de debêntures que se aproximam do vencimento para o passivo circulante pode produzir esse salto sem nenhuma decisão de financiamento. | table: Tabela 1, linha 2025, coluna Dívida CP / Dívida total NF | 3 |

## Explicações e caminhos alternativos ignorados

1. **Tamanho e acesso ao mercado de debêntures** (ver M2). Explica o prazo mais longo das familiares sem a
   SEW e é compatível com a significância justamente no período de crédito barato.
2. **Ciclo monetário, e não a pandemia como choque de crise.** A janela de 2020–2021 coincide com a Selic
   no piso histórico; a de 2022–2025, com juros altos. O texto lê a pandemia como "crise" em que a aversão
   a credores "deveria se manifestar com mais clareza" (§3.5 c), mas para as grandes empresas o período
   foi de crédito abundante e barato. [VERIFICAR: trajetória da Selic no período.]
3. **Modelo de negócio do subsetor** (ver M3). O varejo e a distribuição farmacêutica se financiam com
   fornecedores, o que reduz a dívida financeira sem mudar o passivo total. Isso reproduz exatamente o
   padrão "Exigível/Ativo igual, Dívida/Ativo menor".
4. **Regulação setorial.** Operadoras de planos (Hapvida, Bradsaúde/Odontoprev) estão sujeitas a exigências
   de garantias e de provisões técnicas da ANS, que afetam o passivo e a política de dívida
   independentemente de quem controla a empresa.
5. **Eventos societários e reclassificação contábil** (ver M6 e m8). IPOs, fusões e o vencimento de
   debêntures mudam os indicadores de forma mecânica.
6. **Grupo de comparação residual.** "Não familiar" reúne empresas controladas por banco (SAUD), de capital
   disperso (FLRY, QUAL) e pequenas companhias industriais. Mesmo uma diferença significativa compararia
   famílias com uma mistura, e não com outro tipo de controle definido.

## Perspectivas de partes interessadas ausentes

- Credores como **ofertantes** de crédito (bancos, debenturistas, BNDES): o texto só considera a demanda
  da família, não a oferta de crédito para cada empresa.
- O regulador setorial (ANS), para as operadoras de planos da amostra.
- Acionistas minoritários, que arcam com o custo de uma eventual subalavancagem motivada pela SEW.
- Gerações e perfis distintos de família (fundador × sucessores; família recém-saída de IPO), tratados
  como um bloco homogêneo.

## Premissa não examinada

O trabalho supõe que o endividamento observado é uma **escolha da empresa** (demanda), refletindo
preferências do controlador. Em uma amostra que mistura gigantes com acesso ao mercado de capitais e
empresas pequenas com prejuízo operacional (Biomm com EBITDA negativo até 2024), é provável que a oferta
de crédito determine boa parte do prazo e do nível da dívida. Se for assim, a comparação entre
familiares e não familiares mede, em parte, diferenças de acesso ao crédito, e não de preferência.

## Observações (não são defeitos)

- A contribuição mais defensável do trabalho é metodológica: na mesma amostra, a mudança do critério de
  empresa familiar inverte o sinal da diferença no endividamento oneroso. Isso merece mais destaque do que
  a leitura do prazo. Vale dizer que a inversão acontece porque três empresas (RADL, PFRM, HYPE) trocam de
  grupo, o que também ilustra a fragilidade de amostras pequenas.
- A discussão do resultado nulo (§4.5) depende da leitura de Kayo, Brunaldi e Aldrighi (2018) e de
  Poletti-Hughes e Martínez García (2022), que ainda estão marcados [VERIFICAR]. Se a conferência mudar o
  que esses estudos encontraram, o argumento das "forças opostas" precisa ser revisto.
- O [DECIDIR] sobre manter a menção ao System-GMM (§3.1): manter ajuda a justificar por que não há
  controles (tamanho, setor) e torna mais honesta a limitação apontada em M2 e M3.
- O tom da §4.3 ("indício compatível com a hipótese, e não como sua confirmação") é o adequado; o
  problema é só que o resumo e as considerações não o mantêm.

*Lembrete de integridade: este parecer foi gerado por IA em uma simulação de banca. As decisões sobre o
texto são do autor; confira as regras da FEA-RP/USP sobre uso de IA e declare esse uso se for exigido
(`/ars-disclosure`). As afirmações sobre fatos externos ao manuscrito (Diamond, 1991; datas de IPO; Selic;
ANS; Gómez-Mejía et al., 2007) estão marcadas para conferência e não foram verificadas nesta sessão.*
