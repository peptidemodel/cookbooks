# Coordination

This cookbook works best with a coordination layer, but it must not depend on one to remain scientifically usable.

Important:

- the “scientist / supervisor lane” can be another agent, a human collaborator, or a deliberate self-review checkpoint
- do not hard-code Patchcord into the scientific method
- do not hard-code a specific named supervisor or campaign into the generic workflow

Patchcord is one possible implementation of the coordination layer.
It is recommended when you want cleaner context separation and parallel work,
but the methodology must still function without it.

## What Patchcord Changes

With Patchcord or an equivalent agent-messaging layer, you can split the project into parallel lanes:

- main implementation / compute lane
- scientist / supervisor lane
- literature lane
- orthogonal-model lane
- writing / proposal lane

This does **not** change the scientific method. It changes speed, parallelism, and how cleanly work is handed off.

Recommended pattern:

- keep the main compute and file-editing lane separate from the research-support lane
- let a Codex agent act as the researcher, literature retriever, and target-background copilot
- do not pretend this is an in-notebook or in-Colab integration; it is a separate lane

The adopted Codex `life-science-research` subset for that research-support lane is:

- `research-router-skill`
- `alphafold-skill`
- `rcsb-pdb-skill`
- `uniprot-skill`
- `bindingdb-skill`
- `chembl-skill`
- `ncbi-entrez-skill`
- `ncbi-pmc-skill`

Reference: `github.com/openai/openai/tree/master/plugins/life-science-research` — review if you need the skill patterns.

If you do not have Patchcord:

- use [NO_PATCHCORD_MODE.md](NO_PATCHCORD_MODE.md)
- keep the same phase gates
- replace messaging with written reports and explicit pause points

Do not stop a project just because Patchcord is unavailable.
The right fallback is stricter written checkpoints, not improvisation.

## Recommended Lane Ownership

### Main Research Executor

Owns:

- project files
- code edits
- main compute lane
- final artifact assembly

### Scientist / Supervisor

Owns:

- phase gates
- strategic reframes
- interpretation when two lanes disagree
- stop / continue decisions

This is a role, not a required product-specific agent identity.

### Literature Lane

Owns:

- primary paper retrieval
- corpus sweeps
- provenance checks
- benchmark sequence verification

### Orthogonal Model Lane

Owns:

- alternative structure methods
- descriptor cross-checks
- conformer generation
- alternative hardware validation

## Message Contract

Every serious cross-lane message should contain:

1. current phase
2. what passed or failed
3. exact file paths
4. exact question or requested action
5. if relevant, the commit SHA

## Handoff Rules

When handing work to another lane:

- send paths, not vague descriptions
- send authoritative outputs, not screenshots
- state whether the lane is:
  - ranking
  - geometry-only
  - broken

## Attachments

If attachments are supported:

- prefer real file handoff over pasted tables
- use the platform’s proper file-sharing flow
- send both:
  - attachment path
  - original repo path

## Minimum Team Rhythm

At each meaningful phase boundary, send:

- gate verdict
- current lane interpretation
- next step
