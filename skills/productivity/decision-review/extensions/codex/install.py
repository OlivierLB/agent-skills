#!/usr/bin/env python3
"""Install Decision Review hooks into the current user's Codex CLI config."""
import json
import os
from pathlib import Path

home = Path.home()
config = home / ".codex" / "hooks.json"
script = Path(__file__).resolve().parent / "pre_edit.py"
config.parent.mkdir(parents=True, exist_ok=True)
data = json.loads(config.read_text()) if config.exists() else {"hooks": {}}
hooks = data.setdefault("hooks", {})
entry = {
    "matcher": "apply_patch|Bash",
    "hooks": [{"type": "command", "command": f'python3 "{script}"', "timeout": 10}],
}
existing = hooks.setdefault("PreToolUse", [])
if not any(any(str(script) in h.get("command", "") for h in e.get("hooks", [])) for e in existing):
    existing.append(entry)
prompt_entry = {"hooks": [{"type": "command", "command": f'python3 "{script}"', "timeout": 10}]}
prompts = hooks.setdefault("UserPromptSubmit", [])
if not any(any(str(script) in h.get("command", "") for h in e.get("hooks", [])) for e in prompts):
    prompts.append(prompt_entry)
stops = hooks.setdefault("Stop", [])
stop_entry = {"hooks": [{"type": "command", "command": f'python3 "{script}"', "timeout": 10}]}
if not any(any(str(script) in h.get("command", "") for h in e.get("hooks", [])) for e in stops):
    stops.append(stop_entry)
tmp = config.with_suffix(".json.tmp")
tmp.write_text(json.dumps(data, indent=2) + "\n")
os.chmod(tmp, 0o600)
tmp.replace(config)
print(f"Installed Decision Review Plan-mode hooks in {config}")
