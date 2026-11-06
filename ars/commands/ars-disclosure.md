---
disable-model-invocation: true
name: ars-disclosure
description: ARS academic-paper, modo `disclosure` — pacote de aplicabilidade/status por periódico ou renderização de policy-anchor
model: sonnet
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper` no modo avulso `disclosure` (declaração de uso de IA). O Agente 9 deve carregar `${CLAUDE_PLUGIN_ROOT}/academic-paper/references/disclosure_mode_protocol.md` antes de renderizar; a declaração genérica do formatter não é alternativa. O caminho padrão por periódico retorna a aplicabilidade `REQUIRED`, `ACTION_ONLY`, `NOT_REQUIRED` ou `UNKNOWN`, mais um status de parada tipado explícito quando necessário (15 alvos de política suportados: ICLR / NeurIPS / Nature / Science / ACL / EMNLP mais alvos de publicação médica — ICMJE / NEJM / The Lancet / JAMA / BMJ / PLOS / Frontiers / 中华护理杂志社 / 国际眼科杂志). Para TCC, a instituição normalmente não está na lista: o resultado provável é `UNKNOWN`, e você deve conferir as regras da sua universidade. O caminho `--policy-anchor` usa seu próprio renderizador específico. Espectro de fidelidade, baixa supervisão.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
