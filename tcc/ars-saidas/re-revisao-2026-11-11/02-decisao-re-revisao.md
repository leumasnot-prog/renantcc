# Re-revisão — Fase 2B e decisão

Data: 11/11/2026. Compara a carta do autor (`revisao-2026-11-07/07-triagem-e-resposta.md`) com o veredito cego congelado (`01-verificacao-cega.md`) e confere, no LaTeX atual (`04-resultados.tex`, `05-consideracoes.tex`, alterações ainda não commitadas), os problemas novos N1, N2, N3, N5 e N8.

## 1. Carta × veredito cego

### 1.1 Alegações exageradas (carta "T", evidência PARCIAL ou NÃO RESOLVIDO)

| Item | Carta | Cego | Divergência |
|---|---|---|---|
| RR-02 | T | PARCIAL | A frase "especialmente associada às dívidas de longo prazo [...] cláusulas mais rigorosas" (§2.2) segue sem citação, e a Introdução repete. |
| RR-06 | T | PARCIAL | O Cap. 5 não diz que a variação não foi testada. A recusa de atribuir 2021 a Qualicorp/Fleury ("cálculo do revisor, não conferido") é aceitável. Na prática, é TP. |
| RR-09 | T | PARCIAL | Quando a carta foi escrita, a §4.5 ainda trazia "dependeu da presença". **Corrigido depois** (ver N2): agora está resolvido. |
| RR-23 | T | PARCIAL | A §4.3 ainda falava em "tornou-se significativa" e "se reduziu". O LaTeX atual declara que a comparação é descritiva, mas vale conferir as duas expressões. |
| RR-30 | T | PARCIAL | Falta a frase sobre o efeito mínimo detectável (poder). |
| RR-31 | T | PARCIAL | A frase "planilha e script produzem os mesmos resultados" não está demonstrada: a planilha do C1 só foi corrigida numa cópia (N6). |
| RR-41 | T | PARCIAL | O Exigível ponderado faltava. Foi incluído depois (N8), mas com erro de redação. |
| RR-03, 04, 37 | T / A | PARCIAL / condicionado | O "T" vale só para a escrita: o conteúdo depende de fontes ainda não lidas. RR-04 também não liga Myers/Majluf ao parágrafo da diluição. |

Coincidem com o veredito cego: RR-01, 05, 07, 08, 10–13, 15, 25, 29, 38, 45, 46, 47. Os itens TP (14, 22, 24, 36, 39, 44) e L (27, 34, 35, 42, 43) estão descritos com honestidade.

### 1.2 Recusas ("N")

| Item | Motivo do autor | Decisão |
|---|---|---|
| RR-17 | Os exemplos ficam na §2.1 porque a orientadora pediu "Exemplos" ali | **Aceita.** É uma instrução da orientadora. |
| RR-21 | O título depende da orientadora | **Aceita.** |
| RR-26 | As datas trimestrais contrariam a regra de testar só com dados anuais | **Aceita.** Pode virar uma linha de limitação. |
| RR-32 | Efeito baixo; já há nota no Apêndice B | **Aceita em parte.** Não precisa de reanálise, mas a nota da Tabela 2 deve dizer como a Alliar 2025 (PL negativo) entra na Dívida/(Dívida+PL). É uma frase. |

Itens L (RR-27, 34, 35, 42, 43): para uma banca de TCC, registrar o ponto como limitação é aceitável, exceto no RR-34, cuja limitação tinha uma contradição factual (N1).

## 2. Itens "A": pendências do autor, não falhas

RR-03, 04, 37 (ler Gómez-Mejía 2007, Berrone 2012, Myers 1984, Myers e Majluf 1984, González 2013); RR-14 (quadro dos estudos empíricos, Wildner 2020); RR-16 (dados de Pestana et al., edição da EY, "Acesso em:"); RR-18 (marcadores \verificar); RR-19/40 (conferir o Quadro 5 no FRE e o tipo de controlador das não familiares; inclui N7); RR-20 (gráficos); RR-35 (FREs de 2018/2019); RR-42 (datas dos eventos em fato relevante); RR-43 (definição da Economática). Também Diamond (1991), Kayo et al. (2018) e Poletti-Hughes/Martínez García.

## 3. Problemas novos após os ajustes posteriores

| N | Situação no LaTeX atual | Veredito |
|---|---|---|
| N1 (IPOs) | Cap. 5 agora diz "excluiu as empresas sem informações na base desde 2018, em geral as que abriram capital mais tarde", o que deixa de contradizer a presença de Blau e Rede D'Or. Mas não explica por que as duas têm dados desde 2018. | **PARCIAL.** Falta uma frase na §3.2. |
| N2 (Bradsaúde) | "dependeu da presença" não aparece mais. A §4.4 e a §4.5 dizem "depende da exclusão" / "da composição da amostra". | **RESOLVIDO** |
| N3 (tamanho) | A §4.4 agora traz "embora a diferença de tamanho não seja estatisticamente significativa (p = 0,120; 0,212)". A frase sobre debêntures recebeu \verificar (Barclay e Smith, 1995), e a de Diamond também. Mas a §4.5 ("as familiares da amostra são maiores") e o Cap. 5 ("são, em média, maiores") seguem sem a ressalva. | **PARCIAL** |
| N5 (C1 × C2) | "(no Cenário 1, também Hapvida e Dimed/Panvel)" | **RESOLVIDO.** Resta um ajuste de forma: há uma quebra de linha/parágrafo solta antes de "As duas primeiras". |
| N8 (Exigível ponderado) | 58,9% × 60,0% reportado, mas o texto diz que a diferença "se reduz [...] de 0,8 para 1,1 ponto percentual". De 0,8 para 1,1 é aumento. | **PARCIAL.** É um erro de redação: trocar por "e a do Exigível total / Ativo total passa de 0,8 para 1,1 p.p.". Conferir também o sinal da diferença simples. |

N4 (fontes não lidas) continua como pendência do autor. Agora Diamond também tem marcador. N6 (reprodutibilidade) e N7 (percentuais do Quadro 5) seguem abertos.

## 4. Decisão: **REVISÃO MENOR**

A reescrita resolveu o problema central da primeira rodada: o prazo da dívida passou a ser uma questão exploratória, a dependência da Bradsaúde é declarada, os ICs e o ajuste de Holm são reportados e as explicações concorrentes estão no texto. Para uma banca de TCC, o desenho e as conclusões agora são defensáveis e proporcionais à evidência. O que falta não exige nova análise. São (i) correções pontuais de redação e coerência e (ii) a leitura e conferência de fontes e documentos pelo autor. O item (ii) é condição de integridade: o texto não vai à banca com \verificar sobre fontes que sustentam o argumento das "duas forças". Esse volume de pendência não justifica uma revisão maior, mas impede o aceite.

## 5. Pendências antes da entrega

**(a) O assistente pode fazer no texto**
1. N8: corrigir "se reduz de 0,8 para 1,1".
2. N3: ressalva de não significância do tamanho na §4.5 e no Cap. 5.
3. N1: frase na §3.2 explicando por que Blau e Rede D'Or têm dados desde 2018 (depois de o autor confirmar o motivo).
4. N6/RR-31: reformular "produzem os mesmos resultados" como "o script é a versão de referência; a planilha corrigida confere", ou retirar.
5. RR-02: citar ou suavizar a frase sobre as cláusulas da dívida longa; RR-04: ligar Myers e Majluf ao parágrafo da diluição.
6. RR-23: retirar "tornou-se significativa" e "se reduziu" da §4.3; RR-30: frase sobre o poder; RR-06: "não testado" no Cap. 5.
7. RR-32: nota da Tabela 2 sobre a Alliar 2025; RR-16: caixa de "Martínez García"; RR-22: posição do Quadro 3 e n da Tabela 3; quebra solta em N5.
8. Recompilar (`make`) e conferir `grep '^!' build/main.log`.

**(b) Só o autor pode fazer**
1. Ler e conferir Gómez-Mejía (2007), Berrone et al. (2012), González et al. (2013), Myers (1984), Myers e Majluf (1984), Diamond (1991), Kayo et al. (2018), Poletti-Hughes/Martínez García e Barclay e Smith (1995), e resolver todos os \verificar.
2. Conferir o Quadro 5 no FRE (percentuais, DASA/OFSA 56,7%, HAPV, tipo de controlador) e, se possível, os FREs de 2018.
3. Completar as referências (Pestana et al., EY, datas de acesso).
4. Confirmar as datas dos eventos societários em fato relevante e a definição de dívida da Economática.
5. Refazer as Figuras 1–2 (e, opcionalmente, a da Dívida CP).
6. Decidir com a orientadora o título e a ficha/folha de aprovação; declarar o uso de IA conforme as regras da FEA-RP (`/ars-disclosure`).
