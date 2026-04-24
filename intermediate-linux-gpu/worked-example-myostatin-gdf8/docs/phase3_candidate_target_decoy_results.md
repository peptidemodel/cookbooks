# Phase 3 — Candidate Target-Decoy Results

Fixed-backbone Rosetta interface analysis on the candidate set requested after
the upstream MLX/OpenFold3 full-panel screen.

- reference complex: corrected DF-3/myostatin pose from `3HH2`
- interface definition: `AB_C`
- hotspot-killed receptor residues:
  `A27, A28, A29, A31, A32, A84, A86, A87, A88, A89, A91, A98, B49, B50, B56, B59`

| Candidate | Sequence | real target dG | hotspot-killed dG | rotated dG | delta vs hotspot-killed | delta vs rotated | contacts | dSASA |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| v41f_w49f_i51v | `FNDNTLFKFMVFNG` | -30.606 | -12.410 | 0.000 | 18.196 | 30.606 | 760 | 1099.3 |
| v41y_w49f_i51v | `YNDNTLFKFMVFNG` | -30.602 | -12.410 | 0.000 | 18.193 | 30.602 | 760 | 1104.3 |
| w49f_i51v | `VNDNTLFKFMVFNG` | -30.149 | -12.610 | 0.000 | 17.539 | 30.149 | 811 | 1150.9 |
| m50f_i51v | `VNDNTLFKWFVFNG` | -29.808 | -12.449 | 0.000 | 17.359 | 29.808 | 816 | 1184.3 |
| df3_real | `VNDNTLFKWMIFNG` | -29.697 | -11.654 | 0.000 | 18.043 | 29.697 | 834 | 1171.6 |
| f52y_adversarial | `VNDNTLFKWMIYNG` | -23.342 | -11.656 | 0.000 | 11.686 | 23.342 | 856 | 1189.3 |

## Interpretation

- More negative `real target dG` is better within this lane.
- Larger positive `delta vs rotated` indicates cleaner rejection of a displaced
  peptide placement.
- Larger positive `delta vs hotspot-killed` indicates dependence on the original
  `3HH2` contact patch.

## Cautious Conclusion

The best variants improve the real-target score while preserving strong decoy
separation. That supports promotion to a stronger validation lane, not a final
claim of binding potency or specificity.
