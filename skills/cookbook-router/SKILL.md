---
name: cookbook-router
description: Route a user to the correct cookbook in this repo, then hand off to the local cookbook docs and skill-pack.
---

# Cookbook Router

Use this skill as the first entrypoint when the user cloned the cookbook repo but has not yet picked a workflow.

## What This Skill Does

1. Detect which cookbook fits the user’s environment and intent.
2. Point the agent at the correct cookbook docs and starter template.
3. Load the cookbook-specific skill-pack if one exists.
4. Tell the user, briefly, that the repo is ready and what the next concrete step is.

## Cookbook Selection

Choose `intermediate-linux-gpu/` when:
- the user has Linux plus NVIDIA GPU or cloud GPU
- they want stronger validation lanes
- they need target-decoy or PyRosetta-style follow-up

Choose `intermediate-mlx/` when:
- the user is on Apple Silicon / MLX
- they want local iterative design and preview work
- they are following the MLX-specific docs or examples

Choose `colab-basics/` when:
- the user wants Google Colab or Jupyter notebooks
- they prefer a manual notebook-first workflow
- they are new and want a lightweight, inspectable path

## Required First Response

Your first response should be short and concrete:
- say which cookbook you selected
- name the exact files the user should start from
- mention whether a cookbook-specific skill-pack applies
- state that the repo is ready

## Files To Load

For `intermediate-linux-gpu/`:
- `intermediate-linux-gpu/README.md`
- `intermediate-linux-gpu/PROJECT_STRUCTURE.md`
- `intermediate-linux-gpu/TEMPLATES.md`
- `intermediate-linux-gpu/skill-pack/peptide-research-ops/SKILL.md`

For `intermediate-mlx/`:
- `intermediate-mlx/README.md`
- `intermediate-mlx/docs/PROJECT_STRUCTURE.md`
- `intermediate-mlx/docs/AGENT_BOOTSTRAP.md`
- `intermediate-mlx/skill-pack/peptide-mlx-research-ops/SKILL.md`

For `colab-basics/`:
- `colab-basics/README.md`
- `colab-basics/NOTEBOOK_PLAN.md`

## Constraints

- Do not describe this as “Codex inside Colab”.
- Do not treat notebooks as the main orchestration layer for the agent-first cookbooks.
- Prefer the agent-first cookbooks unless the user explicitly wants notebooks or Colab.
- Keep the explanation brief; route first, then work inside the selected cookbook.
