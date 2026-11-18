# Census — software-testing-is-redundant

## Pin and identity

- Live head (gh API, read first): `66f65b6f44ac0249d11451cac089283aa1756240`
- Clone head (shallow clone, depth 1): same — verified match.
- Visibility (gh API): private. Default branch: master. API description: none.
- Created (gh API): 2026-11-18.
- Toolchain pin (the toolchain file): Lean 4, version 4.19.0. No external libraries.
- Files: a readme (124 lines), three Lean modules, a package file, a check script, a recorded check log, a recorded lake build log, a sums file, and an examples folder with its own runner, transcript, and one example module. All sums in the sums file verified against the clone in this census (all OK).
- Provenance printed in the readme: the qualification module is copied unchanged from an existing qualification proof family supplied during development; the redundancy module and the tests module are the new work.

## Thesis, in plain English

A hand-written test is redundant exactly when its complete scoped obligation is already supported by the qualification closure — no more and no less. For a suite T, a live support base B, and the certified inference rules R of the single behavior graph: T adds nothing to the closure exactly when every obligation in T is already derivable from B under R. Authorship is irrelevant; a generated suite and a manual suite stand or fall by the same criterion. The unrestricted slogan that every hand-written test is redundant is false, and this repo proves a finite counterexample to it alongside the exact theorem.

## Controls and zero-sorries evidence

- Gate evidence is the repo's recorded logs (this census ran no build). The recorded check log: Lean 4.19.0, axiom printouts for 18 theorems (nine from the qualification module, seven from the redundancy module, two from the tests module), ending in the pass line for all three modules and both rejection controls. The recorded lake log: the same printouts as build info lines, ending in a successful build.
- Axiom record in the logs: fifteen of the eighteen printed theorems depend on no axioms at all; three depend only on the standard pair (propositional extensionality and quotient soundness). No theorem depends on a custom axiom or an admitted proof.
- Check script design: it compiles every module with warnings as errors, scans the three modules for the admitted-proof word, the custom-axiom word, and the native-decision word, and runs two negative controls (an admitted proof and a type error), each of which must be rejected.
- This census's own scan of every Lean file in the clone, examples included: no admitted-proof token, no custom-axiom declaration, and no native-decision token anywhere.
- Examples have a separate runner and a recorded transcript (four theorems, one rejected mutation), outside the main gate's compile list — see the example census below.

## Definitions carried

- A support atom must include every distinction relevant to the claimed qualification, as appropriate: artifact and lineage, environment, input, effect, oracle, trust, polarity, experiment identity, and observation scope. The atom type itself is generic; what an atom must encode is a stated obligation on whoever supplies it.
- Derivation: an atom is derived when it is a live root, or when a certified rule (a finite premise list, read conjunctively) concludes it from derived premises. The closure of a base is this least derivation relation.
- A set is closed under the rules when every rule whose premises it holds has its conclusion in it. A model of a base and rules is a closed set containing the base — a model of this admitted Horn-style graph, not of arbitrary physical executions.
- A suite is covered when every one of its obligations is derivable. The join of two supports is their plain union.
- Withdrawal is modeled by filtering live roots and live rules; no historical fact is deleted, and derivations are re-evaluated at the named snapshot.
- The executable decision procedure in the tests module: over a supplied list of models, a test predicate is redundant when every listed model satisfying the evidence predicate also satisfies the test predicate. It is a Boolean list evaluator with a proved exact specification for the supplied catalogue.

## Theorem census — 22 named theorems in the main modules

Token column quotes at most one load-bearing word per theorem. Axioms are from the repo's recorded check log where the theorem is printed there; theorems not printed in the log are marked as such.

### The qualification module — 10 theorems (the closure foundation, copied unchanged)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `least` | Premises: a target set contains every root and is closed under the rules → every derivable atom is in the target set. The closure is the least closed set. | none |
| `closed` | No hypotheses → the derivation relation itself is closed under its rules. Not printed in the audit list. | not printed |
| `monotone` | Premises: every root of a first base is a root of a second, and every rule of a first rule set is a rule of a second → every derivation in the first system holds in the second. | none |
| `idempotent` | No hypotheses → deriving from the closure itself gives exactly the closure. | none |
| `compounding` | No hypotheses → deriving from the union of two bases is the same as deriving from the union of their closures. Compounding preserves every cross-input inference, not just the union of results. | none |
| `independent` (order) | Premises: two candidate saturation results each contain the roots, are closed, and contain nothing underivable → they agree on every atom. Any exhaustive sound saturation equals the same least closure. | none |
| `soundness` | Premises: every root is true at the target reading and the target reading is closed under the rules → every derivable atom is true at that reading. Semantic truth is conditional on validated roots and certificates. | none |
| `withdrawal` | No hypotheses → any derivation from the live roots and live rules after a withdrawal is also a derivation in the original system. Withdrawal adds no new support. | none |
| `surviving` | Premises: a subsystem's roots and rules all remain live after a withdrawal elsewhere → every derivation of the subsystem survives in the withdrawn system. | none |
| `bootstrap` (no) | Premise: every rule has at least one premise → from an empty base, nothing is derivable. Cycles alone cannot create support. **Negation theorem.** | none |

### The redundancy module — 10 theorems (the new exact theory)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `redundancy` (exact) | No hypotheses → a suite is covered exactly when adding it to the base leaves the closure unchanged, atom for atom. The headline necessary-and-sufficient criterion. | none |
| `contextual` | Premises: a suite is covered, and a second rule set extends the first with all previous certificates still valid → the suite stays redundant after any further evidence is appended and the rules so extended. Stability under future composition; deletions are not covered (see the tests). | none |
| `congruence` (compounding) | Premise: two bases have the same closure → joining either with arbitrary future evidence gives the same closure. Equal-closure bases are interchangeable, not merely in agreement on today's display. | none |
| `derivable` (all models) | No hypotheses → an atom is derivable exactly when it holds in every model (every closed set containing the base). Exact logical necessity, with no assumed solver completeness. | none |
| `countermodel` (missing obligation) | Premise: an atom is not derivable → there is a model of the base and rules in which the atom fails, namely the least closure itself. **Separation result.** | none |
| `duplicate` (single) | Premise: one atom is already derivable → adding just that atom as a suite changes no derivation. A repeated derived atom adds nothing. Not printed in the audit list. | not printed |
| `novel` (strict growth) | Premise: one atom is not derivable → adding it strictly expands what is derivable: the old derivations remain, the new atom becomes derivable, and it was not derivable before. **Separation result.** Not printed in the audit list. | not printed |
| `acceptance` | No hypotheses → adding a test predicate leaves the compatible-model acceptance set unchanged exactly when the existing evidence entails that predicate. Not printed in the audit list. | not printed |
| `preserved` (every derived view) | Premise: a suite is covered → any deterministic function of the closure (lawful, unlawful, conflict, and unknown colors, incidence and interaction views, and gates depending only on those atoms) takes the same value with or without the suite. | standard pair |
| `independence` (observational) | Premises: two models have identical observations and different test verdicts → no deterministic predictor using only those observations recovers the verdict for every model. A two-state example suffices. **Negation theorem.** | none |

### The tests module — 2 named theorems (the executable decision)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `correct` (executable decision) | No hypotheses → the Boolean catalogue evaluator returns true exactly when every listed model satisfying the evidence predicate satisfies the test predicate. Exact for the supplied catalogue. | standard pair |
| `exact` (exhaustive catalogue) | Premise: the supplied model list contains every model → the evaluator returns true exactly when every model satisfying the evidence predicate satisfies the test predicate. The global conclusion requires the completeness premise; it is carried, not proved. | standard pair |

### The tests module — 15 checked examples (controls, not named theorems)

Checked by computation or by the theorems above: a two-model decision, positive and negative; the empty catalogue being only vacuously sufficient for its empty scope; duplicate models adding no distinguishing power; a new manual assertion that distinguishes two models the current evidence permits — the finite counterexample to the blanket slogan (flagged below); the observation-independence pattern instantiated twice (a verdict from a bare value, and an effect from a return value alone: equal return values with different effects are not whole-behavior qualification); a duplicate receipt adding no atom while a fresh observation is not a duplicate merely because its result equals an earlier one; a conjunctive two-premise rule deriving its conclusion from both premises and provably not from one alone; opposite support polarity not covered by a positive derivation; two equal outcomes counting as two trials for a count threshold of two, where one does not; and withdrawal invalidating a prior derivation, so redundancy must be rechecked at the current snapshot.

### The example module — 4 theorems (separate runner, recorded transcript)

A capacity policy that accepts load up to 127 and rejects larger loads, under a separately assumed downward-closure shape for the admission decision.

| Token | Hypotheses → conclusion | Axioms (recorded transcript) |
|---|---|---|
| `determine` (two probes) | Premises: the admission decision is downward closed, and it agrees with the threshold policy at loads 127 and 128 → it agrees with the policy at every natural-number load. Two probes replace a 256-case suite, under the shape premise. | standard pair |
| `preserves` (suite) | No hypotheses → requiring agreement on all 256 loads accepts exactly the same decisions as requiring the shape plus agreement at the two probes. Follows from the acceptance theorem. | standard pair |
| `required` (both boundaries) | Premise: a suite is exact for the whole threshold family (it pins the cutoff to 127 against every rival cutoff) → the suite contains both 127 and 128. Each neighbor cutoff differs from the target at just one of the two points. | standard three |
| `matters` (shape) | No hypotheses → a decision with a non-monotone hole at load 40 agrees at both probes yet differs from the policy at 40. The shape premise cannot be dropped. **Counterexample control.** | none |

## Disproofs and refuted claims — flagged

1. **The blanket slogan is refuted.** The repo name read as an unrestricted claim — every hand-written test is redundant — is false, and the repo proves a finite counterexample: with trivial evidence over a two-value world, a manually specified assertion (the value is the top one) is not entailed, so that test is not redundant, with no appeal to undecidability or infinite behavior. The novel-witness theorem is the general form: a genuinely new atom strictly expands the closure.
2. **Return-only equivalence is refuted as whole-behavior qualification.** Two models with equal return values and different effects defeat every predictor of the effect from the return value alone (an instance of the observational independence theorem).
3. **One-premise derivation from a conjunctive rule is refuted.** With a rule requiring both premises, the conclusion is provably not derivable from either premise alone.
4. The three negation or separation results in the main census (no bootstrap, observational independence, missing-obligation countermodel, novel-witness strictness) are also flagged in their rows.

## Premises carried rather than proven (consolidated)

1. Atoms encode every relevant distinction. Independence, non-interference, and exact semantic and effect coverage are obligations of a supplied inference certificate, not conclusions inferred from equal hashes or equal return values.
2. Roots and rules are admitted and valid: semantic truth follows only under the soundness theorem's premises (valid roots, truth-preserving rules). The theorems are about the admitted graph as supplied.
3. The exhaustive-catalogue theorem carries its completeness premise: the supplied model list covers the intended model domain. Without it, the executable decision is exact only for the listed catalogue.
4. A fresh run, a latency sample, an instrumentation result, or a minimum independent sample count, where a gate requires one, is part of the obligation itself. Receipt counts do not prove independence or a population error rate.
5. The contextual stability theorem is about appends and rule extensions only. Withdrawals are explicitly outside it: redundancy must be re-evaluated at the named snapshot after any withdrawal.
6. The capacity example carries its shape premise: downward closure of the implementation's admission decision must be justified separately for the implementation and the venue.

## Non-claims carried

- Not permission to label every test passed, and no production tests have been deleted. A predicate being entailed is not the same event as running an executable in a target environment.
- No deployed test removal, no measured performance gain, no independent review, and no remote publication is claimed (readme claim status). The repo's name is a hypothesis clarified by the exact theorem, not an assertion of the disproved unrestricted slogan.
- The closure theorems are proposition-level proofs, not a claim of an implemented incremental production closure engine. The executable evaluator is linear in catalogue size plus evaluation costs and does not enumerate or solve an arbitrary source program.
- Derived-view preservation does not cover gates depending on omitted counts, timing, metadata, or cost.
- Testing sufficiency does not itself prove that deleting tests makes every metric better, nor that any harness or compiler is correct. Performance and no-regression claims need separately comparable measured costs.
- No second witness graph is introduced: relations and views are over the one qualification graph.
