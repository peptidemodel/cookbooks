---
name: peptide-research-ops
description: >
  Run or supervise intermediate peptide-target research projects in the style
  used in this repo. Use for peptide binder or modulator campaigns where you
  need to recover project state, validate the scoring lane, decide when to
  read more primary papers, decide when to run experiments, decide when to
  stop and ask the supervisor, treat negative results correctly, and hand off
  clean phase outputs.
---

# peptide-research-ops

Use this skill when the task is not a one-off script but an ongoing peptide research campaign with phases, controls, references, target-decoys, and cross-agent supervision.

The coordination method is optional:

- use a messaging layer such as Patchcord if available
- otherwise run the same method in stricter sequence with written checkpoints

Read these only when needed:
- [references/gates.md](references/gates.md) for phase gates and stop conditions
- [references/escalation.md](references/escalation.md) for when to request papers, scientific review, or more compute

## Default workflow

1. Recover state before acting.
2. Classify the current lane.
3. Decide whether the next step is:
   - spec fix
   - reference calibration
   - target-decoy validation
   - candidate generation
   - candidate filtering
   - closeout / reporting
4. Only run new experiments if the lane has passed the prerequisite gate.
5. Preserve negative results explicitly.
6. Report the gate verdict and exact files, not vague summaries.
7. End every experiment with a human-readable conclusion, not just artifacts.

## State recovery

Before changing code or launching compute:

1. Read the project root `README.md`.
2. Read the latest phase report(s) in `docs/`.
3. Read the latest machine-readable result in `pipeline/` or `results/`.
4. Check whether the working tree has uncommitted scientific outputs that matter.
5. Identify:
   - current target structure
   - current hotspot / residue-numbering convention
   - current positive controls
   - current negatives
   - current gate condition

If any of those five are unclear, do not start a new design sweep.

## Lane classification

Treat the current project state as one of these:

- `spec-layer issue`
  - wrong chain
  - wrong numbering
  - wrong reference sequence
- `reference lane not proven`
  - no positive/negative controls yet
- `sequence-insensitive lane`
  - scrambled or poly-Ala survives
- `geometry-only lane`
  - useful for pocket occupancy, not ranking
- `usable ranking lane`
  - real controls beat decoys and negatives cleanly

Say explicitly which one it is before moving on.

## When to run more experiments

Run more experiments only if:

1. target numbering is frozen,
2. at least one positive control is defined,
3. at least one real negative is defined,
4. the current lane passed the prerequisite gate for the next phase.

Do **not** run more candidate batches when:

- scrambled beats real,
- poly-Ala survives,
- a positive control cannot recover the expected pocket,
- the target spec may still be wrong.

In those cases, fix the lane or reframe it.

## How to treat results

Always separate:

- `what the lane can actually claim`
- `what the lane cannot claim`

Typical pattern:

- cheap local lane: hypothesis grinder only
- Rosetta / AF2 lane: target-decoy or geometry gate
- permeability / chemistry proxy: ranking aid, not truth model

Do not let a weak lane silently become the main ranking function.

When a lane fails:

- write a negative-result doc,
- keep the artifacts,
- reframe the lane if still useful,
- stop pretending it is a valid scorer.

## When to request more primary papers

Request or obtain more papers before making a factual claim if any of these are true:

- a reference peptide sequence came from repo lore rather than primary source
- target mechanism is being asserted from summaries only
- exact medicinal chemistry substitutions matter for SAR
- a benchmark peptide is being used as a named literature anchor
- a paper-derived number is driving a gate or ranking rule

For provenance or benchmark disputes, primary papers beat cached summaries.

## When to ask the scientific reviewer or supervisor

Escalate to the active scientific supervisor, designated reviewer, or human user when:

- two lanes disagree and the interpretation changes project direction
- the current phase failed but there are multiple plausible rescue paths
- the biology target framing changes
- a lane needs to be reframed from ranking to geometry-only
- a synthesis shortlist would otherwise be built on ambiguous evidence

Do not ask the reviewer for routine file lookups or trivial bookkeeping. Ask when the scientific interpretation or phase direction is ambiguous.

## When to ask for help from another lane

Ask another specialist lane when the work is genuinely orthogonal:

- orthogonal model lane
  - conformer generation
  - orthogonal descriptor checks
  - alternative hardware or model runs
- literature lane
  - paper corpus retrieval
  - provenance verification
- review lane
  - proposal review
  - external-facing summary review

Do not delegate the main blocking work if you need the result immediately for the next local step.

## Commit and reporting discipline

Commit by phase or by real methodological change.

Every meaningful report back should include:

- gate verdict: `PASS` / `FAIL`
- the exact reason
- authoritative files
- whether the lane is ranking, geometry-only, or broken
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

Do not leave the user with a pile of TSV, JSON, and PDB files as the main output.

For `upload_ready/<design>/card.yaml`:

- use platform field names exactly
- resolve targets to platform slug arrays
- include `parent_card` when the design descends from an existing platform card
- use only platform statuses such as `computed`
- do not invent fields like `mode`, `main_metric`, or `pdb_path`

## Default outputs per phase

- `docs/<phase>.md`
- `pipeline/<phase>/...json`
- `pipeline/<phase>/...tsv`

If a phase has no markdown and no machine-readable summary, it is not complete enough for handoff.

For final closeout, also require:

- `upload_ready/<design>/card.yaml`
- `upload_ready/<design>/structure.pdb`
- `upload_ready/<design>/readme.md`
- `research_log.md`
