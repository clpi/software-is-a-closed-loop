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

## software-is-more-traceable-than-you-think — pin 4420fb1e

- Proven in this repo: 5 theorems of an invoice example, at
  fixture scale, on its recorded transcript (3 on propext and
  quotient soundness, 2 axiom-free), with a recorded rejected
  mutation.
- Absent in this repo: the thesis itself — the witness
  hypergraph construction, the grain determination, and the
  platform-independence proof are recorded in its readme as
  implemented in a lane and not yet landed here. State:
  claimed, not proven, in-repo; the grain map proposed.
  (Live head moved to 5f84b051 after this census; what landed
  there is the continuous job's next re-census.)

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
