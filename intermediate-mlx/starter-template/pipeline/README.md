# Pipeline

Document here:

1. the smoke-test command
2. the preview command
3. the upgrade command
4. where manifests are written
5. how resume state is persisted
6. whether outputs stay local or are written to the platform

Minimum required notes:

- smoke-test command:
- preview command:
- upgrade command:
- current runner YAML:
- current entrypoint:
- manifest location:
- state file location:
- downstream mode:
- canonical structure format:
- known caveats:

Default starter location:

- manifests: `pipeline/manifests/`
- state file: `pipeline/manifests/state.json`
- structure format: `.cif` or `.pdb`, chosen explicitly per project

Command contract:

- smoke test: smallest possible query proving the environment works
- preview: reference or triage panel with the project's default sample count
- upgrade: smaller curated panel with stronger settings that can change a real
  decision

If these commands are not yet runnable, say that explicitly here rather than
leaving them implicit.

Validation checklist before first real batch:

- one smoke-test command has completed successfully
- manifest example has been copied and filled for the run family
- query JSON passes basic JSON validation
- placeholder preflight check passes
- strict schema validation passes
- output path is fixed and documented
- upgrade trigger source-of-truth file is named
- downstream sink is named if the run is platform-bound

First hardening priority:

- fill this file before editing batch plans or upgrade docs
- the active phase doc should reference the command contract written here

Recommended preflight guard:

```bash
python3 scripts/preflight_validate.py
```

This should fail if placeholder strings such as `replace-me`,
`TARGET_SEQUENCE_HERE`, or `REPLACE_ME` are still present.

Recommended strict schema check:

```bash
python3 scripts/validate_schema.py
```

This should fail if required keys, enum values, or manifest/state wiring are
inconsistent.
