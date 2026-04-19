"""
panel_utils.py — utilities for building, saving, and loading scored peptide panels.
"""

import csv
import json
from pathlib import Path
from typing import Dict, List, Optional


def make_reference_panel(
    positive_control: str,
    positive_control_label: str = "reference_positive",
    weak_positive: Optional[str] = None,
    weak_positive_label: str = "weak_positive",
    scrambled_control: Optional[str] = None,
    poly_ala_length: int = 10,
) -> List[Dict]:
    """
    Build a reference panel list for calibration.

    A reference panel should contain:
      1. A real positive control (literature peptide or well-characterised binder)
      2. A weaker or proxy positive (optional but strongly recommended)
      3. A scrambled version of the positive control
      4. A poly-Ala nonsense control

    The poly-Ala control is important: if it scores similarly to the real positive,
    your scoring lane cannot distinguish sequence information at all.
    """
    panel = []

    panel.append({
        "label": positive_control_label,
        "sequence": positive_control,
        "role": "positive_control",
        "description": "Real positive control — should score highest in a sane lane.",
    })

    if weak_positive:
        panel.append({
            "label": weak_positive_label,
            "sequence": weak_positive,
            "role": "positive_control",
            "description": "Weaker or proxy positive — should score below primary but above negatives.",
        })

    scrambled = scrambled_control or _scramble(positive_control)
    panel.append({
        "label": "scrambled_control",
        "sequence": scrambled,
        "role": "negative_control",
        "description": (
            "Same amino acid composition as the positive, but in sorted (alphabetical) order. "
            "Sorted rather than randomly shuffled so the control is deterministic and reproducible. "
            "A composition heuristic cannot distinguish this from the positive — that is expected "
            "and documented. The gate is reference vs poly-Ala, not reference vs scrambled."
        ),
    })

    poly_ala = "A" * min(poly_ala_length, len(positive_control))
    panel.append({
        "label": "poly_ala_control",
        "sequence": poly_ala,
        "role": "nonsense_control",
        "description": (
            "Poly-Alanine control. If this survives well in the lane, "
            "the lane is too permissive or the pocket hints are too broad."
        ),
    })

    return panel


def save_panel_results(results: List[Dict], path: Path) -> None:
    """Save scored panel results to CSV."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not results:
        return
    # Flatten sub_scores into top-level columns for CSV readability
    flat_results = []
    for r in results:
        flat = {k: v for k, v in r.items() if k != "sub_scores"}
        flat.update({f"sub_{k}": v for k, v in r.get("sub_scores", {}).items()})
        flat_results.append(flat)
    # Build fieldnames as union of all rows' keys (preserving order) to handle
    # rows with different sub_score keys without dropping columns.
    seen: set = set()
    fieldnames: List[str] = []
    for row in flat_results:
        for k in row.keys():
            if k not in seen:
                fieldnames.append(k)
                seen.add(k)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(flat_results)


def load_panel_results(path: Path) -> List[Dict]:
    """Load scored panel results from CSV."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Panel results not found at {path}")
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def save_panel_results_json(results: List[Dict], path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(results, indent=2))


def load_panel_results_json(path: Path) -> List[Dict]:
    return json.loads(Path(path).read_text())


def format_panel_table(results: List[Dict]) -> str:
    """Format scored panel as a simple text table."""
    header = f"{'Label':<25} {'Sequence':<22} {'Score':>7} {'Role':<20} {'Interp':<50}"
    sep = "-" * len(header)
    lines = [header, sep]
    for r in results:
        label = str(r.get("label", ""))[:24]
        seq = str(r.get("sequence", ""))[:21]
        score = f"{float(r.get('composite_score', 0)):.4f}"
        role = str(r.get("role", ""))[:19]
        interp = str(r.get("interpretation", ""))[:49]
        lines.append(f"{label:<25} {seq:<22} {score:>7} {role:<20} {interp:<50}")
    return "\n".join(lines)


def _scramble(seq: str) -> str:
    """Return sequence residues in sorted (alphabetical) order.
    Called 'scramble' by convention, but uses sort not random shuffle so
    the control peptide is deterministic across runs."""
    return "".join(sorted(seq))


def generate_single_mutant_variants(
    seed: str,
    positions: Optional[List[int]] = None,
    substitutions: Optional[str] = None,
    max_variants: int = 200,
) -> List[Dict]:
    """
    Generate all single amino-acid substitution variants of a seed peptide.

    positions: list of 0-based positions to scan (default: all)
    substitutions: string of amino acids to try at each position (default: common 15)
    max_variants: cap; positions are completed before stopping, so the actual
        count may exceed max_variants by up to (len(substitutions) - 1)

    Returns list of dicts with label, sequence, position, original_aa, new_aa.
    """
    if substitutions is None:
        substitutions = "ACDEFGHIKLMNPQRSTVWY"
    if positions is None:
        positions = list(range(len(seed)))

    variants = []
    for pos in positions:
        # Cap at position boundaries: finish scanning this position completely
        # before stopping, so the heatmap is never half-filled for a position.
        if len(variants) >= max_variants:
            break
        if pos < 0 or pos >= len(seed):
            continue
        original_aa = seed[pos]
        for new_aa in substitutions:
            if new_aa == original_aa:
                continue
            new_seq = seed[:pos] + new_aa + seed[pos + 1:]
            variants.append({
                "label": f"pos{pos+1}_{original_aa}{pos+1}{new_aa}",
                "sequence": new_seq,
                "role": "sar_variant",
                "position": pos,
                "position_1indexed": pos + 1,
                "original_aa": original_aa,
                "new_aa": new_aa,
                "description": f"Single substitution {original_aa}{pos+1}{new_aa}",
            })

    return variants
