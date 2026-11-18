# Census — software-is-incrementally-certifiable (clpi)

Census date: 2026-11-18 ~01:20–01:35 PST. Method: live head read first via the gh route, then a shallow clone; clone head verified equal to the live head. Clone read only, never edited.

## Pins

- Live head (default branch `master`): `f3b9f896ac76a95e7104c98af66e41413e7e5b2d` — the repo's single commit, "Initial commit", 2026-11-18T08:55:11Z. Clone head matches exactly.
- Visibility: private (GitHub API: `"private": true, "visibility": "private"`).
- Toolchain pin: **none — the repo has no toolchain file at all.** (The other two repos in this set pin `leanprover/lean4:v4.19.0`; this one pins nothing.)
- History: exactly 1 commit. Branches: `master` only. Pull requests: none, any state.
- Complete file list at head (recursive tree, API-verified): **one file only** — a readme (159 bytes). No Lean module, no lakefile, no manifest, no git-ignore, no check log, no controls file.

## Thesis (what the repo claims to prove)

- GitHub description: "Lean 4 proof that incremental monotonic certification is extensive and yields Pareto-optimal dominance across releases."
- Readme, in full: "Lean 4 proof that incremental monotonic certification is extensive and yields Pareto-optimal dominance across releases."
- Plain English: the claim on the tin is that the certification operator (the closure that adds every profile sitting below an already-certified one) is extensive — a certified thing stays certified — and that admission of a release can be decided by that closure together with a componentwise (Pareto) cost bound, giving a dominance order across releases in which a release that is no worse on any cost axis, and better on one, dominates.

## Theorem census at the live head

**Theorem count at the live head: 0.** There is no Lean code in the repo at this pin: no theorem, no lemma, no definition, no example. A text search of the whole clone for theorem / lemma / sorry / axiom finds nothing.

- Disproofs at head: none (nothing is proved or disproved).
- Named premises at head: none stated in any file.
- Side conditions at head: none stated.
- Axiom dependencies at head: no claim of any kind; no print-axioms evidence, no check log, no build log in the repo.
- Zero-sorries claim at head: no such claim is made in the repo; the absence of sorries is vacuous — there is no proof code to contain one.

## Explicit non-claims / boundaries at head

- The readme asserts a finished "Lean 4 proof"; the repo at this pin contains no artifact that could back that assertion, and not even a toolchain pin to build one against. That gap is the headline finding, stated here, not smoothed over.
- Nothing in the repo states any boundary, limitation, or non-claim beyond the one readme sentence.

## Annex — the stand-in module on another repo's unmerged branch (NOT this repo's content)

As with the composable repo: the only Lean code developing this thesis is a **stand-in module inside the safe repo's open pull request branch** (branch head `5c1006a6ae6ee41a4bc19247db3a95589f5a3e9e` at census time). That pull request's body states this repo at the pin above "has no Lake package, so it is not required", and that the stand-in carries equivalence obligations so a later real dependency could replace it if it exports the same closure, profile order, and cost order. The theorems below are **not** theorems of this repo. The stand-in also records this repo's live head as a string constant inside a sibling-pin structure — a string, not a machine-checked dependency.

Stand-in module (file in the safe repo's branch, 14 theorems). Vocabulary, plainly: it imports the composable stand-in; a *profile* is as there; the *closure* of a property of profiles is the set of profiles sitting below some profile with the property; a *cost* is a pair of natural numbers (time, compute); one cost is below another when both components are; one cost *dominates* another when it is below it and strictly smaller on at least one axis.

| # | Theorem (quoted name) | What it proves (hypotheses → conclusion) |
|---|---|---|
| 1 | `c_extensive` | **Extensivity (half the repo's thesis).** Premise: a profile has the property. Conclusion: the profile is in the closure of the property. (Witness: itself, via order reflexivity.) |
| 2 | `c_monotone` | The closure is monotone in the property: premise — every profile with the first property has the second — turns membership in the first closure into membership in the second. |
| 3 | `c_idempotent` | **Idempotence.** The closure of the closure of a property is exactly the closure of the property (equivalence, both directions). |
| 4 | `paretoLE_refl` | The componentwise cost order is reflexive. |
| 5 | `paretoLE_trans` | The componentwise cost order is transitive. |
| 6 | `paretoDominates_le` | Dominance implies the componentwise order (dominating cost is no worse on either axis). |
| 7 | `paretoDominates_irrefl` | **Disproof, flagged:** no cost dominates itself — dominance is irreflexive, because a strict inequality of a number with itself is impossible. This is the stand-in's one explicit "something is false" theorem. |
| 8 | `equivalence_obligation_c` | The closure, as exported, is definitionally the stated existential form (some certified profile above the given one). Interface obligation, proved by reflexivity of the equivalence. |
| 9 | `equivalence_obligation_pareto` | The exported "no worse" relation is definitionally the two componentwise inequalities. Interface obligation. |
| 10 | `equivalence_obligation_paretoDominates` | The exported dominance relation is definitionally "no worse, and strictly better on time or on compute". Interface obligation. |
| 11 | `admit_iff_closure_and_pareto` | Admission of a candidate (a profile plus a cost) under a safety property and a cost bound is equivalent to: the profile is in the closure of the safety property, **and** the cost is componentwise below the bound. This is a definitional unfolding of the admission predicate, proved by simplification. |
| 12 | `admitted_downward` | Premises carried: a candidate is admitted; a second candidate's profile is below the first's; its cost is componentwise below the first's. Conclusion: the second candidate is also admitted. (Downward closure of admission — the "dominance across releases" workhorse.) |
| 13 | `equivalence_obligation_closure` | The exported closure structure's operator is definitionally the closure. Interface obligation. (The structure packages extensivity, monotonicity, and idempotence — theorems #1–#3 — as its fields.) |
| 14 | `equivalence_obligation_paretoExport` | The exported cost-order structure's relation is definitionally the componentwise order. Interface obligation. (The structure packages #4 and #5.) |

- Disproofs in the stand-in: #7 only. No counterexample construction anywhere.
- Named premises carried rather than proved in the stand-in: (a) admission itself is a *definition* (closure membership plus cost bound) — no theorem shows any concrete release is admitted, and the safety property and the bound are inputs throughout; (b) the hypotheses of #12 are inputs; (c) five of the fourteen theorems (#8, #9, #10, #13, #14) are interface obligations that hold by definition, not substantive facts — the substantive content is #1, #2, #3, #6, #7, #11, #12.
- Side conditions in the stand-in: the strictness disjunction in dominance (strict on time **or** strict on compute) in #7/#10; both cost components must satisfy the bound in #11.
- On the thesis wording: the stand-in proves extensivity and idempotence of the closure and the basic order facts about dominance. It does **not** prove "Pareto-optimality" in the sense of an optimal element existing or being attained — no existence or maximality theorem is present. "Yields Pareto-optimal dominance" in the readme/description is stronger than what the stand-in's theorems state.
- Axiom / sorry evidence for the stand-in: no sorry token in the file (text search), no axiom declaration, no per-theorem print-axioms output anywhere. The safe pull request's body claims headline axioms are only the three standard ones and quotes a successful build at toolchain v4.19.0 — sourced in the safe census. This census did not run a build (no Lean toolchain on this machine).
