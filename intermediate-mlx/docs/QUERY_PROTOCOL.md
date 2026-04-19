# Query Protocol

## Core Rule

Keep every OF3-MLX query explicit, reproducible, and boring.

The minimum query JSON should make these things obvious:

- seed
- query name
- chain order
- molecule type
- exact sequences

## Minimal Shape

```json
{
  "seeds": [42],
  "queries": {
    "query_name_here": {
      "chains": [
        {
          "molecule_type": "protein",
          "chain_ids": ["A"],
          "sequence": "TARGET_SEQUENCE"
        },
        {
          "molecule_type": "protein",
          "chain_ids": ["B"],
          "sequence": "PEPTIDE_SEQUENCE"
        }
      ]
    }
  }
}
```

## Naming Rules

Query names should be:

- unique inside the batch
- stable across reruns
- informative enough to recover the target and peptide identity

Default pattern:

- lowercase ASCII only
- tokens separated by underscores
- recommended shape: `{target}_{panel_or_card}_{mode}`

Recommended regex:

```text
^[a-z0-9]+(?:_[a-z0-9]+){1,5}$
```

Examples:

- `df3_myostatin_ref`
- `ace_card0042_preview`
- `glp1r_panela_upgrade`

Bad:

- `test1`
- `query_final_really_final`

Good:

- `df3_myostatin_ref`
- `ace_card_0042_preview`
- `myostatin_candidate_a_preview`

## Chain Rules

Default convention:

- chain `A` = target
- chain `B` = peptide

If you change that, document it in the phase note and manifest.

## Batch Rules

Group by target when possible.

Reason:

- target MSA work is one of the real bottlenecks
- grouped batches make caching and runtime interpretation easier

## Non-Canonical Handling

If residues are proxied or simplified:

- state that explicitly
- preserve the original source sequence elsewhere
- add a warning field in the manifest or result record

Do not silently convert a sequence and keep the same label.

## Output Expectations

For every batch, preserve:

- query JSON
- runner YAML reference
- per-query metrics summary
- manifest or batch metadata
- state snapshot if the run was resumable

## Default Separation Language

When writing a phase report, do not use vague phrases like “looks good.”

Use one of:

- `controls clearly separated`
- `controls directionally separated`
- `controls not separated`

If you say `directionally separated`, explain exactly which metric or review
criterion moved in the expected direction.
