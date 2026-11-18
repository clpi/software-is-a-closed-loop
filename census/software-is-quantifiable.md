# Theorem census — software-is-quantifiable

- Repository: clpi/software-is-quantifiable, read-only local clone.
- Pinned head verified by git read: 37917a4195efb1d0423a422ee954d767a9be1cd3 (matches the task pin; working tree clean at read time).
- Toolchain pin: the toolchain file contains exactly `leanprover/lean4:v4.15.0`; the task brief and the README both call this Lean 4.15.0. The README adds a build record dated 2026-11-17 on Lean 4.15.0, commit 11651562caae (that commit string is as printed in the README).
- Build definition: the package file declares package version 0.1.0 and one default-target Lean library rooted at the root module, which imports all five submodules. Lean core only, no Mathlib, per the README.
- Root module: the root file contains no theorems or definitions of its own; it only imports the five modules below.

## Global claims, sorries, and axiom audit evidence

### Does the README claim zero sorries?

Yes, explicitly, three times in substance:

1. The verdicts "stand on the recorded build run with zero sorries" (introduction).
2. "Zero sorries and zero added axioms in the sources (grep over the tree)" (build evidence).
3. Discipline section: "Zero sorries. Anything unproven would be listed in this table as OPEN …; at the recorded build, no claim is OPEN."

Independent grep during this census (over Lean sources and the README) found no occurrence of the sorry token in any Lean source, no added axiom declaration in any Lean source, and no axiom-audit command in any Lean source. The only occurrences are the README prose claims quoted above.

### Axiom dependencies — what the repo actually states

- There are **no per-theorem axiom statements in the Lean sources**: no axiom-audit commands appear in any module, and no theorem carries an individual axiom annotation.
- The **only** axiom audit evidence in the repo is the global README claim in the build-evidence section:
  - Axiom audit of the headline theorems (by printing their axioms): each depends only on Lean's standard axioms — propositional extensionality, classical choice, and quotient soundness — with no sorry axiom and no custom axiom anywhere.
  - One per-theorem exception is stated in the README: the coverage theorem in the Coverage module (entry C-1 below) depends on **no axioms at all**, because it is the projection of the named premise, which is passed as an argument.
- Therefore, for every theorem below except C-1, per-theorem axioms are recorded as: **not individually stated in the repo; covered only by the README's global headline-theorem audit claim above.**
- Note on scope of that claim: the README says the audit covered "the headline theorems" — it does not enumerate which theorems were audited, so it cannot be read as an audited list of all 46 theorems.
- Build-evidence caveat stated in the README itself: the recorded run did **not** run the normal lake build. Because the build machine's disk quota admitted only a partial toolchain (compiler and Init/Std/Lake libraries, without the Lean-library object files the Lake driver itself loads), every module was compiled directly with the Lean compiler — described in the README as the Lean equivalent of the lake build — including the root module; all six compilations are recorded with exit 0. The README asserts the same tree builds with the lake build unchanged on a complete toolchain.

### Exact claim list the README makes (claims table, claims 1–5 plus 4-prime)

1. **Claim 1 — Finiteness (spec sections 20.0 presentation lemma, 20.1).** A qualification — named software, named criteria, the behavior intended under them — forms a finite problem space. Lean form: the two Finiteness headline theorems (entries F-3, F-4). **Status: PROVEN.**
2. **Claim 2 — Fold correctness (spec sections 17.4, 17.8, 22.D).** The witness join is a semi-lattice, so the accounting fold is order- and duplication-independent and exactly recomputable. Lean form: the eight Fold theorems named in the table (the three join laws, the fold-characterization, the extensionality, permutation, duplication, and append theorems — entries D-1, D-2, D-3, D-7, D-8, D-9, D-10, D-11 below). **Status: PROVEN.**
3. **Claim 3 — Coloring (spec sections 5, 16.8, 20).** Relative to a named snapshot, the coloring computed as a least fixed point over ground Horn rules is sound and complete, and the iteration terminates. Lean form: the four Coloring headline theorems (entries L-12, L-14, L-18, L-19). **Status: PROVEN, under one stated side condition** — the snapshot's universe names every conclusion the rules can produce; the README glosses this as "that is what makes the snapshot a snapshot."
4. **Claim 4 — Pareto (spec sections 20.1, 20.2, 21.3).** The computed ordering is Pareto optimal, never worse than the incumbent, regression-free. Lean form: the five Pareto theorems named in the table (entries P-2, P-5, P-6, P-3, P-8). **Status: PROVEN at the level of bounds, which is the level the spec claims** (README's own qualifier).
5. **Claim 4-prime — Per-execution dominance.** A dominated schedule finishes worse on every single execution. Lean form: entry P-9. **Status: DISPROVEN** — concrete counterexample (bounds [1, 100] against [2, 3]; the dominated schedule can realize 1 against 3). The README notes the spec itself names this boundary at section 20.4: dominance is a statement about bounds, never about one execution.
6. **Claim 5 — Coverage universality (spec section 19).** Every execution crosses the kernel boundary, hence is witnessed. Lean form: entry C-1, conditional on the named platform premise (definition X-4). **Status: PREMISE — assumed, named, never counted as proven.** The README adds: the spec states this as a protection-model argument on three named assumptions (section 19.4) with an exact falsification condition (section 19.5, entry C-2); "the mathematics adds nothing here and this repository says so"; every coverage theorem takes the premise as an argument, so it cannot be smuggled in as a theorem.

README reading-guide claims (for completeness): finiteness falls out of the definitions with no finiteness hypothesis anywhere in the repository; the Fold accounting state is the characteristic function of the recorded witness set and the join is pointwise union; the Coloring module uses ground Horn rules over a finite fact universe, a counting argument over the universe for termination, and soundness/completeness against an inductive derivability relation; the Pareto module works with interval cost bounds on two axes, separation, the frontier, monotone refinement, and the regression gate; the Coverage module presents claim 5 as a premise with its falsification condition.

## Count summary

- **Theorems/lemmas: 46 in total** — Finiteness 4, Fold 12 (including 1 helper in the outer namespace), Coloring 19, Pareto 9, Coverage 2. The root module has 0.
- **Notable definitions/structures/inductives the theorems rest on: 25** — listed in the definitions section after the theorems.
- Disproofs: 1 (entry P-9). Named premises rather than proven claims: 1 premise structure with 3 named assumption fields (definition X-4), consumed by entries C-1 and C-2. Headline side condition: 1 (the Coloring universe condition, see entries L-10 through L-14, L-19).

---

# Theorems by module

Axiom line for every entry except C-1 reads, per the section above: "Not individually stated; README global headline audit only (standard axioms only, no sorry axiom, no custom axiom)." It is abbreviated below as [axioms: global claim only].

## Module: Finiteness (file: SoftwareIsQuantifiable/Finiteness.lean) — claim 1

### F-1. `mem_listsOfLen`
- Proves: characterization of the enumerated lists-of-a-given-length construction (definition N-3). For any alphabet list A, any length n, and any list l: l is a member of the enumerated collection of length-n lists over A if and only if the length of l is exactly n and every element of l is a member of A.
- Hypotheses/side conditions: none beyond the membership statement itself.
- [axioms: global claim only]

### F-2. `mem_alphabet`
- Proves: characterization of a qualification's run–venue alphabet (definition N-4). A pair belongs to the alphabet if and only if its first component is one of the qualification's named runs and its second component is one of its named venues.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-3. `schedules_finite` — HEADLINE, claim 1
- Proves: finiteness of the schedule space. For every qualification q there exists a finite list L of schedules such that every schedule s whose length equals the number of named runs in q, and every step of which pairs a named run with a named venue, is a member of L. The witness L is constructed explicitly: all lists of that fixed length over the qualification's run–venue alphabet.
- Hypotheses/side conditions: the conclusion covers only schedules of length equal to the run count whose steps draw from the presentation — that restriction is part of the statement, not an extra hypothesis on q. No finiteness hypothesis on q is assumed; runs and venues are lists by definition (definition N-1).
- [axioms: global claim only]

### F-4. `valid_orderings_finite` — HEADLINE, claim 1 (spec section 20.1)
- Proves: finiteness of the valid orderings. For every qualification q there exists a finite list L such that every schedule valid for q (definition N-5: one step per run, all steps drawn from the presentation, and every named run covered by some step with a named venue) is a member of L. Proved by reusing F-3's enumeration, since validity implies the length and step conditions of F-3.
- Hypotheses/side conditions: none beyond validity as defined.
- [axioms: global claim only]

## Module: Fold (file: SoftwareIsQuantifiable/Fold.lean) — claim 2

One helper theorem sits in the outer namespace, before the Fold namespace opens; the other eleven are inside the Fold namespace. Witness type W is arbitrary with decidable equality.

### D-0. `decide_false_of_not` (outer namespace, helper)
- Proves: if a decidable proposition does not hold, then deciding it yields false.
- Hypotheses/side conditions: the proposition must have a decidability instance.
- [axioms: global claim only]

### D-1. `join_assoc` — HEADLINE, claim 2
- Proves: the accounting join (definition N-7, pointwise boolean OR of characteristic functions) is associative: joining a with b first, then with c, equals joining a with the join of b and c, for all accounting states a, b, c.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-2. `join_comm` — HEADLINE, claim 2
- Proves: the join is commutative: the join of a and b equals the join of b and a.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-3. `join_idem` — HEADLINE, claim 2
- Proves: the join is idempotent: the join of a with itself equals a.
- Hypotheses/side conditions: none. Together D-1, D-2, D-3 are the semi-lattice laws for the join.
- [axioms: global claim only]

### D-4. `join_empty_left`
- Proves: the empty accounting (nothing recorded, definition N-8) is a left identity for the join: joining empty with a equals a.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-5. `join_empty_right`
- Proves: the empty accounting is a right identity for the join: joining a with empty equals a.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-6. `account_append`
- Proves: the accounting fold (definition N-10) splits over list append: the accounting of the concatenation of two witness lists equals the join of their separate accountings. This is the from-scratch-recompute-over-a-partition agreement.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-7. `account_eq_true_iff` — HEADLINE, claim 2
- Proves: the fold records exactly the presented set: for any witness list ws and any witness x, the accounting of ws marks x as recorded (true) if and only if x occurs in ws.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-8. `account_ext` — HEADLINE, claim 2 (order- and duplication-independence, general form)
- Proves: two witness lists that contain exactly the same witnesses (for every x, x is in the first list if and only if x is in the second) fold to the same accounting state. Hence the fold is a function of the witness set, not of the presenting list.
- Hypotheses/side conditions: the set-equality-of-membership hypothesis stated above.
- [axioms: global claim only]

### D-9. `account_perm` — HEADLINE, claim 2 (permutation-independence)
- Proves: if two witness lists are permutations of each other, they fold to the same accounting state. Proved as a corollary of D-8.
- Hypotheses/side conditions: the permutation hypothesis.
- [axioms: global claim only]

### D-10. `account_append_self` — HEADLINE, claim 2 (duplication-independence)
- Proves: for any witness list l, the accounting of l concatenated with itself equals the accounting of l: presenting every witness twice changes nothing.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### D-11. `account_cons_self`
- Proves: re-appending an already-recorded witness changes nothing: if w already occurs in l, then the accounting of w prepended to l equals the accounting of l.
- Hypotheses/side conditions: w must already occur in l.
- [axioms: global claim only]

## Module: Coloring (file: SoftwareIsQuantifiable/Coloring.lean) — claim 3

Setting for all entries: facts of an arbitrary type F with decidable equality; rules are ground Horn rules (definition N-11); a state is a boolean characteristic function over facts (definition N-12). **The module's side condition**, where it appears, is the hypothesis that for every rule in the rule list, the rule's conclusion is a member of the universe list U — i.e. the universe names every conclusion the rules can produce. It is flagged per entry below.

### L-1. `and_eq_true`
- Proves: boolean helper — if the conjunction of two booleans a and b is true, then a is true and b is true.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-2. `holds_eq_true`
- Proves: characterization of the premises-hold check (definition N-13): all premises in a list hold in a state if and only if every premise p in the list is marked true by the state.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-3. `any_eq_true`
- Proves: characterization of the boolean "any" over a list: it is true if and only if there exists an element of the list satisfying the boolean predicate.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-4. `le_step`
- Proves: one closure step (definition N-14) only adds facts: if a fact is true in a state, it remains true after one step under any rule list.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-5. `iter_eq_of_fixed`
- Proves: once a state is a fixed point of the closure step, iterating the step any number of times stays at that state.
- Hypotheses/side conditions: the state must be a fixed point of the step.
- [axioms: global claim only]

### L-6. `le_iter`
- Proves: facts are never lost along the iteration: if a fact is true in the starting state, it is true after any number of closure-step iterations.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-7. `count_le`
- Proves: the size of a state counted over a universe list (definition N-17) never exceeds the length of the universe list.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-8. `count_le_of_le`
- Proves: counting is monotone in the state: if every fact of the universe true in state p is also true in state q, then the count of p over the universe is at most the count of q.
- Hypotheses/side conditions: the pointwise implication over universe members stated above.
- [axioms: global claim only]

### L-9. `count_lt_of_le_add`
- Proves: counting strictly grows when a state grows somewhere in the universe: if p is pointwise contained in q over the universe and there is a universe member that is true in q but false in p, then the count of p is strictly less than the count of q.
- Hypotheses/side conditions: both the containment and the existence of a newly-true universe member.
- [axioms: global claim only]

### L-10. `exists_added`
- Proves: if one closure step changes a state, then it adds some fact of the universe: there is a member of U that is true after the step and false before.
- Hypotheses/side conditions: **the side condition applies** — every rule's conclusion must lie in U; and the step must actually change the state.
- [axioms: global claim only]

### L-11. `count_iter_ge`
- Proves: along a chain with no fixed point, the count over the universe grows by at least one per step: if for every i < k the i-th iterate is not a fixed point, then (count of the seed) + k is at most the count of the k-th iterate.
- Hypotheses/side conditions: **the side condition applies** (every rule conclusion in U), plus the no-fixed-point-before-k hypothesis.
- [axioms: global claim only]

### L-12. `exists_fixed_point` — HEADLINE, claim 3 (termination)
- Proves: **termination** — the closure iteration reaches a fixed point at some step k with k at most the length of the universe list U: there exists such a k where stepping the k-th iterate leaves it unchanged. (The README paraphrases this as "a fixed point is reached within U.length steps.")
- Hypotheses/side conditions: **the side condition applies** — for every rule in the rule list, the rule's conclusion is in U.
- [axioms: global claim only]

### L-13. `coloring_fixed`
- Proves: the coloring (definition N-18: the closure step iterated universe-length-plus-one times from the seed) is a fixed point of the closure step.
- Hypotheses/side conditions: **the side condition applies** (every rule conclusion in U).
- [axioms: global claim only]

### L-14. `step_sound`
- Proves: one closure step preserves derivability: if every fact true in a state s is derivable from the seed under the rules (in the inductive derivability relation, definition N-19), then every fact true after one step from s is also derivable.
- Hypotheses/side conditions: the derivability-of-s hypothesis. No universe condition.
- [axioms: global claim only]

### L-15. `iter_sound`
- Proves: every fact the iteration reaches is derivable: if every fact true in the starting state is derivable from the seed, then every fact true after any number of iterations is derivable.
- Hypotheses/side conditions: the derivability-of-the-starting-state hypothesis. No universe condition.
- [axioms: global claim only]

### L-16. `deriv_closed`
- Proves: every derivable fact holds in every state that contains the seed and is a fixed point of the closure step: if a fact is derivable from the seed, and a state s marks every seed-true fact true and is unchanged by the step, then s marks the derivable fact true.
- Hypotheses/side conditions: seed containment and the fixed-point property of s. No universe condition.
- [axioms: global claim only]

### L-17. `coloring_sound` — HEADLINE, claim 3 (soundness)
- Proves: **soundness of the coloring** — every fact marked true by the coloring is derivable from the seed under the snapshot's rules.
- Hypotheses/side conditions: **none — notably, the universe side condition is NOT required for soundness.**
- [axioms: global claim only]

### L-18. `coloring_complete` — HEADLINE, claim 3 (completeness)
- Proves: **completeness of the coloring** — every fact derivable from the seed under the rules is marked true by the coloring. Together with L-17, the coloring is exactly the derivable set (the least fixed point).
- Hypotheses/side conditions: **the side condition applies** — for every rule in the rule list, the rule's conclusion is in U. (Completeness, unlike soundness, needs it, via L-13.)
- [axioms: global claim only]

### L-19. `seed_le_coloring`
- Proves: the seed is contained in the coloring: every fact true in the seed is true in the coloring.
- Hypotheses/side conditions: none (no universe condition).
- [axioms: global claim only]

## Module: Pareto (file: SoftwareIsQuantifiable/Pareto.lean) — claim 4 and disproof 4-prime

Setting: costs are natural-number pairs on two axes (time, compute); a schedule's knowledge is an interval bound per axis (definition N-20, with a consistency proof field that the lower bound is at most the upper bound).

### P-1. `dominates_trans`
- Proves: point dominance (definition N-22: no worse on both axes, strictly better on at least one) is transitive: if point a dominates b and b dominates c, then a dominates c.
- Hypotheses/side conditions: the two dominance hypotheses.
- [axioms: global claim only]

### P-2. `separated_sound` — HEADLINE, claim 4
- Proves: **separation is sound.** If a candidate is separated from an incumbent (definition N-23: the candidate's upper bounds are at or below the incumbent's lower bounds on both axes, and strictly below on at least one axis), then for every realization of the candidate inside its bounds and every realization of the incumbent inside its bounds (definition N-24), the candidate's realized point is no worse on both axes and strictly better on at least one — i.e. the candidate dominates the incumbent under every realization consistent with the bounds.
- Hypotheses/side conditions: the separation hypothesis, and both points must actually realize their respective bounds. This is a statement **at the level of bounds**, per the README's claim-4 qualifier.
- [axioms: global claim only]

### P-3. `separated_of_refined` — HEADLINE, claim 4 (refinement is monotone)
- Proves: if a candidate–incumbent pair is separated, and all four interval bounds are refined (each new interval is contained in the old one: lower bound does not decrease, upper bound does not increase, for candidate time, candidate compute, incumbent time, incumbent compute), then the refined pair is still separated. A pair once proved dominated stays dominated as witnesses shrink intervals.
- Hypotheses/side conditions: the original separation plus the four interval-containment hypotheses.
- [axioms: global claim only]

### P-4. `exists_undominated_aux`
- Proves: auxiliary existence lemma — for any fuel bound n, any finite list of points L, and any point x in L whose cost sum is at most n, there is a point y in L such that y dominates x or y equals x, and no point of L dominates y.
- Hypotheses/side conditions: x must be in L and its axis sum must be at most n.
- [axioms: global claim only]

### P-5. `frontier_nonempty` — HEADLINE, claim 4
- Proves: **the frontier is nonempty** — every finite nonempty list of cost points has an undominated element: there is a point y in the list such that no point of the list dominates y.
- Hypotheses/side conditions: the list must be nonempty.
- [axioms: global claim only]

### P-6. `frontier_not_dominated` — HEADLINE, claim 4
- Proves: **no frontier output is dominated by a named incumbent from the same set** — if the output and the incumbent are both in the candidate list, and the output is a frontier element of that list (no list member dominates it), then the incumbent does not dominate the output. This is the regression-freedom content as formalized; the proof is direct application of the frontier property.
- Hypotheses/side conditions: both points in the list, and the output's frontier property as a hypothesis.
- [axioms: global claim only]

### P-7. `and_eq_true`
- Proves: boolean helper (a second, module-local copy of the same lemma as L-1) — if the conjunction of two booleans is true, both are true.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### P-8. `accepts_iff` — HEADLINE, claim 4 (the regression gate is exact)
- Proves: the regression gate (definition N-25: a decidable check that every previously qualified behavior still appears in the candidate's behavior list) accepts if and only if no previously qualified behavior is dropped: the check returns true exactly when every behavior in the qualified list is a member of the candidate list.
- Hypotheses/side conditions: behaviors of an arbitrary type with decidable equality. Both directions are proved.
- [axioms: global claim only]

### P-9. `not_per_execution_dominance` — **DISPROOF, claim 4-prime. FLAGGED: this is a disproof.**
- Proves: the **negation** of per-execution dominance. It is false that for all realized points x, y — where x's time lies in [1, 100] with compute 0, and y's time lies in [2, 3] with compute 0 — y's time is strictly less than x's time. The counterexample is concrete: x realizes time 1 and y realizes time 3, so the supposedly dominating schedule finishes worse on that execution. In the file's own framing: schedule X has witnessed time bounds [1, 100], schedule Y has [2, 3], compute equal; dominance in this design is a statement about bounds, never about a single execution. The README records this as DISPROVEN and notes the spec itself names this boundary at section 20.4.
- Hypotheses/side conditions: none — it is an unconditional negation, proved by exhibiting the two points (1, 0) and (3, 0).
- [axioms: global claim only]

## Module: Coverage (file: SoftwareIsQuantifiable/Coverage.lean) — claim 5, PREMISE

### C-1. `coverage` — **FLAGGED: premise-dependent, NOT a proven claim.**
- Proves: conditional coverage only — **given** a platform premise P (definition X-4) taken as an argument, every execution has a witness that records it. The proof is exactly the projection of the premise's mediation field; the file itself states "the proof is one line because there is nothing to prove: the entire content of the claim is the premise, and the premise is physical, not mathematical."
- Hypotheses/side conditions: **the entire conclusion rests on the assumed premise argument P.** No theorem in the repo derives coverage without it.
- Axioms: **individually stated in the README — depends on no axioms at all**, because it is the projection of the premise passed as an argument. This is the only per-theorem axiom statement in the repo.

### C-2. `coverage_iff`
- Proves: the falsification condition, stated exactly (spec section 19.5): the statement "every execution has a recording witness" holds if and only if it is not the case that there exists an execution that no witness records. Exhibiting one unwitnessed execution on a named platform falsifies the premise for that platform.
- Hypotheses/side conditions: the theorem takes a platform premise P as an argument, but the equivalence stated is a general logical equivalence about witnessed-ness and does not itself assert coverage; it characterizes what failure of coverage means. It does not prove coverage.
- [axioms: global claim only]

---

# Notable definitions the theorems rest on

## Finiteness definitions

### N-1. `Qualification` (structure)
- A qualification as a finite presentation: two fields, the named runs as a list and the named venues as a list, over arbitrary run and venue types. There is no other way to present them in this formalization — this definition is what makes finiteness hold by construction, with no finiteness hypothesis anywhere.

### N-2. `Schedule` (abbreviation)
- A schedule over a qualification: a list of run–venue pairs (a finite sequence of steps).

### N-3. `listsOfLen` (definition)
- The explicit enumeration of every list of exactly a given length over a given alphabet list, built recursively: length zero gives the singleton list containing the empty list; length n+1 prepends each alphabet element to each length-n list. This is the finite witness list used by F-3.

### N-4. `alphabet` (definition)
- A qualification's run–venue alphabet: every pair of a named run with a named venue, as a list.

### N-5. `Valid` (definition)
- A schedule is valid for a qualification when: its length equals the number of named runs; every step pairs a named run with a named venue; and every named run is covered — for each named run there is a named venue such that the pair occurs in the schedule.

## Fold definitions

### N-6. `Acct` (definition)
- An accounting state: a function from witness identities to booleans — the characteristic function of the recorded witness set. Content addressing is modeled by identity: two records with one identity are one witness. (Defined as a plain definition, not an abbreviation.)

### N-7. `join` (definition)
- The join of two accounting states: pointwise boolean OR — the union of the recorded sets. The semi-lattice operation of claim 2.

### N-8. `empty` (definition)
- The empty accounting: the constant-false state, nothing recorded.

### N-9. `single` (definition)
- The accounting of a single witness w: marks x recorded exactly when x equals w (by decidable equality).

### N-10. `account` (definition)
- The accounting of a list of witnesses, folded from scratch: the empty list gives the empty accounting; a head witness joined with the accounting of the tail.

## Coloring definitions

### N-11. `Rule` (structure)
- A ground Horn rule over facts: a list of premises and a single conclusion fact.

### N-12. `State` (abbreviation)
- A coloring state: a function from facts to booleans — which facts currently hold.

### N-13. `holds` (definition)
- Whether every premise in a list holds in a state: the boolean "all" of the state over the list.

### N-14. `step` (definition)
- One closure step: a fact holds after the step if it held before, or if some rule in the list has that fact as its conclusion and all of the rule's premises hold in the current state.

### N-15. `iter` (definition)
- Iteration of the closure step: the n-fold application of the step to a starting state.

### N-16. `contrib` (definition)
- One universe element's contribution to the count: 1 if the state marks it true, 0 if false.

### N-17. `count` (definition)
- The size of a state counted over a universe list: the sum of contributions over the list. The termination argument (L-11, L-12) is a counting argument over this function.

### N-18. `coloring` (definition)
- The coloring of a snapshot: the closure step iterated (length of the universe list) + 1 times from the seed — i.e. iterated past the termination bound of L-12.

### N-19. `Deriv` (inductive relation)
- Derivability from a seed under the rules: a fact is derivable if it is true in the seed, or if it is the conclusion of a rule in the list all of whose premises are derivable. This is the consequence relation the coloring is proved sound (L-17) and complete (L-18) against.

## Pareto definitions

### N-20. `Bounds` (structure)
- An interval bound on one cost axis: a natural-number lower bound, a natural-number upper bound, and a proof field that the lower bound is at most the upper bound.

### N-21. `Point` (abbreviation)
- A cost point: a pair of natural numbers — realized costs on the two axes (time, compute).

### N-22. `dominates` (definition)
- Point dominance: point a dominates point b when a is no worse on both axes and strictly better on at least one axis.

### N-23. `separated` (definition)
- Separation between a candidate and an incumbent, given as four bounds (candidate time, candidate compute, incumbent time, incumbent compute): the candidate's upper bounds are at or below the incumbent's lower bounds on both axes, and strictly below on at least one axis.

### N-24. `realizes` (definition)
- A point realizes a pair of bounds when its first coordinate lies within the time bounds (lower at most coordinate at most upper) and its second coordinate lies within the compute bounds.

### N-25. `accepts` (definition)
- The regression gate as a decidable check: given the previously qualified behavior list and a candidate behavior list (over a type with decidable equality), it returns true exactly when every qualified behavior is a member of the candidate list (boolean "all" with decidable membership).

## Coverage definitions

### X-1. `Execution` (structure)
- An execution of arbitrary software, in any language, on any platform: a single opaque identity field (a natural number). Everything else about an execution is, for this module, only whether it is witnessed.

### X-2. `Witness` (structure)
- A boundary witness: the identity of the execution it records, and a count of boundary events observed at the finest grain the platform affords (process lifecycle, syscall stream, per the doc comment).

### X-3. `Witnessed` (definition)
- A witness records an execution when the witness's execution identity equals the execution's identity.

### X-4. `PlatformPremise` (structure) — **FLAGGED: this is the named PREMISE, assumed, never proved.**
- The platform premise, named as spec section 19.4 names its assumptions. Three fields:
  1. The sensor sits strictly below the observed software in privilege — carried as a proposition field.
  2. The ledger is append-only from below: observed software can cause appends to the witness ledger, never edits or deletions — carried as a proposition field.
  3. Complete mediation: every execution is witnessed — carried as the field stating that for every execution there exists a witness recording it. **This third field is the entire content consumed by theorem C-1**; the first two fields are named in the structure but are not used by C-1's proof, which is the projection of the mediation field alone.
- The module header states the discipline explicitly: the premise appears as an explicitly named field of this structure, every coverage statement takes the premise as an argument, and no theorem in the repository derives coverage without it.

---

# Flags summary

- **DISPROOF: 1** — entry P-9 (Pareto module): per-execution dominance is false, by the concrete counterexample with time bounds [1, 100] versus [2, 3] (realizations 1 against 3, compute 0). README verdict for claim 4-prime: DISPROVEN.
- **PREMISE, not proven: 1** — claim 5 / Coverage module: definition X-4 packages three named assumptions (sensor below, append-only ledger, complete mediation); theorem C-1 merely projects the mediation field from a premise passed as an argument; theorem C-2 states the exact falsification condition (coverage holds if and only if no execution is unwitnessed). README verdict: PREMISE — assumed, named, never counted as proven.
- **SIDE CONDITION: 1 headline condition** — claim 3 / Coloring module: the universe list U must name every conclusion the rules can produce (for every rule in the list, its conclusion is in U). It is required by entries L-10, L-11, L-12, L-13, and L-18 (completeness). It is **not** required by soundness (L-17), by L-14, L-15, L-16, or by L-19. README verdict for claim 3: PROVEN under this one stated condition.
- **Other notable per-theorem conditions** (all stated in the entries): F-3's conclusion ranges only over schedules of run-count length with steps from the presentation; P-2 requires realizations inside the bounds and is a bounds-level statement; P-5 requires a nonempty point list; D-11 requires the witness to already occur in the list; L-5 requires a fixed point; L-16 requires seed containment plus a fixed point.
- **Axioms**: no per-theorem axiom data in the sources; README global headline audit claims standard axioms only (propositional extensionality, classical choice, quotient soundness), no sorry axiom, no custom axiom; sole per-theorem exception stated: C-1 depends on no axioms at all.
- **Sorries**: README claims zero sorries and zero added axioms (grep over the tree); this census's grep of the Lean sources agreed (no sorry token, no axiom declaration, no axiom-audit command in any Lean file).
