# Frontend Agents Plugin

Frontend Agents is a local Codex plugin for production React, Vite, TypeScript, Tailwind, and shadcn/ui frontend work.

It packages:

- Eight focused skills.
- Seven custom agent TOML templates.
- Distilled workflow and reviewer references.
- Adoption and usage docs.
- A bundle validation script.

The default operating model is one accountable main orchestrator, one bounded editor, and specialist read-only reviewers. Review gates are decision-based, not numeric-score based.

## Build Web Apps Interop

When the installed Build Web Apps plugin applies, `frontend-production-workflow` treats it as a main-agent capability rather than a peer subagent. The main agent owns visual concepting, Browser/IAB-first rendered QA, fidelity evidence, and final acceptance, then delegates bounded edits or focused reviews to this plugin's existing editor and reviewer agents.

## What This Plugin Does Not Do

- It does not assume Figma exists in the workflow.
- It does not auto-install custom agent TOMLs from the plugin. Codex currently loads custom agents from `~/.codex/agents/` or `.codex/agents/`, so this repo also tracks project-scoped copies under `.codex/agents/`.
- Each custom agent uses `[[skills.config]]` to attach one focused skill from the tracked plugin source.
- It does not add external publishing or workspace sharing steps.
- It does not add frontend app code to projects.
- It does not replace the official Build Web Apps plugin. It teaches the main workflow how to route to it and how to combine its evidence with local review gates.

## Source Research

The plugin was distilled from the research docs in `/Users/themrb/Documents/personal/frontend-agents/docs/`. Those source files remain unchanged and are the human-facing long-form research record.
