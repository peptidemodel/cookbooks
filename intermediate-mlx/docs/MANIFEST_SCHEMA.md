# Manifest Schema

Use one stable manifest shape per project.

## Canonical Location

Default location:

- per-run manifests: `pipeline/manifests/`
- project resume state: `pipeline/manifests/state.json`

If a project chooses a different location, document that in the root `README.md`
and the active phase doc.

Default repo policy:

- use the canonical starter locations unless a live project has a documented
  reason to differ

## Minimal Manifest Shape

```json
{
  "manifest_version": "1.0",
  "run_id": "replace-me",
  "phase": "phase2_reference_preview",
  "mode": "preview",
  "authority_file": "docs/phase2_reference_preview.md",
  "predicted_at": "2026-04-16T00:00:00Z",
  "model": "openfold3-mlx",
  "model_version": "replace-me",
  "weights_hash": "replace-me",
  "hardware": "replace-me",
  "python_version": "replace-me",
  "mlx_version": "replace-me",
  "runner_yaml": "replace-me",
  "random_seed": 42,
  "num_diffusion_samples": 1,
  "msa_strategy": "replace-me",
  "query_json": "queries/reference_panel.json",
  "output_dir": "results/replace-me",
  "warnings": [],
  "notes": "replace-me"
}
```

## Required Fields

- `manifest_version`
- `run_id`
- `phase`
- `mode`
- `authority_file`
- `predicted_at`
- `model`
- `model_version`
- `weights_hash`
- `hardware`
- `python_version`
- `mlx_version`
- `runner_yaml`
- `random_seed`
- `num_diffusion_samples`
- `query_json`
- `output_dir`

Minimum validation checks before accepting a manifest:

- required fields are present
- `mode` matches the active phase intent
- `authority_file` names the file that set the gate or upgrade decision
- `model_version` is present for real runs
- `query_json` path exists
- `output_dir` path is the intended run destination
- `num_diffusion_samples` matches the command actually used
- `weights_hash` is not blank for real runs

## Optional But Strongly Recommended

- `msa_strategy`
- `warnings`
- `notes`
- copied config hash or commit SHA if available

## State File Shape

Use this default if the project has no better established format:

```json
{
  "phase": "phase3_batch_plan",
  "batch_id": "replace-me",
  "completed": {},
  "failed": {},
  "next_action": "replace-me",
  "blocked_on": null
}
```

## Rule

Do not let every script invent a new manifest shape.
If the schema changes mid-project, record the version bump explicitly.

Per-project schema stability is enough by default.
Do not force one cross-project global schema unless you actually need it.

Default repo policy:

- keep the field set and path conventions aligned with this schema unless a
  live project documents a justified deviation
