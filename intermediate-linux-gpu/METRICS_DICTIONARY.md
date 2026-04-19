# Metrics Dictionary

This file is intentionally blunt.

Each metric gets three answers:

1. what it measures
2. what it is good for
3. what it is bad for

## `iPTM`

What it measures:
- interface confidence from AlphaFold-style multimer prediction

Good for:
- rough interaction confidence
- larger complexes
- early triage

Bad for:
- short peptides
- fine ranking among very small binders

Important:
- short-peptide projects can look artificially weak under raw `iPTM`

## `ipSAE`

What it measures:
- interface score that tries to correct some raw `iPTM` problems using PAE-aware filtering

Good for:
- short-peptide interface assessment
- improved ranking relative to raw `iPTM`

Bad for:
- blind use without checking which `ipSAE` variant is actually stable

Important:
- do not assume every `ipSAE` variant behaves equally well

## `ipsae_d0chn`

What it measures:
- chain-normalized `ipSAE` variant used in this repo as the more stable short-peptide interface metric

Good for:
- final corrected ranking in short-peptide AF2 lanes
- gating and composites when raw `ipsae` is pathological

Bad for:
- claims of experimental affinity

Important:
- in this repo, this became the corrected interface metric in multiple projects

## Hotspot Occupancy

What it measures:
- fraction of predefined target hotspot residues touched by the peptide

Good for:
- checking whether a candidate reaches the intended pocket
- catching wrong-pocket poses

Bad for:
- anything if the residue numbering is wrong

Important:
- if the mapping is wrong, hotspot occupancy becomes nonsense

## Cavity Fraction / Pocket Fraction

What it measures:
- fraction of residues contacted in a named pocket region

Good for:
- geometry gates
- deciding whether a candidate reaches cavity I / cavity II / activation cluster

Bad for:
- sequence-specific ranking by itself

## `binding_like`

What it measures:
- a simplified energy-like score from current pose versus separated chains in the Rosetta lane used here

Good for:
- local comparisons inside one controlled lane
- geometry-adjacent triage

Bad for:
- global truth
- claims of affinity
- ranking if negatives are not defeated

Important:
- if scrambled survives, `binding_like` is not a valid ranking engine for that project

## Target-Decoy Margin

What it measures:
- difference between the real target score and the best decoy score

Good for:
- specificity-aware gating
- deciding whether a lane distinguishes on-target from off-target geometry

Bad for:
- replacing all other evidence

Important:
- a good-looking real target score without decoy separation is weak evidence

## RMSD vs Reference Pose

What it measures:
- structural distance from a known or deposited reference pose

Good for:
- pose recovery checks
- validating whether local docking can stay near a known anchor

Bad for:
- novel binding-mode ranking when no ground truth exists

## Atom Contacts / Interface Residue Count

What it measures:
- raw size or density of the interface contact set

Good for:
- sanity checks
- filtering obviously tiny / non-contacting poses

Bad for:
- ranking good candidates against each other

## cLogP

What it measures:
- estimated hydrophobicity / lipophilicity

Good for:
- rough permeability/developability reasoning
- orthogonal descriptor checks

Bad for:
- direct PK truth
- replacing a full absorption model

## Permeability Proxy

What it measures:
- a hand-built heuristic score intended to rank nasal or other delivery-relevant behavior

Good for:
- relative ranking
- disagreement detection
- triage

Bad for:
- being treated as ground-truth PK

Important:
- proxies help rank
- they do not become biology just because they correlate on a tiny set

## Composite Score

What it measures:
- weighted mixture of multiple metrics

Good for:
- late-stage ranking once each component is individually justified

Bad for:
- hiding a broken lane behind a single number

Important:
- never trust a composite more than the weakest metric inside it
