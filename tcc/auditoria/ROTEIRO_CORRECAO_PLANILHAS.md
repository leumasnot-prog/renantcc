# Roteiro de correção das planilhas (Cenários 1, 2 e 3)

*07/11/2026. Correções aplicadas pelo script `tcc/auditoria/corrigir_planilhas.py`, que grava cópias
`TCC Atual - Cenário N (corrigido).xlsx` em `tcc/arquivos/` e não altera os originais.*

## Como as correções foram verificadas

As três planilhas corrigidas foram recalculadas no LibreOffice, e cada p-valor foi comparado com o
script independente `tcc/analise/resultados_c3.py`. Os valores comparados foram:

- o teste t (`D54`) e o Mann-Whitney (`D63`) das 7 abas de indicador;
- o teste principal da aba Análises (`D38`/`D47`);
- os testes dos 3 subperíodos.

**Os 3 cenários conferem até a 6.ª casa decimal.** Os rótulos passaram a mostrar o n correto:
5 × 11, 7 × 9 e 10 × 6.

As células com `PROCX` (XLOOKUP), como a coluna B da base e os grupos nas abas, aparecem como `#NAME?`
no LibreOffice desta máquina, que não tem essa função. No Google Planilhas elas funcionam. Por isso,
essas fórmulas foram conferidas de outro jeito:

- cada uma aponta para a coluna certa da aba Classificação (I, J ou K);
- essa coluna, recalculada, dá exatamente as familiares de cada cenário.

## O que foi corrigido

| # | Correção | Onde | Antes → depois |
|---|---|---|---|
| C1 | O Cenário 1 lia a classificação do Cenário 2 (erro 1) | Base `Saúde - 1218 à 1225`, coluna B | `PROCX(...;'Classificação'!J:J)` → `I:I` no arquivo do C1. Familiares do C1: BLAU, DASA, BALM, OFSA, RDOR |
| C2 | A aba Análises do C1 e do C2 mostrava os grupos do C3 (erro 6) | Análises, coluna D (20–35) | `'Classificação'!K:K` → `I:I` (C1) e `J:J` (C2) |
| C3 | O Mann-Whitney e os testes usavam as faixas do C3 (erro 2) | Análises `C20:C35` e abas de indicador `A36:A51` | Empresas reordenadas com as familiares em cima. Faixas: C1 = 5 + 11, C2 = 7 + 9, C3 = 10 + 6 |
| C4 | As abas de indicador testavam com a média dos 29 trimestres (erro 3) | 7 abas de indicador | Nova coluna `AH` (média das 8 datas de 31/12: colunas C, G, K, O, S, W, AA, AE) e `AI` (posto). `D54`, `D58`, `D59` e `D60` passam a usar `AH`/`AI`. Agora as abas batem com a aba Análises |
| C5 | Testes com observações não independentes (erro 3) | `D55` nas abas de indicador; `D39` na aba Análises | Removidos, com uma nota explicando o motivo em `C55`/`C39` |
| C6 | A média da empresa cobria só 2021–2023 (erro novo E1) | `Div Liq x Pl`, `AF36:AF51` | `MÉDIA(L:W)` → `MÉDIA(C:AE)` |
| C7 | Rótulo fixo "(10 F × 5 NF)" (erro 5) | `C54` (abas de indicador) e `Análises!C38` | Rótulo calculado com o n real de cada cenário |
| C8 | Os subperíodos não existiam na planilha | Análises `O19:T35` e bloco `B49:F59` | Médias por empresa pré/pandemia/pós, postos, teste t, Mann-Whitney e texto do resultado. Valem para o indicador escolhido em `B1` |
| C9 | Subsetor errado; PGMN não familiar no C1/C2 (erros 4 e 7) | Classificação | BLAU, HYPE e EUFA → "Medicamentos e Outros Produtos". PGMN → "Familiar" no C1 e no C2 (detalhes abaixo) |
| C10 | Referências de células desatualizadas (erro 8) | Metodologias | O texto cita `Análises!D38` e `D54`/coluna AH. Nos arquivos C1/C2, "(Cenário 3)" → "(Cenário N)" |

**Detalhe da PGMN:** a coluna de cenários da aba Classificação usa `PROC` (LOOKUP) na aba Dados, mas
a PGMN não está na aba Dados. Nesse caso, o `PROC` devolve a linha anterior em ordem alfabética, que é
a da PFRM. Por isso a PGMN aparecia como não familiar no C1 e no C2. Agora o valor está escrito
diretamente. Isso não afeta a amostra principal, porque a PGMN não está na base completa.

## O que NÃO foi alterado (decisões ou conferências suas)

- **Aba Cenários:** DMVF e VVEO continuam "A confirmar". Fica para conferir no FRE; não afetam a base
  completa.
- **Abas `Indicadores por cenário` e `Dados`:** são de 13/10 e estão desatualizadas. Sugiro apagar,
  ou renomear com "(histórico)", antes de enviar à banca.
- **Gráficos:** continuam como estavam (ver abaixo).
- **Aba Análises, colunas M/N (média 2018–2025) e `B4:C11`:** já estavam corretas.

## Como levar as correções para o Google Planilhas

O arquivo exportado do Google traz os gráficos como **imagens fixas**, não como gráficos vivos. Por
isso há dois caminhos:

1. **Importar o arquivo corrigido** (mais rápido): no Drive, *Novo > Upload de arquivo*, depois
   *Abrir com Google Planilhas*. As fórmulas recalculam sozinhas. Os gráficos vêm como imagens e
   precisam ser refeitos, o que já estava previsto: datas em dd/mm/aaaa, eixo em %, e um gráfico novo
   para a Dívida CP / Dívida total.
2. **Corrigir a planilha original no Google** (mantém os gráficos vivos): siga a tabela acima, célula
   por célula. No Google Planilhas em português, as fórmulas ficam:
   - `AH36`: `=SEERRO(MÉDIA(C36;G36;K36;O36;S36;W36;AA36;AE36);"")`
   - `AI36`: `=SE(AH36="";"";RANK.AVG(AH36;$AH$36:$AH$51;1))`
   - `D54` (C3): `=T.TEST(AH36:AH45;AH46:AH51;2;3)`. No C2, use `AH36:AH42;AH43:AH51`. No C1, use
     `AH36:AH40;AH41:AH51`.
   - `D58`/`D59`/`D60`: `=CONT.NÚM(...)` e `=SOMA(AI...)`, nas mesmas faixas.
   - `C54`: `="p-valor – médias anuais por empresa ("&D58&" F × "&D59&" NF)"`
   - Ordem das empresas no C2: BLAU, DASA, BALM, OFSA, RDOR, HAPV, PNVL, depois as demais. No C1:
     BLAU, DASA, BALM, OFSA, RDOR, depois as demais.

## Resultados que mudam com a correção (para conferir o texto)

Antes, os Cenários 1 e 2 usavam a classificação errada. Agora (Dívida bruta / Ativo, médias anuais):

| Cenário | F × NF | p (t) | p (MW) |
|---|---|---|---|
| C1 | 5 × 11 | 0,558 | 0,734 |
| C2 | 7 × 9 | 0,801 | 1,000 |
| C3 | 10 × 6 | 0,556 | 0,255 |

Esses são os mesmos valores da Tabela de robustez do Capítulo 4, que veio do script. O texto do TCC
não muda.

No Cenário 1, a Dívida bruta / Ativo no **pré-pandemia** dá p (MW) = 0,089, significativo a 10%, com
as familiares **mais** endividadas. É um resultado isolado de robustez e vai no sentido contrário ao da
H1. Ele não muda as conclusões, mas fica registrado aqui para que nada seja omitido.
