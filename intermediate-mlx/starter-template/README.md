# Starter Template — PeptideModel OF3-MLX Project

This is the neutral starter template for peptide-target structural work on
OpenFold3-MLX for PeptideModel platform users.

Use this when you want to start a project without inheriting one live
workspace's target history, backend URLs, or batch state.

This template is intentionally minimal:

- no fixed target class
- no fixed API endpoint
- no fixed peptide source
- no assumption that preview output is already trustworthy

It is not a runnable software package by itself.
It is a clean scaffold plus the minimum documents needed to begin correctly.

## Folder Map

```text
starter-template/
  README.md
  config/
    target_spec.json
    reference_complexes.json
    hardware_profile.json
  queries/
    reference_panel.json
    candidate_panel.json
  docs/
    phase0_environment_check.md
    phase1_target_freeze.md
    phase2_reference_preview.md
    phase3_batch_plan.md
    phase4_upgrade_validation.md
    phase5_closeout.md
    negative_result_template.md
    pause_state.md
  pipeline/
    README.md
    manifests/
  upload_ready/
    _HOW_TO_USE.md
```

Create these folders only when the project reaches the point where they have
real contents:

- `research/` for target biology, sequence provenance, and control rationale
- `results/` for local preview outputs, rejected designs, and raw promotion inputs
- `validation/` for upgraded validation outputs

Keep `upload_ready/` in the template because platform packaging is an explicit
end-state contract. It must stay empty except for `_HOW_TO_USE.md` until a
design actually passes the promotion gate.

## Minimum Startup Sequence

1. Fill `config/target_spec.json`
2. Fill `config/reference_complexes.json`
3. Fill `config/hardware_profile.json`
4. Fill `queries/reference_panel.json`
5. Write `docs/phase0_environment_check.md`
6. Document the exact smoke/preview/upgrade commands in `pipeline/README.md`
7. Decide the query naming pattern in `docs/phase1_target_freeze.md`
8. Decide whether the project is local-only or platform-writing
9. Decide where manifests and resume state will live
10. Run one smoke test before any large batch

Required explicit choices in `config/target_spec.json`:

- `downstream_mode`: `local_only` or `platform_writeback`
- `canonical_structure_format`: `cif` or `pdb`
- `state_file`: canonical resume path

## First Hardening Step

Before any real run, fill these three things first:

1. `pipeline/README.md`
2. the active phase doc, usually `docs/phase0_environment_check.md`
3. the initial `state.json` location and contents

Reason:

- these three files define the runnable command contract, the live execution
  gate, and the resume path

If those three are still vague, the project is not execution-ready.

For platform-bound projects, also fill:

- downstream write-back expectation in `pipeline/README.md`
- whether `.pdb` or `.cif` will be the canonical structure format

## Non-Negotiable Rule

Do not create a large candidate or backfill panel until:

- the environment is proven
- sequence sources are recorded
- at least one real reference exists
- at least one real negative exists
- you know what preview mode is allowed to claim
