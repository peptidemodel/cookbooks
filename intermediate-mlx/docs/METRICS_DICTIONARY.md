# Metrics Dictionary

These metrics appeared repeatedly in the source MLX workspace. Treat them as
useful signals, not as magic truth.

## `ipTM`

Interface predicted TM-score.

Use for:

- coarse interface confidence
- broad comparison inside the same run family

Do not use alone for:

- final shortlist claims
- strong discrimination when preview mode never separated negatives

## `pTM`

Predicted TM-score for overall structure confidence.

Use for:

- gross fold sanity
- context for whether the global structure is plausible

## `sample_ranking_score`

Model-provided ranking score for a sample.

Use for:

- picking among samples from the same job

Do not over-interpret across unrelated runs without calibration.

## `avg_pLDDT`

Average predicted local distance difference test score.

Use for:

- confidence context
- quickly spotting obviously poor outputs

High `pLDDT` does not guarantee a biologically correct interface.

## `gPDE`

Global predicted distance error summary.

Use for:

- additional confidence context
- broad quality review inside one workflow

## `binding_mode_rmsd`

Useful only if you actually have multiple samples or comparable poses.

In the source workspace, this was more informative than `ipTM` for some
discrimination questions, but it required multi-sample output.

Do not claim binding-mode stability from a one-sample preview run.

## `has_clash`

Useful as a quick red flag, not as a complete validator.

## General Rule

Metrics become trustworthy only after they have been interpreted against:

- real references
- real negatives
- the same run family
- the same claim type
