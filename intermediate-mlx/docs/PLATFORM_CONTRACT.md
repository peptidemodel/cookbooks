# Platform Contract

This is the downstream contract for PeptideModel prediction ingest.

Use this when your MLX run is meant to land in the PeptideModel platform rather
than remain only as local files.

## Bulk API Shape

Prediction ingest goes through:

- `POST /api/predictions/bulk`

Payload shape:

```json
{
  "predictions": [
    {
      "prediction_id": "pep-00127-mlx-001",
      "card_id": "pep-00127",
      "model": "openfold3-mlx"
    }
  ]
}
```

Expected response:

```json
{
  "wrote": 1
}
```

## Required Fields

- `prediction_id`
- `card_id`
- `model`

## Common Optional Fields

- `status`
- `model_version`
- `weights_hash`
- `hardware`
- `mlx_version`
- `python_version`
- `random_seed`
- `msa_strategy`
- `num_diffusion_samples`
- `command_line`
- `runtime_seconds`
- `predicted_at`
- `pdb_path`
- `iptm`
- `ptm`
- `avg_plddt`
- `ranking_score`
- `pde_summary`
- `binding_mode_rmsd`
- `warnings`
- `failure_reason`
- `predicted_by_agent`
- `batch_id`
- `canonical`

## Structure File Formats

Supported downstream structure formats:

- `.pdb`
- `.cif`

Canonical storage pattern:

- `predictions/{card_id}/{prediction_id}.pdb`
- `predictions/{card_id}/{prediction_id}.cif`

Canonical `pdb_path` pattern in the DB:

- relative path such as `pep-00127/pep-00127-mlx-001.cif`

The backend can also tolerate absolute paths, but new runs should prefer the
relative contract.

Default repo policy:

- for platform-facing MLX runs, prefer `.cif` unless a project explicitly
  chooses `.pdb` and records that choice in `config/target_spec.json` and
  `pipeline/README.md`

## YAML

YAML is **not** used for backend prediction ingest.

Important distinction:

- YAML may still exist for local manifests or runner configuration
- PeptideModel prediction write-back is API-driven, not YAML-driven

Do not design prediction delivery around YAML upload.

For cookbook closeout, YAML is still used in `upload_ready/` as a human-facing
upload helper, not as the backend ingest payload.

Expected cookbook packaging:

- `upload_ready/<design>/card.yaml`
- `upload_ready/<design>/structure.pdb` or `.cif`
- `upload_ready/<design>/readme.md`

## Canonical Upload Card Schema

`card.yaml` should map directly to the platform upload form.
Do not improvise field names.

Use this schema:

```yaml
title: "sE_protease_armor — GLP-1R/GIPR agonist (E3A on tirzepatide)"
sequence: YAAGTFTSDYSIALDKIAQKAFVQWLIAGGPSSGAPPPS
targets:
  - glp-1r
  - gipr
scaffold: tirzepatide
parent_card: pep-00016
status: computed

metrics:
  - key: ipTM
    value: 0.894
    tool: Boltz-1
  - key: pLDDT
    value: 0.828
    tool: Boltz-1

source:
  kind: other
  notes: "Predicted by OpenFold3-MLX on Apple Silicon"

structure_file: structure.pdb
readme_file: readme.md
```

Do not use invented top-level fields such as:

- `mode`
- `canonical_structure_format`
- `main_metric`
- `metric_name`
- `pdb_path`
- `caveat`
- `modeling_tool`

## Target Slug Rules

Targets in `card.yaml` must use the platform slug form:

- `targets` must be an array
- use slugs such as `glp-1r`, `gipr`, `ghsr`, `gdf-8`
- do not use human-readable names
- do not use slash-separated strings

If a target has no known platform slug, omit it rather than inventing one.

## Status Rules

Use only the platform status values:

- `designed`
- `computed`
- `reproduced`
- `synthesized`
- `bioassayed`

Do not invent extra levels such as `Computed Level 6` or pipeline phase labels.

## Structured Extras

Use `pde_summary` for structured output that does not have a dedicated column.

Examples:

- global confidence summaries
- extra per-run confidence fields
- structured warning context

## Recommended Platform Metadata

For multi-card or agent-driven runs, set:

- `predicted_by_agent`
- `batch_id`
- `canonical`

Reason:

- these make frontend selection and run-group querying simpler

## Production-Quality Recommended Fields

For production-quality platform ingest, strongly prefer including:

- `model_version`
- `weights_hash`
- `hardware`
- `mlx_version`
- `python_version`
- `random_seed`
- `num_diffusion_samples`
- `command_line`
- `runtime_seconds`
- `predicted_at`
- `pdb_path`
- `predicted_by_agent`
- `batch_id`

Reason:

- backend accepts a smaller minimum contract
- operators usually need a richer provenance contract for audit, reruns, and
  cross-batch comparisons

## Practical Rule

For platform work, local manifests are not enough.

A run is only integrated when:

1. the structure file exists in the expected storage path
2. the backend prediction row has been written
3. the metadata is rich enough to reproduce or audit the run later

Cookbook rule:

- only promoted designs should be packaged into `upload_ready/`
- rejected designs stay local in `results/`, `validation/`, and `research_log.md`
