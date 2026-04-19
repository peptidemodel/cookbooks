# Phase 1 — Reference Calibration

## Goal

Prove that the lane can at least distinguish a meaningful positive reference from obvious negatives.

## Panel

See:

- [reference_panel.json](../candidates/reference_panel.json)

## Why These Four Rows

### `real_df3_reference`

Needed because a campaign must anchor on a verified positive, not internal lore.

### `legacy_internal_seed`

Included because real projects usually have historical baggage. It is better to keep it as an explicit comparator than to quietly pretend it never existed.

### `scrambled_df3`

This is the first real sequence-sensitivity test.

### `poly_ala_14mer`

This is the composition floor. If it survives, something is wrong with the lane.

## Pass Condition

A sane lane should show:

- `real_df3_reference` recovering the intended target surface
- `scrambled_df3` worse than the real reference
- `poly_ala_14mer` clearly weak

## Fail Condition

If:

- scrambled behaves like the real binder, or
- poly-Ala survives,

then the lane is not ready for candidate ranking.

## Main Lesson

Do not design 30 candidates before learning whether the lane respects obvious controls.
