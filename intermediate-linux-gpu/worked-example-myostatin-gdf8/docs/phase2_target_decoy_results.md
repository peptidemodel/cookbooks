# Phase 2 — DF-3 Target-Decoy Results

Fixed-backbone Rosetta interface analysis using the crystal-derived Takayama
DF-3 segment from `3HH2`.

- reference peptide: `VNDNTLFKWMIFNG`
- interface definition: `AB_C`
- receptor contact residues mutated to Ala in hotspot-killed decoy:
  `A27, A28, A29, A31, A32, A84, A86, A87, A88, A89, A91, A98, B49, B50, B56, B59`

| Case | interface_dG | dSASA | interface residues | atom contacts |
|---|---:|---:|---:|---:|
| real_target_df3 | -23.120 | 1137.0 | 39 | 739 |
| hotspot_killed_decoy_df3 | -11.654 | 813.9 | 40 | 279 |
| rotated_decoy_df3 | 0.000 | 0.0 | 0 | 0 |

## Readout

- real target vs hotspot-killed decoy delta: `11.466`
- real target vs rotated decoy delta: `23.120`

Interpretation:

- the corrected DF-3 pose depends on the intended contact patch
- the lane rejects a geometrically displaced peptide
- this is a specificity preflight, not a wet-lab potency claim

## Gate

Only after this phase should candidate variants be compared in the same
target-decoy frame.
