# Phase 0 — Target Freeze

## Goal

Freeze the Myostatin/GDF-8 reference system and interpretation layer before
candidate ranking.

## Inputs

- structure: `3HH2`
- target chain: `C`
- reference peptide: DF-3 segment `VNDNTLFKWMIFNG`
- reference complex interface: `AB_C`
- mechanism hypothesis: short follistatin-derived peptides occupy the
  myostatin interface

## Decisions

1. Anchor the example on the corrected crystal-derived DF-3 reference.
2. Treat chain IDs and residue numbering as first-class spec items.
3. Use hotspot-killed and rotated decoys before candidate claims.
4. Keep candidate outputs separate from platform promotion packages.

## Why This Matters

The real Myostatin project had enough historical attempts that provenance
discipline mattered. If the DF-3 sequence, target chain, or contact-patch
numbering is wrong, later scoring can look precise while answering the wrong
question.

## Output

Authoritative file:

- [target_spec.json](../config/target_spec.json)

## Gate For Phase 1

Before moving on, we must have:

- the corrected DF-3 positive control
- the source structure and interface definition
- explicit hotspot-killed decoy residues
- a rotated-placement decoy concept
