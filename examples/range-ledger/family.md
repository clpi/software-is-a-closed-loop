# Exact range queries, corrections, and release decisions

One signed telemetry window connects fifteen worked examples. Read the scopes before comparing their counts. A bank-only solver, an overlap-receipt solver, and a compiler with direct prefix access can observe different things. Each derives the same sum from the information its venue supplies.

The [linked release proof](Settlement.lean) imports seven actual sibling modules. Its [offline source bundle](sources.json) records their repository, commit, path, Git blob, and SHA-256. Run `sh examples/range-ledger/check.sh` from the repository root to recheck the integration and replay the SQLite experiment. Each linked repository runs its own example and rejects its own mutation.

| Repository | Before | After |
|---|---|---|
| [software-benchmarking-is-redundant-and-suboptimal](https://github.com/clpi/software-benchmarking-is-redundant-and-suboptimal/tree/a85286acc1f62c12992aa3a0ac8dee529b62927d/examples/range-ledger) | 4,097 paired loads from 0 through 4,096 | 2 paired endpoint loads |
| [software-compilers-lose-info](https://github.com/clpi/software-compilers-lose-info/tree/69358971221d66e6304b64ff68a2e111d15231b3/examples/range-ledger) | 6 endpoint occurrences in the source expression | 2 essential direct endpoint values |
| [software-doesnt-have-to-regress](https://github.com/clpi/software-doesnt-have-to-regress/tree/858a85e383fbecc9826186aee2cc0101aea5ea62/examples/range-ledger) | 64 flushes per 4,096 bytes at width 64 | 16 flushes at the maximum safe width of 257 |
| [software-doesnt-need-review](https://github.com/clpi/software-doesnt-need-review/tree/1d504014be0c727b3f12e4d8e17f47dfceb118b6/examples/range-ledger) | Rescan nullable rows to distinguish NULL from zero | One signed sum and one presence bit per shard |
| [software-frontier-is-solvable](https://github.com/clpi/software-frontier-is-solvable/tree/319d41003c59fd18879ba4207ac64ea9636a17a8/examples/range-ledger) | 4,096 worst-case reads in the raw layout | 64 worst-case reads with 64 × 64 tiling |
| [software-fuzzing-is-suboptimal](https://github.com/clpi/software-fuzzing-is-suboptimal/tree/6ed7a59651ae9dab006b7903a98d3d598cca19ea/examples/range-ledger) | 2,145 legal intervals in a 64-sample window | 11 representatives |
| [software-is-a-closed-loop](README.md) | 4,096 raw source values per query | 4 bank sums, 3 overlap receipts, or 2 direct endpoint values |
| [software-is-composable](https://github.com/clpi/software-is-composable/tree/68fa8022f2dac42a123038b9de7ee8859c4fda84/examples/range-ledger) | 4,096 source values to reconstruct the window | 3 signed receipts yielding 160 |
| [software-is-incrementally-certifiable](https://github.com/clpi/software-is-incrementally-certifiable/tree/99ebf87e72fb1e1f2660d7177cc914e7b46bd0b2/examples/range-ledger) | 8 tile totals recomputed | 2 totals change; 6 can be reused |
| [software-is-incrementally-safe](https://github.com/clpi/software-is-incrementally-safe/tree/c4cdfde8f3378ee6a8af2863ff5ce872b81b533a/examples/range-ledger) | Reaggregate both affected groups from their rows | 2 group-total replacements |
| [software-is-more-traceable-than-you-think](https://github.com/clpi/software-is-more-traceable-than-you-think/tree/8f6a128069d0e68e97c4a69d78689c84350b0d2f/examples/range-ledger) | 6 pairwise bridge readings across 4 islands | 3 bridges in a spanning chain |
| [software-is-quantifiable](https://github.com/clpi/software-is-quantifiable/tree/74565dab80a735888c637d39690bdc0ebc5b5bba/examples/range-ledger) | 55 individual readings for [0,55) | 2 existing interval receipts; no new source run |
| [software-is-solvable](https://github.com/clpi/software-is-solvable/tree/3053b78d24bd81299e998bc253c755ab4a5e9b43/examples/range-ledger) | 4,096 source values | 3 retained scalar receipts |
| [software-optimality](https://github.com/clpi/software-optimality/tree/2bd3b419cab4ea222038c2ad766e0b1c0ee9d97f/examples/range-ledger) | 4,096 individual sample reads | 4 bank-total reads |
| [software-testing-is-redundant](https://github.com/clpi/software-testing-is-redundant/tree/18feb7ab60d542007124405fd8e1dc209c68361a/examples/range-ledger) | 8,390,656 nonempty windows | 4,096 singleton probes |

## Measured and proved

On the SQLite fixture, the three release totals were 12,263, 12,263, and 12,264. Two opposite edits changed two tile receipts while leaving the first full-window answer reusable. A subsequent net increase changed the answer. All four read catalogs matched SQL SUM at each epoch.

The independent window replay checked all 8,390,656 nonempty ranges. The test-basis theorem gives the 4,096-probe floor for arbitrary fixed interval probes under the additivity contract. The separate adaptive lower bound applies to the four-bank venue.

With a dedicated three-receipt index, building and serving a single fresh reader costs 4,102 logical reads and writes against 4,096 raw reads. Serving two fresh readers costs 4,105 against 8,192. This counts returned or written scalar rows. Storage-engine page accesses and elapsed time were unmeasured.

The [first example series](../family.md) covers fifteen additional engineering decisions.
