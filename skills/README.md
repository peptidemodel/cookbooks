# Top-Level Skills

Use these as the first agent entrypoint into the cookbook repo.

- `cookbook-router/`
  High-level router skill that decides which cookbook applies and points the agent at the right local docs, template, and skill-pack.

The router does not replace the cookbook-specific skill-packs inside `intermediate-linux-gpu/` and `intermediate-mlx/`. It loads them after selecting the right cookbook.
