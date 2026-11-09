# Decision Review

Decision Review offers decision advice, creative exploration, and general-purpose critical review. See [SKILL.md](SKILL.md) for the roles and workflow; this matrix shows which five roles make up each team.

## Install the skill

Install for Codex with the Skills CLI:

```sh
npx skills add OlivierLB/agent-skills --skill decision-review -a codex -g -y
```

For Plan-mode reminders and checkpoints, follow the [Codex integration install steps](extensions/README.md).

## Roles by mode

| Role | Decision advice | Creative exploration | Critical review |
| --- |:---:|:---:|:---:|
| Contrarian | ✓ | | ✓ |
| First-principles thinker | ✓ | ✓ | ✓ |
| Expansionist | ✓ | ✓ | |
| Outsider | ✓ | ✓ | ✓ |
| Executor | ✓ | | |
| Reframer | | ✓ | |
| Analogy scout | | ✓ | |
| Claim auditor | | | ✓ |
| Adversarial reader | | | ✓ |

## Plan behavior

In Codex Plan mode, optional hooks add a reminder and checkpoint, and block the first `apply_patch` call. They do not run the review or verify completion; shell-based edits are not intercepted. Plan mode alone does not activate the skill. See the integration notes for details.

## License

Distributed under the repository's [MIT license](../../../LICENSE).
