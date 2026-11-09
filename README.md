# Olivier's agent skills

A growing collection of focused skills for AI coding agents. Install only the skills you want, or install the whole collection.

## Install for Codex and Claude

Install one skill for Codex and Claude Code:

```sh
npx skills add OlivierLB/agent-skills --skill council-review -a codex -a claude-code -g -y
```

Install every skill in this collection for both agents:

```sh
npx skills add OlivierLB/agent-skills --skill '*' -a codex -a claude-code -g -y
```

These commands install skills globally so they are available across projects. Remove `-g` to install into the current project instead. Check the installed skills with `npx skills ls -a codex -a claude-code`. Every skill in this collection must support both Codex and Claude Code; see [CONTRIBUTING.md](CONTRIBUTING.md) before adding one. The commands use the open-source [`skills` CLI](https://github.com/vercel-labs/skills), which supports explicit agent selection.

## Skills

| Skill | Purpose |
| --- | --- |
| [`council-review`](skills/productivity/council-review/SKILL.md) | Explore ideas, critically review work, or advise on consequential decisions through five independent perspectives and anonymous peer review. |

## Add a skill

Create a directory under `skills/` with a `SKILL.md` file. Keep each skill focused and self-contained. The skills CLI can then install it by name or as part of the full collection.

## License

MIT. See [LICENSE](LICENSE).
