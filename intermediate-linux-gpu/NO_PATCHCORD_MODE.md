# No-Patchcord Mode

Patchcord is helpful. It is not required.
It is one optional coordination layer, not the scientific method.

You can run the same methodology solo if you replace agent lanes with explicit sequential passes.

## Core Principle

Without Patchcord, you lose parallelism. You do **not** lose the scientific method.

The replacement is:

- do the same work
- in stricter sequence
- with clearer written checkpoints

## Solo Lane Mapping

Without Patchcord, one operator does all four roles in sequence:

1. executor
2. reviewer
3. literature verifier
4. orthogonal skeptic

The critical thing is to switch roles deliberately, not blur them together.

## Solo Working Sequence

For each phase:

1. Run the phase.
2. Write the machine-readable output.
3. Write the markdown report.
4. Stop.
5. Re-read the report in the reviewer role and answer:
   - did the gate pass?
   - what does this lane actually claim?
   - what does it fail to claim?
6. Only then continue.

This pause is the substitute for another agent challenging you.

## Replace Each Missing Lane Explicitly

### Missing Scientific-Review Lane

This means the missing scientific-review role, not a missing Patchcord-specific
agent name.

Compensate by forcing a written gate section in every phase report:

- `Goal`
- `Gate`
- `Pass/Fail`
- `Interpretation`
- `Next step`

### Missing Literature Lane

Compensate by adding a provenance check before using any named benchmark:

- source file or paper
- exact sequence
- real chemistry vs proxy
- structure mapping if relevant

### Missing Orthogonal Model Lane

Compensate by adding at least one orthogonal check:

- different metric
- different target-decoy view
- descriptor cross-check
- alternative structure method if available

If no orthogonal check exists, lower the strength of your claim.

## Minimal Solo Rules

1. Never advance phases from memory alone.
2. Never trust a named benchmark without provenance notes.
3. Never use a lane as a ranking engine unless it beat its negatives.
4. Never skip the written interpretation step.
5. Never let “I’m the only one here” become an excuse for loose claims.
