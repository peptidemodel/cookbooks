# Phase 0 — Target Freeze

## Goal

Freeze the target and the interpretation layer before any candidate generation.

## Inputs

- structure: `3HH2`
- target chain: `C`
- mechanism hypothesis: short follistatin-derived peptides on the myostatin interface

## Decisions

1. Use one explicit target chain and write it down.
2. Treat residue numbering as a first-class spec item.
3. Separate real literature references from old internal sequences.

## Why This Matters

If the target chain or numbering is wrong, later hotspot occupancy and pocket-contact metrics become meaningless.

## Output

Authoritative file:

- [target_spec.json](../config/target_spec.json)

## Gate For Phase 1

Before moving on, we must have:

- one named positive control
- one obvious negative
- one provenance note for any historical internal comparator
