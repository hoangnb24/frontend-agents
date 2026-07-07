---
name: frontend-production-workflow
description: Use for production React, Vite, TypeScript, Tailwind, and shadcn/ui frontend work, including new UI features, AI-generated component hardening, existing project adoption, review-gate orchestration, and validation planning.
---

# Frontend Production Workflow

Use this skill when the task involves React/Vite/shadcn frontend implementation, adoption, review, or production-readiness validation.

## Workflow

1. Detect the mode: existing project adoption, new project bootstrap, new feature, component refactor, or review only.
2. Inspect `AGENTS.md`, `package.json`, existing component folders, shadcn/Tailwind config, scripts, test setup, and any `PRODUCT.md` or `DESIGN.md`.
3. Define the UI contract: user goal, inputs, emitted events, loading, empty, error, disabled, permission, success, and keyboard states.
4. Choose the component layer before editing: `components/ui`, shared app component, feature component, or route/page composition.
5. Create a bounded work order for editing when delegation is useful. Use `frontend-editor-workorder` for the work-order shape.
6. Prefer existing shadcn primitives and project components before custom markup. Do not assume Figma is part of the workflow.
7. For visual creation, redesign, major polish, or rendered UI debugging, route through the installed Build Web Apps plugin first; keep the main agent accountable for design approval, Browser/IAB evidence, and final acceptance.
8. Run decision-based specialist review where risk warrants it: architecture, React, shadcn, accessibility, Vite/performance, and design polish.
9. Send precise rework orders for `Blocked`, `Blocker`, or unresolved `Major` findings. Treat reviewer output as evidence, not numeric scoring.
10. Validate with the project scripts that actually exist, usually lint, typecheck, tests, build, shadcn info/docs, and browser/a11y checks for UI behavior.
11. Summarize changed files, validation, accepted/deferred findings, residual risk, and exact next steps.

## Load References

Load only the files needed for the current task:

- `references/expected-workflow.md` for the end-to-end UI workflow.
- `references/component-layering.md` for ownership and folder decisions.
- `references/project-adoption-playbooks.md` for adopting the workflow in existing or new projects.
- `references/subagent-orchestration.md` for orchestrator/editor/reviewer delegation.
- `references/mcp-and-review-gates.md` for MCP assignment and decision gates.
- `references/build-web-apps-interop.md` for using the installed Build Web Apps plugin from the main-agent workflow.
- `references/source-reference-map.md` for source documents and external references.
