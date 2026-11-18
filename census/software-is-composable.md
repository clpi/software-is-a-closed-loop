# Census — software-is-composable (clpi)

Census date: 2026-11-18, ~01:20–01:50 PST. **This repo moved during the census** — see Movement. Method: live head read first via the gh route, shallow clone, clone head verified equal, every file read. Clones read only, never edited.

## Movement (read this first)

- At census start the live head was `929d8e355857b6557c1b5d1a6bd505d9bdaeea7f` (2026-11-18T08:53:32Z), a skeleton: readme, toolchain file, git-ignore — **zero Lean code, theorem count 0 at that pin**.
- At 09:23:30Z pull request #1 ("Prove incremental release admission", from a side branch) opened-and-merged, and at 09:25:00Z the merge commit `033c12c01299a9b28983bee410c230641adc7d1e` became the live head. Final re-read confirms it is still the head.
- **This census is of the current live head `033c12c…`.** Everything below supersedes the skeleton state.

## Pins

- Live head (default branch `main`): `033c12c01299a9b28983bee410c230641adc7d1e`. Fresh shallow clone head matches exactly.
- Visibility: private (GitHub API).
- Toolchain pin: `leanprover/lean4:v4.19.0`; the readme adds the compiler commit `6caaee842e94` for its recorded run. Core Lean only — the one external dependency is a sibling repo (below), no Mathlib.
- Files at head: a substantial readme, a check script, a recorded check log, a checksum file for copied upstream files, a lakefile + manifest, example inputs with expected output, a harness main file, five root-level upstream modules, and the package's own library (root module + 9 submodules). Theorem total: **94** (49 in the package's own modules, 45 in the five copied upstream modules).

## Thesis (what the repo claims to prove)

Plain English: a new release is *admitted* over an old one exactly when, symbol by symbol, the new symbol keeps every old behaviour, keeps the same number of cost axes, never raises any cost upper bound, and both sides have valid (low ≤ high) bounds. Admission so defined is monotone and composes along chains; an incremental recheck that re-examines exactly the hypergraph-affected set (changed symbols plus everything downstream of them through caller edges) agrees with a full recheck; and the space of schedules/candidates involved is finite, with a fixed observation prefix leaving exactly 2^(free) candidates. The readme's own claims table (19 headline claims) marks each PROVEN, DISPROVEN, or PREMISE — the disproven and premise rows are censused as such below, not as wins.

Dependency / provenance boundaries stated in the readme: the package depends (git require, pinned) on the quantifiable sibling repo and imports **only** its finiteness module; that sibling's Pareto and Coverage modules at the pin "do not typecheck on Lean 4.19.0" and are not imported — "Platform execution coverage is not imported and is not proved." The five root-level modules here are **byte copies** from the optimality sibling repo at its pinned commit (a checksum file matches them), copied because that repo has no lakefile and cannot be required.

## Headline census (the 19 claims in the readme table; axiom evidence from the check log, per theorem)

Status words are the readme's own. Axiom sets are from the recorded check log's per-theorem print-outs (the audit module prints exactly these 19).

| Claim (quoted name) | Status | What it proves, plainly | Axioms (check log) |
|---|---|---|---|
| `scheduleSpace_finite` | PROVEN | For any qualification, the valid schedules form a finite space: some list contains every valid schedule. (A direct application of the imported sibling finiteness theorem.) | propext, choice, Quot.sound |
| `releaseAdmitted_iff` | PROVEN | The executable boolean admission test on releases is true exactly when the propositional admission relation holds (every old symbol found in the new release and symbol-admitted). | propext, Quot.sound |
| `releaseAdmitted_trans` | PROVEN | Admission composes: old→middle and middle→new admitted gives old→new admitted. | propext, choice, Quot.sound |
| `symbolVerdict_admitted_iff` | PROVEN | The executable per-symbol verdict says "admitted" exactly when the boolean symbol-admission test passes. (The refusal-reason correctness is not part of this theorem.) | propext |
| `qualifiedMono` | PROVEN | Premise: a release step is admitted. Then every old symbol is present in the new release with all its qualified behaviours accepted by the new symbol's behaviour list. | propext, Quot.sound |
| `qualifiedTrans` | PROVEN | The behaviour inclusion of the previous row composes along two admitted steps: a behaviour of an original symbol survives into the third release. | propext, choice, Quot.sound |
| `costNoRegression` | PROVEN | Premise: symbol-admitted step; side condition: every axis considered is within the old cost list's length. Then the new symbol does **not** strictly Pareto-dominate the old on upper bounds (not ≤ on all axes with < somewhere). | propext, Quot.sound |
| `costTrans` | PROVEN | Upper-bound non-regression composes: across two admitted symbol steps, the third symbol's bound on any in-range axis is ≤ the first's. | propext, choice, Quot.sound |
| `not_per_execution` | **DISPROVEN** | **Disproof, flagged:** it is false that a bound-admitted step is no worse on *every execution*: the concrete bounds 1..100 → 2..3 admit (upper bound falls) yet execution value 3 in the new range exceeds execution value 1 in the old. The theorem proves the negation of the universal per-execution claim. | propext, choice, Quot.sound |
| `moduleAdmission_compose` | PROVEN | Per-module admission implies whole-release admission, **under the named side condition** that every call stays inside one module (interaction closure), plus module coverage of all old symbols and unique ids in the new release. Premises carried: per-module admission for every module. | propext, Quot.sound |
| `moduleAdmission_counterexample` | **DISPROVEN** | **Counterexample, flagged:** with one cross-module call and a stubbed callee, both modules are admitted separately (computed true) yet the whole composed release is **not** admitted (computed false), and interaction closure indeed fails. So the previous row's side condition cannot be dropped. | propext |
| `evidence_remaining` | PROVEN | Fixing a prefix of independent bits leaves exactly 2^(number of free bits) candidate bit-vectors. | propext, Quot.sound |
| `not_repeated_observation_shrinks` | **DISPROVEN** | **Disproof, flagged:** observing the *same* bit twice does not shrink the candidate set again — the twice-filtered set has the same size as the once-filtered set (2, concretely), by computation. | none |
| `not_disqualification_empties` | **DISPROVEN** | **Disproof, flagged:** one disqualifying bit does not leave zero candidates — filtering 2-bit candidates to first bit false leaves 2, by computation. | none |
| `determined_of_coverage` | **PREMISE** | **Premise-flagged:** *given* a total coverage observation (a structure supplying one boolean per symbol, for all n symbols), filtering candidates to exactly that observation vector leaves exactly 1 candidate. The coverage object is the carried premise (the readme labels the whole claim PREMISE); the counting step is proved from the candidate-set facts. | propext, choice, Quot.sound |
| `inClosure_iff_affected` | PROVEN | The locally defined caller closure of the changed set is exactly the upstream hypergraph module's affected set, for an unchanged call edge set. | propext, Quot.sound |
| `incrementalRecheck_iff` | PROVEN | **Headline incremental claim.** Premises carried: old release's bounds are all valid; and every symbol *outside* the affected set is literally unchanged in the new release (found identical). Then: full release admission holds **iff** every affected symbol passes its individual check. Rechecking only the affected set is exactly as strong as rechecking everything — under those two premises. | propext, choice, Quot.sound |
| `not_recheck_seed_only` | **DISPROVEN** | **Disproof, flagged:** rechecking only the edited symbol is **not** enough: a concrete pair of releases where the edited symbol alone passes its check, the whole release is refused (computed false), the caller of the edited symbol *is* in the closure, and an unrelated symbol is not. | propext |
| `worse_refused` | PROVEN | The worked example: per-symbol verdicts on the example pair are exactly "symbol 1 admitted; symbol 7 refused for cost regression on axis 0", by computation. | none |

## Full theorem census by module (94)

### Package modules (49)

**Profile** (0 theorems): definitions only — cost bounds (low/high naturals), a symbol profile (id, behaviour list, cost bounds), a release (list of profiles), refusal reasons (missing symbol, behaviour dropped, cost regressed, axis mismatch, invalid bounds), verdicts, calls, and two premise structures used later: interaction closure (every call's caller and callee in the same module) and the coverage structure (one boolean observation per symbol — the PREMISE carrier above), plus unique-ids.

**Admission** (13): the boolean behaviour-inclusion test and its correctness equivalence (`accepts_iff`); the propositional symbol-admission relation as a structure (same id, both sides' bounds valid, behaviours kept, same cost-axis count, every paired upper bound non-increasing) and the equivalence of its boolean test (`symbolAdmitted_iff`); helpers on zipped lists (`zip_self_eq`, `zip_rel_trans`, `zip_get`, `find?_pred`, `mem_find?`, `find?_eq_of_mem` — the last needs the unique-ids side condition); symbol-admission reflexivity **given the premise that the profile's bounds are valid** (`SymbolAdmitted.refl`) and transitivity (`symbolAdmitted_trans`); release admission in both forms and their equivalence (`releaseAdmitted_iff`) and transitivity (`releaseAdmitted_trans`); the verdict function and its admitted-case equivalence (`symbolVerdict_admitted_iff`); refusal-reason selection is defined here but no theorem characterises the reasons.

**Finiteness** (1): `scheduleSpace_finite` — headline table.

**Monotonicity** (6): `qualifiedMono`, `qualifiedTrans`, `costNoRegression`, `costTrans`, `not_per_execution` — headline table; plus `bound_step_admitted`, a computed example that tightening bounds 1..100 to 2..3 is symbol-admitted (the same pair used in the per-execution disproof).

**Composition** (11): three lemmas that under interaction closure, stubbing cross-module calls makes no difference to kept behaviours / per-symbol kept sets / whole composed releases (`kept_stub_eq`, `withKept_stub`, `compose_stub`); commutation of module-filtering with composition (`module_compose_list`, `module_compose_comm`); unique-ids preserved by filtering and by id-preserving maps (`pairwise_filter`, `pairwise_map_id`); lookup survives module filtering under unique ids (`find?_filter_module`); admission of a partition assembled from per-module admission (`partition_admits`, premises: module coverage, unique ids in the new release, per-module admission); headline `moduleAdmission_compose` and the counterexample `moduleAdmission_counterexample`.

**Evidence** (13): the candidate set (all boolean vectors of a length) has no duplicates (`candidates_nodup`, via two list lemmas); filtering a duplicate-free list to one member gives the singleton (`filter_eq_singleton`); headline `evidence_remaining` via prefix-filter lemmas (`filter_prefix_nil`, `filter_cons_keep`, `filter_cons_drop` — the mismatched-bit branch contributes nothing, side condition: the two bits differ); headline premise row `determined_of_coverage`; headline disproofs `not_repeated_observation_shrinks`, `not_disqualification_empties`.

**Incremental** (3): `inClosure_iff_affected`, `incrementalRecheck_iff`, `not_recheck_seed_only` — headline table. The closure here is an inductive "seed or caller-of-a-closed-symbol" relation over call pairs.

**Examples** (2): `worse_refused` (headline) and `example_refused`: the boolean release-admission test on the same example pair is false, by computation. (The example pair is the harness example: symbol 7's upper bound rises 4 → 9.)

**Axioms** (0 theorems): the audit module — one print-axioms command for each of the 19 headlines. Its recorded output is the axiom evidence cited above.

**Root module / harness main** (0 theorems): the root only imports the library; the main file is the CSV harness whose decision procedure is the verdict function; the check log records its output matching the expected file (symbol 1 admitted, symbol 7 refused for cost regression).

### Copied upstream modules (45) — provenance: byte copies from the optimality sibling repo at its pinned commit, checksum-verified in-repo

**Qualification** (10) — a general derivation/closure theory: `least` (the derivability relation is the least relation containing the roots and closed under the rules); `closed` (derivability is itself closed); `monotone` (bigger roots and rules derive more); `idempotent` (deriving from derived roots changes nothing); `compounding` (union of root sets corresponds to union of derived sets); `order_independent` (any two closed extensions sandwiched around derivability coincide with it); `soundness` (derivations land in any root-containing closed target); `withdrawal_no_new_support` (**negative flavour:** deriving from withdrawn (live-only) roots and rules still derives in the original system — withdrawal creates no new support); `surviving_subsystem` (derivations inside a still-live subsystem survive withdrawal elsewhere, under live-roots/live-rules premises); `no_bootstrap` (**disproof, flagged:** from no roots, nothing is derivable, provided every rule has at least one premise — that nonemptiness is a carried premise).

**ExecutableClosure** (13) — the computable counterpart: subset-list facts (`subset_members`, `filter_member`, `subsets_count` — the subset list has exactly 2^(length) entries); rule/model check correctness (`ruleOK_exact`, `modelOK_exact`); `close_exact` (membership in the computed closure is exactly inductive derivability, under boundedness premises: roots and rule heads lie in the universe); `close_is_closed`, `close_contains_roots`; `close_order_independent` (equal roots/rules up to equivalence give equal closures, boundedness premises throughout); `executable_monotone` (subset roots/rules give subset closures); `boundedOK_exact`; `checkedClose_admitted` / `checkedClose_rejects` (the checked closure returns a result exactly when the boundedness conditions hold, and refuses — returns nothing — exactly when they fail).

**FiniteFrontier** (4): `frontier_exact` (a candidate is on the frontier exactly when nothing in the candidate list dominates it); `pareto_exact` (the strict Pareto test is true exactly when ≤ on every listed axis and < on some listed axis); `conflict_exact`, `unknown_exact` (the two colour classifications of positive/negative evidence, by case computation).

**FiniteQualification** (3): `candidates_length` (exactly 2^n boolean vectors of length n); `candidates_exact` (the candidate list is exactly the vectors of length n — completeness, not just count); `qualify_exact` (qualified candidates are exactly the length-n vectors the acceptance test passes).

**HypergraphIncremental** (15) — derivation over a hypergraph with an affected-set relation between an old and a new graph: `interaction_is_derived` (interaction is definitional in incidence); `affected_symm` (affectedness is symmetric in old/new); `unchanged_derivation` (a derivation at a symbol **not** affected survives the change); `unaffected_exact` (at an unaffected symbol, old and new derivability are equivalent); `incremental_exact` (**headline of this module:** the incrementally-defined derivability — reusing unaffected parts — is exactly full derivability in the new graph); `executable_full_agrees` (that, in turn, agrees with the executable closure on the corresponding finite data, under boundedness premises); `retracted_cycles_do_not_bootstrap` (**disproof, flagged:** if the new graph has no roots and every edge needs an input, nothing is incrementally derivable — cycles cannot self-start); `incidence_row_unchanged` (an unchanged edge row gives unchanged incidence); `patchedInteraction_exact` and `patchedDominance_exact` (the patched/incremental interaction and dominance functions equal the from-scratch ones on the new graph); `incrementalFrontier_exact` and `qualified_frontier_exact` (the incrementally maintained frontier equals the frontier of the new profiles, and likewise after any deterministic projection of the qualification); `graphOfRecords_edge_exact` (edges of the graph built from records are exactly the live, admitted-kind records); `matrix_update_exact`, `matrix_bit_update_exact` (incrementally updated cell counts / matrix bits equal the counts of the fully edited edge set).

Axiom evidence for the upstream modules: the check log records print-outs for a subset (9 of Qualification's 10, 9 of ExecutableClosure's 13, all 4 of FiniteFrontier's printed results, 3 of FiniteQualification's, 9 of HypergraphIncremental's 15) — every recorded set is within {propext, choice, Quot.sound}, several are empty; the unprinted theorems have **no** per-theorem axiom record in the log (the readme's global claim covers them only as a claim).

## Premises / side conditions — consolidated flags

- PREMISE claim (readme's own label): total coverage in `determined_of_coverage` — the coverage structure is assumed, not produced.
- Carried premises: bounds validity (symbol-admission reflexivity; the recheck equivalence's first hypothesis); **stability outside the affected set** (the recheck equivalence's second hypothesis — symbols outside are *assumed* found unchanged, which is exactly what makes the incremental direction work); interaction closure + module coverage + unique ids (module composition); boundedness of roots/rule-heads inside the universe (executable closure exactness); rule-nonemptiness (no-bootstrap); per-module admission (partition assembly).
- Side conditions: axis-in-range for the cost theorems; distinct-bits for the prefix-drop lemma; unique ids for the lookup lemmas.

## Zero-sorries and controls — evidence

- The check script source-guards the whole tree against the tokens for sorry, admit, axiom (as a declaration), and native decision procedures; runs two negative controls (a scratch sorry proof must be rejected — recorded rejected; a scratch proof that the regressed example is admitted must fail — recorded failing by computation, with the error quoted in the log); builds with warnings as errors; runs the axiom audit; runs the harness and diffs against the expected output; and regenerates the implications listing. The recorded log in the repo shows all stages passing and "Build completed successfully".
- This census independently re-ran the token search on the clone: no escape-hatch tokens outside the audit module's print commands. This census did **not** re-run the build (no Lean toolchain on this machine); the build evidence is the repo's own recorded log, labelled as such.

## Explicit non-claims / boundaries stated in the repo

- The readme's claims table itself marks four claims DISPROVEN and one PREMISE — those are stated as boundaries of the result, and are censused above as disproofs/premise, not as theorems in the repo's favour.
- "Platform execution coverage is not imported and is not proved"; the sibling's Pareto and Coverage modules at the pin do not typecheck on this toolchain and are excluded.
- The copied upstream modules are acknowledged as another repo's bytes (with checksums), not as this repo's original work; the optimality repo "has no lakefile, so a git require does not build" is stated as the reason.
- The per-execution reading of cost bounds is explicitly disclaimed by the disproof row: admission controls upper bounds, not every individual execution value.
