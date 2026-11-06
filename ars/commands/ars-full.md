---
disable-model-invocation: true
name: ars-full
description: ARS pipeline completo — pesquisa → escrita → revisão → revisão do texto → finalização
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-pipeline"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona o orquestrador `academic-pipeline` (`(pipeline)` em `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` — o orquestrador não tem modo nomeado próprio). Carrega a skill e executa o fluxo de pesquisa acadêmica completo (orquestração em 10 etapas: deep-research → academic-paper → integridade → academic-paper-reviewer → revisão do texto → re-revisão → integridade final → finalização).

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-pipeline.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-pipeline/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
