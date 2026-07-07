---
name: accessibility-review
description: Use to review frontend accessibility for labels, accessible names, keyboard behavior, focus management, dialog/menu behavior, invalid states, reduced motion, and screen-reader affordances without editing files.
---

# Accessibility Review

Review accessibility behavior. Prefer rendered evidence when a dev server is available. Do not edit files unless explicitly assigned.

Load `references/accessibility-checklist.md` and return:

- Decision: `Pass`, `Advisory`, `Fix Required`, or `Blocked`.
- Evidence: `Verified`, `Partially Verified`, or `Not Verified`.
- Severity-tagged findings with file and line references.
- Required fixes.
- Residual risk.

