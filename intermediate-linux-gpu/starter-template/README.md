# Starter Template — PeptideModel Linux/GPU Project

This is the public, neutral starter template for PeptideModel platform users.

Use this when you want to start a peptide research project **without** inheriting this repo's project-specific assumptions, runner names, or target history.

This template is intentionally generic:

- no fixed model stack
- no fixed target class
- no fixed scoring metric
- no assumption that Boltz, AF2, or PyRosetta is the first lane

It is for:

- peptide binders
- peptide modulators
- peptide antagonists
- peptide agonist optimization
- short peptide interface-mimic projects

It is **not** a runnable software package by itself.
It is a clean project scaffold plus the minimum documents needed to start correctly.

## When To Use This

Use this starter template if:

- you are starting from zero
- you are outside this repo
- you do not want to inherit our local tooling choices
- you want a portable teaching template

Use `projects/_template/` instead if:

- you are working inside this repo
- you want the existing local runner and notebook conventions immediately

## Folder Map

```text
starter-template/
  README.md
  README.research.md
  config/
    target_spec.json
    reference_peptides.json
    counter_screens.json
  candidates/
    reference_panel.json
    candidate_panel.json
  docs/
    phase0_target_freeze.md
    phase1_reference_calibration.md
    phase2_target_decoy.md
    phase3_candidate_panel.md
    phase4_filtering.md
    phase5_closeout.md
    negative_result_template.md
    pause_state.md
  pipeline/
    README.md
    manifests/
  validation/
    README.md
  research/
    README.md
  results/
    README.md
  upload_ready/
    README.md
```

## Minimum Startup Sequence

1. Fill `config/target_spec.json`
2. Fill `config/reference_peptides.json`
3. Fill `candidates/reference_panel.json`
4. Write `docs/phase0_target_freeze.md`
5. Choose your cheap lane and strong lane in `pipeline/README.md`
6. Document your stronger validation lane in `validation/README.md`
7. Decide whether the project is local-only or platform-writing
8. Decide the canonical structure format and state path
9. Run Phase 1 on references before generating a real candidate panel
10. If the project is platform-bound, create `upload_ready/<design>/card.yaml`
    only for designs that actually passed the promotion gate

## First Hardening Step

Before any real run, fill these three things first:

1. `pipeline/README.md`
2. the active phase doc, usually `docs/phase0_target_freeze.md`
3. the initial `pipeline/manifests/state.json`

Reason:

- these define the runnable command contract, the live execution gate, and the
  resume path

## Non-Negotiable Rule

Do not create a large candidate panel until:

- target numbering is frozen
- at least one positive reference exists
- at least one real negative exists
- you know how the next phase will be judged
- you know whether successful runs stay local or are written to the platform

For platform-bound work, success is not just a Markdown closeout.
Success also requires a valid `upload_ready/<design>/card.yaml` plus matching
`structure.pdb` and `readme.md` for each promoted design.
