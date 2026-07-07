# Build Web Apps Interop

Use this when the installed Build Web Apps plugin is available and the work involves visual creation, redesign, major UI polish, rendered frontend debugging, React/Next.js implementation, shadcn/ui work, or provider-backed frontend integrations.

## Main-Agent Ownership

The main orchestrator owns Build Web Apps usage. Do not create an equal peer "builder" subagent by default.

Main agent responsibilities:

- Decide whether the request triggers Build Web Apps.
- Read the relevant Build Web Apps skill before acting.
- Keep design approval, implementation scope, browser evidence, and final acceptance in one thread.
- Delegate only bounded edits or focused reviews after the Build Web Apps loop has a clear work order or evidence set.
- Merge reviewer findings into the final decision gate.

## Routing

| Request shape | Build Web Apps skill | Local frontend-agents role |
| --- | --- | --- |
| New app, dashboard, game, creative site, hero, redesign, modernization | `build-web-apps:frontend-app-builder` | Main agent drives Image Gen concepting, implementation, Browser/IAB validation, fidelity ledger, then uses reviewers as needed. |
| Rendered UI bug, interaction failure, visual regression, console/runtime issue, responsive breakage | `build-web-apps:frontend-testing-debugging` | Main agent defines the target flow and validates Browser-first; reviewers can inspect accessibility, polish, or performance evidence. |
| React/Next component work or performance-sensitive refactor | `build-web-apps:react-best-practices` | React reviewer checks local code against the same rule families; Vite/perf reviewer checks bundle and runtime risk. |
| shadcn/ui component creation, registry usage, presets, component composition | `build-web-apps:shadcn` | shadcn reviewer verifies CLI usage, registry evidence, composition, tokens, forms, dialogs, and component ownership. |
| Stripe payment, billing, Connect, or marketplace integration | `build-web-apps:stripe-best-practices` | Main agent follows Stripe routing before code; frontend reviewers only assess UI, state, and integration surface quality. |
| Supabase/Postgres schema, query, RLS, or performance work | `build-web-apps:supabase-postgres-best-practices` | Main agent follows database guidance before code; frontend reviewers only assess UI behavior around data states. |

## Required Build Web Apps Behaviors To Preserve

- For new visual surfaces or redesigns, use Image Gen concepting unless the user opts out or the change is a small fix inside an existing design system.
- For full pages, apps, dashboards, games, and product surfaces, design the complete requested surface before coding.
- Treat an accepted concept as the production design spec. Preserve visible copy, hierarchy, layout, palette, typography, assets, density, and responsive behavior.
- For rendered validation, use the Browser plugin / in-app browser first when available. Use Playwright only when Browser is unavailable or blocked, and record why.
- A build passing is not enough for rendered UI work. Verify page identity, nonblank render, no framework overlay, console health, screenshot evidence, and at least one interaction proof.
- For visual work, compare the accepted concept and latest rendered screenshot with `view_image` before final handoff when the concept workflow was used.
- Do not leave QA screenshots, reports, traces, or temporary scripts in the repo unless the user explicitly asks for committed artifacts.

## Delegation Pattern

Use subagents after the main agent has enough context to write a bounded assignment.

- `frontend-editor`: implement a specific slice from the Build Web Apps design system, target flow, or bug fix. The work order must name allowed files and required validation.
- `frontend-architecture-reviewer`: review component ownership, route composition, layering, and reuse after implementation.
- `react-quality-reviewer`: review React state, effects, hooks, memoization, render purity, and behavior tests.
- `shadcn-reviewer`: review shadcn CLI evidence, installed components, composition, semantic tokens, and registry/preset handling.
- `accessibility-reviewer`: review keyboard, focus, labels, names, invalid states, dialogs, and reduced-motion behavior from rendered evidence.
- `vite-performance-reviewer`: review build output, large imports, waterfalls, console/network evidence, and bundle risk.
- `design-polish-reviewer`: review rendered visual quality and responsive behavior, but do not replace the Build Web Apps concept-to-screenshot fidelity gate.

## When Not To Delegate

Keep the work in the main agent when:

- The task is still in concept approval or design-selection mode.
- Browser/IAB setup, screenshots, console logs, and final acceptance evidence are the core work.
- The change is small enough that subagent setup would cost more than direct inspection.
- Multiple agents would need to edit the same files without clear ownership.
- The issue is a provider-routing decision, such as Stripe API selection or Supabase schema/query guidance.

## Final Acceptance

The main agent may accept the work only when:

- The Build Web Apps skill's required evidence has been gathered or a blocker is documented.
- Local reviewer gates have no `Blocked` decisions, no `Blocker` findings, and no unresolved `Major` findings unless the user explicitly accepts the risk.
- Required repo commands pass, or failures are explained as unrelated/external with concrete evidence.
- Any intentional visual or behavior deviations from the accepted concept are listed.
