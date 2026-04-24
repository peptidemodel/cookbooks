# Failure Atlas

This is the part people usually skip, and then they burn weeks.

Most peptide research projects do not fail because the model is bad in an abstract sense. They fail because the operator misreads what kind of failure is happening.

## 1. Wrong Target Numbering

### Symptom

- hotspot occupancy is near zero for everything
- all candidates fail the gate
- visual inspection suggests the peptide is in the right pocket, but the scorer says no

### What It Usually Means

- source PDB numbering and predicted-complex numbering are different
- the hotspot list is biologically right but numerically wrong

### What We Saw

- MC1R had this exact failure mode
- the saved predicted complexes renumbered the receptor chain
- after remapping the hotspot residues, the `0 PASS` situation disappeared

### What To Do

1. inspect a saved predicted complex PDB
2. compare source chain numbering to predicted chain numbering
3. derive the explicit mapping
4. rerun scoring or rescore saved outputs before launching more compute

### What Not To Do

- do not run another big candidate sweep first
- do not treat near-zero hotspot scores as proof the biology is wrong

## 2. Sequence-Insensitive Lane

### Symptom

- scrambled control beats or matches the real binder
- poly-Ala survives
- decoys are too close to the real target

### What It Usually Means

- the lane is not sequence-specific enough for ranking
- it may still be useful for geometry, but not for affinity claims

### What We Saw

- original GHSR Cycle 3 Rosetta lane failed this way
- `scrambled_ghrp6` scored too well on the real receptor
- `ipamorelin` preferred a decoy in one gate

### What To Do

1. freeze the negative result
2. write it down explicitly
3. reframe the lane as geometry-only if that is still defensible
4. stop using it as the main ranking function

### What Not To Do

- do not tighten thresholds and pretend the lane is fixed
- do not keep ranking candidate lists by the same broken score

## 3. Provenance Error

### Symptom

- a literature peptide is widely referenced in the repo
- but no one can point to the exact paper-backed sequence
- names, labels, and actual sequence origins drift apart

### What It Usually Means

- the sequence entered the project through internal lore, a copied structure fragment, or a secondary source

### What We Saw

- old repo “DF-3” in myostatin was not the real Takayama DF-3
- the fake sequence matched the wrong chain fragment from `3HH2`
- the real DF-3 only became clear after checking the actual BMCL papers

### What To Do

1. stop treating the name as verified
2. pull the primary paper if the benchmark matters
3. map the peptide back to the structure explicitly
4. relabel the old internal sequence honestly if needed

### What Not To Do

- do not keep using a literature label because it is convenient

## 4. Cheap Local Surface That Looks Alive But Tells You Nothing

### Symptom

- the local heuristic lane runs
- structures appear
- but real motif, scrambled control, and damaged mutant all score similarly

### What It Usually Means

- the surface may be real
- but the cheap lane is blind there

### What We Saw

- FTL1 `8QU9` cleft under local Boltz behaved like this
- the native motif and controls did not separate meaningfully

### What To Do

1. do not conclude the biology is dead
2. conclude the cheap lane is not informative enough there
3. pivot to a stronger lane or a different surface

## 5. Proxy Overreach

### Symptom

- a hand-built chemistry or permeability proxy starts driving all major decisions
- the proxy fits a tiny calibration set perfectly

### What It Usually Means

- the proxy may be useful for ranking
- but it is still fragile as a truth model

### What We Saw

- GHSR permeability proxy was useful
- but it was explicitly only a ranking aid
- orthogonal descriptor checks were still needed

### What To Do

1. keep the proxy as one axis
2. add orthogonal descriptor or literature checks
3. document where the proxy is trustworthy and where it is not

## 6. Positive Control Fails While Candidates “Pass”

### Symptom

- candidate set looks surprisingly good
- but the canonical positive reference fails or looks mediocre

### What It Usually Means

- gate is mis-specified
- lane is overfitting a bad artifact
- reference assumptions are wrong

### What To Do

Treat this as a red flag first, not as evidence that your new candidates are miraculous.

## 7. General Rule

If a failure changes the interpretation of the whole lane, stop and classify the failure before generating more sequences.

The right question is not:

> “How do I make the score look better?”

It is:

> “What kind of failure is this?”
