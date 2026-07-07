# Installation

This plugin is tracked inside this workspace:

```text
/Users/themrb/Documents/personal/frontend-agents/plugins/frontend-agents
```

Its repo-local marketplace is:

```text
/Users/themrb/Documents/personal/frontend-agents/.agents/plugins/marketplace.json
```

Register the repo marketplace when you want Codex to see this local catalog:

```bash
codex plugin marketplace add /Users/themrb/Documents/personal/frontend-agents
```

Install the plugin only when you want to use it:

```bash
codex plugin add frontend-agents@frontend-agents-local
```

Then start a new Codex thread so the plugin skills are loaded.

## Custom Agents

The plugin includes agent templates in:

```text
/Users/themrb/Documents/personal/frontend-agents/plugins/frontend-agents/agents
```

This repo also tracks project-scoped agent files in:

```text
/Users/themrb/Documents/personal/frontend-agents/.codex/agents
```

Codex custom agents are standalone TOML files. They load from one of:

```text
~/.codex/agents/
.codex/agents/
```

Use the project-scoped `.codex/agents/` location when the agents should travel with a repo. Use the personal location when the agents are for your own local workflow.

Each agent uses the documented `[[skills.config]]` setting to attach exactly one focused skill. In this repo the paths point at the tracked plugin source, for example:

```toml
[[skills.config]]
path = "plugins/frontend-agents/skills/react-quality-review/SKILL.md"
enabled = true
```

If you copy these agents into another project, either keep the same plugin source path in that project or rewrite the `path` values to wherever that project stores the skill files.

## Validation

Run:

```bash
python3 /Users/themrb/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/themrb/Documents/personal/frontend-agents/plugins/frontend-agents
python3 /Users/themrb/Documents/personal/frontend-agents/plugins/frontend-agents/scripts/validate_bundle.py /Users/themrb/Documents/personal/frontend-agents/plugins/frontend-agents
```
