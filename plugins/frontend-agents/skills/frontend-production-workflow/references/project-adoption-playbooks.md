# Project Adoption Playbooks

## Existing Project Adoption

Start with an audit. Do not mass-refactor first.

Return:

1. Current frontend structure.
2. shadcn/Tailwind setup.
3. Existing scripts and validation gaps.
4. Top frontend quality risks.
5. Proposed `.codex/agents` and skill setup.
6. First low-risk adoption PR.

Recommended first PR:

- Add `docs/frontend-workflow.md`.
- Add or update `AGENTS.md`.
- Add project-scoped or plugin-based frontend workflow guidance.
- Add `.codex/agents/*` custom agent files from this plugin's `agents/` templates when subagent use is desired.
- Add validation scripts if missing.
- Do not rewrite existing UI in the adoption PR.

Then apply the workflow to:

- New features.
- Components touched for bugs.
- High-risk shared components.
- High-traffic pages.

## New Project Bootstrap

Start with rules and structure before feature UI.

Baseline:

- Vite + React + TypeScript.
- Tailwind and shadcn initialized.
- `components/ui`, `components/common`, `components/layout`, `features`, `hooks`, `lib`, and `test` folders.
- Vitest and Playwright when appropriate.
- ESLint, typecheck, tests, and production build scripts.
- `PRODUCT.md` and `DESIGN.md` placeholders when design polish review matters.
- Custom agents in `.codex/agents` if subagent workflows are expected.

Do not create a marketing landing page unless explicitly requested. Build the actual app shell or workflow surface.

## New Feature Development

Feature flow:

1. Main agent defines feature contract.
2. Main agent maps components to layers.
3. Main agent writes an editor work order.
4. Editor implements bounded changes.
5. Reviewers inspect independently.
6. Main agent reconciles feedback.
7. Editor or main agent applies fixes.
8. Main agent validates and summarizes.

Use subagents only when the work is large enough or the reviews are independent enough to justify the coordination cost.

