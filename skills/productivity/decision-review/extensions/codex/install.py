#!/usr/bin/env python3
"""Install Decision Review hooks into the current user's Codex CLI config."""
import json
import os
import sys
from pathlib import Path

home = Path.home()
config = home / ".codex" / "hooks.json"
script = Path(__file__).resolve().parent / "pre_edit.py"
config.parent.mkdir(parents=True, exist_ok=True)
try:
    data = json.loads(config.read_text()) if config.exists() else {"hooks": {}}
except json.JSONDecodeError as exc:
    sys.exit(f"Invalid JSON in {config} at line {exc.lineno}, column {exc.colno}; fix it and rerun the installer.")
if not isinstance(data, dict):
    sys.exit(f"Invalid Codex hooks config in {config}: expected a JSON object at the top level.")
hooks = data.setdefault("hooks", {})
if not isinstance(hooks, dict):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks' must be a JSON object.")
entry = {
    "matcher": "apply_patch",
    "hooks": [{"type": "command", "command": f'python3 "{script}"', "timeout": 10}],
}
existing = hooks.setdefault("PreToolUse", [])
if not isinstance(existing, list):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks.PreToolUse' must be a list.")
if any(not isinstance(e, dict) or not isinstance(e.get("hooks", []), list) or any(not isinstance(h, dict) for h in e.get("hooks", [])) for e in existing):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks.PreToolUse' has an invalid structure.")
if not any(any(str(script) in h.get("command", "") for h in e.get("hooks", [])) for e in existing):
    existing.append(entry)
prompt_entry = {"hooks": [{"type": "command", "command": f'python3 "{script}"', "timeout": 10}]}
prompts = hooks.setdefault("UserPromptSubmit", [])
if not isinstance(prompts, list):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks.UserPromptSubmit' must be a list.")
if any(not isinstance(e, dict) or not isinstance(e.get("hooks", []), list) or any(not isinstance(h, dict) for h in e.get("hooks", [])) for e in prompts):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks.UserPromptSubmit' has an invalid structure.")
if not any(any(str(script) in h.get("command", "") for h in e.get("hooks", [])) for e in prompts):
    prompts.append(prompt_entry)
stops = hooks.setdefault("Stop", [])
if not isinstance(stops, list):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks.Stop' must be a list.")
if any(not isinstance(e, dict) or not isinstance(e.get("hooks", []), list) or any(not isinstance(h, dict) for h in e.get("hooks", [])) for e in stops):
    sys.exit(f"Invalid Codex hooks config in {config}: 'hooks.Stop' has an invalid structure.")
stop_entry = {"hooks": [{"type": "command", "command": f'python3 "{script}"', "timeout": 10}]}
if not any(any(str(script) in h.get("command", "") for h in e.get("hooks", [])) for e in stops):
    stops.append(stop_entry)
tmp = config.with_suffix(".json.tmp")
tmp.write_text(json.dumps(data, indent=2) + "\n")
os.chmod(tmp, 0o600)
tmp.replace(config)
print(f"Installed Decision Review Plan-mode hooks in {config}")
