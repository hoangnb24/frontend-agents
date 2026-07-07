# Subagent Orchestration

Use one accountable main orchestrator, one bounded editor, and specialist read-only reviewers.

```text
Main Orchestrator
  |-- Build Web Apps plugin skills when triggered
  |-- frontend-editor
  |-- frontend-architecture-reviewer
  |-- react-quality-reviewer
  |-- shadcn-reviewer
  |-- accessibility-reviewer
  |-- vite-performance-reviewer
  |-- design-polish-reviewer
```

## Main Orchestrator Owns

- Goal and scope.
- Project discovery.
- Build Web Apps routing for visual creation, redesign, rendered QA, React/Next guidance, shadcn guidance, Stripe guidance, and Supabase/Postgres guidance.
- Image Gen concepting and concept approval when `build-web-apps:frontend-app-builder` applies.
- Feature contract.
- Work decomposition.
- Delegation.
- Final decisions.
- Integration.
- Browser/IAB-first rendered validation, screenshot evidence, fidelity ledgers, and final validation.
- Final summary.

## Editor Owns

- Concrete file edits.
- Bounded write scope.
- Tests for assigned files.
- No architecture invention outside the work order.

## Reviewers Own

- Findings only by default.
- No file edits unless explicitly assigned.
- One risk area.
- Short actionable reports with file references.

## When To Use Subagents

Use subagents by default whenever `frontend-production-workflow` is triggered. The main agent should always start as the orchestrator, decide which configured subagents apply, interact with at least one configured subagent for implementation, review, validation, or focused risk assessment, then integrate the result.

At minimum, the orchestrator records:

- Which subagents were used.
- What each subagent was asked to decide or produce.
- Which configured subagents were skipped and why.
- How the reviewer findings changed the final decision.

Use more subagents when:

- The user asks to audit an existing frontend system.
- The user asks for production-readiness review.
- The user asks to review the current diff and more than one risk area is involved.
- The project has configured frontend reviewer agents available.
- Reviews are independent.
- Work can be split by file or module.
- Accessibility, performance, or focused polish checks can run from evidence while the main agent continues.
- The main thread would otherwise fill with noisy logs and exploration.

Use fewer subagents when:

- The change is tiny.
- The work is still in Build Web Apps concept approval or final fidelity acceptance.
- Browser/IAB evidence collection is the main unresolved task.
- The next step is one obvious local investigation.
- Multiple agents would write the same files without clear ownership.
- There is no validation baseline and the main agent can inspect faster.

The only acceptable no-subagent fallback is when subagent roles are unavailable in the current session, the user explicitly forbids delegation, or the task is blocked before a meaningful subagent assignment can be made. State that fallback in the final response.

## Production-Workflow Fan-Out

For any React/Vite/shadcn production workflow, the main orchestrator should first inspect enough context to identify the package manager, app folders, routes, shadcn/Tailwind setup, scripts, changed files, and available UI surfaces. Then assign configured agents with concrete, non-overlapping scopes.

Recommended agent routing:

- `frontend-editor`: bounded implementation with explicit allowed files and a work order.
- `frontend-architecture-reviewer`: structure, layers, feature boundaries, route composition, shared abstractions, and ownership.
- `react-quality-reviewer`: React state/effect/hook correctness, render purity, stale closures, rerender risk, keys, and test shape.
- `shadcn-reviewer`: shadcn/Radix composition, Tailwind tokens, component reuse, forms, dialogs, menus, cards, tabs, icon conventions, and required UI states.
- `accessibility-reviewer`: labels, accessible names, keyboard/focus behavior, invalid states, screen-reader affordances, dialogs, menus, and reduced motion.
- `vite-performance-reviewer`: production build health, imports, dependencies, bundle warnings, code splitting, async waterfalls, and runtime performance risks.
- `design-polish-reviewer`: rendered visual hierarchy, spacing, typography, density, responsive behavior, state polish, and product/design fit.

The orchestrator should pass each reviewer:

- The user goal and current mode.
- Relevant files, folders, routes, or diff range.
- Local docs already read, such as `AGENTS.md`, `PRODUCT.md`, and `DESIGN.md`.
- Commands already run and their results.
- Whether browser/rendered evidence is available.
- The standard Decision/Evidence/Finding output format.

If the orchestrator does not use a configured agent, it must state why: no relevant surface, missing agent role, unavailable evidence, user constraint, or conflict risk.

## Rework Loop

1. First review: full relevant reviewer pass.
2. First rework: fix blockers, majors, and missing required evidence.
3. Second review: only reviewers that returned `Blocked` or `Fix Required`.
4. Second rework: final targeted fixes.
5. If still blocked, escalate with concrete tradeoffs.
