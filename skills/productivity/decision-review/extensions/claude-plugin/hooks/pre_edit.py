#!/usr/bin/env python3
"""Block the first potentially mutating Claude Code tool call in Plan mode."""
import json
import os
import sys
import tempfile
from pathlib import Path

try:
    event = json.load(sys.stdin)
except (json.JSONDecodeError, OSError):
    sys.exit(0)

if event.get("permission_mode") != "plan":
    sys.exit(0)

session = str(event.get("session_id", ""))
if not session or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in session):
    sys.exit(0)

marker = Path(tempfile.gettempdir()) / f"decision-review-claude-{session}.seen"
try:
    fd = os.open(marker, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
except FileExistsError:
    sys.exit(0)
except OSError:
    print("Decision Review: unable to create session marker; edit blocked. Run Decision Review, then retry.", file=sys.stderr)
    sys.exit(2)
else:
    os.close(fd)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Before the first Plan-mode edit, run Decision Review, show findings to the user, then continue with the agreed plan without incorporating advice unless the user asks. Retry the edit after the review."
    }
}))
