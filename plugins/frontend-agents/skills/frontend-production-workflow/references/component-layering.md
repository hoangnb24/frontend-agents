# Component Layering

## Layer 1: shadcn Primitives

Path: `src/components/ui/*`

Purpose:

- Generic primitives copied from shadcn/ui.
- Examples: `Button`, `Dialog`, `Input`, `Card`, `Table`, `Select`, `Tabs`, `Badge`, `Skeleton`.

Rules:

- No business logic.
- No product-specific copy.
- Prefer variants and semantic tokens over one-off classes.
- Preserve accessibility composition.
- Use shadcn CLI dry-run and diff flows for upstream changes.

## Layer 2: Shared App Components

Path: `src/components/common/*` or `src/components/app/*`

Purpose:

- Reusable app-level components.
- Examples: `PageHeader`, `ConfirmDialog`, `DataTableToolbar`, `EmptyResourceState`, `StatusBadge`, `FormSection`.

Rules:

- Accept typed props.
- Do not fetch feature data directly.
- Be reusable across features.
- Expose a small API, not every internal class as a prop.

## Layer 3: Feature Components

Path: `src/features/<feature>/components/*`

Purpose:

- Business-specific UI.
- Examples: `InviteUserDialog`, `BillingPlanCard`, `ProjectMembersTable`, `CouponRedemptionForm`.

Rules:

- Can know domain terms and feature-specific events.
- Compose Layer 1 and Layer 2.
- Keep API calls in hooks, loaders, actions, or service modules when possible.
- Include loading, empty, error, disabled, permission, and success states.

## Layer 4: Route Or Page Composition

Path: project router convention, such as `src/pages/*`, `src/routes/*`, or app-router equivalents.

Purpose:

- Data loading, routing, permissions, high-level layout, and composition.

Rules:

- Avoid large markup-heavy pages.
- Split repeated sections into feature components.
- Keep route-level code splitting in mind for heavy screens.

