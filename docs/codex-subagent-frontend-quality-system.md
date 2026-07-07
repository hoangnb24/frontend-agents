# Codex Subagent Frontend Quality System

Research date: 2026-07-05

This proposal turns the React/Vite/shadcn frontend workflow into a reusable Codex setup using skills, custom subagents, MCP servers, and optional plugin packaging.

## Key Findings

Codex supports custom subagents through standalone TOML files under:

- Personal scope: `~/.codex/agents/`
- Project scope: `.codex/agents/`

Each custom agent file must define:

- `name`
- `description`
- `developer_instructions`

Custom agent files can also include normal Codex config keys such as:

- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `mcp_servers`
- `skills.config`

This means a subagent can be configured with a narrower instruction set, different reasoning effort, selected MCP servers, and selected skill availability.

Important guardrails:

- Codex only spawns subagents when explicitly asked.
- Subagents inherit the current sandbox policy.
- Parent turn runtime overrides are reapplied to spawned child agents.
- Omitted agent settings inherit from the parent session.
- Parallel write-heavy workflows require care because agents can conflict.
- Agents should be narrow and opinionated, with a tool surface that matches the job.

## Recommended Architecture

Use one orchestrator-driven workflow with specialist subagents.

```text
Main Orchestrator Agent
  |
  |-- Editor Agent
  |-- Frontend Architect Reviewer
  |-- React Quality Reviewer
  |-- shadcn Reviewer
  |-- Accessibility Reviewer
  |-- Vite Performance Reviewer
  |-- Design Polish Reviewer
```

The main agent owns:

- Goal and scope.
- Project discovery.
- Feature contract.
- Work decomposition.
- Delegation.
- Final decisions.
- Integration.
- Validation.
- Final summary.

The editor owns:

- Concrete file edits.
- Bounded write scope.
- Tests for assigned files.
- No architectural invention outside the brief.

Reviewers own:

- Findings only by default.
- No file edits unless explicitly assigned.
- Specific risk area.
- Short actionable reports with file references.

## Skill Layout

Create one reusable skill:

```text
frontend-production-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow.md
│   ├── component-layering.md
│   ├── react-quality-rules.md
│   ├── shadcn-quality-rules.md
│   ├── accessibility-checklist.md
│   ├── vite-performance-checklist.md
│   ├── ai-prompt-templates.md
│   ├── subagent-playbook.md
│   └── adoption-playbooks.md
└── scripts/
    ├── frontend-audit.sh
    └── validate-frontend.sh
```

`SKILL.md` should stay short:

```md
---
name: frontend-production-workflow
description: Use for React/Vite/shadcn frontend development, AI-generated component review, new feature implementation, existing project adoption, and production-readiness validation.
---

## Workflow

1. Detect mode: existing project adoption, new project bootstrap, or new feature.
2. Inspect package manager, React, Vite, Tailwind, shadcn, scripts, and structure.
3. Load the relevant reference file.
4. Define the component contract.
5. Decide component layers.
6. Implement or delegate bounded work.
7. Run specialist review.
8. Apply fixes.
9. Validate with lint, typecheck, tests, and build.
10. Summarize changed files, risks, and next steps.
```

## Project Layout

For a project that adopts this workflow:

```text
project/
├── AGENTS.md
├── PRODUCT.md
├── DESIGN.md
├── .codex/
│   ├── config.toml
│   └── agents/
│       ├── frontend-editor.toml
│       ├── frontend-architect-reviewer.toml
│       ├── react-quality-reviewer.toml
│       ├── shadcn-reviewer.toml
│       ├── accessibility-reviewer.toml
│       ├── vite-performance-reviewer.toml
│       └── design-polish-reviewer.toml
├── .agents/
│   └── skills/
│       └── frontend-production-workflow/
├── docs/
│   └── frontend-workflow.md
├── src/
│   ├── components/
│   │   ├── ui/
│   │   ├── common/
│   │   └── layout/
│   ├── features/
│   ├── hooks/
│   ├── lib/
│   ├── routes/ or pages/
│   └── test/
└── package.json
```

## Suggested MCP Server Mapping

Use MCP per agent based on job.

| Agent | MCP servers | Why |
| --- | --- | --- |
| `frontend-editor` | none by default, maybe Context7 | Keep edits local and reduce external noise. |
| `frontend-architect-reviewer` | Context7, OpenAI Docs optional | Verify framework/design-system patterns when needed. |
| `react-quality-reviewer` | Context7 | Check React/library docs for behavior. |
| `shadcn-reviewer` | Context7 or docs MCP for component docs | Verify current component APIs and composition. |
| `accessibility-reviewer` | Playwright MCP, browser tools | Exercise keyboard/focus behavior. |
| `vite-performance-reviewer` | Context7, browser/devtools MCP | Verify Vite behavior, inspect built app. |
| `design-polish-reviewer` | Figma MCP, Browser/Playwright MCP, Impeccable if installed | Compare implementation against design context and rendered UI. |

Keep sensitive MCP servers away from agents that do not need them. For example, a shadcn reviewer probably does not need GitHub write access, Slack, Gmail, or production observability.

## Example Project `.codex/config.toml`

```toml
[agents]
max_threads = 6
max_depth = 1

[features]
multi_agent = true

[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
enabled = true

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp"]
enabled = true

[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
enabled = false
```

Project config only loads when the project is trusted.

## Example Custom Agents

### `frontend-editor.toml`

```toml
name = "frontend-editor"
description = "Implements bounded React/Vite/shadcn frontend changes from a precise work order."
model_reasoning_effort = "medium"

developer_instructions = """
You are an implementation agent for React, Vite, TypeScript, Tailwind, and shadcn/ui.

Only edit files assigned in the work order. Do not redesign architecture unless the work order explicitly allows it.
Use existing project patterns first. Use shadcn primitives before custom markup.
Do not define components inside components. Do not use useEffect for derived render values.
Do not use raw Tailwind colors unless the project has an approved token.
Return changed files, validation run, and unresolved risks.
"""

[[skills.config]]
path = ".agents/skills/frontend-production-workflow/SKILL.md"
enabled = true
```

### `react-quality-reviewer.toml`

```toml
name = "react-quality-reviewer"
description = "Reviews React code for state, effects, hooks, purity, rerender risk, and component boundaries."
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Review React code like a production maintainer.
Focus on correctness, render purity, unnecessary effects, stale closures, hook dependencies, nested component definitions, excessive state, and missing tests.
Do not edit files. Return findings ordered by severity with file and line references.
"""

[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
enabled = true

[[skills.config]]
path = ".agents/skills/frontend-production-workflow/SKILL.md"
enabled = true
```

### `shadcn-reviewer.toml`

```toml
name = "shadcn-reviewer"
description = "Reviews shadcn/ui composition, Tailwind tokens, forms, dialogs, cards, menus, and component reuse."
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Review only shadcn/ui, Tailwind, and design-system correctness.
Check semantic tokens, component composition, form structure, dialog/sheet/drawer titles, card structure, menu groups, tabs lists, avatar fallback, skeleton/badge/empty/alert usage, icon conventions, and dynamic Tailwind class construction.
Do not edit files. Return actionable findings with file and line references.
"""

[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
enabled = true

[[skills.config]]
path = ".agents/skills/frontend-production-workflow/SKILL.md"
enabled = true
```

### `accessibility-reviewer.toml`

```toml
name = "accessibility-reviewer"
description = "Reviews frontend changes for labels, roles, keyboard behavior, focus management, dialog behavior, and screen reader names."
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Review accessibility behavior for the changed UI.
Prefer rendered behavior evidence when a dev server is available.
Check labels, accessible names, keyboard operation, visible focus, aria-invalid, error messages, dialogs, sheets, menus, and reduced-motion concerns.
Do not edit files. Return findings and suggested fixes.
"""

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp"]
enabled = true

[[skills.config]]
path = ".agents/skills/frontend-production-workflow/SKILL.md"
enabled = true
```

### `vite-performance-reviewer.toml`

```toml
name = "vite-performance-reviewer"
description = "Reviews Vite/React frontend changes for bundle, import, async, and production-build risk."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
Review performance and production build risk.
Check avoidable async waterfalls, heavy imports, barrel imports, large dependencies, route-level splitting opportunities, Vite build warnings, dynamic import preload risk, and unnecessary client work.
Do not edit files. Return findings with concrete proof or state when risk is only a hypothesis.
"""

[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
enabled = true

[[skills.config]]
path = ".agents/skills/frontend-production-workflow/SKILL.md"
enabled = true
```

### `design-polish-reviewer.toml`

```toml
name = "design-polish-reviewer"
description = "Reviews rendered UI for visual hierarchy, spacing, typography, density, consistency, and AI-generated design artifacts."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
Review rendered UI quality.
Use PRODUCT.md and DESIGN.md when present. Check hierarchy, density, spacing, typography, contrast, layout responsiveness, empty/loading/error states, and whether the UI matches the product audience.
Do not edit files by default. Return prioritized visual issues and concrete changes.
"""

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp"]
enabled = true

[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
enabled = false

[[skills.config]]
path = ".agents/skills/frontend-production-workflow/SKILL.md"
enabled = true
```

## Orchestrator Flow

The main agent should run this sequence.

```text
1. Inspect
   - package manager
   - React/Vite/Tailwind/shadcn setup
   - scripts
   - existing components
   - PRODUCT.md/DESIGN.md/AGENTS.md

2. Classify work
   - Existing project adoption
   - New project bootstrap
   - New feature development
   - Component refactor
   - Review only

3. Create work order
   - target files
   - allowed files
   - forbidden files
   - component layer
   - states to support
   - validation required

4. Delegate if useful
   - editor for bounded implementation
   - reviewers for independent risk checks

5. Integrate
   - accept/reject findings
   - apply final fixes
   - keep architecture coherent

6. Validate
   - lint
   - typecheck
   - tests
   - build
   - browser/a11y checks when relevant

7. Report
   - changed files
   - validation
   - remaining risks
   - follow-ups
```

## Existing Project Adoption

Start with an audit. Do not mass-refactor first.

```text
Prompt:

Use the frontend-production-workflow skill. Audit this existing React/Vite/shadcn project.
Do not edit product code yet.

Return:
1. Current frontend structure.
2. shadcn/Tailwind setup.
3. Existing scripts and validation gaps.
4. Top 10 frontend quality risks.
5. Proposed .codex/agents and skill setup.
6. First low-risk adoption PR.
```

Recommended first PR:

- Add `docs/frontend-workflow.md`.
- Add or update `AGENTS.md`.
- Add `.agents/skills/frontend-production-workflow`.
- Add `.codex/agents/*` custom agent files.
- Add validation scripts if missing.
- Do not rewrite existing UI yet.

Then apply the workflow to:

- New feature work.
- Components touched for bugs.
- High-risk shared components.
- High-traffic pages.

## New Project Bootstrap

Start with rules and structure before feature UI.

```text
Prompt:

Use frontend-production-workflow. Bootstrap a new React + Vite + TypeScript + Tailwind + shadcn project.
Set up component layers, AGENTS.md, PRODUCT.md, DESIGN.md placeholders, validation scripts, and custom frontend subagents.
Do not create marketing filler; create the actual app shell.
```

Recommended baseline:

- Vite + React + TypeScript.
- shadcn initialized.
- `components/ui`, `components/common`, `components/layout`, `features`.
- Vitest.
- Playwright.
- ESLint.
- Typecheck.
- Production build script.
- `PRODUCT.md` and `DESIGN.md`.
- Custom agents in `.codex/agents`.

## New Feature Development

Use subagents after the main agent defines the contract.

```text
Prompt:

Use frontend-production-workflow for this new feature.
Main agent should orchestrate.
Use frontend-editor only for bounded edits.
Use react-quality-reviewer, shadcn-reviewer, accessibility-reviewer, vite-performance-reviewer, and design-polish-reviewer for independent review.
The main agent decides which findings to apply.
```

Feature flow:

```text
1. Main agent defines feature contract.
2. Main agent maps components to layers.
3. Main agent writes editor work order.
4. Editor implements.
5. Reviewers inspect diff independently.
6. Main agent reconciles feedback.
7. Editor or main agent applies fixes.
8. Main agent validates and summarizes.
```

## Work Order Template for Editor Agent

```text
You are the frontend-editor.

Task:
[specific implementation]

Allowed files:
- [path]
- [path]

Do not touch:
- [path]
- [path]

Required patterns:
- React + TypeScript.
- shadcn primitives.
- Semantic tokens only.
- No derived-state effects.
- No nested component definitions.
- Static Tailwind class names or variant maps.

States:
- loading:
- empty:
- error:
- disabled:
- success:

Validation:
- Run [commands].

Return:
- changed files
- validation output summary
- risks
```

## Review Prompt Template

```text
You are [reviewer-name].

Review the current diff only for [risk area].
Do not edit files.
Return findings ordered by severity.
Each finding must include:
- file path
- line or symbol
- problem
- why it matters
- suggested fix

If there are no issues, say so and list residual risk.
```

## When Not To Use Subagents

Do not spawn subagents when:

- The change is tiny.
- The next step is blocked on one obvious local investigation.
- Multiple agents would touch the same file without clear ownership.
- The project has no validation baseline yet and the main agent can inspect faster.
- Token/time cost matters more than parallelism.

Use subagents when:

- Reviews are independent.
- Work can be split by file/module.
- Browser/a11y/performance checks can run while the main agent continues.
- The main conversation would otherwise be polluted with logs and exploration.

## Recommended Final System

For your frontend workflow, the best long-term setup is:

```text
Plugin or repo-scoped skill:
  frontend-production-workflow

Project config:
  .codex/config.toml

Project custom agents:
  frontend-editor
  react-quality-reviewer
  shadcn-reviewer
  accessibility-reviewer
  vite-performance-reviewer
  design-polish-reviewer

Project docs:
  AGENTS.md
  PRODUCT.md
  DESIGN.md
  docs/frontend-workflow.md
```

The main agent stays accountable. The editor writes bounded patches. Reviewers inspect specific risks. MCP servers are attached only where useful.

## Official Reference Map

- Codex subagent concepts: `/codex/concepts/subagents.md`
- Codex subagent configuration: `/codex/subagents.md`
- Codex skills: `/codex/skills.md`
- Codex MCP: `/codex/mcp.md`
- Codex plugins: `/codex/plugins.md`
- Codex plugin building: `/codex/plugins/build.md`
- Codex config basics: `/codex/config-basic.md`
- Codex advanced config: `/codex/config-advanced.md`
