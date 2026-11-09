# Decision Review

Decision Review offers Decision advice, Creative exploration, and general-purpose Critical review. See [SKILL.md](SKILL.md) for roles and workflow; the matrix below shows team membership.

## Install the skill

For Codex CLI and Claude Code, install from this repository with the Skills CLI:

```sh
npx skills add OlivierLB/agent-skills --skill decision-review -a codex -a claude-code -g -y
```

For the Plan-mode hook behavior, also follow [the host integration install steps](extensions/README.md). Codex CLI and Claude Code use different install mechanisms. The public plugin directory package must omit lifecycle hooks; local host integrations are distributed separately.

## Roles by mode

| Role | Decision advice | Creative exploration | Critical review |
| --- |:---:|:---:|:---:|
| Contrarian | ✓ | | ✓ |
| First-principles thinker | ✓ | ✓ | ✓ |
| Expansionist | ✓ | ✓ | |
| Outsider | ✓ | ✓ | ✓ |
| Executor | ✓ | | ✓ |
| Reframer | | ✓ | |
| Analogy scout | | ✓ | |
| Possibility generator | | | |
| Claim auditor | | | ✓ |

Unassigned roles are defined for possible future teams.

## Plan behavior

When active in Plan mode, the skill reviews the initial request and the agreed plan before its first implementation edit. The pre-edit hook blocks one matching edit call and asks the agent to run the second review; the agent then continues the agreed plan unless the user asks to incorporate findings. Outside Plan mode, invoke Decision Review explicitly.

## License

Distributed under the repository's [MIT license](../../../LICENSE).
