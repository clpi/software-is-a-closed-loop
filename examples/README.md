# Closing a release-tuning loop under a latency cap

| Before | After |
|---|---|
| 8 calls for eight records | 2 calls at the stable admitted pin |

A batch may hold 1, 2, 4, or 8 records. At every pin, propose the next size, recheck the cap, and accept a strict call-count improvement. With cap 4, the pin sequence is 1 → 2 → 4 → 4.

## Why the bound holds

The finite proof covers every named cap and every feasible initial pin. Within three proposals the result passes requalification, is fixed by the next transition, and has minimum calls among all eligible candidates. Size 8 would cost only one call but violates this cap. A change to cap 2 also disqualifies the old winning pin.

The [family index](family.md) links to all 15 worked examples and their verification transcripts.

## Replay

Run from the repository root with Lean 4.19.0 available.

```sh
sh examples/check.sh
```

The runner checks the [proof](BatchTuning.lean) with warnings as errors and prints the computed result and theorem dependencies.

The [verification transcript](verification.txt) includes the observed outputs and the rejected counterexample mutation.

## Scope

The contract uses batch width as the latency bound and assumes exactly eight records and the four named divisors. It establishes no wall-clock result and does not authorize reuse across a changed contract.

## Additional worked example

[One verified range query across four read catalogs](range-ledger/README.md)
