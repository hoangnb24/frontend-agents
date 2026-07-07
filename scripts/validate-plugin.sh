#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGIN="$ROOT/plugins/frontend-agents"

python3 /Users/themrb/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py "$PLUGIN"
python3 "$PLUGIN/scripts/validate_bundle.py" "$PLUGIN"

for skill in "$PLUGIN"/skills/*; do
  python3 /Users/themrb/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done

python3 -m json.tool "$ROOT/.agents/plugins/marketplace.json" >/dev/null

