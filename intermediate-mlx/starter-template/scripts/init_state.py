#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "pipeline" / "manifests" / "state.json"


def main() -> int:
    phase = sys.argv[1] if len(sys.argv) > 1 else "phase0_environment_check"
    batch_id = sys.argv[2] if len(sys.argv) > 2 else datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    state = {
        "phase": phase,
        "batch_id": batch_id,
        "completed": {},
        "failed": {},
        "next_action": "replace-me",
        "blocked_on": None,
    }
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")
    print(f"Initialized {STATE_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
