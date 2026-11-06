---
name: ars-mark-read
description: ARS /ars-mark-read — registrar a declaração do usuário de que leu a fonte de uma ou mais chaves de citação
model: sonnet
---

Registra a declaração `USER_ATTESTED_READ` do usuário para as fontes por trás das chaves de citação indicadas. É uma declaração do usuário, não uma evidência independente de que uma pessoa leu ou entendeu a fonte. Um finalizador pode promover `<!--ref:slug LOW-WARN-->` para `<!--ref:slug ok-->` somente quando o escopo declarado cobre a âncora daquela citação. Conforme a spec v3.6.8 §3.6, o sinal é guardado em um arquivo par da sessão `<passport-stem>_human_read_log.yaml` ao lado do Material Passport ativo; `literature_corpus[]` pertence ao adaptador e NUNCA é alterado para guardar estado de leitura.

O agente que despacha substitui `<path>` abaixo pelo caminho do Material Passport ativo no contexto da sessão antes de executar (as aspas são preservadas para que caminhos com espaços continuem sendo um único argumento). A CLI faz a validação (citation_key deve existir em `literature_corpus[]`; se não existir, emite `[ARS-MARK-READ ERROR: citation_key '<slug>' not in literature_corpus[]]` e se recusa a gravar), 4 checagens de ambiente com falha rápida (sem passport ativo / passport não encontrado / pasta pai ilegível / log de leitura sem permissão de escrita) e gravação somente por acréscimo conforme a regra firme 3 da §3.6.

O escopo de leitura é obrigatório em toda marcação nova (#738; apenas declaração — repasse o que o usuário disser, nunca infira): `--scope {full_text,sections,abstract_only,toc_only,unknown}` registra a cobertura declarada; `--locator "<texto>"` (repetível, exige `--scope sections`) nomeia as seções/páginas lidas; `--note "<texto>"` texto livre (exige `--scope`). Use `--scope unknown` quando o usuário não souber especificar a cobertura. Escopo ausente só é aceito em registros legados. `unknown` explícito e escopo legado ausente continuam como `coverage_unknown`; reconhecem a declaração, mas nunca promovem uma citação ancorada para `ok`. Cobertura de páginas exige um localizador explícito `page`, `p.` ou `pp.` — números soltos e `section <n>` nunca contam como intervalo de páginas. O resolvedor determinístico em `scripts/human_read_attestation_resolver.py` valida estritamente o registro atual e calcula uma decisão de roteamento transitória a cada passagem do finalizador; sua saída não é um recibo de auditoria persistido.

Implementação:
```bash
python3 scripts/ars_mark_read.py $ARGUMENTS --passport-path "<path>"
```

Referência do modo: `docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md` §3.6 + Step 7.
