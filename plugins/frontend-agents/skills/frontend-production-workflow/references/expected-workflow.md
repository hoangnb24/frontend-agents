# Expected Workflow

Use this sequence for new screens, components, refactors, and AI-generated UI changes.

1. Define the UI contract.
   - User goal.
   - Data entering the component.
   - Events leaving the component.
   - Loading, empty, error, disabled, permission, success, and keyboard states.
   - Component layer.

2. Route Build Web Apps work.
   - For new visual surfaces, redesigns, dashboards, games, creative sites, hero work, or major polish, the main agent uses `build-web-apps:frontend-app-builder` before coding.
   - For rendered bugs, interaction failures, responsive issues, console/runtime errors, and UI regressions, the main agent uses `build-web-apps:frontend-testing-debugging`.
   - For React/Next, shadcn, Stripe, or Supabase-specific work, load the matching Build Web Apps skill before implementation or review.
   - Keep Build Web Apps design approval, Browser/IAB evidence, fidelity checks, and final acceptance with the main orchestrator.

3. Inspect the existing design system.
   - Run `npx shadcn@latest info --json` when shadcn is present.
   - Check `components/ui`, shared components, theme tokens, icon library, aliases, and existing layout patterns.
   - Run `npx shadcn@latest docs <component>` for shadcn components being introduced or changed.

4. Implement the first version.
   - Keep components small and typed.
   - Tell any AI/editor which primitives, tokens, and folder layer to use.
   - Forbid raw color drift, dynamic Tailwind construction, nested component definitions, and unnecessary `useEffect`.

5. Refactor into the right layers.
   - Keep `components/ui/*` generic.
   - Put reusable app components under `components/common/*` or `components/app/*`.
   - Put business-specific UI under `features/<feature>/components/*`.
   - Keep route/page files mostly to composition, data wiring, permissions, and layout.

6. Run acceptance review.
   - React: pure render, minimal state, no derived-state effects, correct hook dependencies, stable component boundaries.
   - shadcn/Tailwind: correct primitive composition, semantic tokens, complete static classes, standard loading/empty/error/status primitives.
   - Accessibility: labels, names, keyboard behavior, focus management, visible focus, dialog/menu behavior.
   - Performance: no avoidable waterfalls, controlled imports, route-level splitting where needed, reviewed build warnings.

7. Test behavior.
   - Unit tests for pure utilities and hooks.
   - Component tests for props, states, and user interactions.
   - End-to-end tests for critical journeys.
   - Accessibility scans and manual keyboard checks for important interactive states.

8. Build and inspect production output.
   - Run the repo's lint, typecheck, test, and build scripts.
   - Inspect Vite warnings, chunk sizes, dynamic import behavior, and cache/chunk preload risks.

9. Design polish.
   - Use PRODUCT/DESIGN context when present.
   - Use Impeccable after structure is sane, not as a substitute for engineering review.
   - Check hierarchy, spacing, typography, density, responsive behavior, and state polish.

10. Merge only when reuse is clear.
   - Export from the right location.
   - Document shared component variants and ownership when useful.
   - Avoid shared abstractions until there are at least two credible uses or a strong design-system reason.
