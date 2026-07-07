# Frontend Agents

This repository tracks the local Codex `frontend-agents` plugin source and the research docs it was distilled from.

## Layout

```text
docs/                         # original research documents
plugins/frontend-agents/       # Codex plugin source of truth
.agents/plugins/marketplace.json
.codex/agents/                 # project-scoped custom agents with skills.config
```

## Validate

```bash
scripts/validate-plugin.sh
```

## Make Available In Codex

Register this repo-local marketplace:

```bash
codex plugin marketplace add /Users/themrb/Documents/personal/frontend-agents
```

Install the plugin on demand:

```bash
codex plugin add frontend-agents@frontend-agents-local
```

Start a new Codex thread after installing so the plugin skills are loaded.

## Custom Agents

Plugin-packaged agent templates live under:

```text
plugins/frontend-agents/agents/
```

This repo also tracks active project-scoped copies under:

```text
.codex/agents/
```

Each custom agent uses the documented `[[skills.config]]` setting to attach its focused skill from `plugins/frontend-agents/skills`.
