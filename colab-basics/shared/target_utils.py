"""
target_utils.py — helpers for loading, inspecting, and freezing target structures.

These functions are designed to be readable by someone learning the workflow.
They use biopython for PDB parsing (pip install biopython).
"""

import json
import io
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def fetch_pdb(pdb_id: str, save_path: Optional[Path] = None) -> str:
    """
    Download a PDB file from the RCSB database.

    Returns the PDB text as a string. Optionally saves to disk.

    Example:
        pdb_text = fetch_pdb("1ABC")
    """
    pdb_id = pdb_id.upper().strip()
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url, timeout=30)
    if response.status_code != 200:
        raise ValueError(
            f"Could not fetch PDB {pdb_id} from RCSB "
            f"(HTTP {response.status_code}). "
            f"Check the PDB ID and your internet connection."
        )
    pdb_text = response.text
    if save_path is not None:
        Path(save_path).write_text(pdb_text)
    return pdb_text


def parse_pdb_chains(pdb_text: str, structure_id: str = "target") -> Dict:
    """
    Parse a PDB string and return a summary of all chains and residues.

    Returns a dict with:
      chains: list of chain info dicts
      total_residues: int
      total_chains: int

    Requires biopython.
    """
    try:
        from Bio.PDB import PDBParser
    except ImportError:
        raise ImportError("biopython is required: pip install biopython")

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(structure_id, io.StringIO(pdb_text))

    chain_info = []
    for model in structure:
        for chain in model:
            residues = [r for r in chain.get_residues() if r.id[0] == " "]
            if not residues:
                continue
            res_ids = [r.id[1] for r in residues]
            res_names = [r.resname.strip() for r in residues]
            aa_residues = [r for r in residues if r.resname.strip() in _STANDARD_AA]
            chain_info.append({
                "chain_id": chain.id,
                "n_residues": len(residues),
                "n_amino_acid_residues": len(aa_residues),
                "residue_range": [min(res_ids), max(res_ids)] if res_ids else [None, None],
                "first_residue": res_ids[0] if res_ids else None,
                "last_residue": res_ids[-1] if res_ids else None,
                "residue_names_sample": res_names[:5],
                "note": (
                    "likely peptide ligand" if len(aa_residues) < 30
                    else "protein chain"
                ),
            })
    return {
        "chains": chain_info,
        "total_chains": len(chain_info),
        "total_residues": sum(c["n_residues"] for c in chain_info),
        "structure_id": structure_id,
    }


def extract_pocket_residues(
    pdb_text: str,
    chain_id: str,
    pocket_residue_ids: List[int],
    structure_id: str = "target",
) -> Dict:
    """
    Extract and validate a set of residues that define the binding pocket.

    pocket_residue_ids: list of residue sequence numbers (as they appear in the PDB).

    Returns a dict with:
      found: residues that were found in the structure
      missing: residue IDs that were not found
      pocket_sequence: one-letter code sequence of pocket residues (where possible)
      chain_id: as passed in
    """
    try:
        from Bio.PDB import PDBParser
        from Bio.PDB.Polypeptide import protein_letters_3to1
    except ImportError:
        raise ImportError("biopython is required: pip install biopython")

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(structure_id, io.StringIO(pdb_text))

    residue_map = {}
    for model in structure:
        chain = model[chain_id] if chain_id in [c.id for c in model] else None
        if chain is None:
            raise ValueError(
                f"Chain '{chain_id}' not found in structure. "
                f"Available chains: {[c.id for c in model]}"
            )
        for res in chain.get_residues():
            if res.id[0] == " ":
                residue_map[res.id[1]] = res.resname.strip()

    found = []
    missing = []
    for res_id in pocket_residue_ids:
        if res_id in residue_map:
            found.append({"res_id": res_id, "resname": residue_map[res_id]})
        else:
            missing.append(res_id)

    pocket_seq = ""
    for entry in found:
        three = entry["resname"]
        pocket_seq += _THREE_TO_ONE.get(three, "?")

    return {
        "chain_id": chain_id,
        "requested": pocket_residue_ids,
        "found": found,
        "missing": missing,
        "n_found": len(found),
        "n_missing": len(missing),
        "pocket_sequence": pocket_seq,
        "warning": (
            f"{len(missing)} pocket residue(s) not found: {missing}. "
            "Check your residue IDs against the PDB file."
            if missing else None
        ),
    }


def get_chain_sequence(pdb_text: str, chain_id: str, structure_id: str = "target") -> str:
    """
    Extract the full amino acid sequence of a chain from a PDB string.
    Returns a one-letter code string (unknown residues → 'X').
    Useful for building AF2 multimer FASTA files that include the receptor chain.
    """
    try:
        from Bio.PDB import PDBParser
    except ImportError:
        raise ImportError("biopython is required: pip install biopython")

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(structure_id, io.StringIO(pdb_text))
    for model in structure:
        chain = next((c for c in model if c.id == chain_id), None)
        if chain is None:
            raise ValueError(
                f"Chain '{chain_id}' not found. "
                f"Available chains: {[c.id for c in model]}"
            )
        seq = ""
        for res in chain.get_residues():
            if res.id[0] == " ":
                seq += _THREE_TO_ONE.get(res.resname.strip(), "X")
        return seq
    raise ValueError("No models found in structure")


def make_target_spec(
    pdb_id: str,
    chain_id: str,
    pocket_residue_ids: List[int],
    mechanism_hypothesis: str,
    pocket_description: str,
    positive_reference: str,
    positive_reference_source: str,
    negative_controls: Optional[List[str]] = None,
    notes: str = "",
) -> Dict:
    """
    Build the canonical target_spec dict.

    This dict is saved as target_spec.json and loaded by all subsequent notebooks.
    Fill in the required fields carefully — downstream results depend on them.
    """
    spec = {
        "pdb_id": pdb_id.upper(),
        "chain_id": chain_id,
        "pocket_residue_ids": sorted(pocket_residue_ids),
        "mechanism_hypothesis": mechanism_hypothesis,
        "pocket_description": pocket_description,
        "numbering_note": (
            "Residue IDs are as they appear in the downloaded PDB file. "
            "If you use a renumbered or cleaned structure, update this field."
        ),
        "reference_policy": {
            "positive_control": {
                "sequence": positive_reference,
                "source": positive_reference_source,
            },
            "negative_controls": negative_controls or ["AAAAAAAAAA", "RANDOMCTRL"],
        },
        "notes": notes,
        "cookbook": "colab-basics",
        "version": "1.0",
    }
    return spec


def save_target_spec(spec: Dict, path: Path) -> None:
    Path(path).write_text(json.dumps(spec, indent=2))


def load_target_spec(path: Path) -> Dict:
    return json.loads(Path(path).read_text())


def format_target_summary(spec: Dict, chain_info: Dict, pocket_info: Dict) -> str:
    """
    Build a plain-text summary of the frozen target spec.
    Designed to be readable by someone new to the workflow.
    """
    lines = [
        "=" * 60,
        "TARGET SPEC SUMMARY",
        "=" * 60,
        "",
        f"PDB ID      : {spec['pdb_id']}",
        f"Chain       : {spec['chain_id']}",
        f"Pocket      : {spec['pocket_description']}",
        f"Hypothesis  : {spec['mechanism_hypothesis']}",
        "",
        "--- Pocket Residues ---",
        f"  Requested : {spec['pocket_residue_ids']}",
        f"  Found     : {pocket_info['n_found']} / {len(spec['pocket_residue_ids'])}",
        f"  Sequence  : {pocket_info['pocket_sequence']}",
    ]
    if pocket_info.get("warning"):
        lines.append(f"  WARNING   : {pocket_info['warning']}")
    lines += [
        "",
        "--- Chain Summary ---",
    ]
    for c in chain_info.get("chains", []):
        lines.append(
            f"  Chain {c['chain_id']}: {c['n_amino_acid_residues']} AA residues, "
            f"range {c['residue_range'][0]}–{c['residue_range'][1]} ({c['note']})"
        )
    lines += [
        "",
        "--- Reference Policy ---",
        f"  Positive control  : {spec['reference_policy']['positive_control']['sequence']}",
        f"  Source            : {spec['reference_policy']['positive_control']['source']}",
        f"  Negative controls : {spec['reference_policy']['negative_controls']}",
        "",
        "--- Numbering Note ---",
        f"  {spec['numbering_note']}",
        "",
        "IMPORTANT: Check that the chain and residue IDs above match what you",
        "actually intend. Numbering mismatches are the most common source of",
        "invalid downstream results.",
        "=" * 60,
    ]
    return "\n".join(lines)


_STANDARD_AA = {
    "ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY",
    "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER",
    "THR", "TRP", "TYR", "VAL",
}

_THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
}
