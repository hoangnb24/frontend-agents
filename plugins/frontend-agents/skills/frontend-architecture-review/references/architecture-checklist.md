# Frontend Architecture Checklist

Review areas:

- Correct component layer ownership.
- `components/ui` remains generic and product-agnostic.
- Shared app components have small typed APIs and real reuse value.
- Feature components own business-specific UI without leaking into primitives.
- Route/page files stay thin and mostly handle composition, layout, permissions, and data wiring.
- Feature folder structure is discoverable.
- Shared abstractions are justified by reuse or design-system needs.
- Data fetching is owned by route loaders, hooks, actions, or services rather than generic UI.
- Naming matches project conventions.

Blockers:

- Business-specific logic added to `components/ui`.
- Shared abstraction forces unrelated features into one API.
- Page/route becomes the primary implementation with no reusable feature structure.
- Component ownership makes validation, reuse, or future changes materially harder.

