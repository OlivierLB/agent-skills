#!/usr/bin/env python3
"""Install all skills and host integrations from this checkout."""

import shutil
import subprocess
import sys
from pathlib import Path


root = Path(__file__).resolve().parent
for command in ("npx", "claude"):
    if not shutil.which(command):
        sys.exit(f"Missing {command}; install it, then rerun: python3 install.py")


def run(*args):
    subprocess.run(args, cwd=root, check=True)


run("npx", "--yes", "skills", "add", str(root), "--skill", "*", "-a", "codex", "-a", "claude-code", "-g", "-y")
run(sys.executable, str(root / "skills/productivity/decision-review/extensions/codex/install.py"))

marketplace = "decision-review-local"
if marketplace not in subprocess.check_output(
    ["claude", "plugin", "marketplace", "list"], text=True
):
    run("claude", "plugin", "marketplace", "add", str(root / "skills/productivity/decision-review/extensions/claude-plugin"))

plugin = "decision-review@decision-review-local"
if plugin not in subprocess.check_output(["claude", "plugin", "list"], text=True):
    run("claude", "plugin", "install", plugin, "-s", "user", "-y")

print("All skills, Codex hooks, and Claude Code plugin are installed. Restart both hosts and approve hooks if prompted.")
