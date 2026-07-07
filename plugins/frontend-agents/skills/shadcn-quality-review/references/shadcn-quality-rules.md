# shadcn Quality Rules

Review areas:

- Existing shadcn primitives are used before custom markup.
- Primitive composition preserves required parts such as `DialogTitle`, `CardHeader`, `TabsList`, menu groups, avatar fallback, and form field structure.
- Forms use project shadcn form/field patterns with labels, descriptions, invalid states, and disabled states.
- Dialogs, sheets, and drawers include accessible titles and expected focus behavior.
- Standard primitives are used for common states: `Alert`, `Badge`, `Skeleton`, `Separator`, empty states, status indicators, and toasts.
- Semantic tokens are used instead of raw color drift.
- Tailwind class names are complete and statically detectable.
- Dynamic class names use explicit maps or variants.
- `className` is mostly layout and spacing, not component restyling.
- Icon library matches the project convention from shadcn info or existing code.
- Third-party registry code is treated as untrusted source and reviewed before acceptance.

Blockers:

- Dialog, sheet, drawer, or modal lacks an accessible title.
- Form control lacks a label or accessible name.
- Custom overlay replaces shadcn/Radix behavior without focus and keyboard support.
- Dynamic Tailwind construction can remove production styles.
- Raw color drift creates an inconsistent or inaccessible state.

