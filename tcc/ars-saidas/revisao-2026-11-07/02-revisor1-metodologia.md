# Parecer de revisão por pares: Revisor 1 (Metodologia)

*ARS `academic-paper-reviewer`, modo `full`, Fase 1 (painel). 07/11/2026.*
*`criteria_binding_unavailable`: os critérios da banca não foram fornecidos, e este parecer não afirma aderência a critérios específicos da instituição.*

## Informações do manuscrito
- **Título:** Empresas familiares vs. não familiares: comportamentos de endividamento
- **Tipo:** Trabalho de Conclusão de Curso, Ciências Contábeis, FEA-RP/USP
- **Data da revisão:** 07/11/2026
- **Rodada:** 1.ª revisão
- **Material examinado:** `manuscrito.txt` (texto extraído do PDF), capítulos em `tcc/latex/capitulos/`, tabelas em `tcc/latex/tabelas/`, `tcc/analise/saidas/resultados.md` e `tcc/analise/resultados_c3.py`. Rodei o script uma vez: ele regrava as tabelas sem nenhuma diferença (`git status` limpo). Para algumas verificações (tamanho de efeito, intervalos de confiança, deixar uma empresa de fora, teste de interação, poder), importei as funções do script num arquivo auxiliar fora do repositório, sem alterar nada. **Esses números são cálculos do revisor e o autor deve conferi-los antes de usá-los.**

---

## Informações do revisor

### Papel
Revisor 1 (Metodologia)

### Identidade
Pesquisador em finanças empíricas com formação em econometria e estatística aplicada a dados contábeis, com experiência em amostras pequenas e testes não paramétricos.

### Foco da revisão
(1) Unidade de análise e independência das observações. (2) Adequação e poder dos testes de Welch e Mann-Whitney com 10 × 6 empresas, testes múltiplos e subperíodos definidos depois de ver os dados. (3) Robustez (Cenários 1 e 2, exclusão da Bradsaúde), indicadores com ausências ou valores extremos (Biomm, Alliar) e reprodutibilidade. Atenção especial: as afirmações de "tendência" e o resultado da pandemia são sustentados pelos testes?

---

## Avaliação geral

### Recomendação
- [ ] Aceitar
- [ ] Revisão menor
- [x] **Revisão maior**: não há defeito crítico, e a conclusão central (H1 não confirmada) está bem sustentada. Mas o Resumo e as Considerações Finais leem os resultados com mais força do que os testes permitem, o achado positivo (prazo da dívida) é mais frágil do que o texto diz e falta reportar a magnitude e a incerteza das diferenças. Quase tudo se resolve reescrevendo trechos e acrescentando poucas análises que o script já consegue produzir. No padrão de um TCC, é um trabalho defensável que precisa de ajustes substanciais antes da entrega, não de ser refeito.

### Grau de confiança
**4**: o desenho e a estatística estão no centro da minha especialidade. A interpretação contábil de alguns casos (reclassificação de dívida da Alliar, vencimentos da Qualicorp) depende de notas explicativas que não li.

### Status de calibração
`NOT_CALIBRATED`

### Avaliação resumida
O trabalho compara o endividamento de 10 empresas familiares e 6 não familiares do setor de saúde da B3 (2018–2025). A unidade de análise é a média de cada empresa nas oito datas de 31/12, e os testes são o t de Welch e o de Mann-Whitney, aplicados ao período completo, a três subperíodos e a dois critérios alternativos de classificação. O desenho é adequado ao tamanho da amostra. Abandonar o System-GMM foi a decisão correta, e o tratamento de independência, bicaudalidade e resultados nulos é melhor do que o usual em TCCs. O corpo do texto (4.3, 4.5) é cauteloso.

Os problemas aparecem quando o texto resume os resultados. (a) O resultado da pandemia (p = 0,040/0,043) entra no Resumo e nas Considerações Finais como "exceção" significativa, sem a ressalva de que é exploratório. Além disso, ele não sobrevive a uma correção mínima para múltiplos testes, e a diferença entre pandemia e pré-pandemia não foi testada (pelos meus cálculos, ela não é significativa). (b) "Tendência que se acentuou a partir da pandemia" não foi testada e, na dívida onerosa, contradiz a própria Tabela 1. (c) O "resultado mais estável", a Dívida CP / Dívida total, depende de qualquer uma de três empresas não familiares e da escolha das datas de 31/12. (d) Faltam tamanhos de efeito e intervalos de confiança, que mostrariam que o estudo não consegue descartar diferenças grandes. (e) O texto atribui a análise ao Google Planilhas, mas as tabelas saem de um script Python que o texto não menciona, e a planilha original do Cenário 1 traz a classificação do Cenário 2.

---

## Pontos fortes

### S1: Unidade de análise correta e justificada
O autor calcula uma média por empresa e testa com n = 16, em vez de tratar empresas-trimestre como observações independentes. Isso evita a inflação de significância típica de testes sobre dados empilhados, e a justificativa está explícita.
**Evidence Anchor**: text: §3.5(b) "tratá-las como observações distintas superestimaria a significância das diferenças"

### S2: Escolha de método coerente com n = 16 e leitura correta do resultado nulo
O texto explica por que um painel dinâmico com instrumentos internos não é adequado a 16 empresas, usa um teste paramétrico robusto a variâncias desiguais e outro não paramétrico, mantém testes bicaudais com justificativa e interpreta o resultado nulo como ausência de evidência, não como igualdade.
**Evidence Anchor**: text: §3.5(b) "são interpretados como ausência de evidência estatística de diferença, e não como evidência de que os grupos são iguais"

### S3: Transparência sobre a análise exploratória
O texto reconhece que os subperíodos foram definidos durante a análise, reporta os nove testes de subperíodo (inclusive os nulos) e alerta para a multiplicidade de testes. Esse é o comportamento esperado diante de um risco de *HARKing*, e é raro em trabalhos de graduação.
**Evidence Anchor**: text: §3.5(c) "Por ter sido definida durante a análise, essa divisão tem caráter exploratório"

### S4: Robustez reportada mesmo quando enfraquece a hipótese
O texto reporta a inversão de sinal da dívida onerosa nos Cenários 1 e 2, explica por que ela ocorre (RaiaDrogasil, Profarma e Hypera mudam de grupo) e apresenta a Dívida líquida / EBITDA com e sem a Biomm e com medianas.
**Evidence Anchor**: text: §4.4 "Nos Cenários 1 e 2, que exigem participação familiar maior, a diferença na dívida onerosa inverte o sinal"

### S5: Números fiéis à fonte e tabelas regeneráveis
Conferi todos os valores das Tabelas 1 a 4 e os números citados em 4.1–4.4 contra `resultados.md`, e todos coincidem (há uma única divergência de arredondamento, listada em "Questões menores"). Também confirmei as médias da RaiaDrogasil (12,8%) e da Profarma (16,5%) e o percentual de 66% da Lifemed. O script regrava as tabelas sem diferença.
**Evidence Anchor**: dataset: `tcc/analise/resultados_c3.py` + `tcc/latex/tabelas/*.tex`: execução sem diferenças em relação às tabelas versionadas

---

## Fraquezas

### W1: O resultado da pandemia é lido além do que o teste permite (Resumo, Considerações Finais e interpretação de 3.5c/4.5)
**Problem**: Os testes sustentam apenas que, no subperíodo 2020–2021, a Dívida CP / Dívida total das familiares foi menor (p = 0,040 e 0,043). O texto, porém: (i) apresenta esse resultado no Resumo e na conclusão como a "exceção" significativa, sem dizer que é exploratório; (ii) o enquadra como confirmação de uma previsão ("deveria se manifestar com mais clareza") formulada depois de ver os dados; e (iii) compara a significância entre subperíodos ("tornou-se significativa", "a significância se reduziu") como se isso mostrasse uma mudança de comportamento. A diferença entre um resultado significativo e um não significativo não é, por si, significativa. Nos dados, a distância no pós-pandemia é maior (18,4% × 41,5%, 23 p.p.) que na pandemia (17 p.p.), e o p sobe só porque a variância das não familiares aumenta. Pelos meus cálculos, a variação por empresa entre pré-pandemia e pandemia não difere entre os grupos (Welch p ≈ 0,13; Mann-Whitney p ≈ 0,16). Com correção de Bonferroni ou Holm, mesmo na família mais estreita (Dívida CP nos três subperíodos), o menor p ajustado é ≈ 0,12.
**Evidence Anchor**: text: Resumo "A exceção é a composição da dívida durante a pandemia, quando a menor participação da dívida de curto prazo nas empresas familiares foi significativa ao nível de 5%"
**Why it matters**: O Resumo e as Considerações Finais são o que a banca lê com mais atenção. Do jeito que estão, sugerem um efeito da pandemia que o desenho não identifica.
**Suggestion**: (1) No Resumo e no 2.º parágrafo das Considerações Finais, acrescentar "em análise exploratória, sem correção para múltiplos testes". (2) Em 3.5(c), reescrever a motivação como pergunta exploratória ("examinar se a diferença se altera"), e não como previsão. (3) Em 4.3, trocar a leitura "tornou-se/reduziu-se a significância" por uma comparação direta: testar a diferença entre grupos da variação por empresa (pandemia − pré e pós − pré), que é um teste simples de interação e cabe no script, e reportar que essa variação não é significativa. (4) Reportar a diferença com intervalo de confiança (ver W4).
**Severity**: Major
**Confidence**: 5, especialidade central: inferência em amostras pequenas e testes múltiplos

### W2: Afirmações de "tendência" não testadas e, na dívida onerosa, contrariadas pela Tabela 1
**Problem**: As Considerações Finais dizem que a menor dívida onerosa e a menor dívida de curto prazo das familiares formam uma "tendência que se acentuou a partir da pandemia". Nenhum teste avalia tendência ou mudança ao longo do tempo. Na Dívida bruta / Ativo, a Tabela 1 mostra o contrário a partir de 2023: a distância sobe de 0,9 p.p. (2020) para 9,4 e 11,2 p.p. (2021–2022) e cai para 0,5 p.p. em 2025 ("até quase desaparecer", nas palavras de 4.1). O salto de 2021 nas não familiares vem quase todo de duas empresas: Qualicorp, de 30,7% para 50,6%, e Fleury, de 34,5% para 48,5%. Com 6 empresas, um evento de uma única empresa desloca a média do grupo em 2–3 p.p. Também "em todos os exercícios" (8 de 8) não é evidência independente: são as mesmas empresas, com indicadores muito persistentes, e em 2025 a diferença é de 0,5 p.p.
**Evidence Anchor**: text: Cap. 5, 2.º parágrafo "menor concentração de dívida no curto prazo que as não familiares, tendência que se acentuou a partir da pandemia"
**Why it matters**: É justamente o tipo de leitura descritiva que o texto se propõe a evitar. A banca pode tomá-la como resultado.
**Suggestion**: Substituir por uma descrição limitada ao que os dados mostram, por exemplo: "a distância na dívida onerosa aumentou em 2021–2022 e praticamente desapareceu em 2025; a distância na dívida de curto prazo ficou maior a partir de 2021; nenhuma dessas variações foi testada estatisticamente". Em 4.1, mencionar que a abertura de 2021 reflete principalmente Qualicorp e Fleury. Na nota da coluna "Anos F < NF" (Tabela 2), avisar que a contagem é descritiva e não equivale a oito observações independentes.
**Severity**: Minor
**Confidence**: 5, especialidade central; verificado nos valores por empresa da base

### W3: O "resultado mais consistente" (Dívida CP / Dívida total) é frágil a empresas individuais e à forma de medir
**Problem**: O texto apresenta o prazo da dívida como o resultado "mais estável do trabalho" e "menos sensível". A estabilidade de **sinal** entre cenários existe. A **inferência**, porém, é frágil, e o indicador tem problemas de mensuração não discutidos. Pelos meus cálculos, sobre a base do script:
- Na pandemia (p = 0,040), retirar **qualquer uma** de três das cinco não familiares (Alliar, Lifemed ou Qualicorp) leva o p para 0,10–0,12. É a mesma dependência de uma única empresa que o texto, com razão, aponta na dívida onerosa com a Bradsaúde (4.4), mas aqui ela não é mencionada.
- O indicador anual oscila de forma mecânica: a Qualicorp vai de 100,0% (2018) para 2,6%, 2,4%, 86,2% (2021) e 1,7%, um padrão típico de debêntures com vencimento único que passam para o circulante no último ano. A Alliar chega a 98,9% em 2025, ano de PL negativo, o que sugere reclassificação de dívida de longo prazo para o curto prazo por descumprimento de *covenant* (a confirmar nas notas explicativas). Nesses casos, uma dívida de curto prazo alta é **consequência** de vencimento ou de dificuldade financeira, e não **escolha** de prazo, que é o que a interpretação de Diamond (1991) pressupõe.
- Usar as 29 datas trimestrais em vez das 8 datas de 31/12 leva o p do período completo de 0,112/0,058 para ≈ 0,15/0,20.
- A favor do autor: retirar o subsetor de Comércio e Distribuição (só familiares) **fortalece** a diferença (Mann-Whitney p ≈ 0,035), o que afasta essa explicação alternativa e vale a pena reportar.
**Evidence Anchor**: text: Cap. 5, 3.º parágrafo "manteve a direção nos três critérios de classificação, o que a torna o resultado mais estável do trabalho"
**Why it matters**: É a única contribuição positiva do trabalho e o eixo das Considerações Finais e das sugestões de pesquisa. Se ela depende de eventos de vencimento de duas ou três empresas, a leitura "as famílias preferem dívida mais longa" fica sem sustentação.
**Suggestion**: (1) Acrescentar à robustez a retirada de uma empresa por vez (*leave-one-out*) para a Dívida CP / Dívida total, no período completo e na pandemia, e reportar o intervalo de p-valores. (2) Reportar a versão com as 29 datas, ou a mediana por empresa, como sensibilidade à mensuração. (3) Conferir nas notas explicativas da Alliar (2025) e da Qualicorp (2018, 2021) se houve reclassificação ou vencimento único e, se houve, discutir. (4) Reportar a robustez sem Comércio e Distribuição. (5) Trocar "mais estável" por "o único cujo sinal se manteve em todas as especificações, com significância frágil".
**Severity**: Major
**Confidence**: 4, especialidade central na estatística; a interpretação contábil dos casos individuais depende de notas que não li

### W4: Faltam tamanhos de efeito, intervalos de confiança e uma discussão quantitativa do poder
**Problem**: As tabelas reportam médias e p-valores, mas não a estatística t, os graus de liberdade, a diferença com IC 95% nem um tamanho de efeito. Pelos meus cálculos: na Dívida bruta / Ativo, a diferença é de −4,5 p.p., com IC 95% (Welch) de aproximadamente [−21; +12] p.p. e g de Hedges ≈ −0,3. Na Dívida CP / Dívida total, a diferença é de −17,8 p.p., IC ≈ [−42; +6], g ≈ −1,3, delta de Cliff ≈ −0,64, com gl de Welch ≈ 4,8. Com 10 × 6 empresas e α = 5%, o poder para d = 0,8 é de cerca de 30%, e só se chega a 80% de poder com d ≈ 1,5. O texto diz que o número de empresas "limita o poder", mas não quantifica.
**Evidence Anchor**: table: Tabela 2 (e Tabelas 3 e 4): apenas F, NF, n, p (t), p (MW); sem diferença, IC, estatística de teste ou tamanho de efeito
**Why it matters**: Sem o IC, o leitor não vê que o resultado nulo da dívida onerosa é compatível tanto com familiares 20 p.p. menos endividadas quanto com 12 p.p. mais endividadas. Ou seja, o estudo é **pouco informativo**, e não um "resultado nulo" no sentido forte usado nas Considerações Finais ("O resultado nulo no nível de endividamento [...] é coerente com a literatura"). O tamanho de efeito também mostra que a Dívida CP tem diferença grande (g ≈ −1,3), mas estimada com imprecisão.
**Suggestion**: Acrescentar às Tabelas 2–4 uma coluna "Diferença (IC 95%)" e uma de tamanho de efeito (g de Hedges ou delta de Cliff, coerente com o Mann-Whitney). Em 3.5(b), incluir uma frase sobre o efeito mínimo detectável (d ≈ 1,5 para 80% de poder). Nas Considerações Finais, trocar "resultado nulo" por "ausência de evidência, com estimativas imprecisas".
**Severity**: Major
**Confidence**: 5, especialidade central

### W5: A procedência dos resultados descrita no texto não confere com o material que a banca recebe
**Problem**: O texto diz que a análise foi feita no Google Planilhas e que a planilha "com [...] todas as fórmulas" acompanha o trabalho. As tabelas do Capítulo 4, porém, são geradas por `tcc/analise/resultados_c3.py`, que o manuscrito não menciona. O próprio script registra que "O arquivo 'Cenário 1' está com a classificação do C2 (erro 1)" e por isso fixa no código as listas dos Cenários 1 e 2. Conferi: `TCC Atual - Cenário 1.xlsx` classifica 7 empresas como familiares (BALM, BLAU, DASA, HAPV, OFSA, PNVL, RDOR), enquanto o Quadro 3 e a Tabela 4 trazem 5 × 11 no Cenário 1. Na cópia "(corrigido)", não consegui ler a coluna de classificação como valor (provavelmente são fórmulas sem valor em cache), e por isso não verifiquei se ela confere.
**Evidence Anchor**: text: §3.5 "A análise foi realizada em quatro etapas, com uso do Google Planilhas. A planilha de apoio, com a base de dados, a classificação das empresas e todas as fórmulas, acompanha este trabalho"
**Why it matters**: A banca avalia o texto e pode conferir a planilha. Se a planilha do Cenário 1 tiver outra classificação, a robustez "inverte o sinal" (usada na Discussão e nas Considerações Finais) não pode ser reproduzida a partir dela.
**Suggestion**: (1) Em 3.5, dizer qual ferramenta gerou os números das tabelas (por exemplo: "os testes foram calculados na planilha e conferidos por um script em Python que lê a mesma base") e disponibilizar o script com a planilha. (2) Garantir que a planilha entregue tenha, em cada cenário, exatamente a classificação do Quadro 3. Isso resolve também o [VERIFICAR] sobre a forma de disponibilização. (3) Se as fórmulas de Mann-Whitney e Welch da planilha não reproduzirem os p do script, dizer qual é a versão oficial.
**Severity**: Major
**Confidence**: 4, verificado no script e nas planilhas; não abri todas as abas de fórmulas

### W6: Multiplicidade de testes sem quantificação, e uma afirmação factual incorreta sobre ela
**Problem**: O manuscrito reporta cerca de 40 p-valores distintos (Tabela 2: 10; Tabela 3: 18; Tabela 4: 18 novos; mais o teste sem a Biomm). Sob a hipótese nula global, seriam esperados cerca de 2 resultados a 5% por acaso, e foram observados 2 casos distintos (a pandemia, com dois testes sobre a mesma comparação, e o Welch sem a Bradsaúde). O texto alerta para a multiplicidade (S3), mas em 4.3 afirma que o resultado da pandemia é o único significativo a 5%, o que é falso: a Tabela 4 traz p = 0,027** (Dívida bruta / Ativo sem a Bradsaúde).
**Evidence Anchor**: text: §4.3 "o resultado da pandemia é o único significativo a 5% entre os testes realizados"
**Why it matters**: A frase contradiz uma tabela do próprio trabalho, e a banca pode notar. Quantificar a multiplicidade torna a cautela verificável, e não apenas declarada.
**Suggestion**: Corrigir para "um dos dois resultados significativos a 5%, ambos em análises complementares (subperíodo exploratório e exclusão da Bradsaúde)". Acrescentar uma frase com o número de testes e o p ajustado por Holm do resultado da pandemia dentro da sua família (ver W1).
**Severity**: Minor
**Confidence**: 5, contagem feita nas tabelas do manuscrito

### W7: A robustez de "exclusão da Bradsaúde" é assimétrica e não foi complementada por uma análise de influência
**Problem**: A Bradsaúde foi escolhida para exclusão porque seus zeros "reduzem a média das não familiares", ou seja, por um critério ligado ao sentido do efeito. Uma dívida nula é uma decisão de financiamento legítima (conservadora), e não um erro de dado. Pelos meus cálculos, ao retirar uma empresa por vez, a Bradsaúde é de fato a única cuja saída torna a dívida onerosa significativa. Isso reforça a conclusão do autor, mas precisa ser mostrado. Além disso, a frase "sem ela, passa a ser" exagera: o Mann-Whitney continua só a 10% (0,058).
**Evidence Anchor**: text: §4.4 "com ela, a diferença não é significativa; sem ela, passa a ser"
**Why it matters**: Uma exclusão escolhida pela direção do efeito pode parecer busca de significância, mesmo quando o texto conclui com cautela.
**Suggestion**: Substituir ou complementar por uma retirada de uma empresa por vez, em todas as 16, apresentada em nota ou apêndice. Reescrever: "sem ela, a diferença é significativa a 5% no teste t e a 10% no Mann-Whitney". Em 3.5(d), justificar a exclusão como análise de influência, não pelo efeito sobre a média.
**Severity**: Minor
**Confidence**: 5, especialidade central

### W8: Um indicador limitado a 100% assume valor impossível (Alliar, 2025) e entra na Tabela 2 sem ressalva
**Problem**: O texto trata como secundários os indicadores sobre o PL por serem instáveis com PL negativo (Alliar, 2025). Mas a Dívida bruta / (Dívida bruta + PL), que também depende do PL e é "complementar", vale 245,2% para a Alliar em 2025 (pelos dados da base) e entra na média do período completo (37,2% × 43,5%). Só esse ano eleva a média da Alliar de cerca de 41% para cerca de 67%.
**Evidence Anchor**: table: Tabela 2, linha "Dívida bruta / (Dívida bruta + PL)": 37,2% × 43,5%, p = 0,563/0,255, sem nota sobre a Alliar
**Why it matters**: Uma proporção acima de 100% não tem a interpretação de "proporção de dívida no capital investido" (Quadro 4). O efeito sobre a conclusão é pequeno (o teste já não é significativo), mas é uma inconsistência de tratamento.
**Suggestion**: Aplicar ao indicador a mesma regra dos indicadores sobre o PL: excluir a Alliar em 2025, ou limitar o valor a 100%, ou reclassificá-lo como secundário. De qualquer forma, registrar na nota da Tabela 2.
**Severity**: Minor
**Confidence**: 4, valor lido na base usada pelo script

### W9: p do Mann-Whitney por aproximação normal com n = 10 × 5–6
**Problem**: Com grupos tão pequenos, o p exato está disponível e é o padrão. O script já o calcula: 0,055 em vez de 0,058 no período completo; 0,040 em vez de 0,043 na pandemia; 0,099 em vez de 0,098 no pós-pandemia. Nenhuma conclusão muda de nível de significância.
**Evidence Anchor**: text: §3.5(b) "O p-valor foi obtido pela aproximação normal com correção de continuidade"
**Why it matters**: Um avaliador com formação estatística vai perguntar por que se usou a aproximação quando o exato é viável. Usar o exato também resolve o [DECIDIR] desse ponto.
**Suggestion**: Adotar o p exato (o script já tem `p_mw_exato`) e regerar as tabelas, ou manter a aproximação e dizer em nota que o p exato não altera nenhuma conclusão.
**Severity**: Minor
**Confidence**: 5, especialidade central

### W10: Seleção da amostra por painel completo e classificação fixa com base no Formulário de Referência mais recente
**Problem**: (i) O texto exclui 6 das 22 empresas (27%) por não terem dados em todo o período, entre elas várias familiares (por exemplo, Mater Dei e Pague Menos), embora a média por empresa permita usar períodos incompletos, como já se faz com a HAPV (7 anos) e a Alliar (7 anos na Dívida líquida / EBITDA). (ii) Classificar todas as empresas pela situação atual, em todo o período, gera erro de classificação nos anos anteriores às reorganizações citadas (Hapvida, Rede D'Or, Fleury). Do ponto de vista estatístico, esse erro tende a atenuar as diferenças em direção a zero, o que vale a pena dizer.
**Evidence Anchor**: text: §3.2 "foram mantidas apenas as que possuem informações em todo o intervalo, para que os dois grupos sejam comparados no mesmo período"
**Why it matters**: Ambos afetam a validade externa e a interpretação do resultado nulo, mas não a conclusão central.
**Suggestion**: Reportar, ao menos para o subperíodo 2022–2025, uma sensibilidade com as empresas excluídas. Nas limitações, dizer que a classificação fixa tende a enviesar as diferenças em direção a zero.
**Severity**: Minor
**Confidence**: 4, aplicação de padrões gerais; a classificação em si é tema do Revisor 2

---

## Comentários detalhados

### Pergunta e hipótese
A pergunta é clara e o método consegue respondê-la, no limite descritivo que o próprio texto assume (§3.1). H1 é direcional, e a escolha de testes bicaudais está justificada. Há um descompasso: H1 fala em "alavancagem financeira", e o achado destacado é de **prazo**, que não está na hipótese. O texto deveria tratar o prazo explicitamente como análise complementar, e não como resposta à hipótese.

### Desenho da pesquisa
Comparação transversal de médias por empresa, sem controles. As limitações de confusão por subsetor e tamanho estão reconhecidas (§4.5, Cap. 5). Uma sugestão de baixo custo: comparar apenas dentro do subsetor de Serviços (3 F × 4 NF) é inviável estatisticamente, mas a robustez **sem Comércio e Distribuição** (7 × 6) é viável e informativa (W3).

### Amostra
n = 16 por restrição de método (classificação manual), o que é legítimo. A questão é o poder (W4) e a seleção por painel completo (W10).

### Coleta de dados
Economática, valores consolidados, datas de 31/12 e fluxos dos últimos 12 meses. Tudo bem documentado. O tratamento das ausências (Bradsaúde na Dívida CP, Biomm na Dívida líquida / EBITDA) está explícito. Falta tratar a Alliar na Dívida bruta / (Dívida bruta + PL) (W8).

### Métodos de análise
Welch e Mann-Whitney são adequados. Com gl de Welch entre 4 e 9 e proporções limitadas, o Mann-Whitney deveria ser o teste de referência na Dívida CP. Na Dívida líquida / EBITDA, a média da Biomm com um único ano recebe o mesmo peso de uma média de 8 anos, e a ausência de dados nos anos de EBITDA negativo não é aleatória: são justamente os anos de pior capacidade de pagamento. O texto já relativiza esse indicador, e basta mencionar essa ausência não aleatória numa frase.

### Apresentação dos resultados
Completa e sem sinais de reporte seletivo: os nulos aparecem. Faltam IC e tamanhos de efeito (W4). A frase sobre "único significativo" contradiz a Tabela 4 (W6).

### Reprodutibilidade
Boa do lado do código (S5). Fraca na descrição do texto e na consistência da planilha (W5).

### Falácias metodológicas observadas
- **Diferença entre significativo e não significativo tratada como diferença** (subperíodos, W1).
- **Risco de *HARKing***, mitigado pela declaração de análise exploratória, mas a motivação em 3.5(c) está escrita como previsão (W1).
- **Exclusão escolhida pela direção do efeito** (Bradsaúde, W7), na prática compensada pela conclusão cautelosa.
- **Variável omitida / confusão** (subsetor, tamanho): reconhecida pelo autor. Na Dívida CP, o subsetor parece não explicar o resultado (W3).
- Não encontrei falácia ecológica: a inferência é feita no nível da empresa, que é a unidade de análise.

### Verificação aritmética (registro em prosa, modo padrão)
`no_recomputable_statistics`: o manuscrito não reporta estatísticas de teste nem graus de liberdade (apenas p-valores e médias de razões contínuas), então os procedimentos `p_from_test_statistic`, `grim`, `grimmer` e `n_from_df` não se aplicam. Em substituição, recalculei os resultados a partir da base, com o script do autor, e todos os valores das Tabelas 1–4 conferem (S5).

---

## Perguntas ao autor
1. Nas notas explicativas, a dívida de curto prazo da Alliar em 2025 (98,9%) e da Qualicorp em 2018 e 2021 decorre de vencimento de debêntures ou de reclassificação por descumprimento de *covenant*? Se sim, o indicador ainda mede "preferência por prazo"?
2. Quais números a banca deve considerar oficiais, os da planilha ou os do script? A planilha entregue terá, no Cenário 1, as 5 familiares do Quadro 3?
3. A divisão em subperíodos foi definida antes ou depois de ver as médias anuais da Tabela 1? (Isso define como redigir 3.5c.)
4. Por que usar as 8 datas de 31/12 em vez das 29 datas trimestrais na média por empresa, se as 29 já estão na base? (Na Dívida CP, a escolha muda o p de forma relevante.)

---

## Questões menores
- §4.4: "30,9% contra 26,4% no Cenário 1", mas a Tabela 4 traz 26,3% (valor 26,35, arredondado de forma diferente). Uniformizar.
- §4.2: "as medianas dos grupos são 1,6x e 2,6x". Deixar claro que são medianas **com** a Biomm.
- Tabelas 3 e 4: indicar o n de cada linha também na Tabela 3 (na Dívida CP é 10 × 5).
- Nota das Tabelas 2–4: dizer quantos anos entram na média de cada empresa com dados incompletos (HAPV 7 na Dívida CP; Alliar 7 e Biomm 1 na Dívida líquida / EBITDA). Essa informação está em `resultados.md`, mas não no texto.
- Figuras 1 e 2: o [VERIFICAR] já prevê o gráfico da Dívida CP. Ele é importante, porque é o achado principal.

---

## Julgamentos por critério

Status de calibração: `NOT_CALIBRATED`. Fonte dos critérios: cartão de configuração n.º 2 (foco do Revisor 1) e `references/statistical_reporting_standards.md`. Os critérios da banca não estão disponíveis (`criteria_binding_unavailable`).

| Dimensão | Fonte do critério | Julgamento | Âncoras | Justificativa | Incerteza / limite de escopo | Pesa na decisão? |
|---|---|---|---|---|---|---|
| Originalidade | — | NOT_ASSESSED | — | Fora do escopo do Revisor 1 | — | não |
| Rigor metodológico | Cartão n.º 2, itens 1–2 | PARTLY_MEETS | S1, S2, W1, W3 | Unidade de análise e escolha dos testes corretas; leitura dos subperíodos e fragilidade da Dívida CP não tratadas | Cálculos do revisor a conferir | sim: W1 e W3 exigem reescrita e duas análises curtas |
| Suficiência da evidência | Cartão n.º 2, item 3 | PARTLY_MEETS | S4, W3, W7 | Robustez boa na dívida onerosa; ausente para o achado positivo | Notas explicativas não lidas | sim |
| Reporte estatístico | statistical_reporting_standards.md | PARTLY_MEETS | W4, W6, W9 | p-valores corretos e fiéis; sem IC, sem tamanho de efeito, sem quantificação da multiplicidade | nenhuma identificada | sim (W4) |
| Coerência do argumento (resultados → conclusão) | Cartão n.º 2, "vai se importar com" | PARTLY_MEETS | W1, W2 | O corpo do texto é cauteloso; o Resumo e o Cap. 5 vão além dos testes | — | sim |
| Reprodutibilidade | Cartão n.º 2, item 3 | PARTLY_MEETS | S5, W5 | O script reproduz tudo; o texto e a planilha não conferem com ele | Coluna de classificação da cópia corrigida não lida | sim (W5) |
| Qualidade da escrita | — | NOT_ASSESSED | — | Fora do escopo | — | não |
| Integração da literatura | — | NOT_ASSESSED | — | Revisor 2 | — | não |
| Relevância e impacto | — | NOT_ASSESSED | — | Revisor 3 | — | não |

**Justificativa da recomendação.** Os critérios que pesam na decisão e ainda não estão resolvidos são o rigor (W1, W3), o reporte (W4), a coerência entre resultados e conclusões (W1, W2) e a reprodutibilidade (W5). Todos podem ser corrigidos sem nova coleta de dados: basta reescrever o Resumo, 3.5(c), 4.3 e o Cap. 5, acrescentar ao script IC, tamanho de efeito, retirada de uma empresa por vez e o teste de variação por empresa entre subperíodos, e alinhar a planilha à descrição. A conclusão central, de que H1 não pode ser confirmada, já está correta e bem defendida. Por isso, recomendo **revisão maior** (substancial, mas sem refazer a pesquisa), e não rejeição.

*Lembrete de integridade: este parecer é uma simulação de banca feita por IA. O texto e as decisões são do autor, que deve conferir as regras da FEA-RP/USP sobre o uso de IA e declarar esse uso se for exigido (`/ars-disclosure`).*
