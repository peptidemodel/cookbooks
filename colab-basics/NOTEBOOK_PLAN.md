# Notebook Plan

This file records the rationale behind the five notebooks in this cookbook: why they
exist, why they are ordered this way, and where the scientific claims are intentionally
conservative.

---

## Why Five Notebooks, Not One

A single monolithic notebook encourages skipping gates. When everything is in one file,
it is easy to run a candidate sweep before confirming the lane is sane. The five-notebook
split makes each gate explicit and its output a concrete artifact.

---

## Notebook 1 — Target Surface Sanity

**Why this exists:**

Downstream results are meaningless if the target structure is loaded with the wrong chain,
wrong residue numbering, or an undefined pocket. This failure mode is extremely common.
Notebook 01 exists solely to freeze these assumptions before any scoring runs.

**What it produces:**

A machine-readable `target_spec.json` and a plain-text summary of chain/pocket assumptions.
Every other notebook loads this file and trusts it.

**Conservative decisions:**

- Does not attempt to predict the pocket automatically. The user must specify residues or
  accept a simple distance-based approximation. This is intentional: automated pocket
  finders often choose the wrong site.
- Outputs a frozen spec; does not run any scoring. This is the correct split.

---

## Notebook 2 — Reference Panel Check

**Why this exists:**

Before scoring a novel candidate, you must know whether your scoring lane can tell anything
apart at all. A lane that scores scrambled-sequence and poly-Ala peptides similarly to a
known reference is broken for ranking purposes, regardless of how much compute it uses.

This notebook is about **calibration**, not discovery.

**What it produces:**

A scored panel CSV, a bar chart, and an interpretation summary. The interpretation
explicitly labels the result as pass, degraded, or fail.

**Conservative decisions:**

- The heuristic scoring lane used here is a property-matching proxy, not docking or
  structure prediction. It can demonstrate gross separation if controls are well-chosen,
  but it will not reliably rank fine-grained sequence variants.
- If the panel fails (scrambled or poly-Ala scores similarly to the reference), the
  notebook stops and tells you not to proceed. This is the correct behavior.
- Notebooks 03 and 04 produce less trustworthy results if this notebook has not passed.
  They say so explicitly at their tops.

---

## Notebook 3 — Single Peptide Evaluation

**Why this exists:**

The simplest real question: "I have a peptide idea. Can I test it?" This notebook answers
that question cleanly without requiring the user to set up a full scan. It also serves as
the template for understanding what a single evaluation result bundle looks like before
attempting bulk scans.

**What it produces:**

A JSON result bundle with sub-scores, a plain-language interpretation, and a suggested
action (proceed / needs calibration / likely weak).

**Conservative decisions:**

- Includes a prominent reminder that a passing score here does not mean the peptide binds.
- References the panel result from notebook 02 and warns if that panel was never passed.

---

## Notebook 4 — Small SAR Scan

**Why this exists:**

After evaluating a seed peptide, the natural next step is to explore local variants.
SAR (Structure-Activity Relationship) scanning means systematically changing individual
positions to see which substitutions improve or degrade the score.

This notebook keeps the scan **small by design**:
- Free Colab tier: ≤ 40 variants by default
- Paid tier: ≤ 200 variants

**What it produces:**

A ranked CSV of all variants, a heatmap showing per-position, per-substitution score
changes, and a list of top candidates for promotion.

**Conservative decisions:**

- The heuristic lane used here has limited ability to rank fine-grained substitutions
  reliably. The heatmap shows *relative ordering within this lane*, not affinity predictions.
- The notebook explicitly tells the user that a high-ranking variant from this scan is
  not yet a synthesis candidate; it is a candidate for notebook 05 (strong validation
  handoff).
- Panel size limits are enforced through the config block, not by trust that the user
  will be conservative.

---

## Notebook 5 — Promote to Strong Validation

**Why this exists:**

The cheap heuristic lane is for triage. Before spending real compute on strong validation
(AlphaFold2, Boltz-1, PyRosetta, or any heavier pipeline), you should have a short,
documented rationale for each candidate you are promoting.

This notebook collects shortlisted candidates from notebooks 03 and 04, applies minimum
score thresholds, and writes a clean promotion bundle.

**What it produces:**

- `shortlist.json`: machine-readable candidate list with provenance
- `promotion_summary.md`: human-readable rationale document
- A plain-text next-step protocol for the chosen strong-validation lane

If running strong validation inside Colab is practical (e.g., free AF2 Colab via the
standard community notebook), the notebook includes a section explaining how to prepare
inputs for that flow. It does not attempt to run strong validation itself, because:

- this cookbook is about the workflow gates, not a specific model runner
- strong-validation setup varies too much by lane (AF2 Colab, Boltz-1, PyRosetta local)
- faking a full lane inside a beginner cookbook would be misleading

**Conservative decisions:**

- Score thresholds for promotion are configurable but have conservative defaults.
- The notebook explicitly lists candidates that did not make the shortlist and why.
- The promotion bundle is designed to be handed to a different environment (local GPU,
  hosted GPU, another Colab notebook) rather than consumed here.

---

## Phase Alignment

These notebooks map to the phase system in `intermediate-linux-gpu/COMPUTE_STRATEGY.md`:

| Phase | Cookbook equivalent |
|-------|-------------------|
| Spec freeze | Notebook 01 |
| Cheap local sanity / reference calibration | Notebooks 02–03 |
| Candidate generation / cheap sweep | Notebook 04 |
| Strong validation | Notebook 05 (handoff only) |

The full intermediate cookbook continues from where notebook 05 leaves off, using
higher-fidelity lanes and target-decoy validation.

---

## Open Issues and Limitations

1. **Scoring lane is a heuristic, not docking.** The lane in notebooks 02–04 uses
   sequence composition properties and BLOSUM62 similarity to score peptides. It is
   transparent about this. If you need a real docking score on free Colab, the closest
   practical option is AutoDock Vina (CPU) or ESMFold+interface scoring. This is left
   as a future extension.

2. **Pocket definition is manual.** Notebook 01 does not auto-detect pockets. This is
   intentional (see notebook 01 rationale), but a future version could integrate
   fpocket or SiteMap-lite for guided suggestions.

3. **No target-decoy validation.** Full target-decoy validation (checking whether the
   peptide is specific to the intended target vs. scrambled decoys) is not implemented
   in this cookbook because it requires a heavier lane. This is acknowledged in notebook
   05 as a prerequisite for synthesis-level claims.

4. **ESMFold lane is optional and may fail on free Colab.** The optional stronger scoring
   path using ESM2 embeddings is included as commented code in notebooks 02–04. Memory
   requirements on free Colab are tight for anything larger than ~200 residues.
