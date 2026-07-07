# Frontend Skill Resource Index

Created: 2026-07-05

This index maps the research documents from this session into reusable skill materials.

## Source Documents

| Document | Purpose |
| --- | --- |
| `react-vite-shadcn-ai-frontend-workflow.md` | Core frontend workflow for React, Vite, TypeScript, Tailwind, shadcn/ui, AI-generated components, validation, and bad-practice review. |
| `codex-subagent-frontend-quality-system.md` | Codex subagent architecture, custom agent files, skill distribution model, existing project adoption, new project bootstrap, and new feature flow. |
| `frontend-subagent-mcp-and-review-gates.md` | MCP server assignment, agent-local MCP setup, Impeccable polish workflow, and decision-based review gates. |

## Human-Facing Project Docs

Copy or adapt the source documents into:

```text
docs/frontend-workflow.md
docs/frontend-subagents.md
docs/frontend-review-gates.md
```

Use these for onboarding humans, explaining why the workflow exists, and reviewing the full context.

## Skill Bundle Materials

Use smaller excerpts from the source documents inside `.agents/skills`.

```text
.agents/skills/
├── frontend-production-workflow/
│   ├── SKILL.md
│   └── references/
│       ├── expected-workflow.md
│       ├── component-layering.md
│       ├── project-adoption-playbooks.md
│       ├── subagent-orchestration.md
│       ├── mcp-and-review-gates.md
│       └── source-reference-map.md
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

## Mapping

| Target material | Source |
| --- | --- |
| `frontend-production-workflow/SKILL.md` | Condensed from all three source documents. |
| `expected-workflow.md` | `react-vite-shadcn-ai-frontend-workflow.md` Expected Workflow section. |
| `component-layering.md` | `react-vite-shadcn-ai-frontend-workflow.md` Component Layering Standard section. |
| `project-adoption-playbooks.md` | `codex-subagent-frontend-quality-system.md` Existing Project Adoption, New Project Bootstrap, New Feature Development sections. |
| `subagent-orchestration.md` | `codex-subagent-frontend-quality-system.md` Recommended Architecture and Orchestrator Flow sections. |
| `mcp-and-review-gates.md` | `frontend-subagent-mcp-and-review-gates.md` Recommended MCP Assignment and Review Gate System sections. |
| `source-reference-map.md` | Research Links from this index plus official reference maps from all three source documents. |
| `editor-workorder-template.md` | `codex-subagent-frontend-quality-system.md` Work Order Template for Editor Agent section. |
| `architecture-checklist.md` | Frontend Architecture Reviewer material from `frontend-subagent-mcp-and-review-gates.md` plus component layering ownership rules from `react-vite-shadcn-ai-frontend-workflow.md`. |
| `react-quality-rules.md` | React bad-practice and production-readiness material from `react-vite-shadcn-ai-frontend-workflow.md`. |
| `shadcn-quality-rules.md` | shadcn-specific composition, Tailwind token, form, icon, and registry review material from `react-vite-shadcn-ai-frontend-workflow.md`. |
| `accessibility-checklist.md` | Accessibility checklist from both workflow and review-gate documents. |
| `vite-performance-checklist.md` | Vite production, bundle, async, import, and browser-runtime material from the workflow and review-gate documents. |
| `design-polish-checklist.md` | Design Polish Reviewer checklist from `frontend-subagent-mcp-and-review-gates.md`. |
| `impeccable-workflow.md` | Impeccable Skill and CLI section from `frontend-subagent-mcp-and-review-gates.md`. |

## Research Links

Use these links as source references when generating skill reference files.

### React

| Topic | Link |
| --- | --- |
| Keeping components pure | https://react.dev/learn/keeping-components-pure |
| You might not need an effect | https://react.dev/learn/you-might-not-need-an-effect |
| Reusing logic with custom hooks | https://react.dev/learn/reusing-logic-with-custom-hooks |
| `useMemo` reference | https://react.dev/reference/react/useMemo |
| Exhaustive deps lint | https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps |

### Vite And Testing

| Topic | Link |
| --- | --- |
| Vite production build | https://vite.dev/guide/build |
| Vite features and dynamic imports | https://vite.dev/guide/features |
| Testing Library queries | https://testing-library.com/docs/queries/about/ |
| Vitest browser component testing | https://vitest.dev/guide/browser/component-testing |
| Vitest comparisons | https://vitest.dev/guide/comparisons |
| Playwright accessibility testing | https://playwright.dev/docs/accessibility-testing |

### shadcn, Tailwind, And Radix

| Topic | Link |
| --- | --- |
| shadcn/ui docs | https://ui.shadcn.com/docs |
| shadcn CLI v4 changelog | https://ui.shadcn.com/docs/changelog/2026-03-cli-v4 |
| shadcn directory and registry safety | https://ui.shadcn.com/docs/directory |
| shadcn registry docs | https://ui.shadcn.com/docs/registry |
| Tailwind utility styling and reusable components | https://tailwindcss.com/docs/styling-with-utility-classes |
| Tailwind class detection | https://tailwindcss.com/docs/detecting-classes-in-source-files |
| Radix Dialog | https://www.radix-ui.com/primitives/docs/components/dialog |
| Radix Accessibility | https://www.radix-ui.com/primitives/docs/overview/accessibility |

### Impeccable

| Topic | Link |
| --- | --- |
| Impeccable home | https://impeccable.style/ |
| Impeccable docs | https://impeccable.style/docs/ |
| Impeccable command docs | https://impeccable.style/docs/impeccable/ |
| Impeccable getting started | https://impeccable.style/tutorials/getting-started/ |
| Impeccable GitHub repository | https://github.com/pbakaus/impeccable |

### Codex

| Topic | Link |
| --- | --- |
| Codex subagents | https://developers.openai.com/codex/subagents |
| Codex subagent concepts | https://developers.openai.com/codex/concepts/subagents |
| Codex skills | https://developers.openai.com/codex/skills |
| Codex MCP | https://developers.openai.com/codex/mcp |
| Codex plugins | https://developers.openai.com/codex/plugins |
| Build Codex plugins | https://developers.openai.com/codex/plugins/build |
| Codex config basics | https://developers.openai.com/codex/config-basic |
| Codex advanced config | https://developers.openai.com/codex/config-advanced |

### MCP Servers

| MCP | Link | Suggested use |
| --- | --- | --- |
| Playwright MCP | https://playwright.dev/docs/getting-started-mcp | Agent-local rendered UI, accessibility, screenshots, keyboard/mouse checks. |
| Chrome DevTools MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Agent-local performance traces, console/network debugging. |
| Context7 MCP | https://github.com/upstash/context7 | Current framework/library docs for React, Vite, and related tools. |
| GitHub MCP | https://github.com/github/github-mcp-server | Optional PR, issue, CI, release, and remote repo workflows. |
| Sentry MCP | https://mcp.sentry.dev/ | Optional production runtime error evidence. |
| Axe MCP | https://github.com/dequelabs/axe-mcp-server-public | Optional deeper accessibility remediation. |

## Rule

Full documents are for humans. Skill references should be narrow and loaded only when needed by the orchestrator or a specialist sub-agent.
