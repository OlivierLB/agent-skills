# Install the Plan-mode integration

Install the skill and hook for the host you use. These local integrations are not part of the public directory upload: OpenAI's public plugin submission removes lifecycle hooks. Claude Code can install its plugin with the hook through a marketplace. Codex CLI uses its native user hook configuration; no Desktop app is required. Both hooks need the host to approve/trust them and cannot launch subagents themselves.

## Codex CLI

From the repository root, run:

```sh
python3 skills/productivity/council-review/extensions/codex/install.py
```

The installer merges a `PreToolUse` entry into `~/.codex/hooks.json`, preserving existing hooks. Restart Codex CLI and approve the hook when prompted. To remove it, delete the entry whose command points to `extensions/codex/pre_edit.py` from that file.

The hook detects `permission_mode: "plan"` and blocks the first matching `apply_patch` or `Bash` call in each session. It treats every Bash call as a possible edit. The returned reason asks the agent to run Council Review, show the findings, then continue with the agreed plan. After that first block, later matching calls in the same session pass.

## Claude Code

From the repository root, add the local marketplace and install its plugin:

```sh
claude plugin marketplace add ./skills/productivity/council-review/extensions/claude-plugin
claude plugin install council-review@council-review-local
```

Restart Claude Code and approve/trust the plugin hooks. To uninstall:

```sh
claude plugin uninstall council-review@council-review-local
claude plugin marketplace remove council-review-local
```

The hook matches `Edit`, `Write`, and `Bash`, and blocks the first matching call when the event has `permission_mode: "plan"`. Bash is treated as a possible edit. If the field is absent, the hook allows the call; Plan detection must be verified with the installed Claude Code version.

## What the hooks do

Hooks block the first matching edit and return instructions to the agent. The agent then runs the five-role council in the conversation, presents its review, and continues the existing plan without applying the recommendations unless the user asks. Hooks do not run agents or guarantee the model follows those instructions. Plan-mode first-message review remains a skill instruction because these host hooks cannot themselves invoke the council workflow.
