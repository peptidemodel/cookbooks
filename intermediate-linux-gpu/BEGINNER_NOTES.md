# Beginner Notes

This cookbook is usable by beginners, but only if the AI agent actively translates the method into plain language.

The main beginner failure mode is not lack of effort. It is being buried under jargon and hidden assumptions.

## Rule For The Agent

When a term is likely to confuse a beginner, explain it in plain language the first time it matters.

Translate in context.

## Examples

### “Target-decoy validation”

Plain-language version:

> We are checking whether the peptide really prefers the intended target, instead of sticking equally well to fake versions of the target.

### “Sequence-insensitive lane”

Plain-language version:

> Our current test is too weak. It thinks a scrambled or random peptide works almost as well as the designed one, so we cannot trust it to rank real candidates.

### “Geometry-only lane”

Plain-language version:

> This test can still tell us whether a peptide reaches the right pocket, but it cannot tell us which peptide is truly better.

### “Poly-Ala survives”

Plain-language version:

> A nonsense all-alanine control is passing. That means the test is too permissive or the setup is wrong.

## Beginner Safety Rule

If the project is only a scaffold, the agent must say so clearly.

It should say:

> The template is ready, but the actual cheap-lane and strong-lane scripts still need to be created. I can help generate those next.
