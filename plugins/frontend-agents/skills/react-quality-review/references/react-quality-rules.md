# React Quality Rules

Review areas:

- Render logic is pure and deterministic for the same inputs.
- Component does not mutate props, external objects, stores, refs, or browser state during render.
- State is minimal and not duplicated from props or derived values.
- Derived values are calculated during render instead of stored through effects.
- Effects synchronize with external systems only: network, subscriptions, timers, browser APIs, or non-React widgets.
- Hook dependency lint is obeyed; stale closures are not hidden by disabling lint.
- Components are not defined inside components.
- Lists use stable keys from data IDs when order can change.
- `useMemo` is used as an optimization only when there is a measured or clear reason.
- Tests assert behavior with user-facing queries and interactions, not internal implementation details.

Common blockers:

- State mutation during render.
- Infinite render or effect loop.
- Form/input loses data or focus due to remount.
- Hook dependency bug can use stale critical data.
- Derived-state effect causes flicker, stale display, or unnecessary extra render.

Preferred fixes:

- Calculate derived display values during render.
- Move reusable behavior to custom hooks only when behavior is reused or clarified.
- Move nested components to module scope and pass explicit props.
- Restructure effects instead of suppressing dependency lint.
- Use Testing Library accessible queries such as `getByRole` and `getByLabelText`.

