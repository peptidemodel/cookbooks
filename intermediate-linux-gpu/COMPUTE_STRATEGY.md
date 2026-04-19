# Compute Strategy

The goal is not to use the fanciest compute. The goal is to use the cheapest compute that is still honest for the claim you want to make.

## General Rule

Use:

- cheap compute for broad exploration
- expensive compute for decisive validation

Do not invert that order.

## Lane Types

### Cheap Local Heuristic Lane

Examples:

- local `Boltz-1`
- simple local docking or fixed-pose checks

Use for:

- hypothesis grinding
- surface comparison
- quick SAR scans
- deciding whether a target surface is even worth escalating

Do not use for:

- final shortlist claims
- very fine short-peptide ranking

## CPU Physics Lane

Examples:

- PyRosetta target-decoy
- fixed-backbone scans
- local refine / perturb lanes

Use for:

- hotspot identification
- pose recovery
- adversarial decoy checks
- orthogonal validation

Do not use for:

- pretending a single energy-like number equals affinity

## High-Fidelity Structure Lane

Examples:

- AF2 / Colab
- corrected `ipSAE_d0chn`
- stronger structure predictors

Use for:

- final corrected ranking
- better short-peptide interface assessment
- stronger promotion/rejection decisions

## Alternative Model Lane

Examples:

- OF3-MLX
- alternative structure stack on different hardware
- descriptor-only validation lane

Use for:

- orthogonal confirmation
- reproducibility checks
- alternative geometry or chemistry views

## Practical Budgeting

Before launching a big run, ask:

1. what decision will this run change?
2. has the cheaper prerequisite lane already passed?
3. if this run fails, will I know why?

If the answer to 3 is no, tighten the phase before burning compute.

## Common Waste Patterns

### Waste Pattern 1

Running a big candidate sweep before fixing a numbering bug.

### Waste Pattern 2

Using a high-fidelity lane to rank candidates when references and negatives were never calibrated.

### Waste Pattern 3

Repeating the same broken lane on more sequences instead of diagnosing the failure class.

## Suggested Default Order

1. spec freeze
2. cheap local sanity
3. reference calibration
4. target-decoy
5. candidate generation
6. strong validation
7. closeout

## Hardware Reality

Strong machine does not guarantee good lane behavior.

If a job uses one core badly, fix the orchestration.
If a lane is scientifically broken, more hardware will not save it.

## Final Rule

Spend compute only after you know what would count as success or failure.
