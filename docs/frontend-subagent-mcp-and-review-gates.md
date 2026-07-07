# Frontend Subagent MCP and Review Gate Setup

Validated on: 2026-07-05

This document maps the current MCP servers to frontend sub-agent roles and defines a decision-based review gate so the orchestrator can consistently decide when to send work back to the editor.

## Current MCP Inventory

These MCP servers are currently enabled in this Codex environment.

| MCP server | Status | Transport | Current use | Recommendation |
| --- | --- | --- | --- | --- |
| `shadcn` | enabled | stdio | shadcn registry, component examples, audit checklist | Use for `shadcn-reviewer`; optional for `frontend-editor`. |
| `openaiDeveloperDocs` | enabled | streamable HTTP | Official OpenAI/Codex docs | Use for Codex/OpenAI questions only; not needed for normal frontend review. |
| `deepwiki` | enabled | streamable HTTP | GitHub repo documentation/wiki lookup | Use for library or external repo understanding; optional for architecture/research. |
| `exa` | enabled | streamable HTTP, OAuth | Web/research search | Use only for external research when official docs/MCP are not enough. |
| `morph-mcp` | enabled | stdio | Public GitHub codebase search | Use for upstream dependency code research, not routine local review. |
| `node_repl` | enabled | stdio | Browser automation via in-app browser/Chrome, JS runtime | Use for browser-based UI checks when the browser plugin path is needed. |
| `computer-use` | enabled | stdio | Desktop UI control | Keep out of routine frontend review; use only when a real desktop app interaction is required. |

Current global custom agents:

| Agent | Current note |
| --- | --- |
| `docs_researcher` | Uses `openaiDeveloperDocs` and agent-local `MCP_DOCKER`. Good for docs verification, but not specific enough for frontend quality. |
| `explorer` | Read-only codebase explorer. References agent-local `gkg`. Useful for project discovery, but not a replacement for focused frontend reviewers. |
| `reviewer` | General PR reviewer. Useful as a fallback, but frontend workflow needs narrower reviewers. |

Important config observation:

- Global `~/.codex/config.toml` has `morph-mcp`, `exa`, `deepwiki`, `openaiDeveloperDocs`, and `node_repl`.
- `codex mcp list` also shows plugin-provided `computer-use` and `shadcn`.
- `MCP_DOCKER` and `gkg` are commented out globally but appear inside existing custom agent files, so treat them as agent-local experiments unless validated in that agent.

## Recommended MCP Assignment

Do not give every agent every MCP server. Each agent should have only the tools it needs.

| Sub-agent | MCP servers | Why |
| --- | --- | --- |
| `frontend-editor` | `shadcn` optional | Editor should mostly use local files and the orchestrator work order. `shadcn` is useful when adding/verifying components. |
| `frontend-architect-reviewer` | `context7` optional; `deepwiki` optional | Most architecture review is local structure. Use docs only for framework/library architecture decisions. |
| `react-quality-reviewer` | `context7` optional; `deepwiki` or `morph-mcp` optional | Most React quality review is local code. Use Context7 for current React/library docs and external tools only for upstream behavior questions. |
| `shadcn-reviewer` | `shadcn` | Primary reviewer for shadcn registry, examples, add commands, and component audit checklist. |
| `accessibility-reviewer` | `playwright` agent-local; `axe` optional later | Needs rendered UI, keyboard/focus checks, screenshots, and accessibility tree snapshots. Current global setup has `node_repl`, but Playwright MCP should be attached to this agent specifically. |
| `vite-performance-reviewer` | `chrome-devtools` agent-local; `context7` optional; `morph-mcp` optional | Needs console/network/performance traces, build output, dependency behavior research, and Vite docs when necessary. |
| `design-polish-reviewer` | `playwright` agent-local; `impeccable` skill/CLI; `chrome-devtools` optional | Needs screenshots/rendered UI, responsive behavior, project design context, and deterministic design anti-pattern checks. Figma is intentionally excluded from this workflow. |
| `docs-researcher` | `openaiDeveloperDocs`, `exa`, `deepwiki`, `morph-mcp` | Use as a sidecar for official docs or external research, not as a default reviewer. |

## Recommended Additions

The current setup is enough to start, but agent-local MCP additions would improve frontend review quality.

Use these inside specific custom agent TOML files instead of adding them globally.

### Playwright MCP

```toml
[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]
enabled = true
```

Use for:

- `accessibility-reviewer`
- `design-polish-reviewer`
- `frontend-editor` only when the work order explicitly asks it to verify rendered behavior.

### Chrome DevTools MCP

```toml
[mcp_servers.chrome-devtools]
command = "npx"
args = ["-y", "chrome-devtools-mcp@latest", "--no-usage-statistics", "--no-performance-crux"]
enabled = true
```

Use for:

- `vite-performance-reviewer`
- `design-polish-reviewer` only when console/network evidence is needed.

### Context7 MCP

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"
enabled = true
```

Use for:

- `react-quality-reviewer`
- `vite-performance-reviewer`
- `frontend-architect-reviewer`

If higher rate limits are needed, add the Context7 API key through the supported header/env pattern in the team's Codex config.

### Optional: GitHub MCP

Only add GitHub MCP for agents that need PR, issue, CI, or remote repository context. Do not attach it to normal frontend reviewers by default.

Use for:

- `github-pr-reviewer`
- `ci-diagnostics-reviewer`
- `release-readiness-reviewer`

Prefer read-only/toolset-limited configuration.

### Optional: Sentry MCP

Only add Sentry MCP if the project uses Sentry and the task involves production error evidence.

Use for:

- `production-runtime-reviewer`
- `bug-regression-reviewer`

Do not attach Sentry to design, shadcn, or routine React review agents.

### Optional: Axe MCP

Deque's Axe MCP can be useful for enterprise accessibility remediation. For the default setup, start with Playwright MCP and in-repo axe tests. Add Axe MCP only when the team wants dedicated rendered accessibility scans and remediation guidance.

Use for:

- `accessibility-reviewer`

### Impeccable Skill and CLI

Impeccable should be attached to `design-polish-reviewer` as a skill/CLI workflow, not as an MCP server.

Install project-local:

```bash
npx impeccable install
```

Initialize design context:

```text
/impeccable init
```

Expected project files:

```text
PRODUCT.md
DESIGN.md
```

Recommended polish-agent commands:

```text
/impeccable critique <target page or component>
/impeccable polish <target page or component>
/impeccable audit <target page or component>
npx impeccable detect src/
```

Use Impeccable for:

- visual hierarchy
- spacing and density
- typography
- color restraint
- interaction states
- UX writing polish
- anti-pattern detection
- brand vs product lane consistency

Do not use Impeccable as the source of truth for:

- React state correctness
- shadcn composition correctness
- accessibility compliance gates
- production build health
- bundle/performance gates

Those stay owned by the specialist reviewers.

## Agent Skill Structure

Use dedicated reviewer skills. Keep the orchestrator skill separate.

```text
.agents/skills/
├── frontend-production-workflow/
│   ├── SKILL.md
│   └── references/
│       ├── expected-workflow.md
│       ├── component-layering.md
│       ├── project-adoption-playbooks.md
│       ├── subagent-orchestration.md
│       └── mcp-and-review-gates.md
├── frontend-editor-workorder/
│   ├── SKILL.md
│   └── references/
│       └── editor-workorder-template.md
├── frontend-architecture-review/
│   ├── SKILL.md
│   └── references/
│       └── architecture-checklist.md
├── react-quality-review/
│   ├── SKILL.md
│   └── references/
│       └── react-quality-rules.md
├── shadcn-quality-review/
│   ├── SKILL.md
│   └── references/
│       └── shadcn-quality-rules.md
├── accessibility-review/
│   ├── SKILL.md
│   └── references/
│       └── accessibility-checklist.md
├── vite-performance-review/
│   ├── SKILL.md
│   └── references/
│       └── vite-performance-checklist.md
└── design-polish-review/
    ├── SKILL.md
    └── references/
        ├── design-polish-checklist.md
        └── impeccable-workflow.md
```

Why:

- The orchestrator skill defines the whole workflow.
- Reviewer skills define narrow decision checklists.
- The editor skill defines how to execute a bounded work order.
- Each sub-agent loads only the knowledge it needs.

## Resource Materials For Skills

Use the documents we created as source material for the skill bundle.

| Existing document | Use as | Target skill material |
| --- | --- | --- |
| `react-vite-shadcn-ai-frontend-workflow.md` | Main frontend workflow, component layering, AI prompt template, bad-practice examples, validation checklist, reference links. | `frontend-production-workflow/references/expected-workflow.md`, `component-layering.md`, `react-quality-review/references/react-quality-rules.md`, `shadcn-quality-review/references/shadcn-quality-rules.md`, `accessibility-review/references/accessibility-checklist.md`, `vite-performance-review/references/vite-performance-checklist.md`. |
| `codex-subagent-frontend-quality-system.md` | Codex subagent architecture, custom agent structure, project adoption, new project bootstrap, feature development flow. | `frontend-production-workflow/references/subagent-orchestration.md`, `project-adoption-playbooks.md`, `frontend-editor-workorder/references/editor-workorder-template.md`. |
| `frontend-subagent-mcp-and-review-gates.md` | MCP assignment, agent-local MCP examples, decision gate, reviewer output format, custom agent TOML examples. | `frontend-production-workflow/references/mcp-and-review-gates.md`, each reviewer `SKILL.md`, and `.codex/agents/*.toml`. |

Recommended project docs:

```text
docs/frontend-workflow.md
docs/frontend-subagents.md
docs/frontend-review-gates.md
```

Recommended skill references:

```text
.agents/skills/frontend-production-workflow/references/expected-workflow.md
.agents/skills/frontend-production-workflow/references/component-layering.md
.agents/skills/frontend-production-workflow/references/project-adoption-playbooks.md
.agents/skills/frontend-production-workflow/references/subagent-orchestration.md
.agents/skills/frontend-production-workflow/references/mcp-and-review-gates.md
.agents/skills/react-quality-review/references/react-quality-rules.md
.agents/skills/shadcn-quality-review/references/shadcn-quality-rules.md
.agents/skills/accessibility-review/references/accessibility-checklist.md
.agents/skills/vite-performance-review/references/vite-performance-checklist.md
.agents/skills/design-polish-review/references/design-polish-checklist.md
.agents/skills/design-polish-review/references/impeccable-workflow.md
```

Keep the full research documents in `docs/` for humans. Keep smaller, task-specific excerpts in skill `references/` so sub-agents do not load irrelevant material.

## Review Gate System

Reviewers do not return numeric scores. They return a decision, severity-tagged findings, evidence, and required fixes.

Decision levels:

| Decision | Meaning | Orchestrator action |
| --- | --- | --- |
| `Blocked` | The reviewer could not complete a necessary review, or found a must-fix issue that prevents safe acceptance. | Send to editor or resolve missing evidence before merge. |
| `Fix Required` | The feature mostly works, but there are blocker or major issues that must be fixed. | Send a precise rework order to the editor. |
| `Advisory` | No merge-blocking issue, but there are minor concerns, polish improvements, or residual risks. | Orchestrator decides whether to fix now or defer. |
| `Pass` | No material issue found in this reviewer’s scope. | No action required. |

Severity levels:

| Severity | Meaning | Required action |
| --- | --- | --- |
| `Blocker` | Must fix before merge; feature is broken, inaccessible, unsafe, or cannot build. | Always fix. |
| `Major` | Serious quality issue; likely bug, regression, production risk, or missing required state. | Fix before merge unless user explicitly accepts risk. |
| `Minor` | Real issue with limited impact. | Fix if local and cheap; otherwise track as follow-up. |
| `Nit` | Polish or maintainability preference. | Optional; do not block merge. |

Evidence quality:

| Evidence status | Meaning | Decision impact |
| --- | --- | --- |
| `Verified` | Reviewer inspected code and ran the relevant command/browser/tool. | Decision can be trusted. |
| `Partially Verified` | Reviewer inspected code but could not run one useful verification path. | Cannot be `Pass`; use `Advisory` or stronger. |
| `Not Verified` | Required evidence was unavailable. | Usually `Blocked` unless that evidence is nonessential. |

Reviewer output format:

```md
## Decision
Decision: Fix Required
Evidence: Verified

## Findings
- [Major] path/to/file.tsx:42 - Problem...
- [Minor] path/to/file.tsx:88 - Problem...

## Evidence
- Reviewed files:
- Commands/tools used:
- States checked:

## Required Fixes
1. ...
2. ...

## Residual Risk
- ...
```

## Reviewer Checklists

### Frontend Architecture Reviewer

Review areas:

- Correct component layer ownership.
- Reuse boundaries and API shape.
- Feature folder structure.
- Route/page composition kept thin.
- Shared abstraction is justified.
- Naming and discoverability.

Blockers:

- Business-specific logic added to `components/ui`.
- Shared abstraction forces unrelated features into one API.
- Page/route becomes the primary implementation with no reusable feature structure.

### React Quality Reviewer

Review areas:

- Pure render logic and no render side effects.
- State is minimal and correctly derived.
- Effects are necessary and dependency-safe.
- Component boundaries avoid remount/focus bugs.
- Lists, keys, callbacks, and memoization are sane.
- Tests cover important state transitions.

Blockers:

- State mutation during render.
- Infinite render/effect loop.
- Form/input loses user data or focus due to remount.
- Hook dependency bug that can use stale critical data.

### shadcn Reviewer

Review areas:

- Correct primitive choice.
- Correct composition.
- Semantic tokens and variants.
- Form patterns and validation states.
- Standard loading/empty/error/status primitives.
- Icon and import conventions.

Blockers:

- Dialog/Sheet/Drawer lacks an accessible title.
- Form control lacks label or accessible name.
- Custom overlay replaces shadcn/Radix behavior without focus/keyboard support.
- Dynamic Tailwind class construction breaks production styles.

### Accessibility Reviewer

Review areas:

- Labels and accessible names.
- Keyboard navigation.
- Focus management and visible focus.
- Dialog/menu/sheet behavior.
- Error messaging and invalid states.
- Motion/contrast/responsiveness checks.

Blockers:

- Critical action is mouse-only.
- Modal/dialog traps users or fails focus restoration.
- Form cannot be completed with keyboard/screen reader.
- Icon-only button has no accessible name.

### Vite Performance Reviewer

Review areas:

- Production build remains healthy.
- Imports and dependencies are controlled.
- Heavy routes/components are split appropriately.
- Async work avoids waterfalls.
- Browser/runtime behavior is stable.
- Bundle warnings are understood.

Blockers:

- Production build fails.
- New dependency dramatically increases initial bundle without justification.
- Runtime chunk/loading error for primary route.
- Feature blocks interaction with unnecessary synchronous work.

### Design Polish Reviewer

Review areas:

- PRODUCT.md and DESIGN.md context used correctly.
- Impeccable critique/audit/detect findings handled.
- Visual hierarchy.
- Spacing and density.
- Typography and copy fit.
- Design-system consistency.
- Responsive layout.
- Loading/empty/error polish.

Blockers:

- Text overlaps or is clipped in common viewport.
- Primary workflow is visually hidden or confusing.
- Layout breaks on mobile or desktop viewport.
- Required state is visually indistinguishable from normal state.

Evidence gates:

| Condition | Decision impact |
| --- | --- |
| `PRODUCT.md` missing | `Advisory` or `Blocked` depending on whether product context is required for the change. |
| `DESIGN.md` missing after an established visual system exists | `Advisory`; request Impeccable initialization or design context update. |
| Impeccable unavailable or not installed | `Advisory`; perform manual review from available context and rendered evidence. |
| `npx impeccable detect src/` finds high-severity anti-patterns | `Fix Required` until handled or explicitly deferred. |
| Rendered screenshot/browser evidence unavailable for visual UI work | `Blocked` if visual validation is required; otherwise `Advisory`. |

## Orchestrator Decision Rules

The orchestrator combines reviewer decisions into a final quality gate.

Recommended merge gate:

| Final condition | Orchestrator action |
| --- | --- |
| Any reviewer decision is `Blocked` | Resolve missing evidence or send to editor. No merge. |
| Any `Blocker` finding | Send to editor. No merge. |
| Any `Major` finding | Send to editor unless user explicitly accepts the risk. |
| Required reviewer evidence is missing | Resolve evidence gap before merge or document why evidence is not required. |
| Only `Minor` or `Nit` findings remain | Orchestrator decides whether to fix now or create follow-up. |
| All relevant reviewers return `Pass` or non-blocking `Advisory` | Accept if validation commands pass. |

Reviewer priority by feature type:

| Feature type | Required reviewers |
| --- | --- |
| UI-heavy customer-facing feature | React, shadcn, accessibility, design polish, Vite performance. |
| Internal dashboard feature | Architecture, React, shadcn, accessibility, Vite performance. |
| Shared component or design-system change | Architecture, React, shadcn, accessibility, design polish. |
| Performance-sensitive route | React, Vite performance, accessibility, shadcn if UI changed. |
| Small copy/layout change | shadcn or design polish only, plus accessibility if interactive UI changed. |

## Editor Rework Loop

The orchestrator should generate a precise rework order from reviewer findings.

```text
Editor rework order:

Goal:
- Resolve all Blocker and Major findings from reviewer output.

Must fix:
- Blocker findings.
- Major findings.
- Missing required evidence.

Should fix:
- Minor findings that are cheap and local.

Do not fix:
- Nit findings unless they are in files already being edited.

Allowed files:
- ...

Do not touch:
- ...

Validation:
- npm run lint
- npm run typecheck
- npm run test
- npm run build
```

Maximum loops:

```text
1st review: full reviewer pass.
1st rework: fix blockers/majors.
2nd review: only reviewers that returned Blocked or Fix Required.
2nd rework: final targeted fixes.
If still Blocked or Fix Required: orchestrator escalates to user with concrete tradeoff.
```

## Recommended Custom Agent Files

### `shadcn-reviewer.toml`

```toml
name = "shadcn-reviewer"
description = "Reviews shadcn/ui composition, Tailwind tokens, forms, dialogs, cards, menus, component reuse, and standard UI states."
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Use the shadcn-quality-review skill.
Review only shadcn/ui and Tailwind consistency.
Do not edit files.
Return Decision, Evidence, severity-tagged findings, required fixes, and residual risk.
Use the shadcn MCP when registry, examples, or component audit guidance is needed.
"""

[mcp_servers.shadcn]
command = "npx"
args = ["shadcn@latest", "mcp"]

[[skills.config]]
path = ".agents/skills/shadcn-quality-review/SKILL.md"
enabled = true
```

### `accessibility-reviewer.toml`

```toml
name = "accessibility-reviewer"
description = "Reviews labels, keyboard behavior, focus management, dialog behavior, and screen-reader names."
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Use the accessibility-review skill.
Do not edit files.
Use rendered evidence when available.
Return Decision, Evidence, severity-tagged findings, required fixes, and residual risk.
If browser evidence is required but unavailable, return Blocked and state what could not be verified.
"""

[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]

[[skills.config]]
path = ".agents/skills/accessibility-review/SKILL.md"
enabled = true
```

### `react-quality-reviewer.toml`

```toml
name = "react-quality-reviewer"
description = "Reviews React state, effects, hooks, render purity, rerender risk, component boundaries, and tests."
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Use the react-quality-review skill.
Review React quality only.
Do not edit files.
Return Decision, Evidence, severity-tagged findings, required fixes, and residual risk.
Prefer concrete code evidence over broad style preference.
"""

[[skills.config]]
path = ".agents/skills/react-quality-review/SKILL.md"
enabled = true
```

### `vite-performance-reviewer.toml`

```toml
name = "vite-performance-reviewer"
description = "Reviews production build, imports, dependencies, async waterfalls, bundle risk, and runtime performance."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
Use the vite-performance-review skill.
Do not edit files.
Return Decision, Evidence, severity-tagged findings, required fixes, and residual risk.
If build output or bundle evidence is required but unavailable, return Blocked and state what could not be verified.
"""

[mcp_servers.chrome-devtools]
command = "npx"
args = ["-y", "chrome-devtools-mcp@latest", "--no-usage-statistics", "--no-performance-crux"]

[[skills.config]]
path = ".agents/skills/vite-performance-review/SKILL.md"
enabled = true
```

### `design-polish-reviewer.toml`

```toml
name = "design-polish-reviewer"
description = "Reviews rendered UI hierarchy, spacing, typography, density, responsiveness, design-system consistency, and Impeccable design-context alignment."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
Use the design-polish-review skill.
Use PRODUCT.md and DESIGN.md when present.
Use the Impeccable skill when installed.
Run or request Impeccable evidence where appropriate:
- /impeccable critique for design review
- /impeccable audit for implementation/design checks
- /impeccable polish for targeted refinement recommendations
- npx impeccable detect src/ for deterministic anti-pattern detection
Do not edit files by default.
Return Decision, Evidence, severity-tagged findings, required fixes, and residual risk.
If rendered UI screenshots are required but unavailable, return Blocked and state what could not be verified.
If PRODUCT.md is missing, return Advisory or Blocked depending on whether product context is required, and ask the orchestrator to run /impeccable init.
If Impeccable is unavailable, return Advisory and perform a manual visual review from PRODUCT.md/DESIGN.md plus rendered evidence.
"""

[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]

[[skills.config]]
path = ".agents/skills/design-polish-review/SKILL.md"
enabled = true

# Enable this after `npx impeccable install` confirms the project-local path.
# The installer may choose the correct Codex skill location for the current harness.
#
# [[skills.config]]
# path = ".agents/skills/impeccable/SKILL.md"
# enabled = true
```

## Prompt To Use The System

```text
Use frontend-production-workflow.

Main agent should orchestrate.
Use frontend-editor only for bounded edits.
Use reviewer subagents with decision-based review gates:
- frontend-architecture-reviewer
- react-quality-reviewer
- shadcn-reviewer
- accessibility-reviewer
- vite-performance-reviewer
- design-polish-reviewer

Reviewer output must include:
- Decision: Pass / Fix Required / Blocked
- Evidence: Verified / Partially Verified / Not Verified
- Severity-tagged findings
- Evidence reviewed
- Required fixes

Acceptance gate:
- No Blocked reviewer decisions
- No Blocker findings
- No unresolved Major findings unless user explicitly accepts the risk
- Required validation commands pass
- Missing evidence is resolved or explicitly documented as not required

The orchestrator decides which findings to apply and sends one precise rework order to the editor.
```

## Research Notes

- Playwright MCP is the right fit for accessibility and user-flow review because it operates through structured accessibility snapshots, supports common browser interactions, screenshots, keyboard/mouse actions, and works with MCP clients including Codex.
- Chrome DevTools MCP is the right fit for performance review because it exposes console/network debugging and performance trace tooling, including trace start/stop and performance insight analysis.
- Context7 is the right fit for framework/library documentation because it fetches current code examples and version-specific docs into the agent context.
- shadcn MCP is already installed and is the best fit for shadcn registry/component review.
- Impeccable is the right fit for the design-polish reviewer because it installs as a design skill plus CLI workflow, creates `PRODUCT.md` and `DESIGN.md`, offers `critique`, `audit`, `polish`, and `detect`, and targets visual quality/AI design anti-patterns.
- GitHub MCP is useful for PR, issue, CI, and remote repository workflows, but should be read-only or toolset-limited and should not be attached to routine frontend reviewers.
- Sentry MCP is useful only when production runtime evidence matters.
- Figma MCP is intentionally excluded because this workflow does not use Figma.
