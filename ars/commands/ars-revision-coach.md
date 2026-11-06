---
disable-model-invocation: true
name: ars-revision-coach
description: ARS academic-paper, `revision-coach` — roteiro de revisão a partir de pareceres ou esqueleto de resposta a uma comissão real
---

Primeiro invoque a ferramenta Skill com `skill: "academic-research-skills:academic-paper"`. Passe o modo e o pedido do usuário descritos abaixo como argumentos. Use a skill carregada e seus arquivos de apoio antes de produzir o resultado. Responda ao usuário em português do Brasil.

Aciona a skill `academic-paper` no modo `revision-coach`. Comentários comuns de revisores produzem um Roteiro de Revisão mais um esqueleto de Carta de Resposta, sem escrever a revisão. Se, e somente se, o usuário identificar explicitamente uma comissão real ou um órgão institucional de revisão (por exemplo, um comitê de ética/CEP), use a variante de correspondência com comissão #668: preserve a fonte em UTF-8, emita o rastreador de pendências separado e o esqueleto de resposta com espaços reservados, e rode seu verificador determinístico de completude. Nunca infira autoridade de comissão pelo tom, e nunca emita prioridade, gravidade, determinação ou Schema 11 nesse ramo. Roda no modelo herdado da sessão.

Referência do modo: `${CLAUDE_PLUGIN_ROOT}/MODE_REGISTRY.md` § academic-paper.
Entrada da skill: `${CLAUDE_PLUGIN_ROOT}/academic-paper/SKILL.md`.

Resolva os recursos do plugin a partir de `${CLAUDE_PLUGIN_ROOT}`, não do diretório de trabalho do projeto do trabalho acadêmico. Se a skill ou um arquivo necessário não puder ser carregado, informe a falha de carregamento e pare; não substitua as instruções do modo por este resumo do comando.
