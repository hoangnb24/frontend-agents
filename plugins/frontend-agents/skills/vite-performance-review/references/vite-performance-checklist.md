# Vite Performance Checklist

Review areas:

- Production build succeeds.
- Vite build warnings are reviewed and understood.
- Large dependencies are not imported casually into initial routes.
- Heavy routes and components are dynamically imported when appropriate.
- Barrel imports do not drag unnecessary code into hot paths.
- Independent async work is parallelized where safe.
- UI does not block interaction with unnecessary synchronous work.
- Dynamic import preload errors are handled if deployment can leave users on old HTML and chunks.
- Browser console and network behavior are clean for the changed route.
- Bundle or chunk changes are justified by feature value.

Blockers:

- Production build fails.
- New dependency dramatically increases initial bundle without justification.
- Runtime chunk/loading error affects a primary route.
- Feature blocks interaction with avoidable synchronous work.
- Async waterfall creates user-visible delay for critical content.

Useful evidence:

- `npm run build` or project equivalent.
- Bundle analyzer output when available.
- Chrome DevTools console/network/performance trace when runtime behavior is in scope.
- Vite config and import graph inspection for chunking and dependency issues.

