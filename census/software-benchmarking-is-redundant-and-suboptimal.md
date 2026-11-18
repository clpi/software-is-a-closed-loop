# Census — software-benchmarking-is-redundant-and-suboptimal

## Pin and identity

- Live head (gh API, read first): `4314a181bc3d1fb35972031273c796aca10d15f5`
- Clone head (shallow clone, depth 1): same — verified match. (The head given in the commissioning brief differs from the live head at one digit position; the live API head and the clone head agree with each other, and this census is taken at the live head.)
- Visibility (gh API): private. Default branch: master. API description: none.
- Created (gh API): 2026-11-18.
- Toolchain pin (the toolchain file): Lean 4, version 4.19.0. No math library, per the readme.
- Files: a readme (87 lines), four Lean modules, a package file, a check script, a sums file, and an examples folder with its own runner, transcript, and one example module. There is no recorded check log and no recorded lake log for the main modules in this repo — see the controls section for what that means for gate evidence. All sums in the sums file verified against the clone in this census (all OK); the sums file covers the four modules, the package file, the readme, the check script, and the toolchain file — it does not cover the examples folder or its transcript.
- Provenance printed in the readme: the qualification module and the redundancy module are copied unchanged from the companion testing repo. This census verified that claim firsthand: both files are byte-identical to their counterparts in the testing repo at its pinned head (the file hashes in the two sums files also agree). The benchmark module and the tests module are the new work. The shared files are shared proof code over the one graph, not a separate graph.

## Thesis, in plain English

Benchmarking is redundant and less than optimal only conditionally, and this repo proves the exact conditions. A benchmark result is logically redundant exactly when every atom it contributes is already derivable from the named evidence snapshot under the admitted rules — adding it then leaves the whole derivation closure unchanged, which is stronger than leaving one display cell unchanged. A plan can replace another for every encoded purpose when its evidence derives all of the other's evidence; if it also costs no more on every declared axis and strictly less on at least one, the replaced plan is not Pareto optimal among admitted plans. In particular a fully covered, positive-cost plan is dominated by omission — provided omission itself is admissible, and provided every possible outcome of the experiment is covered, not just one already-known passing result. A blanket claim that physical measurement is unnecessary is not made and would not follow.

## Controls and zero-sorries evidence

- Gate evidence state: unlike its companion repos, this repo carries no recorded main-gate log. The check script's pass line exists only as the script's own final message; no recorded run of it stands in the repo. The gate's verdict at this pin is therefore unknown from recorded logs, and the readme's axiom statements below are labeled as readme claims, not as recorded-log evidence. What this census verified firsthand is the script's design, the source proofs, the sums, and the scan next. The examples folder does carry a recorded transcript (four theorems, one rejected mutation).
- Readme axiom claim (claimed in the readme, not in a recorded log): the new printed benchmark theorems use no axioms; one inherited extensional-view theorem uses the standard pair (propositional extensionality and quotient soundness); no theorem uses the admitted-proof axiom. The benchmark module prints axiom sets for five of its ten theorems at the end of the file, so a gate run would produce exactly those reports — but no such run is recorded in the repo.
- Check script design: it scans the four modules for the admitted-proof word, the custom-axiom word, and the native-decision word; compiles each module with warnings as errors and fails if any printed report names the admitted-proof axiom; runs two negative controls (an admitted proof and a type error), each of which must be rejected; and runs four scanner controls, one per forbidden token. It describes itself as a source guard, not a general security sandbox.
- This census's own scan of every Lean file in the clone, examples included: no admitted-proof token, no custom-axiom declaration, and no native-decision token anywhere.

## Definitions carried

- An atom must encode the distinctions the purpose cares about, as applicable: artifact, lineage, workload, venue, environment epoch, protocol, units, aggregation, polarity, sample identity, effects, and dependencies. Scope is part of the atom, not an inherited display label.
- The closure foundation is the companion's, carried unchanged: derivation from live roots under finite-premise conjunctive rules, the least closure, closed sets, withdrawal by filtering live roots and rules.
- Covered, in the companion's sense: every atom of a result set is derivable from the named snapshot. The join of two supports is their plain union.
- A receipt, a deliberately small executable illustration rather than a full schema: a context (five natural-number fields — artifact, workload, venue, epoch, protocol), a sample identity, a metric identity, and a value.
- A plan: a stated evidence set (the result it denotes — not a claim that execution will produce it) and a declared cost function from axes to natural numbers. A cost is a declared vector, not an inferred physical runtime.
- One plan covers another, relative to a snapshot and rules, when every evidence atom of the second is derivable from the snapshot joined with the first plan's evidence. One plan is no worse than another when its cost is no greater on every axis. Dominance is coverage plus no-worse plus strictly less cost on at least one axis.
- Pareto standing, relative to a snapshot, rules, and an admitted-plan predicate: a plan has it when it is admitted and no admitted plan dominates it.
- The omission plan: no evidence, zero cost on every axis. It describes pure omission only; it must not silently stand for an expensive reconstruction procedure.
- Purpose-relative redundancy: a result set is redundant for a stated purpose when, for every purpose atom, derivability with the result set joined holds exactly when derivability without it holds. This can be strictly weaker than total evidence redundancy.

## Theorem census — the benchmark module, 10 new theorems

Token column quotes at most one load-bearing word per theorem. The companion foundation (20 further named theorems in the two copied modules) is censused in full in the testing draft and is summarized after this table; it is not recounted as new work here. Axioms: no recorded log exists (see controls); the readme claim for the printed theorems is marked as a claim, and unprinted theorems are marked as such.

| Token | Hypotheses → conclusion | Axioms |
|---|---|---|
| `purpose` (coverage preserves) | Premises: one plan covers another relative to a snapshot and rules, and the second plan supports a stated purpose → the first plan supports the same purpose. Replacement for every encoded purpose. | readme claim: none (printed at file end; no recorded log) |
| `pareto` (dominated, not) | Premises: a plan is admitted, and it dominates another plan → the dominated plan does not have Pareto standing among the admitted plans. A genuine dominance statement, not merely absence from a frontier. **Negation theorem.** | not printed |
| `dominated` (covered, positive cost) | Premises: every evidence atom of a plan is already covered by the snapshot, and the plan has positive cost on at least one axis → the omission plan dominates it. Carries the admissibility side condition on omission, stated in the premises section, not in the theorem. | readme claim: none (printed at file end; no recorded log) |
| `redundant` (all outcomes) | Premise: for every possible outcome of an experiment, that outcome's result set is covered by the snapshot → for every outcome, joining that outcome's results to the snapshot changes no derivation. Prospective removal needs coverage of every outcome; one known passing result is not enough. | readme claim: none (printed at file end; no recorded log) |
| `redundant` (purpose, from covered) | Premise: a result set is fully covered by the snapshot → it is purpose-redundant for every purpose. Total redundancy is the stronger condition; the tests show the purpose form holding where total redundancy is not claimed. | not printed |
| `dominance` (additive context) | Premise: one plan dominates another → appending the same surrounding cost to both preserves dominance, strictness included. Proved only for stated additive accounting. | readme claim: none (printed at file end; no recorded log) |
| `sound` (derived result) | Premises: every root of the snapshot is true at a target reading, and that reading is closed under the rules → every result derived with a plan's evidence joined is true at that reading. Semantic validity is a separate premise, never inferred from an identical hash; this is the companion soundness theorem applied. | not printed |
| `iff` (no rules) | No hypotheses → with an empty rule set, an atom is derivable exactly when it is one of the roots themselves. No certificates means exactly the actual roots, not cross-context transfer. | not printed |
| `derived` (fresh sample, not) | Premise: an old receipt and a fresh receipt differ in sample identity → the fresh receipt is not derivable from the old one alone under an empty rule set. A new sample identity cannot be fabricated by replaying an old receipt. **Negation theorem.** | readme claim: none (printed at file end; no recorded log) |
| `derived` (stale context, not) | Premise: an old receipt and a fresh receipt differ in context → the fresh receipt is not derivable from the old one alone under an empty rule set. **Negation theorem.** | not printed |

### The tests module — 17 checked examples (controls, not named theorems)

Checked by computation or by the theorems above: a fresh sample, a stale epoch, a changed venue, and a changed protocol each not derivable from the original receipt, while the receipt itself is derivable; two distinct roots jointly satisfying a sample-count obligation where duplicating one root does not — evidence identity, explicitly not a statistical independence proof; a positive-cost repeated plan dominated by omission, and therefore without Pareto standing; a zero-cost plan redundant but **not** strictly dominated by omission (the strictness boundary); a coverage and cost tradeoff in which the broader, costlier plan is not no-worse than the narrower one, so greater output does not automatically dominate; two plans with equal functional output and unequal declared costs, standing for the rule that equal outputs do not imply equal runtime; a flaky experiment whose passing outcome is covered while its failing outcome is not, so the experiment is not prospectively redundant; the parallel-span counterexample (flagged below); a withdrawn origin leaving its old qualification underivable; and purpose-relative redundancy holding alongside a new unrelated receipt.

### The companion foundation carried unchanged — 20 named theorems (summary)

The qualification module (10 theorems: least closure, closure of the derivation relation itself, monotonicity, idempotence, compounding, order independence of saturation, soundness, withdrawal adding no support, surviving subsystems, and no bootstrap from cycles) and the redundancy module (10 theorems: the exact redundancy criterion, stability under future composition, compounding congruence, derivability exactly as truth in all closed-set models, a countermodel for every missing obligation, single-duplicate redundancy, strict growth from a novel witness, the acceptance criterion, preservation of every derived view, and observational independence). Full row-by-row census, with recorded-log axioms, stands in the testing draft at that repo's pin; the files here are byte-identical copies, verified in this census. Their evidence state at their home is proven, with recorded logs; in this repo they carry no recorded log of their own.

### The example module — 4 theorems (separate runner, recorded transcript)

A benchmark campaign over eight shards: seven immutable, independently scoped shard receipts are already certified and reusable; one shard (the fourth, index three) has changed and needs a fresh result. Cost is one unit per benchmark execution.

| Token | Hypotheses → conclusion | Axioms (recorded transcript) |
|---|---|---|
| `covers` (cheaper) | No hypotheses → the one-run plan (rerun only the changed shard) dominates the eight-run plan (rerun every shard): it covers every result the eight-run plan requires, at cost 1 against 8. | propositional extensionality only |
| `frontier` (old, off) | No hypotheses → the eight-run plan does not have Pareto standing among admitted plans, by the dominance theorem applied to the cheaper plan. **Negation theorem.** | propositional extensionality only |
| `required` (fresh) | No hypotheses → no single reported number computed from the seven unchanged results alone equals the correct total in both worlds where the changed shard's value is 10 (total 80) and where it is 25 (total 95). A zero-run reporter cannot distinguish the worlds. **Negation theorem.** | propositional extensionality only |
| `campaign` (minimum) | Premise: a plan covers every result the eight-run plan requires → its run list has at least one run. Any complete alternative needs the changed shard. | propositional extensionality only |

The transcript records the computed tuple (8 shards, the changed shard alone in the fresh list, totals 80 and 95) and a rejected control: rerunning a certified shard instead of the changed shard fails the check (exit 1).

## Disproofs and refuted claims — flagged

1. **Strict local savings composing under parallel span is refuted.** The tests carry the counterexample by computation: 1 is less than 2, yet the maximum of 1 and 10 equals the maximum of 2 and 10. A local saving can be absorbed by a parallel span; the additive-context theorem must not be applied to parallel makespan without another proof, and arbitrary venue-parallel speedups require a different certified cost law.
2. **Equal functional output implying equal cost is refuted as a reading.** Two plans return the same value with declared costs 100 and 10; no theorem here equates runtime from output identity, and the example stands as the control against that inference.
3. **One covered outcome making a flaky experiment redundant is refuted.** The passing outcome's results are covered and the failing outcome's are provably not, so prospective removal fails the all-outcomes condition.
4. **Zero-cost redundancy implying strict dominance is refuted.** A zero-cost covered plan is redundant, but omission does not strictly dominate it, because no axis is strictly cheaper.
5. The negation theorems in the main census (dominated plans lack Pareto standing; fresh samples and stale contexts are not derivable from an old receipt) and in the example census (the old campaign off the frontier; a fresh run required) are also flagged in their rows.

## Premises carried rather than proven (consolidated)

1. Atoms encode every distinction the purpose cares about (the list under Definitions). A new receipt identity is not proof of statistical independence, and content addressing establishes identity, not the truth or completeness of dependency metadata, policies, or certificates.
2. Omission admissibility: the covered-plan dominance theorem concludes that omission dominates; whether the omission plan is itself admissible — that checking stored certificates, retrieving evidence, and operational effects are charged or represented — is a separate obligation the readme states and the theorem does not discharge. Zero cost describes pure omission only.
3. Outcome completeness: prospective removal requires a catalogue of every possible outcome that covers the real experiment. This repo does not derive such completeness by fiat; the catalogue's fidelity is carried.
4. Cost standing: a cost relation may be established by an exact accounting model or by a separately scoped empirical comparison. Empirical claims must retain their uncertainty and sampling scope; no speedup or statistical confidence is claimed by these symbolic proofs.
5. Soundness premises: semantic truth requires valid roots and truth-preserving rules, per the soundness theorems. Withdrawn origins remove live derivations; history remains immutable, and qualifications are read at the named snapshot.
6. Additivity: the composition theorem speaks only where the stated accounting really is additive. Parallel span is the named case where it is not.

## Non-claims carried

- Not a blanket claim that physical measurement is unnecessary, and not a proof that all hand-authored benchmarks can be deleted. This is a proof project, not yet a benchmark runner, an empirical venue study, or a complete experiment optimizer.
- No speedup and no statistical confidence is claimed by the symbolic proofs. Equal functional outputs do not imply equal runtime.
- The check script is a source guard, not a general metaprogram security sandbox (its own description).
- Independent review is required before publication (readme).
- No recorded main-gate log stands in this repo: the gate's passing at this pin, and the readme's per-theorem axiom claims for the main modules, are not evidenced by a recorded run, and this census ran no build. The example transcript is the only recorded gate output in the repo, and the sums file does not cover it.

## Watch delta — 2026-11-18, the second hourly re-synthesis watch

The watch re-read the live head at the enumeration head a85286acc1f62c12992aa3a0ac8dee529b62927d and shallow-cloned it. Mechanical count at that head, by the watch's own method (every theorem or lemma declaration in every Lean file in the tree): 37 declarations (37 distinct short names) across 7 Lean files, no sorry token and no custom axiom declaration in any file, 17 example declarations. The same method at the last recorded head 4314a181bc3d1fb35972031273c796aca10d15f5 counted 34 declarations (34 distinct short names). Name comparison, one mechanical method both times: 3 names gained, 0 lost. The prose placements in this annex stand at the census pin 4314a181bc3d1fb35972031273c796aca10d15f5; a full re-census at the new head is owed and the owed mark in the ledger stands.
