# Manifests

Use this folder for reproducibility manifests and batch metadata.

Typical contents:

- per-run manifest JSON
- batch summary files
- canonical `state.json`
- copied runner settings for archived runs

Minimum expectations:

- one manifest per meaningful run family
- one canonical `state.json` for resume behavior
- enough metadata to reproduce or audit the run later

Recommended contents of each manifest:

- run identity
- phase
- authority file
- model and model version
- weights hash
- runtime environment details
- query JSON path
- output directory
- downstream mode
- canonical structure format

Keep the manifest format stable within one project.

Do not treat this folder as optional bookkeeping.
For this methodology, manifests and state are part of the runnable contract.
