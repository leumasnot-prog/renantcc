# Parecer – Revisor de Adequação (banca de TCC)

*Skill ARS `academic-paper-reviewer`, modo `full`, assento EIC (Revisor de Adequação, papel "Journal-Fit Reviewer" adaptado para banca de TCC). Parecer de um assento do painel: a decisão editorial cabe ao sintetizador.*

## Informações do manuscrito
- **Título:** Empresas familiares vs. não familiares: comportamentos de endividamento
- **Tipo:** Trabalho de Conclusão de Curso, Ciências Contábeis, FEA-RP/USP
- **Fonte avaliada:** `manuscrito.txt` (texto extraído do PDF), com conferência pontual de `tcc/latex/main.tex` e `capitulos/02-referencial.tex`
- **Data do parecer:** 07/11/2026
- **Rodada:** 1.ª

---

## Informações do revisor

### Papel
Revisor de Adequação (EIC), adaptado para banca de TCC.

### Identidade
Professor de Contabilidade Financeira de uma faculdade de economia, administração e contabilidade de universidade pública, com experiência em orientar e avaliar TCCs. Conhece os critérios usuais de bancas de graduação: contribuição, coerência entre problema, método e conclusão, e adequação às normas.

### Foco da revisão
(1) Se o trabalho tem o escopo e a contribuição esperados de um TCC de graduação; (2) se problema, objetivos, hipótese, método e conclusão estão alinhados; (3) apresentação: clareza, ABNT e uso de quadros, tabelas e figuras. Atenção especial: a conclusão responde ao problema da Introdução sem prometer mais do que o método entrega?

### Vínculo com critérios
`criteria_binding_unavailable`

Os critérios formais da banca não foram fornecidos. Este parecer não afirma aderência a nenhum critério institucional específico; as referências a "o que uma banca costuma esperar" são o julgamento do revisor, não uma norma vinculante.

### Status de calibração
`NOT_CALIBRATED`

---

## Avaliação geral

### Recomendação
- [ ] Aceitar
- [ ] Revisão menor
- [x] **Revisão maior**
- [ ] Rejeitar

"Revisão maior" aqui significa reescrita substancial de partes do texto (enquadramento da hipótese, argumento sobre o prazo da dívida e referencial teórico). Não exige novos dados nem nova análise, e o núcleo empírico se sustenta. Na linguagem de banca, é um trabalho aprovável depois de ajustes, e não um trabalho em risco.

### Confiança
**4** (alta). Adequação, coerência e normas estão dentro da minha área. Tenho menos segurança em detalhes estatísticos finos e na literatura internacional recente; nesses pontos, sinalizo a confiança achado a achado.

A confiança só informa incerteza e escopo; não altera severidade nem peso na decisão.

### Avaliação resumida
O trabalho compara o endividamento de 10 empresas familiares e 6 não familiares do setor de saúde da B3 (2018–2025), a partir da hipótese, derivada da riqueza socioemocional (SEW), de que as familiares se endividam menos. Usa indicadores contábeis, testes de Welch e de Mann-Whitney sobre médias por empresa, subperíodos em torno da pandemia e três critérios de classificação. Conclui que a hipótese não se confirma e que a diferença mais estável está no prazo da dívida.

Para um TCC de graduação, o escopo é adequado e a execução é cuidadosa. A conclusão responde diretamente ao problema de pesquisa e não declara confirmação onde não há. O trabalho declara com honestidade o caráter exploratório dos subperíodos, o problema dos testes múltiplos e a sensibilidade dos resultados. A classificação das empresas é o ponto mais bem documentado do texto.

As fraquezas estão no enquadramento, não nos dados. A hipótese trata só do nível de endividamento, mas a mensagem final do Resumo e das Considerações recai sobre o prazo, que nunca foi formulado como hipótese. O argumento teórico sobre o prazo é unilateral: o próprio texto associa os *covenants* à dívida de longo prazo. E o referencial teórico é curto para sustentar a hipótese: o conceito de SEW se apoia quase só em um estudo sobre remuneração de executivos. Há ainda inconsistências pontuais entre texto e tabelas, lacunas de ABNT nas referências e nos pré-textuais, e 11 pendências [VERIFICAR]/[DECIDIR] abertas.

Recomendo revisão maior, concentrada nos capítulos 2 e 5 e no Resumo.

---

## Pontos fortes

### S1: A conclusão responde ao problema, sem confirmar o que não foi confirmado
O problema pergunta se o controle familiar "está associado a diferentes níveis de endividamento", e as Considerações finais respondem nos mesmos termos. É exatamente o que a banca procura: o resultado nulo é assumido e explicado, e não maquiado.
**Âncora de evidência**: `text: Cap. 5, 4.º parágrafo "não foram encontradas evidências estatisticamente significativas de que a estrutura de controle familiar esteja associada a um nível de endividamento diferente"`

### S2: Interpretação correta de resultados não significativos
O texto distingue explicitamente "ausência de evidência" de "evidência de igualdade" e apoia essa leitura em referência pertinente (Wasserstein e Lazar, 2016). Muitos TCCs erram nesse ponto.
**Âncora de evidência**: `text: §3.5(b) "os resultados não significativos são interpretados como ausência de evidência estatística de diferença, e não como evidência de que os grupos são iguais"`

### S3: Classificação das empresas documentada e testada sob três critérios
O Quadro 2 reúne os critérios de seis trabalhos. O Quadro 3 transforma esses critérios em três cenários com a contagem de cada grupo, e as regras (a)–(e) da §3.3 explicam os casos difíceis (bloco de três famílias na RaiaDrogasil, FIP na Dasa, família Pardini fora do controle na Fleury). Isso torna a classificação auditável pela banca, e é a contribuição metodológica mais sólida do trabalho.
**Âncora de evidência**: `table: Quadro 3 — Cenários 1, 2 e 3 com base na literatura e grupos 5 × 11, 7 × 9 e 10 × 6`

### S4: Unidade de análise justificada
O trabalho usa uma observação por empresa nos testes e explica por quê. Isso evita a armadilha comum de tratar 29 trimestres × 16 empresas como observações independentes.
**Âncora de evidência**: `text: §3.5(b) "as observações de uma mesma empresa em trimestres ou anos consecutivos não são independentes entre si"`

### S5: Robustez reportada mesmo quando contraria a hipótese
A Tabela 4 mostra a inversão de sinal da dívida onerosa nos Cenários 1 e 2, e o texto explica a inversão pela saída de RaiaDrogasil, Profarma e Hypera do grupo familiar e pelo modelo de negócio do comércio e distribuição. Relatar o resultado desfavorável e explicá-lo é sinal de maturidade.
**Âncora de evidência**: `table: Tabela 4 — linhas C1 e C2, Dív. bruta / Ativo, F > NF (30,9% × 26,3% e 28,7% × 27,0%)`

### S6: Mudança de desenho explicada, com escopo coerente com um TCC
A passagem do System-GMM previsto no projeto para a comparação entre grupos foi justificada pelo tamanho da amostra, e não escondida. O desenho final (descritivo-comparativo, sem pretensão causal) é compatível com 16 empresas e está declarado logo no início da §3.1.
**Âncora de evidência**: `text: §3.1 "Com esse número de unidades, estimadores de painel dinâmico baseados em instrumentos internos não são adequados"`

---

## Fraquezas

### W1: A hipótese trata só do nível de endividamento, mas a conclusão principal é sobre o prazo
**Problema**: O problema de pesquisa (Cap. 1) pergunta por "níveis de endividamento", e a H1 (§2.2) trata só do nível. O objetivo geral já fala em "nível e a composição", mas a composição por prazo nunca vira hipótese. Mesmo assim, a última frase do Resumo, o 3.º parágrafo da §4.5 e o 4.º parágrafo do Cap. 5 apresentam o prazo como o achado central ("a diferença entre os grupos está mais no prazo do que na quantidade de dívida"). Quem lê só o Resumo e as Considerações sai com a impressão de que o trabalho mostrou algo sobre o prazo que ele não se propôs a testar.
**Âncora de evidência**: `text: §2.2, H1 "Empresas de controle familiar apresentam um nível de alavancagem financeira inferior ao de empresas não familiares"`
**Por que importa**: É o ponto em que a banca mais testa a coerência entre problema, hipótese e conclusão. O resultado sobre o prazo é o mais interessante do trabalho, mas é marginal no período completo (p = 0,058 só no Mann-Whitney), significativo a 5% apenas em um subperíodo exploratório e obtido entre muitos testes.
**Sugestão**: Escolha um caminho e aplique-o em todo o texto. (a) Incluir o prazo no problema ou num objetivo específico e apresentá-lo, na §2.2, como expectativa secundária derivada de Diamond (1991), dizendo com honestidade que ela não foi formalizada como hipótese antes da análise; ou (b) manter a H1 como está e rotular o achado sobre o prazo, no Resumo e no Cap. 5, como "resultado exploratório, não previsto na hipótese". Em qualquer caso, a última frase do Resumo deveria mencionar que o resultado sobre o prazo é exploratório.
**Severidade**: MAIOR
**Confiança**: 5 — núcleo da minha área: coerência estrutural de trabalhos acadêmicos

### W2: O argumento teórico sobre o prazo é unilateral
**Problema**: A Introdução e a §2.2 dizem que os *covenants* (o principal canal de interferência dos credores) se concentram na dívida de longo prazo. Logo depois, a §2.2 argumenta que a dívida de curto prazo expõe a empresa à renovação, e conclui que a família preferiria prazos mais longos. Pela lógica do próprio texto, a aversão à interferência dos credores pode levar a evitar tanto a dívida longa (por causa dos *covenants*) quanto a curta (por causa do refinanciamento). O texto não explica por que o segundo canal prevaleceria.
**Âncora de evidência**: `text: §2.2, 2.º parágrafo "Essa relação de risco é especialmente associada às dívidas de longo prazo, que normalmente apresentam cláusulas restritivas mais rigorosas"`
**Por que importa**: A interpretação central da §4.5 e do Cap. 5 ("a aversão à interferência de credores parece se manifestar mais na escolha do prazo") depende dessa preferência. Sem enfrentar a ambiguidade, a explicação parece construída depois de ver o resultado, e um membro da banca pode apontar que a teoria apresentada previa o contrário.
**Sugestão**: Acrescentar à §2.2 um parágrafo que pese os dois canais, explicando, por exemplo, por que o risco de não renovação em crise seria mais ameaçador ao controle do que *covenants* negociados de antemão, e reconhecer que a previsão teórica sobre o prazo é ambígua. Na §4.5, mencionar explicações alternativas para o prazo além da preferência familiar (por exemplo, o perfil de dívida típico de cada subsetor), já que o Quadro 1 mostra que o comércio e distribuição só tem empresas familiares.
**Severidade**: MAIOR
**Confiança**: 4 — área própria (contabilidade e dívida); o peso relativo dos dois canais na literatura é assunto do revisor de domínio

### W3: Referencial teórico curto para sustentar a hipótese
**Problema**: O Cap. 2 tem cerca de duas páginas e meia. O conceito de SEW, base da hipótese, é definido e sustentado quase só por Santos e Silva (2018), um estudo sobre remuneração de executivos, e por Ames et al. (2020). Não aparece a formulação original do conceito. As teorias do *trade-off* e da *pecking order*, mencionadas na Introdução, continuam sem citação (pendência já marcada pelo autor). O título da §2.1 promete "Conflitos de agência", mas o tema recebe uma frase.
**Âncora de evidência**: `absence: Cap. 2 (§2.1–2.2) — expected citação da formulação original do conceito de SEW e das teorias do trade-off e da pecking order; checked Cap. 1, §2.1, §2.2, §4.5 e lista de Referências`
**Por que importa**: A banca avalia se a hipótese decorre de uma base teórica suficiente. Apoiar o conceito central em um trabalho cujo objeto é outro (remuneração) enfraquece a derivação da H1, e um TCC de Contabilidade com hipótese sobre estrutura de capital costuma citar as teorias clássicas na fonte.
**Sugestão**: (i) Citar a fonte seminal do SEW. Sugestão a conferir antes de usar: Gómez-Mejía et al. (2007), *Administrative Science Quarterly*, sobre riqueza socioemocional e risco em empresas familiares. (ii) Resolver o [VERIFICAR] de Myers (1984) e de Myers e Majluf (1984). (iii) Ampliar a §2.1 com o conflito de agência entre controlador e minoritários, que é o mais relevante em empresas familiares brasileiras, ou retirar "Conflitos de agência" do título. (iv) Se possível, trazer um ou dois estudos nacionais sobre empresas familiares e endividamento além dos já citados. Todas as referências novas precisam ser verificadas na fonte.
**Severidade**: MAIOR
**Confiança**: 4 — o padrão de citar a fonte original é critério usual de banca; a literatura internacional recente é ponto cego declarado

### W4: Afirmação de que a diferença "se acentuou a partir da pandemia" não corresponde à Tabela 1
**Problema**: As Considerações finais dizem que a menor dívida onerosa das familiares foi uma "tendência que se acentuou a partir da pandemia". A Tabela 1 e a §4.1 mostram outra coisa: a diferença se ampliou em 2021–2022, voltou a se estreitar a partir de 2024 e quase desapareceu em 2025 (26,4% × 26,9%). Para o prazo, a frase é aceitável; para a dívida onerosa, não.
**Âncora de evidência**: `text: Cap. 5, 2.º parágrafo "tendência que se acentuou a partir da pandemia"`
**Por que importa**: É uma afirmação de síntese que contradiz a tabela do próprio trabalho; a banca costuma conferir esse tipo de frase.
**Sugestão**: Separar os dois indicadores: "na dívida onerosa, a diferença se ampliou em 2021–2022 e praticamente desapareceu em 2025; no prazo, ela se manteve ampla desde 2021".
**Severidade**: MENOR
**Confiança**: 5 — leitura direta da Tabela 1

### W5: Afirmação de que o resultado da pandemia é "o único significativo a 5%" contradiz a Tabela 4
**Problema**: A §4.3 diz que o resultado da pandemia é o único significativo a 5% "entre os testes realizados". A Tabela 4 mostra outro resultado a 5%: a Dívida bruta / Ativo sem a Bradsaúde (p = 0,027 no teste t). O Resumo e o Cap. 5 repetem a ideia ao tratar a pandemia como "a exceção".
**Âncora de evidência**: `text: §4.3, último parágrafo "o resultado da pandemia é o único significativo a 5% entre os testes realizados"`
**Por que importa**: A frase é um argumento de cautela (multiplicidade); se está factualmente errada, a cautela perde credibilidade.
**Sugestão**: Escrever "o único significativo a 5% na especificação principal" ou citar também o resultado sem a Bradsaúde.
**Severidade**: MENOR
**Confiança**: 5 — conferência entre texto e tabela

### W6: Divergência de valor entre a §4.4 e a Tabela 4
**Problema**: A §4.4 informa "30,9% contra 26,4% no Cenário 1", e a Tabela 4 registra 26,3% para as não familiares em C1.
**Âncora de evidência**: `table: Tabela 4 — linha C1, Dív. bruta / Ativo, NF = 26,3% (a §4.4 informa 26,4%)`
**Por que importa**: É pequena, mas a banca lê com a tabela ao lado, e divergências numéricas minam a confiança no restante.
**Sugestão**: Corrigir o texto para o valor da tabela (que sai do script) e refazer a conferência de todos os números citados no texto contra as Tabelas 1 a 4.
**Severidade**: MENOR
**Confiança**: 5 — conferência entre texto e tabela

### W7: Redação ambígua sobre o papel da Bradsaúde
**Problema**: As Considerações dizem que a diferença na dívida onerosa "dependeu da presença" da Bradsaúde. Na verdade, a Bradsaúde (dívida zero) reduz a média das não familiares e, portanto, diminui a diferença; é a falta de significância que depende dela. Um leitor apressado entende o contrário. Além disso, uma empresa sem dívida financeira é, em si, uma política de financiamento conservadora; excluí-la só do grupo não familiar favorece a hipótese, e o texto não discute isso.
**Âncora de evidência**: `text: Cap. 5, 3.º parágrafo "A diferença no endividamento oneroso dependeu da presença de uma única empresa sem dívida financeira"`
**Por que importa**: Afeta a leitura de um dos dois resultados de robustez destacados no Resumo.
**Sugestão**: Reescrever como "a significância da diferença dependeu da exclusão da Bradsaúde, cuja dívida nula reduz a média das não familiares" e acrescentar, na §3.5(d) ou na §4.4, uma frase dizendo por que a empresa continua na amostra principal: dívida zero é uma escolha legítima de financiamento.
**Severidade**: MENOR
**Confiança**: 4 — clareza de texto; a adequação estatística da exclusão é assunto do revisor de metodologia

### W8: Uso de Jensen (1986) desconectado do argumento
**Problema**: A Introdução diz que a política conservadora estaria "alinhada à Teoria da Agência" e invoca o argumento do fluxo de caixa livre de Jensen (1986). Esse argumento trata da dívida como disciplina sobre gestores com caixa ocioso, e não da aversão de controladores à interferência de credores. A ligação lógica entre as duas ideias não aparece, e o parênteses ("e, portanto, menor fluxo de caixa livre ocioso") deixa a frase difícil de seguir.
**Âncora de evidência**: `text: Cap. 1, 4.º parágrafo "alinhada à Teoria da Agência, que prevê que empresas com muitas oportunidades de crescimento"`
**Por que importa**: Um professor de finanças tende a apontar a citação como deslocada; o restante do argumento não depende dela.
**Sugestão**: Retirar a frase ou reescrevê-la para dizer o que Jensen efetivamente sustenta e como isso se relaciona (ou se contrapõe) à hipótese.
**Severidade**: MENOR
**Confiança**: 4 — teoria de finanças corporativas de graduação

### W9: A Introdução promete "evitar" o efeito setorial; o trabalho mostra que ele permanece
**Problema**: A Introdução justifica o recorte setorial dizendo que a comparação "precisa evitar" a confusão entre setor e controle. A §4.4 e as limitações mostram que o efeito do subsetor (comércio e distribuição só com familiares) continua presente. A §3.2 usa um verbo mais adequado ("reduzir").
**Âncora de evidência**: `text: Cap. 1, 4.º parágrafo "precisa evitar que diferenças setoriais sejam confundidas com o efeito da estrutura de controle"`
**Por que importa**: É um pequeno excesso de promessa no início que o próprio trabalho desmente depois.
**Sugestão**: Usar "reduzir" na Introdução, como na §3.2.
**Severidade**: MENOR
**Confiança**: 5 — coerência interna

### W10: Termo da hipótese diferente do indicador principal
**Problema**: H1 e Cap. 5 falam em "alavancagem financeira"; o indicador principal é o "endividamento oneroso" (Dívida bruta / Ativo total). Em Contabilidade, "alavancagem financeira" também designa o efeito da dívida sobre o retorno do PL (GAF), o que pode confundir a banca.
**Âncora de evidência**: `text: Cap. 5, 1.º parágrafo "apresentariam menor alavancagem financeira"`
**Por que importa**: Clareza conceitual; a banca pergunta qual indicador operacionaliza a hipótese.
**Sugestão**: Reformular a H1 com o termo do indicador ("menor endividamento oneroso") ou dizer, logo após a H1, qual indicador a operacionaliza.
**Severidade**: MENOR
**Confiança**: 4 — terminologia contábil

### W11: Afirmação de contribuição sem suporte
**Problema**: O Cap. 5 diz que o setor é "ainda pouco explorado" nos estudos brasileiros sobre empresas familiares, sem citar nenhum levantamento que mostre isso. A justificativa da escolha do setor de saúde também está pendente (há um [VERIFICAR] na §3.2).
**Âncora de evidência**: `text: Cap. 5, 5.º parágrafo "sobre um setor ainda pouco explorado nos estudos sobre empresas familiares no Brasil"`
**Por que importa**: A banca costuma perguntar "como você sabe que é pouco explorado?".
**Sugestão**: Ou apoiar a afirmação na busca bibliográfica feita (por exemplo, "nos estudos nacionais consultados, nenhum se restringe ao setor de saúde"), ou retirá-la e destacar como contribuição o que o trabalho de fato mostra: a sensibilidade ao critério de classificação e o período com a pandemia.
**Severidade**: MENOR
**Confiança**: 4 — critério usual de banca

### W12: A Discussão dialoga pouco com os estudos nacionais mais próximos
**Problema**: Wildner, Oro e Petry (2020), sobre propriedade familiar e estrutura de capital de empresas brasileiras, é citado uma única vez, numa lista da Introdução, e não reaparece na Discussão. A §4.5 compara os resultados quase só com Kayo, Brunaldi e Aldrighi (2018) e Poletti-Hughes e Martínez García (2022). Pestana, Gomes e Lopes (2021), que estuda empresas portuguesas, é usado na Introdução para caracterizar o "ambiente corporativo brasileiro".
**Âncora de evidência**: `text: Referências "Influência da propriedade familiar na estrutura e custo de capital das empresas brasileiras"`
**Por que importa**: A Discussão é onde a banca espera ver o trabalho se posicionar em relação aos estudos anteriores.
**Sugestão**: Na §4.5, comparar a direção (e, se possível, a magnitude) dos resultados com os de Wildner, Oro e Petry (2020), depois de conferir no artigo o que ele encontrou. Na Introdução, usar uma fonte brasileira para a caracterização das empresas familiares no Brasil, ou deixar claro que Pestana et al. tratam de Portugal.
**Severidade**: MENOR
**Confiança**: 3 — não conferi o conteúdo de Wildner et al. (2020)

### W13: Pré-textuais incompletos para as ilustrações e tabelas existentes
**Problema**: Há Lista de quadros, mas não há Lista de tabelas nem Lista de ilustrações, embora o trabalho tenha 4 tabelas e 2 figuras. Em `main.tex`, as duas listas estão comentadas, com a nota "descomente ... quando houver figuras e tabelas". Também não há lista de siglas (SEW, B3, PL, EBITDA, CVM, FIP).
**Âncora de evidência**: `absence: pré-textuais — expected Lista de tabelas e Lista de ilustrações (NBR 14724); checked Lista de quadros, Sumário e trecho dos pré-textuais em tcc/latex/main.tex`
**Por que importa**: Elementos de forma que a banca confere com facilidade; a falta de uma lista quando existe a outra chama atenção.
**Sugestão**: Descomentar `\listoffigures*` e `\listoftables*`; avaliar uma lista de abreviaturas e siglas; conferir com o modelo do curso se a folha de aprovação e a ficha catalográfica são exigidas (ambas estão comentadas).
**Severidade**: MENOR
**Confiança**: 4 — NBR 14724; o modelo exato da FEA-RP não foi fornecido

### W14: Lacunas de ABNT nas referências
**Problema**: (i) Pestana, Gomes e Lopes (2021) está incompleta: sem volume, número, páginas ou DOI. (ii) "Martínez García" aparece em caixa baixa na citação (§4.5, Cap. 5) e na referência, enquanto os demais sobrenomes estão em caixa alta. (iii) Os documentos *on-line* (Lei n.º 6.404/1976 e EY/University of St. Gallen) não trazem "Acesso em:"; na Lei, a ementa aparece depois do endereço eletrônico. (iv) "s.d." para o índice da EY: a NBR 6023 recomenda indicar data provável entre colchetes.
**Âncora de evidência**: `text: Referências, Pestana, Gomes e Lopes "Revista Contabilidade & Finanças, São Paulo, 2021"`
**Por que importa**: Adequação às normas é critério explícito em bancas de graduação, e o CLAUDE.md do projeto fixa a ABNT.
**Sugestão**: Completar a referência de Pestana et al. com os dados conferidos na fonte; corrigir a caixa de Martínez García no `.bib` (por exemplo, `{MARTÍNEZ GARCÍA}`, ou o campo de sobrenome protegido); incluir "Acesso em:" nos documentos *on-line*; trocar "s.d." por data provável entre colchetes ou pela data de acesso, conforme o manual da instituição.
**Severidade**: MENOR
**Confiança**: 4 — NBR 6023; o manual da FEA-RP não foi fornecido

### W15: Exemplos empíricos no referencial teórico, repetidos na Metodologia
**Problema**: A §2.1 descreve a Baumer e a RaiaDrogasil (participações, cargos) dentro do referencial teórico, e a §3.3(b) repete o caso da RaiaDrogasil.
**Âncora de evidência**: `text: §2.1, 1.º parágrafo "a Baumer ilustra a presença simultânea dessas três dimensões"`
**Por que importa**: Mistura teoria e dados da amostra; a banca pode ler como falta de clareza sobre a função de cada capítulo.
**Sugestão**: Levar os dois exemplos para a §3.3, onde já estão as regras de classificação, e deixar a §2.1 só com o conceito.
**Severidade**: MENOR
**Confiança**: 4 — estrutura de trabalhos acadêmicos

---

## Comentários detalhados

### Adequação a um TCC de graduação
O tema (estrutura de controle e endividamento) é clássico em Contabilidade e Finanças, e o recorte (um setor, 16 empresas, 2018–2025) é viável para um aluno de graduação. A coleta manual nos Formulários de Referência é um esforço próprio e verificável. Em extensão (cerca de 29 páginas e 9.300 palavras), o trabalho está no padrão de um TCC. O que separaria um bom TCC de um TCC muito bom aqui é o Cap. 2 (W3) e a coerência do enquadramento (W1, W2).

### Originalidade e contribuição
A contribuição honesta é modesta e adequada ao nível: evidência descritiva recente (com a pandemia) em um setor, e demonstração de que o resultado depende do critério de classificação. A segunda é a mais defensável e deveria ganhar mais destaque nas Considerações. A afirmação de "setor pouco explorado" precisa de suporte (W11).

### Coerência estrutural (título → Resumo → Introdução → conclusão)
- **Título:** genérico ("comportamentos de endividamento") e não menciona o setor de saúde nem a B3. Sugiro algo como "Endividamento de empresas familiares e não familiares no setor de saúde da B3 (2018–2025)", se o curso permitir.
- **Problema × conclusão:** alinhados no nível (S1). Desalinhados na ênfase final sobre o prazo (W1).
- **Objetivos específicos:** os três são cumpridos: (i) Quadro 3; (ii) Tabelas 1 e 2; (iii) Tabelas 3 e 4.
- **Hipótese direcional × testes bicaudais:** a justificativa (§3.5) é razoável e está declarada.

### Título e Resumo
O Resumo tem cerca de 260 palavras, dentro da faixa usual da NBR 6028 para trabalhos acadêmicos, e cobre objetivo, base teórica, amostra, método, resultados e conclusão. Dois ajustes: marcar o resultado sobre o prazo como exploratório (W1) e revisar a afirmação sobre "a exceção" (W5). As palavras-chave são adequadas. O Abstract corresponde ao Resumo.

### Conclusão
A primeira metade do 4.º parágrafo do Cap. 5 é exemplar. A segunda metade ("A evidência descritiva, porém, sugere...") é aceitável porque usa "sugere" e "compatível", mas deveria dizer explicitamente que o resultado sobre o prazo foi obtido em análise exploratória e entre muitos testes, como a §4.5 já faz ("Dois cuidados limitam essa interpretação"). As limitações estão completas e honestas. As sugestões de pesquisa futura decorrem dos resultados.

### Apresentação: quadros, tabelas e figuras
- Quadros e tabelas estão numerados, titulados e com fonte, como exige a ABNT/IBGE. Os quadros (texto) e as tabelas (números) estão usados corretamente.
- As Figuras 1 e 2 não puderam ser avaliadas no texto extraído. O próprio autor já registrou que precisam ser refeitas, e que falta o gráfico da Dívida CP / Dívida total. Como é o resultado que a conclusão destaca, considero esse gráfico prioritário.
- "As Figura 1 e Figura 2" (§4.1) deve ser "As Figuras 1 e 2".
- Na Tabela 2, um asterisco só no 0,058 pode passar despercebido; o padrão está explicado na nota, então está correto.

### Pendências [VERIFICAR]/[DECIDIR]
Há 11 marcadores abertos. Não os trato como erros novos, mas todos precisam desaparecer da versão entregue, e os de verificação de citação (Myers; Oliveira e Kayo; Poletti-Hughes e Martínez García; Kayo et al.) são condição para a regra de integridade das referências. Duas opiniões, já que o autor pediu decisão:
- **[DECIDIR] System-GMM (§3.1):** manter uma versão curta. A banca valoriza a transparência sobre a mudança de desenho (S6).
- **[DECIDIR] p exato no Mann-Whitney (§3.5):** com grupos de 10 × 6, o p exato costuma ser preferido à aproximação normal. Deixo a decisão final ao revisor de metodologia (fora do meu foco; confiança 2).
- **[VERIFICAR] planilha (§3.5):** como a banca avalia só o texto, sem defesa oral, um apêndice com a classificação das empresas (participações e cargos) e um link para a planilha e o script ajudariam muito.

---

## Perguntas ao autor
1. O prazo da dívida foi pensado como hipótese desde o projeto ou surgiu durante a análise? A resposta define qual das duas opções da W1 é a honesta.
2. Por que a família preferiria se expor a *covenants* de longo prazo a se expor ao refinanciamento de curto prazo (W2)? Há algum estudo que sustente essa preferência?
3. O padrão do prazo continua se o subsetor de comércio e distribuição (só familiares) ficar de fora? Não estou pedindo a análise, mas, se ela já estiver na planilha, ela responderia à objeção mais provável da banca.
4. O manual do curso exige folha de aprovação, ficha catalográfica ou declaração de uso de IA? Lembro que o uso de ferramentas de IA na revisão deve ser declarado se a instituição exigir (`/ars-disclosure`).

---

## Questões menores (abaixo do limiar de achado)

### Linguagem
- §4.1: "As Figura 1 e Figura 2" → "As Figuras 1 e 2".
- Cap. 1, 1.º parágrafo: o [VERIFICAR] interrompe a frase; na versão final, a citação de *Trade-Off* e *Pecking Order* deve vir junto da primeira menção.
- Os termos estrangeiros (*Trade-Off*, *Pecking Order*, *covenants*) devem estar em itálico de forma uniforme; no texto extraído não dá para conferir o itálico.

### Citação
- As citações de Santos e Silva (2018) no Resumo e no Abstract são aceitáveis, mas alguns manuais preferem evitar citações no resumo; conferir no modelo do curso.
- A linha "Citado N vezes nas páginas" (*backref* do abnTeX2) não é exigida pela NBR 6023; conferir se a banca ou o modelo do curso a aceita.

### Layout
- Na §3.3, a lista (b)–(e) é interrompida pelo Quadro 3 no meio do item (b) ("nos ... Cenários 1 e 2"); posicionar o quadro antes ou depois da lista.
- O [VERIFICAR] dos percentuais da §3.3 também fica dividido entre duas páginas.

---

## Julgamentos por critério

Status de calibração: `NOT_CALIBRATED`. `criteria_binding_unavailable`: a fonte dos critérios abaixo é o cartão de configuração do revisor e as expectativas usuais de bancas de graduação, não critérios formais da banca.

| Dimensão / critério | Fonte do critério | Julgamento | Âncoras | Justificativa | Incerteza / limite de escopo | Pesa na decisão? |
|---|---|---|---|---|---|---|
| Escopo e contribuição de TCC | Cartão n.º 1, foco (1) | MEETS | S6; W11 | Escopo viável e bem executado; contribuição modesta, mas real | Sem critérios formais da banca | Não: atendido |
| Alinhamento problema–objetivos–hipótese–conclusão | Cartão n.º 1, foco (2) | PARTLY_MEETS | S1; W1; W2; W9 | Nível alinhado; ênfase final no prazo sem hipótese nem argumento completo | Depende de como o prazo surgiu (Pergunta 1) | Sim: W1 e W2 são reparáveis com reescrita |
| Conclusão sem prometer além do método | Cartão n.º 1, atenção especial | PARTLY_MEETS | S1; S2; W1; W4; W5 | Resposta ao problema correta; afirmações de síntese pontualmente maiores que as tabelas | Nenhuma relevante | Sim: reparável com reescrita |
| Fundamentação teórica da hipótese | Expectativa usual de banca | PARTLY_MEETS | W3; W8; W12 | SEW apoiado em fonte indireta; teorias clássicas sem citação | Literatura internacional é ponto cego declarado | Sim: reparável |
| Transparência e honestidade metodológica | Expectativa usual de banca | EXCEEDS | S2; S4; S5; S6 | Exploratório, multiplicidade e sensibilidade declarados | Detalhes estatísticos fora do meu foco | Não: ponto forte |
| Apresentação: quadros, tabelas e figuras | Cartão n.º 1, foco (3) | PARTLY_MEETS | S3; W6; W13 | Quadros e tabelas bons; figuras pendentes; listas faltando | Figuras não avaliáveis no texto extraído | Não sozinho |
| ABNT (NBR 6023, 10520, 14724, 6028) | Cartão n.º 1, foco (3); CLAUDE.md do projeto | PARTLY_MEETS | W13; W14 | Estrutura correta; lacunas pontuais em referências e pré-textuais | Manual da FEA-RP não fornecido | Não sozinho |
| Rigor estatístico | Fora do remit deste assento | NOT_ASSESSED | — | Cabe ao Revisor 1 | — | — |

Explicação da recomendação: os critérios que pesam na decisão e seguem abertos são o alinhamento entre hipótese e conclusão (W1, W2) e a fundamentação teórica (W3). Os três são reparáveis com reescrita, sem novos dados. Os méritos em transparência não compensam numericamente essas lacunas, mas indicam que o trabalho tem base sólida para a revisão.
