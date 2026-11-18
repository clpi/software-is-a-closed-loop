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

## software-is-quantifiable — census pin 37917a41 (head ba27febf)

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

## software-optimality — census pin 0ea4626b (head aab49084)

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

## software-is-composable — pin 033c12c0

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

## software-is-incrementally-certifiable — pin f3b9f896

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

## software-is-incrementally-safe — head 94661358; branch 5c1006a6

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

## software-doesnt-have-to-regress — pin 24d36c13

- Proven: 0. On named premises: none stated.
- Absent: the entire claim — a release process with
  per-symbol certification never has to regress — has no
  formal statement in the repo (two-line readme, no
  toolchain pin). Its components are proven elsewhere
  (synthesis.md section 3.8); the release-level statement is
  proven nowhere.
- Controls in tree: none. Gate state: none.

## software-doesnt-need-review — pin ae5f3918

- Proven: 0. On named premises: none stated.
- Absent: any formal statement of when manual review is
  redundant given per-symbol certification — the audit's
  verdict is that no such statement exists to check. The
  proposal half of the readme is likewise absent as a design.
- Controls in tree: none. Gate state: none.

## software-is-solvable — pin 815e125f

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

## software-frontier-is-solvable — pin c7ffc6d0

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
