# Phase 4 — Filtering

## Goal

Filter candidates through the lane(s) that survived earlier validation.

## Decide Before Running

- what is the geometry gate?
- what is the specificity gate?
- what is the chemistry / permeability / developability axis?
- which metric is only diagnostic and which is ranking-capable?

## Pass Condition

Candidates survive the defined filters without obvious control failures.

## Fail Condition

- positives miss the gate
- negatives survive
- the lane behaves inconsistently with earlier validation

If that happens, stop and write a negative-result report.
