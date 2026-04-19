# Pause State

Paused:

Reason:

Completed:

Failed:

Next action:

Blocked on:

Suggested `state.json` shape:

```json
{
  "phase": "phase3_batch_plan",
  "batch_id": "replace-me",
  "completed": {},
  "failed": {},
  "next_action": "replace-me",
  "blocked_on": null
}
```

Startup rule:

- choose the canonical `state.json` location before the first smoke run
- keep the chosen path consistent with `pipeline/README.md`
- prefer the committed template path `pipeline/manifests/state.json` unless the
  project has a strong reason to differ
