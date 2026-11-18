# One verified range query across four read catalogs

| Before | After |
|---|---|
| 4,096 raw source values per query | 4 bank sums, 3 overlap receipts, or 2 direct endpoint values |

The same signed total can be reconstructed under three different indexed access contracts. The linked proof instantiates the actual adaptive lower bound, overlap solver, interval composer, identifiability criterion, exact correction rule, compiler expression, and test-basis theorem from seven sibling modules.

## Derivation

A validated overlap chain computes the same value as the folded endpoint program. Reusing the total across epochs is exact iff the endpoint displacements match. Two canceling edits leave the total unchanged; a later +1 edit forces replacement. With equal cost for source reads, receipt writes, and indexed reads, building the three-receipt index breaks even in favor of the index at the second fresh query.

## Replay

From the repository root run `sh examples/check.sh` to check both example series. To run this case alone use `sh examples/range-ledger/check.sh`. The [Lean proof](Settlement.lean) and [verification transcript](verification.txt) record the positive result and a rejected semantic mutation. The runner also executes the [independent replay](replay.py).

## Scope

Counts are logical row reads/writes. Each comparison names the available catalog; a persisted final-answer cache would be a different contract. The amortization counts the overlap-only build. Filesystem pages, SQLite VM time, provenance validation, and elapsed time have different costs.

The [family index](family.md) links each engineering result to its published proof. The checker replays the seven imported source modules from byte-verified offline pins.
