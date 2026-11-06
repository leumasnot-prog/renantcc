---
name: ars-unmark-read
description: ARS /ars-unmark-read — revogar a declaração de leitura do usuário para uma ou mais chaves de citação
model: sonnet
---

Revoga uma declaração `USER_ATTESTED_READ` registrada antes para as chaves de citação indicadas. Pela regra firme 3 da spec v3.6.8 §3.6, o arquivo par da sessão `<passport-stem>_human_read_log.yaml` é somente por acréscimo: a revogação grava um campo `rescinded_at: <ISO 8601>` na entrada correspondente em vez de apagá-la, para que a reauditoria reconstrua a trajetória do sinal do usuário. A próxima passagem do finalizador rebaixa qualquer `<!--ref:slug ok-->` dependente de cobertura de volta para `<!--ref:slug LOW-WARN-->` para cada slug revogado.

O agente que despacha substitui `<path>` abaixo pelo caminho do Material Passport ativo no contexto da sessão antes de executar. A CLI exige que a citation_key exista em `literature_corpus[]` E tenha uma marcação anterior não revogada no log de leitura; falha de forma rígida caso contrário, com a mensagem canônica `[ARS-MARK-READ ERROR: ...]`.

Implementação:
```bash
python3 scripts/ars_mark_read.py $ARGUMENTS --passport-path "<path>" --unmark
```

Referência do modo: `docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md` §3.6 + Step 7.
