# Install the Plan-mode integration

Install the skill and hook for the host you use. The public plugin directory submission excludes lifecycle hooks, so hook integrations are installed locally. Codex hooks can inject instructions and force a continuation, but cannot invoke the skill or launch its agents themselves.

## Codex CLI

From the repository root, run:

```sh
python3 skills/productivity/council-review/extensions/codex/install.py
```

The installer merges `UserPromptSubmit`, `Stop`, and `PreToolUse` hooks into `~/.codex/hooks.json`, preserving existing entries and avoiding duplicates. Restart Codex CLI and approve the hooks if prompted. On the first prompt in Plan mode, `UserPromptSubmit` adds the skill instruction and `Stop` forces one continuation before the answer can finish. `PreToolUse` also blocks the first matching `apply_patch` or `Bash` call per session. It treats every Bash call as a possible edit. Later matching calls pass. The continuation is a stronger checkpoint, not proof that the model completed the review.

## Claude Code

The local marketplace and complete plugin package are in `claude-plugin/`. From the repository root:

```sh
claude plugin marketplace add ./skills/productivity/council-review/extensions/claude-plugin
claude plugin install council-review@council-review-local
```

Restart Claude Code and approve/trust the plugin hooks. To remove it:

```sh
claude plugin uninstall council-review@council-review-local
claude plugin marketplace remove council-review-local
```

The plugin contains `.claude-plugin/plugin.json`, the skill under `skills/council-review/`, and a `PreToolUse` hook. The hook matches `Edit`, `Write`, and `Bash`, and is expected to block the first matching call in Plan mode.

## After the hook blocks

The hook returns an instruction to the agent; it does not run the council. The agent must run the five-role review in the conversation, show the result, and continue the agreed plan without incorporating recommendations unless the user asks. Hooks do not guarantee that the model follows this instruction. The first-message Plan review is also an instruction to the agent, not a hook-triggered council run.
