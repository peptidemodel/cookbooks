# PeptideModel Cookbooks

This repo is a collection of reusable peptide-research cookbooks. Each top-level directory is a cookbook with its own templates, docs, examples, and skill support.

## Cookbooks

- `intermediate-linux-gpu/`
  Agent-first Linux/GPU cookbook for stronger structure-prediction, target-decoy, and physics-based lanes.
- `intermediate-mlx/`
  Agent-first Apple Silicon / MLX cookbook for local iterative design and preview work.
- `colab-basics/`
  Notebook-first manual track for Google Colab and Jupyter users who want a lighter guided workflow.
- `skills/`
  Top-level agent entrypoint that routes a user to the right cookbook and existing skill-pack.

## Entry Points

- Agent-first: start with `skills/cookbook-router/SKILL.md`
- Manual / notebook-first: start with `colab-basics/README.md`

## Mental Model

- `results/` = working outputs and local experiment artifacts
- `upload_ready/` = only promoted designs ready for platform packaging
- `docs/` / project readmes = human interpretation and handoff context
