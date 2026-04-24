# Upload Ready

This folder is the platform packaging boundary.

Keep this folder in every project so the final destination is obvious from day
one. Do not put working outputs, rejected designs, raw result bundles, or
scratch notes here.

Create one folder per promoted design only after the promotion gate passes:

```text
upload_ready/
  design_slug/
    card.yaml
    structure.pdb
    readme.md
```

`card.yaml` should map directly to the PeptideModel upload form and reference
the files beside it:

```yaml
title: "Replace Me"
sequence: "REPLACE_ME"
targets:
  - replace-me
scaffold: "Replace Me"
parent_card: null
status: computed

metrics:
  - key: interface_dG
    value: 0.0
    tool: "Replace Me"

source:
  kind: cookbook
  notes: "Replace Me"

structure_file: structure.pdb
readme_file: readme.md
```
