# Workflow

## The Real Loop

Use this loop for an intermediate research project:

1. Freeze the target spec
2. Build a reference panel
3. Validate the lane on references and negatives
4. Generate a candidate panel
5. Score candidates
6. Promote only what survives orthogonal checks
7. Write a closeout before changing direction
8. If this is a platform run, package the results into the platform deliverable
   layer

That is the project loop. Not every run is a design run.

## Phase System

### Phase 0: Target Freeze

Goal:
- define the receptor / target structure and hotspot map correctly

Outputs:

- `target.pdb`
- hotspot list
- chain mapping note
- reference peptides table

Do not proceed if:

- chain IDs are unclear
- source numbering vs predicted numbering is not reconciled
- you do not know what the positive control is

### Phase 1: Reference Calibration

Goal:
- show the lane behaves sensibly on known positives and known negatives

Minimal panel:

- 1 real positive control
- 1 weaker or proxy positive
- 1 poly-Ala or composition-only negative
- 1 scrambled or wrong-order negative

What you are checking:

- does the lane recover the known pose or at least the known pocket?
- does it separate real from obviously bad controls?

If not:
- stop
- do not move into candidate ranking

### Phase 2: Target-Decoy Specificity

Goal:
- stress the lane against adversarial false positives

Typical decoys:

- hotspot-killed receptor
- rotated cavity decoy
- intracellular-face decoy

What you want:

- real target better than decoys for real positives
- negatives should not survive cleanly

If scrambled or poly-Ala still scores as a winner, do not treat the lane as sequence-specific.

### Phase 3: Candidate Design

Goal:
- build a disciplined candidate panel

Rules:

- organize candidates into explicit SAR series
- keep clear hypotheses per series
- include negatives inside the same panel
- keep references in the same file for direct comparison

Good series examples:

- N-terminal bulk scan
- aromatic handle swap
- C-terminal charge edits
- hybrid reference-chimera series
- explicit collapse negatives

The point is not “more sequences.” The point is interpretable movement.

### Phase 4: Candidate Filtering

Goal:
- remove candidates that fail geometry, specificity, or developability

Important lesson from this repo:

Sometimes the structure lane should only be used as a **geometry gate**, not a ranking function.

If energy-like scores are noisy but geometry is still informative:

- use geometry to pass/fail candidates
- rank surviving candidates on a separate, justified axis

Examples of separate axes:

- permeability proxy
- synthetic simplicity
- selectivity margin
- hotspot occupancy

### Phase 5: Closeout And Packaging

Goal:
- produce a short list with honest caveats, a human-readable conclusion, and
  platform-ready packaging for promoted designs

Each finalist should have:

- sequence
- why it survived
- what lane it passed
- what lane still looks weak
- what assumption remains unverified
- whether it was written into the PeptideModel platform

Do not write the final report like marketing. Write it like a controlled engineering summary.

Required outputs at the end of every experiment, in this order:

1. print a short plain-language conclusion directly in the chat
2. create `upload_ready/` folders for promoted designs only
3. write a local `research_log.md` for failures, lessons, and reproducibility

The chat conclusion is the primary output the person sees first.
Do not make the human dig through TSVs, JSONs, and PDB paths to understand what happened.

The conclusion must:

- say what happened in plain language
- name the best result and why it is biologically interesting
- say honestly how many designs failed and normalize that
- say clearly whether anything should be published
- suggest specific next experiments

Keep it short and readable in the terminal.

Promotion gate:

Pass:

- `ipTM >= 0.80` for peptides longer than 27 residues
- or `ipSAE_d0chn >= 0.75` for peptides 27 residues or shorter
- candidate differs from the parent or reference by at least 1 residue
- a valid PDB file exists
- candidate is not the parent or reference itself

Fail:

- everything else

If all designs fail the gate:

- say so directly in the chat conclusion
- do not create a design folder under `upload_ready/`
- keep the designs in local `results/`
- explain what failed in `research_log.md`
- suggest what to try next

Packaging rules for promoted designs:

- create `upload_ready/<design>/card.yaml`
- create `upload_ready/<design>/structure.pdb`
- create `upload_ready/<design>/readme.md`
- use platform field names exactly
- resolve targets to platform slugs before writing `card.yaml`
- include `parent_card` when the design descends from an existing platform card
- use platform statuses only: `designed`, `computed`, `reproduced`, `synthesized`, `bioassayed`

Do not invent extra platform status levels or closeout levels.

## Cheap Lane vs Strong Lane

### Cheap Local Lane

Use for:

- hypothesis grinding
- broad candidate triage
- testing whether a surface gives any coherent models at all

Examples from this repo:

- `Boltz-1` local pipeline on the M40

Do not use it for:

- final synthesis ranking
- very fine SAR claims
- close calls among short peptides

### Strong Validation Lane

Use for:

- target-decoy checks
- better structure prediction
- corrected interface metrics
- final shortlist justification

Examples from this repo:

- AF2 / Colab with corrected `ipSAE_d0chn`
- PyRosetta target-decoy validation

## What To Log Every Phase

Minimum per phase:

- what was the goal?
- what exact inputs were used?
- what was the gate?
- did it pass?
- what files are authoritative?

If you cannot answer those five, the phase is not documented enough.

## Platform Write-Back Rule

If the project is meant for PeptideModel platform ingest, do not stop at local
files only.

A platform-ready run should preserve:

- local result artifacts
- local manifest or provenance note
- backend prediction payload fields
- final relative `.pdb` or `.cif` path contract
- `upload_ready/<design>/card.yaml` for repo-local publication packaging

Do not put rejected designs or pipeline intermediates into `upload_ready/`.

## Structural Export Rules

For platform-facing closeout, make these explicit:

- which model is the canonical exported structure
- whether `.pdb` or `.cif` is the canonical public format
- whether chain IDs were normalized
- what confidence or ranking metrics travel with the export

Do not leave the exported structure choice implicit when multiple models exist.

## Common Failure Modes

### 1. Numbering Bug

Symptom:
- everything scores near zero or everything passes nonsense controls

Cause:
- source numbering and predicted numbering differ

Fix:
- explicitly map the target residues

### 2. Sequence-Insensitive Lane

Symptom:
- scrambled control beats the real binder
- poly-Ala survives

Interpretation:
- your lane is not sequence-specific enough for ranking

Response:
- demote it to geometry-only or discard it

### 3. Proxy Overreach

Symptom:
- a hand-tuned developability proxy starts driving major decisions

Interpretation:
- useful for ranking
- dangerous as a truth model

Response:
- add orthogonal descriptor checks
- use it as one axis, not the whole claim

### 4. Overclaiming From One Lane

Symptom:
- “top hit” chosen from one metric without adversarial checks

Response:
- add negative controls and target-decoys before claiming anything

## The Engineer’s Rule

When a lane fails, preserve the negative result and reframe the lane.

Do not silently swap methods and pretend the old one never existed.
