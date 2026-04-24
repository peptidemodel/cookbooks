# PeptideModel.com Platform MLX Cookbook

This folder is a compact handover for someone who wants to run peptide-target
structure work for the PeptideModel.com platform in the style extracted from a
real `openfold-3-mlx` workspace:

- Apple Silicon first
- OpenFold3-MLX as the main structure lane
- explicit preview mode versus upgraded validation mode
- grouped batching to reuse expensive MSA work
- reproducibility manifests for every meaningful run
- pause/resume discipline for long backfills and research campaigns
- downstream write-back discipline for the PeptideModel platform

This is not a software manual for every OpenFold feature.
It is a practical operating guide for peptide-target structural work on MLX for
new PeptideModel platform users.

Important:

- this cookbook is platform-oriented, not machine-status-oriented
- it is not the status page for the original machine
- it does not define the current active batch or supervisor identity
- live project state still belongs in project-local docs

Repo role:

- treat this cookbook as the normative default for new MLX peptide work in this
  repo unless a live project explicitly documents a justified deviation
- deviations should be written in the project root `README.md` and the active
  phase doc

## What This Cookbook Assumes

You already know:

- basic Python and shell
- basic Git
- what a FASTA or amino-acid sequence looks like
- what `ipTM` and `pLDDT` roughly mean

It does **not** assume you already know how to structure an MLX prediction
project or how to decide when one-sample OF3 output is informative enough.

## What This Cookbook Gives You

1. A repeatable Apple-Silicon project layout
2. A phase system for peptide-target structural prediction
3. Rules for preview mode versus upgraded validation
4. Batch and manifest discipline for long runs
5. The downstream PeptideModel ingest contract
6. Failure patterns seen in real OF3-MLX peptide work
7. A neutral starter template
8. A packaged operational skill

## Read In This Order

1. [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)
2. [WORKFLOW.md](docs/WORKFLOW.md)
3. [BEGINNER_NOTES.md](docs/BEGINNER_NOTES.md)
4. [AGENT_BOOTSTRAP.md](docs/AGENT_BOOTSTRAP.md)
5. [CHECKLISTS.md](docs/CHECKLISTS.md)
6. [QUERY_PROTOCOL.md](docs/QUERY_PROTOCOL.md)
7. [MANIFEST_SCHEMA.md](docs/MANIFEST_SCHEMA.md)
8. [PLATFORM_CONTRACT.md](docs/PLATFORM_CONTRACT.md)
9. [METRICS_DICTIONARY.md](docs/METRICS_DICTIONARY.md)
10. [COMPUTE_STRATEGY.md](docs/COMPUTE_STRATEGY.md)
11. [FAILURE_ATLAS.md](docs/FAILURE_ATLAS.md)
12. [PROVENANCE_PROTOCOL.md](docs/PROVENANCE_PROTOCOL.md)
13. [PAUSE_RESUME_PROTOCOL.md](docs/PAUSE_RESUME_PROTOCOL.md)
14. [CLAIMS_LADDER.md](docs/CLAIMS_LADDER.md)
15. [myostatin-gdf8-preview](myostatin-gdf8-preview)
16. [starter-template](starter-template)
17. [skill-pack](skill-pack)

## Core Idea

A platform MLX peptide project should be run like a controlled prediction
program, not like a pile of ad hoc JSON files.

The pattern is:

1. Freeze target identity and sequence sources.
2. Verify the environment and weights once.
3. Build a small reference panel with positives and negatives.
4. Run preview predictions cheaply.
5. Escalate only the useful cases to multi-sample or orthogonal validation.
6. Preserve both wins and failures with manifests and state files.

If you skip step 3, later candidate rankings are usually fiction.

## Minimal Tool Stack

At minimum:

- Apple Silicon Mac with adequate unified memory
- Python environment for `openfold-3-mlx`
- local model weights
- one documented runner YAML
- one append-only results path

Useful but optional:

- a backend API for card ingestion or result write-back
- a second structure lane for cross-checking
- descriptor or chemistry post-filters
- a coordination channel for long-running batches
- a separate Codex agent for research support outside the main MLX batch lane

## Recommended Codex Research Support

For the intermediate MLX cookbook, we strongly recommend having a Codex agent
available as a separate researcher or literature-support lane.

Important:

- this is not an in-notebook integration
- this is not “Codex inside Google Colab”
- the Codex agent should run beside your main MLX workflow, not inside the notebook itself

Use that agent for:

- target and accession normalization before freezing inputs
- UniProt, RCSB, and AlphaFold structure/background lookup
- ligand and assay precedent checks before spending upgraded validation compute
- PubMed and PMC literature follow-up
- broad target-background questions before expanding preview or upgrade batches

The adopted Codex `life-science-research` subset for this role is:

- `research-router-skill`
- `alphafold-skill`
- `rcsb-pdb-skill`
- `uniprot-skill`
- `bindingdb-skill`
- `chembl-skill`
- `ncbi-entrez-skill`
- `ncbi-pmc-skill`

Reference: `github.com/openai/openai/tree/master/plugins/life-science-research` — review if you need the skill patterns.

This is useful in the MLX workflow because the research agent can work in parallel
with the main prediction executor while preserving preview-vs-upgrade discipline.

## Non-Negotiable Working Principles

- one project, one folder
- one target sequence source per live campaign
- one manifest format per run family
- one canonical state path per project, preferably `pipeline/manifests/state.json`
- one explicit meaning for `preview` and `upgrade`
- do not rank by `ipTM` alone until references and negatives have been checked
- long runs need `state.json` or equivalent resume bookkeeping

## Scope Boundary

This cookbook is about:

- setting up OF3-MLX peptide projects
- structuring query JSONs and batches
- handling preview versus upgraded compute
- logging manifests and failures honestly
- mapping successful runs into the PeptideModel platform contract

It is not about:

- medicinal chemistry optimization
- wet-lab assay design
- training the model from scratch
- one operator's private runtime state

## Worked Example

The cookbook includes one standalone MLX teaching example:

- [myostatin-gdf8-preview](myostatin-gdf8-preview)

It demonstrates the Myostatin/GDF-8 preview lane on Apple Silicon using
MLX-style query JSON, preview-vs-upgrade gates, MLX memory limits, and the final
`upload_ready/` packaging boundary. It is intentionally separate from the
Linux/GPU target-decoy example so Mac users have a complete local entrypoint.

## Public Starter Template

The cookbook includes a neutral platform-oriented starter template:

- [starter-template](starter-template)

Use that when you want a PeptideModel-oriented OF3-MLX project scaffold rather
than a copy of one live workspace.

## Distributable Skill

The cookbook also includes a packaged copy of the operational skill:

- [skill-pack/peptide-mlx-research-ops](skill-pack/peptide-mlx-research-ops)

Use that when you want to hand the method to another Codex-style environment
without giving it the whole repo.
