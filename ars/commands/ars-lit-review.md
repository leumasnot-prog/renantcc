---
disable-model-invocation: true
name: ars-lit-review
description: ARS academic-paper, modo `lit-review` — bibliografia anotada em formato de artigo
model: sonnet
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper` no modo `lit-review`. Produz uma bibliografia anotada apresentada como seção de revisão de literatura. Espectro de fidelidade, supervisão média.

Permaneça no modo `lit-review` de `academic-paper` e não reabra a escolha do fluxo de trabalho: se os artigos ou fontes a que o pedido se refere estiverem faltando, peça-os ao usuário ou ofereça buscá-los dentro deste modo.

A nota de forma de revisão da skill (#921) pertence a este modo e não reabre essa escolha: mostre-a e aguarde quando a skill mandar, e continue no modo `lit-review` se o autor a pular.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
