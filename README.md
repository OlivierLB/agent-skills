# Olivier's agent skills

A growing collection of focused skills for AI agents. Install only the skills you want, or install the whole collection.

[![skills.sh](https://skills.sh/b/OlivierLB/agent-skills)](https://skills.sh/b/OlivierLB/agent-skills)

Skills are distributed from this GitHub repository. New installs fetch the current version; existing installs can pull updates with `npx skills update`.

## Install everything

Clone this repository, then run:

```sh
python3 install.py
```

This installs all skills and available Codex integrations. Restart Codex after installation and approve hooks if prompted. The installer requires Node.js/npm.

## Install one skill

Install an individual skill for Codex with the open-source [`skills` CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add OlivierLB/agent-skills --skill <skill-name> -a codex -g -y
```

The `-g` option installs globally across projects. Remove it to install into the current project. Check installed skills with `npx skills ls -a codex`.

Install all skills for Codex with:

```sh
npx skills add OlivierLB/agent-skills --skill '*' -a codex -g -y
```

Update installed skills from GitHub sources with:

```sh
npx skills update
```

## Skills

| Skill | Purpose | Install name |
| --- | --- | --- |
| [Decision Review](skills/productivity/decision-review/SKILL.md) | Explore ideas, critically review work, or advise on consequential decisions through multiple perspectives. | `decision-review` |
| [Source Synthesis](skills/research/source-synthesis/SKILL.md) | Choose and assess sources for any research question, then synthesize findings with appropriate uncertainty. | `source-synthesis` |

## Add a skill

Create a directory under `skills/` with a `SKILL.md` file and Agent Skills `name` and `description` frontmatter. Keep each skill focused and self-contained. See [CONTRIBUTING.md](CONTRIBUTING.md) before adding a skill.

## License

MIT. See [LICENSE](LICENSE).
