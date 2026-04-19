# Workflow

## The Real Loop

Use this loop for an intermediate MLX peptide project:

1. Freeze the environment and weights
2. Freeze target and peptide sequence sources
3. Build a reference panel
4. Run preview predictions
5. Classify the lane honestly
6. Escalate only useful cases to upgrade validation
7. Write outputs into the platform contract if this is a platform run
8. Write a closeout before changing direction

Not every run is a batch run. Sometimes the right action is to stop and fix
specification, provenance, or state handling.

## Phase System

### Phase 0: Environment Check

Goal:

- prove the Apple Silicon environment actually runs

Outputs:

- successful check command
- weights location and hash
- runner YAML choice
- hardware profile note

Do not proceed if:

- weights are missing
- the runner config is unknown
- one trivial prediction cannot complete

### Phase 1: Target Freeze

Goal:

- define target and peptide sequence sources correctly

Outputs:

- `target_spec.json`
- reference peptide list
- sequence provenance note
- preview/upgraded decision rule

Do not proceed if:

- the target sequence source is ambiguous
- a key reference is lore instead of provenance-backed
- non-canonical handling is still undefined

### Phase 2: Reference Preview

Goal:

- show that preview mode behaves sensibly on real controls

Minimal panel:

- 1 real positive or anchor complex
- 1 related target or counter-screen
- 1 scrambled, damaged, or obvious negative

What you are checking:

- does OF3-MLX produce coherent complexes at all?
- do positive and negative controls separate enough to justify more compute?
- do metrics and visuals tell the same story?

Default interpretation rule:

- `PASS`: controls clearly separated
- `SOFT PASS`: controls directionally separated and upgraded validation would
  change a real decision
- `FAIL`: controls not separated or outputs are too incoherent to interpret

If not:

- stop
- do not treat preview ranking as meaningful

### Phase 3: Batch Plan

Goal:

- structure the run before burning hours

Rules:

- group by target when MSA reuse matters
- keep query names stable and unique
- set explicit batch size and stop conditions
- define what gets written to `state.json`
- define whether the batch is local-only or backend-writing

The point is not to run more cards. The point is to run interpretable cards.

### Phase 4: Upgrade Validation

Goal:

- spend more compute only where it changes a decision

Typical upgrades:

- increase diffusion samples
- run target-decoy checks
- compare against another structure lane
- add post-hoc descriptor checks

Important lesson from the source workspace:

One-sample preview mode is useful for existence proofs and broad backfill.
It is usually not enough for strong discrimination claims.

### Phase 5: Closeout

Goal:

- produce a short list with honest caveats and a human-readable conclusion

Each promoted result should state:

- what mode it passed
- what metrics were used
- what remains uncertain
- what exact manifest reproduces it
- whether it was written into the PeptideModel platform

Required outputs at the end of every experiment, in this order:

1. print a short plain-language conclusion directly in the chat
2. create `upload_ready/` folders for promoted designs only
3. write a local `research_log.md` for failures, lessons, and reproducibility

The chat conclusion is the first thing the person should read.
Do not make them reverse-engineer the experiment from manifests and raw result files.

The conclusion must:

- say what happened in plain language
- name the best result and why it is interesting
- say honestly how many designs failed
- say clearly whether anything should be published
- suggest specific next experiments

## Preview Mode vs Upgrade Mode

### Preview Mode

Use for:

- smoke tests
- broad backfill
- reference sanity checks
- quick existence proofs

Typical pattern:

- `num_diffusion_samples = 1`
- cached or grouped MSA reuse where possible
- minimal but complete manifest logging

Do not use it for:

- strong sequence-specific ranking claims
- binding mode RMSD interpretation
- final promotion of marginal candidates

### Upgrade Mode

Use for:

- shortlisted candidates
- ambiguous but important references
- adversarial target-decoy checks
- pose stability or clustering questions

Typical pattern:

- more diffusion samples
- more careful manual inspection
- orthogonal comparison lane

## Platform Write-Back Rule

If the project is meant for PeptideModel platform ingest, do not stop at local
files only.

A platform-ready run should preserve:

- local manifest
- local structure file
- backend prediction payload fields
- final relative `pdb_path` or `.cif` path contract
- `upload_ready/<design>/card.yaml`
- `upload_ready/<design>/structure.pdb` or `.cif`
- `upload_ready/<design>/readme.md`

Promotion gate:

Pass:

- `ipTM >= 0.80` for peptides longer than 27 residues
- or `ipSAE_d0chn >= 0.75` for peptides 27 residues or shorter
- candidate differs from the parent or reference by at least 1 residue
- a valid structure file exists
- candidate is not the parent or reference itself

Fail:

- everything else

If all designs fail the gate:

- say so directly in the chat conclusion
- do not create `upload_ready/`
- keep the designs in local `results/` or `validation/`
- explain what failed in `research_log.md`
- suggest what to try next

Packaging rules for promoted designs:

- create `upload_ready/<design>/card.yaml`
- create `upload_ready/<design>/structure.pdb` or `.cif`
- create `upload_ready/<design>/readme.md`
- use platform field names exactly
- resolve targets to platform slugs before writing `card.yaml`
- include `parent_card` when the design descends from an existing platform card
- use platform statuses only: `designed`, `computed`, `reproduced`, `synthesized`, `bioassayed`

Do not invent extra platform levels or phase labels for card status.

## The Engineer’s Rule

If preview mode fails to separate controls, preserve the failure and reframe the
lane. Do not quietly tighten thresholds and keep ranking candidates anyway.
