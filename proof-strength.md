# Proof-strength ledger — the software proof family

The tracking instrument for the proof family: per repo, at
its current pin, what is proven, what rests on named
premises, what is absent (claimed or implied with no formal
statement), what controls stand in the tree, and the gate
state. Refreshed on every re-synthesis (resynthesis.md).

Two defect rules bind this ledger:

- A repo whose proven set SHRINKS between refreshes is a
  regression, flagged in the run record of the re-synthesis
  that sees it — never silently absorbed.
- A repo whose pin MOVES without this ledger moving in the
  same re-synthesis is a synthesis defect, flagged in the run
  record. The ledger and the pins move together or the run
  says why not.

States are at each claim's evidence level. Relayed audit
states are marked relayed until the verification lane
reports (next-steps.md step 1). First ledger: 2026-11-18,
at the first synthesis's census pins.

## software-is-quantifiable — census pin f3709926 (sweep refresh 2026-11-18; first-synthesis pin 37917a41)

- Proven: 46 theorems — finiteness (4), the fold (12),
  coloring (19, under the universe side condition), Pareto
  at bounds (8), and the per-execution dominance DISPROOF
  (1, counted as a proven result: the claim it kills stays
  dead).
- On named premises: coverage — the coverage theorem is the
  platform premise's mediation field restated; the premise
  (sensor below, append-only ledger, complete mediation) is
  carried, and the audit notes the sensor-below field is an
  arbitrary proposition that can be True.
- Absent: nothing in the repo's own claim list lacks a
  statement; the Idol-native form of these results is absent
  (that absence is next-steps O9, an engine-side item).
- Controls in tree: the disproof's counterexample inside the
  Pareto module; the recorded build compiled every module
  directly, exit 0.
- Gate state: green at the census pin by the repo's recorded
  build (partial toolchain, direct compilation, warnings not
  errors in this repo). Relayed: the external audit at head
  ba27febf ran the lake build green with 63 theorems and
  clean hygiene.

## software-optimality — census pin b52c3170 (sweep refresh 2026-11-18; first-synthesis pin 0ea4626b; head moved again after the sweep census — see the sweep section)

- Proven: the fourteen modules' results as placed in
  synthesis.md — the axiom-free closure core, the
  fail-closed executable bridge, exact frontier, exact
  schedules enumeration, the campaigns' checked arithmetic,
  scoped admission and selection, exact relevance profiles,
  incremental-equals-full over the hypergraph.
- On named premises: accepted improvement rests on a
  supplied preservation checker being sound; semantic
  soundness of scoped qualification rests on an explicit
  validation premise; the scoped-evidence external
  obligations (authenticity, digest-to-bytes binding, parser
  correctness, authorization) are named premises, not
  theorems.
- Absent (no formal statement yet): the design document's
  five proposed items — the linked-certificate principal
  theorem, the coverage-certificate upgrade, typed transfer
  edges, the product decomposition, the certificate forms;
  the four-way coloring's lawful and unlawful
  characterizations; the two general-Pareto obligations
  (bounds-derivation soundness, aggregation well-defined).
- Controls in tree: the negative-controls document and its
  cases; executable guards in the closure, evidence, and
  campaign modules, including a synthetic over-cap rejection.
- Gate state: green firsthand at the census pin (the
  topology lane's baseline run of the check script: exit 0,
  no errors or warnings). Relayed: the audit at af23f5d
  counted 26 files and 172 theorems, build green.

## software-is-composable — pin a3058ba6 (sweep refresh 2026-11-18; first-synthesis pin 033c12c0)

- Proven: 49 own theorems; of its 19 headline claims, 13
  proven and 5 DISPROVEN (per-execution monotonicity, module
  composition without interaction closure, repeated
  observation shrinking, disqualification emptying, seed-only
  recheck) — the disproofs are proven results and stand in
  the proven column as such.
- On named premises: 1 headline claim (coverage determines
  the candidate) rests on the supplied total-coverage
  structure; further carried premises: bounds validity,
  stability outside the affected set, interaction closure as
  a side condition.
- Absent: refusal-reason correctness has no characterization
  theorem; platform execution coverage is not imported and
  not proved (the sibling modules for it do not typecheck on
  this toolchain at the import pin).
- Controls in tree: the check script's two negative controls
  (a sorry proof must be rejected — recorded rejected; a
  proof that the regressed example is admitted must fail —
  recorded failing), plus the harness output diffed against
  its expected file.
- Gate state: the repo's recorded check log is green;
  the census did not re-run the build (no toolchain on the
  census host). Relayed conflict: the external audit at the
  earlier pin 929d8e35 found no proof in the repo at all —
  true at that pin; the verification lane settles the pair.

## software-is-incrementally-certifiable — pin c9ffd49a (sweep refresh 2026-11-18)

- Proven: 0 at the default head.
- On named premises: none stated in the repo.
- Absent: the entire thesis — certification extensivity and
  Pareto-optimal dominance across releases — has no formal
  statement in the repo (one readme sentence; no toolchain
  pin). Its stand-in on the safe branch proves extensivity,
  monotonicity, idempotence, and cost-order facts (14
  theorems, 5 of them definitional interface obligations)
  and no optimality existence theorem; that content is the
  stand-in's, not this repo's.
- Controls in tree: none.
- Gate state: none — no check script, no toolchain pin.

## software-is-incrementally-safe — head 8ad1dd26; branch 5c1006a6 unmerged (sweep refresh 2026-11-18)

- Proven: 0 at the default head. On the unmerged branch: 54
  theorems in its own modules plus 32 in two stand-ins —
  carried at exactly the audited strength (synthesis.md
  section 6, F1–F5): its safety is per-event allow-list
  membership with order invisible; its NI is taint
  reachability; its preservation theorems are exact given
  the closure hypothesis.
- On named premises: the closure hypothesis and cone
  acceptance per delta; base-release safety, NI, and
  forbidden-emptiness assumed; the empty-allowance policy
  premise; monotonicity where it substitutes for checking.
- Absent: any theorem from checker acceptance to the
  abstract properties (the executable checker is not
  connected, and it trusts submitter-supplied dependencies,
  labels, and budgets — relayed counterexamples show the
  same change accepted after editing them); completeness of
  the computed cone and of observation collection; liveness
  of any kind.
- Controls in tree (branch): two computed verdicts — a
  forbidden-activating delta refused by name, a benign delta
  accepted; the branch retains its earlier red commit (the
  checker once accepted everything) in its history.
- Gate state: no check log in the repo; the build claim
  rests on the pull-request body's quoted log. Relayed: the
  audit built the branch at de1b3071 green.

## software-doesnt-have-to-regress — pin c36829da (sweep refresh 2026-11-18)

- Proven: 0. On named premises: none stated.
- Absent: the entire claim — a release process with
  per-symbol certification never has to regress — has no
  formal statement in the repo (two-line readme, no
  toolchain pin). Its components are proven elsewhere
  (synthesis.md section 3.8); the release-level statement is
  proven nowhere.
- Controls in tree: none. Gate state: none.

## software-doesnt-need-review — pin 40b1e885 (sweep refresh 2026-11-18)

- Proven: 0. On named premises: none stated.
- Absent: any formal statement of when manual review is
  redundant given per-symbol certification — the audit's
  verdict is that no such statement exists to check. The
  proposal half of the readme is likewise absent as a design.
- Controls in tree: none. Gate state: none.

## software-is-solvable — pin 5bbceee7 (sweep refresh 2026-11-18)

- Proven: 48 named theorems (closure core 10, executable
  closure 13, hyperlattice 15, executable witness 10),
  including the no-bootstrap DISPROOF under its side premise.
  Two of the four modules are byte-identical to
  software-optimality's (duplication, synthesis.md section 4).
- On named premises: admission and authentication of roots
  and edges; truth of roots and truth preservation of rules
  (the soundness theorem's premises); classifier exactness
  for the resolution strictness results; boundedness for
  every executable bridge; the qualification gate supplied;
  withdrawal input already resolved.
- Absent: no production performance claim is made (the
  reference enumeration is exponential by design); semantic
  equivalence from hashing is explicitly not claimed.
- Controls in tree: 35 kernel guards (29 in the test module,
  6 in the executable closure) plus one evaluated closure
  example — synergy, duplicate-append, projection, and
  malformed-domain cases among them.
- Gate state: check script bans sorry, admission, axiom, and
  native-decision tokens and compiles with warnings as
  errors; the recorded check log ends in PASS. Relayed: the
  audit built this pin green and confirmed hygiene.

## software-frontier-is-solvable — pin 6a41c7be (sweep refresh 2026-11-18)

- Proven: 14 theorems, every one with a printed axiom line
  (standard axioms or none) — exact insertion and retraction
  equations, guardedness, evaluator exactness, existence —
  and two DISPROOFS by counterexample (frontier membership
  does not imply no regression; frontier-only storage loses
  retraction information), plus three negation theorems.
- On named premises: eligibility, costs, and the dominance
  relation are supplied by the caller; insertion assumes
  irreflexivity; existence assumes a strict partial order
  and a nonempty list; guarded existence assumes the
  baseline present and eligible.
- Absent: candidate-generator completeness (explicitly not
  claimed); any runtime or performance claim (the evaluator
  is a full-scan oracle); the hypergraph link is by
  convention — the repo does not import it.
- Controls in tree: 15 kernel-reduced examples, including
  both counterexamples as fixtures, tie and resurrection
  cases, and the empty-axis case.
- Gate state: check script with token bans and warnings as
  errors; recorded check log green. Relayed: the audit built
  this pin green.

## software-is-more-traceable-than-you-think — not landed

- Announced 2026-11-18; no repo existed at the first
  synthesis. Every column enters on the re-enumeration that
  first sees it: proven, premises, absent, controls, gate —
  all currently unrecorded, colored unknown.

## Sweep refresh — 2026-11-18 (estate-wide content sweep)

The rows above were first written at the first synthesis's
pins. This section restates every row at the sweep's census
pin and adds the rows for the repos the sweep found
proof-bearing outside the original family. The annex files in
census/ carry the full censuses these lines summarize.

Refreshed rows, at their sweep pins:

- software-is-quantifiable — f3709926. Proven: 186 theorems
  (was 46): finiteness 13, fold 17, coloring 36 under the same
  universe side condition, Pareto 35, coverage module 10, and
  two new modules (interface 54, instance 21). Disproofs grew
  from 1 to 9, plus 10 further counterexample results. On
  named premises: coverage — restructured, and the coverage
  name is now an abbreviation of the premise's mediation
  field, not a theorem; a new axiom-free vacuity theorem
  stands beside it. Toolchain: Lean 4.19.0 (was 4.15.0). Gate:
  the readme records a warnings-as-errors build at exit 0;
  the portable replayer record covers the earlier 63-theorem
  base only.
- software-optimality — b52c3170 (live head moved to a2e492cb
  after this census; re-census owed). Proven: 412
  declarations across 33 root modules and a composition
  package (was 14 modules). Discharged in this refresh: the
  two general Pareto obligations (bounds-derivation
  soundness; aggregation well-defined) and the design items
  in fenced forms — the linked certificate in its eligible
  specialization plus the enumerated-generator upgrade, typed
  transfer as checked pairs, the coverage upgrade for the
  enumerated generator and named catalogues, product
  decomposition in its fenced forms (unrestricted forms
  disproven), and the certificate forms including worklist
  agreement. Not discharged: the coloring lawful and unlawful
  characterizations. Gate: two recorded logs at the pin,
  247 axiom prints, all standard or empty.
- software-is-composable — a3058ba6 (live head moved to
  7d72fd08 after this census; re-census owed). Proven: its own
  theorems grew 49 to 52 (a new bridge module); the same 19
  headlines stand with the same axiom sets. Defect-rule note,
  flagged rather than absorbed: the in-tree theorem count
  fell from 94 to 56 because the 45 byte-copied upstream
  modules were removed and replaced by pinned dependencies on
  optimality and quantifiable. That is de-duplication, not a
  shrink of the proven set — the claims those modules carried
  are now cited at their stronger homes, and the repo's own
  proven set grew. The recorded gate log predates the bridge
  module, so the 3 bridge theorems' axiom sets are unknown
  from recorded evidence.
- software-is-incrementally-certifiable — c9ffd49a. Proven at
  head: 7 theorems, all inside a worked Merkle-tree repair
  example with recorded axiom sets and a rejected control.
  Absent: the library itself — the thesis (certification
  extensivity with Pareto dominance across releases) remains
  claimed, not proven; no toolchain pin or lakefile yet.
- software-is-incrementally-safe — head 8ad1dd26. Proven at
  head: 6 theorems inside a worked policy-migration example.
  The former branch content (86 theorems at audited strength)
  has NOT merged; its pull request is still open and none of
  its files are in the head tree. The thesis at head remains
  claimed, not proven. No proven-set shrink: the branch
  content was never head content.
- software-doesnt-have-to-regress — c36829da. Proven: 131
  theorems (125 library across six modules, plus guards and
  example theorems), where the first synthesis recorded 0.
  Recorded gate log passes; 28 headline axiom prints, all
  standard or none. Absent at this pin: nothing in its claim
  list lacks a statement; its dependencies are pinned at
  older sibling pins, recorded in its annex.
- software-doesnt-need-review — 40b1e885. Proven: 82 theorems
  in tree (76 library across ten modules, 4 example, 2 inside
  planted controls that must fail), where the first synthesis
  recorded 0. The broad redundancy claim is refuted in its
  own table; only the narrow cone form is proven. Gate: a
  complete check script stands in the tree but no recorded
  run log does — recorded pass unknown.
- software-is-solvable — 5bbceee7. Proven: 51 (library
  unchanged at 48 with the same names; 3 new example theorems,
  all axiom-free). Guards unchanged at 35; recorded log
  passes; the two shared modules re-verified byte-identical
  to optimality at its sweep pin.
- software-frontier-is-solvable — 6a41c7be. Proven: 18
  (library unchanged at 14 with the same axiom sets; 4 new
  example theorems). Examples 15 and disproofs 2 unchanged;
  recorded log identical to the first census.

New rows from the sweep:

## idol-semi — pin 508d7c66 (the same tree stands as semi-persistent at the same pin)

- Proven: 2,053 named theorems across 156 Lean files —
  congruence closure 493, matching 1,483 (engine, flattened
  views, environment, steps, proof files, base), fidelity 72,
  final 5 — plus a conformance development of executable
  generators (200 fixtures per family, no theorems), and
  Verus proofs on the Rust side (proof functions in the
  abstract domains, verified containers, anti-unification,
  and engine crates). Nine disproofs flagged in its annex.
- On named premises: the anti-unification crate expressly
  does not claim the derived value equals the optimum or that
  the solver is refined; the container crate's verified-fact
  count is a recorded claim dated 2026-08-24, with no log in
  the tree.
- Absent: a recorded check log at this head — the check
  script and CI gate stand in the tree, and the census token
  scan is clean (no admitted proofs; 424 print-axioms lines
  across 23 check files), so theorems are proven as source
  statements while a passing gate at this exact head is
  claimed, not proven. One internal trusted-body count
  discrepancy is recorded as unknown in its annex.
- Controls in tree: the conformance fixtures and the check
  files. Toolchain: Lean with Mathlib at version 4.35.0 —
  the only Mathlib-bearing proof tree in the estate.

## premise-retraction-playground — pin 47f469a4

- Proven: the additive form of retraction exactness as
  ordinary mathematics in its readme (not machine-checked);
  its two demo fits independently recomputed in the sweep
  with exact rational arithmetic, matching all six printed
  weight values.
- Absent: any kernel-checked form; the page's general
  exactness claim for its own code is claimed, not proven —
  an executed run-time verification, placed below
  kernel-checked proof in this ledger. Controls: the in-page
  exact comparisons (five, byte-identical). Gate: none in
  tree.

## software-compilers-lose-info — pin f531e31a

- Proven: 33 theorems (loss 12, preservation 10, basic 5,
  completeness 2, implications 4), plus the hypergraph
  instance of the join-semilattice premise shape and a
  4-theorem example. Of 14 audited headline results: 10
  axiom-free, 4 on propext and quotient soundness only. The
  other 19 theorems are not in the audit print list; their
  axiom state is unknown from recorded evidence.
- On named premises: the general join-semilattice claim over
  all software states is a labeled premise; no theorem
  depends on it.
- Absent (by the repo's own scoping): merge behavior as the
  join of behaviors — derivation growth is proven one
  direction only. Controls: a recorded rejected mutation in
  the example. Gate: the recorded check log at the pin.

## software-is-more-traceable-than-you-think — pin 8f6a1280 (sweep re-census 2026-11-18; prior census pin 4420fb1e, superseded — the proof landed between the two pins)

- Proven in this repo: 43 theorems over 4 Lean files — the
  construction (20: losslessness on both faces of the fold,
  order independence in membership form, permutation and
  duplication independence, time independence in membership
  and reassignment form, retraction exactness on both faces
  and in recomputation form, all quantified over arbitrary
  node/event/time types and an arbitrary lifting, so free of
  any platform token — mechanically audited, 0 hits over 52
  platform words), the adversarial controls (12: three
  standing counterexamples proving duplication, order and
  retraction independence non-vacuous, plus the symbol-grain
  necessity control), the invoice example (5, incl. the
  route-free-receipt impossibility), and the bridge-repair
  example (6, incl. two-never-enough ambiguity and the exact
  three-bridge restore).
- On named premises: PREMISE (one) — returns_head's
  `contributed` restates the conclusion (it is fold_edges),
  and its witnessed-head hypothesis is not read by the proof
  term. The real-execution lifting (kernel-boundary sensing)
  is stated, never formalized; the store-level hypergraph and
  grain map are execution-verified over the frozen snapshot,
  not proven; the store carries no timestamps — exact time is
  batch-and-step-index, weaker than the claim's narrative.
- Controls in tree: the three *_claim_fails counterexamples
  in the Controls module; the range-ledger must-fail mutation
  control in the gate; grain and residue controls at concrete
  data.
- Gate state: green on the repo's committed receipts covering
  every Lean file with warnings as errors (proof/check.sh is
  the widened family gate with escape scan and axiom-subset
  check over proof/; the two examples' gates compile
  warnings-as-errors, range-ledger with a must-fail control).
  Printed axioms: propext and Quot.sound only. Caveats: the
  independent re-run was NOT EXECUTED (no Lean toolchain in
  the census environment) — carried as a verification-lane
  item; the examples gate lacks the escape scan and axiom
  check; one receipt line in examples/verification.txt (the
  invoice mutation control) has no corresponding in-tree
  gate step at this pin.
- Name verdict: proves a weaker statement — lossless,
  order/duplication/time-independent, retraction-exact,
  platform-free by universal quantification fold of an
  arbitrary witness stream. That real executions emit
  informative witnesses is the unformalized lifting premise;
  the store-level grain is executed, not proven. No
  dishonest overclaim: the readme's evidence states are
  accurate at the pin.

## idol-theses — pin d207be6e

- Proven: 35 native theorems (merge 20, fold 5, frontier 8
  plus 1 private helper, cited-registry 2), stated at the
  strengths the repo itself states. Its cited tranche carries
  9 family theses at their homes' strengths: 6 proven with
  side conditions, 1 refuted (per-execution dominance),
  coverage a premise.
- Absent: the 16-entry future-work remainder is stated as
  named work, not results — it includes 2 further refuted
  entries and premise, proposed, and claimed-not-proven
  entries, none counted as proved. Gate: the check script
  enforces full coverage and prints axioms for 14 theorems,
  but no recorded check log sits in the repo — a passing run
  at this pin is not evidenced in-repo. (Live head moved to
  ea7437ac after this census; re-census owed.)

## software-testing-is-redundant — pin 66f65b6f

- Proven: 22 theorems (foundation 10, copied unchanged;
  redundancy theory 10; executable decision 2), plus 15
  checked examples and a 4-theorem capacity example. Of 18
  printed theorems, 15 are axiom-free and 3 rest on the
  standard pair only.
- Refuted in-repo: the unrestricted slogan of its name, by a
  finite counterexample; the surviving general form is the
  novel-witness strict-growth theorem.
- Controls: the recorded gate log passes with both rejection
  controls; sums verified in the sweep.

## software-fuzzing-is-suboptimal — pin 18d9569b

- Proven: 15 theorems (dominance core 8, executable checker
  2, fixtures 5), plus 18 checked examples and a 5-theorem
  campaign example. Of 9 printed theorems: 4 axiom-free, 4 on
  propositional extensionality only, 1 on the standard pair.
- Refuted in-repo: blanket fixed-over-adaptive superiority,
  and its converse once the target is justified — the pair is
  the standing countermodel.
- Controls: the recorded gate log passes, including rejection
  of a proof hole, a false derivation, and four forbidden
  tokens. Gate-coverage note: the gate's token scan covers
  the three main modules; the example runs under its own
  runner.

## software-benchmarking-is-redundant-and-suboptimal — pin 4314a181

- Proven in source: 10 new theorems in the benchmark module,
  plus 17 checked examples and a 4-theorem campaign example;
  the 20 foundation theorems are byte-identical copies of the
  testing repo's at its pin, counted there.
- Refuted in-repo: strict savings composing under parallel
  span; equal output implying equal cost; one covered outcome
  making a flaky experiment redundant; zero-cost redundancy
  implying strict dominance.
- Absent: a recorded main-gate run — the check script stands
  in the tree with its controls, unrecorded, so the gate
  verdict at this pin is unknown from recorded logs and the
  readme's no-axioms statement for the new theorems is
  carried as claimed.

## idol — pin 561cf395 (proof-bearing content only)

- Proven: 7 theorems in one Lean file of the compiler tree
  (the elaboration frontier: certain and possible dominance
  exactness, axis composition, certificate soundness under a
  cover premise, closure least and union), zero sorry tokens
  by the sweep's scan; the file prints axioms for six of the
  seven when compiled.
- On named premises: the file's own header — qualification
  relative to the supplied catalogue, observer, and axes;
  measurement truth and envelope coverage external.
- Absent: a recorded check log covering the file — gate state
  unknown. The repo's checked-evidence tree is executed
  evidence at its own named pins (4,918 controls, in its own
  words not independent proved theorems), accounted in its
  annex and never in this ledger's proven column. (Live head
  moved to c8336841 after this census; re-census owed.)

## software-is-a-closed-loop — pin d8047804 (its own content)

- Proven: 3 theorems of its checked tuning example, all
  axiom-free, with the run recorded in the tree and a
  rejected control (advancing beyond the cap refused).
- Absent: nothing else is claimed — the theorem statements in
  its annex are other repos' results, counted at their homes.

## Watch addendum — 2026-11-18, the hourly re-synthesis watch

The scheduled watch ran the full procedure on its own reads:
the estate re-enumerated completely through the gh route at
565 repos, every head read individually (no read errors),
diffed against the first synthesis pins. Eleven repos had
moved (the nine original proof repos, idol, and one long-tail
repo that gained its first commit), seven were new (five new
proof repos, idol-theses, and this repo itself), none were
gone, and the paper source hash was unchanged at
f5d709743cac11d937e7716b7f39c056, so no paper re-sync was
owed. The estate-wide content sweep landed its re-censuses
in this repo during the same window; the watch verified them
against its own clones and counts and adds this addendum,
the annex watch deltas, and one corrected census row.

Defect-rule dispositions from the watch's same-method name
comparison (theorem names at the first census pin against
names at the live head, one mechanical method both times):

- The composable in-tree shrink is flagged, not absorbed:
  the whole-tree distinct name count fell (92 to 64) while
  the repo's own proven set grew (47 to 60, no own name
  lost). The fall is the removal of copied sibling modules,
  whose claims now stand at their stronger homes. This
  confirms the sweep's de-duplication disposition above.
- Two quantifiable names from the first pin are absent as
  theorem declarations at the new pin: the coverage name is
  now an abbreviation of the premise's mediation field, with
  new coverage theorems beside it, and the release-acceptance
  name was superseded by the named release forms. Flagged
  here; the sweep's refreshed row records the restructure.
- Ten optimality names from the first pin are absent as
  declarations at the sweep census pin; three still occur in
  the tree and seven do not occur at all, among them the
  earlier optimum-certificate forms, superseded in substance
  by the linked-certificate results the sweep's refreshed row
  records as discharged in their eligible specialization.
  The proven set as a whole grew (134 to 428 distinct names
  by the watch's method). Flagged here, not absorbed.
- No other refreshed repo lost a name: solvable gained three
  and lost none; frontier gained four and lost none; the
  four repos that stood at zero proven (certifiable, safe at
  head, regress, review) gained 7, 6, 131, and 82
  declarations respectively.
- Five repos moved past their sweep census pins during the
  window (optimality, composable, traceability, idol-theses,
  idol). The ledger rows for those repos stand at their
  census pins with the owed mark; the annex watch deltas
  record the watch's mechanical counts at the live heads.
  No pin moved without a ledger entry saying so.

## Watch refresh — 2026-11-18, the second hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and cloned every moved
proof repo at its fresh head. Counts below are the watch's
mechanical method, one method at both heads: every theorem
or lemma declaration in every Lean file, with distinct
short names compared between the last recorded head and
the fresh head. Placements stand at the census pins named
in each row; a full theorem-level re-census at each fresh
head is owed, except for this repo itself, re-censused in
full in its annex.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in every moved proof repo, and the idol repo's
  one Lean file is byte-identical between its pins. No
  regression is flagged.
- No pin moved without this ledger moving: every moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-quantifiable — fresh head d88acbdc (census
  pin f3709926). Proven by the watch method: 208
  declarations, 204 distinct names (was 189 and 185 at the
  last recorded head); 19 gained, none lost. The growth is
  the range example and one verification controls file.
  Premises, absent set, and controls stand as the sweep row
  records. Gate: as the sweep row records.
- software-optimality — enumeration head f759c33f, cloned
  head ec1eadda (census pin b52c3170). Proven by the watch
  method: 557 declarations, 536 distinct names at the
  cloned head (was 470 and 450 at the last recorded head);
  86 gained, none lost. Eight new root modules — a
  historical certificates group, an observation group, and
  a three-valued gate — beside the range example. Gate: a
  recorded check log stands at the cloned head, its axiom
  prints ending in the new observation modules, all
  standard or empty as printed there.
- software-is-composable — fresh head dce6564b (census pin
  a3058ba6). Proven: 70 declarations, 67 distinct names
  (was 66 and 64); 3 gained, none lost — the range example
  only. Premises, absent set, controls, and gate stand as
  the sweep row records.
- software-is-incrementally-certifiable — fresh head
  36901673 (census pin c9ffd49a). State change at the head:
  a full library now stands there — 88 declarations, 88
  distinct names (was 7) — where the sweep row recorded
  seven example theorems and the thesis absent as a
  library. Proven at the head, at the strength the tree
  states: the certification closure results in the repo's
  own claims table, marked proven there, with one union
  reading marked disproven. On named premises: the five
  premises the repo's own readme now names (required
  nonempty, nothing outside, no coverage gaps, an
  independence premise, a coverage premise). Absent: a
  full census of the new library in this ledger — owed.
  Gate: a recorded check log stands in the tree and ends
  in a pass.
- software-is-incrementally-safe — enumeration head
  dafd79a4, cloned head c9592e93 (head census pin
  8ad1dd26). State change at the head: a full library now
  stands there — 131 declarations, 129 distinct names at
  the cloned head (was 6 at the head) — where the sweep
  row recorded six example theorems and the former branch
  content unmerged. The repo's own claims table marks its
  first findings proven at the head, and its readme names
  the spec authority trust the checker does not derive.
  Absent: a full census of the new library in this ledger
  — owed; the audited-strength caveats of the sweep row
  stand until that census lands. Gate: no recorded check
  log stands in the head tree — a passing gate at this
  head is unrecorded.
- software-doesnt-have-to-regress — fresh head 858a85e3
  (census pin c36829da). Proven: 137 declarations (was
  131); 6 gained, none lost — the range example only.
  Gate: the recorded log stands as the sweep row records.
- software-doesnt-need-review — fresh head 1d504014
  (census pin 40b1e885). Proven: 85 declarations (was
  82); 3 gained, none lost — the range example only. The
  only sorry token and the only axiom declaration in the
  tree sit inside the planted controls that must fail, as
  the sweep row records. Gate: still unrecorded, as the
  sweep row records.
- software-is-solvable — fresh head 3053b78d (census pin
  5bbceee7). Proven: 54 declarations (was 51); 3 gained,
  none lost — the range example only. Gate: the recorded
  log stands as the sweep row records.
- software-frontier-is-solvable — fresh head 22418d56
  (census pin 6a41c7be). Proven: 66 declarations, 63
  distinct names (was 18); 45 gained, none lost. Five new
  library files stand beside the range example, so the
  growth is library growth. Gate: a recorded check log
  stands at the fresh head with axiom prints for the new
  modules, standard or empty as printed there.
- software-compilers-lose-info — fresh head 69358971
  (census pin f531e31a). Proven: 41 declarations (was
  37); 4 gained, none lost — the range example only.
  Gate: the recorded log stands as its row records.
- software-is-more-traceable-than-you-think — fresh head
  8f6a1280 (census pin 4420fb1e). Proven in this repo: 43
  declarations by the watch method (was 37 at the last
  recorded head); 6 gained, none lost — the range example
  only. Absent: the thesis itself, still claimed and not
  proven in-repo, as its row records.
- idol-theses — fresh head c443ebe1 (census pin
  d207be6e). Proven: 87 declarations, 75 distinct names
  (was 35 and 23 at the last recorded head); 52 gained,
  none lost — one new solver dominance file. Gate: still
  no recorded check log in the repo, as its row records.
- software-testing-is-redundant — fresh head 18feb7ab
  (census pin 66f65b6f). Proven: 30 declarations (was
  26); 4 gained, none lost — the range example only.
  Gate: the recorded log stands as its row records.
- software-fuzzing-is-suboptimal — fresh head 6ed7a596
  (census pin 18d9569b). Proven: 27 declarations (was
  21); 6 gained, none lost — the range example only.
  Gate: the recorded log stands as its row records.
- software-benchmarking-is-redundant-and-suboptimal —
  fresh head a85286ac (census pin 4314a181). Proven in
  source: 37 declarations (was 34); 3 gained, none lost
  — the range example only. Gate: still unrecorded for
  the main gate, as its row records.
- idol — enumeration head ef3dbcfa (census pin 561cf395,
  proof-bearing content only). Proven: unchanged — the
  one Lean file is byte-identical at both pins, 4,733
  bytes, still carrying its 7 theorems on the premises
  its row records. Gate: unknown, as its row records.
- software-is-a-closed-loop — new census pin d558669b.
  Proven: 11 theorems of its own (was 3): the first
  example's three, axiom-free, plus the range example's
  eight, six on subsets of the standard axioms, one
  axiom-free, and one with no printed axiom line in the
  recorded transcript, its axiom state unrecorded.
  Controls: the recorded transcript's rejected control
  stands beside the first example's. Gate: the recorded
  verification transcript in the tree.

## Watch refresh — 2026-11-18, the third hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and cloned every moved
proof repo at its fresh head. Counts below are the watch
mechanical method, one method at both heads: every theorem
or lemma declaration in every Lean file, with distinct
short names compared between the last recorded head and
the fresh head. Placements stand at the census pins named
in each row; a full theorem-level re-census at each fresh
head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in every moved proof repo: the optimality repo
  gained 52 names, the safe repo gained 17, the composable
  repo held its set, the idol frontier file is unchanged
  while its release tools files gained nine declarations
  with no name lost, and this repo's eleven names stand
  unchanged. No regression is flagged.
- No pin moved without this ledger moving: every moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-optimality — fresh head 95df5fb7 (census
  pin b52c3170). Proven by the watch method: 684
  declarations, 588 distinct names (was 557 and 536 at the
  last recorded cloned head); 52 gained, none lost.
  Eleven new Lean files: a root module on the executable
  incremental form, and composition developments on axiom
  audit, exhaustive edits, identity and representation,
  and incremental selection, with a portable evidence
  folder. Premises and absent set stand as the sweep row
  records. Gate: a recorded check log stands in the tree
  at the fresh head.
- software-is-composable — fresh head 7b174646 (census
  pin a3058ba6). Proven: 70 declarations, 67 distinct
  names, unchanged from the last recorded head; no name
  gained and none lost. The movement is a dependency
  re-pin in the lake file and its manifest, with a readme
  update; no library source file changed. Premises,
  absent set, controls, and gate stand as the sweep row
  records.
- software-is-incrementally-safe — fresh head 23a22552
  (census pin 8ad1dd26). Proven by the watch method: 148
  declarations, 146 distinct names (was 131 and 129 at
  the last recorded cloned head); 17 gained, none lost.
  The growth stands in the model, cone, check, and
  ordered increment modules, with one new audit file.
  The audited-strength caveats of the sweep row stand
  until a full census of the library lands. Gate: no
  recorded check log stands in the head tree, as the
  sweep row records for the earlier head.
- idol — fresh head 2f44b4fe (census pin 561cf395,
  proof-bearing content only). Proven: the frontier file
  is unchanged — byte-identical at both pins, 4,733
  bytes, still carrying its 7 theorems on the premises
  its row records. A second development in the release
  tools folder, landed after the census pin and not in
  the sweep census, grew in this window: its retention
  file carries 20 declarations (was 16 at the last
  recorded head; 4 gained, none lost) and a new
  qualification file carries 5, with print-axioms lines
  for all five in the file and no sorry token in either
  file by the watch scan. Gate: unknown for the frontier
  file, as its row records, and unknown for the release
  tools files — no recorded check log covering them was
  read in this watch. A full census of the release tools
  development is owed.
- software-is-a-closed-loop — fresh head 98761a1a
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the census pin and at the fresh
  head, which is the head the second watch landed; the
  commits between them carry no Lean change. Controls
  and gate stand as the second watch row records.

## High-impact proofs addendum — 2026-11-18

Gate verdicts executed cold by the high-impact proofs
lane, each the repo's own gate at the pin named. They
replace the unknown or stale-pin gate states in the
rows above until the next census carries them into
the rows themselves. Full record: the high-impact
proofs lane record of 2026-11-18 in the workspace
research folder.

- idol — the release tools development the watch
  addendum above left at gate unknown is now gated.
  At head 294c31b8 the repo's own release
  qualification gate ran end to end: it fetches
  software-is-quantifiable at c90ed607 and
  software-optimality at 2bd3b419 (verifying each
  fetched head equals its pin), builds both,
  compiles the retention file, then compiles the
  release qualification file against them, warnings
  as errors throughout, with zero error, warning,
  or sorry lines. The qualification file's five
  theorems carry their full audit: one depends on
  no axioms; the other four depend only on propext
  and Quot.sound. With the release preparation
  lane's standalone runs, all four Lean files in
  the repo stand verified at this head.
- software-frontier-is-solvable — gate GREEN at
  22418d56.
- software-testing-is-redundant — gate GREEN at
  18feb7ab.
- software-fuzzing-is-suboptimal — gate GREEN at
  6ed7a596.
- software-benchmarking-is-redundant-and-suboptimal
  — gate GREEN at a85286ac, its first recorded main
  gate run.
- software-is-solvable — gate GREEN at 3053b78d
  (root-module coverage, as its gate defines it).
- software-compilers-lose-info — gates GREEN at
  69358971, root and examples; the independent
  re-check its landing record owed.
- software-is-more-traceable-than-you-think —
  gates GREEN at 8f6a1280, proof and examples; the
  proof gate is the widened every-file form and its
  axiom subset check passed on propext and
  Quot.sound.
- idol-semi and semi-persistent — gate at 508d7c66
  still UNVERIFIED. The re-run is blocked on the
  host disk quota: the Lean 4.35.0 toolchain
  archive is staged, but its extraction was
  refused at 174 MB (error 122, disk quota
  exceeded). The run resumes at the extraction
  step when quota lands.

## Watch refresh — 2026-11-18, the fourth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, cloned the moved safe
repo at its fresh head, and read the idol tree in full at
its fresh head. Counts below are the watch mechanical
method, one method at both heads: every theorem or lemma
declaration in every Lean file, with distinct short names
compared between the last recorded head and the fresh
head. Placements stand at the census pins named in each
row; a full theorem-level re-census at each fresh head
is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in every moved proof repo: the safe repo
  gained three names, the idol repo's recorded files are
  byte-identical while a new file added ten declarations,
  and this repo's eleven names stand unchanged. The safe
  repo's premise set shrank by discharge — its string cone
  hypothesis is proven in this window, per its merge
  record — which is a strengthening, not a regression.
  No regression is flagged.
- No pin moved without this ledger moving: every moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-incrementally-safe — fresh head 97e55d28
  (census pin 8ad1dd26). Proven by the watch method: 151
  declarations, 149 distinct names (was 148 and 146 at
  the last recorded head); 3 gained, none lost. The
  growth is one new module on the natural-number text
  representation, one audit module, and one example file.
  On named premises: the string cone hypothesis is
  discharged by the new module's injectivity proof, as
  its merge record states; the audited-strength caveats
  of the sweep row stand until a full census of the
  library lands. Gate: no recorded check log stands in
  the head tree — a passing gate at this head is
  unrecorded.
- idol — fresh head 107e52a9 (census pin 561cf395,
  proof-bearing content only). Proven: the frontier file
  is unchanged — byte-identical at both pins, 4,733
  bytes, still carrying its 7 theorems on the premises
  its row records; the release tools files are
  byte-identical at both heads (retention 20
  declarations, qualification 5), and their gate verdict
  stands in the high-impact addendum above at its named
  pin. A third development stands new at the fresh head:
  a history file in the solver benchmarks incidence
  folder carrying 10 declarations on witnessed derivation
  histories and finite solver costs, no sorry token by
  the watch scan. Gate: unknown for the new file — no
  recorded check log covering it was read in this watch.
  A full census of the new development is owed.
- software-is-a-closed-loop — fresh head 65914d1a
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which stands one ledger addendum commit
  past the head the third watch recorded; the commit
  between them carries no Lean change. Controls and gate
  stand as the second watch row records.

## Watch refresh — 2026-11-18, the fifth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, read the idol tree in
full at its fresh head, and cloned the semi repo at its
fresh head. Evidence below rests on tree reads at both
heads of each moved proof repo: blob identity file by
file, not counts alone. Placements stand at the census
pins named in each row; a full theorem-level re-census
at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. Every Lean file in both moved
  proof repos is byte-identical between the last recorded
  head and the fresh head, so no name was lost in either;
  this repo's eleven names stand unchanged. No regression
  is flagged.
- No pin moved without this ledger moving: every moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- idol — fresh head 586ff5a1 (census pin 561cf395,
  proof-bearing content only). Proven: unchanged — all
  five Lean files stand at the same blobs at both heads:
  the frontier file with its 7 theorems on the premises
  its row records, the release tools files with their 20
  and 5 declarations, and the solver history file with
  its 10, beside the proof data sample that remains test
  data. The movement between the heads is compiler and
  gate work: 3 files added, 1 removed, 23 changed, none
  of them Lean. Gate: the release tools verdict stands
  in the high-impact addendum above at its named pin;
  the solver history file's gate remains unknown, as
  its row records.
- idol-semi — fresh head 238717ba (census pin 508d7c66).
  Proven: unchanged — all 156 Lean files are byte-identical
  between the census pin and the fresh head, and no Rust
  file changed, so the congruence closure, matching, and
  fidelity development and the Rust verification stand
  exactly as the sweep row records. Counted at the fresh
  head by the watch method: 1,865 declarations, 1,736
  distinct short names, no sorry token, 424 print-axioms
  lines; that mechanical count runs lower than the sweep
  census's fuller count of the same content, and the
  content identity is the governing evidence. The
  movement is ten added files of analysis and parity
  tooling. Absent: a recorded check log still stands
  nowhere in the tree, so a passing gate at the fresh
  head remains claimed, not proven; the gate re-run at
  the shared pin remains blocked on host disk quota, as
  the high-impact addendum records. Placement note:
  semi-persistent did not move and still stands at
  508d7c66, so the two repos no longer share one head;
  their proof content remains identical, and this row
  now tracks the semi repo's head, with the mirror's
  head recorded here until it moves.
- software-is-a-closed-loop — fresh head 68630ed9
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the fourth watch landed;
  the commits between them are that watch's placement,
  ledger, and pins commits and carry no Lean change.
  Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-18, the sixth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the one other
moved repo by tree at its fresh head. Evidence below rests
on the tree and commit reads at both heads of the moved
proof repo: no Lean file changed between them. Placements
stand at the census pins named in each row; a full
theorem-level re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 97d26e80
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the fifth watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.

## Watch refresh — 2026-11-18, the seventh hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree reads at both heads of the moved proof repo: no Lean
file changed between them. Placements stand at the census
pins named in each row; a full theorem-level re-census
at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head b07314d3
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the sixth watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-18, the eighth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually (four transport failures re-read to
matching heads), and read the moved repos by tree at their
fresh heads. Evidence below rests on the tree and commit
reads at both heads of the moved proof repo: no Lean file
changed between them. Placements stand at the census pins
named in each row; a full theorem-level re-census at each
fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 22957bf6
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the seventh watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The three other moved repos this watch, the compiler port,
the relay, and the sites repo, are not proof repos and
carry no ledger rows: all three were read by tree at their
fresh heads, no proof-assistant source was found in any of
them, and they remain proof-free by the named check, as
their census entries record.

## Watch refresh — 2026-11-18, the ninth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them. Placements stand
at the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 2fe3ad5f
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the eighth watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.

## Watch refresh — 2026-11-18, the tenth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them. Placements stand
at the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 10a786e7
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the ninth watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-18, the eleventh hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them. Placements stand
at the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head ba9a0763
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the tenth watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-18, the twelfth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually (three first reads re-read individually:
two to matching heads, one to its recorded empty state),
and read the moved repos by tree at their fresh heads.
Evidence below rests on the tree and commit reads at both
heads of the moved proof repo: no Lean file changed
between them. Placements stand at the census pins named
in each row; a full theorem-level re-census at each fresh
head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 8050b17f
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the eleventh watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.

## Watch refresh — 2026-11-18, the thirteenth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them, and the theorem
name set is identical at both heads. Placements stand at
the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 6a0c90d3
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the twelfth watch landed;
  the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-18, the fourteenth hourly re-synthesis watch

The watch re-enumerated the estate at 565 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them, and the theorem
name set is identical at both heads. Placements stand at
the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 97920cbd
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the thirteenth watch
  landed; the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.

## Watch refresh — 2026-11-18, the fifteenth hourly re-synthesis watch

The watch re-enumerated the estate at 566 repos, every head
read individually (one transport failure re-read to its
recorded empty state), read the moved repos by tree at their
fresh heads, and censused the one new repo in full at its
head. Evidence below rests on the tree and commit reads at
both heads of the moved proof repo: no Lean file changed
between them, and the theorem name set is identical at both
heads. Evidence for the new repo rests on its full census in
its annex. Placements stand at the census pins named in each
row; a full theorem-level re-census at each fresh head is
owed, except for the new repo, censused in full at its head
in this pass.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. The new proof repo enters with
  its full set at its first pin; it has no earlier set to
  shrink against. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass,
  and the new proof repo's row is added below in this same
  pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head fe96c58f
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the fourteenth watch
  landed; the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

New row, at its census pin, which is its head:

- software-profiling-is-synthesizable — pin a53c4bf5.
  Proven: 20 theorem declarations across three Lean files
  — the measurement core (baseline independence, finiteness
  derived from the contract, compounding, distinctness,
  incremental accounting, idempotence, elimination, the
  optimum and solved results, and falsification), the
  completion results (sufficiency, freedom at one
  coordinate, standing carried under subsets, invariance
  under relabeling, parametric verdicts, and the swapping
  of commuting effects), one grid length helper, and three
  adversarial controls. Of the 19 declarations the recorded
  log prints, 9 depend on no axioms, 3 on propositional
  extensionality only, and 7 on the standard pair; the
  helper is not printed in the log, so its axiom state is
  unrecorded there. On named premises: one premise of the
  model — facts about a runtime or a job enter only as
  certified witness states; the Lean development carries
  no premise of its own. Absent, at the repo's own states:
  the visibility vector has no formalization yet
  (proposed), the campaign bridge is proposed semantics
  discharged per campaign, and re-solving over a sequence
  of cost assignments is open. Controls in tree: the three
  adversarial controls, each a concrete counterexample
  proving its weakened condition load bearing. Gate: the
  check script stands in the tree and the recorded check
  log at the pin ends in its axiom subset check passing —
  green on the recorded log; this watch ran no build.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-18, the sixteenth hourly re-synthesis watch

The watch re-enumerated the estate at 566 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them, and the theorem
name set is identical at both heads. Placements stand at
the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head c0356504
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the fifteenth watch
  landed; the commits between them are that watch's
  census, annex, placement, ledger, and pins commits and
  carry no Lean change. Controls and gate stand as the
  second watch row records.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.

## Watch refresh — 2026-11-18, the seventeenth hourly re-synthesis watch

The watch re-enumerated the estate at 566 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them, and the theorem
name set is identical at both heads. Placements stand at
the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head a7be4e02
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the sixteenth watch
  landed; the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-18, the eighteenth hourly re-synthesis watch

The watch re-enumerated the estate at 566 repos, every head
read individually with no errors, and read the moved repos
by tree at their fresh heads. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo: no Lean file changed between them, and the theorem
name set is identical at both heads. Placements stand at
the census pins named in each row; a full theorem-level
re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 30513d21
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the seventeenth watch
  landed; the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.

## Watch refresh — 2026-11-19, the nineteenth hourly re-synthesis watch

The watch re-enumerated the estate at 566 repos, every head
read, and read the moved repos by tree at their fresh
heads. Evidence below rests on the tree and commit reads
at both heads of the moved proof repo: no Lean file
changed between them, and the theorem name set is
identical at both heads. Placements stand at the census
pins named in each row; a full theorem-level re-census
at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass.
  No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 2aac8180
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the eighteenth watch
  landed; the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record.

## Watch refresh — 2026-11-19, the twentieth hourly re-synthesis watch

The watch re-enumerated the estate at 567 repos, every head
read individually with no errors, read the moved repos by
tree at their fresh heads, and censused the one new repo in
full at its head. Evidence below rests on the tree and
commit reads at both heads of the moved proof repo: no Lean
file changed between them, and the theorem name set is
identical at both heads. Evidence for the new repo rests on
its full census in its annex. Placements stand at the census
pins named in each row; a full theorem-level re-census at
each fresh head is owed, except for the new repo, censused
in full at its head in this pass.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files
  are unchanged between the last recorded head and the
  fresh head, and its theorem name set is identical at
  both heads, so no name was lost; this repo's eleven
  names stand unchanged. The new proof repo enters with
  its full set at its first pin; it has no earlier set to
  shrink against. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass,
  and the new proof repo's row is added below in this same
  pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head ec47f7e
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the nineteenth watch
  landed; the commits between them are that watch's annex,
  placement, ledger, and pins commits and carry no Lean
  change. Controls and gate stand as the second watch
  row records.

New row, at its census pin, which is its head:

- software-losses-are-compositional — pin d1159dc1.
  Proven: 17 theorem declarations across two Lean files —
  the composition core (additive recording, compositional
  projection in its two part and three way forms, the gap
  reading, composition of loss freeness in its two part
  and three way forms, compounding, monotonicity,
  localization, finiteness derived from the contract, and
  method soundness per axis and over all axes), two helper
  results carrying the additive and finiteness theorems,
  and three adversarial controls. Of the 15 declarations
  the recorded log prints, 3 depend on no axioms, 4 on
  propositional extensionality only, 7 on the standard
  pair, and 1 on the full standard set; the two helpers
  are not printed in the log, so their axiom states are
  unrecorded there. On named premises: two premises of
  the model — record fidelity, which is a concrete
  campaign's evidence, and re-measure, the model flipping
  no beat cell; the Lean development carries no premise
  of its own. Absent, at the repo's own states: richer
  derivations, weighted axes, and continuous axes are
  proposed, none formalized. Controls in tree: the three
  adversarial controls, each a proved negation over a
  concrete counterexample proving its weakened condition
  load bearing. Gate: the check script stands in the tree
  and the recorded check log at the pin ends in its axiom
  subset check passing — green on the recorded log; this
  watch ran no build.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found, and it remains proof-free by the
named check, as its census entry records.
## Watch refresh — 2026-11-19, the twenty-first hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head
read individually with no errors, read the moved repos by
tree at their fresh heads, re-censused the one moved proof
repo whose content changed in full at its fresh head, and
censused the one new proof repo in full at its head.
Evidence below rests on the tree and commit reads at both
heads of the moved proof repos, on the full file reads at
both heads of the losses repo, and on the new repo's full
census in its annex. Placements stand at the census pins
named in each row; a full theorem-level re-census at each
fresh head is owed, except for the losses repo, re-censused
in full at its fresh head in this pass, and the new repo,
censused in full at its head in this pass.

Defect-rule dispositions for this refresh:

- No proven set shrank. The losses repo gained one name
  and lost none between its census pin and its fresh
  head, and this repo's Lean files are unchanged between
  the last recorded head and the fresh head, with its
  theorem name set identical at both heads, so no name
  was lost; this repo's eleven names stand unchanged.
  The new proof repo enters with its full set at its
  first pin; it has no earlier set to shrink against. No
  regression is flagged.
- No pin moved without this ledger moving: both moved
  proof repos have their rows restated below in this
  same pass, and the new proof repo's row is added below
  in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head f2c3b6d6
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the twentieth watch
  landed; the five commits between them are that watch's
  census, annex, placement, ledger, and pins commits and
  carry no Lean change. Controls and gate stand as the
  second watch row records.
- software-losses-are-compositional — new census pin
  12ee66e9 (was d1159dc1). Proven: 18 theorem
  declarations across two Lean files (was 17) — one
  gained, none lost: the tightness of the compounding
  bound, standing beside the compounding result it
  sharpens, on the standard pair in the recorded log.
  The recorded check log at the new pin prints 16
  declarations (was 15): 3 depend on no axioms, 4 on
  propositional extensionality only, 8 on the standard
  pair, and 1 on the full standard set; the two helpers
  remain unprinted, their axiom states unrecorded there.
  The controls file is byte-identical at both pins, so
  the three adversarial controls stand unchanged. On
  named premises and absent items: unchanged from the
  twentieth watch row — record fidelity and re-measure
  carried as premises, richer derivations, weighted
  axes, and continuous axes proposed. Gate: the recorded
  check log at the new pin ends in its axiom subset
  check passing — green on the recorded log; this watch
  ran no build.

New row, at its census pin, which is its head:

- software-persistence-is-minimal — pin eb01cf2e.
  Proven: 53 theorem declarations across three Lean
  files — the core (derivability closed under recorded
  edges and monotone in the store and the edges,
  elimination of the derivable with the derivable set
  unchanged, certificate run and checker soundness with
  monotonicity and composition, the candidate count as
  a computed power, cost additivity, the domination
  bridge, minimality checker soundness, domination
  irreflexive and transitive, minima by construction
  with existence in any nonempty candidate list,
  domination lifting and whole minima having minimum
  parts, and semi-persistent readability with version
  cost splitting and the kept premise), the controls
  file's general no-derivation result, and the synthesis
  file (the losses core mirrored and discharged,
  baseline independence and least cost proved here, fold
  membership and retraction proved here, the
  only-carrying recovery limit, and the joined theorem
  assembling the method). Of the 52 declarations the
  recorded log prints, 11 depend on no axioms, 19 on
  propositional extensionality only, and 22 on the
  standard pair; the sum append helper is not printed in
  the log, so its axiom state is unrecorded there. On
  named premises: two campaign premises (edge
  faithfulness and cost fidelity), and inside the joined
  theorem's antecedent five premises labeled by their
  sources (coverage, spec authority, the general
  join-semilattice claim, witness faithfulness, and
  record fidelity), with the remaining family results
  carried as restated hypotheses of that theorem.
  Absent, at the repo's own states: candidate
  completeness and the end-to-end methodology are
  proposed, and the profiling development's visibility
  vector and re-solving over cost sequences are
  inherited as open. Controls in tree: four adversarial
  controls, each a proved negation over concrete numbers
  proving its weakened condition load bearing. Gate: the
  check script stands in the tree and the recorded check
  log at the pin ends in its axiom subset check passing
  — green on the recorded log; this watch ran no build.

The two other moved repos this watch, the compiler port
and the relay, are not proof repos and carry no ledger
rows: both were read by tree at their fresh heads, no
proof-assistant source was found in either, and they
remain proof-free by the named check, as their census
entries record. The second new repo this watch, the
bidirectional repo, stands empty at its first
enumeration, carries no provable results, and carries
no ledger row; it enters this ledger on the enumeration
that first sees its content.

## Watch refresh — 2026-11-19, the twenty-second hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head
read individually with no errors, read the moved repos by
tree at their fresh heads, read every Lean file of the two
moved library proof repos in full at both heads, and
censused the one newly proof-bearing repo in full at its
head. Evidence below rests on the tree and file reads at
both heads of the moved proof repos and on the new repo's
full census in its annex. Placements stand at the census
pins named in each row; a full theorem-level re-census at
each fresh head is owed, except for the new repo, censused
in full at its head in this pass.

Defect-rule dispositions for this refresh:

- No proven set shrank. The theses repo gained fourteen
  names and lost none between its last recorded head and
  its fresh head, the frontier repo gained thirty-eight
  and lost none, and this repo's Lean files are unchanged
  between the last recorded head and the fresh head, with
  its theorem name set identical at both heads, so no name
  was lost; this repo's eleven names stand unchanged. The
  newly proof-bearing repo enters with its full set at its
  first pin; it has no earlier set to shrink against. No
  regression is flagged.
- No pin moved without this ledger moving: every moved
  proof repo has its row restated below in this same pass,
  and the newly proof-bearing repo's row is added below in
  this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 3baddd44
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the twenty-first watch
  landed; the six commits between them are that watch's
  census, re-census, delta, placement, ledger, and pins
  commits and carry no Lean change. Controls and gate
  stand as the second watch row records.
- idol-theses — fresh head b6e810c5 (census pin
  d207be6e). Proven: 101 declarations, 82 distinct names
  (was 87 and 75 at the last recorded head); 14 gained,
  none lost. The growth is the synthesis pass landing in
  this repo: a synthesis module of composition glue (7)
  and a compose module carrying the composer theorem,
  its lemmas, and one control (7), beside a third cited
  group that grows the cited tranche from seventeen
  theses to thirty-four at the pins the pass read back,
  and a campaign document. The audit file prints axioms
  for the fourteen new theorems. Premises and absent set
  stand as the sweep row records, with the pass's
  composed claims not landed carried in the future work
  file at proposed state. Gate: still no recorded check
  log in the repo, as its row records; the check script
  now compiles both new modules.
- software-frontier-is-solvable — fresh head cdeae4ad
  (census pin 6a41c7be). Proven: 104 declarations, 94
  distinct names (was 66 and 63 at the last recorded
  head); 38 gained, none lost — one new search module
  proving the general search layer of the bounded
  technique: join laws, least saturation, compounding
  and tightening bounds, the exact nondominated
  qualified frontier, premise-tracked speculation, and
  order-independent weighting with a sound trace, beside
  three new controls proved as negations. Premises stand
  as its row records; the finiteness of the qualified
  space is cited from the quantifiable home, not
  re-proved. Gate: a recorded check log stands at the
  fresh head, printing axioms for 23 of the 38 new
  declarations, all standard or empty as printed there;
  the other 15 are unprinted, their axiom states
  unrecorded there.

New row, at its census pin, which is its head:

- software-is-bidirectional — pin b14fc92b. Proven: 73
  theorem declarations across three Lean files — the
  core model (the hyperlattice of states up to
  equivalence, derivability closure, the analysis and
  synthesis maps with both round trips and the
  reengineering round trip, independent derivability
  under a complete recording, smallness against the
  power of two, premise-cone speculation, bounds over
  candidate lists attained and compounding and
  tightening under joins with certified optima, the
  finite candidate grid, and the named measures with
  their characterizations, including the exact
  suboptimality forms for scheduling, venue, and test
  sets), the composition (the losses core mirrored and
  discharged, the persistence elimination result and
  the recorded-state lattice discharged in this
  vocabulary, and the joined theorem assembling the
  method), and four standing controls. Of the 74
  declarations the recorded log prints — the 73
  theorems plus the optimum decision definition — 19
  depend on no axioms, 27 on propositional
  extensionality only, and 28 on the standard pair, with
  no classical choice anywhere. On named premises: the
  joined theorem's six (contract fidelity, record
  fidelity, re-measure, coverage, spec authority, and
  witness faithfulness), with the family's remaining
  results carried as restated hypotheses at their homes'
  pins. Absent, at the repo's own states: the content
  bound under injectivity, the visibility vector, and
  time-varying re-solving are proposed; a ten-entry gap
  register stands in its specification, each gap owned
  with its closing route. Controls in tree: the four
  adversarial controls, each a proved negation over a
  concrete counterexample proving its weakened condition
  load bearing. Gate: the check script stands in the
  tree in the family gate form and the recorded check
  log at the pin ends in its axiom subset check passing
  — green on the recorded log; this watch ran no build.

The three other moved repos this watch, the library, the
relay, and the sites repo, are not proof repos and carry
no ledger rows: all three were read by tree at their fresh
heads, no proof-assistant source was found in any of them,
and they remain proof-free by the named check, as their
census entries record.
## Watch refresh — 2026-11-19, the twenty-third hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head
read individually with no errors, read the moved repos by
tree at their fresh heads, and censused the one newly
proof-bearing repo in full at its head. Evidence below rests
on the tree reads at both heads of the moved repos, on the
blob comparison of this repo's two Lean files between its
heads, and on the new repo's full census in its annex.
Placements stand at the census pins named in each row; a
full theorem-level re-census at each fresh head is owed,
except for the new repo, censused in full at its head in
this pass.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are
  byte-identical between the last recorded head and the
  fresh head, with its theorem name set identical at both
  heads, so no name was lost; this repo's eleven names
  stand unchanged. The newly proof-bearing repo enters
  with its full set at its first pin; it has no earlier
  set to shrink against. No regression is flagged.
- No pin moved without this ledger moving: the one moved
  proof repo has its row restated below in this same pass,
  and the newly proof-bearing repo's row is added below in
  this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head b0fd67d9
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the twenty-second watch
  landed; the five commits between them are that watch's
  census, annex, placement, ledger, and pins commits and
  carry no Lean change. Controls and gate stand as the
  second watch row records.

New row, at its census pin, which is its head:

- idol-lib — pin ad22a681 (proof-bearing content only,
  inside the campaign folder of the library ports repo).
  Proven: 38 theorem declarations across two Lean files —
  the campaign kernel (25: reconstruction injectivity
  under a round trip and the history obstruction, intent
  axes under a factorization, simulation and safety
  transfer, the joined effect bound, the rewrite
  composer for contract and budget, the commuting swap,
  idempotence composing under commutation with the
  unconditional reading disproven by a three-state
  counterexample, the keyed ledger quartet, weighted cost
  monotonicity and the robust economic bound, contract
  cover soundness, hypergraph derivation soundness and
  witness reuse under retention, and the finite minimum
  with feasibility and declared-universe optimality) and
  the atlas proofs (13: gathering and the batch composer,
  the deduplicated work lower bound, frontier exactness,
  sufficient state and the distinguishing lower bound, the
  score update and break-even laws, the Adler scan laws,
  and the Bellman lower bound with its minimax
  certificate) — plus six witness examples checked by
  decision over the two recorded snapshots, counted as
  checked examples, not theorems. Of the kernel's 25, the
  recorded receipt prints all: 15 depend on no axioms and
  10 on propositional extensionality only. Of the atlas
  file's 13, the recorded check text prints 10: 2 on no
  axioms, 1 on propositional extensionality only, 5 on
  propositional extensionality and quotient soundness, and
  2 on the full standard set; the other three (gathering,
  the shifted scan, the Bellman lower bound) are unprinted
  there, their axiom states unrecorded. On named premises:
  the repo's own trust boundary stands as the campaign's
  premise — the theorems concern an abstract model, and
  every concrete application owes the named hypotheses
  plus an implementation-to-model refinement witness.
  Absent: that refinement — no theorem connects the model
  to the library's ports or the measured systems; the
  wider campaign program (the Ocean execution model
  carried end to end, the public surface) stands proposed
  at the repo's own states, and the atlas measurements
  stand as measured and constructed evidence with their
  unmeasured cells recorded. Controls in tree: five
  recorded negative controls for the kernel gate, each
  rejected as required (an empty proof file, a missing
  effect-bound family, a missing axiom audit, an admitted
  proof hole, and a custom axiom asserting falsity), beside
  the atlas gate's own controls and receipt-mutation
  checks in the recorded campaign log. Gate: the kernel
  gate is green on its recorded receipt at the pin —
  kernel-checked, exit 0 — and this census verified the
  receipt's source and checker hashes against the tree at
  the pin; the atlas gate stands in the tree in the form
  its annex records, with a recorded campaign check log.
  This watch ran no build.

The three other moved repos this watch, the compiler port,
the relay, and the sites repo, are not proof repos and carry
no ledger rows: all three were read by tree at their fresh
heads, no proof-assistant source was found in any of them,
and they remain proof-free by the named check, as their
census entries record.

## Watch refresh — 2026-11-19, the twenty-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head
read individually with no errors, read the moved repos by
tree at their fresh heads, and re-censused the one moved
proof repo with new proof content in full at its head.
Evidence below rests on the tree reads at both heads of
the moved repos, on the blob comparison of this repo's two
Lean files between its heads, and on the library repo's
full re-census in its annex, including the firsthand hash
verification recorded there. Placements stand at the
census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are
  byte-identical between the last recorded head and the
  fresh head, so its eleven names stand unchanged. The
  library repo's proven set grew from thirty-eight
  theorems to sixty-five: its three earlier Lean files
  are byte-identical at the fresh head, so no name was
  lost, and the added file carries twenty-seven new
  names. No regression is flagged.
- No pin moved without this ledger moving: both moved
  proof repos have their rows restated below in this
  same pass, and the library repo's census pin moves in
  this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 91adf89e
  (census pin d558669b). Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at the
  fresh head, which is the head the twenty-third watch
  landed; the five commits between them are that watch's
  census, annex, placement, ledger, and pins commits and
  carry no Lean change. Controls and gate stand as the
  second watch row records.
- idol-lib — new census pin 4dee2311, which is its fresh
  head. Proven: 65 theorem declarations across three
  Lean files — the campaign kernel (25) and the atlas
  proofs (13) unchanged at the axiom states their row
  above records, beside the six witness examples checked
  by decision, and a new Pareto package (27) proving
  Pareto unimprovability in its abstract models: the
  strict domination relation, the global witness with
  its finite, cone, normalization, and cell-cover forms,
  the weighted score results, the standing
  counterexamples (a zero-weight scalar minimum that is
  not Pareto optimal, an omitted alternative, and
  component optima that need not compose), bounded
  uncertainty, and the retention model with its concrete
  optimal instance. Of the new package's 27, its recorded
  receipt prints all: 14 depend on no axioms, 2 on
  propositional extensionality only, 10 on propositional
  extensionality and quotient soundness, and 1 on the
  full standard set. On named premises: the package's
  own scope — natural-valued abstract models only, no
  software or measured-cost refinement proved there —
  beside the campaign's standing trust boundary from its
  row above. Absent: that refinement, unchanged, and, at
  the repo's own state, actual-software release admission
  under the new Pareto requirement, which stands open
  with the release command refusing it. Controls in
  tree: the kernel gate's five recorded negative
  controls and the atlas gate's controls stand as their
  row above records, and the new package carries five
  recorded negative controls of its own, each rejected
  as required (an empty proof file, a missing robust
  scenario family, a missing axiom audit, an admitted
  proof hole, and a custom axiom). Gate: the new
  package's recorded receipt at the pin is
  kernel-checked with exit 0, and this watch verified
  its source and checker hashes against the tree at the
  pin firsthand; the kernel receipt was re-recorded in
  this window at a fresh time stamp with the same source
  and checker hashes and the same kernel-checked status.
  This watch ran no build.

The one other moved repo this watch, the compiler port,
is not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant source
was found in it, and it remains proof-free by the named
check, as its census entry records.

## Watch refresh — 2026-11-19, the twenty-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 52daadf5 (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the twenty-fourth watch landed; the five commits between them are that watch's re-census, delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The two other moved repos this watch, the compiler port and the relay, are not proof repos and carry no ledger rows: both were read by tree at their fresh heads, no proof-assistant source was found in either, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-19, the twenty-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head. Evidence below rests on the tree reads at both heads of the moved repo and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 3d3bffdd (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the twenty-fifth watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-19, the twenty-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 4b801137 (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the twenty-sixth watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The three other moved repos this watch, the compiler port, the relay, and the sites repo, are not proof repos and carry no ledger rows: all three were read by tree at their fresh heads, no proof-assistant source was found in any of them, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-19, the twenty-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually. Six first reads failed on transport stream errors; each was re-read individually and matched its last recorded head, or its recorded empty state, so the final reads carry no errors. The moved repos were read by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head b2a74028 (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the twenty-seventh watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-19, the twenty-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually, no read errors. The moved repos were read by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 47a30a1c (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the twenty-eighth watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The two other moved repos this watch, the compiler port and the relay, are not proof repos and carry no ledger rows: both were read by tree at their fresh heads, no proof-assistant source was found in either, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-19, the thirtieth hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually, no read errors. The moved repos were read by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 4e9d508a (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the twenty-ninth watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-19, the thirty-first hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually, no read errors. The moved repos were read by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 2eee5466 (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the thirtieth watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the relay, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-19, the thirty-second hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually, no read errors. The moved repos were read by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved repos and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 5cc9c826 (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the thirty-first watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-19, the thirty-third hourly re-synthesis watch

The watch re-enumerated the estate at 569 repos, every head read individually, no read errors. The moved repo was read by tree at its fresh head. Evidence below rests on the tree reads at both heads of the moved repo and on the blob comparison of this repo's two Lean files between its heads. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 4b34e16b (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the thirty-second watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-19, the thirty-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 570 repos, every head read individually, no read errors, and read the moved and new repos by tree at their fresh heads. Evidence below rests on the tree reads at both heads of the moved proof repo and on the full census of the new proof repo in its annex. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are byte-identical between the last recorded head and the fresh head, so its eleven names stand unchanged, counted by the watch method over the tree at each pin with the same name set at both. The new proof repo enters with its full set at its first pin; there is no earlier set for it to shrink from. No regression is flagged.
- No pin moved without this ledger moving: every moved or new proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head ab1531f9 (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the thirty-third watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-redundant-compute-expands — new census pin 1ea28648. Proven: 37 theorems in four Lean files — the redundancy measure and its append algebra (the exact split, monotonicity in the seen list, superadditivity, the strict overlap unit, appearance at a join, and the duplicate witness characterization), derivability monotone in the store and in the recorded edges, the graph measure monotone under expansion with witnessed redundancy persistent and expansion transitive, compounding into joined structures with strict units for shared nodes and shared incidence values, and the touch kernel of witness reconstruction (monotone in the sample and under expansion, the inside count bounded by the touched count), assembled in one joined theorem. Of the 37 printed declarations: 2 depend on no axioms, 4 on propositional extensionality only, and 31 on the standard pair. On named premises: the empirical yield rate, carried as the joined theorem's explicit antecedent; the listing reading of growth; and mirror fidelity for the derivability development mirrored from the persistence home. Refuted in the tree: the universal form — not every graph is witnessed redundant — by its standing control, beside five further controls (the zero graph, removal destroying redundancy, the absent strict gain without overlap, touching not containing, and the empty sample). Absent: a compounding rate beyond the proved bound, not claimed; premise-closed reconstruction, proposed and not formalized. Gate: the recorded check log at the pin ends in its axiom subset check passing; this watch ran no build of its own.

## Watch refresh — 2026-11-19, the thirty-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every head read individually, no read errors, and read the moved and new repos by tree at their fresh heads, with every Lean file of the moved proof repo read in full at both heads. Evidence below rests on the tree reads at both heads of the moved proof repos and on the full censuses of the new proof repos in their annexes. Placements stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. The frontier repo gained twenty-three declarations and lost none — every Lean file at its last recorded head is byte-identical at its fresh head — and this repo's eleven names stand unchanged, its two Lean files byte-identical between its heads. The two new proof repos enter with their full sets at their first pins; there is no earlier set for either to shrink from. No regression is flagged.
- No pin moved without this ledger moving: every moved or new proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-frontier-is-solvable — fresh head 60f33193 (census pin 6a41c7be). Proven by the watch method: 127 declarations, 111 distinct short names (was 104 and 94 at the last recorded head); 23 gained, none lost — all in one new file, the candidate module: the candidate record and its structural measures, the gap as a first-class object with its exact scan and its bound, the solved set under a weighting epoch proved exactly the nondominated qualified set under that epoch's measures, weighting independence given the axes, exact update forms for qualified and disqualified appends, joins, and retraction, epoch history replay and preservation, and two proved refutation controls on a named demo space (an epoch axes change changes the solved set; an appended dominating candidate removes a solved member). Premises and absent set stand as the sweep row records, beside the candidate layer's named canonical model premise and its labeled scan count premise, both carried in its annex delta. Gate: a recorded check log stands at the fresh head, its build ending in success, printing axioms for 21 of the 23 new declarations, all standard or empty as printed there; the two unprinted declarations' axiom states are unrecorded there. A full census of the new library in this ledger is owed, as the owed mark in its annex records.
- software-is-a-closed-loop — fresh head 2df09d7b (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the thirty-fourth watch landed; the five commits between them are that watch's census, delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-certification-is-monotone — new census pin 4539760e. Proven: 19 theorems in two Lean files — chain soundness and chain composition (the incremental covers full property at transition grain and at chain grain, both axiom-free on the repo's record), the certificate checker's clause, soundness, regression honesty and its not certified corollary, chain certification of endpoints, and overall certified soundness, beside the control file's nine supporting results and its assembled control refuting endpoint-only comparison (the endpoint-only checker accepts a transition whose interior regresses, no chain evidence for it exists, and the pipeline's checker rejects the matching claim). On named premises: the four world premises the specification names, each with its falsification route (the measure as a function of state, the increment relation as the recorded history, a step's record as an executed check, and orientation). Absent: nothing in the repo's own proved list lacks a statement; its first certificate artifact reads not certified, with three dimensions unmeasured and their gaps named on the artifact — executed evidence, counted nowhere in the proven column. Controls in tree: the assembled control and its supporting results. Gate: the check script stands in the tree; the specification records a cold pass at the landing pin and no build log file stands in the tree, so the gate verdict at this pin is carried at the specification's recorded strength.
- software-redundancy-is-equivalence — new census pin 14992281. Proven: 1 theorem, the seed fact of the logic (two propositions joined by a two way implication are equal), on propositional extensionality only by the recorded log — a skeleton fact, not a theorem of the program, at the repo's own stated strength. On named premises: the two inherited labels the specification states (witness honesty and reading fidelity), which bind where the model is applied. Absent as proven, and carried as proposed at exactly that strength: the model's definitions in Lean form, and all eight claims of the specification's claims section (monotonicity under expansion, compounding, appearance, coloring, bounds, reconciliation, scope, and the registry clauses) with its five standing controls — none has a Lean statement yet. Controls in tree: none standing; the five controls are proposed. Gate: the recorded gate log at the pin prints the seed fact and ends in its axiom subset check passing — green at the pin for the skeleton alone.

## Watch refresh — 2026-11-19, the thirty-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually, no read errors. The moved
repos were read by tree at their fresh heads. Evidence
below rests on the tree reads at both heads of the
moved proof repo and on the blob comparison of this
repo's two Lean files between its heads. Placements
stand at the census pins named in each row.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are
  byte-identical between the last recorded head and the
  fresh head, so its eleven names stand unchanged,
  counted by the watch method over the tree at each pin
  with the same name set at both. No regression is
  flagged.
- No pin moved without this ledger moving: the one
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head f93c5fcc
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the thirty-fifth
  watch landed; the seven commits between them are that
  watch's census, delta, placement, ledger, and pins
  commits and carry no Lean change. Controls and gate
  stand as the second watch row records.

The two other moved repos this watch, the compiler
port and the relay, are not proof repos and carry no
ledger rows: both were read by tree at their fresh
heads, no proof-assistant source was found in either,
and they remain proof-free by the named check.

## Watch refresh — 2026-11-19, the thirty-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually, no read errors. The moved
repos were read by tree at their fresh heads, and the
moved equivalence repo was re-censused in full at its
fresh head, every file read at both pins. Evidence
below rests on the tree reads at both heads of the
moved proof repos and on the full re-census of the
equivalence repo in its annex. Placements stand at
the census pins named in each row, beside the
equivalence row's new pin.

Defect-rule dispositions for this refresh:

- One name loss is flagged, not absorbed, and no
  proven set shrank as a whole. The equivalence repo's
  proven set grew from 1 declaration to 217, and the
  name comparison between its pins, one mechanical
  method at both, finds exactly one lost name: the
  seed fact of the skeleton pin, a fact of the logic
  that stood only so the family gate had a compiled
  development to check. The rewritten core file does
  not restate it; the model's own theorems stand in
  its place, and no theorem of the program was lost.
  This repo's Lean files are byte-identical between
  its heads, so its eleven names stand unchanged.
  The seed loss is recorded as a flagged regression
  of the name set at skeleton strength, with its
  disposition stated here and in the annex.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-redundancy-is-equivalence — new census pin
  37514fb7 (first census pin 14992281). Proven: 217
  theorems in eight Lean files — the canonical model
  implemented (terms with decidable spelling equality,
  the three scopes and their nesting, the one lattice,
  the hypergraph with its validity predicate,
  equivalence, levels, the finite resolved upper bound,
  and redundancy as excess), the four growth operations
  with their preservation and run facts, and all eight
  claims of the specification proved under the names
  the specification assigns: monotonicity under
  expansion, compounding as accumulation of effective
  joins with no additive claim over shared content,
  appearance with its control direction under the
  stated separateness premise, coloring with the
  two-filter rule for the derived mark, bounds with the
  reading and the record kept apart, reconciliation in
  either order, scope widening as growth only, and the
  registry clauses (uniqueness and provenance exact,
  determinism of the recorded color, epoch appends as
  the only reweighting). The derived views layer stands
  proved beside them: derivability monotone in the
  store and in the steps, with its elimination fact.
  On named premises: the two inherited labels, now
  stated as explicit premise definitions in the tree
  (witness honesty and reading fidelity), each with
  its falsification route; no theorem depends on
  either. Absent as proven, at their own stated
  states: the resolution algorithm specification,
  whose claims are proposed (theorem to be, premise,
  or named open gap) and which nothing in its lane
  implements; and the case register's eighty-three
  seed cases, accounted or gap at that same strength.
  The built registry is measured behavior, not proven:
  fifteen entries over 321 witnessed terms, excess
  zero throughout, its second epoch solved by
  exhaustive search over the searched scheme set
  alone, its excess and colored weights unidentifiable
  on this set as its record owns. Controls in tree:
  the five standing controls, each now a proved
  statement over concrete data and each printed in
  the gate log. Gate: the recorded log at the pin
  prints thirty-eight axiom audits — four axiom-free,
  two on propositional extensionality only, the rest
  on subsets of the standard three — and ends in its
  axiom subset check passing; green at the pin by the
  recorded log, for the whole development.
- software-is-a-closed-loop — fresh head 944a8a13
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the thirty-sixth
  watch landed; the four commits between them are that
  watch's delta, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand
  as the second watch row records.

The one other moved repo this watch, the compiler
port, is not a proof repo and carries no ledger row:
it was read by tree at its fresh head, no
proof-assistant source was found in it, and it remains
proof-free by the named check.

## Watch refresh — 2026-11-19, the thirty-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually, no read errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated. Evidence below rests on the tree
reads at both heads of the moved proof repos: every
Lean file in each is byte-identical between the last
recorded head and the fresh head. Placements stand
at the census pins named in each row; a full
theorem-level re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. Every Lean file in both moved
  proof repos is byte-identical between the last
  recorded head and the fresh head, so no name was
  lost in either; the semi repo's counts by the watch
  method stand unchanged at 1,865 declarations and
  1,736 distinct names, and this repo's eleven names
  stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- idol-semi — fresh head 0d730e5b (census pin
  508d7c66). Proven: unchanged — all 156 Lean files
  are byte-identical between the census pin, the last
  recorded head, and the fresh head, and no Rust file
  changed in source, so the congruence closure,
  matching, and fidelity development and the Rust
  verification stand exactly as the sweep row
  records. Counted at the fresh head by the watch
  method: 1,865 declarations, 1,736 distinct short
  names, no name gained and none lost. The movement
  is fifteen added files — a native Idol projection
  folder and a parity outcome folder — beside twenty
  changed files of integration workflows and Rust
  manifests, over seventeen commits. Absent: a
  recorded check log still stands nowhere in the
  tree, so a passing gate at the fresh head remains
  claimed, not proven; the gate re-run at the shared
  pin remains blocked on host disk quota, as the
  high-impact addendum records. Placement note: the
  mirror repo did not move and still stands at
  508d7c66, so the two repos' heads stand further
  apart; their proof content remains identical, and
  this row tracks the semi repo's head, with the
  mirror's head recorded here until it moves.
- software-is-a-closed-loop — fresh head 8a230cf9
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the thirty-seventh
  watch landed; the five commits between them are that
  watch's re-census, delta, placement, ledger, and pins
  commits and carry no Lean change. Controls and gate
  stand as the second watch row records.

The one other moved repo this watch, the compiler
port, is not a proof repo and carries no ledger row:
it was read by tree at its fresh head, no
proof-assistant source was found in it, and it remains
proof-free by the named check.

## Watch refresh — 2026-11-19, the thirty-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head c123715b (census pin d558669b). Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the thirty-eighth watch landed; the four commits between them are that watch's delta, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The two other moved repos this watch, the compiler port and the relay, are not proof repos and carry no ledger rows: both were read by tree at their fresh heads, no proof-assistant source was found in either, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-19, the fortieth hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo,
and on the recorded check log read in full at the
redundant compute repo's fresh head. Placements stand
at the census pins named in each row; a full
theorem-level re-census at each fresh head is owed
where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The library repo's Lean files
  are byte-identical between its census pin and its
  fresh head, and this repo's are byte-identical
  between its last recorded head and its fresh head,
  so no name was lost in either; the redundant compute
  repo's original four files are byte-identical and
  its count grew from 37 to 194 declarations with no
  name lost. No regression is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- idol-lib — fresh head 0052f16e (census pin
  4dee2311). Proven: unchanged — all four Lean files
  are byte-identical between the census pin and the
  fresh head, so the campaign kernel, the atlas
  development, the Pareto package, and the witness
  examples stand exactly as their rows record: 65
  declarations, the same name set, no name gained and
  none lost. The movement is a realization route in
  five commits — five hash batteries run without the
  compiler, one further hash entry with its generator,
  vectors, and verifier, and transcript hardening —
  twelve files added and the ledger changed, none of
  them proof content. Premises, absent set, controls,
  and gate stand as the census records.
- software-redundant-compute-expands — fresh head
  559f308b (census pin 1ea28648). Proven: 194
  declarations in thirteen Lean files by the watch
  method (was 37 in four files at the census pin);
  157 gained, none lost, the original four files
  byte-identical. The growth is the canonical layer —
  one record log with the mirrored derivability
  definitions proved again and an equivalence of terms
  at each level — the measure restated on that log as
  redundant support, the append-only coloring, intent
  composition, the case hierarchy, the resolution
  algorithm with its Pareto result over its stated
  objective set, and the further measurement units.
  On named premises: the yield premise and the mirror
  fidelity premise stand as its census row records;
  the listing premise is discharged at this head by
  the re-listing file, which proves the measure
  invariant under every re-listing. Absent restated:
  the premise-closed reconstruction its census carried
  as proposed is proven at this head in kernel form by
  the sample file; its measured protocol run remains
  outside the repo, not a result here. Controls: the
  original six stand unchanged in their file, beside
  the new files' own concrete controls. Gate: the
  recorded check log in the tree at the fresh head,
  read in full by this watch, prints axiom lines for
  189 of the 194 declarations — 15 on no axioms, 32 on
  propositional extensionality only, 118 on the
  standard pair, 24 on the full standard set — and
  ends in its axiom subset check passing; five counted
  declarations carry no printed line, among them the
  canonical file's three equivalence properties, so
  their axiom state is unrecorded from the log. A full
  theorem-level re-census at the fresh head is owed.
- software-is-a-closed-loop — fresh head 00ed9e0f
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the thirty-ninth
  watch landed; the four commits between them are that
  watch's delta, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The three other moved repos this watch, the compiler
port, the operating system repo, and the personal
site repo, are not proof repos and carry no ledger
rows: all three were read by tree at their fresh
heads, no proof-assistant source was found in any of
them, and they remain proof-free by the named check,
as their census entries record.

## Watch refresh — 2026-11-19, the forty-first hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads. Evidence
below rests on the tree and commit reads at both
heads of the moved proof repo: no Lean file changed
between them. Placements stand at the census pins
named in each row; a full theorem-level re-census
at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean
  files are unchanged between the last recorded head
  and the fresh head, so no name was lost; this repo's
  eleven names stand unchanged. No regression is
  flagged.
- No pin moved without this ledger moving: the one
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head a36ac17a
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the fortieth
  watch landed; the four commits between them are that
  watch's delta, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The one other moved repo this watch, the relay, is
not a proof repo and carries no ledger row: it was
read by tree at its fresh head, no proof-assistant
source was found in it, and it remains proof-free by
the named check, as its census entry records.

## Watch refresh — 2026-11-19, the forty-second hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads. Evidence
below rests on the tree and commit reads at both
heads of the moved proof repo: no Lean file changed
between them. Placements stand at the census pins
named in each row; a full theorem-level re-census
at each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean
  files are unchanged between the last recorded head
  and the fresh head, so no name was lost; this repo's
  eleven names stand unchanged. No regression is
  flagged.
- No pin moved without this ledger moving: the one
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 95627cdf
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the forty-first
  watch landed; the four commits between them are that
  watch's delta, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The one other moved repo this watch, the compiler
port, is not a proof repo and carries no ledger row:
it was read by tree at its fresh head, no
proof-assistant source was found in it, and it
remains proof-free by the named check, as its census
entry records.

## Watch refresh — 2026-11-20, the forty-third hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads. Evidence
below rests on the tree and commit reads at both
heads of the moved proof repo: no Lean file changed
between them. Placements stand at the census pins
named in each row; a full theorem-level re-census at
each fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean
  files are unchanged between the last recorded head
  and the fresh head, so no name was lost; this repo's
  eleven names stand unchanged. No regression is
  flagged.
- No pin moved without this ledger moving: the one
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head baab58d7
  (census pin d558669b). Proven: 11 theorems, unchanged
  — the same name set at the last recorded head and at
  the fresh head, which is the head the forty-second
  watch landed; the four commits between them are that
  watch's delta, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The two other moved repos this watch, the compiler
port and the relay, are not proof repos and carry no
ledger rows: both were read by tree at their fresh
heads, no proof-assistant source was found in either
of them, and they remain proof-free by the named
check, as their census entries record.

## Watch refresh — 2026-11-20, the forty-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 572 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated; the eyes repo's four proof files were
read in full and censused at theorem level, as its new
annex records. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Name comparison at both heads
  of every moved proof repo shows no name lost: the
  safe repo gained ninety-seven distinct names by
  addition beside byte-identical earlier files, the
  redundant compute repo gained seven beside
  byte-identical files, the library repo and the
  compiler repo and this repo have every Lean file
  byte-identical between heads, and the eyes repo is
  newly proof-bearing with nothing to lose. One
  counting clarification is flagged here rather than
  absorbed: of the library repo's eight mechanically
  gained names, six are isolated oracle fixture
  theorems at fixture strength and two are not proven
  results at all — a false statement proven by an
  admitted proof and a conditional result on a planted
  false axiom, both planted controls with their
  dependence recorded in the tree — so the library's
  proven set is recorded unchanged below, not grown.
  No regression is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass, and the newly proof-bearing eyes repo has
  its row added. No synthesis defect is flagged.

Restated rows at the fresh heads:

- software-is-a-closed-loop — fresh head
  54cb6a491f14e90ae022d0420d0489832305f16f, census pin
  d558669b standing. Proven: the eleven declarations
  of the two-paper development, unchanged — both Lean
  files are byte-identical between the last recorded
  head baab58d7 and the fresh head, the four commits
  between them being the forty-third watch landing
  itself. Premise, absent, controls, and gate state
  stand as the last full row records.
- software-is-incrementally-safe — fresh head
  32174a7cbf2b12f7390a07ccdb7041fbf6043886, census pin
  8ad1dd26 standing with a full theorem-level
  re-census at the fresh head owed. Proven: 277
  declarations in thirty-two Lean files by the watch
  method, 246 distinct names, where the last recorded
  head carries 151 and 149 — ninety-seven distinct
  names gained, none lost, every earlier file
  byte-identical. The gain is a whole new family
  development: necessary dominance with the least
  sound cone contained in the necessary one, dataflow
  locality, an executable cone checker proven in both
  directions with its least closed cone, partition
  fineness as key occupation, saturation, an exact
  parallel unknown result, and six worked examples
  each proving their good change admitted and their
  bad change refused. Premise: the audited-strength
  caveats of the last full row stand for the earlier
  developments and extend to the family development,
  whose strength rests on this watch's reading and
  its in-tree audit file printing axiom lines for
  forty-seven family names, not on a recorded gate
  run. Absent: a recorded check log at the fresh head
  — none stands in the tree. Controls: the worked
  examples' refused bad changes stand as proved
  refusal results in form. Gate state: no recorded
  log at the fresh head, so a passing gate there is
  unrecorded, as at the last recorded head.
- software-optimality — fresh head
  0bbc1f3b8aa38afe17e02ccbd7ddd0e7722b3cb0, census pin
  b52c3170 standing with a full re-census at the
  fresh head owed. Proven: the library's proven set
  is unchanged — every library Lean file is
  byte-identical between the last recorded head
  95df5fb7 and the fresh head. The mechanical count
  rose from 684 declarations and 588 distinct names
  to 692 and 596, and all eight gained names stand in
  new oracle fixture files: six kernel fixture
  theorems proven at fixture strength, their recorded
  evidence printing five depending on no axioms and
  one on propositional extensionality only; one
  admission fixture proven by an admitted proof, a
  planted control, not a proven result; and one
  conditional fixture on a planted explicit false
  axiom, likewise a control. Premise: no library
  premise moved; the two fixture controls carry their
  planted premises on their face, recorded in the
  tree's evidence files. Absent: nothing new — the
  absent set of the last full row stands. Controls:
  the oracle slice adds its own expected-outcome
  controls — the admission warning and strict error,
  the axiom dependence, the invalid fixture's expected
  type mismatch, and the runtime result — asserted by
  the oracle script with the evidence files standing
  as the recorded run; its readme states the slice is
  a noncompeting read-only inventory, not an
  implementation or a parity certificate. Gate state:
  the library's recorded logs stand at the census
  pin; the oracle evidence and the two portable
  evidence check logs of nine passing tests each are
  recorded runs at the fresh head for their own
  slices only.
- software-redundant-compute-expands — fresh head
  05e0584eb5f0f7f43bd2274a92d5dcfde1122e16, census pin
  1ea28648 standing with a full theorem-level
  re-census at the fresh head owed. Proven: 202
  declarations in fourteen Lean files by the watch
  method with comments stripped, 154 distinct names,
  where the last recorded head carries 195 and 147 —
  seven gained, none lost, the other thirteen files
  byte-identical. The new candidate impact file
  proves, over a two-seed joint rule, that
  reachability is not qualification: each seed
  necessary, the qualification form exact,
  complementarity of the two seeds, agreement of the
  canonical log view with the direct form, and the
  appended joint consequence in the log view.
  Premise: the yield premise and the mirror fidelity
  premise stand as the last full row records. Absent:
  a recorded gate run covering the new file — the
  recorded check log in the tree predates it and
  stands unchanged. Controls: the non-closed and
  single-seed refusals stand as proved results in the
  developments. Gate state: the recorded log covers
  the earlier tree within the standard set; the new
  file's gate rests on its own print lines for its
  last three results and this watch's reading.
- idol — fresh head
  a4720380558bf2a5349258d4e410592f26b24c07, census pin
  561cf395 standing. Proven: unchanged — all five
  Lean files are byte-identical between the last
  recorded head 586ff5a1 and the fresh head, read by
  tree in full with no read truncated: the frontier
  file's seven declarations, the retention file's
  twenty and the qualification file's five in the
  release tools development, and the solver history
  file's ten, with the proof data sample standing as
  test data counted nowhere. The movement is
  twenty-two commits of compiler and gate work, the
  wholesale directive ratchet landing among them, no
  Lean file among the files added or changed.
  Premise, absent, controls, and gate state stand as
  the last full row records, including the owed full
  census of the release tools and solver
  developments.
- idol-eyes — new row, census pin and fresh head
  1dc24f4fcd8240ab6fbc9056dba7726e5c62bd98. Proven:
  sixty-one declarations in four Lean files, read in
  full and censused at theorem level in this pass, as
  its annex records — the canonical file's
  twenty-four (the derivability core proven again
  from the mirrored definitions, the resolution-chain
  model, and the view laws over the one append-only
  record log), the certification file's twenty-three
  (the admission decision exact, permutation and
  sublist invariance, regression finality in both
  forms, the unmeasured refusal, witnessed admission,
  transitivity over steps, dimension antitonicity,
  and the beat results with the tie and loss
  controls), and the union file's fourteen (meeting
  the union as exactly admission over each incumbent
  and exactly pooled domination, the unmeasured
  incumbent refusal, the ceiling form, and union
  regression finality), beside an axioms file printing
  lines for twenty-nine of the sixty-one. Premise:
  four named premises carried on the files' own
  headers, not proved — faithful score normalization
  at ingest, measurement records stating what was
  measured under the campaign's same-contract rules,
  the declared maximum as the true maximum of the
  normalized score with a failed run ingested at zero
  on every cost dimension, and mirror fidelity of the
  restated definitions. Absent: axiom lines for the
  canonical file's twenty-four theorems, which carry
  none in the axioms file, so their axiom state is
  unrecorded; and a recorded run of the repo's check
  script at the pin. Controls: no dedicated controls
  file; the refusal theorems stand as proved controls
  inside the developments, and the check script's
  escape scan stands as a gate control — the watch
  scan found no escape token in the three proof
  files. Gate state: the check script stands in the
  proof folder at the named Lean version, compiling
  the three files and running the axioms file, but no
  recorded run stands in the tree, so a passing gate
  at the pin is claimed by the script's presence, not
  proven.

The compiler port and the relay also moved and were
read by tree at their fresh heads: no proof-assistant
source stands in either and no tree read was
truncated, so both remain proof-free by the named
check and carry no ledger row.

## Watch refresh — 2026-11-20, the forty-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 573 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated; the new reversible repo's three proof
files and the library repo's new space package were
read in full and censused at theorem level, as their
annex records. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Name comparison at both heads
  of every moved proof repo, one mechanical method at
  both heads, shows no name lost: the frontier repo
  gained seventy-nine distinct names by addition beside
  byte-identical earlier files, the redundant compute
  repo gained thirty-nine beside byte-identical files,
  the library repo gained fifty-two distinct names in a
  wholly new package beside byte-identical earlier
  files, this repo has every Lean file byte-identical
  between heads, and the reversible repo is new with
  nothing to lose. One counting note is flagged here
  rather than absorbed: the redundant compute repo's
  last recorded head reads 201 declarations by this
  watch's method, one below the forty-fourth watch's
  recorded 202 for the same head; the file identity
  evidence governs, and the gain and loss figures in
  its row are computed at one method at both heads. No
  regression is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass, and the new reversible repo has its row
  added. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-frontier-is-solvable — fresh head
  eb29b7de88e8ee7145f876f13d6a18c355dba60a, census pin
  6a41c7be standing with a full theorem-level
  re-census at the fresh head owed. Proven: 206
  declarations, 190 distinct names by the watch method
  (was 127 and 111 at the last recorded head); 79
  gained, none lost. The growth is two new library
  modules: the pipeline module (28 — determinism of the
  derived view, the selected action's frontier
  standing, incremental reevaluation equal to full,
  compensation restoring the solved set, stop soundness
  in both faces, and three proved refutation controls,
  on six premises its header labels and carries), with
  a recorded check log at the fresh head ending in a
  successful build and printing all 28 declarations —
  7 on no axioms, 6 on propositional extensionality
  only, 13 on the standard pair, 2 on the full standard
  set; and the worklist module (51 — the indexed
  closure exactly the least full closure at every
  append prefix, with four closing controls), with a
  recorded check log at the fresh head ending in a
  successful build and printing 13 of the 51 — the
  other 38 carry no printed line, so their axiom state
  is unrecorded from the log. Premises and the absent
  set stand as the earlier rows record, beside the
  pipeline module's own six labeled premises.
- software-redundant-compute-expands — fresh head
  4da720a704151c92c7ee28278ba8538703638271, census pin
  1ea28648 standing with a full theorem-level
  re-census at the fresh head owed. Proven: 240
  declarations, 192 distinct names by the watch method
  (was 201 and 153 at the last recorded head by the
  same method); 39 gained, none lost. The growth is
  three new files beside fourteen byte-identical ones:
  certified action selection over the canonical layer
  (13, its stop exact and invariant under reweighting),
  the canonical closure worklist (15, its drained run
  exactly the canonical closure, with its resume
  forms), and the intelligence join (11, convergence at
  a delivered cut and exact reconstruction from a
  delivered set). Each new file prints its own
  declarations in source — the closure and join files
  all of theirs, the action file twelve of thirteen —
  and the recorded check log in the proof folder is
  byte-identical between the heads and predates all
  three, so no recorded gate run covering them stands
  in the tree. Premises restated: the yield premise and
  the mirror fidelity premise stand as the census row
  records; the listing premise stands discharged, as
  the fortieth watch recorded.
- idol-lib — new census pin and fresh head
  578b8b3a7e212082bf0d1f8a5a582cca63af3a19. Proven:
  120 declarations in total, every one with a distinct
  name at this head — the 65 of the earlier censuses
  unchanged in four byte-identical files, plus 55 in a
  new space package of ten theorem files over the
  behavioral hypergraphs of the fourteen witnessed
  libraries, re-censused at theorem level in full in
  this pass, as its annex records: the two data levels
  reconciled in the kernel (the chain nesting at both
  levels, nothing at the current level measured or
  qualified, the earlier level's 155 qualified
  definitions retracted by the level change, 318 of
  321 keys kept with 106 new), determination exactly
  factorization through a battery with the helper and
  unseen input forms refuted, merging by name and by
  body refuted and merging by whole closure sound
  under the named locality premise, the host cone
  spanning in the joined graph with the per-library
  form refuted, constructed dominance transferring
  only in the proved direction with the wrong direction
  refuted and one named rewrite's measured loss proved
  over its own record, verdicts append only and
  carrying only under an unchanged closure, and the
  realized batteries passing on their receipts while
  qualifying nothing. On named premises: the locality
  premise, battery coverage, the price of compute, and
  the public fields of an observation, as the annex
  restates. Absent: per-symbol profiles, UNMEASURED at
  the repo's own state, and the model to program
  refinement of the earlier rows. Controls: the
  package's data regeneration check stands in its
  check script; the refutations above stand as proved
  controls inside the development. Gate state: the
  check script stands in the tree and its axioms file
  prints 44 of the 55 new theorems in source, but no
  recorded run of the script stands in the tree, so a
  passing gate at this pin is unrecorded — one step
  below the kernel and Pareto packages' recorded,
  hash-bound strength.
- software-is-reversible — new row, census pin and
  fresh head 984f1faf3d0f74116a4b38b550b11e7c56237faa.
  Proven: 55 declarations in three Lean files, read in
  full and censused at theorem level in this pass, as
  its annex records — the root development's 38 (the
  frontier before weights counterexample at two scales,
  the break-even rule in full cost form, the closure
  worklist count laws, the one-append update and
  compensation in place, the reversible action
  structure with its refusal form, stop soundness in
  its acceptable and certified faces with the threshold
  form refuted, the powerset count law, and tensor
  edits as overlays) and the scoped development's 17
  (the finite inverse theory — an inverse exactly under
  injectivity, collisions impossible, composition, the
  residual form — with its fiber and rank results and
  five helpers). On named premises: the repo's premise
  register — the canonical premise, extraction fidelity,
  execution fidelity, witness honesty, reading fidelity,
  axis meaning, threshold choice, progress, and counted
  cost — carried at its stated strengths. Absent:
  reversibility at the execution layer, UNMEASURED in
  the repo's own census until its validation system
  demonstrates the round trip per action; the general
  symmetric form of the never-selected result and the
  worklist equality against the canonical home's view
  semantics, both stated and unproved as named lemmas
  with owners; and the resolution algorithm's carried
  gaps. Controls: the threshold refutation and the two
  never-selected results stand proved in the root file.
  Gate state: the scoped development carries a recorded
  axiom audit in its tree printing 12 of its 17 — 4 on
  no axioms, 4 on propositional extensionality only, 4
  on the standard pair, the five helpers unprinted; the
  root development's axioms file prints all 38 in
  source and its gate pass is recorded as a claim in
  the repo's own census, with no recorded log file in
  the tree, so that pass stands claimed at the repo's
  stated strength, not proven from a log.
- software-is-a-closed-loop — fresh head
  5cb332bb1bb2b50481bade8c9f38277ce4337a58, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the forty-fourth
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The compiler port, the relay, and the sites repo also
moved and were read by tree at their fresh heads: no
proof-assistant source stands in any of them and no
tree read was truncated, so all three remain proof-free
by the named check and carry no ledger row.

## Watch refresh — 2026-11-20, the forty-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 573 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated; the reversible repo's seven proof files
were read in full and re-censused at theorem level, as
its annex records. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Name comparison at both heads
  of every moved proof repo, one mechanical method at
  both heads, shows no name lost: the reversible repo
  gained thirty-nine distinct names beside a
  byte-identical scoped development, and the compiler
  repo, the eyes repo, the library repo, the
  equivalence repo, and this repo have every Lean file
  byte-identical between heads. No regression is
  flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass, and the reversible repo's census pin moves
  with its row. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  bc63b1dff892ec981514910e4334ecd704ca3e74, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the forty-fifth
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.
- idol — fresh head
  8705d4cfb40cfa006fb94ce637c6179f6d49aa3a, census pin
  561cf395 standing (proof-bearing content only).
  Proven: unchanged — all five Lean files are
  byte-identical between the last recorded head and
  the fresh head, counted at forty-five declarations
  by the watch method: the frontier file with its 7
  theorems on the premises its row records, the
  release tools files with their 20 and 5, the solver
  history file with its 10, and the proof data sample
  that remains test data, counted nowhere. The
  movement is two commits of compiler work, four files
  changed and none of them Lean. Gate: the release
  tools verdict stands in the high-impact addendum
  above at its named pin; the solver history file's
  gate remains unknown, and the full census of the
  release tools and solver developments remains owed.
- idol-eyes — fresh head
  1b0e92d37f87c62197486e812ab90ba28dd381a7, census pin
  1dc24f4f standing. Proven: 61 theorems, unchanged —
  all four Lean files are byte-identical between the
  census pin and the fresh head, the same name set at
  both. The movement is two commits of harness
  evidence work: one retained offline evidence record
  added and the harness document changed. Premises,
  absent set, and controls stand as its census row
  records. Gate: a passing run at the fresh head is
  unrecorded, as its census row records for the pin.
- idol-lib — fresh head
  a76bd4f922a4dc4737d49705248dfbeb9c380fa4, census pin
  578b8b3a standing. Proven: 120 theorems, unchanged —
  all twenty Lean files are byte-identical between
  the census pin and the fresh head, the same name
  set at both, in three theorem files beside six
  checked witness examples and the space package's
  sixteen files. The movement is two commits landing
  a protocol buffers port slice of thirteen files and
  its ledger record, none of them Lean. Premises,
  absent set, and controls stand as its re-census row
  records. Gate: unrecorded at the census pin, as
  that row records.
- software-is-reversible — census pin moves to the
  fresh head fcb9595310d8a0782cb7fca1b2203d80b28c8d8c
  on the full re-census in this pass. Proven: 94
  declarations in seven Lean files (was 55 in three
  at the last census pin), thirty-nine gained and
  none lost — the root development at 42, its four
  gains closing named work: the general symmetric
  form of the never-selected result, stated and
  unproved at the last pin, proved in three parts
  (the segment form, the frontier form, and the
  canonical form), and the overlay collapse lemma;
  the scoped development at 17, byte-identical; and
  four new example developments — action consensus 9
  (the fiber exact under append, certification
  preserved under refinement, the countermodel
  exactness, the alias obstruction control), product
  frontier 5 (the coordinate law, the product
  frontier exact, replay under a frozen bridge, and
  the coupled join control), suffix page 10 (block
  enumeration, selection, mass, and paging exact
  against the reference, with duplicate freeness),
  and compositional pruning 11 (dominance composition,
  the additive continuation exact, the kept frontier
  and its image exact under coverage, and the status
  forms). On named premises: the repo's premise
  register stands as its census row records, carried
  at its stated strengths. Absent: reversibility at
  the execution layer, UNMEASURED in the repo's own
  census; and the worklist equality against the
  canonical home's view semantics, still stated and
  unproved as a named lemma — the one of the two
  named lemmas that remains, its sibling now proved.
  Controls: the threshold refutation and the
  never-selected results stand proved in the root
  file, joined by the alias obstruction and coupled
  join controls in the new developments. Gate state:
  the root development's axioms file prints all 42
  in source and its cold pass at that count is
  recorded as a claim in the repo's own census, with
  no recorded log file in the tree; the scoped
  development's recorded audit stands as its row
  records; the action consensus log prints all nine
  (five axiom-free, four on propositional
  extensionality only) and the product frontier log
  prints all five (three axiom-free, two on
  propositional extensionality only); the suffix
  page log prints seven of its ten on subsets of the
  standard pair, the remaining three unprinted; and
  the compositional pruning file prints seven of its
  eleven in source with no recorded log, so its gate
  stands unrecorded.
- software-redundancy-is-equivalence — fresh head
  37794d7492c1d2c0b01546e4762b3059007e68a3, census pin
  37514fb7 standing. Proven: 217 declarations,
  unchanged — all nine Lean files are byte-identical
  between the census pin and the fresh head, the
  same name set at both. The movement is two commits
  of registry and approach space work: the first
  witnessed join entered in the registry, the third
  epoch solved there, and the approach space founded
  by its semantic axes, all registry and document
  content at their own states. Premises, absent set,
  and controls stand as its census row records.
  Gate: green at the census pin by the repo's
  recorded log, as its census row records.

The compiler port, the relay, and the sites repo also
moved and were read by tree at their fresh heads: no
proof-assistant source stands in any of them and no
tree read was truncated, so all three remain proof-free
by the named check and carry no ledger row.

## Watch refresh — 2026-11-20, the forty-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 574 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated; the new and grown developments were
read in full and counted at theorem level, as their
annex records. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Name comparison at both heads
  of every moved proof repo, one mechanical method at
  both heads, shows the compiler repo, the library
  repo, the reversible repo, and this repo with every
  Lean file byte-identical; the frontier repo gained
  thirty-four declarations and lost none; and the
  review and certifiable repos grew by forty-two and
  ninety-nine names. Two name losses are flagged here,
  not absorbed: the review repo lost its two planted
  admitted proof control names and the certifiable repo
  lost its one, in each case because the control file
  left the Lean inventory by rename to a non-Lean
  fixture file, byte-identical, where it stands as an
  explicit rejection or expected failure control under
  the new gate. Those declarations were controls that
  must fail, never proven results; no library or
  statement name was lost in either repo. No regression
  is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass, and the new proof repo's row is entered
  below with its census pin set in this same pass. No
  synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  5ce896f926ed1ff0c8e459507c1abbf3639d725e, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the forty-sixth
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.
- idol — fresh head
  77693466eab09156388857cea49e551bcf9f647e, census pin
  561cf395 standing (proof-bearing content only).
  Proven: unchanged — all five Lean files are
  byte-identical between the last recorded head and
  the fresh head, counted at forty-five declarations
  by the watch method: the frontier file with its 7
  theorems on the premises its row records, the
  release tools files with their 20 and 5, the solver
  history file with its 10, and the proof data sample
  that remains test data, counted nowhere. The
  movement is four commits of compiler and gate work,
  one evidence file added and four files changed and
  none of them Lean. Gate: the release tools verdict
  stands in the high-impact addendum above at its named
  pin; the solver history file's gate remains unknown,
  and the full census of the release tools and solver
  developments remains owed.
- idol-lib — fresh head
  0be14af8d63a749c5121dbf790665cf38593b077, census pin
  578b8b3a standing. Proven: 120 theorems, unchanged —
  all twenty Lean files are byte-identical between
  the census pin and the fresh head, the same name
  set at both, in three theorem files beside six
  checked witness examples and the space package's
  sixteen files. The movement is eight commits
  extending the realization route to every verifier
  home: twelve files added, a realization source for
  each of ten homes and a blocker record for the
  redundant home, and three files changed, none of
  them Lean. Premises, absent set, and controls stand
  as its re-census row records. Gate: unrecorded at
  the census pin, as that row records.
- software-is-reversible — fresh head
  0ac60e7db7207c7b823283836fa66138a5ee7e3f, census pin
  fcb95953 standing. Proven: 94 declarations,
  unchanged — all seven Lean files are byte-identical
  between the census pin and the fresh head, the same
  name set at both. The movement is one commit, the
  repo's own census addendum, recording that the
  worklist equality lemma — the one named unproved
  lemma its re-census row carried — stands proved in
  the frontier home at its fresh head in this same
  window, so no named unproved lemma from its census
  remains. Premises stand as its re-census row
  records. Absent: reversibility at the execution
  layer, UNMEASURED still. Controls and gate stand as
  its re-census row records, development by
  development.
- software-doesnt-need-review — fresh head
  36411de6f40a751739afcc5aa9ed262e84fd550d, census pin
  40b1e885 standing. Proven: 126 declarations by the
  watch method (was 86 at the last recorded head),
  42 gained and the 2 planted control names lost by
  rename, flagged above. The gain is a statement
  package in its own isolated build beside the
  byte-identical legacy library: its three original
  propositions stand inhabited — the full closure
  claim with its exact absorption characterization,
  the relevant claim, and the omission claim, all
  three axiom-free — with the stronger prospective
  core and application forms, the redundancy
  characterizations, and the finite checker
  correctness, 23 new non-control theorems in all;
  and 18 standing counterexample theorems, ten
  retained and eight new, refuting the stronger
  readings its claim file names. On named premises:
  the application premises for any production
  omission stand open, as its claim file names them;
  no production instance is certified. Controls: the
  18 counterexamples in tree, beside the gate controls
  its verification record lists, including the renamed
  fixtures run as rejection controls. Gate: a recorded
  publisher log stands at the fresh head, its
  verification record stating exit 0 over both
  packages with the axiom audit inside the standard
  three; the independent exact pin recheck that record
  requires stands owed, so the pass is carried at the
  publisher's strength, not as an independent receipt.
  A full re-census at the fresh head is owed.
- software-frontier-is-solvable — fresh head
  307dffca9b7165f4fb92fa30575b940df9613a1a, census pin
  6a41c7be standing. Proven: 240 declarations by the
  watch method (was 206 at the last recorded head),
  34 gained and none lost — the canonical view file
  (24: the canonical definitions carried verbatim from
  their home and proved again, the resolution level
  chain with its nesting, projection, join, and
  refinement results, and two standing controls) and
  the bridge file (10: the derivation predicates of
  the worklist and the canonical view proved the same
  predicate on the stated fragment, the fixed view
  equality, the append form at every prefix with its
  carried set instantiation, and a non-vacuity
  control) — closing the worklist equality lemma the
  reversible home carried as named work. On named
  premises: the bridge's stated fragment conditions —
  the fixed chain, log, level, and color test, empty
  roots and seed, membership readings on both sides —
  carried exactly as its header states; the earlier
  premises stand as the sweep row records. Absent
  stands as the sweep row records. Controls: the two
  canonical controls join the tree's earlier controls.
  Gate: a recorded check log stands at the fresh head
  and ends in a successful build, printing all 10
  bridge declarations and 20 of the 24 canonical ones
  on subsets of the standard set; the remaining four
  carry no printed line in that log. A full re-census
  at the fresh head is owed.
- software-is-incrementally-certifiable — fresh head
  3d4952bb86a41d0b8f23eef4248ae2914da3a4be, census pin
  c9ffd49a standing. Proven: 187 declarations by the
  watch method (was 89 at the last recorded head), 99
  gained and the 1 planted control name lost by
  rename, flagged above. The gain is a proof and
  falsification duet: the historical model recovered
  from the safe home's audited branch pin (32
  declarations across its two legacy files) under a
  documented namespace transformation, with its bridge
  to the canonical interface (3); the legacy sequence
  results (23) — the unrestricted thesis refuted by
  checked counterexample, adjacent nonregression
  exactly equivalent to all pairs nonregression,
  strict improvement exactly witnessed, and the
  guarded step form under a fixed requirement set;
  the canonical release sequence results (15) —
  adjacent exactly equivalent to all pairs, observed
  behavior retained, frontier coverage, history
  frontier membership, strict refinement without
  return, and the executable step check exact; and
  the duet controls (26) standing the refutations as
  theorems. On named premises: the five application
  premises its duet record names — faithful costs,
  faithful behaviors, authoritative obligations,
  pipeline enforcement, and global candidate coverage
  — stand as premises, and temporal nonregression
  replaces the unqualified global optimality claim,
  as that record corrects it. Controls: the duet
  controls in tree, beside the renamed admitted proof
  fixture run as an expected failure. Gate: the new
  all files gate contract stands in the tree, but no
  recorded run log or receipt stands at the fresh
  head, so a passing gate at this head is unrecorded;
  the independent recheck its duet record requires
  stands owed. A full re-census at the fresh head is
  owed.
- software-is-a-parametric-language-model — census pin
  set to its head ca4ca2b39181bb93a717b3edbb58ab476761fa5c
  on the first census in this pass. Proven: 40
  theorems in one Lean file — the fraction arithmetic
  (13), the selection machinery (7, its specification
  with at most one satisfier), the decoder (6, its
  answer the unique satisfier of its specification),
  certification soundness under the coverage premise
  and blocking proved outright (2), the overlay round
  trip, positivity, and cone invariance (8), route one
  locality (2), and two standing controls proved
  (greedy uncertified on its control table; an
  unresolved bound blocking certification), as its
  annex census itemizes. On named premises: the coverage premise,
  named with its falsification route, holding by
  construction for probability rows and checkable for
  an arbitrary table; the six pipeline premises
  carried over. Absent and unmeasured, as the repo
  prints: the real checkpoint cells UNMEASURED under
  a named access blocker, code generation beyond
  fixture scale, live serving, and the demo surface's
  conformance each UNMEASURED with blockers named;
  the compression horizon proposed; the registry
  append of its extract owed. Controls in tree: the
  two proved standing controls. Gate: green at the
  pin by the repo's recorded log — warnings as
  errors, escape scan clean, all 40 axiom lines
  printed inside the standard three, 9 depending on
  no axioms.

The api repo, the compiler port, the operating system
repo, and the relay also moved and were read by tree
at their fresh heads: no proof-assistant source stands
in any of them and no tree read was truncated, so all
four remain proof-free by the named check and carry no
ledger row.

## Watch refresh — 2026-11-20, the forty-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 574 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in every moved proof repo: both moved
  proof repos carry every Lean file byte-identical
  between the last recorded head and the fresh head, so
  no name was gained and none lost in either. No
  regression is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  880b629700c822d2886fe59e71f3a94945d253b3, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the forty-seventh
  watch landed; the five commits between them are that
  watch's annex, placement, ledger, correction, and
  pins commits and carry no Lean change. Controls and
  gate stand as the second watch row records.
- idol — fresh head
  cc66b42aea404ef6980f2744ec600947c230bf1e, census pin
  561cf395 standing (proof-bearing content only).
  Proven: unchanged — all five Lean files are
  byte-identical between the last recorded head and
  the fresh head, counted at forty-five declarations
  by the watch method: the frontier file with its 7
  theorems on the premises its row records, the
  release tools files with their 20 and 5, the solver
  history file with its 10, and the proof data sample
  that remains test data, counted nowhere. The
  movement is four commits of compiler, library, and
  gate work, ninety-three files changed and none
  added or removed and none of them Lean. Gate: the
  release tools verdict stands in the high-impact
  addendum above at its named pin; the solver history
  file's gate remains unknown, and the full census of
  the release tools and solver developments remains
  owed.

The relay also moved and was read by tree at its
fresh head: no proof-assistant source stands in it
and its tree read was not truncated, so it remains
proof-free by the named check and carries no ledger
row.

## Watch refresh — 2026-11-20, the forty-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 574 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated. Evidence below rests on the tree and
commit reads at both heads of each moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in every moved proof repo: both moved
  proof repos carry every Lean file byte-identical
  between the last recorded head and the fresh head, so
  no name was gained and none lost in either. No
  regression is flagged.
- No pin moved without this ledger moving: every
  moved proof repo has its row restated below in this
  same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  9bd2735a98e9d3478610e3aa31f042261fe3ae3a, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the forty-eighth
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.
- idol — fresh head
  e9d05c2a4b0fbb439456f0fe88492f8cbca6c996, census pin
  561cf395 standing (proof-bearing content only).
  Proven: unchanged — all five Lean files are
  byte-identical between the last recorded head and
  the fresh head, counted at forty-five declarations
  by the watch method: the frontier file with its 7
  theorems on the premises its row records, the
  release tools files with their 20 and 5, the solver
  history file with its 10, and the proof data sample
  that remains test data, counted nowhere. The
  movement is two commits of specification and
  compiler work, three files added and five changed
  and none of them Lean. Gate: the release
  tools verdict stands in the high-impact addendum
  above at its named pin; the solver history file's
  gate remains unknown, and the full census of the
  release tools and solver developments remains
  owed.

The compiler port also moved and was read by tree at
its fresh head: no proof-assistant source stands in
it and its tree read was not truncated, so it remains
proof-free by the named check and carries no ledger
row.

## Watch refresh — 2026-11-20, the fiftieth hourly re-synthesis watch

The watch re-enumerated the estate at 574 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated. Evidence below rests on the tree and
commit reads at both heads of the moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in the moved proof repo: it carries every
  Lean file byte-identical between the last recorded
  head and the fresh head, so no name was gained and
  none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved
  proof repo has its row restated below in this same
  pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  8a4aee975bc2a0bbbc76fdb8a03b97ba25a2cc5c, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the forty-ninth
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The compiler port also moved and was read by tree at
its fresh head: no proof-assistant source stands in
it and its tree read was not truncated, so it remains
proof-free by the named check and carries no ledger
row.

## Watch refresh — 2026-11-20, the fifty-first hourly re-synthesis watch

The watch re-enumerated the estate at 574 repos, every
head read individually with no errors, and read the
moved repos by tree at their fresh heads in full, no
read truncated. Evidence below rests on the tree and
commit reads at both heads of the moved proof repo.
Placements stand at the census pins named in each row;
a full theorem-level re-census at each fresh head is
owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in the moved proof repo: it carries every
  Lean file byte-identical between the last recorded
  head and the fresh head, so no name was gained and
  none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved
  proof repo has its row restated below in this same
  pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  8f5c966582142d1be61b853b8231376a97d83e41, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the fiftieth
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

The compiler port and the sites repo also moved and
were read by tree at their fresh heads: no
proof-assistant source stands in either and neither
tree read was truncated, so both remain proof-free by
the named check and carry no ledger rows.

## Watch refresh — 2026-11-20, the fifty-second hourly re-synthesis watch

The watch re-enumerated the estate at 574 repos, every
head read individually with no errors, and read the
moved repo by tree at its fresh head in full, no read
truncated. Evidence below rests on the tree and commit
reads at both heads of the moved proof repo. Placements
stand at the census pins named in each row; a full
theorem-level re-census at each fresh head is owed
where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison found zero
  lost names in the moved proof repo: it carries every
  Lean file byte-identical between the last recorded
  head and the fresh head, so no name was gained and
  none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved
  proof repo has its row restated below in this same
  pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  310f038904f1d26bac511f5cc1e7d917c0b61f24, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the fifty-first
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

## Watch refresh — 2026-11-20, the fifty-third hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every
head read individually with no errors, and read the
moved and new repos by tree at their fresh heads in
full, no read truncated. Evidence below rests on the
tree and commit reads at both heads of the moved proof
repo and on the full first census of the new proof
repo. Placements stand at the census pins named in
each row; a full theorem-level re-census at each fresh
head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo carries
  every Lean file byte-identical between the last
  recorded head and the fresh head, so no name was
  gained and none lost; the new proof repo enters with
  its full set at its first census, so nothing of its
  stands lost. No regression is flagged.
- No pin moved without this ledger moving: the moved
  proof repo has its row restated below in this same
  pass, and the new proof repo's row is entered below
  in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head
  9237f128c1e6fcfe7c268fbf7de6de0d64f451d4, census pin
  d558669b standing. Proven: 11 theorems, unchanged —
  the same name set at the last recorded head and at
  the fresh head, which is the head the fifty-second
  watch landed; the four commits between them are that
  watch's annex, placement, ledger, and pins commits
  and carry no Lean change. Controls and gate stand as
  the second watch row records.

New row, entered at its first census:

- software-tensors-are-editable — census pin
  9d7afd54bf8e7c8dbd335b6530d4cdc6b6d14d18, its head at
  entry. Proven: 14 theorems in one Lean file — the
  delta algebra (6), reversal exactness (1),
  admissibility (2), and the view results (3), beside
  the two standing controls counted in that set. On
  named premises: none carried as a register; the
  composition result's one side condition — cross
  agreement at tied coordinates — stands inside its
  own statement, and its unconditional form stands
  refuted by the first control. Absent: the scale
  transport of the abstract core, the per-schema
  check, and the tie evidence method, owed or blocked
  as its annex records; the specification's policy,
  recurrence, and receipt sections proposed, not
  proved; and every behavioral effect unknown, with
  two fixture-bound behavioral cells blocked on
  fixtures not on the machine. Controls in tree: the
  two proved standing controls, inside the core file.
  Gate state: green at the pin by the repo's recorded
  log — warnings as errors, the escape scan, and an
  axiom line for all 14 theorems, one axiom-free,
  seven on propositional extensionality only, one on
  quotient soundness only, and five on that pair,
  ending in its subset check passing.

## Watch refresh — 2026-11-20, the fifty-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of each moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Both moved proof repos carry every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost in either. No regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head e25ad67ae7d663d3dd4e27e854ecb0476ade5238, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-third watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-tensors-are-editable — fresh head eb0c79ae5c78f4d46f03d0baa5d3891e6d994300, census pin 9d7afd54bf8e7c8dbd335b6530d4cdc6b6d14d18 standing. Proven: 14 theorems in one Lean file, unchanged — the same name set at both heads, because the one commit between them changes only the repo's own census file and every other file is byte-identical. On named premises, absent set, controls, and gate stand as its entered row records, with one census correction carried: a checkpoint in a local model store, missed at the founding census because the store's blobs carry no file extension, is now recorded in the source census as verified firsthand on disk, with the plain statement that no blocked item depends on it — so the two fixture-bound behavioral cells remain blocked, the specification's further sections remain proposed, and every behavioral effect remains unknown, exactly as its entered row records. A full theorem-level re-census at the fresh head is owed.

## Watch refresh — 2026-11-20, the fifty-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 2d93f74446d7a753a74afb52dba49dd8928b56b6, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-fourth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the fifty-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 82efc0f9d71eb2cc3abac92db15b2967979f4709, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-fifth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the fifty-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 804a2cefac1ed4d728882b888ae49495478f2c32, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-sixth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the fifty-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 3726560a90b40d37b2ff24b0c773e0e1b8a8d1f9, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-seventh watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the fifty-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 575 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 248e38622545e1150d82dd12174c0753dc77fb05, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-eighth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the sixtieth hourly re-synthesis watch

The watch re-enumerated the estate at 576 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. The one new repo was read by tree at its head in the same pass: its tree holds a single ignore file, so it is proof-free by the named check and carries no ledger row. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 16bb6ed6ba60dd9029eec728e3d22ba2bc6a4a59, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the fifty-ninth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the sixty-first hourly re-synthesis watch

The watch re-enumerated the estate at 576 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of each moved proof repo, and on the full first census of the newly proof-bearing repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Three moved proof repos carry every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost in any of them; the fourth moved repo is newly proof-bearing with fifty-four theorems gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated or entered below in this same pass. No synthesis defect is flagged.

Restated and entered rows, at their fresh heads:

- deterministic-llms — census pin set to its head 6151727a7ec67d15fdbb0fbfa48c2f305057aa69 on the first census in this pass. Proven: 54 theorems in four Lean files — the core file (31: the order laws, the pick laws with the uniqueness of the unbeaten candidate, determinism under any candidate order, certification sound and complete, rescoring and reweighting equal to recompute, the margin cone, axis locality, cache invisibility, the prefix law, and cached lookup); the search file (19: the dominance and sum laws, the archive holding exactly the Pareto front in any arrival order, per-factor minima plans, and Chebyshev weights reaching their target); the skipping file (2: drafted acceptance is exactly the rule's own generation, and batched acceptance under its premise); and the sparse file (2: a membership helper and the exact sparse rule). On named premises: the batched-scoring equality, carried inside the batch acceptance theorem's own statement and measured bitwise on the recorded run; the float forward pass's determinism and the axes' meanings carried as measured, never proved, as the repo states. Absent and unmeasured, as the repo prints: any other model, human quality judgment, long outputs, cross-machine determinism, native or Idol implementations, the exact cone region, and decompilation beyond the token embedding — the embedding-direction form refuted in its ledger at executed strength, the broader claim unmeasured. Controls in tree: the two proved standing controls in the search file (an unsupported front point reached by aimed Chebyshev weights, and no positive weighted sum picking it), beside executed controls counted as executed evidence — the clean fixture the gate replay must pass, the tampered copy it must fail, the do-nothing axis control, and the gamed controls labelled gamed and never counted. Gate: green at the pin by the repo's recorded log — the cold build completing, axiom lines for seventeen named theorems every one inside the standard three, and the check passing; the gate script fails closed on any axiom-check error after its recorded correction. The search file is carried, by the repo's own statement, copied unchanged from the redundant compute repo's seventh pull request — a second home for the same content.
- idol — fresh head 948b55cb764817b137260a77059499b34f14dbea, census pin 561cf395 standing (proof-bearing content only). Proven: unchanged — all five Lean files are byte-identical between the last recorded head and the fresh head, counted at forty-five declarations by the watch method: the frontier file with its 7, the retention file with its 20, the qualification file with its 5, the solver history file with its 10, and the proof data sample with its 3, which remains test data counted nowhere. The one commit between the heads changes only the Wasm source. On named premises, absent set, controls, and gate stand as the earlier rows record; the full census of the release tools and solver developments remains owed.
- idol-lib — fresh head f8a45b4cced3def7ab2684bab0b7e629d5957f8f, census pin 578b8b3a standing. Proven: 120 theorems, unchanged — all twenty Lean files are byte-identical between the census pin and the fresh head, the same name set at both, counted by the watch method over the tree at each pin. The twenty-one commits between the last recorded head and the fresh head land a new native port and its evidence, seven files added and eight changed, none of them Lean. On named premises, absent set, controls, and gate stand as its re-census row records: proven in source at the census pin, the gate at that pin unrecorded.
- software-is-a-closed-loop — fresh head 4fa8035ff75d2a460a070ab0a3394fd1b5391e21, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixtieth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-20, the sixty-second hourly re-synthesis watch

The watch re-enumerated the estate at 576 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head aca5e3658effcc90bd0d0d72d271d70225f8957d, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-first watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the sites repo, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-20, the sixty-third hourly re-synthesis watch

The watch re-enumerated the estate at 576 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The one moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 1c81fa03873a46425d076f97558587e99adaa770, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-second watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the sites repo, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-20, the sixty-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved and new repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of each moved proof repo and on the full first read of the new proof repo. Placements stand at the census pins named in each row; a full theorem-level re-census at each fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Both moved proof repos carry every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost in either; the new proof repo enters with fifty-eight theorems gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass, and the new proof repo has its row entered below. No synthesis defect is flagged.

Restated and entered rows, at their fresh heads:

- deterministic-llms — fresh head 8c4aa56af769ccba2b32e7a11c160cffc3f34227, census pin 6151727a7ec67d15fdbb0fbfa48c2f305057aa69 standing. Proven: 54 theorems, unchanged — every Lean file is byte-identical between the census pin and the fresh head, the same name set at both. The movement is two commits of executed-layer growth: twelve files added, the architecture, density, and multi-model harness modules with their frozen contracts and recorded reports, and seven files changed, among them the claims ledger and the specification — executed evidence at its own strength, counted nowhere in the proven column. On named premises, absent and unmeasured sets, controls, and gate stand as its entered row records.
- software-is-a-closed-loop — fresh head d0d257263adadc470576c36df876b01028679066, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-third watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-has-a-highest-minimal-axis — census pin set to its head 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646 on the first census in this pass. Proven: 58 theorems in two Lean files — the core file (42: the finite list machinery; monotonicity of the live set, the emergence measure, and the live count under subsets; structure forcing, a sufficient set engaging exactly the full set's hyperedges; existence of a highest minimal set for every instance; strict fall of the measure on every proper subset of a highest minimal set; maximality over every minimal sufficient set with uniqueness of the refinement vector; functoriality of the induced transformation with exact preservation of the engaged structure; the degenerate characterization with its empty and singleton contract corollary; and the corrected dead axis facts) and the controls file (16: the axis set enumeration and the standing checks on the specification's three named instances, proved by kernel decision). On named premises: the positivity of the weight of every hyperedge of size at least two, a field of the instance itself and load bearing for structure forcing. Refuted in the tree by standing control: the stronger dead axis sentence, and the reading that every minimal sufficient set is highest. Absent: the solver the specification contracts for stands proposed, with no implementation in the tree, and the arena validation instance the specification names is absent from the tree. Controls in tree: the sixteen standing controls above. Gate: green at the pin by the repo's recorded log — axiom lines printed for all 58 theorems, every one inside the standard three, and the subset check passing; the gate script is the widened family form and fails closed on any principle outside the allowed set.

The two other moved repos this watch, the compiler port and the sites repo, are not proof repos and carry no ledger rows: both were read by tree at their fresh heads, no proof-assistant source was found in either, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-20, the sixty-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head 8715ef37f8e9ce72462bb25b51ee4591e43b9586, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-fourth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The other moved repo this watch, the sites repo, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-20, the sixty-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head 704761096bc055eda998b28bf4b6af760f37c46b, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-fifth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the sixty-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head 031d22022d12825bab177d7a2edcc75bdf071cce, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-sixth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the sixty-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head 00e2c4358183d4a832d400bfc4ab61eb6e92005e, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-seventh watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the sixty-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of the moved proof repo. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo carries every Lean file byte-identical between the last recorded head and the fresh head, so no name was gained and none lost. No regression is flagged.
- No pin moved without this ledger moving: the moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head 46c480137ed01ab2355c0f0c9c54f600cff13be8, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head, which is the head the sixty-eighth watch landed; the four commits between them are that watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The two other moved repos this watch, the compiler port and the sites repo, are not proof repos and carry no ledger rows: both were read by tree at their fresh heads, no proof-assistant source was found in either, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-21, the seventieth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of each moved proof repo. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. Two moved proof repos grew (five names gained in one, ninety-five in the other), three carry every Lean file byte-identical between the last recorded head and the fresh head, and no name was lost in any of the five. No regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- deterministic-llms — fresh head a71ef232225fee24479449e19e9980c1b964f209, census pin 6151727a standing. Proven: 59 theorems, grown from 54 — the five new theorems stand in one new Lean file, the loop development (the admission, rejection, and scope soundness results and the two architecture coverage results), with no name lost and no sorry and no axiom declaration at either head. Premise set, controls, and gate state stand as the last refresh records; the check script and the recorded reports changed at the fresh head beside the new file.
- software-redundant-compute-expands — fresh head 1c794e29c897053658ce47e7a42cac6a712621f2, census pin 1ea28648 standing, full re-census at the fresh head owed. Proven: 335 declarations (287 distinct names), grown from 240 (192 distinct) — ninety-five names gained across three new proof files, the worklist development at fifty, the closure development at twenty-six, and the algorithm search development at nineteen, with none lost and no sorry and no axiom declaration at either head. The recorded check log in the proof folder grew at the fresh head. Premise set and controls stand as the last refresh records.
- idol-eyes — fresh head 4586347ff8316a85a2ca06016bb062546d21eef9, census pin 1dc24f4f standing. Proven: 61 theorems, unchanged — every Lean file byte-identical between the heads; the movement is a dated claims audit folder of scripts, raw outputs, and recorded check outputs, which is audit evidence at its own strength and is counted nowhere in the proven column. Premise set, controls, and gate state stand as the last refresh records.
- idol-lib — fresh head da0f414837a68e8e81246f1a04b33f6f4fa83424, census pin 578b8b3a standing. Proven: 120 theorems, unchanged — every Lean file byte-identical between the heads; the movement is one new data format port and its evidence, none of it Lean. Premise set, controls, and gate state stand as the last refresh records.
- software-is-a-closed-loop — fresh head 80b31f59e9aa7e18b9184c8913f1606a5732944d, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the six commits between them are the sixty-ninth watch landing and one further lane's re-census of the traceability repo inside this repo, landed by merge, and carry no Lean change. Controls and gate stand as the second watch row records.

The three other moved repos this watch, the compiler port, the relay, and the sites repo, are not proof repos and carry no ledger rows: all were read by tree at their fresh heads, no proof-assistant source was found in any of them, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-21, the seventy-first hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads in full, no read truncated. Evidence below rests on the tree and commit reads at both heads of each moved proof repo. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed where the row says so.

Defect-rule dispositions for this refresh:

- No proven set shrank. One moved proof repo grew (eight names gained, none lost), two carry every Lean file byte-identical between the last recorded head and the fresh head, and no name was lost in any of the three. No regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- idol-lib — fresh head c3ecf2652cf92d98480a2b1df82dca279b21721d, census pin 578b8b3a standing, the fresh head's growth recorded at delta strength. Proven: 128 theorems, grown from 120 — the eight new theorems stand in one new Lean file, the level three development of the space package (the level three counts and total, the receipt facts for qualified definitions, the first-version overlap fact, the level two unchanged fact, and the recorded runs passing), with no name lost and no sorry token and no axiom declaration at either head; three further Lean files were extended with no declaration change, the axioms file, the root file, and the data file. Premise set and controls stand as the last refresh records; the gate at the fresh head is unrecorded in this watch's reading.
- idol — fresh head bf96bd300c6f0c970b8e8bb7e1b654c2983c894f, census pin 561cf395 standing (proof-bearing content only). Proven: unchanged — all five Lean files are byte-identical between the last recorded head and the fresh head, counted at forty-five declarations by the watch method: the frontier file with its 7, the retention file with its 20, the qualification file with its 5, the solver history file with its 10, and the proof data sample with its 3, which remains test data counted nowhere. The one commit between the heads is gate hygiene and frontier benchmark record work. On named premises, absent set, controls, and gate stand as the earlier rows record; the full census of the release tools and solver developments remains owed.
- software-is-a-closed-loop — fresh head 02a254991791315483424df475b8f8db4815ad86, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventieth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The two other moved repos this watch, the compiler port and the sites repo, are not proof repos and carry no ledger rows: both were read by tree at their fresh heads, no proof-assistant source was found in either, and they remain proof-free by the named check, as their census entries record.

## Watch refresh — 2026-11-21, the seventy-second hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head ebde0c4497095de310aa0b661cccdeb0dc45914d, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-first watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the seventy-third hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 90af117067daa60f077a0f42e72a36bccae0fc75, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-second watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-21, the seventy-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 577 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head ae85d7aa2d17e023d2d366fe1f1dcaf209c90254, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-third watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.


## Watch refresh — 2026-11-21, the seventy-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 3b571361eee8033aff466ca7d9bb5fb6b10c00d4, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-fourth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The two other moved repos this watch, the compiler port and the sites repo, are not proof repos and carry no ledger rows: each was read by tree at its fresh head, no proof-assistant source was found in either, and both remain proof-free by the named check, as their census entries record. The one new repo this watch, the emergence program repo, carries no proof content in its tree at its founding head by the same check, so it takes no ledger row; its state is recorded as proposed in the census.


## Watch refresh — 2026-11-21, the seventy-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repos: no Lean file changed in this repo between its heads, and the emergence repo's Lean file was read in full at its fresh head. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; its eleven names stand unchanged. The emergence repo carried no proven set at its last recorded head and carries twenty-two theorems at its fresh head, so its set grew from none. No regression is flagged.
- No pin moved without this ledger moving: both moved proof repos have their rows restated or entered below in this same pass. No synthesis defect is flagged.

Restated and new rows, at their fresh heads:

- software-is-a-closed-loop — fresh head dd3fe3297adc349eb1870212be516b194a68ca4a, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-fifth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-emergence-is-decidable — new row, entered at its census pin ee3086521932c19f4ed0a054d4362cf21d525972, which is its fresh head. Proven: 22 theorems in one Lean file — the tally algebra, formation from the level-1 projection alone with first-reach stability under appends, restart exactness and prefix determination, the freeze laws, the exact group-step exchange, the joint tally as the componentwise sum of the level tallies, and the shuffle marginal laws. Premise set: the measure monotonicity obligation is proved in conditional form, its engaged-inclusion antecedent discharged by the view construction and not in the file; and the no-free-capability obligation stands as a named premise in the file, unproved, not an axiom, depended on by no theorem, discharged if ever only by the rung 6 certificate. Absent set: any in-repo proof of rungs 2, 4, 5, or 6 and of the endgame interfaces — proposed in the repo's specification, none proved in its tree. Refuted in-repo: the rung 3 capability claim, printed as no win in both registered families under both decision rules in the repo's own record at the pin. Controls in tree: the rung record's independent checker evidence — 336 runs replay-exact, 2352 of 2352 append-cut agreements, 672 of 672 restart agreements, 336 of 336 tally pair compositions, and zero load-bearing blocks in both ablations. Gate state: recorded in the repo's own tree at the pin — a cold compile clean with an axiom audit printing only the standard set and no sorry anywhere; the watch read the file and the record firsthand and did not re-run the compile, so the gate stands at recorded strength.


## Watch refresh — 2026-11-21, the seventy-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repos: no Lean file changed in this repo between its heads, and the emergence repo's three new Lean files and its three rung records were read in full at its fresh head, its earlier file byte-identical between the heads. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; its eleven names stand unchanged. The emergence repo carried twenty-two theorems at its last census pin and carries sixty-three at its fresh head, with every earlier name standing, so its set grew by forty-one. No regression is flagged.
- No pin moved without this ledger moving: both moved proof repos have their rows restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 3f9a5e3d01e6a4bafa68a12febff1ee94a48a1e9, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-sixth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-emergence-is-decidable — restated at its census pin cddf398adceac41c4c171b8b012d9dc07af7e7f5, which is its fresh head. Proven: 63 theorems in four Lean files — the twenty-two of rung 3 standing unchanged, joined by fourteen for rung 4 (extraction determinism, information equality, selection-only carriage, null exactness, and carriage replay), ten for rung 5 (restart and replay exactness, the tally at every cut, and curve well-definedness), and seventeen for rung 6 (decidability, detector correctness, margin monotonicity, certificate checkability, and reweighting stability in scoped form only). Premise set: the rung 3 no-free-capability obligation and the measure monotonicity obligation in its conditional form stand as before; the rung 4 transfer bound stands as a named premise; one rung 5 obligation stands as a premise by construction review and its accumulation monotonicity obligation as a named premise; and the rung 6 soundness and completeness obligations stand as named premises, each stated as a definition depended on by no theorem. Absent set: any in-repo proof of rung 2 and of the endgame interfaces — proposed in the repo's specification, none proved in its tree. Refuted in-repo: the rung 4 transfer claim, measured exactly zero in both registered pairs under both decision rules; the rung 5 compounding claim, its field gain below the frozen control spread under both rules and its region gain matched by the frozen control; and the certificate precondition — the earlier records do not separate, the needed threshold does not exist, and all twenty-five instances stand not certified in the repo's own rung 6 record, in agreement with every battery outcome. Controls in tree: the rung records' independent checker evidence — rung 4 zero failures with replay, append-cut, restart, view, extraction, and search agreement exact; rung 5 zero failures across replay, cut folds, append-cut equality, restarts, and budget shapes; rung 6 zero failures on all twenty-five certificates, seven of seven fixtures in agreement, and no verdict flips across the registered band. Gate state: recorded in the repo's own tree at the pin — each new file a cold compile clean with an axiom audit printing only the standard set and no sorry beyond the header word in the rung 4 file; the watch read the files and the records firsthand and did not re-run the compiles, so the gate stands at recorded strength.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.


## Watch refresh — 2026-11-21, the seventy-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors. Evidence below rests on the tree and commit reads at both heads of the one moved proof repo: no Lean file changed in this repo between its heads — both Lean files are byte-identical at the two pins, with the same eleven theorem names counted at each. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; its eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head a1eaec3f29ac8feafeafaad4725fd4d2cc4f3255, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-seventh watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the seventy-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head c7bbc44b32790a4a9676207635eb1a4af8d38815, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-eighth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-21, the eightieth hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors. Evidence below rests on the tree and commit reads at both heads of the one moved proof repo: no Lean file changed in this repo between its heads — both Lean files are byte-identical at the two pins, with the same eleven theorem names counted at each. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; its eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head d262e09378890aa2bdaddb28f4fe8495b06e0a9b, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the seventy-ninth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the eighty-first hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually. One first read failed on a transport stream error; it was re-read individually and matched its last recorded head, so the final reads carry no errors. Evidence below rests on the tree and commit reads at both heads of the moved proof repos: the emergence repo's four rung Lean files are byte-identical between its heads and its new audit Lean file was read in full at its fresh head, and no Lean file changed in this repo between its heads. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. The emergence repo carried sixty-three theorems at its last census pin and carries sixty-eight at its fresh head, with every earlier name standing, so its set grew by five. This repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; its eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: both moved proof repos have their rows restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-emergence-is-decidable — restated at its census pin 8eb2906bbf4266129056fcad5b3318dfb2fc31dc, which is its fresh head. Proven: 68 theorems in five Lean files — the sixty-three of rungs 3 to 6 standing unchanged in their four files, joined by five in a new audit file (a split lemma over list membership, a sum bound over a duplicate-free family, the engaged bound, a carry step, and the closing theorem) proving the accumulation monotonicity premise for the concrete measure, the total weight of a cut's engaged edges, in conditional form: for any two cuts in order, if every edge of the earlier cut is a member of the later cut's family and the live set only grows, the earlier measure is at most the later. Premise set: the accumulation monotonicity premise is discharged by this file and leaves the premise set; one named hypothesis stands inside the proof, a duplicate-free edge family, stated in the audit record as constructional in the rung 5 instrument. The three remaining carried premises stand: the rung 3 no-free-capability obligation and the rung 4 transfer bound, both hanging from the rung 6 certificate soundness theorem whose threshold does not exist because the earlier records do not separate; and the rung 5 no-forgetting obligation, its content verified in full on the persisted artifacts by the audit, its discharge awaiting the endgame derivation machinery. The rung 3 measure monotonicity obligation's conditional form and the rung 6 completeness obligation stand as the seventy-seventh watch row records, and reweighting stability stands proved in scoped form only. Absent set: any in-repo proof of rung 2 and of the endgame interfaces — proposed in the repo's specification, none proved in its tree. Refuted in-repo: the rung 3 composition claim, the rung 4 transfer claim, and the rung 5 compounding claim, each falsified as registered in the repo's own records, and the certificate precondition — the earlier records do not separate, the needed threshold does not exist, and all twenty-five instances stand not certified; the audit record states that no battery outcome is reinterpreted by it, and the discharged premise's antecedent held at exactly one of fifty-six measured checkpoint pairs. Controls in tree: the rung records' independent checker evidence stands as the seventy-seventh watch row records, joined by the audit record's own gate result for the new file. Gate state: recorded in the repo's own tree at the pin — the new audit file a cold compile clean with an axiom audit printing only the standard allowed set and no sorry beyond the header word; the watch read the file and the record firsthand and did not re-run the compile, so the gate stands at recorded strength.
- software-is-a-closed-loop — fresh head 9fe3f69c4e92e2eab28f3e1b2f08db04cac69527, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eightieth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the eighty-second hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors. Evidence below rests on the tree and commit reads at both heads of the one moved proof repo: no Lean file changed in this repo between its heads — both Lean files are byte-identical at the two pins, with the same eleven theorem names counted at each. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. This repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; its eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head ba4cbf9c3506e13a937e8f50ab841177a49dbedd, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-first watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the eighty-third hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 4463db950fd4d8f1aab2a5bd2b118678d349a62d, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-second watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

The one other moved repo this watch, the compiler port, is not a proof repo and carries no ledger row: it was read by tree at its fresh head, no proof-assistant source was found in it, and it remains proof-free by the named check, as its census entry records.

## Watch refresh — 2026-11-21, the eighty-fourth hourly re-synthesis watch

The watch re-enumerated the estate at 578 repos, every head read individually with no errors, and read the moved repo by tree at its fresh head. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head d2cb9195e099d3cb7388a889daf8266966b82480, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-third watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the eighty-fifth hourly re-synthesis watch

The watch re-enumerated the estate at 579 repos, every head read individually with the empty repos each confirmed on a second read, and read every moved proof repo by tree at both heads. Evidence below rests on the tree, commit, and content reads at both heads of each moved proof repo. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed for every moved repo whose pin stands.

Defect-rule dispositions for this refresh:

- No proven set shrank in count. Seven moved proof repos grew or stood unchanged with no name lost. One name loss is flagged, not absorbed: the traceability repo lost one name, the premise-carrying head theorem quoted in its annex delta, while its count grew from 43 to 56 — its premise is owed a re-trace against its replacements in the full re-census, and until that re-trace lands the lost name's premise is carried as unresolved in this row. No other regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass, and the one new proof repo's row is entered below at its census pin. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- idol-lib — fresh head c919ad409e112964ac2515216d849c780813ae48, census pin 578b8b3a standing. Proven: 128 theorems, unchanged — every Lean file byte-identical between the last recorded head and the fresh head, the same name set at both, counted by the watch method over the tree at each pin, with no sorry token and no axiom declaration. The four commits between the heads land an exact battery subject and its test in the space qualification folder, none of them Lean. Premise set, controls, and gate state stand as the seventy-first watch row records: proven in source at the census pin, the gate at the fresh head unrecorded in this watch's reading.
- software-doesnt-have-to-regress — fresh head f07f8e7595eb70afe84a40403f54481dfc22f6cc, census pin c36829da standing, full re-census at the fresh head owed. Proven: 203 declarations across 17 Lean files by the watch method, grown from 137 across 14 — sixty-six names gained, none lost, no sorry token and no custom axiom declaration at either head. The growth is one commit landing a readings audit: the replacement relation's reflexivity, transitivity, and admission characterization, the certified and permitted characterizations, and the refusal form of each conjunct of the reading — cost, capability, context, and envelope — beside counterexamples in the tree, among them that a cost-only reading accepts a capability deletion, that a scalar score improvement can regress, and that a fixed budget admits a regressing pair, with three negative control files added. Premise set, absent set, and gate state stand as the annex records at the census pin, restated for the new package in the owed re-census.
- software-emergence-is-decidable — fresh head 5b7a0e022f1b5023f33a444e5334c026f8c7f147, census pin 8eb2906b standing, full re-census at the fresh head owed. Proven: 78 declarations in six Lean files by the watch method, grown from 69 in five at the last recorded head — nine names gained, none lost, no axiom declaration, and the only sorry token the new file's header phrase stating it has none. The four rung files and the audit file are byte-identical between the heads, so the sixty-eight theorems of the census at the pin stand unchanged; the nine new declarations are the filter and sum lemmas of an indexed fold scan in one new file, whose companion record closes the fold form of the scan gap — one indexed pass answering the tick, message, and subset counterfactuals exactly — and names the system-level replay form as that gap's only remaining content. Premise set: the three carried premises stand as the eighty-first watch row records; the scan record adds no premise and discharges none. Absent and refuted stand as that row records: any in-repo proof of rung 2 and of the endgame interfaces absent, and every registered capability claim refuted as registered. Gate state: recorded strength — the watch read the new file and its record firsthand and did not re-run the compile.
- software-has-a-highest-minimal-axis — fresh head b12fdb2411f23df33c02f4695f0b2d8c09ecaa89, census pin 63d9d3f standing, full re-census at the fresh head owed. Proven: 58 theorems, unchanged — no Lean file changed between the heads, the same name set at both, counted by the watch method, on the one named premise the sixty-fourth watch row records: the positivity of the weight of every hyperedge of size at least two. Absent set movement: the solver the specification contracts for no longer stands absent — two commits landed a deterministic finite solver in a new folder, with its model, an independent checker, fixtures, and a validation record, recorded here at delta strength from the tree and commit reads; its validation is the repo's own record, read firsthand and not re-run by this watch. Controls and gate stand as the sixty-fourth watch row records, with the proof folder's check log and script changed at the fresh head.
- software-is-a-closed-loop — fresh head a8c39c06481f066d9b96da80abaab213d84c754f, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-fourth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-is-composable — fresh head 99f9a0ba67097876e6dcba5886712db456479991, census pin a3058ba6 standing, full re-census at the fresh head owed. Proven: 149 declarations across 21 Lean files by the watch method, grown from 70 across 16 — seventy-nine names gained, none lost, no sorry token and no custom axiom declaration at either head. The growth is six commits landing an audited interaction model: the interaction developments with their monotonicity and recheck characterizations, the legacy embedding, and the counterexamples standing in the tree — individually safe components composing to a leak, and rule and topology changes breaking a global refinement — beside two audit files, five negative control files, and a verification folder of recorded gate logs and receipts for one candidate pin. Premise set and absent set stand as the annex records at the census pin, restated for the new package in the owed re-census; gate evidence at the fresh head is the repo's recorded receipts, read firsthand and not re-run by this watch.
- software-is-more-traceable-than-you-think — fresh head 2d35b503aa74b2ac2397d9cc6af0c4049c609b4e, census pin 4420fb1e standing, full re-census at the fresh head owed. Proven: 56 declarations across 5 Lean files by the watch method, grown from 43 across 4 — fourteen names gained and one lost, no sorry token and no custom axiom declaration at either head. The one lost name is flagged above: the premise-carrying head theorem quoted in the annex delta no longer stands in the tree, and the premise it carried — the contribution assignment behind the head claim — is carried here as unresolved until the owed re-census re-traces it against the recorded-edge and recorded-head forms that replaced it. The new results prove the contributor selection sound and order-sensitive, refuse a missing edge, and prove the failure forms beside those replacements, in a new return controls file of ten declarations and three new declarations in the main proof file. Gate evidence at the fresh head is the repo's recorded receipts in its new receipts folder, read firsthand and not re-run by this watch; the independent re-run gap recorded in the annex stands.
- software-redundant-compute-expands — fresh head 84eb1cd954dcc7b927c5dd42b96caa62a8784e1e, census pin 1ea28648 standing, full re-census at the fresh head owed. Proven: 362 declarations across 25 Lean files by the watch method, grown from 335 across 23 — twenty-seven names gained, none lost, no sorry token and no axiom declaration at either head. The growth is three commits landing an admission development in two new Lean files: the admission claims sound over grounded facts, the honest replay and reach forms, and the named refusal forms, beside an Idol kernel example with its controls, mutants, and replay receipts standing as executed evidence at its own state, not a machine-checked refinement of the Lean model. Premise set and controls stand as the seventieth watch row records; the recorded check log in the proof folder changed at the fresh head.
- software-proofs-are-portable — new row, entered at its census pin d2dd570c01a94304f34bb2a7c49bb4f56b28a5d0, which is its fresh head. Proven: 4 theorems in one Lean file over an abstract digest, depending on no axioms at all — soundness (verification of the combined artifact implies the certified property of the artifact alone), the transplant bound (a transplant verifies only if the two artifacts share a digest), the refusal (a different-digest artifact refuses with the genuine certificate, no further premise), and sameness under its one named premise. Premise set: the separation premise — the digest separates the two artifacts in question, the finite-range form of collision resistance, assumed in the open for the digest the instance uses and proved nowhere in the repo — and the validity of the underlying certificate as issued, whose soundness stands in the issuing repo at its pin. Absent set: any issuer authentication beyond the anchored digests, and any re-issuance of the issuing gate's remaining releases — both named as not claimed in the repo's spec. Controls in tree: the standing attack battery — determinism, the honest bundle, a flip in the artifact, a flip in the certificate, a transplant onto the earlier tree, and the forgery over the genuine artifact, the first passing and the attack forms each refused — beside the executed control that the detached form falls to the same forgery. The instance's carried reading stands not certified, its three unmeasured dimensions standing as blockers; the construction upgrades no reading. Gate state: recorded pass at the pin in the instance folder — escape scan, cold build with warnings as errors, and the battery — read firsthand by this watch and not re-run, so the gate stands at recorded strength.

## Watch refresh — 2026-11-21, the eighty-sixth hourly re-synthesis watch

The watch re-enumerated the estate at 581 repos, every head read individually with no errors, and read both new proof repos in full at their heads and this repo by tree at its fresh head. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh head is owed for this repo.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. Both new proof repos enter with their full proven sets at their census pins. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass, and both new proof repos rows are entered below at their census pins. No synthesis defect is flagged.

Restated row, at its fresh head:

- software-is-a-closed-loop — fresh head 3be6373a799dd40543c5bdf577fde1a17a98ffb9, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-fifth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

New rows, entered at their census pins:

- software-checking-is-choral — new row, entered at its census pin f1ce1cb45bb25475fb2dca522a220cb4b5347240, which is its fresh head. Proven: 14 theorem declarations in two Lean files — the cone point result, the joined verdict over a covering family of three cones in both directions, the audit point and audit join results, and their supporting fuel, fold, and helper lemmas, beside the two rank lemmas of the controls file. Recorded axiom states at the pin: the fuel and fold results on no axioms, the main results on propositional extensionality and quotient soundness only, the controls on propositional extensionality only. Premise set: a rank function decreasing along every dependency, a boundary agreeing with the whole check outside the cone, and an audit reading the environment only at the module and its dependencies, beside the operational premise that each checker runs the subject pinned toolchain. Absent set: the split gate run over its instance, and any wall-clock, speedup, or fraction figure — all named as not claimed, the runs standing as future work. Controls in tree: two standing controls on concrete two-module developments, proving the boundary premise and the coverage premise each load-bearing. Gate state: the gate script stands in the tree — escape scan, cold compile with warnings as errors, and the allowed-principle check — and the readme records the audit at the founding pin; no recorded gate log file stands in the tree, and this watch did not re-run the gate, so the gate stands at recorded strength.
- software-estate-is-censused — new row, entered at its census pin 1a67fef4d6d9bca33e41844f7f66d93678a96b65, which is its fresh head. Proven: 5 theorem declarations in one Lean file — the two point-update lemmas and the three headline results: one append step preserving the accounting exactly, every append sequence preserving it, and an untouched repo keeping its pin and its count — over an opaque counting function, so the results hold for every declaration basis. Recorded axiom states at the pin: the soundness and steps results on propositional extensionality and quotient soundness, the kept result on propositional extensionality alone. Premise set: counting by declaration at a named head under the basis stated in the counter header, shared by both accountings, and the append-only property that a run moves a pin or does not and changes nothing else. Absent set: counts at pins outside its window and under any other basis, both named as not stated. Controls in tree: the standing checker over the landed evidence, failing closed on the first disagreement between the incremental and from-scratch accountings, beside the evidence file holding both tables at every run in its window with empty disagreement lists throughout. One named exclusion stands in the open: the incrementally safe content branch entry does not resolve at its census pin and is carried uncounted by both accountings, not as an agreement. Gate state: the readme records the Lean gate cold green with warnings as errors at the landing pin; this watch read the sources, scripts, and evidence as text only and executed none of them, so the gate stands at recorded strength.

## Watch refresh — 2026-11-21, the eighty-seventh hourly re-synthesis watch

The watch re-enumerated the estate at 582 repos, every head read individually with no errors, and read the whole trees of the moved and new proof repos at both heads where a prior head stands. Evidence below rests on the tree and commit reads at both heads of the moved proof repos. Placements stand at the census pins named in the rows; a full theorem-level re-census at each fresh head is owed for the moved repos.

Defect-rule dispositions for this refresh:

- No proven set shrank. The name comparison at both moved proof repos found no name lost, and this repo's eleven names stand unchanged. The one name lost at the traceability repo's previous head stays flagged at that strength; this movement neither restores it nor loses another. No regression is flagged.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass, and the new proof repo row is entered below at its census pin. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-doesnt-have-to-regress — fresh head fdca9789547ad62536ab71d7689d99dc7754a116, census pin c36829da standing, full re-census at the fresh head owed. Proven: 385 declarations across 27 Lean files by the watch method, grown from 203 across 17 — no name lost, no sorry token and no custom axiom declaration at either head. The growth is two commits landing the dynamic release process: cached decisions equal to fresh checking, exact replay reusing every judgment, recertification required on context change with stale evidence refused, reversible edits restoring state while preserving append-only history, and greedy arrival, adoption, and selection staying safe while an invalid baseline blocks deployment, beside its worked valid and refused example forms. Premise set, absent set, controls, and gate state stand as the annex records at the census pin, restated for the new package in the owed re-census; gate evidence at the fresh head is the repo's recorded workflow and check script, read firsthand and not re-run by this watch.
- software-is-more-traceable-than-you-think — fresh head f8424a64b319bad8888e6cb54d9a01e7d8a3dc7a, census pin 4420fb1e standing, full re-census at the fresh head owed. Proven: 284 declarations across 20 Lean files by the watch method, grown from 56 across 5 — no name lost, no sorry token and no custom axiom declaration at either head. The growth is six commits landing the cumulative incremental hypergraph pipeline: reuse exact against fresh computation, zero work on a hit and one on a miss, the shared diamond compression from the exponential form to the linear form, every binary selection correct, and fabricated cached or captured values refused, beside the recorded retained row and proof counts across seven revisions. Premise set, absent set, and controls stand as the annex records at the census pin, restated for the new package in the owed re-census. Gate evidence at the fresh head is the repo's recorded campaign, gate, and test receipts, read firsthand and not re-run by this watch.
- software-is-a-closed-loop — fresh head 485577498b5ea8fc368ebe6c741ef1dfd49b84c3, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-sixth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

New row, entered at its census pin:

- software-qualification-is-two-sided — new row, entered at its census pin 6d68fbd81f45865050e0a7411a8e91a3919b6c5f, which is its fresh head. Proven: 19 theorem declarations in three Lean files — the boundary result, the margin result, and the growth result, beside their space, distance, and fold lemmas and the three standing controls. Recorded axiom states at the pin: the boundary and margin results on propositional extensionality, classical choice, and quotient soundness; the growth result on propositional extensionality and quotient soundness; one control on propositional extensionality alone and two controls on no axioms. Premise set: the configuration space finite by the definition of qualification, taken as an explicit list; distance counted in single-premise changes; and strengthening as enlargement of the qualified set. Absent set: any predictive verdict on the hinge width — the registered flip test is void on its instance with zero observed flips — and any width figure for a subject other than the recorded frontier instance, both named as not claimed in the repo. Controls in tree: three standing controls on concrete data, proving the failing existence premise load-bearing, the monotonicity not vacuous, and the strengthening premise load-bearing. Gate state: the gate script stands in the tree — escape scan, cold compile with warnings as errors, and the allowed-principle check — and the readme records the audit at the founding pin; no recorded gate log file stands in the tree, and this watch did not re-run the gate, so the gate stands at recorded strength.

## Watch refresh — 2026-11-21, the eighty-eighth hourly re-synthesis watch

The watch re-enumerated the estate at 582 repos, every head read individually, with one first read failing on a transport stream error and matching its last recorded head on an individual re-read, so the final reads carry no errors, and read the moved repo by tree at its fresh head. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 924a52e42c90ae51d27d9614ad5d13360dfd031f, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-seventh watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the eighty-ninth hourly re-synthesis watch

The watch re-enumerated the estate at 582 repos, every head read individually, with the eighty empty repos returning no branch and matching their recorded empty state, so the final reads carry no errors, and read the moved repo by tree at its fresh head. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 788ca52c92d7b5c2e54f29571f6cf8a54abc3195, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-eighth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-21, the ninetieth hourly re-synthesis watch

The watch re-enumerated the estate at 582 repos, every head read individually, with the eighty empty repos returning no branch and matching their recorded empty state, so the final reads carry no errors, and read the moved repos by tree at their fresh heads. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. The other moved repo, the compiler port, carries no proof-assistant content at its fresh head and has no ledger row. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head 0b0f4365cd51524264081c4f507aafa054ea6fed, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the eighty-ninth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.

## Watch refresh — 2026-11-22, the ninety-first hourly re-synthesis watch

The watch re-enumerated the estate at 582 repos, every head read individually, with the eighty empty repos returning no branch and matching their recorded empty state, so the final reads carry no errors, and read each moved proof repo by tree at its fresh head and at its last recorded head, with no read truncated. Placements stand at the census pins named in the rows; a full theorem-level re-census at the fresh heads is owed where the annex deltas say so.

Defect-rule dispositions for this refresh:

- One proven set shrank, flagged as a regression: the solvable repo's total count fell from fifty-four to fifty-three, and twenty-two distinct names present at its last recorded head are absent at its fresh head, against twenty-two gained. Whether the lost names are renames is unproven on this reading, so the flag stands and is not silently absorbed. No other moved proof repo lost a name.
- No pin moved without this ledger moving: every moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- idol-eyes — fresh head 48ca231dc5ad668a55e4a6a0b71df7875b27d16c, census pin 1dc24f4f standing. Proven by the watch method: 97 declarations, up from 61, with 36 distinct names gained and none lost, in six Lean files, up from four; two new Lean files carry the growth, an action development and a plan development. Premises, absent set, controls, and gate stand as the annex census records, with the gate state at the fresh head unrecorded in this reading.
- idol-lib — fresh head f550d3aa8df7af9d9819d6a23830e3e728813781, census pin 578b8b3a standing. Proven: 128 declarations, unchanged — the same name set at the last recorded head and at the fresh head, every Lean file byte-identical between them; the movement is a new kernel evidence folder and a ledger change only. Controls and gate stand as the annex records.
- software-doesnt-have-to-regress — fresh head a2def8ab06a992de8ba42a12f90e20d44f5d8823, census pin c36829da standing. Proven by the watch method: 434 declarations, up from 385, with 49 distinct names gained and none lost, in thirty Lean files, up from twenty-seven; the growth is three new definitional audit developments. Premises, absent set, controls, and gate stand as the annex census records.
- software-frontier-is-solvable — fresh head 6b04ab26d33c092816d2aa82b5ef5e6c53631cab, census pin 6a41c7be standing. Proven by the watch method: 263 declarations, up from 240, with 23 distinct names gained and none lost, in eighteen Lean files, up from sixteen; the growth is a link hypergraph development and a link Pareto development. Premises, absent set, controls, and gate stand as the annex census records.
- software-is-a-closed-loop — fresh head 58facb0b7595c1ad4a122e3076afcc947309a061, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the ninetieth watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
- software-is-incrementally-safe — fresh head 9452fac91f7ddd555d590d76ecfbb65689be28d5, census pin 8ad1dd26 standing. Proven by the watch method: 281 declarations, up from 277, with 4 distinct names gained and none lost, in thirty-four Lean files, up from thirty-two; the growth is a submitted trace system development and a gate axioms file, beside the new gate folder. Premises, absent set, controls, and gate stand as the annex census records, and the head and branch contents stay distinct as recorded there.
- software-is-more-traceable-than-you-think — fresh head 03ed5be28011f26978350a90d16faa48e05324e7, census pin 4420fb1e standing. Proven by the watch method: 307 declarations, up from 284, with 23 distinct names gained and none lost, in twenty-two Lean files, up from twenty; the growth is a headed return development and its controls. Premises, absent set, controls, and gate stand as the annex census records.
- software-is-solvable — fresh head ccf7a358ba8e6b8a614a10c32182230822701276, census pin 5bbceee7 standing. Proven by the watch method: 53 declarations, down from 54, with 22 distinct names gained and 22 lost, the distinct count standing at 53 at both heads, in seven Lean files at both heads; two Lean files were removed and one new Pareto development was added in a restructure. This row carries the regression flag recorded above. Premises, absent set, controls, and gate stand as the annex census records.
- software-optimality — fresh head 06b09449d580e6192138deedbdac2a341c7c51a7, census pin b52c3170 standing. Proven by the watch method: 760 declarations, up from 692, with 66 distinct names gained and none lost, the distinct count rising from 596 to 662, in eighty-two Lean files, up from eighty; the growth is a closure strength development and a frontier obligations controls development, beside changes in the composition, frontier, Pareto, campaign, and selection developments. Premises, absent set, controls, and gate stand as the annex census records.

## Watch refresh — 2026-11-22, the ninety-second hourly re-synthesis watch

The watch re-enumerated the estate at 582 repos, every head read individually, with the eighty empty repos returning no branch and matching their recorded empty state, so the final reads carry no errors, and read the moved repo by tree at its fresh head. Evidence below rests on the tree and commit reads at both heads of the moved proof repo: no Lean file changed between them. Placements stand at the census pins named in the row; a full theorem-level re-census at the fresh head is owed.

Defect-rule dispositions for this refresh:

- No proven set shrank. The moved proof repo's Lean files are unchanged between the last recorded head and the fresh head, so no name was lost; this repo's eleven names stand unchanged. No regression is flagged.
- No pin moved without this ledger moving: the one moved proof repo has its row restated below in this same pass. No synthesis defect is flagged.

Restated rows, at their fresh heads:

- software-is-a-closed-loop — fresh head b07a75ed98d69336460135483a983e3187308040, census pin d558669b standing. Proven: 11 theorems, unchanged — the same name set at the last recorded head and at the fresh head; the four commits between them are the ninety-first watch's annex, placement, ledger, and pins commits and carry no Lean change. Controls and gate stand as the second watch row records.
