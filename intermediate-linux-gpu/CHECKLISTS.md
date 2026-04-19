# Checklists

## New Project Kickoff

- Create a fresh project folder from the template
- Add `target.pdb`
- Add `peptide_config.py`
- Record target chain and residue numbering
- Write a short `target_brief.md`
- Define at least one positive control
- Define at least one negative control
- Decide which lane is cheap triage and which lane is strong validation

Do not start candidate generation before this is done.

## Phase 0: Target Freeze

- Is the source structure the right biological state?
- Are chain IDs frozen in writing?
- Are hotspot residues documented in source numbering?
- If predicted complexes renumber chains, is that mapping documented?
- Do you know what the scorer will actually read?

If any answer is no, stop.

## Phase 1: Reference Calibration

- Positive control included
- Weaker / proxy control included
- Poly-Ala or composition-only negative included
- Scrambled negative included
- Output summary written to TSV and markdown

Pass condition:
- obvious negatives do not behave like strong positives

## Phase 2: Target-Decoy

- Real target built
- Hotspot-killed decoy built
- Rotated or cavity-disrupted decoy built
- Wrong-face / irrelevant decoy built if possible
- Same scoring lane used across all

Pass condition:
- real positives prefer the real target
- negatives do not look equally good everywhere

## Phase 3: Candidate Panel

- Panel file exists in JSON or TSV
- References included in the same panel
- Explicit negatives included in the same panel
- Each series has a hypothesis
- Each sequence has a label

Do not ship unnamed sequences.

## Phase 4: Filtering

- Geometry gate defined
- Specificity gate defined
- Developability or permeability axis defined
- Ranking rule written down before running

If you change the ranking rule after seeing results, document why.

## Phase 5: Final Shortlist

For each finalist:

- sequence
- series
- best surviving lane
- key metric
- main caveat
- whether it beat the real reference or only a proxy

Before calling the experiment complete:

- plain-language chat conclusion drafted
- publish / do-not-publish verdict stated explicitly
- best result named with one sentence of biology
- specific next experiments suggested
- failures summarized honestly

If any design passed the promotion gate:

- `upload_ready/` exists
- one folder per promoted design
- each folder contains only `card.yaml`, `structure.pdb`, and `readme.md`
- `targets` uses platform slug array form
- `status: computed` is present
- `parent_card` is included when the design forks an existing platform card
- no invented fields such as `mode`, `main_metric`, `metric_name`, `pdb_path`, or `modeling_tool`

Always:

- `research_log.md` written locally
- failed designs kept out of `upload_ready/`
- pipeline intermediates kept in `results/` or `pipeline/`, not in the upload package

## Commit Hygiene

Commit per phase or per meaningful methodological change.

Good:
- “Add target-decoy validation for corrected DF-3 panel”
- “Fix MC1R hotspot numbering and rescore saved runs”

Bad:
- “misc”
- “more updates”
- “stuff”

## Team Coordination

When multiple agents or collaborators are involved:

- assign lane ownership explicitly
- separate compute lanes from analysis lanes
- send file paths, commit SHAs, and gate verdicts
- do not rely on verbal summaries only

Every cross-agent update should include:

- what was run
- what passed or failed
- where the files are
- what the next gate is
