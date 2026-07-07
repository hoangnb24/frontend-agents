# React, Vite, shadcn/ui, and AI Frontend Workflow

Research date: 2026-07-05

This workflow is for teams using React, Vite, Tailwind, shadcn/ui, and AI-generated code. The goal is to make AI output reusable, scalable, accessible, and reviewable instead of accepting visually plausible but fragile components.

## Expected Workflow

Use this sequence for every new screen, component, or AI-generated UI change.

1. Define the UI contract
   - What is the user trying to do?
   - What data enters the component?
   - What events leave the component?
   - What loading, empty, error, disabled, and permission states must exist?
   - Is this a primitive UI component, shared app component, feature component, or page?

2. Inspect the existing design system
   - Run `npx shadcn@latest info --json`.
   - Check existing `components/ui`, shared components, theme tokens, icon library, and aliases.
   - Use existing shadcn components before creating custom markup.
   - Run `npx shadcn@latest docs <component>` for every shadcn component being used.

3. Generate or implement the first version
   - Ask AI to produce a small, typed component with explicit props.
   - Tell AI which shadcn primitives, tokens, and folder layer to use.
   - Forbid raw colors, dynamic Tailwind class construction, nested components, and unnecessary `useEffect`.

4. Refactor into the right layers
   - Keep `components/ui/*` generic.
   - Put reusable app components in `components/common/*`.
   - Put business-specific UI in `features/<feature>/components/*`.
   - Keep route/page files mostly as composition, data wiring, and layout.
   - Extract hooks only for reusable behavior, not just to hide complexity.

5. Run the acceptance checklist
   - React: pure render, minimal state, no derived-state effects, no nested component definitions.
   - shadcn: correct composition, semantic tokens, accessible labels/titles, standard loading/empty/error components.
   - Tailwind: complete static class names, no conflicting class soup, no raw color drift.
   - Accessibility: keyboard navigation, labels, focus management, visible focus, screen-reader names.
   - Performance: no avoidable waterfalls, route-level splitting for heavy screens, no accidental huge imports.

6. Test behavior, not implementation
   - Unit tests for pure utilities and hooks.
   - Component tests for props, user interactions, loading, empty, error, and disabled states.
   - End-to-end tests for critical user journeys.
   - Accessibility scan for important pages and interactive states.

7. Build and inspect production output
   - Run `npm run lint`, `npm run typecheck`, `npm run test`, and `npm run build`.
   - Inspect Vite build warnings, chunk sizes, and dynamic import behavior.
   - Fix chunk preload errors and HTML cache settings where deployment can leave users on old chunks.

8. Design review and polish
   - Use Impeccable after code structure is sane, not as a substitute for engineering review.
   - Run `/impeccable init` once per project so `PRODUCT.md` and `DESIGN.md` exist.
   - Use `/impeccable critique`, `/impeccable polish`, `/impeccable distill`, or `npx impeccable detect src/` for design consistency and common AI UI anti-patterns.

9. Merge only when the component is documented enough to reuse
   - Export from the right location.
   - Add usage examples if the component is shared.
   - Document variants and ownership.
   - Avoid adding a shared abstraction until there are at least two credible uses or a strong design-system reason.

## Component Layering Standard

### Layer 1: shadcn primitives

Path: `src/components/ui/*`

Purpose:
- Generic primitives copied from shadcn/ui.
- Examples: `Button`, `Dialog`, `Input`, `Card`, `Table`, `Select`, `Tabs`, `Badge`, `Skeleton`.

Rules:
- Do not add business logic here.
- Do not hardcode product-specific copy.
- Prefer variants and semantic tokens over one-off classes.
- Keep accessibility composition intact.
- If updating from upstream, use the shadcn CLI dry-run and diff flow rather than raw copy/paste.

### Layer 2: shared app components

Path: `src/components/common/*` or `src/components/app/*`

Purpose:
- Reusable components with app-level conventions.
- Examples: `PageHeader`, `ConfirmDialog`, `DataTableToolbar`, `EmptyResourceState`, `StatusBadge`, `FormSection`.

Rules:
- Accept typed props.
- Do not fetch feature data directly.
- Be reusable across features.
- Expose a small API, not every internal class as a prop.

### Layer 3: feature components

Path: `src/features/<feature>/components/*`

Purpose:
- Business-specific UI.
- Examples: `InviteUserDialog`, `BillingPlanCard`, `ProjectMembersTable`, `CouponRedemptionForm`.

Rules:
- Can know domain terms and feature-specific events.
- Should still compose Layer 1 and Layer 2.
- Keep API calls in hooks or route-level loaders where possible.
- Include loading, empty, error, and disabled states.

### Layer 4: route/page composition

Path depends on router: `src/pages/*`, `src/routes/*`, or equivalent.

Purpose:
- Data loading, routing, permissions, high-level layout, and composition.

Rules:
- Avoid large markup-heavy pages.
- Split repeated sections into feature components.
- Keep route-level code splitting in mind for heavy screens.

## AI Prompt Template

Use this when asking AI to create or modify frontend code:

```text
Build this as production React + Vite + TypeScript using shadcn/ui.

Context:
- Component layer: [ui primitive | shared app component | feature component | route/page]
- Target path: [path]
- Existing primitives to use: [Button, Dialog, Field, Input, Card, Table, etc.]
- Icon library from shadcn info: [lucide/tabler/etc.]
- Design tokens: use semantic shadcn/Tailwind tokens only.

Functional contract:
- Props:
- Events/callbacks:
- Loading state:
- Empty state:
- Error state:
- Disabled/permission state:
- Keyboard behavior:

Hard rules:
- Do not use raw Tailwind colors like bg-blue-500 unless this project has an approved token for it.
- Do not build custom versions of shadcn primitives.
- Do not define components inside components.
- Do not use useEffect for values that can be derived during render.
- Do not dynamically construct Tailwind class names like bg-${color}-500.
- Use complete static class names or variant maps.
- Use shadcn composition correctly: DialogTitle, CardHeader, SelectGroup, TabsList, AvatarFallback, etc.
- Add accessible labels and names for controls.
- Keep the component small; extract helper components only when they are reusable or clarify structure.

Validation:
- Include the tests or checklist needed to prove this works.
```

## Bad Practices and Fixes

### 1. One giant AI-generated component

Bad:
- 300+ lines.
- Fetches data.
- Owns form state.
- Renders layout.
- Contains modal logic.
- Defines helper components inside itself.
- Uses many hardcoded styles.

Fix:
- Move domain API logic into a hook or route loader.
- Extract feature subcomponents.
- Keep the page as composition.
- Move reusable UI to shared components only if it has a real reuse case.

### 2. `useEffect` for derived state

Bad:
```tsx
const [fullName, setFullName] = useState("")

useEffect(() => {
  setFullName(firstName + " " + lastName)
}, [firstName, lastName])
```

Good:
```tsx
const fullName = `${firstName} ${lastName}`
```

React's guidance is clear: if there is no external system, you usually do not need an effect. Calculate display values during render.

### 3. Ignoring hook dependency lint

Bad:
```tsx
useEffect(() => {
  fetchUser(userId)
}, [])
```

Good:
```tsx
useEffect(() => {
  fetchUser(userId)
}, [userId])
```

If adding dependencies causes loops, restructure the code. Do not silence the linter as a default response.

### 4. Defining components inside components

Bad:
```tsx
function Profile({ user }) {
  function Avatar() {
    return <img src={user.avatarUrl} alt="" />
  }

  return <Avatar />
}
```

Good:
```tsx
function Avatar({ src }: { src: string }) {
  return <img src={src} alt="" />
}

function Profile({ user }: { user: User }) {
  return <Avatar src={user.avatarUrl} />
}
```

Nested component definitions create a new component type on every render, which can remount children and lose focus/state.

### 5. Dynamic Tailwind class construction

Bad:
```tsx
<div className={`bg-${status}-500`} />
```

Good:
```tsx
const statusClass = {
  success: "bg-success text-success-foreground",
  warning: "bg-warning text-warning-foreground",
  danger: "bg-destructive text-destructive-foreground",
}[status]

<div className={statusClass} />
```

Tailwind scans source as text, so classes must exist in full at build time.

### 6. Raw design drift

Bad:
```tsx
<div className="bg-blue-500 text-white dark:bg-blue-300">
```

Good:
```tsx
<div className="bg-primary text-primary-foreground">
```

In shadcn projects, use semantic tokens and variants. Add project tokens deliberately when the design system needs new meaning.

### 7. Rebuilding primitives manually

Bad:
```tsx
<div className="fixed inset-0 z-[999]">
  <div role="dialog">...</div>
</div>
```

Good:
```tsx
<Dialog>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Edit profile</DialogTitle>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

Use shadcn/Radix primitives because they encode focus management, keyboard behavior, roles, and expected composition.

### 8. Custom loading, empty, and status markup everywhere

Bad:
```tsx
<div className="animate-pulse h-4 w-40 rounded bg-gray-200" />
<span className="rounded-full bg-green-100 px-2 text-green-700">Active</span>
```

Good:
```tsx
<Skeleton className="h-4 w-40" />
<Badge variant="secondary">Active</Badge>
```

Use standard primitives so the product feels consistent.

### 9. Testing CSS classes instead of behavior

Bad:
```tsx
expect(button).toHaveClass("bg-primary")
```

Better:
```tsx
await user.click(screen.getByRole("button", { name: /save/i }))
expect(onSave).toHaveBeenCalled()
```

Tests should resemble how users interact with the UI. Use accessible queries first.

### 10. Treating registry code as trusted

Bad:
- Add a third-party shadcn block.
- Commit it immediately.

Good:
- Add it with explicit registry.
- Read every added file.
- Fix imports to match project aliases.
- Replace icon library if needed.
- Check composition, accessibility, dynamic Tailwind, and dependency changes.

shadcn's registry docs explicitly warn that community registry code is third-party code and should be reviewed.

## Production Readiness Checklist

### Component contract

- Props are typed and minimal.
- Events are named by domain action, for example `onInvite`, `onArchive`, `onSave`.
- Component does not mutate props or external objects during render.
- Component has clear loading, empty, error, disabled, and success states.
- Component does not fetch data unless its layer explicitly owns data.

### React correctness

- Render logic is pure.
- Derived values are calculated during render.
- Effects are only for external synchronization: network, subscriptions, timers, browser APIs, non-React widgets.
- Hook dependency lint is obeyed.
- Expensive calculations use `useMemo` only after measurement or a clear reason.
- No nested component definitions.
- Lists have stable keys from data IDs, not array indexes when order can change.

### shadcn and Tailwind consistency

- Existing primitives are used first.
- `className` is mostly layout, not component restyling.
- Raw colors are avoided in favor of semantic tokens.
- Standard primitives are used: `Alert`, `Empty`, `Badge`, `Skeleton`, `Separator`, `sonner`.
- Forms use `FieldGroup`, `Field`, `FieldLabel`, `FieldDescription`, and proper invalid/disabled states.
- Dialog/Sheet/Drawer include accessible titles.
- Select/Menu/Command items are inside their group components.
- Tailwind class names are complete and statically detectable.
- Conflicting utilities are avoided.

### Accessibility

- Interactive elements are native controls or accessible primitives.
- Every form control has a label.
- Icon-only buttons have accessible names.
- Dialogs and sheets have titles and correct focus behavior.
- Keyboard-only operation works.
- Focus is visible.
- Error messages are connected to fields where relevant.
- Reduced-motion behavior is considered for animation-heavy UI.

### Performance

- Independent async work is parallelized with `Promise.all`.
- Heavy routes/components are dynamically imported when appropriate.
- Large libraries are not imported casually into the initial route.
- Bundle warnings are reviewed.
- Vite dynamic import preload errors are handled if the deployment strategy can leave users on old HTML/chunks.
- Production build is tested, not just dev server behavior.

### Tests

- Utilities and hooks: Vitest unit tests.
- UI components: behavior-focused component tests.
- Important pages: Playwright end-to-end tests.
- Accessibility: Playwright + axe for representative pages and revealed UI states.
- Tests use `getByRole`, `getByLabelText`, and user interactions before implementation-specific selectors.

## Recommended Validation Commands

Adapt names to the project scripts:

```bash
npm run lint
npm run typecheck
npm run test
npm run build
npx shadcn@latest info --json
npx shadcn@latest docs button dialog form input select tabs
npx impeccable detect src/
```

For visual and accessibility work:

```bash
npm run dev
npm run test:e2e
```

Add Playwright + axe checks for high-value pages and interactions.

## When To Use Impeccable

Use Impeccable for design consistency and AI UI review, not as the only production-readiness gate.

Best uses:
- Start a project: `/impeccable init`
- Ask for recommendation: `/impeccable`
- Review a rough UI: `/impeccable critique`
- Final design pass: `/impeccable polish`
- Reduce visual noise: `/impeccable distill`
- Browser-based iteration: `/impeccable live`
- PR/CI detector: `npx impeccable detect src/`

What it helps with:
- Product vs brand design context.
- Avoiding common AI frontend tells.
- Enforcing design vocabulary across agents.
- Reading tokens, components, and design rules before making UI changes.

What it does not replace:
- TypeScript correctness.
- React state architecture.
- shadcn composition review.
- Accessibility testing.
- Bundle and production build checks.
- Human product judgment.

## Suggested PR Review Template

```md
## Frontend Review

### Component layer
- [ ] Correct layer: ui/common/feature/page
- [ ] Props and events are typed and minimal
- [ ] No business logic in shared primitives

### React
- [ ] Pure render logic
- [ ] No derived-state effects
- [ ] Hook dependencies are correct
- [ ] No components defined inside components
- [ ] State is minimal and local

### shadcn/Tailwind
- [ ] Existing shadcn primitives used first
- [ ] Semantic tokens used instead of raw colors
- [ ] Correct component composition
- [ ] Static Tailwind classes or variant maps

### Accessibility
- [ ] Labels and accessible names present
- [ ] Keyboard behavior works
- [ ] Dialog/sheet focus behavior works
- [ ] Empty/error/loading/disabled states covered

### Validation
- [ ] lint
- [ ] typecheck
- [ ] tests
- [ ] production build
- [ ] bundle warnings reviewed
- [ ] a11y scan where relevant
```

## Source References

- React: components should be pure and return the same JSX for the same inputs: https://react.dev/learn/keeping-components-pure
- React: effects are for synchronizing with external systems; derived values should usually be calculated during render: https://react.dev/learn/you-might-not-need-an-effect
- React: custom hooks extract reusable behavior between components: https://react.dev/learn/reusing-logic-with-custom-hooks
- React: `useMemo` should be treated as a performance optimization, not a correctness requirement: https://react.dev/reference/react/useMemo
- React ESLint: missing hook dependencies cause stale closures; fighting the linter usually means restructuring: https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps
- Vite: production builds, chunking strategy, and dynamic import preload error handling: https://vite.dev/guide/build
- Vite: dynamic imports and async chunk loading behavior: https://vite.dev/guide/features
- shadcn/ui: open code, composition, distribution, AI-ready components: https://ui.shadcn.com/docs
- shadcn CLI v4: skills, presets, dry run, templates, monorepo, agent-oriented workflows: https://ui.shadcn.com/docs/changelog/2026-03-cli-v4
- shadcn registry: community registry code must be reviewed: https://ui.shadcn.com/docs/directory
- shadcn registry: custom registries can distribute components, hooks, pages, config, and rules: https://ui.shadcn.com/docs/registry
- Tailwind: reuse styles through components in React/Vue/Svelte for repeated cross-file UI: https://tailwindcss.com/docs/styling-with-utility-classes
- Tailwind: class detection is text-based; do not dynamically construct class names: https://tailwindcss.com/docs/detecting-classes-in-source-files
- Radix Dialog: focus trapping, screen reader announcements, title/description, escape behavior: https://www.radix-ui.com/primitives/docs/components/dialog
- Radix Accessibility: WAI-ARIA, focus management, keyboard navigation, labels: https://www.radix-ui.com/primitives/docs/overview/accessibility
- Testing Library: prefer user-facing accessible queries like `getByRole` and `getByLabelText`: https://testing-library.com/docs/queries/about/
- Vitest: component testing focuses on isolated UI behavior and real browser mode catches layout/focus issues: https://vitest.dev/guide/browser/component-testing
- Vitest comparisons: use Vitest for unit/component tests and Playwright for critical browser workflows: https://vitest.dev/guide/comparisons
- Playwright accessibility testing: integrate axe scans, but combine automation with manual assessment: https://playwright.dev/docs/accessibility-testing
- Impeccable: design vocabulary for agents, product/design context, detector, live mode: https://impeccable.style/
- Impeccable command docs: `PRODUCT.md`, `DESIGN.md`, init, critique, polish, live: https://impeccable.style/docs/impeccable/
