# Theorem census — software-is-quantifiable (refresh draft)

- Repository: clpi/software-is-quantifiable, read-only local clone (shallow, depth 1) under the sweep scratch clones directory.
- Pinned head verified by git read: f370992611d8c722e4897e67dbb8eaecf3d872ed (commit subject: "Add checked before-and-after example for ledger repair"). This is the head the clone actually carries; it matches the brief's short pin.
- Toolchain pin: the toolchain file contains exactly `leanprover/lean4:v4.19.0`. This is a change from the old census pin (see Delta).
- Build definition: the package file declares one default-target Lean library rooted at the root module, which imports all seven submodules. Lean core only, no Mathlib, per the README.
- Root module: the root file contains no theorems or definitions of its own; it only imports the seven modules below.
- This draft replaces the census taken at the old pin; entries carried forward from that census are marked "carried forward" and were re-verified present, by name, in the sources at the new head. New entries are marked "new at this head".

## Delta against the old census

- Old pin: 37917a4195efb1d0423a422ee954d767a9be1cd3. New pin: f370992611d8c722e4897e67dbb8eaecf3d872ed.
- Toolchain: Lean 4.15.0 at the old pin; Lean 4.19.0 at the new pin. The README keeps the earlier 4.15.0 verification notes and labels them as not the record for the current pin.
- Theorems: 46 at the old pin; 186 at the new pin (library modules only). An intermediate recorded run, preserved in the repo's coverage verification directory, audited 63 declared theorems at its base on Lean 4.15.0 — that is the relayed 63 count, and it is a record for that earlier base, not for this head.
- Modules: five at the old pin; seven at the new pin. Two modules are new: the shared interface module (54 theorems) and a synthetic instance module (21 theorems). Growth inside the old five: Finiteness 4 to 13, Fold 12 to 17, Coloring 19 to 36, Pareto 9 to 35, Coverage 2 to 10.
- Removals and replacements: one old theorem is gone in its old form. The old Pareto gate-exactness entry (old P-8, the plain behavior gate) is replaced by a split gate: a behavior half with its own exactness theorem, plus combined release and replacement gates with their own exactness and no-regression theorems (entries P-10, P-30, P-32, P-33 below). The old Coverage theorem C-1 is no longer a theorem at all: the name now denotes an abbreviation of the premise's mediation field (see Coverage section). Its falsification companion (old C-2) survives in a strengthened, roster-relative form (entry C-3 below).
- Disproofs and refusal results: 19 negative results in total (9 universal-claim disproofs plus counterexamples and concrete refusals; see flags summary). Old census: 1 disproof.
- Sorries: zero at the old pin; zero at the new pin (see scan below).
- Axiom posture: at the old pin there were no axiom-audit commands in any source. At the new pin the sources themselves carry axiom-audit commands in three modules (Coverage 8, Interface 19, Pareto 3), and the README names six theorems as depending on no axioms. The only recorded audit output in the repo is the intermediate run's, covering its 63 theorems at the earlier base.
- Gate state: the README records a full lake build with warnings as errors, exit 0, on Lean 4.19.0 for this branch (see gate section). The committed portable replayer record covers the earlier base only.
- The coverage premise still stands as a premise, in a restructured form (validator, ledger, and roster are now parameters; the sensor-below field is now a decidable rank comparison rather than an arbitrary proposition). The coloring side condition still stands exactly as stated (see flags summary).

## Global claims, sorries, and axiom audit evidence

### Does the README claim zero sorries?

Yes. The introduction states the verdicts "stand on the recorded build run with zero sorries" (the README prints the token in backticks). The build-evidence section states: zero sorries, zero admits, and zero added axioms. The discipline section repeats: zero sorries; anything unproven would be listed as OPEN; at the recorded build, no claim is OPEN.

Independent grep during this census (over every Lean file in the tree, library, examples, and verification controls) found no occurrence of the sorry token, no admit token used as a proof escape (the only matches are an ordinary English word inside a doc comment and names of the admission definitions in the Pareto module), no added axiom declaration, and no native-decision token. The only occurrences of the sorry word are the README prose claims.

### Axiom dependencies — what the repo actually states

- The README build evidence states: printing axioms on the headline theorems shows only the three standard axioms — propositional extensionality, classical choice, and quotient soundness — or no axioms.
- The README names six theorems as depending on no axioms at all: two Pareto composition theorems and the Pareto-to-interface bridge (tokens in the entries P-13, P-17, P-26 below), two interface theorems (entries I-26, I-30), and the Coverage vacuous-witness theorem (entry C-2).
- The sources carry axiom-audit commands at the ends of three modules: Coverage (8 commands), Interface (19 commands), Pareto (3 commands). Their outputs at this head are not recorded in the repo.
- The intermediate recorded run (coverage verification directory) audited all 63 declared theorems of its earlier base: exit 0, dependencies limited to the three standard axioms, with several theorems recorded as depending on no axioms (including, at that base, the coverage abbreviation and the coloring iteration lemmas). That record names its base and its Lean 4.15.0 toolchain; it does not cover this head.
- Therefore, for theorems at this head other than the six the README names as axiom-free, per-theorem axioms are recorded as: **not individually stated in the repo at this head; covered only by the README's headline-theorem audit claim above.** Abbreviated below as [axioms: global claim only].

### Gate state

- README build evidence: recorded on this branch with Lean 4.19.0 (release commit beginning 6caaee); the lake build with warnings-as-errors flag exited 0 and reported no warnings.
- The committed replayer record (coverage verification directory, record file with status "passed") covers the earlier base: clean build exit 0, upstream Pareto controls exit 0, the 63-theorem axiom audit exit 0, and four damaged-definition controls each rejected with exit 1 (fabricated recorded coverage, bypassed validator, omitted compute gate, omitted behavior gate). Its toolchain is Lean 4.15.0. It is evidence for that base, not for this head.
- The examples directory carries a check script that compiles the Coverage module and the ledger-repair example directly with the Lean compiler, warnings as errors. No recorded log for that script is committed.
- The Pareto repair note in the verification directory records the preceding Pareto correction: build passed, and independent review checked it plus eight executable guards and four proof controls under both Lean 4.15.0 and 4.19.0.

### Exact claim list the README makes (claims table, claims 1–13 with primed disproofs)

1. **Claim 1 — Finiteness.** As at the old pin. **Status: PROVEN.**
2. **Claim 2 — Fold correctness.** As at the old pin. **Status: PROVEN.**
3. **Claim 3 — Coloring.** Sound, complete, terminating, as at the old pin. **Status: PROVEN, under the one stated side condition** (the universe names every conclusion the rules can produce).
4. **Claim 4 — Pareto selection, separation, and no-regression admission.** Now includes the guarded (admitted) frontier existence and soundness theorems and the sequential/parallel separation theorems. **Status: PROVEN at the level of bounds and named scopes.** The README adds a new caution theorem: frontier membership alone permits an incomparable regression (entry P-27).
5. **Claim 4a — No qualified behavior lost (one half of admission).** The behavior gate compares the submission's offered behaviors against the prior qualification's qualified list; refusal theorems cover a submission that drops or empties that set. **Status: PROVEN.**
6. **Claim 4-prime — Per-execution dominance.** **Status: DISPROVEN**, as at the old pin (entry P-9).
7. **Claim 4-double-prime — Scalarization and Minkowski frontier equality.** The subset direction and "a positive-weight minimum is undominated" are **PROVEN**; both universal converses are **DISPROVEN** (entries P-17, P-24, P-25).
8. **Claim 5 — Coverage.** **Status: PREMISE — not a theorem.** The coverage name is an abbreviation of the premise's mediation field. The falsification conditions are stated on the roster (entries C-3, C-8).
9. **Claim 6 — Profile preorder and Pareto dominance on a measure space (the shared interface).** **Status: PROVEN on aligned profiles.**
10. **Claim 6-prime — Measure improvement alone dominates.** **Status: DISPROVEN** (entry I-31).
11. **Claim 7 — Products of measure spaces.** Both halves no-worse with one half strict yields dominance on the concatenation. **Status: PROVEN.**
12. **Claim 7-prime — The concatenation comparison splits into the halves.** **Status: DISPROVEN** (entries I-34, I-38).
13. **Claim 8 — Assemblies of per-symbol profiles compose, matched by symbol.** **Status: PROVEN** under duplicate-free symbol lists and full profile coverage, with refusal theorems for duplicate candidates, repeated profiles, and misaligned additions.
14. **Claim 8-prime — Index order is the profile preorder.** **Status: DISPROVEN** (entry I-44).
15. **Claim 9 — Exact finite enumerator; valid schedules close under side-respecting composition.** **Status: PROVEN.**
16. **Claim 9-prime — Every valid schedule of a product qualification is a side-respecting composite.** **Status: DISPROVEN** (entry F-12).
17. **Claim 10 — The witness fold composes across a sum of witness domains.** **Status: PROVEN** (entry D-16).
18. **Claim 11 — Coloring compounds; segregated domains factor.** **Status: PROVEN under the same snapshot condition as claim 3.**
19. **Claim 11-prime — Coloring distributes over join.** **Status: DISPROVEN** on the command-path rules, by the instance counterexample (entry S-10).
20. **Claim 12 — Separation is preserved by sequential sums and by parallel makespan.** **Status: PROVEN** (entries P-13, P-14).
21. **Claim 12-prime — Every Pareto point is a positive weighted-sum minimum.** **Status: DISPROVEN** (entry P-15); the true direction is entry P-17.
22. **Claim 12-double-prime — The Minkowski sum of frontiers is the frontier of the sum.** Subset direction **PROVEN** (entry P-24); equality **DISPROVEN** (entry P-25).
23. **Claim 12-triple-prime — The two-axis order is the interface order on time and compute.** **Status: PROVEN** (entry P-26).
24. **Claim 13 — The theorems apply to a two-component command path (synthetic).** **Status: PROVEN for the synthetic data in the instance module. Not measurements of a deployed system** (README's own qualifier).

## Count summary

- **Theorems/lemmas: 186 in total** in the library — Finiteness 13, Fold 17, Coloring 36, Pareto 35, Coverage 10, Interface 54, Instance 21. The root module has 0.
- Outside the library: the ledger-repair example file carries 3 theorems of its own; the Pareto controls file in the verification directory carries 0 theorems (executable guards and proof controls only).
- Disproofs and refusal results: 9 universal-claim disproofs, plus 10 further counterexample and concrete refusal results (19 negative results in total; see flags summary). Named premise: 1 premise structure, restructured (definition X-4 below), consumed by the coverage abbreviation. Headline side condition: 1 (the Coloring universe condition), unchanged.
- Definitions: the old census listed 25 notable definitions across the five old modules; those definitions all still stand, joined by the interface vocabulary (measure space, profile, alignment, the preorder and dominance relations, release assemblies, the frontier filter), the Pareto additions (bound addition and maximum, the weighted-sum function, the boolean dominance check, the exploratory frontier, the admitted filter, the two combined gates, the prior-qualification and submission structures), the Coverage additions (the recorded and missing checkers, the privilege-rank comparison), the Finiteness additions (the boolean validity check, the filtered valid-schedule list, the product qualification, the combined schedule, the composite list), the Coloring additions (the state order, the state join, the sum-domain embeddings), the Fold additions (the tagged-account embedding), and the instance module's synthetic data. A full definition-by-definition recount was not performed for this refresh; the theorem-level delta is exact.

---

# Theorems by module

Axiom line for every entry except the six README-named axiom-free theorems reads: [axioms: global claim only] (see the axiom section above).

## Module: Finiteness — claim 1 and claim 9

### F-1. `mem_listsOfLen` — carried forward
- Proves: characterization of the enumerated lists-of-a-given-length construction. Unchanged in substance.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-2. `mem_alphabet` — carried forward
- Proves: characterization of a qualification's run–venue alphabet. Unchanged.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-3. `schedules_finite` — HEADLINE, claim 1 — carried forward
- Proves: finiteness of the schedule space, by the explicit enumeration of all lists of run-count length over the run–venue alphabet. Unchanged.
- Hypotheses/side conditions: the conclusion ranges over schedules of run-count length with steps from the presentation; no finiteness hypothesis on the qualification.
- [axioms: global claim only]

### F-4. `valid_orderings_finite` — HEADLINE, claim 1 — carried forward
- Proves: finiteness of the valid orderings, by reuse of F-3. Unchanged.
- Hypotheses/side conditions: none beyond validity as defined.
- [axioms: global claim only]

### F-5. `length_flatMap_const` — new at this head
- Proves: a flat-map length lemma — if every image list of a function over a list has the same length n, the flattened length is the list length times n. Supporting lemma for F-6.
- Hypotheses/side conditions: the constant-image-length hypothesis.
- [axioms: global claim only]

### F-6. `listsOfLen_length` — new at this head, claim 9
- Proves: the enumeration is exactly counted: the number of lists of length n over an alphabet list A is the length of A raised to n.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-7. `schedules_card` — new at this head, claim 9
- Proves: the schedule enumeration for a qualification has exactly the alphabet size raised to the run count many members.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-8. `validB_iff` — new at this head, claim 9
- Proves: the boolean validity check is exact: it returns true if and only if the schedule is valid in the propositional sense.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-9. `mem_validSchedules` — new at this head, claim 9
- Proves: the filtered valid-schedule list contains exactly the valid schedules: membership if and only if valid.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-10. `validSchedules_length_le` — new at this head
- Proves: the valid-schedule count is at most the full schedule count of F-7.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### F-11. `combine_valid` — new at this head, claim 9
- Proves: closure under side-respecting composition — combining a valid schedule of one qualification with a valid schedule of another yields a valid schedule of the product qualification.
- Hypotheses/side conditions: validity of both component schedules.
- [axioms: global claim only]

### F-12. `not_all_valid_side_respecting` — **DISPROOF, claim 9-prime. New at this head.**
- Proves: the negation of the converse of F-11: there exists a schedule valid for a product qualification (over unit sum types) that is not a side-respecting composite — a run of one component may be wired to a venue of the other.
- Hypotheses/side conditions: none — an exhibited counterexample.
- [axioms: global claim only]

### F-13. `mem_composites` — new at this head, claim 9
- Proves: characterization of the composite list: a combined schedule is in the composites of two schedule lists if and only if it is the combination of a member of the first and a member of the second.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

## Module: Fold — claim 2 and claim 10

Entries D-0 through D-11 are carried forward unchanged from the old census (the outer-namespace helper, the three join laws, the two empty identities, the append split, the fold characterization, extensionality, permutation, duplication, and re-append results). All twelve were re-verified present by name.

### D-12. `account_map_inl` — new at this head
- Proves: accounting commutes with left tagging: the account of a left-tagged witness list, read at a left-tagged witness, equals the account of the original list at that witness.
- Hypotheses/side conditions: decidable equality on both witness types.
- [axioms: global claim only]

### D-13. `account_map_inl_inr` — new at this head
- Proves: a left-tagged list records no right-tagged witness: the account read at any right-tagged witness is false.
- Hypotheses/side conditions: decidable equality on both types.
- [axioms: global claim only]

### D-14. `account_map_inr` — new at this head
- Proves: the right-tagging mirror of D-12.
- Hypotheses/side conditions: decidable equality on both types.
- [axioms: global claim only]

### D-15. `account_map_inr_inl` — new at this head
- Proves: the right-tagging mirror of D-13.
- Hypotheses/side conditions: decidable equality on both types.
- [axioms: global claim only]

### D-16. `account_sum` — HEADLINE, claim 10 — new at this head
- Proves: the witness fold composes across a sum of witness domains: the account of a tagged concatenation (left list left-tagged, right list right-tagged) is exactly the side-by-side embedding of the two component accounts.
- Hypotheses/side conditions: decidable equality on both types.
- [axioms: global claim only]

## Module: Coloring — claim 3 and claim 11

Setting unchanged: ground Horn rules over a finite fact universe; the side condition, where it appears, is that every rule's conclusion lies in the universe list. Entries L-1 through L-19 are carried forward unchanged from the old census (helpers, step and iteration monotonicity of membership, the counting argument, termination, the fixed-point property, step and iteration soundness, derivability closure, soundness without the side condition, completeness with it, seed containment). All nineteen were re-verified present by name, with the side condition appearing in exactly the entries the old census flagged (L-10, L-11, L-12, L-13, L-18).

### L-20. `stateLe_refl` — new at this head
- Proves: the pointwise state order (one state below another when every true fact of the first is true in the second) is reflexive.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-21. `stateLe_trans` — new at this head
- Proves: the state order is transitive.
- Hypotheses/side conditions: the two order hypotheses.
- [axioms: global claim only]

### L-22. `stateLe_antisymm` — new at this head
- Proves: the state order is antisymmetric: mutual order gives equal states.
- Hypotheses/side conditions: the two order hypotheses.
- [axioms: global claim only]

### L-23. `step_mono` — new at this head
- Proves: one closure step is monotone in the state order.
- Hypotheses/side conditions: the order hypothesis on the two states.
- [axioms: global claim only]

### L-24. `iter_mono` — new at this head
- Proves: iteration of the closure step is monotone in the state order, at every step count.
- Hypotheses/side conditions: the order hypothesis.
- [axioms: global claim only]

### L-25. `coloring_mono_seed` — new at this head, claim 11
- Proves: the coloring is monotone in the seed: a larger seed colors to a larger coloring. Notably, no universe side condition is required.
- Hypotheses/side conditions: the seed order hypothesis only.
- [axioms: global claim only]

### L-26. `coloring_idem` — new at this head, claim 11
- Proves: coloring is idempotent: coloring the coloring of a seed gives the coloring of the seed.
- Hypotheses/side conditions: **the side condition applies** (every rule conclusion in the universe).
- [axioms: global claim only]

### L-27. `stateLe_join_left` — new at this head
- Proves: each state is below the pointwise join of the two states.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-28. `stateLe_join_right` — new at this head
- Proves: the right-hand mirror of L-27.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### L-29. `stateLe_join` — new at this head
- Proves: the state join is the least upper bound: any state above both joinands is above the join.
- Hypotheses/side conditions: the two order hypotheses.
- [axioms: global claim only]

### L-30. `coloring_compound` — HEADLINE, claim 11 — new at this head
- Proves: coloring compounds: the coloring of the join of two seeds equals the coloring of the join of their separate colorings.
- Hypotheses/side conditions: **the side condition applies** (every rule conclusion in the universe).
- [axioms: global claim only]

### L-31. `deriv_embed_left` — new at this head
- Proves: derivability embeds on the left of a sum fact domain: a fact derivable in the first system is derivable, left-tagged, in the combined system whose rules are the two embedded rule lists concatenated.
- Hypotheses/side conditions: the component derivation.
- [axioms: global claim only]

### L-32. `deriv_embed_right` — new at this head
- Proves: the right-hand mirror of L-31.
- Hypotheses/side conditions: the component derivation.
- [axioms: global claim only]

### L-33. `deriv_segregated` — new at this head
- Proves: derivability in the combined sum system segregates: a derivable tagged fact's untagged counterpart is derivable in its own component system (both directions of the tag stated conjunctively).
- Hypotheses/side conditions: the combined derivation.
- [axioms: global claim only]

### L-34. `embed_universe_closed` — new at this head
- Proves: the embedded universe is closed for the embedded rules: if each component universe names its rules' conclusions, the combined embedded universe names every embedded rule's conclusion. This is the side-condition transfer for the segregated colorings.
- Hypotheses/side conditions: both component side conditions.
- [axioms: global claim only]

### L-35. `coloring_segregated_left` — HEADLINE, claim 11 — new at this head
- Proves: on a sum of fact domains with no cross-rule, the combined coloring read at a left-tagged fact is that side's own coloring.
- Hypotheses/side conditions: **both component side conditions apply**; decidable equality on both fact types.
- [axioms: global claim only]

### L-36. `coloring_segregated_right` — HEADLINE, claim 11 — new at this head
- Proves: the right-hand mirror of L-35.
- Hypotheses/side conditions: **both component side conditions apply**; decidable equality on both fact types.
- [axioms: global claim only]

## Module: Pareto — claim 4, 4a, and the primed disproofs

Setting unchanged (two natural-number axes, interval bounds with a consistency proof field), extended with bound addition and maximum, a weighted-sum function, a boolean dominance check, an exploratory frontier filter, an incumbent-guarded admitted filter, and two combined gates over a prior qualification and a behavior submission. Entries P-1 through P-7 and P-9 are carried forward from the old census (dominance transitivity, separation soundness, monotone refinement, the auxiliary existence lemma, frontier nonemptiness, frontier non-domination, the boolean helper, and the per-execution disproof) and were re-verified present by name. Old entry P-8 (the plain gate exactness) is **removed**, replaced by P-10 and the combined gates P-30 to P-33.

### P-10. `noQualifiedBehaviorLost_iff` — HEADLINE, claim 4a — new at this head (replaces old P-8)
- Proves: the behavior half of admission is exact: the no-qualified-behavior-lost check returns true if and only if every behavior in the prior qualification's qualified list is a member of the submission's offered list.
- Hypotheses/side conditions: behaviors of an arbitrary type with decidable equality.
- [axioms: global claim only]

### P-11. `max_le_max` — new at this head
- Proves: maximum is monotone in both arguments.
- Hypotheses/side conditions: the two component inequalities.
- [axioms: global claim only]

### P-12. `max_lt_max` — new at this head
- Proves: maximum is strictly monotone when both arguments strictly grow.
- Hypotheses/side conditions: the two strict inequalities.
- [axioms: global claim only]

### P-13. `separated_sum` — HEADLINE, claim 12 — new at this head
- Proves: separation is preserved by sequential sums: if two candidate–incumbent pairs are separated, the pair of componentwise bound sums is separated.
- Hypotheses/side conditions: the two separation hypotheses.
- Axioms: **individually stated in the README — depends on no axioms at all.**

### P-14. `separated_parallel` — HEADLINE, claim 12 — new at this head
- Proves: separation is preserved by parallel composition: time bounds combine by maximum, compute bounds by sum, and the combined pair is separated.
- Hypotheses/side conditions: the two separation hypotheses.
- [axioms: global claim only]

### P-15. `not_scalarized` — **DISPROOF, claim 12-prime. New at this head.**
- Proves: the point (2, 2) is not a minimizer of any positive weighted sum against both (0, 3) and (3, 0): there are no positive weights under which its weighted sum is at most both rivals'.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### P-16. `weighted_strict` — new at this head
- Proves: weighted sums respect dominance: with positive weights, a point no worse on both axes and strictly better on one has a strictly smaller weighted sum.
- Hypotheses/side conditions: positive weights; the two no-worse inequalities and one strict.
- [axioms: global claim only]

### P-17. `scalar_optimum_undominated` — HEADLINE, claims 4-double-prime and 12-prime (the true direction) — new at this head
- Proves: a positive weighted-sum minimum over a list is undominated in that list: no list member dominates it.
- Hypotheses/side conditions: positive weights; membership; optimality against every list member.
- Axioms: **individually stated in the README — depends on no axioms at all.**

### P-18. `dominatesB_iff` — new at this head
- Proves: the boolean dominance check is exact against the propositional dominance relation.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### P-19. `frontier_exact` — new at this head
- Proves: the exploratory frontier filter is exact: a point is in the computed frontier of a list if and only if it is in the list and no list member dominates it.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### P-20. `frontier_antichain` — new at this head
- Proves: the computed frontier is an antichain: no frontier member dominates another.
- Hypotheses/side conditions: both memberships in the computed frontier.
- [axioms: global claim only]

### P-21. `scalar_frontier_point` — new at this head, claim 12-prime (witness)
- Proves: the point (2, 2) is on the frontier of the three-point list (0, 3), (2, 2), (3, 0) — the concrete undominated witness for the scalarization disproof P-15.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### P-22. `dominates_add_left` — new at this head
- Proves: dominance is preserved under adding a common point on the left summand: if one point dominates another, their sums with any fixed point preserve the dominance.
- Hypotheses/side conditions: the dominance hypothesis.
- [axioms: global claim only]

### P-23. `dominates_add_right` — new at this head
- Proves: the right-summand mirror of P-22.
- Hypotheses/side conditions: the dominance hypothesis.
- [axioms: global claim only]

### P-24. `minkowski_frontier_subset` — HEADLINE, claim 12-double-prime (the direction that holds) — new at this head
- Proves: an undominated sum point has undominated summands: if a sum of a point from one list and a point from another is dominated by no member of the Minkowski sum list, then neither summand is dominated within its own list.
- Hypotheses/side conditions: both summand memberships and the undominated hypothesis over the sum list.
- [axioms: global claim only]

### P-25. `not_frontier_minkowski` — **DISPROOF, claim 12-double-prime. New at this head.**
- Proves: the Minkowski frontier equality fails: (0, 3) is undominated in its list and (3, 0) is undominated in its list, yet their sum (3, 3) is dominated by a member of the sum list (the (2, 2) sum).
- Hypotheses/side conditions: none — concrete lists.
- [axioms: global claim only]

### P-26. `dominates_iff_interface` — HEADLINE, claim 12-triple-prime — new at this head
- Proves: the bridge: two-axis Pareto dominance of two points holds if and only if the interface dominance relation holds of their profiles on the time-and-compute space, observed behavior held.
- Hypotheses/side conditions: none.
- Axioms: **individually stated in the README — depends on no axioms at all.**

### P-27. `frontier_can_regress` — **COUNTEREXAMPLE, claim 4 caution. New at this head.**
- Proves: frontier membership alone permits an incomparable regression: there is a concrete incumbent and candidate list whose frontier output is no worse in the dominance sense yet worse on an axis the incumbent held — the reason claim 4 is stated with the guarded frontier, not the exploratory one.
- Hypotheses/side conditions: none — concrete points.
- [axioms: global claim only]

### P-28. `admitted_noWorse` — new at this head, claim 4
- Proves: every member of the incumbent-guarded admitted filter is no worse than the incumbent on both axes (point-level no-worse).
- Hypotheses/side conditions: membership in the admitted filter.
- [axioms: global claim only]

### P-29. `admitted_frontier_exists` — HEADLINE, claim 4 — new at this head
- Proves: the guarded frontier is nonempty whenever the incumbent is among the candidates: there is an admitted output no worse than the incumbent and dominated by no admitted candidate.
- Hypotheses/side conditions: the incumbent must be a member of the candidate list.
- [axioms: global claim only]

### P-30. `admitted_frontier_sound` — HEADLINE, claim 4 — new at this head
- Proves: a guarded-frontier output is no worse than the incumbent and is dominated by no candidate at all (not merely no admitted candidate).
- Hypotheses/side conditions: admitted membership and the frontier property over the admitted list.
- [axioms: global claim only]

### P-31. `acceptsRelease_iff` — new at this head, claims 4 and 4a
- Proves: the combined release gate is exact: it accepts if and only if the contexts match, no qualified behavior is lost (P-10), and the output is no worse than the incumbent — the gate's full conjunction, both directions.
- Hypotheses/side conditions: decidable equality on behaviors and on contexts.
- [axioms: global claim only]

### P-32. `weaklySeparated_sound` — new at this head
- Proves: weak separation (upper bounds at or below lower bounds on both axes, no strict axis required) is sound at the no-worse level: every realization of the candidate is no worse than every realization of the incumbent.
- Hypotheses/side conditions: the weak separation hypothesis and both realizations inside their bounds.
- [axioms: global claim only]

### P-33. `acceptsReplacement_iff` — new at this head
- Proves: the interval replacement gate is exact: it accepts if and only if the contexts match, no qualified behavior is lost, and the candidate and incumbent bounds are weakly separated.
- Hypotheses/side conditions: decidable equality on behaviors and contexts.
- [axioms: global claim only]

### P-34. `replacement_no_regression` — HEADLINE, claim 4 — new at this head
- Proves: an accepted replacement does not regress: if the replacement gate accepts, then for every realization of the candidate bounds and every realization of the incumbent bounds, the candidate's realized point is no worse than the incumbent's. The README's scope note applies: this all-realizations statement is conditional on the supplied bounds.
- Hypotheses/side conditions: gate acceptance (which includes context match, behavior retention, and weak separation).
- [axioms: global claim only]

### P-35. `omitted_qualified_behavior_refused` — new at this head, claim 4a (control)
- Proves: a concrete refusal — a submission omitting a qualified behavior makes the behavior check false.
- Hypotheses/side conditions: none — concrete lists.
- [axioms: global claim only]

### P-36. `empty_submission_refused_when_qualified` — new at this head, claim 4a (control)
- Proves: a concrete refusal — an empty submission against a nonempty prior qualification makes the behavior check false.
- Hypotheses/side conditions: none — concrete lists.
- [axioms: global claim only]

(Note: entry numbering in this module runs P-1 to P-7 and P-9 carried forward, then P-10 to P-36 new, totaling 35 with P-35/P-36 as the last two; the module's theorem count of 35 includes the carried-forward helper P-7.)

## Module: Coverage — claim 5, PREMISE (restructured)

The module was rewritten since the old pin. The old module's identity-only witnessed predicate remains, but coverage is now stated against an actual ledger, a caller-supplied validator, and an independently supplied roster of executions. The premise structure is parameterized by all three.

### X-4 (revised). The platform premise structure — **FLAGGED: this is still the named PREMISE, assumed, never proved.**
- Fields now: the sensor's privilege rank and the observed software's privilege rank (natural numbers); a proof that the sensor-below check (strict rank comparison, a decidable boolean) holds for those ranks — this field is now a checkable comparison, not an arbitrary proposition as at the old pin; the append-only condition carried as a proposition field together with a field stating it holds; and the mediation field: every roster execution has a validated record in the ledger (the recorded checker returns true).
- The coverage name is now an **abbreviation** of the premise's mediation field — the file's own doc comment reads "Assumption, not a derived theorem", and the README states the same. Old entry C-1's theorem is therefore **removed as a theorem**; the premise status is unchanged and is now more explicit.

### C-2. `unrestricted_witness` — new at this head. **FLAGGED: a vacuity result, read carefully.**
- Proves: for every execution there exists a witness under the identity-only predicate — a record carrying the execution's identity and zero events. The README's gloss: this construction reads no ledger, so the protection-model premise supplies no evidence that any particular collector observed a run.
- Hypotheses/side conditions: none.
- Axioms: **individually stated in the README — depends on no axioms at all.**

### C-3. `coverage_iff` — carried forward in strengthened form (old C-2)
- Proves: the falsification condition, now roster-relative: every roster execution has a validated ledger record if and only if there is no roster execution whose recorded check is false. An unrecorded handle outside the roster is not a counterexample (the file's doc comment).
- Hypotheses/side conditions: none — a general equivalence about the recorded checker; it does not prove coverage.
- [axioms: global claim only]

### C-4. `recorded_exact` — new at this head
- Proves: the recorded checker is exact: it returns true for an execution if and only if some witness in the ledger passes the supplied validator and names that execution.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-5. `missing_exact` — new at this head
- Proves: the missing checker is exact: an execution is in the missing list if and only if it is in the roster and no validated ledger witness names it.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-6. `recorded_append` — new at this head
- Proves: recorded-ness splits over ledger append: recorded in the concatenated ledger is the boolean OR of recorded in each part.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-7. `missing_append` — new at this head
- Proves: an execution is missing from a concatenated ledger exactly when it is missing from both parts.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-8. `missing_empty` — new at this head
- Proves: with an empty ledger the entire roster is missing — even though C-2's vacuous witness exists for each execution.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-9. `coverage_missing_iff` — new at this head
- Proves: complete roster coverage holds if and only if the missing list is empty: the existing missing checker is exactly the coverage obligation; there is no separate coverage evaluator.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-10. `empty_roster_covered` — new at this head
- Proves: vacuous coverage of an empty roster, with any ledger including the empty one.
- Hypotheses/side conditions: none.
- [axioms: global claim only]

### C-11. `empty_ledger_has_no_platform_premise` — new at this head
- Proves: a nonempty roster cannot be mediated by an empty ledger: no platform premise instance exists for an empty ledger and a nonempty roster.
- Hypotheses/side conditions: the roster is nonempty.
- [axioms: global claim only]

The module also carries two executable guards on the recorded checker (a zero-event record fails a positive-event validator; a positive-event record passes) and the eight axiom-audit commands noted in the axiom section. Deployment obligations named in the README and unchanged in kind: authenticity, unique execution identities, roster completeness, and whether the validator enforces the intended policy are not proved.

## Module: Interface — claims 6, 7, 8 and their primed disproofs — NEW MODULE

The stable interface downstream repositories import or mirror. It has no local imports. Vocabulary: a polarity per axis (minimize or maximize); a measure space as a finite ordered list of named axes; a profile as one symbol, one reading per axis, and a separate observed-behavior bit (not a measure); alignment as the reading vector having one entry per axis; the measure comparison (same symbol, no worse on every axis, ignoring the observed bit); the behavior comparison (the incumbent's observed bit implies the candidate's); the combined no-worse relation; strict improvement on the full vector; dominance as no-worse plus a strict axis; profile concatenation (readings concatenated, observed bits conjoined); releases as finite profile lists matched by symbol, with duplicate-free symbol lists and full alignment required by the release order; and the frontier filter keeping aligned undominated profiles.

### I-1. `axisLe_refl` — the per-axis comparison is reflexive.
### I-2. `axisLe_trans` — the per-axis comparison is transitive.
### I-3. `axisLe_antisymm` — the per-axis comparison is antisymmetric (equal readings).
### I-4. `not_axisLt_self` — the strict per-axis comparison is irreflexive.
### I-5. `axisLt_trans_le` — strict then no-worse composes to strict, per axis.
### I-6. `axisLe_trans_lt` — no-worse then strict composes to strict, per axis.
### I-7. `axisLt_le` — strict per-axis comparison implies the no-worse one.
### I-8. `axesLe_refl` — the vector comparison is reflexive on vectors of the space's length.
### I-9. `axesLe_length` — vector comparison forces both vectors to the space's length.
### I-10. `axesLe_trans` — the vector comparison is transitive.
### I-11. `axesLe_antisymm` — the vector comparison is antisymmetric.
### I-12. `axesLt_le` — strict vector comparison implies the no-worse one.
### I-13. `axesLt_irrefl` — the strict vector comparison is irreflexive.
### I-14. `not_axesLt_of_short_vector` — **REFUSAL, claim 6.** A short vector whose first coordinate is strict is not strictly below: the strict vector comparison refuses vectors that do not cover the space.
### I-15. `axesLt_trans_le` — vector-level strict/no-worse composition, one direction.
### I-16. `axesLe_trans_lt` — vector-level no-worse/strict composition, other direction.
### I-17. `axesLe_append` — the vector comparison splits exactly over a concatenation of spaces, given the left vectors have the left space's length.
### I-18. `axesLt_append` — the strict vector comparison over a concatenation holds exactly when one half is strict and the other is no-worse.
### I-19. `measuresLe_aligned` — measure comparison forces both profiles aligned.
### I-20. `measuresLe_refl` — measure comparison is reflexive on aligned profiles.
### I-21. `measuresLe_trans` — measure comparison is transitive.
### I-22. `measuresLe_antisymm_readings` — mutual measure comparison gives equal symbols and equal readings (the observed bit is ignored, as documented).
### I-23. `behaviorLe_refl` — the behavior comparison is reflexive.
### I-24. `behaviorLe_trans` — the behavior comparison is transitive.
### I-25. `noWorse_refl` — the combined no-worse relation is reflexive on aligned profiles.
### I-26. `noWorse_trans` — HEADLINE, claim 6. The combined relation is transitive. Axioms: **individually stated in the README — depends on no axioms at all.**
### I-27. `noWorse_antisymm` — HEADLINE, claim 6. Mutual no-worse gives equal profiles.
### I-28. `not_strictlyBetter_self` — strict improvement is irreflexive.
### I-29. `not_dominates_self` — HEADLINE, claim 6. Dominance is irreflexive.
### I-30. `dominates_trans` — HEADLINE, claim 6. Dominance is transitive. Axioms: **individually stated in the README — depends on no axioms at all.**
### I-31. `dominates_noWorse` — dominance implies no-worse.
### I-32. `not_dominates_from_measures` — **DISPROOF, claim 6-prime.** Measure improvement plus strict improvement does not imply dominance when the observed behavior is dropped: a concrete pair is measure-below and strictly better yet not dominating.
### I-33. `behaviorLe_append` — the behavior comparison composes over profile concatenation (same-symbol hypotheses).
### I-34. `measuresLe_append_iff` — HEADLINE, claim 7. Measure comparison splits exactly over concatenated spaces, given alignment of the left halves.
### I-35. `noWorse_append` — HEADLINE, claim 7. No-worse on both halves gives no-worse on the concatenation.
### I-36. `not_noWorse_append_converse` — **DISPROOF, claim 7-prime.** No-worse on a concatenation does not imply no-worse on a half: the conjoined observed bits can hide a dropped behavior on one half.
### I-37. `dominates_append_left` — HEADLINE, claim 7. Dominance on the left half plus no-worse on the right gives dominance on the concatenation.
### I-38. `dominates_append_right` — HEADLINE, claim 7. The right-half mirror of I-37.
### I-39. `dominates_append_of_halves` — HEADLINE, claim 7. No-worse on both halves with strictness on either gives dominance on the concatenation.
### I-40. `not_dominates_append_splits` — **DISPROOF, claim 7-prime.** Dominance on a concatenation does not split into the halves.
### I-41. `uniqueSymbols_append` — duplicate-free symbol lists over disjoint symbols concatenate to a duplicate-free list.
### I-42. `profilesAligned_append` — full alignment composes over release concatenation.
### I-43. `releaseLe_refl` — the release order is reflexive under duplicate-free symbols and full alignment.
### I-44. `releaseLe_trans` — HEADLINE, claim 8. The release order is transitive.
### I-45. `releaseLe_append` — HEADLINE, claim 8. Release order composes over concatenation of symbol-disjoint assemblies.
### I-46. `releaseDominates_append_left` — HEADLINE, claim 8. Release dominance on the left plus release order on the right gives release dominance on the concatenation (symbol-disjointness hypotheses).
### I-47. `releaseDominates_append_right` — HEADLINE, claim 8. The right-hand mirror of I-46.
### I-48. `not_index_aligned_preorder` — **DISPROOF, claim 8-prime.** Zipping two releases by position is not the release order: swapping two symbols keeps the release order and breaks a position-wise comparison (concrete readings 9 against 1).
### I-49. `duplicate_candidate_not_releaseLe` — **REFUSAL, claim 8.** A candidate pairing a no-worse profile with a regressing duplicate of the same symbol does not pass the release order.
### I-50. `repeated_profile_not_releaseLe` — **REFUSAL, claim 8.** Even a second exact copy of one profile does not pass the release order.
### I-51. `misaligned_addition_not_releaseLe` — **REFUSAL, claim 8.** A candidate adding a short vector on a symbol only it names does not pass the release order.
### I-52. `frontier_exact` — HEADLINE, claim 6. The interface frontier is exact: a profile is in the frontier of a list if and only if it is in the list, is aligned, and no list member dominates it.
### I-53. `frontier_antichain` — no frontier member dominates another frontier member.
### I-54. `misaligned_not_on_frontier` — **REFUSAL, claim 6.** A misaligned profile is excluded from the frontier (concrete profile).

All interface entries: [axioms: global claim only] except I-26 and I-30 as noted. The module ends with the 19 axiom-audit commands noted in the axiom section. README boundary: release-sequence monotonicity is not in this repository; it belongs to the sibling repositories.

## Module: Instance — claim 13 — NEW MODULE

A synthetic two-component command path (a gate step then a commit step) exercising the library theorems on concrete data. All results are kernel-checked facts about the synthetic data; the README states they are not measurements of a deployed system.

### S-1. `service_schedule_card` — the synthetic service's schedule enumeration has exactly 16 members.
### S-2. `service_valid_count` — the synthetic service has exactly 8 valid schedules.
### S-3. `pathSchedule_valid` — the named path schedule is valid for the service.
### S-4. `accounts_compose` — the instance of the fold sum theorem (D-16) on the gate and commit witness lists.
### S-5. `duplicate_witness_free` — re-presenting an already-recorded gate witness changes the account not at all (instance of D-11).
### S-6. `path_universe_closed` — the path universe names every path rule's conclusion: the claim-3 side condition, discharged for this instance.
### S-7. `gate_misses_committed` — coloring the gate seed alone leaves the committed fact false.
### S-8. `commit_misses_committed` — coloring the commit seed alone leaves the committed fact false.
### S-9. `joint_colors_committed` — coloring the joined seed makes the committed fact true.
### S-10. `not_coloring_distributes_on_path` — **DISPROOF, claim 11-prime.** The join of the separate colorings leaves the committed fact false while the coloring of the join makes it true (conjunction of S-7/S-8-style facts with S-9): coloring does not distribute over join on these rules.
### S-11. `service_compounds` — the instance of the coloring compounding theorem (L-30) on the two seeds.
### S-12. `gate_separated` — the gate step's candidate is separated from its incumbent (concrete bounds).
### S-13. `commit_separated` — the commit step's candidate is separated from its incumbent.
### S-14. `path_separated` — the summed path bounds are separated: the instance of the sequential-sum theorem (P-13).
### S-15. `deployments_frontier` — the computed frontier of the deployment list is the whole list (no member dominates another).
### S-16. `trimmed_rejected` — the trimmed submission fails the behavior check against the prior behaviors.
### S-17. `empty_submission_rejected` — the empty submission fails the behavior check.
### S-18. `full_kept` — the full submission passes the behavior check.
### S-19. `cost_does_not_excuse_behavior_drop` — a faster profile that drops observed behavior is measure-below but not no-worse in the interface order (instance of I-32's moral).
### S-20. `request_two_uncovered` — the second named request is not recorded by the instance's one-record ledger under its validator.
### S-21. `path_requests_covered` — every named path request is recorded once the ledger carries both records.

All instance entries: [axioms: global claim only].

---

# Flags summary

- **DISPROOFS: 9 universal-claim disproofs** — P-9 (per-execution dominance, carried forward), F-12 (every valid product schedule is side-respecting), P-15 (every Pareto point is scalarizable), P-25 (Minkowski frontier equality), I-32 (measure improvement alone dominates), I-36 and I-40 (the concatenation comparisons split — two disproofs), I-48 (index order is the release preorder), S-10 (coloring distributes over join).
- **COUNTEREXAMPLE / REFUSAL results beyond those:** P-27 (frontier membership permits regression), I-14 (short-vector strictness refused), I-49, I-50, I-51 (release-order refusals), I-54 (misaligned profile excluded), P-35, P-36 (behavior-gate refusals), S-16, S-17 (instance refusals).
- **PREMISE, not proven: 1 — unchanged in status, restructured in form.** Claim 5 / Coverage: the premise structure is now parameterized by validator, ledger, and roster; its sensor-below field is a decidable rank comparison; its append-only field remains an assumed proposition; its mediation field is the entire content consumed by the coverage abbreviation, which is an abbreviation, not a theorem. The falsification conditions (C-3, C-9) are proved; coverage itself is not.
- **VACUITY result, new:** C-2 proves the identity-only witnessed predicate is satisfiable by construction for every execution, and C-8 proves an empty ledger still leaves the whole roster missing. The README is explicit that the premise supplies no evidence any collector observed a run.
- **SIDE CONDITION: 1 headline condition — still stands exactly as stated.** Claim 3 / Coloring: the universe list must name every conclusion the rules can produce. Required by L-10, L-11, L-12, L-13, L-18 (carried forward) and by the new L-26, L-30, and (on both sides) L-35, L-36. Not required by soundness (L-17), by the new monotonicity results (L-23, L-24, L-25), or by L-19. The instance module discharges it for its concrete rules (S-6).
- **REMOVED since the old census:** the old Pareto plain gate theorem (old P-8), replaced by the split behavior gate and the two combined gates (P-10, P-31, P-33, P-34); and the old Coverage theorem form (old C-1), replaced by an abbreviation of the premise field plus the ledger-relative checker theorems (C-3 to C-11).
- **Axioms:** README headline audit claims standard axioms only, or none; six theorems are individually named in the README as depending on no axioms (P-13, P-17, P-26, I-26, I-30, C-2). In-source axiom-audit commands now exist in three modules but their outputs at this head are not recorded in the repo; the only recorded full audit is the intermediate run's 63-theorem audit at its earlier base on Lean 4.15.0.
- **Sorries:** README claims zero sorries, zero admits, zero added axioms; this census's grep of every Lean file in the tree agreed (no sorry token, no axiom declaration, no native-decision token).
- **Gate:** README-recorded lake build with warnings as errors, exit 0, on Lean 4.19.0 at this branch; committed replayer record covers the earlier 63-theorem base only. This census did not run a build.

## Watch delta — 2026-11-18, the second hourly re-synthesis watch

The watch re-read the live head at the enumeration head d88acbdc3ba78fff994067d2c73bcc01622b3f61 and shallow-cloned it. Mechanical count at that head, by the watch's own method (every theorem or lemma declaration in every Lean file in the tree): 208 declarations (204 distinct short names) across 14 Lean files, no sorry token and no custom axiom declaration in any file, 39 example declarations. The same method at the last recorded head f370992611d8c722e4897e67dbb8eaecf3d872ed counted 189 declarations (185 distinct short names). Name comparison, one mechanical method both times: 19 names gained, 0 lost. The prose placements in this annex stand at the census pin f370992611d8c722e4897e67dbb8eaecf3d872ed; a full re-census at the new head is owed and the owed mark in the ledger stands.
