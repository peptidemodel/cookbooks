---
name: peptide-mlx-research-ops
description: >
  Run or supervise intermediate peptide-target structural prediction projects
  using OpenFold3-MLX on Apple Silicon. Use for state recovery, reference
  calibration, preview-vs-upgrade decisions, batch orchestration, manifest
  discipline, and honest treatment of failures in peptide-target prediction
  campaigns.
---

# peptide-mlx-research-ops

Use this skill when the task is not a one-off OF3 command but an ongoing
peptide-target MLX research campaign with phases, controls, batches, and resume
state.

Read these only when needed:

- [references/gates.md](references/gates.md) for phase gates and stop conditions
- [references/escalation.md](references/escalation.md) for when to spend more
  compute or ask for more provenance

## Default workflow

1. Recover state before acting.
2. Classify the lane.
3. Decide whether the next step is:
   - environment proof
   - target freeze
   - reference preview
   - batch planning
   - upgraded validation
   - closeout or pause
4. Only run more compute if the prerequisite gate passed.
5. Preserve negative results explicitly.
6. Report the gate verdict and exact files, not vague summaries.
7. End every experiment with a human-readable conclusion, not just manifests.

## State recovery

Before changing code or launching compute:

1. Read the project root `README.md`.
2. Read the latest phase report in `docs/`.
3. Read the active config and query panel.
4. Read the latest machine-readable result in `results/` or `validation/`.
5. Check for pause or state files.

Identify:

- target sequence source
- peptide panel source
- preview sample count
- upgrade trigger
- current failure class

If any of those five are unclear, do not start a new batch.

## Lane classification

Treat the current state as one of these:

- `environment not proven`
- `spec-layer issue`
- `reference lane not proven`
- `preview-only lane`
- `upgrade-ready lane`
- `paused backfill`

Say explicitly which one it is before moving on.

## When to run more compute

Run more compute only if:

1. the environment is proven,
2. target and peptide provenance are recorded,
3. at least one real reference exists,
4. at least one real negative or counter-screen exists,
5. the next run would change a real decision.

Do **not** run more compute when:

- preview never separated controls,
- query naming or sequence provenance is ambiguous,
- the same failure keeps recurring without classification,
- the batch is not resumable.

## How to treat results

Always separate:

- what preview mode can actually claim
- what upgraded validation can claim

Typical pattern:

- smoke test: environment proof only
- preview mode: existence proof or broad triage
- upgrade mode: stronger promotion or rejection decisions

Do not let one-sample preview output quietly become your final ranking lane.

## Commit and reporting discipline

Every meaningful report should include:

- gate verdict: `PASS` / `FAIL` / `PAUSED`
- the exact reason
- authoritative files
- whether the lane is preview-only or upgrade-ready
- next step

## Required end-of-experiment outputs

When an experiment is complete:

1. print a short plain-language conclusion directly in chat
2. decide publish vs do-not-publish using the cookbook promotion gate
3. create `upload_ready/` folders only for promoted designs
4. write `research_log.md` for failures, lessons, and reproducibility

The chat conclusion must:

- say what happened in plain language
- name the best result and why it is interesting
- be honest about failures
- say clearly whether anything should be published
- suggest specific next experiments

Do not leave the user with only raw manifests, TSVs, JSONs, and structure files.

For `upload_ready/<design>/card.yaml`:

- use platform field names exactly
- resolve targets to platform slug arrays
- include `parent_card` when the design descends from an existing platform card
- use only platform statuses such as `computed`
- do not invent fields like `mode`, `main_metric`, or `pdb_path`
