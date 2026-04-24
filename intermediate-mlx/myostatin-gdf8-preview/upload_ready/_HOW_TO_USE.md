# Upload Ready

This is the platform packaging boundary.

Do not add preview results here. Create a design folder only after upgraded
validation passes.

Expected final shape:

```text
upload_ready/
  design_slug/
    card.yaml
    structure.cif
    readme.md
```

Example card shape:

```yaml
title: "DF-3 / Myostatin preview-derived candidate"
sequence: "REPLACE_WITH_VALIDATED_SEQUENCE"
targets:
  - myostatin
scaffold: "DF-3-derived"
parent_card: null
status: computed

metrics:
  - key: ipTM
    value: 0.0
    tool: "OpenFold3-MLX"
    run_class: upgraded_validation

source:
  kind: cookbook
  notes: "Promoted only after upgraded validation; preview alone is insufficient."

structure_file: structure.cif
readme_file: readme.md
```
