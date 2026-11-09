# Adding skills

This collection targets **Codex**.

- Put it under `skills/<category>/<skill-name>/SKILL.md` and use the Agent Skills `name` and `description` frontmatter.
- Document host capabilities and limitations accurately; never imply a capability is available when it is not.
- Add the skill to the README catalog and provide a Codex installation command based on the `skills` CLI.

Before publishing a new skill, install it for both hosts and confirm it appears in each agent's skill list:

```sh
npx skills add OlivierLB/agent-skills --skill <skill-name> -a codex -g -y
npx skills ls -a codex
```
