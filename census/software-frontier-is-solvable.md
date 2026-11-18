# Census — software-frontier-is-solvable — refresh draft

Census date: 2026-11-18, ~02:10–02:40 PST. Method: live head read first via the gh route, shallow clone (depth 1), clone head verified equal, every file read; checksums verified in the clone. Clone read only, never edited. This draft replaces the census of the older pin; changes are marked in the Delta section.

## Pin and identity

- Old census pin: `c7ffc6d03e8bc4f795afcae983ee6bb3533a4e69` — 14 named theorems, 15 examples, 2 disproofs.
- Live head (default branch `master`): `6a41c7be3c1b01492f96b75cbf0a28b11ab9faff`. Clone head matches exactly. Head commit subject, plainly: add a checked before-and-after example for replica placement.
- Visibility: private. Default branch: master.
- Toolchain pin: Lean 4.19.0.
- Files: the readme (unchanged length), the same two Lean modules, the check script, the recorded check log, the sums file — plus a new worked-examples folder. All sums in the sums file verified against the clone in this census (all OK). Theorem total in tree: **18** (14 library, unchanged; 4 in the new worked example). Examples: **15**, unchanged.

## Delta (old pin to this pin)

- **The library is unchanged.** Same frontier module with the same 14 named theorems (names and axiom sets re-verified against the recorded log, identical to the old census), same test module with the same 15 kernel-reduced examples, same two flagged disproof examples, same readme. Every carried-forward section below stands as written in the old census.
- **The only addition is a worked example.** A new examples folder carries one standalone proof file (4 theorems) applying the frontier results to replica placement, with its own readme, runner, recorded verification transcript, and a rejected control. Censused at the end.

## Thesis, in plain English — carried forward, still true

Exact finite qualification frontiers are solvable: given candidate identities, graph-derived eligibility, and integer cost axes supplied by a caller, strict dominance in the componentwise cost order and the nondominated frontier over the eligible candidates admit exact insertion and retraction update equations, an exact executable evaluator, a baseline no-worse guard whose frontier is nonempty while the baseline stays eligible, and a guaranteed frontier member in any nonempty finite candidate list under any strict partial order.

## Controls and zero-sorries evidence — carried forward, re-verified

- Check script: greps the root modules and rejects any sorry, admit, axiom, or native-decision token, compiles each with warnings as errors, and fails on sorry-axiom, error, or warning output. (Scope note: the script greps the root-level modules; the worked example has its own runner.)
- Check log: a successful run on Lean 4.19.0, with an axiom line for **every** one of the 14 named theorems. No theorem depends on any custom axiom; dependencies are only the standard foundational ones noted per theorem, or none. Re-read in this census; identical to the old census's record.
- Readme global claim: no custom axioms or admitted proofs are used.
- This census independently re-ran the token search over the whole tree, examples included: no escape-hatch tokens anywhere.
- Concrete controls: 15 kernel-reduced examples in the test module (census below).

## Definitions carried (premises of the whole development) — carried forward

- Candidate and axis types are generic. Costs are a supplied function to integers per axis; minimisation-oriented.
- No-worse: one candidate is no worse than another when its cost is at most the other's on **every** axis (all axes, not only selected ones, in the propositional definition).
- Strict dominance: no-worse on every axis **and** strictly less on at least one axis.
- Frontier membership: eligible, and no eligible candidate strictly dominates it — relative to a supplied eligibility predicate and a supplied dominance relation.
- Insertion eligibility: previously eligible or equal to the inserted identity. Retraction eligibility: eligible and not removed. Guarded eligibility: eligible and no-worse than the baseline on every axis.
- The executable evaluator: filter candidates by a boolean eligibility, then keep those not boolean-dominated by any live candidate. The finite-axis boolean comparison checks all listed axes no-worse and any listed axis strict.

## Theorem census — 14 named theorems (carried forward; names and axioms re-verified)

Token column quotes at most one load-bearing word per theorem.

| Token | Hypotheses to conclusion | Axioms (check log) |
|---|---|---|
| `irrefl` (dominance irreflexive) | No candidate strictly dominates itself. Negation theorem. | one standard axiom |
| `trans` (dominance transitive) | First dominates second and second dominates third, so first dominates third. | one standard axiom |
| `ties` (not dominated) | Premise: two candidates have equal cost on every axis — then neither strictly dominates the other. Negation theorem. Equal vectors never dominate. | one standard axiom |
| `insertion` (exact) | Side premise: the dominance relation is irreflexive. After inserting a candidate, frontier membership is exactly: an old frontier member not dominated by the inserted one, or the inserted candidate itself with no old eligible dominator. Headline update equation. | none |
| `retraction` (exact) | After removing a set, a survivor is on the frontier exactly when it is eligible, not removed, and **every** former eligible dominator of it was removed. Multiple dominators are all accounted for. | standard three |
| `surviving` | Premises: a candidate was on the old frontier and is not removed — then it is on the frontier after retraction. | none |
| `live` (dominator blocks) | Premises: a candidate is eligible, not removed, and dominates another — then the other is **not** on the frontier after retraction. Negation theorem: a live dominator blocks resurrection. | none |
| `derived` (view extensional) | Premises: two eligibility predicates are pointwise equivalent and two dominance relations are pointwise equivalent — then the frontiers they define coincide. Storage and index layout are irrelevant given extensionally equal views. | none |
| `guarded` (no regression) | Premise: a candidate is on the baseline-guarded frontier — then it is no-worse than the baseline on every selected objective. The guard property itself, extracted. | none |
| `guarded` (global frontier) | Premise: a candidate is on the baseline-guarded frontier — then it is also on the unguarded frontier over all eligible candidates. Guarded members are globally nondominated. | one standard axiom |
| `compute` (exact) | Membership in the executable evaluator's output holds exactly when the candidate is a frontier member under the propositional specification built from list membership, boolean eligibility, and boolean dominance. The evaluator-to-spec bridge. | two of the standard three |
| `pareto` (exact) | The boolean finite-axis comparison is true exactly when cost is at most on every listed axis and strictly less on at least one listed axis. Side condition: only the listed axes count; an empty axis list makes the strict part false, so nothing dominates. | two of the standard three |
| `frontier` (exists) | Premises: the relation is irreflexive and transitive (a strict partial order), and the candidate list is nonempty — then some list member is a frontier member (eligibility is list membership). | standard three |
| `guarded` (frontier exists) | Premises: the baseline is in the candidate list and the baseline is eligible — then some member of the list is on the baseline-guarded frontier. The guarded frontier cannot be emptied while the baseline remains. | standard three |

## Test module — 15 kernel-reduced examples (controls, not named theorems) — carried forward

Concrete costs over identities 0 to 4 and two axes, where two identities tie exactly, one trades one axis against the other, one is best on both, and one is worst on both. The examples check by computation: empty input and all-ineligible input give empty frontiers; an incomparable pair is both retained; ties are retained as separate identities, including duplicate occurrences in the output list; the all-dominating identity alone survives; a dominated identity is dropped; removing the dominator resurrects the previously dominated pair; removing one of two dominators does **not** resurrect the worst identity; eligibility restricted to a single identity yields just it; the guard examples below; and the empty-axis comparison keeps everyone.

### Explicit counterexamples — disproofs flagged (the readme calls out exactly these two) — carried forward

1. **Frontier membership does not imply no regression against a baseline.** Example: an identity is in the frontier of a two-candidate set yet its cost on the first axis is strictly worse than the baseline identity's. Frontier membership alone is disproved as a no-regression guarantee — that is what the separate guard is for.
2. **Frontier-only storage loses information needed for exact retraction.** Example: two populations with the same current frontier have different frontiers after removing the same identity. Storing only the current frontier is disproved as sufficient state for exact future retraction; dominated candidates (or equivalent reconstructible source data) must be retained.

The three negation theorems in the census (irreflexivity, ties, live-dominator-blocks) are also flagged above as negation results, distinct from these two counterexamples to plausible claims.

### Worked example: replica placement (4 theorems) — new at this pin

A standalone example in the examples folder. It enumerates placement layouts for replicas across hubs and proves: every layout's stated cost pair is as computed (one quoted name: `every_layout`); the frontier over all layouts is exactly the stated nondominated set, under the repo's own frontier machinery; the before-and-after computation (the full layout list against its frontier, and the frontier after a hub goes offline); and that keeping only the winners fails — the winners-only set does not determine the post-retraction frontier, an instance of the second disproof above. The example transcript records axiom sets for three of the four theorems (the layout computation fact is not printed): the frontier result uses two of the standard three, the other two printed theorems use none. A rejected control is recorded (retaining offline hub placements fails).

## Premises carried rather than proven (consolidated) — carried forward, still true

1. Eligibility is **supplied** by the caller and is graph-derived in intended use; the graph-to-qualification adapter and authorised transfer certificates remain responsible for valid eligibility (readme). This repo proves frontier calculations *from* the supplied views.
2. Cost axes are supplied: integer-valued, minimisation-oriented, with consistent units, scope, and orientation — the caller's responsibility (readme).
3. The dominance relation in the update and existence theorems is supplied; insertion additionally assumes its irreflexivity, and existence assumes irreflexivity plus transitivity. For the concrete componentwise relation those properties are proved (the first two theorems), but the general theorems carry them as premises.
4. The candidate population is supplied and finite (a list); completeness of the candidate generator is not proved (readme non-claim).
5. Identities: ties keep separate identities; list duplicates do not change membership but remain duplicate output entries — normalising identities upstream is the caller's job when set cardinality is required (readme).

## Side conditions stated — carried forward

- The insertion equation requires an irreflexive dominance relation.
- Existence requires a nonempty list; guarded existence requires the baseline present in the list and eligible.
- Empty selected-axis list: every eligible candidate ties; no strict dominance (by the exactness theorem for the boolean comparison).
- Deterministic input order yields deterministic output order; canonical serialisation and sorting are not supplied.
- An observation append can change costs and eligibility arbitrarily; nothing here assumes an append improves cost or preserves eligibility, and retraction can resurrect previously dominated candidates (readme interpretation).

## Explicit non-claims and boundaries (readme) — carried forward, still true

- The companion proves frontier calculations from supplied views, **not** physical runtime measurements, semantic lowering, or completeness of the candidate generator.
- A raw incidence matrix is not a proof of semantic equivalence.
- The executable evaluator is a deliberately full-scan reference oracle, **not** a claimed optimised incremental runtime; the update equations justify incremental membership updates, but no optimised runtime is provided or claimed.
- Work of the exact finite reference calculation is stated as order m-squared times a for m candidates and a axes. **No empirical performance claim, no universal speedup.**
- **No global optimum beyond the supplied candidate population**, and no automatic strict growth per witness follows from these theorems.
- No second graph or evidence store is introduced; qualification happens at a named snapshot of the authoritative graph (interpretation section).

## Watch delta — 2026-11-18, the second hourly re-synthesis watch

The watch re-read the live head at the enumeration head 22418d56604c96fdc1ba2875f3167e228b6ac6f3 and shallow-cloned it. Mechanical count at that head, by the watch's own method (every theorem or lemma declaration in every Lean file in the tree): 66 declarations (63 distinct short names) across 10 Lean files, no sorry token and no custom axiom declaration in any file, 15 example declarations. The same method at the last recorded head 6a41c7be3c1b01492f96b75cbf0a28b11ab9faff counted 18 declarations (18 distinct short names). Name comparison, one mechanical method both times: 45 names gained, 0 lost. The prose placements in this annex stand at the census pin 6a41c7be3c1b01492f96b75cbf0a28b11ab9faff; a full re-census at the new head is owed and the owed mark in the ledger stands.

Five new library files stand beside the range example, so the growth is library growth, not example growth alone. A full theorem-level census at the new pin is owed.
