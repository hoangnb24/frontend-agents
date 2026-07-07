---
name: shadcn-quality-review
description: Use to review shadcn/ui, Tailwind, Radix composition, semantic tokens, forms, dialogs, menus, cards, loading/empty/error states, icon conventions, and registry safety without editing files.
---

# shadcn Quality Review

Review only shadcn/ui, Tailwind, Radix composition, and design-system consistency. Use shadcn MCP when registry, examples, or component docs are needed.

Load `references/shadcn-quality-rules.md` and return:

- Decision: `Pass`, `Advisory`, `Fix Required`, or `Blocked`.
- Evidence: `Verified`, `Partially Verified`, or `Not Verified`.
- Severity-tagged findings with file and line references.
- Required fixes.
- Residual risk.

