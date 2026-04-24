# Phase 1 — Reference Calibration

## Goal

Prove that the fixed-backbone target-decoy lane can distinguish the corrected
DF-3 reference on the real target from structural decoys.

## Panel

See:

- [reference_panel.json](../candidates/reference_panel.json)

## Why These Rows

### `df3_real`

Needed because a campaign must anchor on a verified positive, not internal lore
or a stale candidate dump.

### hotspot-killed receptor decoy

Mutates the original contact patch to Ala. This asks whether the peptide depends
on the intended Myostatin interface rather than generic surface contact.

### rotated peptide decoy

Moves the peptide away from the intended placement. This asks whether the lane
can reject a geometrically broken complex.

## Pass Condition

A sane lane should show:

- strongly negative real-target `interface_dG`
- weaker hotspot-killed decoy `interface_dG`
- near-zero rotated-decoy `interface_dG`

## Fail Condition

If:

- the hotspot-killed decoy scores like the real target, or
- the rotated decoy still appears favorable,

then the lane is not ready for candidate ranking.

## Main Lesson

Do not rank candidates before learning whether the lane respects target decoys.
