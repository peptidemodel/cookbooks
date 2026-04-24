# PeptideModel.com Platform Linux/GPU Cookbook

This folder is a compact handover for someone who wants to run research in the style used in this repo:

- Linux-first
- Linux GPU friendly
- local heuristic generation on modest hardware
- stronger validation on a higher-fidelity lane
- clean per-project folders
- phase-gated progress
- explicit negative results
- downstream write-back discipline for the PeptideModel platform

This is not a literature review and not a theoretical textbook. It is a practical operating manual.

Important:

- this cookbook is platform-oriented, not machine-status-oriented
- it is not the status page for this repo
- it does not define the currently active supervisor, campaign, or machine state
- those are runtime questions and must be answered by project-local or environment-local docs

Repo role:

- treat this cookbook as the normative default for new Linux/GPU peptide work in
  this repo unless a live project explicitly documents a justified deviation
- deviations should be written in the project root `README.md` and the active
  phase doc

## What This Cookbook Assumes

You already know:

- basic Python and shell
- basic Git
- what a PDB is
- what peptide sequences look like
- what docking / structure prediction is at a high level

It does **not** assume you are a structural biologist.

It also does not assume you already know how to implement the actual pipeline scripts. The agent is expected to help build those.

## What This Cookbook Gives You

1. A repeatable project layout
2. A concrete research loop
3. A phase system that prevents you from optimizing noise
4. Rules for when to trust a result and when to stop
5. Handoff templates for team or agent-based collaboration
6. A method that still works in solo mode without any messaging product
7. The downstream PeptideModel ingest contract
8. A beginner-safe workflow where the agent is expected to generate missing pipeline pieces

## Read In This Order

1. [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)
2. [WORKFLOW.md](docs/WORKFLOW.md)
3. [BEGINNER_NOTES.md](docs/BEGINNER_NOTES.md)
4. [AGENT_BOOTSTRAP.md](docs/AGENT_BOOTSTRAP.md)
5. [CHECKLISTS.md](docs/CHECKLISTS.md)
6. [PLATFORM_CONTRACT.md](docs/PLATFORM_CONTRACT.md)
7. [TEMPLATES.md](docs/TEMPLATES.md)
8. [COORDINATION.md](docs/COORDINATION.md)
9. [NO_PATCHCORD_MODE.md](docs/NO_PATCHCORD_MODE.md)
10. [METRICS_DICTIONARY.md](docs/METRICS_DICTIONARY.md)
11. [PAUSE_RESUME_PROTOCOL.md](docs/PAUSE_RESUME_PROTOCOL.md)
12. [COMPUTE_STRATEGY.md](docs/COMPUTE_STRATEGY.md)
13. [FAILURE_ATLAS.md](docs/FAILURE_ATLAS.md)
14. [CLAIMS_LADDER.md](docs/CLAIMS_LADDER.md)
15. [PROVENANCE_PROTOCOL.md](docs/PROVENANCE_PROTOCOL.md)
16. [worked-example-myostatin-gdf8](worked-example-myostatin-gdf8)
17. [starter-template](starter-template)
18. [skill-pack](skill-pack)

## Core Idea

A platform peptide project should be run like a controlled engineering program, not like a pile of ad hoc scripts.

The pattern is:

1. Freeze the target and numbering.
2. Build the reference lane.
3. Prove the scoring lane is not obviously broken.
4. Generate candidates.
5. Kill weak claims early with negative controls and target-decoys.
6. Preserve both wins and failures in versioned artifacts.

If you skip step 2 or 3, later rankings are usually fiction.

## Minimal Tool Stack

At minimum:

- Linux machine
- Python environment
- Git
- one local structure-prediction lane
  - in this repo that was often `Boltz-1` for cheap local screening
- one stronger validation lane
  - in this repo that was often AF2 / Colab / `ipSAE` or PyRosetta target-decoy work

Optional but useful:

- PyRosetta
- RDKit
- PyMOL
- a coordination layer such as Patchcord, or any equivalent messaging setup
- a separate Codex agent for research support outside the main compute or notebook lane

## Recommended Codex Research Support

For the intermediate Linux/GPU cookbook, we strongly recommend having a Codex agent
available as a separate researcher or literature-support lane.

Important:

- this is not an in-notebook integration
- this is not “Codex inside Google Colab”
- the Codex agent should run beside your main workflow, not inside the notebook itself

Use that agent for:

- target and accession normalization
- UniProt, RCSB, and AlphaFold structure/background lookup
- ligand and assay precedent checks
- PubMed and PMC literature follow-up
- broad target-background questions before you commit compute

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

This is especially useful in the intermediate workflow because the research agent can
work in parallel with the main executor while preserving the phase-gated method.

## Coordination Model

Patchcord is optional.
It is one possible implementation of a coordination layer, not part of the
scientific method itself.

The methodology should work in two modes:

- coordinated multi-lane mode with a messaging layer such as Patchcord
- solo sequential mode without any messaging layer

Use:

- [COORDINATION.md](docs/COORDINATION.md) for team mode
- [NO_PATCHCORD_MODE.md](docs/NO_PATCHCORD_MODE.md) for solo mode

## Non-Negotiable Working Principles

- One project, one folder
- One target definition per live campaign
- One append-only results path per experiment lane
- One canonical state path per project, preferably `pipeline/manifests/state.json`
- Commit by phase, not by random file drift
- Do not rank by a metric until you have shown it separates a real control from a bad control
- Negative results are first-class outputs

## Scope Boundary

This cookbook is about:

- setting up projects
- running structured design cycles
- handling local vs high-fidelity validation
- managing artifacts and claims
- mapping promoted runs into the PeptideModel platform contract

Repo-specific runtime context may live outside the cookbook in files like:

- [session_state_2026-04-15.md](../docs/session_state_2026-04-15.md)
- [TOOLING_STATUS.md](../docs/TOOLING_STATUS.md)
- [FRESH_AGENT_FAQ.md](../docs/FRESH_AGENT_FAQ.md)

Those are examples of runtime/state documents, not part of the generic method itself.

They are useful for questions like:

- active supervisor identity
- currently hot campaign
- current machine/tool readiness
- which skill copy is authoritative

It is not about:

- medicinal chemistry optimization at the end
- wet-lab assay design
- cloud-scale infrastructure
- one operator's private runtime state

## Distributable Skill

The cookbook also includes a distributable copy of the operational skill:

- [skill-pack/peptide-research-ops](skill-pack/peptide-research-ops)

Use that when you want to hand the workflow to another Codex-style environment without giving it the entire repo.

## Worked Example

The cookbook includes one canonical representative example:

- [worked-example-myostatin-gdf8](worked-example-myostatin-gdf8)

This is a compact public extraction of the real Myostatin/GDF-8 target-decoy
workflow. It is the example to use when you want to understand the cookbook's
phase-gated validation style.

## Public Starter Template

The cookbook also now includes a neutral public starter template:

- [starter-template](starter-template)

Use that if you want a PeptideModel-oriented Linux/GPU peptide project scaffold rather than this repo’s operational `_template`.
