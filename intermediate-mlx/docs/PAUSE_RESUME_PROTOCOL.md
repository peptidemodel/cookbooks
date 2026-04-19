# Pause / Resume Protocol

Long MLX runs should assume interruption.

## When To Pause

Pause when:

- the lane failed a control gate
- the machine cannot finish the planned batch safely
- a higher-priority platform job interrupts the research lane
- three consecutive failures suggest a systemic issue

## What To Save

At minimum, save:

- current phase
- batch identifier
- completed IDs
- failed IDs
- next resume action
- known blockers

## Suggested `state.json` Shape

```json
{
  "phase": "phase3_batch_plan",
  "batch_id": "2026-04-16-smoke",
  "completed": {},
  "failed": {},
  "next_action": "resume target-grouped batch on ACE",
  "blocked_on": null
}
```

## Required Pause Note

Every significant pause should also have a short markdown note stating:

- why the project paused
- what was completed
- what still needs verification
- where the authoritative files are

## Resume Checklist

1. read the latest pause note
2. read `state.json`
3. confirm the environment still matches the manifest assumptions
4. verify whether the previous failure was local or methodological
5. resume only from the documented next action or replace it explicitly
