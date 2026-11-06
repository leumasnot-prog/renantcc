---
disable-model-invocation: true
name: ars-rebuttal-audit
description: ARS academic-paper, modo `rebuttal-audit` — auditar um rascunho de resposta existente frente aos comentários dos revisores
model: sonnet
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper` no modo `rebuttal-audit`. Exige AMBOS: os comentários dos revisores E um rascunho de resposta já existente para avaliar. Produz um relatório consultivo de QA (cobertura por comentário + lacunas + sinais de risco). NÃO gera uma nova resposta e NÃO emite Schema 11 / Material Passport / status verificado (a invocação avulsa roda fora do pipeline). Espectro de fidelidade, baixa supervisão.

Se houver apenas comentários dos revisores (ainda sem rascunho), use `revision-coach`.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
