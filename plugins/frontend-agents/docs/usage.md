# Usage

## New Feature

```text
Use frontend-production-workflow for this new feature.
Main agent must orchestrate: define scope, create the subagent interaction plan, assign bounded work or review to configured subagents, integrate results, and make final decisions.
If this is a new visual surface, redesign, rendered UI bug, or major polish pass, route through the installed Build Web Apps plugin first.
Use frontend-editor only for bounded edits.
Use reviewer subagents with decision-based review gates before acceptance:
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
Main agent must orchestrate: own Build Web Apps routing, Image Gen concepting when required, Browser/IAB-first validation, screenshots, fidelity ledger, subagent assignments, and final acceptance.
Delegate bounded implementation or focused review to frontend-editor and reviewer subagents after the Build Web Apps target flow or design spec is clear.
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
Main agent must orchestrate the review and use configured reviewer subagents by default. Spawn the reviewers relevant to the files changed:
- frontend-architecture-reviewer
- react-quality-reviewer
- shadcn-reviewer
- accessibility-reviewer
- vite-performance-reviewer
- design-polish-reviewer

Do not edit files unless I ask for fixes after the review.
In the final report, include each reviewer decision and explicitly list any skipped reviewer with the reason.
```

## Existing Project Audit

```text
Use frontend-production-workflow. Audit this existing React/Vite/shadcn project.
Do not edit product code yet.

Main agent must orchestrate: inspect the repo, fan out to configured reviewer subagents wherever the surface exists, integrate findings, and decide the recommended adoption path:
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

## Bounded Editor Work

```text
Use frontend-editor-workorder to create a precise work order for this UI change.
Then use frontend-editor only for the allowed files. Main agent remains the orchestrator and must integrate the editor result plus any relevant reviewer findings.
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
