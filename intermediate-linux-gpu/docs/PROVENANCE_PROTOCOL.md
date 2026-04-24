# Provenance Protocol

This protocol is for reference peptides, benchmark ligands, and named literature anchors.

If a peptide name enters the project, you must know what evidence backs that name.

## Allowed Provenance Labels

Use one of these labels explicitly.

### `primary-paper-backed`

Meaning:

- sequence verified from the actual paper or patent text

Use when:

- the exact sequence is visible in the primary source

### `secondary-source-backed`

Meaning:

- sequence comes from a review, database, or trusted secondary source
- primary source not yet checked directly

Use when:

- you need a working reference but the primary paper is not yet in hand

### `structure-derived`

Meaning:

- sequence extracted directly from a solved structure

Use when:

- the peptide is visible in a PDB complex

Important:

- structure-derived does **not** mean the literature naming is verified

### `proxy-sequence`

Meaning:

- the real molecule contains non-standard chemistry, D-amino acids, cyclization, acylation, or other features
- the project is using a standard-AA or simplified approximation

Use when:

- you need computational comparability but are not modeling the full chemistry

### `legacy-internal`

Meaning:

- old internal label or sequence carried in repo history
- not currently trusted as literature truth

Use when:

- you discover an attribution or provenance problem

## Required Questions For Every Named Reference

Before relying on a named benchmark, answer:

1. What is the exact sequence we are using?
2. Is it the real chemistry or a proxy?
3. Which paper, patent, database, or structure backs it?
4. Is the name attached to the correct sequence?
5. If extracted from structure, which chain and residues?

If any answer is missing, do not treat the benchmark name as settled.

## When Primary Source Is Mandatory

Primary source is mandatory when:

- the sequence identity is disputed
- you are claiming a literature benchmark
- substitutions or noncanonical residues matter for SAR
- the sequence will appear in a synthesis or proposal document

## Structure Extraction Rule

If you extract a peptide from a PDB:

record:

- PDB ID
- chain
- residue range
- extracted sequence
- whether that extraction matches the literature name

This is how you avoid wrong-chain mistakes.

## Recommended Reference Table Fields

Use fields like:

```json
{
  "label": "df3",
  "sequence": "VNDNTLFKWMIFNG",
  "chemistry": "amide",
  "provenance": "primary-paper-backed",
  "source": "Takayama 2019 BMCL",
  "structure_match": {
    "pdb": "3HH2",
    "chain": "C",
    "residues": "41-54"
  },
  "notes": "real DF-3; not the legacy internal 3HH2 myostatin-chain fragment"
}
```

## What To Do When Provenance Breaks

If you discover the benchmark is wrong:

1. do not hide it
2. write a correction note
3. relabel the old sequence honestly
4. rebuild the affected reference lane
5. tell collaborators which conclusions were based on the bad reference

## Practical Rule

Do not let a convenient label outrun the evidence behind it.
