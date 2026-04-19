# Phase 0 — Environment Check

Goal:

- verify OF3-MLX runs on the intended Apple Silicon machine

Record:

- exact command used
- runner YAML
- entrypoint path
- output directory shape
- weights hash
- any warnings or caveats
- where `state.json` will live during execution
- whether the run is `local_only` or `platform_writeback`

Gate:

- at least one smoke-test prediction completes and writes outputs

Startup priority:

- this should be the first active phase doc filled before any real run

Definition of done:

- one smoke-test run completed
- the exact command, manifest location, and state path are written here
