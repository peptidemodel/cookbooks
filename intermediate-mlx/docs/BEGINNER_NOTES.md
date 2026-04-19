# Beginner Notes

## What This Cookbook Is Teaching

This cookbook is not teaching you how to reimplement OpenFold.
It is teaching you how to run peptide-target structural prediction work without
lying to yourself about what the outputs mean.

## The Three Most Important Ideas

### 1. One good JSON is better than ten mystery runs

Keep query inputs explicit and versioned.
If you cannot reconstruct the chain order and sequence source, the run is not
scientifically useful.

### 2. One-sample preview output is not a final answer

Preview mode is mainly for:

- environment proof
- coarse screening
- broad backfill
- deciding what deserves more compute

It is not automatically a trustworthy ranking lane.

### 3. Save manifests, not just structures

A lone CIF file is not enough.
You need:

- model version
- weights hash
- hardware note
- seed
- sample count
- runner config

Without that, later reproduction becomes guesswork.

## If You Do Not Yet Have Pipeline Scripts

That is normal.

Start by creating:

1. a target spec JSON
2. a reference panel JSON
3. a pipeline README with exact commands
4. a tiny smoke-test query

Then let the agent help generate the runner scripts.

## What To Ask the Agent For

Good requests:

- “build a query JSON from this target and peptide panel”
- “write a manifest schema for these runs”
- “create a batch runner that preserves state and resumes safely”
- “summarize which cards should be upgraded from preview mode”

Bad requests:

- “pick the best peptide” when no controls exist
- “rank these by ipTM” when preview mode never separated negatives

## First Safe Milestone

Before any large batch, you should have:

- one successful smoke-test run
- one documented reference panel
- one negative control
- one explicit statement of what preview mode is allowed to claim
