# Impeccable Workflow

Use Impeccable for design consistency and AI UI review after code structure is sane. It does not replace React correctness, shadcn composition, accessibility, production build, or human product judgment.

Project-local install:

```bash
npx impeccable install
```

Initialize design context:

```text
/impeccable init
```

Expected project files:

```text
PRODUCT.md
DESIGN.md
```

Useful commands:

```text
/impeccable critique <target page or component>
/impeccable polish <target page or component>
/impeccable audit <target page or component>
/impeccable distill <target page or component>
npx impeccable detect src/
```

Use Impeccable for:

- visual hierarchy
- spacing and density
- typography
- color restraint
- interaction states
- UX writing polish
- anti-pattern detection
- product vs brand lane consistency

Do not use Impeccable as source of truth for:

- React state correctness
- shadcn composition correctness
- accessibility compliance gates
- production build health
- bundle and performance gates

