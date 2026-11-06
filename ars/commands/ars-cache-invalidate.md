---
name: ars-cache-invalidate
description: ARS /ars-cache-invalidate — apagar as entradas de verificação em cache de uma chave de citação
model: sonnet
---

Invalida o cache persistente de verificação de uma chave de citação, para que a próxima execução do pipeline a verifique de novo, ao vivo, no Crossref / OpenAlex / Semantic Scholar / arXiv, em vez de devolver um veredito antigo do cache. Use quando os metadados de uma citação mudaram (por exemplo, um preprint ganhou DOI publicado) ou quando uma verificação anterior parece errada.

O cache (spec v3.11 #182 Delta 2) é um armazenamento SQLite local em `~/.cache/ars/verification.db` (altere via `ARS_VERIFICATION_CACHE_PATH`), indexado por `(citation_key, resolver_name, query_form)` com validade de 90 dias. Este comando remove **todas** as entradas em cache da chave de citação indicada (os quatro resolvedores, todas as formas de consulta); outras citações não são afetadas. É idempotente — invalidar uma chave sem linhas em cache é uma operação nula bem-sucedida.

**Cascata de invalidação (#541, incondicional)**: após a invalidação, o próximo gate regenera a linha de resumo de verificação da citação e reexecuta os vereditos de auditoria da Fase E para as afirmações que a citam — incondicionalmente (nenhuma base é guardada para comparação), cobrindo status de existência, metadados e evidência recuperada. Um aviso por idade também aponta automaticamente entradas antigas nos gates (`ARS_CACHE_STALE_ADVISORY_DAYS`, padrão 30; reverificação ao vivo opcional via `ARS_CACHE_REVALIDATE=1`).

Para invalidar o cache **inteiro** de uma vez (por exemplo, após um bug sistêmico de resolvedor que guardou muitos falsos negativos), apague o arquivo diretamente: `rm ~/.cache/ars/verification.db`. Ele é recriado vazio na próxima execução.

Implementação:
```bash
python3 scripts/ars_cache_invalidate.py $ARGUMENTS
```

Referência do modo: `docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md` §2 Delta 2.
