# Créditos e registro da adaptação (pt-BR)

**Obra original:** Academic Research Skills (ARS) v3.24.2, © 2026 Cheng-I Wu (Imbad0202)
<https://github.com/Imbad0202/academic-research-skills>, commit `6d9388674de1ad0437ad95db3d52f92b92204d84`.

**Licença:** Creative Commons Atribuição-NãoComercial 4.0 Internacional (CC BY-NC 4.0),
texto completo em `ars/LICENSE`. Esta adaptação também é distribuída sob CC BY-NC 4.0
e **só pode ser usada para fins não comerciais**, como este TCC.

## O que foi alterado
1. **Descrições das 5 skills** (`ars/*/SKILL.md`, campo `description`): traduzidas para
   pt-BR, com gatilhos em português ("revisão de literatura", "TCC", "simular banca"
   etc.). Os gatilhos originais foram mantidos em parte.
2. **16 comandos** (`ars/commands/ars-*.md`): descrição e texto traduzidos para pt-BR,
   com a instrução de responder em português. Caminhos, nomes de arquivos, flags e
   tokens técnicos ficaram iguais.
3. **Marketplace** (`ars/.claude-plugin/marketplace.json`): renomeado para `ars-ptbr`
   para a instalação local por projeto.
4. **Arquivos novos deste repositório:** `CLAUDE.md` (idioma, normas ABNT, integridade),
   `GUIA-ARS.md` (guia de uso em português), este arquivo e `.claude/settings.json`.
5. **Arquivos omitidos da cópia** (não são usados durante o uso das skills): `.git`,
   `evals/`, `tests/`, `audits/`, `examples/`, `plugin-evals*`, `scripts/fixtures`,
   `scripts/test_*`, `CHANGELOG.md`, `docs/changelog-archive`, `.github/` e os READMEs
   em ja/ko/zh-CN/es. A tradução comunitária `ars/README.pt-BR.md` foi mantida.

## O que **não** foi traduzido, e por quê
Os corpos dos `SKILL.md`, os agentes e os protocolos em `ars/shared/` e `*/references/`
(cerca de 3,9 MB de instruções operacionais) continuam em inglês. Eles são lidos pelo
modelo, não pelo usuário, e contêm tokens contratuais exatos (nomes de campos, IRON
RULES, marcadores) que os scripts de verificação em `ars/scripts/` comparam literalmente.
Traduzir esses arquivos quebraria essas verificações e não mudaria o idioma das
respostas, que saem em português por causa do `CLAUDE.md` e dos comandos.

## Atualizar a partir do original
Clone o repositório original, copie as pastas de novo para `ars/` e reaplique os itens
1 a 3 acima.
