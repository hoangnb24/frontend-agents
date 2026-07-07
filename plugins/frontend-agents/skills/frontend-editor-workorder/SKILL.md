---
name: frontend-editor-workorder
description: Use to create or execute a bounded frontend editor work order for React, Vite, TypeScript, Tailwind, and shadcn/ui changes with explicit allowed files, states, constraints, and validation.
---

# Frontend Editor Workorder

Use this skill when a frontend implementation should be delegated or constrained before editing.

## Rules

- Edit only files allowed by the work order.
- Use existing project patterns first.
- Use shadcn primitives before custom markup.
- Use semantic tokens and static Tailwind class names or explicit variant maps.
- Do not define components inside components.
- Do not use `useEffect` for values that can be derived during render.
- Do not introduce architecture outside the brief.
- Return changed files, validation run, and unresolved risks.

Load `references/editor-workorder-template.md` before writing or executing a work order.

