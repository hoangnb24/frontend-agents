#!/usr/bin/env python3
"""Validate the frontend-agents plugin bundle structure."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_SKILLS = [
    "frontend-production-workflow",
    "frontend-editor-workorder",
    "frontend-architecture-review",
    "react-quality-review",
    "shadcn-quality-review",
    "accessibility-review",
    "vite-performance-review",
    "design-polish-review",
]

REQUIRED_AGENTS = [
    "frontend-editor.toml",
    "frontend-architecture-reviewer.toml",
    "react-quality-reviewer.toml",
    "shadcn-reviewer.toml",
    "accessibility-reviewer.toml",
    "vite-performance-reviewer.toml",
    "design-polish-reviewer.toml",
]

REQUIRED_AGENT_SKILLS = {
    "frontend-editor.toml": "plugins/frontend-agents/skills/frontend-editor-workorder/SKILL.md",
    "frontend-architecture-reviewer.toml": "plugins/frontend-agents/skills/frontend-architecture-review/SKILL.md",
    "react-quality-reviewer.toml": "plugins/frontend-agents/skills/react-quality-review/SKILL.md",
    "shadcn-reviewer.toml": "plugins/frontend-agents/skills/shadcn-quality-review/SKILL.md",
    "accessibility-reviewer.toml": "plugins/frontend-agents/skills/accessibility-review/SKILL.md",
    "vite-performance-reviewer.toml": "plugins/frontend-agents/skills/vite-performance-review/SKILL.md",
    "design-polish-reviewer.toml": "plugins/frontend-agents/skills/design-polish-review/SKILL.md",
}

REQUIRED_REFERENCE_FILES = [
    "skills/frontend-production-workflow/references/expected-workflow.md",
    "skills/frontend-production-workflow/references/component-layering.md",
    "skills/frontend-production-workflow/references/project-adoption-playbooks.md",
    "skills/frontend-production-workflow/references/subagent-orchestration.md",
    "skills/frontend-production-workflow/references/mcp-and-review-gates.md",
    "skills/frontend-production-workflow/references/build-web-apps-interop.md",
    "skills/frontend-production-workflow/references/source-reference-map.md",
    "skills/frontend-editor-workorder/references/editor-workorder-template.md",
    "skills/frontend-architecture-review/references/architecture-checklist.md",
    "skills/react-quality-review/references/react-quality-rules.md",
    "skills/shadcn-quality-review/references/shadcn-quality-rules.md",
    "skills/accessibility-review/references/accessibility-checklist.md",
    "skills/vite-performance-review/references/vite-performance-checklist.md",
    "skills/design-polish-review/references/design-polish-checklist.md",
    "skills/design-polish-review/references/impeccable-workflow.md",
]

REQUIRED_DOCS = [
    "docs/README.md",
    "docs/installation.md",
    "docs/adoption.md",
    "docs/usage.md",
    "docs/source-transformation.md",
    "BUILD_LOG.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def parse_skill_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{path} is missing YAML front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"{path} has malformed front matter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def parse_agent_required_fields(path: Path) -> dict[str, str]:
    text = path.read_text()
    fields: dict[str, str] = {}
    for key in ("name", "description"):
        match = re.search(rf'(?m)^{key}\s*=\s*"([^"]+)"\s*$', text)
        if not match:
            fail(f"{path.name} missing required key {key}")
        fields[key] = match.group(1)
    match = re.search(r'(?ms)^developer_instructions\s*=\s*"""(.*?)"""', text)
    if not match:
        fail(f"{path.name} missing required key developer_instructions")
    fields["developer_instructions"] = match.group(1).strip()
    return fields


def parse_agent_skill_configs(path: Path) -> list[dict[str, str]]:
    text = path.read_text()
    configs: list[dict[str, str]] = []
    for block in re.split(r"(?m)^\s*\[\[skills\.config\]\]\s*$", text)[1:]:
        next_table = re.search(r"(?m)^\s*\[", block)
        body = block[: next_table.start()] if next_table else block
        path_match = re.search(r'(?m)^\s*path\s*=\s*"([^"]+)"\s*$', body)
        enabled_match = re.search(r"(?m)^\s*enabled\s*=\s*(true|false)\s*$", body)
        configs.append(
            {
                "path": path_match.group(1) if path_match else "",
                "enabled": enabled_match.group(1) if enabled_match else "",
            }
        )
    return configs


def main() -> int:
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd().resolve()

    manifest_path = root / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        fail("missing .codex-plugin/plugin.json")
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("name") != "frontend-agents":
        fail("plugin manifest name must be frontend-agents")
    if "[TODO:" in manifest_path.read_text():
        fail("plugin manifest contains TODO placeholder")
    if manifest.get("skills") != "./skills/":
        fail("plugin manifest must point skills to ./skills/")
    if "agents" in manifest:
        fail("plugin manifest must not declare unsupported agents field")

    for skill_name in REQUIRED_SKILLS:
        skill_path = root / "skills" / skill_name / "SKILL.md"
        if not skill_path.is_file():
            fail(f"missing skill {skill_name}")
        fields = parse_skill_front_matter(skill_path)
        if fields.get("name") != skill_name:
            fail(f"{skill_path} has wrong skill name")
        description = fields.get("description", "")
        if len(description) < 40:
            fail(f"{skill_path} description is too short for reliable triggering")

    for rel_path in REQUIRED_REFERENCE_FILES:
        path = root / rel_path
        if not path.is_file():
            fail(f"missing reference file {rel_path}")
        if path.stat().st_size < 120:
            fail(f"reference file {rel_path} is unexpectedly small")

    for agent_file in REQUIRED_AGENTS:
        path = root / "agents" / agent_file
        if not path.is_file():
            fail(f"missing agent file {agent_file}")
        data = parse_agent_required_fields(path)
        text = path.read_text()
        if "/.codex/plugins/cache/" in text:
            fail(f"{agent_file} must not reference plugin cache paths")
        for key in ("name", "description", "developer_instructions"):
            if key not in data or not str(data[key]).strip():
                fail(f"{agent_file} missing required key {key}")
        if data["name"] == "frontend-architect-reviewer":
            fail("agent should use frontend-architecture-reviewer name")
        configs = parse_agent_skill_configs(path)
        if len(configs) != 1:
            fail(f"{agent_file} must declare exactly one [[skills.config]] block")
        expected_path = REQUIRED_AGENT_SKILLS[agent_file]
        if configs[0]["path"] != expected_path:
            fail(f"{agent_file} skill path must be {expected_path}")
        if configs[0]["enabled"] != "true":
            fail(f"{agent_file} skill config must set enabled = true")
        if not (root.parent.parent / expected_path).is_file():
            fail(f"{agent_file} references missing skill path {expected_path}")

    project_agents_dir = root.parent.parent / ".codex" / "agents"
    if project_agents_dir.is_dir():
        for agent_file in REQUIRED_AGENTS:
            project_agent = project_agents_dir / agent_file
            if not project_agent.is_file():
                fail(f"missing project-scoped agent copy .codex/agents/{agent_file}")
            if project_agent.read_text() != (root / "agents" / agent_file).read_text():
                fail(f".codex/agents/{agent_file} must match plugins/frontend-agents/agents/{agent_file}")

    for rel_path in REQUIRED_DOCS:
        if not (root / rel_path).is_file():
            fail(f"missing doc/log {rel_path}")

    print(f"frontend-agents bundle validation passed: {root}")
    print(f"skills={len(REQUIRED_SKILLS)} agents={len(REQUIRED_AGENTS)} references={len(REQUIRED_REFERENCE_FILES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
