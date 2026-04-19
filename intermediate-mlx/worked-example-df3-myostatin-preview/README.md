# Worked Example — DF3 Myostatin Preview

This is a teaching example, not a live project.

Purpose:

- show how to go from a real peptide-target reference idea to a usable OF3-MLX
  preview panel
- demonstrate target-versus-counter-screen structure in query JSON
- show what a cautious preview-phase report looks like

This example is based on real patterns seen in the source `openfold-3-mlx`
workspace, but it is simplified and intentionally conservative.

## What This Example Covers

1. target freeze
2. reference and counter-screen setup
3. preview reference panel construction
4. why preview is still not the same as final validation

## Folder Map

```text
worked-example-df3-myostatin-preview/
  README.md
  config/
    target_spec.json
  queries/
    reference_panel.json
  docs/
    phase1_target_freeze.md
    phase2_reference_preview.md
    phase3_upgrade_plan.md
```

## Main Teaching Point

A clean preview panel is already useful if it shows:

- the target sequence source
- the peptide source
- at least one counter-screen or related target
- what preview mode is and is not allowed to claim
