# Failure Atlas

This is the part most people skip, and then they waste days rerunning bad
batches.

## 1. Environment Looks Installed But Does Not Actually Predict

### Symptom

- commands import cleanly
- but the first real prediction crashes or never writes outputs

### What It Usually Means

- weights path is wrong
- runner YAML is mismatched
- environment proof never happened

### What To Do

1. run the smallest smoke test
2. verify output directory shape
3. record the exact command that worked

## 2. Sequence-Insensitive Preview Lane

### Symptom

- positives and negatives look too similar
- preview `ipTM` does not separate controls
- a scrambled or damaged peptide looks competitive

### What It Usually Means

- one-sample preview mode is not strong enough for ranking
- the lane may still be useful for existence proof or geometry review

### What To Do

1. preserve the negative result
2. reframe the lane as preview-only
3. escalate only shortlisted cases to upgrade mode

## 3. Query-Name or Cache Artifact

### Symptom

- identical or near-identical biological inputs behave differently for a reason
  that does not map cleanly to the biology

### What It Usually Means

- caching or upstream MSA behavior is coupled to query identity or retrieval
  details

### What To Do

1. keep query naming stable and unique
2. document naming conventions
3. avoid changing labels casually between reruns

## 4. OOM or Token Explosion

### Symptom

- large complexes crash
- long batches die on a subset of cards

### What It Usually Means

- complex size exceeded what the hardware can carry comfortably
- batch planning ignored hardware limits

### What To Do

1. log the failing case explicitly
2. reduce scope or sample count
3. separate oversized queries into their own lane

## 5. Non-Canonical Residues Silently Flattened

### Symptom

- sequence used in the run differs from the biologically described sequence
- later interpretation forgets that proxying happened

### What It Usually Means

- convenience conversion drifted into unmarked provenance loss

### What To Do

1. preserve the original source sequence
2. record the proxied sequence separately
3. attach a warning in the manifest

## 6. Long Backfill Without Resume State

### Symptom

- machine restarts or timeouts erase progress
- operator cannot tell what completed and what failed

### What It Usually Means

- orchestration was treated like a one-shot script instead of a resumable job

### What To Do

1. maintain `state.json` or equivalent
2. log completed and failed IDs
3. checkpoint by batch, not only at the end

## 7. Metric Overclaiming

### Symptom

- one scalar metric becomes the full story
- no manual review or adversarial checks occur

### What It Usually Means

- the workflow is drifting from structured research into leaderboard theater

### What To Do

1. restate what the metric can and cannot claim
2. compare against controls
3. add upgraded validation before promotion

## General Rule

If a failure changes the interpretation of the whole lane, stop and classify
the failure before launching more compute.
