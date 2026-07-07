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

Use subagents when:

- Reviews are independent.
- Work can be split by file or module.
- Accessibility, performance, or focused polish checks can run from evidence while the main agent continues.
- The main thread would otherwise fill with noisy logs and exploration.

Do not use subagents when:

- The change is tiny.
- The work is still in Build Web Apps concept approval or final fidelity acceptance.
- Browser/IAB evidence collection is the main unresolved task.
- The next step is one obvious local investigation.
- Multiple agents would write the same files without clear ownership.
- There is no validation baseline and the main agent can inspect faster.

## Rework Loop

1. First review: full relevant reviewer pass.
2. First rework: fix blockers, majors, and missing required evidence.
3. Second review: only reviewers that returned `Blocked` or `Fix Required`.
4. Second rework: final targeted fixes.
5. If still blocked, escalate with concrete tradeoffs.
