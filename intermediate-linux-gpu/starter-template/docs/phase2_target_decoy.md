# Phase 2 — Target-Decoy

## Goal

Stress the lane against adversarial false positives.

## Minimum Decoys

- hotspot-killed target
- rotated-surface decoy
- wrong-face decoy

## Pass Condition

- real positives prefer the real target
- negatives do not survive broadly

## If Scrambled Beats Real

The lane is not sequence-specific enough for ranking.

Possible actions:

- reframe it as geometry-only
- replace it with a stronger lane
- diagnose the target spec before running more candidates
