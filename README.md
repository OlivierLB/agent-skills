# Olivier's agent skills

A growing collection of focused skills for AI agents. Install only the skills you want, or install the whole collection.

[![skills.sh](https://skills.sh/b/OlivierLB/agent-skills)](https://skills.sh/b/OlivierLB/agent-skills)

Skills are distributed from this GitHub repository. New installs fetch the current version; existing installs can pull updates with `npx skills update`.

The current collection version is **1.0.0**. Releases use Semantic Versioning and Git tags (`v1.0.0`); the [changelog](CHANGELOG.md) records user-facing changes. Pin an installation to a release for reproducibility, or omit the version to follow the latest branch.

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

To install a specific release, append its tag to the repository name, for example:

```sh
npx skills add OlivierLB/agent-skills@v1.0.0 --skill source-synthesis -a codex -g -y
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

## Versioning and releases

The repository is released as one collection: a release tag versions all included skills and integrations together. Follow Semantic Versioning: increment the patch number for compatible fixes, the minor number for backward-compatible additions, and the major number for incompatible changes. Update `VERSION` and `CHANGELOG.md` for each release, then create and push the matching Git tag (for example, `v1.0.0`). Installations can pin that tag with `npx skills add OlivierLB/agent-skills@v1.0.0`.

## Add a skill

Create a directory under `skills/` with a `SKILL.md` file and Agent Skills `name` and `description` frontmatter. Keep each skill focused and self-contained. See [CONTRIBUTING.md](CONTRIBUTING.md) before adding a skill.

## License

MIT. See [LICENSE](LICENSE).
