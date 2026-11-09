# Olivier's agent skills

A growing collection of focused skills for AI coding agents. Install only the skills you want, or install the whole collection.

## Install

Install one skill:

```sh
npx skills add OlivierLB/agent-skills --skill council-review
```

Install every skill in this collection:

```sh
npx skills add OlivierLB/agent-skills --all
```

The installer detects supported agents and asks where to install. Add `--global` for user-wide installation or `--agent codex` to target Codex. See the [skills CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for current options.

## Skills

| Skill | Purpose |
| --- | --- |
| [`council-review`](skills/productivity/council-review/SKILL.md) | Review a meaningful decision through five independent perspectives, anonymous peer review, and a clear recommendation. |

## Add a skill

Create a directory under `skills/` with a `SKILL.md` file. Keep each skill focused and self-contained. The skills CLI can then install it by name or as part of the full collection.

## License

MIT. See [LICENSE](LICENSE).
