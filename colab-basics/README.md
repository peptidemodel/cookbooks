# Peptide Research: Colab Basics Cookbook

A Colab-first, beginner-readable cookbook for structured peptide research workflows.
Five small notebooks that take you from a raw PDB structure to a defensible promotion
decision, without requiring a local Linux machine or expensive cloud compute.

---

## Quick Start in Colab

1. Click the **notebook 01** badge below.
2. In Colab, add a new code cell above the first notebook cell and run:
   `!git clone https://github.com/peptidemodel/cookbooks /content/cookbooks`
3. Then run the notebook cells in order from the top.

Start with **notebook 01** — do not open a later notebook first.

---

## Who This Is For

- Researchers who want to run peptide design explorations in Google Colab
- Beginners to intermediate users who know some Python but are new to peptide modeling
- Anyone who wants a repeatable starting point before committing to a full project setup

This cookbook assumes:
- basic Python familiarity
- you know what a PDB file is
- you know roughly what peptides and proteins are
- you do not need to be a structural biologist

---

## What This Cookbook Can Support

Claims you can make after completing the full sequence:

- "I have a frozen, documented target spec with explicit chain and numbering assumptions."
- "My scoring lane can distinguish a reference peptide from obvious nonsense controls."
- "This candidate peptide is worth deeper investigation under a stronger lane."
- "I have a shortlist and a documented rationale for promoting it to strong validation."

---

## What This Cookbook Cannot Support

- Binding affinity values (Kd, Ki, IC50)
- Claims that any peptide "binds" the target
- Fine-grained potency ranking without a validated physics-based or structure-prediction lane
- Synthesis recommendations from notebook scores alone

The heuristic scoring lane used in these notebooks is a **workflow calibration tool**,
not a docking engine. Read the "What this notebook cannot prove" section in each notebook.

---

## Notebook Order

Work through these in order. Later notebooks depend on outputs from earlier ones.

| # | Notebook | Open in Colab | Purpose | Tier |
|---|----------|--------------|---------|------|
| 01 | `01_target_surface_sanity.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/peptidemodel/cookbooks/blob/main/colab-basics/notebooks/01_target_surface_sanity.ipynb) | Freeze target chain, pocket, numbering | Free |
| 02 | `02_reference_panel_check.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/peptidemodel/cookbooks/blob/main/colab-basics/notebooks/02_reference_panel_check.ipynb) | Prove the lane separates reference from nonsense | Free |
| 03 | `03_single_peptide_eval.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/peptidemodel/cookbooks/blob/main/colab-basics/notebooks/03_single_peptide_eval.ipynb) | Evaluate one candidate peptide | Free |
| 04 | `04_small_sar_scan.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/peptidemodel/cookbooks/blob/main/colab-basics/notebooks/04_small_sar_scan.ipynb) | Scan variants of a seed peptide | Free / Paid |
| 05 | `05_promote_to_strong_validation.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/peptidemodel/cookbooks/blob/main/colab-basics/notebooks/05_promote_to_strong_validation.ipynb) | Build promotion bundle for stronger validation | Free |

**Start with notebook 01.** Do not skip to 03 or 04 before completing 01 and 02.

---

## Free vs Paid Colab: What Changes

| Behavior | Free Colab | Paid Colab |
|----------|-----------|------------|
| Heuristic scoring lane | Full | Full |
| Reference panel size | 4 peptides | 4–20 peptides |
| SAR scan panel size | ≤ 40 variants | ≤ 200 variants |
| Optional ESMFold lane | Risky (RAM limit) | Feasible |
| Boltz-1 or AF2 GPU lane | Not recommended | Feasible |
| Session persistence | None | None (save workspace!) |

The main bottleneck on free Colab is **session memory and runtime limits**, not this
notebook's code. All notebooks write outputs to disk so you can resume after disconnects.

---

## How to Use the Workspace

Each notebook writes outputs under `./workspace/` relative to the notebook location.
In Colab, outputs are lost when the session ends unless you persist them to Google Drive.
NB01 contains a commented-out Drive-mount block in the config cell — uncomment the two
lines to save outputs to `MyDrive/peptide_workspace` across sessions.

Default workspace layout after running all notebooks:

```
workspace/
  target_spec.json          # frozen target spec from notebook 01
  target_summary.txt        # human-readable spec summary
  {PDB_ID}.pdb              # downloaded PDB file from notebook 01
  reference_panel/
    panel_scores.csv        # scored reference panel from notebook 02
    panel_chart.png
    panel_interpretation.txt
  single_eval/
    eval_result.json        # single peptide result from notebook 03
    sub_score_breakdown.png
  sar_scan/
    sar_scores.csv          # all SAR variants ranked by score (notebook 04)
    sar_shortlist.csv       # improved variants only
    sar_heatmap.png
    sar_scan_meta.json      # scan metadata and top-5 summary
  promotion/
    shortlist.json          # machine-readable promotion bundle (notebook 05)
    promotion_summary.md    # human-readable rationale and handoff protocol
    shortlist_candidates.fasta  # FASTA for AF2 multimer / Boltz-1 input
    upload_stubs/
      <label>/
        card.yaml           # canonical platform upload card (fill in after structure prediction)
        readme.md           # readme stub for platform card
```

---

## How This Cookbook Differs From Project Notebooks Under projects/

Project-specific notebooks under `projects/*/colab/` are handoff artifacts for a
specific target (e.g., myostatin, orexin). They assume a particular PDB, chain
assignment, and reference panel.

This cookbook is:
- target-agnostic: you supply the PDB ID and pocket definition
- workflow-first: it teaches you the decision gates, not just the scripts
- parameterized: same notebooks work for different targets by changing config

Use project notebooks when you have a real project to run.
Use this cookbook to learn the methodology or start a new target from scratch.

---

## Relationship to the Intermediate Cookbook

The `intermediate-linux-gpu/` cookbook in this repo is the normative reference
for full Linux/GPU projects with multi-lane validation. This Colab cookbook is a
lightweight entry point that respects the same phase discipline:

- freeze the spec first
- calibrate before sweeping
- never claim more than the lane supports
- keep negative controls visible

If you outgrow this cookbook, migrate your work into the intermediate cookbook structure.
