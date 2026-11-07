# Relatório de análise de campo (Fase 0 – `field_analyst_agent`)

*ARS `academic-paper-reviewer`, modo `full`, 07/11/2026. Manuscrito: `tcc/latex/build/main.pdf`
(texto extraído em `manuscrito.txt`).*

## Dados básicos do trabalho
- **Título:** Empresas familiares vs. não familiares: comportamentos de endividamento
- **Resumo:** cerca de 260 palavras (com Abstract em inglês)
- **Texto completo:** cerca de 9.300 palavras (29 páginas)
- **Referências:** 18
- **Tipo:** Trabalho de Conclusão de Curso, Ciências Contábeis, FEA-RP/USP

## Análise de campo

| Dimensão | Resultado |
|---|---|
| Disciplina principal | Contabilidade e finanças corporativas (estrutura de capital) |
| Disciplinas secundárias | Governança corporativa e empresas familiares; estatística aplicada |
| Paradigma | Quantitativo |
| Tipo de método | Estudo comparativo descritivo, com testes de diferença entre grupos (Welch, Mann-Whitney), subperíodos e robustez |
| Público-alvo | Banca de TCC: a orientadora e dois professores avaliam o texto, sem defesa oral (segundo `CONTEXTO_TCC.md`). Não há periódico-alvo. `criteria_binding_unavailable`: os critérios da banca não foram fornecidos, então o painel não afirma aderência a critérios específicos |
| Maturidade | Versão pré-entrega: estrutura completa (5 capítulos), referências formatadas e marcadores [VERIFICAR]/[DECIDIR] ainda abertos |

## Cartões de configuração dos revisores

### Cartão de configuração n.º 1
**Papel:** EIC · **Nome de exibição:** Revisor de Adequação (banca)
**Identidade:** professor de Contabilidade Financeira de uma faculdade de economia, administração e
contabilidade de universidade pública. Já orientou e avaliou dezenas de TCCs e conhece os critérios
usuais de bancas de graduação (contribuição, coerência entre problema, método e conclusão, e
adequação às normas).
**Foco da revisão:**
1. Se o trabalho tem o escopo e a contribuição esperados de um TCC de graduação.
2. Se problema, objetivos, hipótese, método e conclusão estão alinhados.
3. Apresentação: clareza, ABNT e uso de quadros, tabelas e figuras.

**Vai se importar especialmente com:** se a conclusão responde ao problema formulado na Introdução
sem prometer mais do que o método entrega.
**Possíveis pontos cegos:** detalhes estatísticos finos e literatura internacional recente.

### Cartão de configuração n.º 2
**Papel:** Revisor 1 (metodologia)
**Identidade:** pesquisador em finanças empíricas com formação em econometria e estatística
aplicada a dados contábeis, com experiência em amostras pequenas e testes não paramétricos.
**Foco da revisão:**
1. Unidade de análise e independência das observações (média por empresa, datas de 31/12).
2. Adequação e poder dos testes de Welch e Mann-Whitney com 10 × 6 empresas; testes múltiplos e
   subperíodos definidos depois de ver os dados.
3. Robustez (Cenários 1 e 2, exclusão da Bradsaúde), indicadores com valores ausentes ou extremos
   (Biomm, Alliar) e reprodutibilidade (planilha e script).

**Vai se importar especialmente com:** se as afirmações de "tendência" e o resultado da pandemia são
sustentados pelos testes, sem que se leia além do que o p-valor permite.
**Possíveis pontos cegos:** o debate teórico sobre riqueza socioemocional (SEW).

### Cartão de configuração n.º 3
**Papel:** Revisor 2 (domínio)
**Identidade:** pesquisador de governança corporativa e empresas familiares no Brasil, que já
publicou sobre estrutura de propriedade e controle na B3 e conhece a literatura sobre SEW e
estrutura de capital.
**Foco da revisão:**
1. Cobertura da literatura: SEW, agência, *trade-off*, *pecking order*, estudos brasileiros sobre
   familiares e endividamento.
2. Fundamentação da hipótese e do argumento sobre prazo da dívida (Diamond, 1991).
3. Validade da proxy de empresa familiar (Santos e Silva, 2018) e comparação com os outros critérios.

**Vai se importar especialmente com:** se a classificação das empresas (participação indireta, blocos
de controle, data fixa do FRE) é defensável e se faltam estudos-chave.
**Possíveis pontos cegos:** detalhes de cálculo estatístico.

### Cartão de configuração n.º 4
**Papel:** Revisor 3 (perspectiva prática e setorial)
**Identidade:** analista de crédito corporativo e de setor de saúde (visão de banco e de agência de
rating), com conhecimento de *covenants*, ciclo de caixa de varejo farmacêutico e
hospitais/operadoras.
**Foco da revisão:**
1. Se as diferenças podem ser explicadas pelo modelo de negócio dos subsetores (varejo e distribuição
   × hospitais × operadoras de planos) e por eventos corporativos (fusões, IPOs, aquisições).
2. Leitura prática dos indicadores (Dívida líquida/EBITDA, prazo da dívida e refinanciamento na
   pandemia).
3. Implicações para credores, investidores e gestores.

**Vai se importar especialmente com:** se o "efeito família" não é, na verdade, efeito do subsetor,
do tamanho ou de eventos como as fusões de Hapvida e NotreDame e de Rede D'Or e SulAmérica.
**Possíveis pontos cegos:** o rigor estatístico formal.

*(5.º assento fixo: Advogado do Diabo, sem cartão; contesta o argumento central.)*

## Recomendações de estratégia
- O ponto mais sensível é a força das conclusões diante de um resultado nulo: tendência descritiva ×
  inferência.
- Há tensão esperada entre o Revisor 1 (cautela estatística) e o Revisor 3 (explicações setoriais
  alternativas). O sintetizador deve reconciliar as duas leituras.
