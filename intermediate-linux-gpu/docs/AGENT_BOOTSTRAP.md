# Agent Bootstrap

The public starter template is not a runnable package by itself.

That is intentional.

It provides:

- project structure
- phase logic
- documentation expectations

It does **not** provide:

- the final cheap-lane implementation
- the final strong-lane implementation
- a universal scoring script

Those must be chosen and generated for the specific project.

## Authority Rules

Default authority for project decisions:

- phase gate and next-step decision: latest active phase doc in `docs/`
- frozen target or reference specification: `config/`
- command contract, state location, and downstream mode: `pipeline/README.md`

If `pipeline/README.md` and the active phase doc disagree on runnable command
details, `pipeline/README.md` is authoritative for the command contract.

The active phase doc should reference that command contract and record any
phase-specific caveats or temporary restrictions.

If they drift, stop and reconcile before running a new batch.

## What The Agent Must Do

When helping a beginner, the agent should:

1. recommend one cheap lane
2. recommend one stronger validation lane
3. explain why they fit the target and hardware
4. generate the starter scripts or notebook stubs
5. define the machine-readable outputs

## What The Agent Must Not Do

Do not leave the beginner with:

- “implement the pipeline”
- “choose your own scoring function”
- “figure out a cheap lane”

Those are exactly the parts the agent should help construct.

## Example User Requests

- “Help me choose a cheap local lane for this project.”
- “Help me write the first screening script for the reference panel.”
- “Help me set up the stronger validation lane.”
- “Help me define the results TSV / JSON structure.”

## Minimal Beginner Flow

1. fill the target and reference files
2. ask the agent to generate the cheap lane
3. run the reference panel
4. ask the agent to generate the stronger validation lane
5. continue phase-by-phase
