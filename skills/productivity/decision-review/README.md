# Decision Review

Decision Review offers decision advice, creative exploration, and general-purpose critical review. See [SKILL.md](SKILL.md) for the self-contained roles, role matrix, and workflow.

## Install the skill

Install for Codex with the Skills CLI:

```sh
npx skills add OlivierLB/agent-skills --skill decision-review -a codex -g -y
```

For Plan-mode reminders and checkpoints, follow the [Codex integration install steps](extensions/README.md).

## Plan behavior

In Codex Plan mode, optional hooks add a reminder and checkpoint, and block the first `apply_patch` call. They do not run the review or verify completion; shell-based edits are not intercepted. Plan mode alone does not activate the skill. See the integration notes for details.

## License

Distributed under the repository's [MIT license](../../../LICENSE).
