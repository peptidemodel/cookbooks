#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict | list:
    with path.open() as f:
        return json.load(f)


def ensure_keys(obj: dict, keys: list[str], path: Path, problems: list[str]) -> None:
    for key in keys:
        if key not in obj:
            problems.append(f"{path.relative_to(ROOT)} missing key `{key}`")


def main() -> int:
    problems: list[str] = []

    target_spec_path = ROOT / "config" / "target_spec.json"
    hardware_path = ROOT / "config" / "hardware_profile.json"
    ref_complexes_path = ROOT / "config" / "reference_complexes.json"
    manifest_path = ROOT / "pipeline" / "manifests" / "example_manifest.json"
    state_path = ROOT / "pipeline" / "manifests" / "state.json"
    ref_panel_path = ROOT / "queries" / "reference_panel.json"
    cand_panel_path = ROOT / "queries" / "candidate_panel.json"

    target_spec = load_json(target_spec_path)
    hardware = load_json(hardware_path)
    ref_complexes = load_json(ref_complexes_path)
    manifest = load_json(manifest_path)
    state = load_json(state_path)
    ref_panel = load_json(ref_panel_path)
    cand_panel = load_json(cand_panel_path)

    ensure_keys(
        target_spec,
        [
            "project_name",
            "downstream_mode",
            "canonical_structure_format",
            "target_id",
            "target_display_name",
            "target_sequence_source",
            "default_chain_order",
            "state_file",
            "preview_mode",
            "upgrade_mode",
        ],
        target_spec_path,
        problems,
    )

    if target_spec.get("downstream_mode") not in {"local_only", "platform_writeback", "replace-me"}:
        problems.append(
            "config/target_spec.json `downstream_mode` must be one of "
            "`local_only`, `platform_writeback`, or placeholder `replace-me`"
        )
    if target_spec.get("canonical_structure_format") not in {"cif", "pdb", "replace-me"}:
        problems.append(
            "config/target_spec.json `canonical_structure_format` must be one of "
            "`cif`, `pdb`, or placeholder `replace-me`"
        )
    if target_spec.get("state_file") != "pipeline/manifests/state.json":
        problems.append(
            "config/target_spec.json `state_file` should default to `pipeline/manifests/state.json`"
        )

    ensure_keys(
        hardware,
        [
            "hardware",
            "memory_gb",
            "python_version",
            "mlx_version",
            "weights_path",
            "weights_hash",
            "runner_yaml",
            "entrypoint",
        ],
        hardware_path,
        problems,
    )

    if not isinstance(ref_complexes, list) or not ref_complexes:
        problems.append("config/reference_complexes.json must be a non-empty array")
    else:
        for idx, item in enumerate(ref_complexes):
            if not isinstance(item, dict):
                problems.append(
                    f"config/reference_complexes.json item {idx} must be an object"
                )
                continue
            ensure_keys(
                item,
                ["id", "target_id", "peptide_sequence", "role", "source", "notes"],
                ref_complexes_path,
                problems,
            )
            role = item.get("role")
            if role not in {"positive", "negative", "replace-me"}:
                problems.append(
                    f"config/reference_complexes.json item {idx} `role` must be `positive` or `negative`"
                )

    ensure_keys(
        manifest,
        [
            "manifest_version",
            "run_id",
            "phase",
            "mode",
            "authority_file",
            "predicted_at",
            "model",
            "model_version",
            "weights_hash",
            "hardware",
            "python_version",
            "mlx_version",
            "runner_yaml",
            "entrypoint",
            "random_seed",
            "num_diffusion_samples",
            "query_json",
            "output_dir",
            "downstream_mode",
            "canonical_structure_format",
        ],
        manifest_path,
        problems,
    )

    if manifest.get("downstream_mode") not in {"local_only", "platform_writeback", "replace-me"}:
        problems.append(
            "pipeline/manifests/example_manifest.json `downstream_mode` must be valid"
        )
    if manifest.get("canonical_structure_format") not in {"cif", "pdb", "replace-me"}:
        problems.append(
            "pipeline/manifests/example_manifest.json `canonical_structure_format` must be valid"
        )

    ensure_keys(
        state,
        ["phase", "batch_id", "completed", "failed", "next_action", "blocked_on"],
        state_path,
        problems,
    )

    for panel, path in [(ref_panel, ref_panel_path), (cand_panel, cand_panel_path)]:
        if not isinstance(panel, dict):
            problems.append(f"{path.relative_to(ROOT)} should be a JSON object")
            continue
        if "seeds" not in panel or "queries" not in panel:
            problems.append(f"{path.relative_to(ROOT)} must contain `seeds` and `queries`")
            continue
        queries = panel["queries"]
        if not isinstance(queries, dict) or not queries:
            problems.append(f"{path.relative_to(ROOT)} `queries` must be a non-empty object")
            continue
        for qname, qobj in queries.items():
            if not isinstance(qobj, dict) or "chains" not in qobj:
                problems.append(f"{path.relative_to(ROOT)} query `{qname}` must contain `chains`")
                continue
            chains = qobj["chains"]
            if not isinstance(chains, list) or len(chains) < 2:
                problems.append(f"{path.relative_to(ROOT)} query `{qname}` must have at least 2 chains")
                continue
            first_two = chains[:2]
            chain_ids = [c.get("chain_ids", [None])[0] for c in first_two]
            if chain_ids != ["A", "B"]:
                problems.append(
                    f"{path.relative_to(ROOT)} query `{qname}` should default to chain_ids `A` then `B`"
                )

    if manifest.get("downstream_mode") != target_spec.get("downstream_mode"):
        problems.append(
            "downstream_mode mismatch between config/target_spec.json and pipeline/manifests/example_manifest.json"
        )
    if manifest.get("canonical_structure_format") != target_spec.get("canonical_structure_format"):
        problems.append(
            "canonical_structure_format mismatch between config/target_spec.json and pipeline/manifests/example_manifest.json"
        )

    if problems:
        print("Schema validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
