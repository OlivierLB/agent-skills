# Codex directory package

This folder contains the Codex plugin manifest and listing icon for the public
Decision Review package. The package builder copies the canonical skill from
`skills/productivity/decision-review/SKILL.md`, so the plugin does not maintain
a second source copy.

Build a self-contained ZIP for the OpenAI Plugins dashboard:

```sh
python3 codex-plugin/package.py /tmp/decision-review-plugin-1.0.0.zip
```

The ZIP deliberately excludes local Codex lifecycle hooks. The public plugin
directory does not currently accept plugin ZIPs that contain lifecycle hooks.
The package includes only the skill and its listing assets.
