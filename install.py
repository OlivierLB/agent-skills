#!/usr/bin/env python3
"""Install all skills and host integrations from this checkout."""

import shutil
import subprocess
import sys
from pathlib import Path


root = Path(__file__).resolve().parent
for command in ("npx",):
    if not shutil.which(command):
        sys.exit(f"Missing {command}; install it, then rerun: python3 install.py")


def run(*args):
    subprocess.run(args, cwd=root, check=True)


run("npx", "--yes", "skills", "add", str(root), "--skill", "*", "-a", "codex", "-g", "-y")
run(sys.executable, str(root / "skills/productivity/decision-review/extensions/codex/install.py"))
print("All skills and Codex hooks are installed. Restart Codex and approve hooks if prompted.")
