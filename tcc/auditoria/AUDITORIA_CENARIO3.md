# Auditoria da planilha `TCC Atual - Cenário 3.xlsx`

> **Atualização 07/11/2026:** as correções da seção 4 foram aplicadas nos três cenários. Ver `ROTEIRO_CORRECAO_PLANILHAS.md`.

*Feita em 06/11/2026. Todos os números foram recalculados de forma independente, a partir da aba-base
`Saúde - 1218 à 1225`, com o script `recalculo_c3.py`, e comparados com os valores salvos na
planilha e com o `CONTEXTO_TCC.md`.*

---

## 1. Resultado geral

| O que foi conferido | Situação |
|---|---|
| Classificação na base (coluna B) | ✅ 10 Familiares × 6 Não Familiares, igual à tabela 4.2 do contexto |
| Base sem linhas duplicadas (empresa × indicador) | ✅ |
| Fórmulas de valor por empresa (`MÉDIASES` por coluna de data) | ✅ apontam para as colunas certas (conferi as 16 × 29 células de uma aba inteira) |
| Faixas dos testes (familiares em cima, linhas 36–45 × 46–51; 20–29 × 30–35) | ✅ corretas no C3 |
| Médias e p-valores do teste t (tabelas 7.1 e 7.2 do contexto) | ✅ conferem |
| p-valores de Mann-Whitney na tabela 7.1 | ⚠️ **3 de 6 estão errados** (vieram de dados trimestrais), ver item 3 |
| Aba `Div Liq x Pl` | ❌ **erro novo**: a média da empresa usa só 2021–2023 |
| Erros 3, 4, 5 e 8 da lista do contexto | ❌ confirmados |

**Conclusões do TCC: nenhuma muda.** A leitura do item 7.4 do contexto continua valendo. O que muda são
alguns p-valores que iriam para as tabelas, além da rastreabilidade (de onde cada número sai).

---

## 2. Erros encontrados (em ordem de prioridade)

### E1 (novo, ALTO). `Div Liq x Pl`: a média da empresa cobre o período errado
- `AF36:AF51` = `=SEERRO(MÉDIA(L36:W36);"")` → usa só os trimestres de **03/2021 a 12/2023**.
  Nas outras abas é `C36:AE36` (período completo).
- Consequência: a aba mostra Mann-Whitney **p = 0,093 ("Significativo a 10%")** e t p = 0,256.
  Com o período completo, os valores certos são t p = 0,763 e MW p = 0,481 (trimestral), ou t p = 0,855 e
  MW p = 0,625 (anual). **Não há nada significativo nesse indicador.**
- Correção: em `AF36`, digite `=SEERRO(MÉDIA(C36:AE36);"")` e arraste até `AF51`.

### E2 (ALTO). As abas de indicador testam com trimestres, não com dados anuais (erro 3 do contexto, ampliado)
- `D55` ("observações empresa-ano") usa as 29 colunas trimestrais × 16 empresas (~460 observações). Na aba
  `Div Bruta x Atv t`, ela mostra **p = 0,002 ("Significativo a 5%")**. Esse número **não pode ir para o TCC**.
- `D54` e o Mann-Whitney (`D58:D63`) usam a **média dos 29 trimestres** (`AF`), enquanto a aba `Análises`
  usa a **média dos 8 fechamentos de 31/12** (`M`). Isso dá dois "testes principais" diferentes para o mesmo
  indicador (Dívida bruta/Ativo: 0,564 na aba do indicador × 0,556 em `Análises`). Pela regra 6 do contexto,
  vale o anual.
- `Análises!D39` (empresa-ano, 8 × 16 = 128 observações) tem o mesmo problema de não independência, em grau
  menor. Não use para inferência.
- Correção: ver seção 4, passos 2 e 3.

### E3 (MÉDIO). A tabela 7.1 do contexto mistura duas fontes no Mann-Whitney
O teste t de todas as linhas é anual, mas o MW de três linhas foi copiado das abas trimestrais:

| Indicador | MW no contexto | MW anual correto (fórmula da planilha) | MW anual exato |
|---|---|---|---|
| Exigível / Ativo | 0,871 | **0,957** | 0,958 |
| D/(D+PL) | 0,357 | **0,255** | 0,263 |
| Dívida líquida / EBITDA | 0,481 | **0,416** | 0,428 |

### E4 (MÉDIO). Dois cálculos diferentes de Mann-Whitney
A planilha usa a **aproximação normal com correção de continuidade**. Parte dos números do contexto
(0,040 na pandemia, 0,055 na Dív CP) é o **p exato**, calculado em Python. Os dois são aceitáveis e nenhuma
conclusão muda, mas o texto precisa usar **um só**, o mesmo que a banca vai encontrar na planilha.
Recomendação: usar o da planilha e dizer na Metodologia "teste U de Mann-Whitney, aproximação normal com
correção de continuidade".

| | Fórmula da planilha | Exato |
|---|---|---|
| Dív CP/Dív total, pandemia 2020–21 | 0,043 | 0,040 |
| Dív CP/Dív total, período completo | 0,058 | 0,055 |
| Dív CP/Dív total, pós 2022–25 | 0,098 | 0,099 |

### E5 (MÉDIO). Dívida líquida / EBITDA da BIOM vem de **um único ano**
A Economática traz "-" quando o EBITDA é negativo (BIOM de 2018 a 2024). A "média 2018–2025" da BIOM é só o
valor de 2025 (**16,1x**), e é ela que puxa a média das não familiares para **4,4x**. Sem a BIOM, essa média
é **2,0x**; as medianas são 1,6x (F) × 2,6x (NF). No texto, diga isso explicitamente e prefira apresentar a
mediana ou tratar a BIOM como "não aplicável" nesse indicador. Não apresente "1,4x × 4,4x" como contraste.
A AALR também não tem 2025 nesse indicador (7 anos).

### E6 (MÉDIO, erro 4 do contexto). Subsetor errado na aba `Classificação`
BLAU, HYPE e EUFA estão no **subsetor** (coluna C) "Comércio e Distribuição"; o certo é "Medicamentos e
Outros Produtos". A coluna D (segmento) está certa. **Atenção:** se a regressão com dummies de subsetor
(feita em Python) leu essa coluna, ela agrupou BLAU e HYPE com as varejistas. O resultado "−5,9 p.p.,
p = 0,37" precisa ser refeito antes de ir para o texto.

### E7 (BAIXO, erro 5). Rótulo fixo "(10 F × 5 NF)"
Em `Análises!C38` e em `C54` das 7 abas. O certo é 10 × 6 (e 10 × 5 na Dív CP/Dív total, porque a SAUD não
tem dívida). Use rótulo dinâmico (seção 4, passo 4).

### E8 (BAIXO, erro 8). `Metodologias!A11` cita "C37/C38"
As células reais são `Análises!D38` (principal) e `D39`. Corrija o texto.

### E9 (BAIXO, rastreabilidade). Os resultados do TCC não estão fixados em nenhuma aba
`Análises` mostra **um indicador por vez** (seletor `B1`), e a Dívida CP/Dívida total não tem aba própria.
Os subperíodos (pré, pandemia, pós) não existem na planilha: só foram calculados fora dela. Tudo o que
estiver nas tabelas do TCC precisa ser reproduzível na planilha (seção 4, passos 5 e 6).

### Pontos para conferir na fonte (não são erros da planilha)
- **HAPV, Dívida bruta = 0 em 12/2018** (e nos dois primeiros trimestres de 2019). Pode ser real (a Hapvida
  tinha pouca ou nenhuma dívida bancária antes das debêntures), mas confira na DFP de 2018, como no caso SAUD.
- **AALR, PL negativo em 2025**: produz −805% em Exigível/PL e −186% em Dívida bruta/PL. É mais um motivo para
  deixar os indicadores sobre PL como secundários (já é o que o contexto propõe).

---

## 3. Tabelas corrigidas (Cenário 3, dados anuais de 31/12, uma média por empresa)

p(MW) = fórmula da planilha (aproximação normal com correção de continuidade). Entre parênteses, o p exato.

### 3.1 Período completo 2018–2025 (substitui a tabela 7.1)

| Indicador | Familiar | Não fam. | n | Anos F < NF | p (t Welch) | p (MW) |
|---|---|---|---|---|---|---|
| Dívida bruta / Ativo | 26,1% | 30,6% | 10 × 6 | 8 de 8 | 0,556 | 0,255 (0,263) |
| Exigível / Ativo | 55,4% | 56,2% | 10 × 6 | 4 de 8 | 0,885 | 0,957 (0,958) |
| D/(D+PL) | 37,2% | 43,5% | 10 × 6 | 6 de 8 | 0,563 | 0,255 (0,263) |
| Dívida líquida / EBITDA* | 1,4x | 4,4x | 10 × 6 | 5 de 8 | 0,285 | 0,416 (0,428) |
| Dívida CP / Dívida total | 20,4% | 38,2% | 10 × 5 | 8 de 8 | 0,112 | **0,058** (0,055) |
| Liquidez corrente | 2,18x | 1,48x | 10 × 6 | F maior em 8 de 8 | **0,064** | 0,116 (0,118) |

\* NF sem a BIOM = 2,0x; medianas 1,6x × 2,6x (ver E5).

### 3.2 Subperíodos (confere com a tabela 7.2; só o MW muda na terceira casa)

| Indicador | Período | Familiar | Não fam. | p (t) | p (MW) |
|---|---|---|---|---|---|
| Dívida CP / Dívida total | 2018–2019 | 24,9% | 33,4% | 0,435 | 0,298 (0,310) |
| Dívida CP / Dívida total | **2020–2021** | 19,5% | 36,4% | **0,040** | **0,043** (0,040) |
| Dívida CP / Dívida total | 2022–2025 | 18,4% | 41,5% | 0,130 | **0,098** (0,099) |
| Dívida bruta / Ativo | 2018–2019 | 25,4% | 27,3% | 0,815 | 0,625 |
| Dívida bruta / Ativo | 2020–2021 | 27,8% | 33,0% | 0,543 | 0,255 (0,263) |
| Dívida bruta / Ativo | 2022–2025 | 25,5% | 31,0% | 0,497 | 0,416 |
| Exigível / Ativo | 2020–2021 | 56,8% | 58,1% | 0,825 | 0,871 (0,875) |

### 3.3 Robustez sem a SAUD (não estava no contexto, só a regressão)

| Indicador | Familiar | Não fam. (sem SAUD) | p (t) | p (MW) |
|---|---|---|---|---|
| Dívida bruta / Ativo | 26,1% | 36,7% | **0,027** | **0,058** |
| D/(D+PL) | 37,2% | 52,2% | **0,033** | **0,058** |
| Exigível / Ativo | 55,4% | 59,8% | 0,348 | 0,759 |
| Dívida líquida / EBITDA | 1,4x | 5,4x | 0,219 | 0,126 |

**Como usar no texto:** a exclusão da SAUD já estava prevista como robustez (decisão de 15/10), justificada
por ser a única empresa **sem nenhuma dívida financeira**. Então é legítimo reportar o resultado, mas
**como robustez, ao lado da amostra principal**, e não como resultado principal. A frase honesta é: "na
amostra completa a diferença não é significativa; excluindo a única empresa sem dívida financeira, a
diferença na dívida onerosa passa a ser significativa a 5% (t) e a 10% (MW), o que indica que o resultado
é sensível a uma única observação". Ou seja, isso **reforça** a cautela, não a substitui.

---

## 4. Roteiro de correção no Google Planilhas (locale pt-BR)

**Antes de tudo:** Arquivo > Fazer uma cópia (guarde a versão de hoje).

1. **E1, aba `Div Liq x Pl`:** em `AF36`, `=SEERRO(MÉDIA(C36:AE36);"")` e arraste até `AF51`.

2. **E2, testes anuais nas 7 abas de indicador.** As colunas de 31/12 nessas abas são
   C, G, K, O, S, W, AA, AE. Em cada aba:
   - `AH35` = `Média anual (31/12)` e `AI35` = `Posto anual`
   - `AH36`: `=SEERRO(MÉDIA(C36;G36;K36;O36;S36;W36;AA36;AE36);"")`, arrastar até `AH51`
   - `AI36`: `=SE(AH36="";"";RANK.AVG(AH36;$AH$36:$AH$51;1))`, arrastar até `AI51`
   - `D54`: `=T.TEST(AH36:AH45;AH46:AH51;2;3)`
   - `D58`: `=CONT.NÚM(AH36:AH45)` · `D59`: `=CONT.NÚM(AH46:AH51)` · `D60`: `=SOMA(AI36:AI45)`
   - Assim, `D54` e `D63` passam a bater com a aba `Análises` (Dívida bruta/Ativo: 0,556 e 0,255).
   - Mantenha as colunas `AF`/`AG` (médias trimestrais) só para os gráficos, ou apague-as.

3. **E2, remover a pseudo-replicação:** apague as linhas 55 (abas de indicador) e 39 (`Análises`). Se quiser
   mantê-las, renomeie para "complementar – não usar para inferência (observações não independentes)".

4. **E7, rótulos dinâmicos:**
   - `Análises!C38`: `="p-valor – médias por empresa ("&D42&" F × "&D43&" NF)"`
   - `C54` de cada aba: `="p-valor – médias anuais por empresa ("&D58&" F × "&D59&" NF)"`

5. **E9, subperíodos na aba `Análises`** (colunas E…L = 2018…2025):
   - `O19` Pré (2018–19) · `P19` Pandemia (2020–21) · `Q19` Pós (2022–25)
   - `O20`: `=SEERRO(MÉDIA(E20:F20);"")` · `P20`: `=SEERRO(MÉDIA(G20:H20);"")` · `Q20`: `=SEERRO(MÉDIA(I20:L20);"")`, arrastar até a linha 35
   - Postos: `R20`: `=SE(O20="";"";RANK.AVG(O20;O$20:O$35;1))`, arrastar para S e T e até a linha 35
   - Teste t do subperíodo (ex.: pandemia): `=T.TEST(P20:P29;P30:P35;2;3)`
   - MW do subperíodo: repita o bloco D42:D47 trocando `M`/`N` pelas colunas do subperíodo (ex.: `P`/`S`)
   - Confira: com `B1` = `Divida CP / Divida Tt %`, a pandemia deve dar t = 0,040 e MW = 0,043.

6. **E9, aba nova `Resultados`:** para cada indicador, troque `B1` em `Análises` e copie os resultados com
   *Colar especial > Somente valores* para uma tabela fixa (indicador × período: médias, n, p t, p MW). Anote
   no topo: "valores copiados de Análises com B1 = <indicador> em <data>". Essa tabela é a fonte das tabelas
   do TCC.

7. **E6:** em `Classificação`, coluna C, troque BLAU, HYPE e EUFA para `Medicamentos e Outros Produtos`.

8. **E8:** em `Metodologias!A11`, troque "C37 (principal)" por "Análises!D38 (principal)" e "C38" por
   "Análises!D39".

Depois de corrigir, baixe o .xlsx (Arquivo > Fazer download > Microsoft Excel) e me envie. Eu rodo o
`recalculo_c3.py` de novo para confirmar que tudo bate.

---

## 5. Decisões que são suas (e da Maisa)

1. **Qual p-valor de Mann-Whitney reportar**: o da planilha (recomendado, rastreável) ou o exato.
2. **Dívida líquida / EBITDA**: reportar com a média e uma nota, trocar pela mediana ou excluir a BIOM
   desse indicador. A escolha precisa valer igualmente para os dois grupos e ser declarada.
3. **Regressão exploratória**: refazer com o subsetor corrigido e um script em R, ou tirá-la do TCC e citar
   só os testes.
