# Phase Gates

## Phase 0 — Target Freeze

Required:
- target PDB chosen
- chain IDs frozen
- hotspot numbering documented
- reference peptide(s) defined

Stop if:
- source numbering vs predicted numbering is unclear

## Phase 1 — Reference Calibration

Required:
- positive control
- weaker/proxy positive
- scrambled or poly-Ala negative

Pass if:
- obvious negatives do not behave like real positives

## Phase 2 — Target-Decoy

Required:
- real target
- hotspot-killed decoy
- rotated / wrong-face decoy if possible

Pass if:
- real positives prefer real target
- negatives do not survive broadly

If scrambled beats real:
- lane is not sequence-specific

## Phase 3 — Candidate Panel

Required:
- labeled panel
- explicit SAR series
- references and negatives in the same panel

Pass condition:
- panel is interpretable, not just large

## Phase 4 — Filtering

Define explicitly which of these are gates:
- geometry
- specificity
- permeability / chemistry
- synthetic simplicity

If one lane fails but still shows pocket occupancy:
- reframe it to geometry-only

## Phase 5 — Closeout

Each finalist must state:
- why it survived
- what lane supports it
- what caveat remains

Do not produce a synthesis shortlist from a red-gated lane.
