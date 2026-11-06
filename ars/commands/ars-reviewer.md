---
disable-model-invocation: true
name: ars-reviewer
description: ARS academic-paper-reviewer, modo `full` — painel simulado de revisão por pares
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper-reviewer"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper-reviewer` no modo `full`. Respeite modos alternativos explícitos quando presentes: `quick`, `methodology-focus`, `re-review`, `guided` ou `calibration`. Roda no modelo herdado da sessão — o piso `opus` do frontmatter v3.7.0 foi retirado na revisão de 2026-06, para que um modelo de sessão mais forte nunca seja rebaixado silenciosamente.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper-reviewer.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper-reviewer/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
