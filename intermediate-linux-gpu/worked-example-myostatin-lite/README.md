# Worked Example — Myostatin Lite

This is a teaching example, not a live project.

Purpose:

- show how to go from a target idea to a usable Phase 1 setup
- demonstrate the file layout and decision logic
- show how references, negatives, and gates are written down

This example is based on the style of the real myostatin work in this repo, but it is intentionally simplified.

## What This Example Covers

1. target freeze
2. reference table
3. reference calibration panel
4. target-decoy planning
5. what a phase report should look like

It does **not** include:

- full compute outputs
- complete high-fidelity scoring
- real synthesis recommendations

## Folder Map

```text
worked-example-myostatin-lite/
  README.md
  config/
    target_spec.json
  candidates/
    reference_panel.json
  docs/
    phase0_target_freeze.md
    phase1_reference_calibration.md
    phase2_target_decoy_plan.md
```

## How To Read It

1. read [phase0_target_freeze.md](docs/phase0_target_freeze.md)
2. inspect [target_spec.json](config/target_spec.json)
3. inspect [reference_panel.json](candidates/reference_panel.json)
4. read [phase1_reference_calibration.md](docs/phase1_reference_calibration.md)
5. read [phase2_target_decoy_plan.md](docs/phase2_target_decoy_plan.md)

## Main Teaching Point

The example is deliberately boring in a good way.

It shows that before generating “interesting” candidates, you should already know:

- the target structure
- the chain and residue numbering
- the reference peptide provenance
- the negative controls
- the gate for the next phase

That discipline is what makes later results interpretable.
