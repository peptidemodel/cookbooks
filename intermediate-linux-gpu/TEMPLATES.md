# Templates

## 1. Project Root README Template

```md
# <project-name>

## Target
- Primary target:
- Primary structure:
- Primary chain:

## Mechanism Hypothesis
- 

## Current Phase
- 

## Active Phase Doc
- `docs/...`

## Main Outputs
- `docs/...`
- `pipeline/...`
- `results/...`

## Platform Mode
- `local_only` | `platform_writeback`

## Current Decision Rule
- 
```

## 1b. Research README Template

```md
# <project-name> Research Notes

## Environment
- primary lane:
- stronger lane:

## Canonical Commands
- smoke:
- reference:
- candidate:

## Authoritative Files
- `docs/...`
- `pipeline/...`
- `results/...`
- `upload_ready/...`
```

## 2. Phase Report Template

```md
# <project> <phase-name>

## Goal
- 

## Inputs
- target:
- panel:
- script:

## Gate
- 

## Result
- PASS / FAIL

## Key Numbers
- 

## Main Files
- 

## Interpretation
- 

## Next Step
- 
```

## 3. Candidate Panel Row Template

Use JSON or TSV, but keep the same logical fields:

```json
{
  "label": "sA_example",
  "sequence": "AWAWFK",
  "series": "series_a",
  "hypothesis": "What this mutation is trying to test.",
  "inspiration": "reference peptide or mechanism",
  "sar_move": "single concise move description",
  "standard_l_aa_only": true
}
```

## 4. Negative Result Template

```md
# <project> Negative Result

## What Failed
- 

## Why It Matters
- 

## Evidence
- scrambled control:
- poly-Ala:
- decoy comparison:

## What The Lane Can Still Be Used For
- geometry only
- rough triage only
- not usable

## What Not To Claim
- 
```

## 5. Final Peptide Card Template

```md
## <label>

- Sequence:
- Intended target:
- Best surviving evidence:
- Main metric:
- Main advantage:
- Main caveat:
- Ready for:
  - more computation
  - synthesis
  - hold
```

## 5b. Platform Card YAML Template

```yaml
title: "sE_protease_armor — GLP-1R/GIPR agonist (E3A on tirzepatide)"
sequence: "YAAGTFTSDYSIALDKIAQKAFVQWLIAGGPSSGAPPPS"
targets:
  - glp-1r
  - gipr
scaffold: tirzepatide
parent_card: pep-00016
status: computed

metrics:
  - key: ipTM
    value: 0.894
    tool: Boltz-1
  - key: pLDDT
    value: 0.828
    tool: Boltz-1

source:
  kind: other
  notes: "Designed by ColabDesign, predicted by Boltz-1 on NVIDIA Tesla M40"

structure_file: structure.pdb
readme_file: readme.md
```

Rules:

- `targets` must use platform slugs, not human-readable names
- use `parent_card` when the design is derived from an existing platform card
- use `status: computed` for prediction-only cards
- do not invent field names
- do not include local pipeline metadata such as `mode`

## 5c. Upload-Ready Folder Template

```text
upload_ready/
  lead_a/
    card.yaml
    structure.pdb
    readme.md
```

One folder per promoted design.
Nothing else belongs in `upload_ready/`.

## 5d. Public Readme Template

```md
## <label> — <target>

Short plain-language description of what changed and why it might matter.

### Prediction
- Model:
- Main metric:
- Reference comparison:

### Design rationale
- 

### Limitations
- computational prediction only
- what still needs wet-lab confirmation
```

## 5e. Research Log Template

```md
# Research Log — <project> <run>

## What passed
- 

## What failed
- 

## Best result
- label:
- why it is interesting:

## What not to publish
- 

## Next experiments
- 

## Reproducibility notes
- model:
- seed:
- runtime:
- hardware:
- command:
```

## 6. Experiment-Loop Rules For Agents

If an AI agent runs the project:

1. Read the project root `README.md`
2. Read the current phase report
3. Read the reference panel summary before touching candidates
4. Never alter the target spec silently
5. Never delete failed experiments from the record
6. When a lane fails, write the failure down before changing tools
7. At the end, print the conclusion in chat before pointing to files
8. Create `upload_ready/` only for promoted designs
9. Write `research_log.md` as the local teaching document

## 7. Minimal Command Pattern

Cheap local lane:

```bash
cd project/pipeline
python run_experiment.py --check
python run_experiment.py
```

High-fidelity validation lane:

```bash
python some_phase_target_decoy.py
python some_phase_reference_panel.py
```

The exact commands differ by project. The pattern does not:

- validate environment
- run references
- run decoys
- then candidates

## 8. The One-Line Rule

Before every new phase, write one line that answers:

> What would have to happen for this phase to be considered a failure?

If you cannot answer that before you run it, the phase is not designed tightly enough.
