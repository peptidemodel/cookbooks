# Phase 3 — Batch Plan

Goal:

- plan grouped or resumable runs before launching them

Record:

- grouping strategy
- batch size
- stop conditions
- retry rules
- state file format
- downstream mode for this batch

Gate:

- the batch plan is specific enough that another operator could resume it

Definition of done:

- grouping, retry rules, and state-file behavior are concrete enough to resume
