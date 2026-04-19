# Pipeline

This folder is intentionally neutral.

Do not assume:

- a fixed runner name
- a fixed model family
- a fixed hardware target

Document here:

1. your cheap local lane
2. your stronger validation lane
3. the exact commands used to verify each lane
4. what each lane is allowed to claim
5. whether outputs stay local or are written to the platform
6. where manifests and state are written

## Minimum Required Notes

- cheap lane command:
- strong lane command:
- check command:
- downstream mode:
- canonical structure format:
- manifest location:
- state file location:
- current status:
- known caveats:

For platform-bound projects, also document:

- prediction write-back path or API handoff
- canonical relative `.pdb` or `.cif` path pattern
- which exported structure becomes canonical when multiple models exist

Default starter location:

- manifests: `pipeline/manifests/`
- state file: `pipeline/manifests/state.json`

First hardening priority:

- fill this file before editing later phase docs
- the active phase doc should reference the command contract written here
