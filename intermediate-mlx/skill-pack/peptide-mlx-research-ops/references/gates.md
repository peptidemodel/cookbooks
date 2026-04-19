# Gates

## Environment Gate

Pass only if:

- one smoke-test run completes
- the output structure and metrics files exist
- weights and runner config are documented

## Reference Preview Gate

Pass only if:

- the panel contains at least one positive and one negative or counter-screen
- outputs are coherent enough to interpret
- preview mode is explicitly classified as useful or not useful

## Batch Gate

Pass only if:

- grouping strategy is defined
- resume state is defined
- failure and retry rules are written down

## Upgrade Gate

Pass only if:

- preview output is directionally useful
- the upgraded run would change a real decision
- manifest discipline is already in place
