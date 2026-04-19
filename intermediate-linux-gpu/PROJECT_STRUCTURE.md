# Project Structure

## The Base Layout

Use a clean per-target folder. The minimal structure is:

```text
my-project/
  README.md
  README.research.md
  config/
    target.pdb
    peptide_config.py
    target_structures.json
    pocket_definition.json
  pipeline/
    run_experiment.py
    score.py
  colab/
    setup_pipeline.ipynb
  docs/
    APPROACH.md
    program.md
  research/
    target_brief.md
    openalex_queries.json
  results/
  upload_ready/
```

This is close to the repo template in `projects/_template/`.

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

Contains runnable code, not notes.

Typical responsibilities:

- build candidate complexes
- run local prediction / docking
- score structures
- emit machine-readable outputs
- define downstream write-back expectations when the project targets the platform

Rule:
- do not mix scratch outputs into the pipeline code folder itself unless the pipeline is explicitly designed that way

### `colab/`

Contains portable high-fidelity runs:

- notebook
- notebook generator
- bundle scripts for remote execution

This lane is slower and more expensive. Use it after you have something worth validating.

### `docs/`

Contains project decisions and operating notes:

- why this target
- what the current phase means
- what the current scoring lane can and cannot claim

If someone joins late, `docs/` is where they recover context.

### `research/`

Contains the scientific basis:

- internal summaries
- structure notes
- exported search results

Do not bury key scientific assumptions only in chat.

### `results/`

Contains clean experiment outputs that belong to the project.

Examples:

- reference-panel summaries
- phase reports
- selected PDBs
- TSV rankings
- all working outputs, including rejected designs and raw promotion inputs

### `upload_ready/`

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

For platform-facing or public repos, prefer two readme layers:

- `README.md`
  - executive summary
  - why the project matters
  - what the main result is
- `README.research.md`
  - technical reproduction notes
  - lane descriptions
  - artifacts and command references

This avoids forcing one file to serve two incompatible audiences.

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
