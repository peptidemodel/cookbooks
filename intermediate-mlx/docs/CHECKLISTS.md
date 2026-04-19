# Checklists

## Before First Prediction

- hardware profile recorded
- weights path recorded
- weights hash recorded
- runner YAML chosen
- smoke-test manifest location chosen
- smoke-test command documented
- output directory convention chosen

## Before Reference Preview

- target sequence source recorded
- peptide sequence source recorded
- reference positive defined
- real negative defined
- query names chosen
- chain order frozen

## Before Large Batch

- preview results reviewed manually at least once
- batch grouping rule defined
- batch size defined
- timeout rule defined
- retry rule defined
- `state.json` fields defined
- failure logging format defined
- query naming pattern documented

## Before Promotion to Upgrade Mode

- preview lane separated at least one control from one negative
- upgrade trigger is named in the active phase doc
- upgraded run would change a decision
- manifest format is complete
- output storage location is clear
- expected stop condition is written down

## Before Final Closeout

- promoted results have manifests
- failed results are preserved
- unresolved caveats are listed
- authoritative files are named
- next recommended phase is explicit
- plain-language chat conclusion drafted
- publish / do-not-publish verdict stated explicitly
- best result named with one sentence of biology
- `research_log.md` written locally

If any design passed the promotion gate:

- `upload_ready/` exists
- one folder per promoted design
- each folder contains only `card.yaml`, `structure.pdb` or `.cif`, and `readme.md`
- `targets` uses platform slug array form
- `status: computed` is present
- `parent_card` is included when the design forks an existing platform card
- no invented fields such as `mode`, `main_metric`, `metric_name`, `pdb_path`, or `modeling_tool`

Never put failed designs or pipeline intermediates into `upload_ready/`.
