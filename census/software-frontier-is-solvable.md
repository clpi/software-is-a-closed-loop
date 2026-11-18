# Census — software-frontier-is-solvable

## Pin and identity

- Live head (gh API, read first): `c7ffc6d03e8bc4f795afcae983ee6bb3533a4e69`
- Clone head (shallow clone, depth 1): same — verified match.
- Visibility (gh API): private. Default branch: master (only branch). API description: none.
- Toolchain pin (lean-toolchain file): Lean 4, version 4.19.0.
- Files: README (43 lines), two Lean modules (below), a check script, a check log, a sums file. All sums verified against the clone in this census (all OK). Standalone companion to the hypergraph formalization in the sibling repo; it introduces no second graph or evidence store (README).

## Thesis, in plain English

Exact finite qualification frontiers are solvable: given candidate identities, graph-derived eligibility, and integer cost axes supplied by a caller, strict Pareto dominance and the nondominated frontier over the eligible candidates admit exact insertion and retraction update equations, an exact executable evaluator, a baseline no-worse guard whose frontier is nonempty while the baseline stays eligible, and a guaranteed frontier member in any nonempty finite candidate list under any strict partial order.

## Controls and zero-sorries evidence

- Check script: greps both modules and rejects any sorry / admit / axiom / native-decide token, compiles each with warnings as errors, fails on sorry-axiom / error / warning output.
- Check log: successful run on Lean 4.19.0, with a print-axioms line for **every** one of the 14 named theorems (source: the module's print-axioms statements, recorded in the log). No theorem depends on any custom axiom; dependencies are only the standard foundational ones noted per theorem, or none.
- README global claim: no custom axioms or admitted proofs are used.
- Concrete controls: 15 kernel-reduced examples in the test module (census below).

## Definitions carried (premises of the whole development)

- Candidate and axis types are generic. Costs are a supplied function to integers per axis; minimization-oriented.
- "No worse" (one token: `NoWorse`): one candidate is no worse than another when its cost is ≤ on **every** axis (all axes, not only selected ones, in the propositional definition).
- Strict dominance: no-worse on every axis **and** strictly less on at least one axis.
- Frontier membership: eligible, and no eligible candidate strictly dominates it — relative to a supplied eligibility predicate and a supplied dominance relation.
- Insertion eligibility: previously eligible or equal to the inserted identity. Retraction eligibility: eligible and not removed. Guarded eligibility: eligible and no-worse than the baseline on every axis.
- The executable evaluator: filter candidates by a Boolean eligibility, then keep those not Boolean-dominated by any live candidate. The finite-axis Boolean comparison checks all listed axes no-worse and any listed axis strict.

## Theorem census — 14 named theorems (module: Frontier; namespace token omitted)

Token column quotes at most one load-bearing word per theorem.

| Token | Hypotheses → conclusion | Axioms (check log) |
|---|---|---|
| `irrefl` (dominance irreflexive) | No hypotheses → no candidate strictly dominates itself. **Negation theorem.** | propext only |
| `trans` (dominance transitive) | x dominates y and y dominates z → x dominates z. | propext only |
| `ties` (not dominated) | Premise: x and y have equal cost on every axis → x does not strictly dominate y. **Negation theorem.** Equal vectors never dominate. | propext only |
| `insertion` (exact) | SIDE CONDITION / premise: the dominance relation is irreflexive → after inserting z, frontier membership is exactly: (old frontier member not dominated by z), or (the candidate is z and no old eligible candidate dominates z). Headline update equation. | none |
| `retraction` (exact) | No hypotheses beyond the definitions → after removing a set, a survivor is on the frontier exactly when it is eligible, not removed, and **every** former eligible dominator of it was removed. Multiple dominators are all accounted for. | standard three: propext, classical choice, quotient soundness |
| `surviving` | Premises: x was on the old frontier and x is not removed → x is on the frontier after retraction. | none |
| `live` (dominator blocks) | Premises: y is eligible, y is not removed, and y dominates x → x is **not** on the frontier after retraction. **Negation theorem** — a live dominator blocks resurrection. | none |
| `derived` (view extensional) | Premises: two eligibility predicates are pointwise iff and two dominance relations are pointwise iff → the frontiers they define coincide (iff). Storage/index layout is irrelevant given extensionally equal views. | none |
| `guarded` (no regression) | Premise: x is on the baseline-guarded frontier → x is no-worse than the baseline on every selected objective. The guard property itself, extracted. | none |
| `guarded` (global frontier) | Premise: x is on the baseline-guarded frontier → x is also on the unguarded frontier over all eligible candidates. Guarded members are globally nondominated. | propext only |
| `compute` (exact) | No hypotheses → membership in the executable evaluator's output holds exactly when the candidate is a frontier member under the propositional specification built from list membership, Boolean eligibility and Boolean dominance. Evaluator/spec bridge. | propext, quotient soundness |
| `pareto` (exact) | No hypotheses → the Boolean finite-axis comparison is true exactly when: cost ≤ on every listed axis and cost < on at least one listed axis. SIDE CONDITION: only the listed axes count; an empty axis list makes the strict part false, so nothing dominates. | propext, quotient soundness |
| `frontier` (exists) | PREMISES: the relation is irreflexive and transitive (a strict partial order), and the candidate list is nonempty → some list member is a frontier member (eligible = list membership). | standard three |
| `guarded` (frontier exists) | PREMISES: the baseline is in the candidate list and the baseline is eligible → some member of the list is on the baseline-guarded frontier (with eligibility = list membership plus the guard). The guarded frontier cannot be emptied while the baseline remains. | standard three |

## Test module — 15 kernel-reduced examples (controls, not named theorems)

Concrete costs over identities 0–4 and two axes, where 0 and 3 tie exactly, 1 trades one axis against the other, 2 is best on both, 4 is worst on both. The examples check by computation: empty input and all-ineligible input give empty frontiers; incomparable pair both retained; ties retained as separate identities, including duplicate occurrences in the output list; the all-dominating identity alone survives; a dominated identity is dropped; removing the dominator resurrects the previously dominated pair; removing one of two dominators does **not** resurrect the worst identity; eligibility restricted to a single identity yields just it; the guard examples below; empty-axis comparison keeps everyone.

### Explicit counterexamples — DISPROOFS flagged (README calls out exactly these two)

1. **Pareto membership does not imply no regression against a baseline.** Example: identity 1 is in the frontier of {0,1} yet its cost on the first axis is strictly worse than baseline identity 0's. Frontier membership alone is disproved as a no-regression guarantee — that is what the separate guard is for.
2. **Frontier-only storage loses information needed for exact retraction.** Example: populations {0,1,2} and {2} have the same current frontier, but after removing identity 2 their frontiers differ. Storing only the current frontier is disproved as sufficient state for exact future retraction; dominated candidates (or equivalent reconstructible source data) must be retained.

The three negation theorems in the census (irreflexivity, ties, live-dominator-blocks) are also flagged above as negation results, distinct from these two counterexamples to plausible claims.

## Premises carried rather than proven (consolidated)

1. Eligibility is **supplied** by the caller and is graph-derived in intended use; the graph-to-qualification adapter and authorized transfer certificates remain responsible for valid eligibility (README). This repo proves frontier calculations *from* the supplied views.
2. Cost axes are supplied: integer-valued, minimization-oriented, with consistent units, scope and orientation — the caller's responsibility (README).
3. The dominance relation in the update/existence theorems is supplied; insertion additionally assumes its irreflexivity, and existence assumes irreflexivity + transitivity. For the concrete Pareto relation those properties are proved (first two theorems), but the general theorems carry them as premises.
4. Candidate population is supplied and finite (a list); completeness of the candidate generator is not proved (README non-claim).
5. Identities: ties keep separate identities; list duplicates do not change membership but remain duplicate output entries — normalizing identities upstream is the caller's job when set cardinality is required (README).

## Side conditions stated

- Insertion equation requires an irreflexive dominance relation.
- Existence requires a nonempty list; guarded existence requires the baseline present in the list and eligible.
- Empty selected-axis list: every eligible candidate ties; no strict dominance (by the exactness theorem for the Boolean comparison).
- Deterministic input order yields deterministic output order; canonical serialization/sorting is not supplied.
- An observation append can change costs/eligibility arbitrarily; nothing here assumes an append improves cost or preserves eligibility, and retraction can resurrect previously dominated candidates (README interpretation).

## Explicit NON-CLAIMS / boundaries (README)

- The companion proves frontier calculations from supplied views, **not** physical runtime measurements, semantic lowering, or completeness of the candidate generator.
- A raw incidence matrix is not a proof of semantic equivalence.
- The executable evaluator is a deliberately full-scan reference oracle, **not** a claimed optimized incremental runtime; the update equations justify incremental membership updates, but no optimized runtime is provided or claimed.
- Work of the exact finite reference calculation is stated as order m²·a for m candidates and a axes. **No empirical performance claim, no universal speedup.**
- **No global optimum beyond the supplied candidate population**, and no automatic strict growth per witness follows from these theorems.
- No second graph or evidence store is introduced; qualification happens at a named snapshot of the authoritative graph (interpretation section).
