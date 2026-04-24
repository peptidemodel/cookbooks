# Myostatin / GDF-8 Preview — MLX Worked Example

This is the standalone MLX worked example for the MLX cookbook.

It uses the same Myostatin/GDF-8 scientific story as the Linux/GPU cookbook, but
expresses it as an MLX preview workflow so Mac users do not need to open the
Linux folder to understand what to do.

Purpose:

- show the corrected DF-3/Myostatin reference in MLX query form
- demonstrate target, counter-screen, and chain-order discipline
- show where preview results, upgrade decisions, and upload packages belong
- make clear that preview is not final validation

## What This Example Covers

1. corrected DF-3 provenance
2. Myostatin target and related-family counter-screens
3. MLX preview query JSON
4. preview-vs-upgrade gate
5. final `upload_ready/` package shape

## Folder Map

```text
myostatin-gdf8-preview/
  README.md
  sequences.json
  config/
    target_spec.json
  query.json
  manifest.json
  phase_verdict.md
  results/
    README.md
    scores_summary.json
    pep-00127_confidences.json
    pep-00127.cif
    pep-10785_confidences.json
    pep-10785.cif
  upload_ready/
    _HOW_TO_USE.md
```

## Panel

| Card | Sequence | OF3-MLX ipTM | Identity |
|---|---|---:|---|
| `pep-00127` | `VNDNTLFKWMIFNG` | 0.675 | corrected Takayama DF-3 |
| `pep-10785` | `WRQNTRYSRIEAIKIQILSKLRL` | 0.455 | myostatin prodomain minimum peptide |

## Main Teaching Point

The corrected reference matters.

In the science project, the historical sequence `TPTKMSPINMLYFN` was corrected:
it is not Takayama DF-3. Real DF-3 is `VNDNTLFKWMIFNG`, derived from the
follistatin segment in `3HH2`.

MLX preview should therefore start from the corrected DF-3 reference, test
counter-screens, and promote only after stronger validation.

This MLX example is deliberately modest: only two OF3-MLX Myostatin cards were
available. The science project used AF2-Multimer with 25-seed statistical
scoring and ipSAE-style evaluation; these single-seed OF3-MLX preview scores do
not reproduce or replace that stronger lane.
