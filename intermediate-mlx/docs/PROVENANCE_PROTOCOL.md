# Provenance Protocol

Every meaningful OF3-MLX result should have a reproducibility manifest.

## Minimum Manifest Fields

At minimum, record:

- `model`
- `model_version`
- `weights_hash`
- `hardware`
- `python_version`
- `mlx_version`
- `runner_yaml`
- `random_seed`
- `num_diffusion_samples`
- `msa_strategy`
- `predicted_at`

## Also Preserve

- the exact query JSON
- the output directory
- warnings such as proxied residues
- batch identifier if part of a long run

## Why This Matters

Without a manifest, later debugging becomes ambiguous:

- was the difference biological?
- was it a sample-count change?
- was it a weights change?
- was it a hardware or environment change?

## Sequence Provenance Rule

For every peptide and target in a meaningful panel, preserve:

- source identifier
- exact sequence used in the run
- whether the sequence was proxied or simplified
- any counter-screen relationship

## Naming Rule

Do not reuse labels carelessly.

If the sequence changes, or the proxy status changes, change the label or add a
clear suffix. A convenient old name is not worth provenance drift.
