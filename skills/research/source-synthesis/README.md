# Source Synthesis

Source Synthesis helps choose sources suited to a research question and assess whether the information they provide is reliable, relevant, current, and applicable. It covers official records, expert guidance, original studies, journalism, historical material, product information, forums, and firsthand accounts.

See [SKILL.md](SKILL.md) for the complete workflow.

## Install

Install for Codex with the Skills CLI:

```sh
npx skills add OlivierLB/agent-skills --skill source-synthesis -a codex -g -y
```

Remove `-g` to install into the current project instead of globally. Confirm the skill is available with:

```sh
npx skills ls -a codex
```

## Use

Codex can select the skill when a task involves researching a question and assessing its sources. You can also request it explicitly, for example: “Use Source Synthesis to research this question and assess the reliability of the sources.”

## License

Distributed under the repository's [MIT license](../../../LICENSE).
