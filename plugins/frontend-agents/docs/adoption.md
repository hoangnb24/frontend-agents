# Project Adoption

## Existing Projects

Use this prompt:

```text
Use frontend-production-workflow. Audit this existing React/Vite/shadcn project.
Do not edit product code yet.
Main agent must orchestrate: inspect the repo, fan out to configured reviewer subagents by default, integrate findings, and decide the recommended adoption path:
- frontend-architecture-reviewer
- react-quality-reviewer
- shadcn-reviewer
- accessibility-reviewer
- vite-performance-reviewer
- design-polish-reviewer

Return:
1. Current frontend structure.
2. shadcn/Tailwind setup.
3. Existing scripts and validation gaps.
4. Reviewer decisions and severity-tagged findings.
5. Top frontend quality risks.
6. Recommended custom-agent or workflow gaps.
7. First low-risk adoption PR.

If a reviewer is skipped, state the reason.
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
Main agent must orchestrate: create the subagent interaction plan, use frontend-editor for bounded file creation when useful, and run relevant reviewer subagents before acceptance.
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
