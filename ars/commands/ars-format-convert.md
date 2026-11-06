---
disable-model-invocation: true
name: ars-format-convert
description: ARS academic-paper, modo `format-convert` — converter para LaTeX / DOCX / PDF / Markdown
model: sonnet
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper` no modo `format-convert`. Converte um trabalho entre LaTeX, DOCX (via Pandoc), PDF ou Markdown, e converte estilos de citação entre os principais formatos. Espectro de fidelidade, baixa supervisão.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
