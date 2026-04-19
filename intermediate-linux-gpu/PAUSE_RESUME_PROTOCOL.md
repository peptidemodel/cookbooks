# Pause / Resume Protocol

Research projects pause. That is normal.

The dangerous part is not the pause. It is losing the exact state of the project when priorities change.

## When To Pause

Pause a project when:

- priorities shift
- compute is being reassigned
- the current lane is blocked and the next move is not yet chosen
- another campaign becomes strategically higher value

## What Must Be Preserved Before Pausing

1. current git SHA
2. current phase
3. what is done
4. what was queued next
5. open scientific questions
6. authoritative output files
7. local-only artifacts that still matter

## Required Pause File

Create a `PAUSED.md` in the project root if the pause is more than trivial.

Minimum contents:

```md
# PAUSED

- pause date:
- git SHA:
- current phase:
- completed phases:
- next queued work:
- open scientific questions:
- authoritative files:
- important local-only artifacts:
- why the pause happened:
```

## What To Commit Before Pausing

Commit:

- finished phase reports
- machine-readable summaries
- scripts that were actually used
- negative-result documents
- any reframing docs that explain the current lane

Do not leave the only explanation in chat.

## What Can Stay Uncommitted

Possibly local-only:

- huge scratch pose directories
- downloaded archives that can be recreated
- temporary plots

But if a local artifact is scientifically important, mention it in `PAUSED.md`.

## Resume Checklist

On resume:

1. read `PAUSED.md`
2. read the latest phase report
3. inspect the latest JSON / TSV output
4. verify whether the working tree still contains important local artifacts
5. restate the lane classification before running new compute

## Rule

Do not resume by memory.

Resume by:

- phase report
- machine-readable output
- pause note

That is how you avoid repeating old mistakes or forgetting why a lane was demoted.
