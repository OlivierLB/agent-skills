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

integrations = sorted(root.glob("skills/*/*/extensions/codex/install.py"))
for installer in integrations:
    run(sys.executable, str(installer))

print("All skills and available Codex integrations are installed. Restart Codex and approve hooks if prompted.")
