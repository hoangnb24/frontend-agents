# Usage

## New Feature

```text
Use frontend-production-workflow for this new feature.
Main agent should orchestrate.
If this is a new visual surface, redesign, rendered UI bug, or major polish pass, route through the installed Build Web Apps plugin first.
Use frontend-editor only for bounded edits.
Use reviewer subagents with decision-based review gates:
- frontend-architecture-reviewer
- react-quality-reviewer
- shadcn-reviewer
- accessibility-reviewer
- vite-performance-reviewer
- design-polish-reviewer

Acceptance gate:
- No Blocked reviewer decisions.
- No Blocker findings.
- No unresolved Major findings unless I explicitly accept the risk.
- Required validation commands pass.
- Missing evidence is resolved or explicitly documented as not required.
```

## Build Web Apps Plugin

```text
Use frontend-production-workflow and the installed Build Web Apps plugin.
Main agent owns Build Web Apps routing, Image Gen concepting when required, Browser/IAB-first validation, screenshots, fidelity ledger, and final acceptance.
Delegate only bounded implementation or focused review to frontend-editor and reviewer subagents after the Build Web Apps target flow or design spec is clear.
```

Useful routing:

- `build-web-apps:frontend-app-builder` for new apps, dashboards, games, creative sites, heroes, redesigns, and modernization.
- `build-web-apps:frontend-testing-debugging` for rendered bugs, interactions, responsive issues, console errors, visual regressions, and frontend QA.
- `build-web-apps:react-best-practices` for React/Next component and performance-sensitive work.
- `build-web-apps:shadcn` for shadcn/ui registry, CLI, component composition, and preset work.
- `build-web-apps:stripe-best-practices` and `build-web-apps:supabase-postgres-best-practices` for provider-backed frontend features.

## Review Only

```text
Use frontend-production-workflow to review the current diff.
Spawn only the reviewers relevant to the files changed.
Do not edit files unless I ask for fixes after the review.
```

## Bounded Editor Work

```text
Use frontend-editor-workorder to create a precise work order for this UI change.
Then use frontend-editor only for the allowed files.
```

## Reviewer Output

Reviewers should return:

```md
## Decision
Decision: Pass | Advisory | Fix Required | Blocked
Evidence: Verified | Partially Verified | Not Verified

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
