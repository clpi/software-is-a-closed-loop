# Census — software-fuzzing-is-suboptimal

## Pin and identity

- Live head (gh API, read first): `18d9569b581a3d2900b0613b33fc00e4b464ffa5`
- Clone head (shallow clone, depth 1): same — verified match.
- Visibility (gh API): private. Default branch: master. API description: none.
- Created (gh API): 2026-11-18.
- Toolchain pin (the toolchain file): Lean 4, version 4.19.0. Standard library only, per the readme; no project axioms.
- Files: a readme (35 lines), three Lean modules, a package file in table form, a check script, a separate negative-controls script, a recorded check log, a sums file, and an examples folder with its own runner, transcript, and one example module. All sums in the sums file verified against the clone in this census (all OK).

## Thesis, in plain English

Suboptimality of an evidence-generation plan is a conditional, checked comparison, never a universal claim that fuzzing is inferior. Within one fixed contract — semantics, venue, workload, and cost units all fixed — a plan is summarized by the goals it covers and its declared cost. One plan dominates another when it covers every goal the other covers at no greater cost, and strictly dominates when it also costs strictly less or covers an extra goal. Under that relation: dominance is transitive and preserves admissibility, replacement composes under additive cost and union coverage, a certified replay that adds no new goal is strictly dominated by its own omission when its cost is positive, and pointwise dominance over deterministic seed executions lifts to whole finite seed campaigns. An executable checker accepts exactly the submissions with matching contracts, full coverage, and strictly reduced declared cost. A finite countermodel shows why the unconditional version of the claim is false: with feedback, an adaptive plan can beat every fixed plan, and with the target already justified, the adaptive plan is itself strictly dominated.

## Controls and zero-sorries evidence

- Gate evidence is the repo's recorded log (this census ran no build). The recorded check log: Lean 4.19.0, axiom printouts for nine theorems, and a final pass line stating that a proof hole, a false derivation, and four forbidden-token controls against the actual gate were all rejected.
- Axiom record in the log: four of the nine printed theorems depend on no axioms at all; four depend only on propositional extensionality; one depends on the standard pair (propositional extensionality and quotient soundness). No theorem depends on a custom axiom or an admitted proof.
- Check script design: it pins the toolchain version by a version check, scans the three main modules for the admitted-proof word, the custom-axiom word, and the native-decision word, compiles each module with warnings as errors, and fails if any printed axiom report names the admitted-proof axiom.
- Negative-controls script (separate from the check script): it verifies that an admitted proof hole and a false derivation are each rejected by the compiler, and that the actual gate rejects each of the four forbidden tokens planted in the tests module. Its pass line is the last line of the recorded check log.
- This census's own scan of every Lean file in the clone, examples included: no admitted-proof token, no custom-axiom declaration, and no native-decision token anywhere. Note the gate's own token scan covers only the three main modules; the example module is covered by its own runner and by this census's scan, not by the main gate's scan.
- Examples have a separate runner and a recorded transcript (five theorems, one rejected mutation), outside the main gate's compile list — see the example census below.

## Definitions carried

- A plan summary, within one fixed contract: the set of goals covered (a goal-to-truth-value predicate over a generic goal type) and a declared cost, a natural number.
- Dominance: every goal covered by the second plan is covered by the first, and the first costs no more. Strict dominance adds: strictly lower cost, or an extra covered goal.
- The join of two summaries: union of coverage, sum of costs. This additive-cost, union-coverage algebra is the only composition the replacement theorems speak about.
- Admissibility: cost within a stated budget, and every required goal covered.
- A campaign: the join of the summaries of a deterministic run function over an explicit list of seeds. A seed list is an execution catalogue — a multiset of runs in which duplicates really incur cost — not a probability distribution.
- A comparison contract: four natural-number identity fields (semantics, venue, workload, units), compared by decidable equality. In production these identities must be authenticated commitments, not submitter guesses; that binding is an external obligation.
- A finite plan submission: a contract, a Boolean coverage table over a finite goal index type, and a declared cost. Its summary reads coverage as the entries marked true.

## Theorem census — 15 named theorems in the main modules

Token column quotes at most one load-bearing word per theorem. Axioms are from the repo's recorded check log where the theorem is printed there; theorems not printed in the log are marked as such.

### The fuzzing module — 8 theorems

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `trans` (dominance) | One summary dominates a second and the second dominates a third → the first dominates the third. Not printed in the audit list. | not printed |
| `admissibility` (preserved) | Premises: one summary dominates another, and the second is admissible under a budget and required goals → the first is admissible under the same budget and requirements. Not printed in the audit list. | not printed |
| `replacement` | Premise: one summary dominates another → joining each with the same context summary preserves dominance, under additive cost and union coverage. | not printed |
| `replacement` (strict cost) | Premises: one summary dominates another and costs strictly less → the joined summaries stand in strict dominance. Positive cost savings stay strict in any context; coverage-only strictness need not (see the tests). | none |
| `replay` (redundant) | Premises: every goal a replay covers is already covered by a retained summary, and the replay costs a positive amount → the retained summary strictly dominates the join of itself with the replay. Omission strictly dominates a certified no-new-goal replay. | none |
| `lift` (campaign) | Premise: at every seed, one run function dominates another pointwise → the campaign of the first over any seed list dominates the campaign of the second over the same list, repeated seeds and repeated costs included. | none |
| `seed` (duplicate) | Premise: one deterministic run summary has positive cost → the single run strictly dominates the join of the run with itself. Equal-cost equal-seed replay is redundant only under the determinism and no-fresh-sample conditions stated in the premises section. | not printed |
| `iff` (comparable) | No hypotheses → the Boolean contract comparison returns true exactly when the two contracts are equal. Not printed in the audit list. | not printed |

### The certificate module — 2 theorems, plus 5 checked examples

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `exact` (checker) | No hypotheses → the executable checker accepts a replacement exactly when the contracts match, the replacement dominates the baseline summary, and its declared cost is strictly lower. Equal costs are deliberately not accepted by this cost-strict checker, even if coverage improves. | propositional extensionality only |
| `strict` (certified) | Premise: the checker accepts a replacement against a baseline → the replacement summary strictly dominates the baseline summary. Accepted certificates connect to the mathematical relation. | propositional extensionality only |

The module's five checked examples fix a two-goal baseline at cost 3 and a cheaper twin at cost 2: the cheaper twin is accepted; the reverse direction, the baseline against itself, a coverage-dropping variant, and a contract-mismatched variant are each rejected by computation.

### The tests module — 5 named theorems, plus 13 checked examples

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `three` (saved) | No hypotheses → a cost-1 summary strictly dominates a cost-4 summary covering the same single goal. Proved directly. Not printed in the audit list. | not printed |
| `worlds` (adaptive, all) | No hypotheses → in the three-world oracle model (below), the two-query feedback policy finds the goal in every world. Proved by decision. | propositional extensionality only |
| `misses` (fixed two) | No hypotheses → every fixed two-query plan, including plans that use the probe, misses at least one world of the three. **DISPROOF of blanket fixed-over-adaptive superiority** — see the flagged section. Proved by a finite check over the three worlds. | propositional extensionality only |
| `dominates` (known target) | No hypotheses → in the same model, with the target already justified, a one-query targeted hit strictly dominates the two-query adaptive policy. The converse direction of the flagged pair: adaptivity itself can be the waste. | standard pair |
| `redundant` (fresh sample, not) | No hypotheses → a summary covering only sample zero does not dominate the join of itself with a summary covering a distinct sample one. A fresh independent sample is a distinct goal; deleting it is not a dominating replacement. **Negation theorem.** | none |

The 13 checked examples cover: admissibility of the cheap summary and non-admissibility of the expensive one under a budget of 1; an empty summary not dominating a covering one; a repeated single run strictly dominated by itself once, by the duplicate-seed theorem; a three-run repeated-seed campaign costing exactly 3, covering its goal and not another; contract comparison agreeing on identical contracts and disagreeing when any one of the four identity fields differs (four examples); and a coverage-only strict dominance at equal zero cost, standing as the witness that coverage strictness exists at plan level even though only cost strictness is promised to survive composition.

## The oracle model behind the flagged pair

Fully specified and finite: three worlds; two kinds of query, a probe and a targeted hit, each costing one. The probe reveals the world; a hit discovers the goal exactly when its target matches the world. The feedback policy probes first, then hits the revealed target, and succeeds in every world within two queries. Every fixed two-query plan — a pair of queries chosen without feedback, probe included among the choices — misses some world. Conversely, when the target is already justified, one targeted hit at cost 1 strictly dominates the two-query adaptive policy at cost 2. The oracle and the unit probe cost are explicit model assumptions, not assertions about arbitrary software.

## The example module — 5 named theorems, plus one private helper (separate runner, recorded transcript)

A frame format: a frame is a pair of nibbles in which the second must be the complement of the first; decoding a valid frame yields its command, one of sixteen.

| Token | Hypotheses → conclusion | Axioms (recorded transcript) |
|---|---|---|
| `invertible` | No hypotheses → a frame decodes to a given command exactly when the command is below sixteen and the frame is the encoding of that command. The encoder supplies the only valid second nibble for each first nibble, over every natural-number pair given to the decoder. | standard three |
| `campaign` (exact) | No hypotheses → the raw campaign (all 256 pairs over the two-nibble grid) and the directed campaign (16 frames, one per command) see exactly the commands 0 through 15 in order, and their lengths are 256 and 16. Proved by decision. | none |
| `certificate` (accepted) | No hypotheses → the executable checker accepts the directed campaign's plan against the raw campaign's plan: same contract, same coverage, strictly lower declared cost. | standard pair |
| `invocations` (minimum) | Premise: a campaign of frames sees every command below sixteen → it has at least 16 frames. Any covering campaign requires at least as many calls as the directed one. Proved through a private counting helper. | standard three |
| `boundary` (rejection) | No hypotheses → the raw campaign contains a rejected frame and the directed campaign contains none. If malformed-input rejection becomes a goal, the valid-only campaign omits it. **Boundary control.** | none |

The transcript records the computed triple (256 raw frames, 16 directed frames, the seen list 0 through 15) and a rejected control: using the wrong complement in the generator fails the check (exit 1).

## Disproofs and refuted claims — flagged

1. **Blanket fixed-over-adaptive superiority is disproved.** Every fixed two-query plan misses a world of the three-world oracle, while the feedback policy succeeds in all three within the same two-query budget. Together with the known-target theorem (the adaptive policy strictly dominated once the target is justified), this is the countermodel the readme names for why unconditional fuzzing inferiority is false: the repo's title claim holds only as the conditional, contract-bound comparison.
2. **Fresh-sample redundancy is refuted.** A distinct independent sample is a distinct goal; the duplicate-seed theorem does not extend to it, by the fresh-sample negation theorem.
3. **Coverage-only strictness surviving composition is refuted as a general promise.** The strict replacement theorem is proved only for cost strictness; the readme and the tests record that a coverage-only advantage can disappear when the surrounding context already covers the extra goal. Only the cost form is stated as a theorem.

## Premises carried rather than proven (consolidated)

1. One fixed contract: semantics, venue, workload, and cost units are fixed across any comparison, and contract identities must be bound to authoritative commitments by integration. The checker proves comparison of submitted summaries, not that the summaries faithfully describe execution.
2. Declared costs are natural numbers in a stated accounting. Actual execution time and measurement validity are not consequences of the natural-number cost arithmetic.
3. Composition is the stated algebra only: additive costs and union coverage. Other cost laws (parallel span, for instance) are outside the replacement theorems.
4. The duplicate-seed result carries its conditions in its statement and header: the summary itself is deterministic, and the qualification carries no fresh-sample or count requirement. Where such a requirement exists, a repeated run is a new goal, not a duplicate.
5. Goals may encode traces, input and output relations, intent obligations, or sample identities; the theorems do not manufacture those semantics from set membership.
6. The oracle model is a model: probe availability, unit query cost, and the three-world structure are assumptions of the fixture, not findings about arbitrary software.

## Non-claims carried

- No universal claim that fuzzing is inferior, and no claim of universal Pareto optimality. The exact gain is a checked strict comparison under a named qualification contract.
- No hit probability, confidence interval, independence, generalization, or expected-runtime conclusion is proved. A seed list is a catalogue, not a distribution; such claims need a separately specified distribution, oracle, and cost model.
- These are model theorems, not fabricated benchmark results, and not proofs that a particular deployed engine is faster.
- The standalone library creates no second authoritative graph and implements no Merkle-style authentication, lineage transfers, withdrawals, scheduler, or runtime instrumentation; findings can be recorded as derived views over an authoritative graph maintained elsewhere.
- The example makes no estimate of random-search runtime or fault-finding power; its baseline is exhaustive raw enumeration and its objective is distinct successful commands only.

## Watch delta — 2026-11-18, the second hourly re-synthesis watch

The watch re-read the live head at the enumeration head 6ed7a59651ae9dab006b7903a98d3d598cca19ea and shallow-cloned it. Mechanical count at that head, by the watch's own method (every theorem or lemma declaration in every Lean file in the tree): 27 declarations (27 distinct short names) across 5 Lean files, no sorry token and no custom axiom declaration in any file, 18 example declarations. The same method at the last recorded head 18d9569b581a3d2900b0613b33fc00e4b464ffa5 counted 21 declarations (21 distinct short names). Name comparison, one mechanical method both times: 6 names gained, 0 lost. The prose placements in this annex stand at the census pin 18d9569b581a3d2900b0613b33fc00e4b464ffa5; a full re-census at the new head is owed and the owed mark in the ledger stands.
