# Project Adoption

## Existing Projects

Use this prompt:

```text
Use frontend-production-workflow. Audit this existing React/Vite/shadcn project.
Do not edit product code yet.

Return:
1. Current frontend structure.
2. shadcn/Tailwind setup.
3. Existing scripts and validation gaps.
4. Top frontend quality risks.
5. Recommended custom agents.
6. First low-risk adoption PR.
```

Recommended first PR:

- Add or update `AGENTS.md`.
- Add `docs/frontend-workflow.md`.
- Copy selected agent TOMLs from the plugin into `.codex/agents/`.
- Add validation scripts only if missing.
- Avoid product UI refactors in the adoption PR.

## New Projects

Use this prompt:

```text
Use frontend-production-workflow. Bootstrap a new React + Vite + TypeScript + Tailwind + shadcn project.
Set up component layers, AGENTS.md, PRODUCT.md, DESIGN.md placeholders, validation scripts, and custom frontend subagents.
Do not create marketing filler; create the actual app shell.
```

Baseline structure:

```text
src/
  components/
    ui/
    common/
    layout/
  features/
  hooks/
  lib/
  routes/ or pages/
  test/
```

