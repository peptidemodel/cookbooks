# PeptideModel Cookbooks

Public repo: `https://github.com/peptidemodel/cookbooks`

This repo is a collection of reusable peptide-research cookbooks. Each top-level directory is a cookbook with its own templates, docs, examples, and skill support.

## Start Here

Agent-first path:
1. Clone the repo.
2. Point Claude Code or Codex at this repo.
3. Start with `skills/cookbook-router/SKILL.md`.
4. Let the agent route you to the right cookbook and local skill-pack.

Notebook-first path:
1. Start with `colab-basics/README.md`.
2. Open the notebook badges there in Google Colab.
3. Clone this repo into Colab with:
   `!git clone https://github.com/peptidemodel/cookbooks /content/cookbooks`

## Cookbooks

- `intermediate-linux-gpu/`
  Agent-first Linux/GPU cookbook for stronger structure-prediction, target-decoy, and physics-based lanes.
- `intermediate-mlx/`
  Agent-first Apple Silicon / MLX cookbook for local iterative design and preview work.
- `colab-basics/`
  Notebook-first manual track for Google Colab and Jupyter users who want a lighter guided workflow.
- `skills/`
  Top-level agent entrypoint that routes a user to the right cookbook and existing skill-pack.

## Mental Model

- `config/`, `queries` or `candidates`, `docs`, `pipeline`, and `upload_ready` = starter template core
- `research/`, `results/`, and `validation/` = create-on-use project folders
- `upload_ready/` = platform packaging contract; add design folders only after promotion
- `docs/` / project readmes = human interpretation and handoff context
