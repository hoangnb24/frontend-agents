# Editor Work Order Template

```text
You are the frontend-editor.

Task:
[specific implementation]

Allowed files:
- [path]
- [path]

Do not touch:
- [path]
- [path]

Component layer:
[ui primitive | shared app component | feature component | route/page]

Required patterns:
- React + TypeScript.
- shadcn primitives before custom markup.
- Semantic shadcn/Tailwind tokens only.
- No derived-state effects.
- No nested component definitions.
- Static Tailwind class names or explicit variant maps.
- Existing project conventions first.

Functional contract:
- Props:
- Events/callbacks:
- Loading state:
- Empty state:
- Error state:
- Disabled/permission state:
- Success state:
- Keyboard behavior:

Validation:
- Run [commands].

Return:
- Changed files.
- Validation output summary.
- Risks or incomplete evidence.
```

