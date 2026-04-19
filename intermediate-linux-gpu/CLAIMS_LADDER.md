# Claims Ladder

This ladder defines what you are allowed to claim at each stage.

If you claim more than the lane supports, you are writing fiction.

## Level 0: Target Setup Only

Evidence:

- target structure chosen
- hotspot residues defined
- references listed

Allowed claim:

- “We have a prepared target and a defined design hypothesis.”

Not allowed:

- any statement about candidate quality
- any statement about binding

## Level 1: Cheap Local Heuristic

Evidence:

- local screen runs
- some candidates produce plausible complexes

Allowed claim:

- “This surface / sequence class is worth escalating.”

Not allowed:

- final ranking
- potency claims
- synthesis shortlist

Examples:

- local Boltz on M40

## Level 2: Geometry Gate

Evidence:

- the lane can place peptides into the intended pocket
- pocket occupancy or cavity contact is meaningful
- but sequence specificity may still be weak

Allowed claim:

- “These candidates geometrically fit the intended pocket better than others.”

Not allowed:

- “This is the strongest binder”
- fine SAR based on energy-like ordering

Examples:

- re-scoped GHSR geometric filter

## Level 3: Reference Calibration Pass

Evidence:

- real positive control behaves better than obvious negatives
- proxy / weaker controls behave plausibly

Allowed claim:

- “The lane is at least directionally sane.”

Not allowed:

- final synthesis ranking unless specificity is also proven

## Level 4: Target-Decoy Specificity Pass

Evidence:

- real target beats decoys for real positives
- negatives do not survive broadly

Allowed claim:

- “This lane can support specificity-aware promotion or rejection.”

Still not automatically allowed:

- fine-grained potency ranking if the metric is noisy

## Level 5: Corrected High-Fidelity Interface Ranking

Evidence:

- high-fidelity structure lane
- corrected interface metric
- validated controls
- clean interpretation of numbering and chains

Allowed claim:

- “This is our current computational shortlist under the corrected lane.”

Examples:

- corrected myostatin AF2 / target-decoy lane
- corrected MC1R `ipSAE_d0chn` + hotspot lane

Still not equivalent to:

- experimental affinity
- selectivity in cells

## Level 6: Synthesis-Ready Recommendation

Evidence:

- candidate survives the best available computational lane
- references and negatives behave sensibly
- chemistry / developability caveats are explicit
- benchmark provenance is verified

Allowed claim:

- “This is a rational synthesis candidate.”

Not allowed:

- “This peptide is experimentally superior” unless you have data

## Special Rule For Proxies

Proxy metrics can support:

- ranking
- triage
- disagreement flags

Proxy metrics do **not** automatically support:

- PK truth
- biological equivalence
- medicinal-chemistry equivalence

## Special Rule For Negative Results

If a lane fails:

- you may still claim what it is useful for
- you may not claim what it failed to support

Example:

- if scrambled survives, you may still use the lane as a geometry screen
- you may not use it as a sequence-specific ranking engine

## Safe Wording

Good:

- “top candidate under the corrected computational lane”
- “geometrically consistent with the target pocket”
- “passes target-decoy on our current fixed-backbone Rosetta setup”

Bad:

- “best binder”
- “selective”
- “same or better than literature peptide”

unless you actually have the stronger evidence
