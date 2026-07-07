---
name: react-quality-review
description: Use to review React code for render purity, state, effects, hooks, dependencies, component boundaries, rerender risk, stale closures, and behavior-focused tests without editing files.
---

# React Quality Review

Review React quality only. Prefer concrete code evidence over broad style preference.

Load `references/react-quality-rules.md` and return:

- Decision: `Pass`, `Advisory`, `Fix Required`, or `Blocked`.
- Evidence: `Verified`, `Partially Verified`, or `Not Verified`.
- Severity-tagged findings with file and line references.
- Required fixes.
- Residual risk.

