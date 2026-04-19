# Phase 0 — Target Freeze

## Goal

Freeze the target and interpretation layer before candidate generation.

## Required Outputs

- one target structure or model
- one explicit target chain
- numbering policy
- reference table
- declared next gate
- downstream mode
- canonical structure format
- canonical state file path

## Questions To Answer

1. What exact structure is the target spec built on?
2. Which chain is the target?
3. Are hotspot residues known?
4. If predicted complexes renumber residues, how will that mapping be handled?
5. What positive reference will anchor Phase 1?

## Pass Condition

Everything above is written down in `config/` and this doc.

## Definition of Done

- target numbering, downstream mode, structure format, and state path are all explicit

## Fail Condition

If any of the five questions is unanswered, the project is not ready for Phase 1.
