---
name: frontend-production-workflow
description: Use for production React, Vite, TypeScript, Tailwind, and shadcn/ui frontend work, including new UI features, AI-generated component hardening, existing project adoption, review-gate orchestration, and validation planning.
---

# Frontend Production Workflow

Use this skill when the task involves React/Vite/shadcn frontend implementation, adoption, review, or production-readiness validation.

## Workflow

1. Act as the main orchestrator for every production workflow run. Own scope, decisions, subagent assignments, integration, validation, and final acceptance.
2. Detect the mode: existing project adoption, new project bootstrap, new feature, component refactor, audit, or review only.
3. Inspect `AGENTS.md`, `package.json`, existing component folders, shadcn/Tailwind config, scripts, test setup, and any `PRODUCT.md` or `DESIGN.md`.
4. Define the UI contract: user goal, inputs, emitted events, loading, empty, error, disabled, permission, success, and keyboard states.
5. Choose the component layer before editing: `components/ui`, shared app component, feature component, or route/page composition.
6. Create a subagent interaction plan for the current mode before doing the bulk of the work. Use at least one configured subagent for implementation, review, validation, or focused risk assessment unless subagents are unavailable or the user explicitly forbids delegation.
7. For implementation mode, create a bounded work order and use `frontend-editor` for clearly scoped edits. Use `frontend-editor-workorder` for the work-order shape.
8. For audit or review-only mode, fan out to the configured reviewers that match the surface: `frontend-architecture-reviewer`, `react-quality-reviewer`, `shadcn-reviewer`, `accessibility-reviewer`, `vite-performance-reviewer`, and `design-polish-reviewer`.
9. Prefer existing shadcn primitives and project components before custom markup. Do not assume Figma is part of the workflow.
10. For visual creation, redesign, major polish, or rendered UI debugging, route through the installed Build Web Apps plugin first; keep the main agent accountable for design approval, Browser/IAB evidence, and final acceptance.
11. Run decision-based specialist review through the configured reviewer subagents before acceptance wherever the changed or inspected surface creates frontend risk. If a configured subagent is unavailable or skipped, state that fallback explicitly.
12. Send precise rework orders for `Blocked`, `Blocker`, or unresolved `Major` findings. Treat reviewer output as evidence, not numeric scoring.
13. Validate with the project scripts that actually exist, usually lint, typecheck, tests, build, shadcn info/docs, and browser/a11y checks for UI behavior.
14. Summarize changed files, validation, accepted/deferred findings, residual risk, which subagents ran, which were skipped, and exact next steps.

## Orchestrator And Subagent Delegation

When this skill is triggered, the main agent must behave as an orchestrator, not as a solo implementer. The orchestrator makes the plan, chooses the relevant subagents, gives each one a bounded assignment, integrates their results, decides what to accept or rework, and reports the delegation outcome.

Default subagent map:

- `frontend-editor`: bounded implementation from a precise work order.
- `frontend-architecture-reviewer`: component layers, feature boundaries, route composition, shared abstractions, and ownership.
- `react-quality-reviewer`: state, effects, hooks, render purity, stale closures, rerender risk, and behavior-focused tests.
- `shadcn-reviewer`: shadcn/Radix composition, semantic tokens, Tailwind usage, forms, dialogs, menus, cards, tabs, icons, loading, empty, and error states.
- `accessibility-reviewer`: labels, accessible names, keyboard behavior, focus management, invalid states, dialogs, menus, reduced motion, and rendered accessibility evidence.
- `vite-performance-reviewer`: production build health, imports, bundle risk, code splitting, async waterfalls, dependency weight, and runtime performance evidence.
- `design-polish-reviewer`: rendered hierarchy, spacing, density, typography, responsive layout, state polish, and product/design consistency.

Default interaction patterns:

- Existing project adoption: use reviewer fan-out, then recommend the first adoption PR.
- New feature or refactor: use `frontend-editor` for scoped edits when edits are needed, then run the relevant reviewers before acceptance.
- New project bootstrap: use the orchestrator for structure and contract decisions, use `frontend-editor` for bounded file creation when useful, then run architecture, React, shadcn, accessibility, performance, and design-polish review as relevant.
- Rendered debugging or polish: use Build Web Apps routing first when applicable, then use accessibility, performance, and design-polish reviewers against the rendered evidence.
- Review-only or audit: use reviewer fan-out and do not edit unless the user asks for fixes.

The orchestrator should inspect the project first, then assign each subagent a concrete scope: files, routes, changed diff, commands already run, and evidence needed. Use fewer subagents only when the repository lacks that surface area, the user requested a narrower review, or a role is unavailable. In the final response, list subagent decisions and note any skipped configured subagent with the reason.

## Load References

Load only the files needed for the current task:

- `references/expected-workflow.md` for the end-to-end UI workflow.
- `references/component-layering.md` for ownership and folder decisions.
- `references/project-adoption-playbooks.md` for adopting the workflow in existing or new projects.
- `references/subagent-orchestration.md` for orchestrator/editor/reviewer delegation.
- `references/mcp-and-review-gates.md` for MCP assignment and decision gates.
- `references/build-web-apps-interop.md` for using the installed Build Web Apps plugin from the main-agent workflow.
- `references/source-reference-map.md` for source documents and external references.
