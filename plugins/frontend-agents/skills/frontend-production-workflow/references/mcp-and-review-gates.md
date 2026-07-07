# MCP And Review Gates

## Agent-Local MCP Guidance

Do not give every agent every MCP server. Attach tools only where they support the job.

When the installed Build Web Apps plugin applies, the main agent should use its Browser/IAB-first workflow before falling back to agent-local Playwright. Subagents consume or extend that evidence; they should not create a separate competing browser path unless the work order explicitly asks for it.

| Agent | Suggested MCP | Use |
| --- | --- | --- |
| `frontend-editor` | none by default; `shadcn` optional | Local edits, shadcn component lookup when explicitly needed. |
| `frontend-architecture-reviewer` | `context7` optional, `deepwiki` optional | Framework or external architecture docs when local evidence is insufficient. |
| `react-quality-reviewer` | `context7` optional | Current React/library docs when behavior is uncertain. |
| `shadcn-reviewer` | `shadcn` | Registry, component examples, audit guidance. |
| `accessibility-reviewer` | `playwright`; `axe` optional | Rendered UI, keyboard/focus behavior, accessibility snapshots. |
| `vite-performance-reviewer` | `chrome-devtools`; `context7` optional | Console/network/performance traces, Vite docs, runtime evidence. |
| `design-polish-reviewer` | `playwright`; Impeccable skill/CLI | Screenshots, responsive behavior, design consistency. |

Figma is intentionally excluded from the default workflow.

## Build Web Apps Gate

For work routed through Build Web Apps, add these acceptance checks before applying the normal merge gate:

- `frontend-app-builder`: accepted concept exists when required, implementation follows the concept as source of truth, concept and rendered screenshot were inspected with `view_image`, at least five concrete comparison points were checked, and intentional deviations are listed.
- `frontend-testing-debugging`: target flow is defined, Browser/IAB availability is classified, page identity and nonblank render are verified, framework overlay is absent, console health is checked, screenshot evidence is captured, and at least one interaction proof is recorded.
- `react-best-practices`: relevant React/Next performance rule families were considered for changed code.
- `shadcn`: `npx shadcn@latest info`/docs/registry evidence was used when adding, updating, or reviewing shadcn components.
- `stripe-best-practices` or `supabase-postgres-best-practices`: provider routing was read before implementation and any frontend-only review explicitly stays within UI/state boundaries.

## Decision Levels

| Decision | Meaning | Orchestrator action |
| --- | --- | --- |
| `Blocked` | Review could not complete or found a must-fix issue that prevents safe acceptance. | Resolve missing evidence or send to editor. |
| `Fix Required` | Feature mostly works, but blocker or major issues must be fixed. | Send precise rework order to editor. |
| `Advisory` | No merge-blocking issue, but minor concerns or residual risks remain. | Decide whether to fix now or defer. |
| `Pass` | No material issue found in reviewer scope. | No action required. |

## Severity Levels

| Severity | Meaning | Required action |
| --- | --- | --- |
| `Blocker` | Feature is broken, inaccessible, unsafe, or cannot build. | Always fix. |
| `Major` | Serious likely bug, regression, production risk, or missing required state. | Fix unless user explicitly accepts risk. |
| `Minor` | Real issue with limited impact. | Fix if local and cheap, otherwise track. |
| `Nit` | Polish or maintainability preference. | Optional. |

## Evidence Status

| Evidence | Meaning |
| --- | --- |
| `Verified` | Code was inspected and relevant command/browser/tool evidence was gathered. |
| `Partially Verified` | Code was inspected but one useful verification path could not run. |
| `Not Verified` | Required evidence was unavailable. |

`Pass` requires sufficient evidence for the reviewer scope. Missing required evidence usually becomes `Blocked` or `Advisory`, depending on whether that evidence is essential.

## Reviewer Output Format

```md
## Decision
Decision: Fix Required
Evidence: Verified

## Findings
- [Major] path/to/file.tsx:42 - Problem...

## Evidence
- Reviewed files:
- Commands/tools used:
- States checked:

## Required Fixes
1. ...

## Residual Risk
- ...
```

## Merge Gate

- Any `Blocked` reviewer decision blocks acceptance until resolved.
- Any `Blocker` finding blocks acceptance.
- Any unresolved `Major` finding requires a fix unless the user explicitly accepts the risk.
- Missing required evidence must be resolved or explicitly documented as not required.
- Only `Minor` or `Nit` findings may be accepted or tracked by orchestrator judgment.
