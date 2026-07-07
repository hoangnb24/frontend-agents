# Project Adoption Playbooks

## Existing Project Adoption

Start with an audit. Do not mass-refactor first.

Return:

1. Current frontend structure.
2. shadcn/Tailwind setup.
3. Existing scripts and validation gaps.
4. Reviewer decisions and severity-tagged findings.
5. Top frontend quality risks.
6. Proposed `.codex/agents` and skill setup.
7. First low-risk adoption PR.

Recommended first PR:

- Add `docs/frontend-workflow.md`.
- Add or update `AGENTS.md`.
- Add project-scoped or plugin-based frontend workflow guidance.
- Add `.codex/agents/*` custom agent files from this plugin's `agents/` templates so the production workflow can orchestrate configured subagents.
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
- Custom agents in `.codex/agents` so the production workflow can orchestrate configured subagents.

Do not create a marketing landing page unless explicitly requested. Build the actual app shell or workflow surface.

## New Feature Development

Feature flow:

1. Main agent acts as orchestrator and creates the subagent interaction plan.
2. Main agent defines feature contract.
3. Main agent maps components to layers.
4. Main agent writes an editor work order.
5. `frontend-editor` implements bounded changes when edits are needed.
6. Relevant reviewers inspect independently before acceptance.
7. Main agent reconciles feedback.
8. Editor or main agent applies fixes.
9. Main agent validates and summarizes.

Use fewer subagents for narrow work, but do not silently collapse the production workflow into a solo main-agent pass. If a configured subagent is skipped, record the reason.
