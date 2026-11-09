# Adding skills

Every skill in this collection must install and work in both **Codex** and **Claude Code**.

- Put it under `skills/<category>/<skill-name>/SKILL.md` and use the Agent Skills `name` and `description` frontmatter.
- Keep the instructions platform-neutral. When the workflow needs sub-agents, tools, or other host capabilities, name the equivalent behavior for Codex and Claude Code; never silently assume a tool exists in both.
- If a capability is missing in either host, give a clear fallback and label it as a single-agent result rather than pretending independent agents ran.
- Add the skill to the README catalog and keep its install command based on the `skills` CLI, targeting both `codex` and `claude-code`.

Before publishing a new skill, install it for both hosts and confirm it appears in each agent's skill list:

```sh
npx skills add OlivierLB/agent-skills --skill <skill-name> -a codex -a claude-code -g -y
npx skills ls -a codex -a claude-code
```
