# Phase Verdict

Status:

- `PREVIEW`

This example is grounded in the Myostatin/GDF-8 science project and corrected
DF-3 provenance. It contains the available OF3-MLX preview artifacts for two
Myostatin cards.

## Preview Results

Run class:

- OpenFold3-MLX v0.3.1
- Apple M4 Base 16 GB
- ColabFold MSA
- one diffusion sample
- seed `42`

| Card | Sequence | ipTM | Verdict |
|---|---|---:|---|
| `pep-00127` | `VNDNTLFKWMIFNG` | 0.675 | medium-low preview signal |
| `pep-10785` | `WRQNTRYSRIEAIKIQILSKLRL` | 0.455 | weak preview signal |

## Upgrade Criteria

Upgrade only if the next run would change a real decision. A stronger follow-up
should include:

- multiple diffusion samples
- mean and standard deviation of ipTM or an equivalent MLX-native confidence
  summary
- manual structure review
- comparison against the science project's stronger AF2-Multimer/ipSAE lane
- explicit statement of whether the result is still only preview

## Not Claimed

This example does not claim:

- final binding affinity
- selectivity versus GDF11 or Activin A
- platform-ready upload status
- equivalence to Linux/GPU Rosetta target-decoy results
- reproduction of the science project's 25-seed AF2-Multimer/ipSAE results
- that `pep-00127` is a strong binder because `ipTM=0.675`

## Connection To The Science Project

The science project at `/home/now/code/peptide-play/projects/myostatin-gdf8/`
used AF2-Multimer with 25-seed statistical scoring and ipSAE-style evaluation.
This MLX example shows available OF3-MLX single-seed preview results for the
same Myostatin/GDF-8 narrative. It is a lightweight Mac preview lane, not a
replacement for the full statistical analysis.
