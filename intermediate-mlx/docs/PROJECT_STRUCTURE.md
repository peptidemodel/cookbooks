# Project Structure

## The Base Layout

Use a clean per-project folder. The minimal structure is:

```text
my-mlx-project/
  README.md
  config/
    target_spec.json
    reference_complexes.json
    hardware_profile.json
  queries/
    reference_panel.json
    candidate_panel.json
  pipeline/
    README.md
    manifests/
  docs/
    phase0_environment_check.md
    phase1_target_freeze.md
    phase2_reference_preview.md
    phase3_batch_plan.md
    phase4_upgrade_validation.md
    phase5_closeout.md
    pause_state.md
  research/
    target_brief.md
    provenance_notes.md
  results/
  validation/
  upload_ready/
```

## Why This Layout Works

### `config/`

Contains frozen specification and machine assumptions:

- target IDs and sequence sources
- peptide/reference identities
- hardware memory assumptions
- preview and upgrade defaults

If `config/` is wrong, the whole project is wrong.

### `queries/`

Contains machine-readable input panels.

Typical responsibilities:

- reference panel for calibration
- candidate or batch panels for later phases
- explicit query names and chain order

Do not scatter live query definitions across shell history.

### `pipeline/`

Contains runner notes, manifest format, and automation.

Typical responsibilities:

- build OF3 query JSON
- launch prediction runs
- collect metrics
- persist state for resume
- define downstream write-back expectations when the project targets the
  platform

### `docs/`

Contains phase decisions and operational truth:

- what phase the project is in
- what the current gate is
- why preview is or is not sufficient
- what is paused and how to resume

### `research/`

Contains the scientific basis:

- target biology notes
- sequence provenance
- literature-derived controls

Do not bury reference provenance only in commit messages.

### `results/`

Contains clean phase outputs:

- per-query summaries
- aggregated metrics
- archived manifests
- selected CIF or PDB outputs
- all working outputs, including rejected designs and raw promotion inputs

### `validation/`

Contains upgraded validation outputs:

- multi-sample follow-up
- target-decoy checks
- orthogonal-lane comparisons

### `upload_ready/`

Contains promoted designs only.

One folder per promoted design:

- `card.yaml`
- `structure.pdb` or `.cif`
- `readme.md`

Do not put:

- rejected designs
- manifests or batch intermediates
- scratch closeouts
- raw result bundles

## The Project Root `README.md`

Every project root should answer:

1. What target or target family is being studied?
2. What peptide set is being evaluated?
3. What counts as `preview` versus `upgrade`?
4. What phase is active right now?
5. What is the active phase doc path?
6. Which files are authoritative?
7. Is this run local-only or intended for platform write-back?

If the root `README` cannot answer those seven, the project is not handoff-ready.

## The Single Most Important Structural Rule

Keep sequence source and query naming explicit.

Always document:

- target accession or source record
- peptide source and whether residues were proxied
- query naming convention
- chain assignment
- seed and sample count

Real MLX projects fail when query naming, sequence provenance, or chain order
is left implicit.
