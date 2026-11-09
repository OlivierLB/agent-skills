#!/usr/bin/env python3
"""Prompt for Council Review and require one continuation in Plan mode."""

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

tmp = Path(tempfile.gettempdir())
event_name = event.get("hook_event_name")

if event_name == "UserPromptSubmit":
    first = tmp / f"council-review-first-{session}.seen"
    try:
        fd = os.open(first, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.close(fd)
    except FileExistsError:
        sys.exit(0)

    pending = tmp / f"council-review-stop-{session}.pending"
    try:
        fd = os.open(pending, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.close(fd)
    except OSError as exc:
        first.unlink(missing_ok=True)
        print(f"Council Review: unable to create Plan-mode checkpoint: {exc}", file=sys.stderr)
        sys.exit(2)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "Plan mode: immediately invoke and complete the council-review skill on the user's initial request before drafting a plan or answering. Then continue with the task."
        }
    }))
    sys.exit(0)

if event_name == "Stop":
    pending = tmp / f"council-review-stop-{session}.pending"
    try:
        pending.unlink()
    except FileNotFoundError:
        sys.exit(0)
    except OSError:
        sys.exit(0)

    print(json.dumps({
        "decision": "block",
        "reason": "Before finalizing the response to the initial Plan-mode request, run the council-review skill now if you have not already completed it. If completed, include its synthesized findings before answering the user's request. Do not merely state that the review should be run."
    }))
    sys.exit(0)

if event_name != "PreToolUse":
    sys.exit(0)

marker = tmp / f"council-review-{session}.seen"
try:
    fd = os.open(marker, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
except FileExistsError:
    sys.exit(0)
except OSError:
    print("Council Review: unable to create session marker; edit blocked. Run Council Review, then retry.", file=sys.stderr)
    sys.exit(2)
else:
    os.close(fd)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Before the first Plan-mode edit, run Council Review, show findings to the user, then continue with the agreed plan without incorporating advice unless the user asks. Retry the edit after the review."
    }
}))
