# Census — software-is-incrementally-safe (clpi)

Census date: 2026-11-18 ~01:20–01:35 PST. Method: live head read first via the gh route, then a shallow clone; clone head verified equal to the live head. Clones read only, never edited. This repo moved during the census — see "the branch" below; every pin below is timestamped by that fact.

## Pins — live head

- Live head (default branch `master`): `9466135815aa80e714d2a6999fd0aa8807375ff3` — commit "Pin Lean toolchain v4.19.0", 2026-11-18T08:56:26Z; re-read and unchanged at the end of the census. Clone head matches exactly.
- Visibility: private (GitHub API: `"private": true, "visibility": "private"`).
- Toolchain pin: `leanprover/lean4:v4.19.0` (the repo's toolchain file).
- History on the default branch: exactly 1 commit. Complete file list at head (recursive tree, API-verified): **one file only** — the toolchain file (25 bytes). **No readme, no Lean module, no lakefile, no manifest, no check log, no controls file.**

## Thesis (what the repo claims to prove)

- The repo itself states nothing: there is no readme at the live head.
- GitHub description: "Lean 4 proof that safety is preserved incrementally across releases, with security consequences (noninterference, monotone capability shrinkage), built on software-is-composable."
- Plain English: the claimed thesis is that if a release is safe, and each change (delta) is checked only on the symbols it touches plus their dependency cone, then the changed release is still safe — and the same incremental check preserves noninterference (low observers never see high data), keeps every symbol's reachable observations inside its allowance (capabilities only shrink), and respects the Pareto cost allowance.

## Theorem census at the live head

**Theorem count at the live head: 0.** No Lean code exists at this pin. Text search of the clone for theorem / lemma / sorry / axiom: nothing (there is almost nothing to search).

- Disproofs, premises, side conditions at head: none stated anywhere.
- Axiom dependencies at head: no claim of any kind; no print-axioms evidence, no check log, no build log in the repo.
- Zero-sorries claim at head: none made; vacuously, there is no proof code to contain a sorry.

## The branch — where all the actual proof code lives (NOT the live head)

The repo has exactly one other branch, carrying open pull request #1, "Prove incremental safety and its security consequences" (opened 2026-11-18T09:17:58Z, base `master`):

- At first read the branch head was `de1b30716e2b758141d5940056f37cd678464032` ("feat: prove incremental safety and its security consequences", 09:17:37Z), on top of a red test commit (09:08:31Z) and the toolchain pin.
- **During this census the branch advanced** to `5c1006a6ae6ee41a4bc19247db3a95589f5a3e9e` ("fix: visit each symbol once when collecting reachable observations", 09:23:58Z). The census below is of `5c1006a…`; the delta from the earlier branch head touched only the checker module (+6 theorems, listed there).
- The branch is a full Lake package: a lakefile declaring three libraries (the two stand-in modules for the sibling repos, plus this repo's own library as the default target), an empty dependency manifest (no external packages), the same v4.19.0 toolchain pin. Its own modules import the two stand-ins — **not** the sibling repos themselves. The pull request body states this boundary explicitly: the sibling repos at their current pins "have no Lake package, so they are not required", and the stand-ins carry equivalence obligations so a later real dependency could replace them if it exports the same operations.
- Branch theorem total: **86 theorems + 1 unnamed example** — 32 in the two stand-in modules (censused in the composable and certifiable census files) and **54 in this repo's own five modules**, censused below. The root module of this repo's library contains no theorems; it only imports the five modules.

### Module: Safety (13 theorems)

Vocabulary, plainly: a *safety property* is defined as a property of profiles that is a fixed point of the certification closure — anything in the closure already has the property. A *trace* is a list of observations; a release's traces are the lists whose every observation is produced by some symbol of the release.

| # | Theorem (quoted name) | What it proves (hypotheses → conclusion) |
|---|---|---|
| 1 | `c_isSafetyProperty` | The closure of any property is itself a safety property (from closure idempotence). |
| 2 | `safetyProperty_iff_fixed` | A property is a safety property iff, for every profile, closure membership and the property are equivalent. |
| 3 | `safetyProperty_iff_downwardClosed` | A property is a safety property iff it is downward closed: any profile below a profile with the property also has it. |
| 4 | `prefix_mem` | List lemma: an element of a prefix of a list is an element of the whole list. |
| 5 | `allowedTraces_prefixClosed` | The allowed traces (every observation satisfies a given allowance predicate) are prefix-closed: a prefix of an allowed trace is allowed. |
| 6 | `tracesOf_prefixClosed` | A release's traces are prefix-closed: a prefix of a release trace is a release trace. |
| 7 | `allowedProfile_eq_c` | For the "all observations allowed" profile property, closure membership is equivalent to the property itself. |
| 8 | `allowedProfile_safetyProperty` | The "all observations allowed" property is a safety property. |
| 9 | `behaviorSafe_iff_traceSafe` | Per-symbol safety (every symbol's profile only produces allowed observations) is equivalent to trace safety (every trace of the release is allowed). |
| 10 | `releaseSafe_iff_traceSafety` | The same equivalence with per-symbol safety stated via the certification closure. |
| 11 | `safe_downward` | Premises carried: the property is a safety property; every symbol of a release has it; a second release is pointwise below the first. Conclusion: every symbol of the second release has it. Safety descends along the release order. |
| 12 | `equivalence_obligation_upstream` | The packaged upstream export (closure, profile order, cost order together) agrees definitionally with the stand-ins' operations. Interface obligation. |
| 13 | `isSafety_transport` | Premise carried: for an arbitrary upstream export, its closure membership implies the property. Conclusion: the property is a safety property. Transports safety across an interface that merely *agrees* with the closure. |

### Module: Increment (6 theorems) — the incremental core

Named premises defined here, carried by nearly everything downstream:

- **Closure hypothesis** (per delta): every symbol in the delta's dependency cone is inspected by the delta. A named hypothesis, assumed — never proved — in every theorem that uses it.
- **Cone acceptance** (per delta): every inspected symbol's reachable observations after the delta are within the allowance. Also assumed, per delta.
- **Release safety**: every observation reachable from any symbol (through dependencies) is within the allowance for that symbol.

| # | Theorem (quoted name) | What it proves (hypotheses → conclusion) |
|---|---|---|
| 1 | `incremental_iff_scratch` | **Headline.** Premises: the base release is safe; the closure hypothesis holds for the delta. Conclusion (equivalence): cone acceptance of the delta holds **iff** the release after applying the delta is safe from scratch. Checking the cone is exactly as good as re-checking everything. |
| 2 | `preserve_safety` | The forward direction of #1 as a standalone: safe base + closure hypothesis + cone acceptance → the applied release is safe. |
| 3 | `allScratch_final` | Premise: a chain in which every step's resulting release is safe from scratch. Conclusion: the chain's final release is safe. |
| 4 | `chain_incremental_iff_scratch` | Premise: the closure hypotheses hold for every step of a chain. Conclusion (equivalence): stepwise incremental acceptance of the whole chain iff every release in the chain is safe from scratch. |
| 5 | `chain_final_of_incremental` | Closure hypotheses for the chain + stepwise incremental acceptance → the chain's final release is safe. |
| 6 | `composed_incremental_iff_final` | Premises: safe base; the closure hypothesis for the single delta composed from a whole list of deltas. Conclusion (equivalence): cone acceptance of the composed delta iff the release obtained by applying the deltas one by one is safe. Bridges the composable stand-in's composition theorem and #1. |

### Module: Security (9 theorems)

| # | Theorem (quoted name) | What it proves (hypotheses → conclusion) |
|---|---|---|
| 1 | `capability_within_allowance` | Safe base + closure hypothesis + cone acceptance → after the delta, every reachable observation of every symbol is within that symbol's allowance. A restatement of safety preservation in allowance language. |
| 2 | `chain_capabilities_within_allowance` | The chain form of #1: chain closure hypotheses + stepwise acceptance → the final release stays within allowance everywhere. |
| 3 | `capability_shrinks` | **Monotone capability shrinkage.** Premises carried: the delta is monotone in the composable sense (each changed symbol's update is below its original profile); the base release is within allowance. Conclusion: the applied release is within allowance. Note: this one does **not** use the closure hypothesis or cone acceptance — monotonicity of the delta substitutes for checking. |
| 4 | `noninterference_preserved` | **Noninterference.** Definitions: a behaviour assignment is noninterfering when every observation reachable from a low symbol (flagged not-high) is itself not-high. Premises: base is noninterfering; closure hypothesis; the NI form of cone acceptance (inspected symbols' post-delta reachable observations from low symbols are not-high). Conclusion: the applied release is noninterfering. |
| 5 | `chain_noninterference` | The chain form of #4: stepwise NI acceptance (with per-step closure hypotheses) → the final release is noninterfering. |
| 6 | `forbidden_preserved` | Premises: base release produces no observations at all from forbidden symbols; closure hypothesis; the forbidden form of cone acceptance. Conclusion: the applied release also produces no observations from forbidden symbols. |
| 7 | `forbidden_introduced_refused` | **Disproof, flagged.** Premises: policy premise — a forbidden symbol's allowance is empty (nothing is allowed from it); the symbol is forbidden; the delta changes it; the delta's update for it produces a specific observation; closure hypothesis. Conclusion: cone acceptance of this delta is **false** (its negation is proved). I.e. a delta that gives a forbidden symbol any behaviour cannot pass the incremental check. This is the theorem behind the executable refusal example below. |
| 8 | `authority_pareto_bounded` | Cost transitivity: used cost below a bound, and the bound below an allowance, gives used cost below the allowance. |
| 9 | `admitted_release_downward` | The certifiable stand-in's downward-admission theorem, re-exported: an admitted candidate plus a profile-and-cost-smaller candidate gives admission of the smaller one. |

### Module: Checker (24 theorems) — the executable checker

Vocabulary, plainly: an executable delta is concrete string data (changed symbols with their new observation lists, dependency pairs, inspected symbols, high/low flags, two cost bounds). The checker computes the cone by bounded iteration, computes reachable observations by a fuel-bounded, visit-each-symbol-once collection, and returns a verdict: accept, or refuse *naming a symbol*. Theorems marked † are the six added by the branch-advancing commit during this census.

| # | Theorem (quoted name) | What it proves |
|---|---|---|
| 1 | `cycle_reached_once` † | By computation (`decide`): on a 3-symbol dependency cycle, the collected reachable observations from the first symbol are exactly its three observations, once each. |
| 2 | `dense_reached_once` † | By computation: on the 5-symbol complete dependency graph, collection from one symbol yields exactly the five observations, once each. |
| 3 | `not_isEmpty_iff` | A list's emptiness flag is false exactly when the list is non-empty. Helper. |
| 4 | `bool_not_true_iff_false` | Boolean negation helper. |
| 5 | `isForbiddenHit_iff` | The forbidden-hit test is true exactly when the symbol is in the forbidden list and its post-delta behaviour is non-empty. |
| 6 | `changedCost_of_nil` | A delta with no changed symbols has change cost zero. |
| 7 | `changedSymbols_nil` | If the changed-symbol list is empty, the changed list itself is empty. |
| 8 | `paretoOK_zero` | A zero-cost delta passes the cost test against any bounds. |
| 9 | `paretoOK_iff` | The executable cost test passes exactly when the (cost, cost) pair is componentwise below the (time bound, compute bound) pair, in the certifiable stand-in's order. Side condition: the same change cost is used for **both** axes — the executable cost model does not distinguish time from compute. |
| 10 | `find?_none_iff` | A list search finds nothing exactly when the test is false for every element. Helper. |
| 11 | `check_accept_iff` | **Checker characterisation, accept side.** The checker accepts exactly when: no cone symbol is uninspected, no cone symbol is a forbidden hit, no cone symbol has an unsafe reachable observation, and the cost test passes — all four, as computed lists/flags. |
| 12 | `check_refuse_iff` | **Checker characterisation, refuse side.** The checker refuses naming a symbol exactly when that symbol is the first failure in the fixed priority order: uninspected cone symbol; else forbidden hit; else unsafe observation; else cost failure naming the first changed symbol. |
| 13 | `forbidden_refusal_names` | Premises: no uninspected cone symbol; the forbidden scan returns a name. Conclusion: the checker refuses by that name, the name really is forbidden with non-empty post-delta behaviour, and every earlier cone symbol is not a forbidden hit — the refusal is correctly named, not just any refusal. |
| 14 | `accept_imp_pareto` | Acceptance implies the cost pair is within bounds (in the stand-in's order). |
| 15 | `accept_imp_no_new_forbidden` | Acceptance implies every forbidden symbol in the cone has empty post-delta behaviour. |
| 16 | `symReach_obs` † | Any observation of a symbol reachable by the executable dependency-step relation is reachable in the composable stand-in's inductive reachability sense. |
| 17 | `mem_directDeps` † | Membership in the computed direct-dependency list is equivalent to the pair being in the dependency list. |
| 18 | `collect_sym` † | Soundness of collection: any collected observation comes from the behaviour of some symbol reachable (by dependency steps) from some symbol on the initial work list. |
| 19 | `reachedObs_imp_reaches` † | Soundness bridge: any observation in the executable collected list is reachable in the inductive sense. One direction only — see non-claims. |
| 20 | `parents_mem` | Any symbol produced by the cone-expansion step has a dependency edge into the current cone set. |
| 21 | `expand_cone` | One expansion step stays inside the inductive cone, given the current set is inside it. |
| 22 | `iter_cone` | Every iterate of cone expansion, from changed symbols as seeds, stays inside the inductive cone. |
| 23 | `coneExec_sound` | **Soundness of the executable cone:** every symbol in the computed cone list is in the inductive dependency cone. One direction only — see non-claims. |
| 24 | `checker_scope_in_cone` | Premise: the checker refuses a name and there was no uninspected-symbol failure. Conclusion: the named symbol is in the computed cone, or it is the first changed symbol (the cost-failure case of #12). Refusals are scoped to the cone, modulo that one case. |

### Module: Example (2 theorems + 1 unnamed example)

| # | Theorem (quoted name) | What it proves |
|---|---|---|
| 1 | `evil_refused` | By computation (`decide`): the checker, with a one-symbol forbidden list naming the changed symbol in a concrete delta that gives it a spawning behaviour, returns refuse **by that symbol's name**. The unnamed example directly above it states the same equation. The symbol name itself is quoted in the file; it is the branch's designated forbidden symbol. |
| 2 | `benign_accepted` | By computation: a concrete harmless delta (one logging symbol, allowed to write, within cost bounds) is accepted. |

A top-level evaluation command in this module prints the refusal verdict when the file is elaborated; the pull request body quotes that output.

## Disproofs — flagged explicitly (branch)

- `forbidden_introduced_refused` (Security #7): the one genuine impossibility theorem — cone acceptance of a delta that activates a forbidden symbol is disproved from the stated premises.
- `evil_refused` (Example #1): a computed, concrete refusal — a disproof by evaluation that the checker accepts that delta.
- In the stand-in modules on the same branch: the certifiable stand-in's irreflexivity theorem (no cost dominates itself) and the composable stand-in's not-in-cone theorem (a symbol outside the cone was not changed). See the sibling census files.
- Nothing else in the branch is a disproof; there is no other counterexample construction.

## Named premises carried rather than proved — flagged explicitly (branch)

1. **The closure hypothesis** (per delta, and per chain step): every cone symbol is inspected. Assumed in the headline equivalence, safety preservation, chain theorems, noninterference, and forbidden-symbol preservation. The executable checker *enforces* its concrete analogue (it refuses uninspected cone symbols), but the abstract theorems take it as an input.
2. **Cone acceptance** (and its NI and forbidden variants): the per-delta check result is an assumed proposition in the abstract theorems; only for the two concrete example deltas is a checker verdict actually computed.
3. **Base-release facts**: base safety, base noninterference, and base forbidden-emptiness are all assumed, never established for any concrete release in the abstract modules.
4. **The policy premise** in the disproof (Security #7): forbidden symbols have empty allowance — an input about the policy, not a theorem.
5. **The monotonicity premise** in Security #3: changed updates sit below original profiles — an input (the same carried premise as the composable headline).
6. **Interface agreement**: the safety-transport theorem (Safety #13) assumes an export's closure implies the property; the equivalence-obligation theorems show agreement only for the *canonical* stand-ins, by definition.

## Side conditions — stated (branch)

- Changed-flag case splits (changed = true / false) drive the apply lemmas underneath everything.
- The headline equivalence needs the closure hypothesis as a *side hypothesis*, not as part of the acceptance predicate — with it dropped, only the trivial direction (from-scratch safety implies acceptance) survives, by the proof's own structure.
- Executable bounds are fuel-style: the cone is iterated a fixed number of times computed from the input sizes, and observation collection runs on a fixed fuel computed from the dependency list's length. The soundness theorems (#19, #23) are proved for those bounded computations.
- The executable cost test uses one number (total changed-behaviour size) for both the time and the compute bound (Checker #9).
- Two modules open the classical namespace; consistent with the axiom claim below, classical choice may be among the dependencies of the chain/NI proofs — no per-theorem breakdown exists in the repo to say which.

## Axiom dependencies and zero-sorries — evidence, sourced precisely (branch)

- **In-repo evidence: none of the strongest kind.** No file in the branch contains a print-axioms command or its output; there is no check log, no build log, and no CI configuration in the repo at either pin.
- **Textual evidence:** a search of every Lean file on the branch finds no sorry token and no axiom declaration.
- **Pull-request-body evidence (not in the repo):** PR #1's body claims "Headline axioms are only `propext`, `Classical.choice`, and `Quot.sound`" and that the refusal example "uses none"; and it quotes a build log at toolchain v4.19.0 ending "Build completed successfully", including the evaluation line printing the refusal verdict. The body was written against the current branch head. This census did **not** independently run the build — no Lean toolchain is installed on this machine — so kernel-checked status rests on that quoted log, labelled here as such.

## Explicit non-claims / boundaries (branch and head)

- The branch does **not** import or depend on the sibling repos; it re-implements them as stand-ins and says so in the pull request body. Nothing on the branch proves anything about the sibling repos' actual contents (which, at their live heads, are empty — see the sibling censuses).
- Soundness without stated completeness, twice: the executable cone is proved to contain only true cone members, and collected observations are proved to be truly reachable — but no theorem on the branch states the converse (that every cone member is computed, or every reachable observation is collected). The checker characterisations (#11, #12) are exact for the *computed* lists, which is a statement about the checker itself, not about the inductive notions.
- The pull request body itself corrects an over-strong reading: "The chain statement that is actually true" is the equivalence **given the closure hypotheses** — the unconditional version is not claimed there, and is not proved.
- The earlier red commit on the branch is retained in its history: at that commit the checker accepted every delta and the refusal example failed by computation. The fix is the later commits; the branch does not hide the red state.
- At the live head, the repo claims nothing at all — no readme — so the description-field thesis above is a claim about a proof that, at the default branch's pin, is not in the repo.
