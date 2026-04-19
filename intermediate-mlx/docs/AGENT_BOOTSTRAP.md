# Agent Bootstrap

Use this when a fresh Codex-style agent enters an MLX peptide project.

## Read These First

1. project root `README.md`
2. latest phase doc in `docs/`
3. `config/target_spec.json`
4. latest query panel in `queries/`
5. latest machine-readable result in `results/` or `validation/`
6. `docs/pause_state.md` if it exists

## Separate Research Lane

If a second Codex-style agent is available, use it as a separate research-support lane,
not as an in-notebook integration.

Recommended adopted subset from Codex `life-science-research`:

- `research-router-skill`
- `alphafold-skill`
- `rcsb-pdb-skill`
- `uniprot-skill`
- `bindingdb-skill`
- `chembl-skill`
- `ncbi-entrez-skill`
- `ncbi-pmc-skill`

Reference: `github.com/openai/openai/tree/master/plugins/life-science-research` — review if you need the skill patterns.

Use that lane for target-background questions, accession normalization, structure lookup,
ligand precedent, and literature follow-up while the main MLX executor owns batches,
manifests, and upgrade decisions.

## Recover These Facts Before Acting

Identify:

- target sequence source
- peptide panel source
- query naming convention
- current preview sample count
- upgrade criteria
- current failure class, if any

If any of those six are unclear, do not launch a new batch yet.

## Authority Rules

Default authority for project decisions:

- phase gate and upgrade trigger: latest active phase doc in `docs/`
- frozen structural or sequence specification: `config/`
- query naming convention: project root `README.md` or `docs/phase1_target_freeze.md`
- command contract, manifest location, and state location: `pipeline/README.md`

If two files disagree, the latest active phase doc wins for execution and the
spec files must be reconciled before the next batch.

Command-detail precedence:

- if `pipeline/README.md` and the active phase doc disagree on runnable command
  details, `pipeline/README.md` is authoritative for the command contract
- the active phase doc should reference that command contract and record any
  phase-specific caveats or temporary restrictions

If command details drift between the two, stop and reconcile before running a
new batch.

Required follow-up when root `README.md` and the active phase doc disagree:

1. follow the active phase doc for immediate execution decisions
2. record the mismatch in the next phase note or pause note
3. create an explicit reconciliation task before the next batch

Do not leave the disagreement as silent drift.

## Default Classification

Classify the project state as one of:

- `environment not proven`
- `spec-layer issue`
- `reference lane not proven`
- `preview-only lane`
- `upgrade-ready lane`
- `paused backfill`

Say the classification explicitly before proposing next steps.

## Default Next-Step Logic

If `environment not proven`:

- run only the smallest smoke test

If `spec-layer issue`:

- fix provenance, naming, or chain order first

If `reference lane not proven`:

- build or rerun the reference panel before candidate batches

If `preview-only lane`:

- use it for existence proof or triage only

If `upgrade-ready lane`:

- spend more compute only on cases that change a real decision

If `paused backfill`:

- inspect state files and resume conditions before editing automation

## Blocker Priority

If multiple blockers appear at once, resolve them in this order:

1. environment failure
2. provenance or spec mismatch
3. malformed query or naming drift
4. incoherent or low-quality outputs
5. weak control separation

Reason:

- later-stage interpretation is meaningless if the earlier layers are wrong

## Reporting Discipline

Every meaningful report back should include:

- gate verdict: `PASS` / `FAIL` / `PAUSED`
- reason
- authoritative files
- what the lane can claim
- next step

At experiment closeout, also require:

1. a short plain-language conclusion printed in chat
2. a publish / do-not-publish verdict
3. `upload_ready/` folders only for promoted designs
4. a local `research_log.md`

Do not treat raw manifests and result files as the primary user-facing output.

For `card.yaml` in `upload_ready/`:

- use platform field names exactly
- resolve targets to platform slug arrays
- include `parent_card` when applicable
- use only platform status values such as `computed`
- do not invent local pipeline fields
