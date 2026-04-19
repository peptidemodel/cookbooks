# Phase 2 — Target-Decoy Plan

## Goal

Stress the lane against adversarial false positives before candidate generation expands.

## Planned Decoys

### 1. Hotspot-killed decoy

Purpose:

- test whether the peptide truly depends on the intended interface patch

### 2. Rotated surface decoy

Purpose:

- test whether the lane just likes sticking the peptide onto any exposed surface

### 3. Wrong-face decoy

Purpose:

- test whether the lane has any real spatial preference

## Desired Interpretation

We want:

- real target better than decoys for the real positive
- negatives not surviving across all targets

## What To Do If It Fails

If the real positive does not separate from decoys:

- do not move to large candidate design
- classify the failure first:
  - spec issue
  - sequence-insensitive lane
  - geometry-only lane

## Main Lesson

Target-decoy is not an optional “extra.”

It is what tells you whether your lane is actually testing on-target behavior or just generating attractive nonsense.
