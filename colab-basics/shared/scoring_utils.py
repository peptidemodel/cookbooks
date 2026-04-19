"""
scoring_utils.py — peptide scoring utilities for the Colab basics cookbook.

IMPORTANT — READ THIS FIRST:

The score produced here is a COMPOSITION AND PROPERTY HEURISTIC, not a
physics-based score and not a docking score. It measures how well a peptide's
gross properties (charge, hydrophobicity, length, sequence similarity) match
the pocket hints defined in your target spec.

What this score can support:
- Gross sanity checks: is the peptide completely the wrong charge?
- Calibration: does a known reference score better than an obvious nonsense control?
- Triage: which variants look most different from the seed?

What this score cannot support:
- Binding affinity predictions
- Fine-grained potency ranking
- Selectivity claims

For higher-fidelity scoring, see the optional ESMFold section at the bottom of this file.
"""

import math
import json
from typing import Dict, List, Optional, Tuple


# ── Amino acid properties ────────────────────────────────────────────────────
# charge: net charge at pH 7 (approximate)
# hydrophobic: 0 = hydrophilic, 1 = hydrophobic (Kyte-Doolittle normalised, rough)
# size: 0 = small, 1 = large
AMINO_ACID_PROPS: Dict[str, Dict[str, float]] = {
    "A": {"charge": 0.0,  "hydrophobic": 0.62, "size": 0.2},
    "R": {"charge": 1.0,  "hydrophobic": 0.0,  "size": 0.9},
    "N": {"charge": 0.0,  "hydrophobic": 0.0,  "size": 0.5},
    "D": {"charge": -1.0, "hydrophobic": 0.0,  "size": 0.5},
    "C": {"charge": 0.0,  "hydrophobic": 0.73, "size": 0.4},
    "Q": {"charge": 0.0,  "hydrophobic": 0.0,  "size": 0.6},
    "E": {"charge": -1.0, "hydrophobic": 0.0,  "size": 0.6},
    "G": {"charge": 0.0,  "hydrophobic": 0.0,  "size": 0.1},
    "H": {"charge": 0.1,  "hydrophobic": 0.17, "size": 0.6},
    "I": {"charge": 0.0,  "hydrophobic": 1.0,  "size": 0.5},
    "L": {"charge": 0.0,  "hydrophobic": 0.96, "size": 0.5},
    "K": {"charge": 1.0,  "hydrophobic": 0.0,  "size": 0.7},
    "M": {"charge": 0.0,  "hydrophobic": 0.74, "size": 0.6},
    "F": {"charge": 0.0,  "hydrophobic": 1.0,  "size": 0.7},
    "P": {"charge": 0.0,  "hydrophobic": 0.36, "size": 0.4},
    "S": {"charge": 0.0,  "hydrophobic": 0.0,  "size": 0.3},
    "T": {"charge": 0.0,  "hydrophobic": 0.0,  "size": 0.4},
    "W": {"charge": 0.0,  "hydrophobic": 0.97, "size": 0.9},
    "Y": {"charge": 0.0,  "hydrophobic": 0.63, "size": 0.8},
    "V": {"charge": 0.0,  "hydrophobic": 0.86, "size": 0.4},
}

# BLOSUM62 similarity matrix (subset for scoring purposes)
# Values are log-odds scores from the standard BLOSUM62 matrix.
# We use this to compare a candidate to the positive reference sequence.
BLOSUM62 = {
    ("A","A"): 4,  ("A","R"):-1, ("A","N"):-2, ("A","D"):-2, ("A","C"): 0,
    ("A","Q"):-1,  ("A","E"):-1, ("A","G"): 0, ("A","H"):-2, ("A","I"):-1,
    ("A","L"):-1,  ("A","K"):-1, ("A","M"):-1, ("A","F"):-2, ("A","P"):-1,
    ("A","S"): 1,  ("A","T"): 0, ("A","W"):-3, ("A","Y"):-2, ("A","V"): 0,
    ("R","R"): 5,  ("R","N"):-1, ("R","D"):-2, ("R","C"):-3, ("R","Q"): 1,
    ("R","E"): 0,  ("R","G"):-2, ("R","H"): 0, ("R","I"):-3, ("R","L"):-2,
    ("R","K"): 2,  ("R","M"):-1, ("R","F"):-3, ("R","P"):-2, ("R","S"):-1,
    ("R","T"):-1,  ("R","W"):-3, ("R","Y"):-2, ("R","V"):-3,
    ("N","N"): 6,  ("N","D"): 1, ("N","C"):-3, ("N","Q"): 0, ("N","E"): 0,
    ("N","G"): 0,  ("N","H"): 1, ("N","I"):-3, ("N","L"):-3, ("N","K"): 0,
    ("N","M"):-2,  ("N","F"):-3, ("N","P"):-2, ("N","S"): 1, ("N","T"): 0,
    ("N","W"):-4,  ("N","Y"):-2, ("N","V"):-3,
    ("D","D"): 6,  ("D","C"):-3, ("D","Q"): 0, ("D","E"): 2, ("D","G"):-1,
    ("D","H"):-1,  ("D","I"):-3, ("D","L"):-4, ("D","K"):-1, ("D","M"):-3,
    ("D","F"):-3,  ("D","P"):-1, ("D","S"): 0, ("D","T"):-1, ("D","W"):-4,
    ("D","Y"):-3,  ("D","V"):-3,
    ("C","C"): 9,  ("C","Q"):-3, ("C","E"):-4, ("C","G"):-3, ("C","H"):-3,
    ("C","I"):-1,  ("C","L"):-1, ("C","K"):-3, ("C","M"):-1, ("C","F"):-2,
    ("C","P"):-3,  ("C","S"):-1, ("C","T"):-1, ("C","W"):-2, ("C","Y"):-2,
    ("C","V"):-1,
    ("Q","Q"): 5,  ("Q","E"): 2, ("Q","G"):-2, ("Q","H"): 0, ("Q","I"):-3,
    ("Q","L"):-2,  ("Q","K"): 1, ("Q","M"): 0, ("Q","F"):-3, ("Q","P"):-1,
    ("Q","S"): 0,  ("Q","T"):-1, ("Q","W"):-2, ("Q","Y"):-1, ("Q","V"):-2,
    ("E","E"): 5,  ("E","G"):-2, ("E","H"): 0, ("E","I"):-3, ("E","L"):-3,
    ("E","K"): 1,  ("E","M"):-2, ("E","F"):-3, ("E","P"):-1, ("E","S"): 0,
    ("E","T"):-1,  ("E","W"):-3, ("E","Y"):-2, ("E","V"):-2,
    ("G","G"): 6,  ("G","H"):-2, ("G","I"):-4, ("G","L"):-4, ("G","K"):-2,
    ("G","M"):-3,  ("G","F"):-3, ("G","P"):-2, ("G","S"): 0, ("G","T"):-2,
    ("G","W"):-2,  ("G","Y"):-3, ("G","V"):-3,
    ("H","H"): 8,  ("H","I"):-3, ("H","L"):-3, ("H","K"):-1, ("H","M"):-2,
    ("H","F"):-1,  ("H","P"):-2, ("H","S"):-1, ("H","T"):-2, ("H","W"):-2,
    ("H","Y"): 2,  ("H","V"):-3,
    ("I","I"): 4,  ("I","L"): 2, ("I","K"):-1, ("I","M"): 1, ("I","F"): 0,
    ("I","P"):-3,  ("I","S"):-2, ("I","T"):-1, ("I","W"):-3, ("I","Y"):-1,
    ("I","V"): 3,
    ("L","L"): 4,  ("L","K"):-2, ("L","M"): 2, ("L","F"): 0, ("L","P"):-3,
    ("L","S"):-2,  ("L","T"):-1, ("L","W"):-2, ("L","Y"):-1, ("L","V"): 1,
    ("K","K"): 5,  ("K","M"):-1, ("K","F"):-3, ("K","P"):-1, ("K","S"): 0,
    ("K","T"):-1,  ("K","W"):-3, ("K","Y"):-2, ("K","V"):-2,
    ("M","M"): 5,  ("M","F"): 0, ("M","P"):-2, ("M","S"):-1, ("M","T"):-1,
    ("M","W"):-1,  ("M","Y"):-1, ("M","V"): 1,
    ("F","F"): 6,  ("F","P"):-4, ("F","S"):-2, ("F","T"):-2, ("F","W"): 1,
    ("F","Y"): 3,  ("F","V"):-1,
    ("P","P"): 7,  ("P","S"):-1, ("P","T"):-1, ("P","W"):-4, ("P","Y"):-3,
    ("P","V"):-2,
    ("S","S"): 4,  ("S","T"): 1, ("S","W"):-3, ("S","Y"):-2, ("S","V"):-2,
    ("T","T"): 5,  ("T","W"):-2, ("T","Y"):-2, ("T","V"): 0,
    ("W","W"): 11, ("W","Y"): 2, ("W","V"):-3,
    ("Y","Y"): 7,  ("Y","V"):-1,
    ("V","V"): 4,
}


def _blosum62(a: str, b: str) -> int:
    """Look up BLOSUM62 score for pair (a,b), symmetric."""
    if a == b:
        return BLOSUM62.get((a, a), 0)
    pair = (min(a, b), max(a, b))
    return BLOSUM62.get(pair, BLOSUM62.get((a, b), 0))


def peptide_net_charge(seq: str) -> float:
    props = AMINO_ACID_PROPS
    return sum(props.get(aa, {}).get("charge", 0.0) for aa in seq.upper() if aa in props)


def peptide_hydrophobic_fraction(seq: str) -> float:
    seq = seq.upper()
    props = AMINO_ACID_PROPS
    hydro = [props.get(aa, {}).get("hydrophobic", 0.0) for aa in seq if aa in props]
    return sum(hydro) / len(hydro) if hydro else 0.0


def blosum_similarity(seq_a: str, seq_b: str) -> float:
    """
    Normalised BLOSUM62 similarity between two sequences.
    Aligns the starts of both sequences for min(len_a, len_b) positions — no gaps,
    no dynamic programming. Longer sequence tail is ignored.
    Returns value in [-1, 1] range (roughly).
    """
    a = seq_a.upper()
    b = seq_b.upper()
    if not a or not b:
        return 0.0
    min_len = min(len(a), len(b))
    max_len = max(len(a), len(b))
    # Score the overlap at the start (simple, not dynamic programming)
    raw = sum(_blosum62(a[i], b[i]) for i in range(min_len))
    max_self = sum(_blosum62(c, c) for c in a[:min_len])
    if max_self <= 0:
        return 0.0
    return raw / max_self


def score_peptide(
    sequence: str,
    target_spec: Dict,
    positive_reference: Optional[str] = None,
) -> Dict:
    """
    Score a single peptide against a target spec using the heuristic lane.

    Returns a dict with:
      composite_score: float in [0, 1] (higher nominally better)
      sub_scores: dict of named sub-scores
      interpretation: plain-text string
      lane: always "heuristic_composition" to be explicit

    target_spec must have the fields written by notebook 01's make_target_spec().
    positive_reference overrides the one in target_spec if provided.
    """
    seq = sequence.upper().replace(" ", "")
    valid = {aa for aa in AMINO_ACID_PROPS}
    unknown = [aa for aa in seq if aa not in valid]
    if unknown:
        return {
            "sequence": sequence,
            "composite_score": 0.0,
            "sub_scores": {},
            "interpretation": f"Sequence contains unknown amino acids: {unknown}. Check input.",
            "lane": "heuristic_composition",
            "error": True,
        }

    ref_seq = positive_reference or (
        target_spec.get("reference_policy", {})
        .get("positive_control", {})
        .get("sequence", "")
    )
    pocket_hints = target_spec.get("pocket_hints", {})
    optimal_len_min = pocket_hints.get("optimal_length_min", 8)
    optimal_len_max = pocket_hints.get("optimal_length_max", 20)
    pocket_charge_hint = pocket_hints.get("pocket_net_charge_hint", 0.0)
    pocket_hydrophobic_hint = pocket_hints.get("pocket_hydrophobic_hint", 0.5)

    # Sub-score 1: length fitness
    length = len(seq)
    if optimal_len_min <= length <= optimal_len_max:
        length_score = 1.0
    else:
        overshoot = max(0, length - optimal_len_max)
        undershoot = max(0, optimal_len_min - length)
        penalty = max(overshoot, undershoot)
        length_score = max(0.0, 1.0 - penalty * 0.1)

    # Sub-score 2: charge magnitude match
    # A charged pocket (|hint| >= 1) rewards peptides that are themselves
    # significantly charged (either sign). A near-neutral pocket rewards neutrality.
    # This does NOT use similarity to the reference — it compares the peptide's
    # intrinsic charge character against the pocket hint, so poly-Ala (neutral)
    # will score poorly when the pocket hint indicates a charged surface.
    pep_charge = peptide_net_charge(seq)
    pocket_charge_magnitude = abs(pocket_charge_hint)
    pep_charge_magnitude = abs(pep_charge)
    if pocket_charge_magnitude >= 1.0:
        # Charged pocket: sigmoid maps charge_magnitude 0→0.27, 1→0.50, 2→0.73, 3→0.88
        charge_score = _sigmoid(pep_charge_magnitude - 1.0)
    else:
        # Near-neutral pocket: reward neutral-ish peptides
        charge_score = _sigmoid(1.0 - pep_charge_magnitude)

    # Sub-score 3: hydrophobic match
    pep_hydro = peptide_hydrophobic_fraction(seq)
    hydro_diff = abs(pep_hydro - pocket_hydrophobic_hint)
    hydro_score = max(0.0, 1.0 - hydro_diff)

    # Composite: length + charge + hydrophobic only.
    # BLOSUM similarity to the reference is intentionally NOT part of the composite.
    # Including it would make the calibration panel circular (the reference would
    # always "pass" because it scores high similarity to itself). BLOSUM is reported
    # separately as a diagnostic below.
    weights = {"length": 0.30, "charge": 0.40, "hydrophobic": 0.30}
    composite = (
        weights["length"] * length_score
        + weights["charge"] * charge_score
        + weights["hydrophobic"] * hydro_score
    )

    # Diagnostic: BLOSUM similarity to reference (NOT in composite)
    blosum_diag = 0.0
    if ref_seq:
        blosum_diag = max(0.0, min(1.0, (blosum_similarity(seq, ref_seq) + 1.0) / 2.0))

    sub_scores = {
        "length_score": round(length_score, 3),
        "charge_score": round(charge_score, 3),
        "hydrophobic_score": round(hydro_score, 3),
        "net_charge": round(pep_charge, 2),
        "hydrophobic_fraction": round(pep_hydro, 3),
        "length": length,
        "reference_similarity_blosum": round(blosum_diag, 3),
        "blosum_note": "diagnostic only — not included in composite_score",
    }

    interpretation = _interpret_score(composite, sub_scores)

    return {
        "sequence": sequence,
        "composite_score": round(composite, 4),
        "sub_scores": sub_scores,
        "interpretation": interpretation,
        "lane": "heuristic_composition",
        "error": False,
    }


def score_panel(
    panel: List[Dict],
    target_spec: Dict,
) -> List[Dict]:
    """
    Score a list of peptides. Each entry should be a dict with 'label' and 'sequence'.
    Returns the same list with score results added to each entry.
    """
    ref_seq = (
        target_spec.get("reference_policy", {})
        .get("positive_control", {})
        .get("sequence", "")
    )
    results = []
    for entry in panel:
        result = score_peptide(entry["sequence"], target_spec, positive_reference=ref_seq)
        results.append({**entry, **result})
    results.sort(key=lambda x: x.get("composite_score", 0.0), reverse=True)
    return results


def interpret_panel_separation(panel_results: List[Dict]) -> Tuple[str, str]:
    """
    Given scored panel results, determine if the lane separates them adequately.

    The primary gate is: does the reference clearly outscore the NONSENSE control
    (poly-Ala)? That is the only check a composition heuristic can support without
    becoming circular.

    The scrambled control is reported separately as informational. A pure composition
    heuristic CANNOT distinguish a sequence from its scrambled version (same amino acid
    content, different order). That is expected and documented — it is not a failure.

    Returns (status, explanation) where status is one of:
      "pass"     — reference clearly above nonsense control (margin > 0.15)
      "degraded" — weak separation from nonsense (margin 0.07–0.15)
      "fail"     — no separation from nonsense control (margin <= 0.07)
      "unknown"  — cannot assess (missing roles)
    """
    by_role: Dict[str, List[float]] = {}
    for entry in panel_results:
        role = entry.get("role", "unknown")
        by_role.setdefault(role, []).append(float(entry.get("composite_score", 0.0)))

    pos_scores = by_role.get("positive_control", [])
    nonsense_scores = by_role.get("nonsense_control", [])
    scrambled_scores = by_role.get("negative_control", [])

    if not pos_scores or not nonsense_scores:
        return (
            "unknown",
            "Cannot assess: need at least one positive_control and one nonsense_control "
            "(poly-Ala) in the panel. Check panel construction.",
        )

    best_pos = max(pos_scores)
    worst_pos = min(pos_scores)
    best_nonsense = max(nonsense_scores)
    margin = best_pos - best_nonsense

    # Scrambled info line (informational only — not part of pass/fail)
    if scrambled_scores:
        best_scrambled = max(scrambled_scores)
        scrambled_note = (
            f"Scrambled control: {best_scrambled:.3f} "
            f"({'above' if best_scrambled > best_nonsense else 'below'} nonsense). "
            "Note: a composition heuristic cannot distinguish reference from scrambled "
            "(same amino acid content). That is expected."
        )
    else:
        scrambled_note = "No scrambled control included in this panel."

    if margin > 0.15 and worst_pos > best_nonsense:
        status = "pass"
        explanation = (
            f"Reference clearly outscores the nonsense (poly-Ala) control. "
            f"Best positive: {best_pos:.3f}, best nonsense: {best_nonsense:.3f}, "
            f"margin: {margin:.3f}. "
            "The lane can support rough composition-based triage. "
            f"{scrambled_note}"
        )
    elif margin > 0.07:
        status = "degraded"
        explanation = (
            f"Weak but present separation from the nonsense control. "
            f"Best positive: {best_pos:.3f}, best nonsense: {best_nonsense:.3f}, "
            f"margin: {margin:.3f}. "
            "Fine-grained ranking is not reliable. "
            "Consider adjusting POCKET_NET_CHARGE_HINT or POCKET_HYDROPHOBIC_HINT in notebook 01. "
            f"{scrambled_note}"
        )
    else:
        status = "fail"
        explanation = (
            f"Reference does NOT clearly outscore the poly-Ala nonsense control. "
            f"Best positive: {best_pos:.3f}, best nonsense: {best_nonsense:.3f}, "
            f"margin: {margin:.3f}. "
            "DO NOT proceed. The pocket hints are not discriminating enough to support "
            "any ranking. Common causes: POCKET_NET_CHARGE_HINT is near 0 when the pocket "
            "is actually charged, or POCKET_HYDROPHOBIC_HINT is wrong. "
            "Fix notebook 01 config and re-run. "
            f"{scrambled_note}"
        )
    return status, explanation


def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def _interpret_score(composite: float, sub_scores: Dict) -> str:
    if composite >= 0.70:
        return (
            f"Score {composite:.3f}: Passes basic property checks. "
            "Worth including in further evaluation. "
            "This does NOT mean the peptide binds."
        )
    elif composite >= 0.50:
        return (
            f"Score {composite:.3f}: Moderate property match. "
            "May be worth scanning variants. "
            "Heuristic lane has limited resolution at this range."
        )
    elif composite >= 0.30:
        return (
            f"Score {composite:.3f}: Weak property match. "
            "Consider a different sequence or reviewing pocket hints."
        )
    else:
        return (
            f"Score {composite:.3f}: Poor property match. "
            f"Net charge: {sub_scores.get('net_charge', 'N/A')}, "
            f"hydrophobic fraction: {sub_scores.get('hydrophobic_fraction', 'N/A'):.2f}. "
            "Likely wrong composition for this pocket."
        )


# ── Optional stronger lane placeholder ──────────────────────────────────────
# To use ESM2 embeddings for scoring (requires transformers, esm, torch):
#
# from transformers import AutoTokenizer, EsmModel
# import torch
#
# def score_peptide_esm(sequence, target_spec, esm_model, tokenizer):
#     """
#     Score using cosine similarity of ESM2 embeddings to a reference.
#     Requires: pip install transformers torch
#     On free Colab this may OOM for large models. Use esm2_t6_8M_UR50D (smallest).
#     """
#     ref_seq = target_spec["reference_policy"]["positive_control"]["sequence"]
#     inputs_a = tokenizer(sequence, return_tensors="pt")
#     inputs_b = tokenizer(ref_seq, return_tensors="pt")
#     with torch.no_grad():
#         emb_a = esm_model(**inputs_a).last_hidden_state.mean(dim=1)
#         emb_b = esm_model(**inputs_b).last_hidden_state.mean(dim=1)
#     cos_sim = torch.nn.functional.cosine_similarity(emb_a, emb_b).item()
#     return {"esm_similarity": cos_sim, "lane": "esm2_embedding"}
