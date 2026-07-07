# Accessibility Checklist

Review areas:

- Interactive elements are native controls or accessible primitives.
- Every form control has a visible label or programmatic accessible name.
- Icon-only buttons have accessible names.
- Dialogs, sheets, menus, selects, comboboxes, and popovers have expected roles, focus behavior, escape behavior, and focus restoration.
- Keyboard-only operation reaches and operates all interactive UI.
- Focus is visible and not trapped unexpectedly.
- Error messages are connected to fields when relevant.
- Disabled and invalid states are communicated visually and semantically.
- Reduced-motion behavior is considered for animation-heavy UI.
- Text contrast and responsive layout are acceptable for common states.

Blockers:

- Critical action is mouse-only.
- Modal/dialog traps users or fails focus restoration.
- Form cannot be completed with keyboard or screen reader.
- Icon-only button has no accessible name.
- Error state prevents recovery or is not announced where required.

Evidence:

- Static JSX/HTML review is useful but not enough for complex interactive UI.
- Rendered keyboard and focus checks are required when the change adds or changes dialogs, menus, forms, routing, or complex interactions.
- Automated axe/Playwright scans help, but do not replace manual keyboard and screen-reader semantics review.

