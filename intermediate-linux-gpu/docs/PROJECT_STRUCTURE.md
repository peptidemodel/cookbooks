# Project Structure

## The Base Layout

Use a clean per-target folder. The minimal structure is:

```text
my-project/
  README.md
  config/
    target_spec.json
    reference_peptides.json
    counter_screens.json
  candidates/
    reference_panel.json
    candidate_panel.json
  pipeline/
    README.md
    manifests/
  upload_ready/
    _HOW_TO_USE.md
  docs/
    phase0_target_freeze.md
    phase1_reference_calibration.md
    phase2_target_decoy.md
    phase3_candidate_panel.md
    phase4_filtering.md
    phase5_closeout.md
    pause_state.md
```

Create `research/`, `results/`, and `validation/` only when they have real
contents. Keep `upload_ready/` in the starter because platform packaging is a
core contract, but it should contain only `_HOW_TO_USE.md` until promotion.

## Why This Layout Works

### `config/`

Contains the frozen experimental specification:

- target structure
- hotspot residues
- chain identities
- counter-screen targets
- reference peptide definitions

If `config/` is wrong, the whole project is wrong. Treat it as the spec layer.

### `pipeline/`

Contains runner notes, command contracts, manifest format, and automation.

Typical responsibilities:

- build candidate complexes
- run local prediction / docking
- score structures
- emit machine-readable outputs
- define downstream write-back expectations when the project targets the platform

Rule:
- do not mix scratch outputs into the pipeline code folder itself unless the pipeline is explicitly designed that way

### `docs/`

Contains project decisions and operating notes:

- why this target
- what the current phase means
- what the current scoring lane can and cannot claim

If someone joins late, `docs/` is where they recover context.

### `research/`

Create only when needed.

Contains the scientific basis:

- internal summaries
- structure notes
- exported search results

Do not bury key scientific assumptions only in chat.

### `results/`

Create only when needed.

Contains clean experiment outputs that belong to the project.

Examples:

- reference-panel summaries
- phase reports
- selected PDBs
- TSV rankings
- all working outputs, including rejected designs and raw promotion inputs

### `upload_ready/`

Exists from the start because platform upload packaging is part of the cookbook
contract. Add design folders only after a design passes the promotion gate.

Contains promoted designs only.

One folder per promoted design:

- `card.yaml`
- `structure.pdb`
- `readme.md`

Do not put:

- rejected designs
- TSV or JSON pipeline intermediates
- scratch summaries
- raw result bundles

## The Project Root `README.md`

Every project root should answer:

1. What is the target?
2. What is the mechanism hypothesis?
3. What is the main structure or receptor used right now?
4. What is the current phase?
5. What is the active phase doc path?
6. Which files are the authoritative outputs?
7. Is this run local-only or intended for platform write-back?

If the root `README` cannot answer those seven, the project is not handoff-ready.

## README Split Guidance

For larger platform-facing or public projects, two readme layers can be useful:

- `README.md`
  - executive summary
  - why the project matters
  - what the main result is
- `README.research.md`
  - technical reproduction notes
  - lane descriptions
  - artifacts and command references

This avoids forcing one file to serve two incompatible audiences.

Do not add `README.research.md` to the starter template until there is enough
technical reproduction detail to justify a second root file.

## The Single Most Important Structural Rule

Keep target numbering explicit.

Always document:

- source PDB chain
- source residue numbering
- predicted-complex renumbering, if different
- the exact residue list used by the scorer

This repo hit this failure mode multiple times:

- target pocket was biologically right
- but residue numbering in the scorer was wrong
- all downstream rankings looked broken until the mapping was fixed

Do not leave numbering implicit.
