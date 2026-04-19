# Manifests

Use this folder for reproducibility manifests and batch metadata.

Typical contents:

- per-run manifest JSON
- canonical `state.json`
- batch summary files
- copied runner settings for archived runs

Minimum expectations:

- one manifest per meaningful run family
- one canonical `state.json` for resume behavior
- enough metadata to reproduce or audit the run later

Do not treat this folder as optional bookkeeping.
For this methodology, manifests and state are part of the runnable contract.
