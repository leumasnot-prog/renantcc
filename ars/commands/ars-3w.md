---
disable-model-invocation: true
name: ars-3w
description: ARS deep-research, modo `three-way-scan` — comparação de artigos por POR QUÊ / COMO / O QUÊ
model: sonnet
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:deep-research"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `deep-research` no modo `three-way-scan`. Produz uma lista curta de artigos comparados por POR QUÊ (WHY) / COMO (HOW) / O QUÊ (WHAT), mais uma síntese entre artigos (POR QUÊ comum, COMO divergente, O QUÊ mais forte, lacuna não resolvida). Mais leve que `lit-review`; escale para `lit-review` / `systematic-review` para cobertura completa. Espectro de fidelidade, baixa supervisão.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § deep-research.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/deep-research/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
