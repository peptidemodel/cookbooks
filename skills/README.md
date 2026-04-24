# Top-Level Skills

Public repo: `https://github.com/peptidemodel/cookbooks`

Use these as the first agent entrypoint after cloning the repo locally.

Recommended flow:
1. Clone `https://github.com/peptidemodel/cookbooks`
2. Open the repo in Claude Code or Codex
3. Start with `skills/cookbook-router/SKILL.md`
4. Let the router select the correct cookbook and then load the cookbook-specific skill-pack

Available top-level skill:
- `cookbook-router/`
  High-level router skill that decides which cookbook applies and points the agent at the right local docs, template, and skill-pack.

The router does not replace the cookbook-specific skill-packs inside `intermediate-linux-gpu/` and `intermediate-mlx/`. It loads them after selecting the right cookbook.
