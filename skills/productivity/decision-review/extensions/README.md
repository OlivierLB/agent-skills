# Install the Codex Plan-mode integration

From the repository root, install the skill and its Codex hooks:

```sh
python3 skills/productivity/decision-review/extensions/codex/install.py
```

The installer merges `UserPromptSubmit`, `Stop`, and `PreToolUse` hooks into
`~/.codex/hooks.json`, preserving existing entries and avoiding duplicates.
Restart Codex CLI and approve the hooks if prompted. On the first prompt in
Plan mode, `UserPromptSubmit` adds the skill instruction and `Stop` forces one
continuation before the answer can finish. `PreToolUse` blocks the first
matching `apply_patch` call per session. Shell-based edits are not intercepted.
The continuation is a checkpoint, not proof that the review was completed.

## After the hook blocks

The hook returns an instruction to the agent; it does not run the review. The
agent must run the five-role review in the conversation, show the result, and
continue the agreed plan without incorporating recommendations unless the user
asks. Hooks do not guarantee that the model follows this instruction. The
first-message Plan review is also an instruction to the agent, not a
hook-triggered review.
