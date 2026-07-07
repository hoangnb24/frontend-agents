#!/usr/bin/env bash
set -euo pipefail

"$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/register-marketplace.sh"
codex plugin add frontend-agents@frontend-agents-local

