# Design Polish Checklist

Review areas:

- Product audience and task density are respected.
- Visual hierarchy makes the primary workflow obvious.
- Spacing is consistent and not arbitrary.
- Typography fits the container and does not use oversized display type inside compact UI.
- Text does not clip, overlap, or overflow in common desktop and mobile viewports.
- Layout remains coherent at responsive breakpoints.
- Loading, empty, error, disabled, and success states look deliberate.
- Controls use familiar component patterns and icons where appropriate.
- Design-system tokens and component variants are used consistently.
- The UI does not show common AI-generated artifacts: generic card grids, decorative blobs, weak information density, random gradients, inconsistent radii, or placeholder-like copy.

Blockers:

- Text overlaps or is clipped in a common viewport.
- Primary workflow is visually hidden or confusing.
- Layout breaks on mobile or desktop.
- Required state is visually indistinguishable from normal state.
- Contrast or hierarchy makes a critical action hard to perceive.

Evidence gates:

- Missing rendered evidence for visual UI work usually means `Blocked` if visual validation is required.
- Missing `PRODUCT.md` is `Advisory` unless product context is essential to judging the change.
- Missing `DESIGN.md` after an established visual system exists is `Advisory`.

