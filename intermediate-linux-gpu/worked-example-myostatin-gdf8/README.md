# Worked Example — Myostatin / GDF-8

This is the single representative Myostatin example for the cookbooks.

It is a compact public example extracted from the real science workspace at
`/home/now/code/peptide-play/projects/myostatin-gdf8`, with heavy raw artifacts,
model outputs, notebooks, and local machine paths removed.

Purpose:

- show the approach that best represents the current PeptideModel method
- anchor on a corrected DF-3/myostatin reference instead of internal lore
- demonstrate phase-gated target-decoy validation before candidate claims
- preserve negative controls and interpretation limits

This is not a live result bundle. It is a curated teaching copy of the method.

## What This Example Covers

1. target freeze
2. reference and provenance correction
3. DF-3 target-decoy preflight
4. candidate target-decoy comparison
5. cautious claims from a structural scoring lane

It does **not** include:

- full raw PDB output sets
- notebooks
- copied model weights
- real synthesis recommendations

## Folder Map

```text
worked-example-myostatin-gdf8/
  README.md
  config/
    target_spec.json
  candidates/
    reference_panel.json
  docs/
    phase0_target_freeze.md
    phase1_reference_calibration.md
    phase2_target_decoy_results.md
    phase3_candidate_target_decoy_results.md
  upload_ready/
    v41f_w49f_i51v/
      card.yaml
      structure.pdb
      readme.md
```

## How To Read It

1. read [phase0_target_freeze.md](docs/phase0_target_freeze.md)
2. inspect [target_spec.json](config/target_spec.json)
3. inspect [reference_panel.json](candidates/reference_panel.json)
4. read [phase1_reference_calibration.md](docs/phase1_reference_calibration.md)
5. read [phase2_target_decoy_results.md](docs/phase2_target_decoy_results.md)
6. read [phase3_candidate_target_decoy_results.md](docs/phase3_candidate_target_decoy_results.md)
7. inspect [upload_ready/v41f_w49f_i51v](upload_ready/v41f_w49f_i51v)

## Main Teaching Point

The example shows the discipline that made the real Myostatin work interpretable:

- the target structure
- the chain and residue numbering
- the reference peptide provenance
- the decoy construction
- the gate between reference validation and candidate claims

Do not rank candidates until the lane has shown that the known reference depends
on the intended contact patch and separates from decoys.

## Upload Package

The example includes one concrete final package:

- [upload_ready/v41f_w49f_i51v](upload_ready/v41f_w49f_i51v)

This shows the expected Linux/GPU end state: a platform card, a `structure.pdb`,
and a short design readme. It is a worked-example artifact, not a wet-lab claim.
