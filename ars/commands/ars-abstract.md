---
disable-model-invocation: true
name: ars-abstract
description: ARS academic-paper, modo `abstract-only` — resumo bilíngue + palavras-chave
model: sonnet
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper` no modo `abstract-only`. Produz um resumo bilíngue mais palavras-chave. Os idiomas do resumo seguem o `output_language_pair` declarado na execução, um valor por execução cujo padrão é `zh-tw-en` (zh-TW + EN) — portanto, para um TCC em português, peça explicitamente "resumo em português + abstract em inglês" (Resumo/Abstract). Espectro de fidelidade, supervisão média. Carrega a camada PATTERN PROTECTION do `report_compiler_agent` v3.6.7 quando invocado pelo pipeline.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
