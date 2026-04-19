# Compute Strategy

The goal is not to use the most compute.
The goal is to use the cheapest Apple-Silicon compute that is still honest for
the claim you want to make.

## General Rule

Use:

- smoke tests for environment proof
- preview mode for broad triage
- upgrade mode for real decisions

Do not invert that order.

## Lane Types

### Smoke-Test Lane

Use for:

- first environment proof
- verifying weights and runner configuration
- checking basic output structure

Typical pattern:

- one tiny query
- one seed
- one sample

### Preview Lane

Use for:

- reference sanity
- broad platform backfill
- cheap existence proof
- deciding what deserves more compute

Typical pattern:

- one sample per query
- grouped batches by target
- strict manifest logging

### Upgrade Lane

Use for:

- shortlisted candidates
- discrimination questions
- target-decoy checks
- pose stability questions

Typical pattern:

- more diffusion samples
- smaller, more curated panels
- manual inspection plus metrics

Preferred order under constrained compute:

1. add more diffusion samples for the smallest decision-critical panel
2. run target-decoy or damaged-control checks on shortlisted cases
3. use an orthogonal model lane only after the first two are informative or
   blocked

Reason:

- sample-depth often answers stability questions most directly
- decoy checks usually test discrimination more cheaply than a whole new lane
- orthogonal lanes are valuable, but they cost more setup and interpretation

## Practical Budgeting

Before a big run, ask:

1. what decision will this run change?
2. has the cheaper prerequisite lane already passed?
3. if the run fails, will I know why?

If the answer to 3 is no, tighten the phase before burning compute.

## Common Waste Patterns

### Waste Pattern 1

Running a giant backfill before the environment is proven on a small query.

### Waste Pattern 2

Treating one-sample preview output as if it were final validation.

### Waste Pattern 3

Repeating a sequence-insensitive lane on more peptides instead of diagnosing the
failure class.

### Waste Pattern 4

Ignoring token or memory limits until a long batch crashes halfway through.

## Hardware Reality

Consumer hardware is a feature, not an excuse.

Real discipline on Apple Silicon means:

- respecting unified memory limits
- grouping work to avoid repeated setup costs
- saving resumable state
- promoting only the cases worth more runtime

## Final Rule

Spend more compute only after you know what counts as success or failure.
