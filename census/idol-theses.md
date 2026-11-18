# Census — idol-theses

## Pin and identity

- Live head (gh API, read first): `d207be6e23b2f9d72b5b16e1d85b7ea3003ec56c`
- Clone head (shallow clone, depth 1): same — verified match.
- Visibility (gh API): public. Default branch: master. API description: none.
- Created (gh API): 2026-11-18.
- Toolchain pin (the toolchain file): Lean 4, version 4.19.0. No other dependency; the package manifest lists no packages.
- Files: a readme (92 lines), a future work file (240 lines), six Lean modules plus the package file, and a check script. There is no recorded check log and no sums file in this repo — see the controls section for what that means for gate evidence.
- Structure of the census itself: this repo is a partial census by design. One tranche is proved natively here (three files), one tranche is cited to two family homes (nine theses, statements and states carried, proofs elsewhere), and the remainder stands as named future work with closing conditions (sixteen entries). The split is recorded exactly below; nothing in the second or third part is counted as proved here.

## Thesis, in plain English

Every claim of the Idol program that an observation could refute is a thesis, and each thesis belongs in one native Lean home at its strongest reachable form, stated with the observation that would refute it. A thesis already proved at full strength in a family home is cited, never proved again. A thesis with a fixed statement and no home yet is proved here natively where reachable; what is not reachable stands as named future work with its closing condition, never as a silently weakened theorem. Evidence states use four forms — settled intent, proposed semantics, implemented behavior, verified behavior — with proven, disproven, and premise used where the Lean record earns them.

## Controls and zero-sorries evidence

- Check script (the repo's recorded gate design; no run was performed by this census): it rejects any admitted-proof word, custom-axiom word, or compiler escape hatch word in every Lean file at the top level; it fails if any top-level Lean file is outside its compile list, so no file can stand outside the gate; it compiles each file with warnings as errors; and it runs an audit file whose printed axiom sets must stay inside the standard three.
- Gate evidence state: there is no recorded check log in the repo, so a passing run is not evidenced in the repo itself. The gate's verdict at this pin is therefore unknown from recorded logs; what this census verified firsthand is the script's design, the source proofs below, and the scan next.
- This census's own scan of every Lean file in the clone: no admitted-proof token, no custom-axiom declaration, and no native-decision token anywhere. Zero admitted proofs at the source level.
- Axiom audit file: it prints axiom sets for 14 of the native theorems (a subset — see the census notes). The readme states the allowed set is only the standard three, and no custom axioms are used.

## Definitions carried

- A class of terms is carried as its characteristic function (a term-to-truth-value function) — the same representation the witness fold of the qualification construction is built from.
- The information order: one class is below another when every member of the first is a member of the second.
- Merge is the union of two classes; the shared part is their overlap; the empty class has no members.
- The fold of a witness feed is the class of exactly the witnesses the feed presents; the deduplicated feed keeps each witness at its first presentation only.
- Frontier file: a cost is one natural number per axis, axes named by a finite list. Weak dominance is no axis worse; strict dominance is weak dominance and strictly better on one named axis. The frontier of a list is its members that no member of the list strictly dominates. A decidable dominance test (all axes no worse, any axis strict) is proved equal to the strict relation.
- The cited registry is data: one row per cited thesis, naming its short name, its home, the pin the citation was read at, and its evidence state as a string.

## Theorem census — native tranche, 35 named theorems (plus one private helper)

Token column quotes at most one load-bearing word per theorem. Axioms column: this repo has no recorded per-theorem axiom log; the audit file prints sets for the 14 marked theorems, and the gate (by design) rejects any set outside the standard three. Where the audit does not print a theorem, its axiom set is unknown from the repo's records.

### The merge module — 20 theorems (the foundation claim, algebraic half)

| Token | Hypotheses → conclusion | Axioms |
|---|---|---|
| `refl` | No hypotheses → the information order is reflexive: every class is below itself. | not printed |
| `trans` | One class below a second and the second below a third → the first is below the third. | not printed |
| `antisymm` | Two classes each below the other → they are equal. | printed in audit |
| `bottom` | No hypotheses → the empty class is below every class. | not printed |
| `upper` (left) | No hypotheses → each part is below the merge of the pair. | not printed |
| `upper` (right) | No hypotheses → the other part is below the merge of the pair. | not printed |
| `least` | A class above both parts → it is above their merge. Merge is the least upper bound; with the two upper bounds this is the provision the foundation claim was missing, at this representation. | printed in audit |
| `assoc` (merge) | No hypotheses → merge is associative. | printed in audit |
| `comm` (merge) | No hypotheses → merge is commutative. | not printed |
| `idem` (merge) | No hypotheses → merging a class with itself changes nothing. | not printed |
| `empty` (merge, left) | No hypotheses → merging the empty class on the left changes nothing. | not printed |
| `empty` (merge, right) | No hypotheses → merging the empty class on the right changes nothing. | not printed |
| `lower` (left) | No hypotheses → the shared part is below each part. | not printed |
| `lower` (right) | No hypotheses → the shared part is below the other part. | not printed |
| `greatest` | A class below both parts → it is below their shared part. The shared part is the greatest lower bound. | printed in audit |
| `assoc` (shared part) | No hypotheses → the shared part operation is associative. | not printed |
| `comm` (shared part) | No hypotheses → the shared part operation is commutative. | not printed |
| `idem` (shared part) | No hypotheses → the shared part of a class with itself is itself. | not printed |
| `left` (absorption) | No hypotheses → merging a class with a shared part of it changes nothing. | printed in audit |
| `right` (absorption) | No hypotheses → the shared part of a class with a merge of it changes nothing. Dual absorption law; merge and shared part form a lattice. | printed in audit |

### The fold module — 5 theorems (the fold forms the family homes do not carry)

All five carry a decidability premise on witness equality, supplied by the statement itself.

| Token | Hypotheses → conclusion | Axioms |
|---|---|---|
| `mem` | No hypotheses → the fold of a feed holds a witness exactly when the witness is in the feed. The fold records exactly the presented set. | printed in audit |
| `mono` | Premise: every witness of a first feed is in a second feed → the fold of the first is below the fold of the second in the information order. | printed in audit |
| `mem` (deduplicated feed) | No hypotheses → a witness is in the deduplicated feed exactly when it is in the original feed. Helper for the duplication law. | not printed |
| `duplicates` | No hypotheses → folding the deduplicated feed gives the same class as folding the feed. | printed in audit |
| `drop` | No hypotheses → after filtering one named witness out of a feed, the fold holds a witness exactly when it was in the feed and is not the removed one. Removal is exact, at that witness and no other. | printed in audit |

### The frontier module — 8 named theorems, plus one private helper

| Token | Hypotheses → conclusion | Axioms |
|---|---|---|
| `mono` (total cost) | Premise: one cost is weakly dominant over another on the named axes → its total cost over those axes is no greater. | not printed |
| `lt` (total cost) | Premise: one cost strictly dominates another on the named axes → its total cost is strictly smaller. | printed in audit |
| `trans` (strict dominance) | One cost strictly dominates a second and the second a third → the first strictly dominates the third. | not printed |
| `iff` (decidable test) | No hypotheses → the decidable dominance test returns true exactly when strict dominance holds. | not printed |
| `frontier` (membership) | No hypotheses → a candidate is in the frontier exactly when it is in the list and no list member strictly dominates it. | not printed |
| `covered` | Premise: a candidate is in the list → it is on the frontier, or some frontier member strictly dominates it. Coverage by the frontier, plain list form. Proved through a private helper that descends on total cost. | printed in audit |
| `again` | No hypotheses → membership in the frontier of the frontier holds exactly when it holds in the frontier. A second pass changes nothing. | printed in audit |
| `kept` | Premises: a candidate is on the frontier of a first list, and no member of an added list strictly dominates it → it is on the frontier of the joined list. | printed in audit |

### The cited module — 2 theorems about the registry itself

| Token | Hypotheses → conclusion | Axioms |
|---|---|---|
| `count` | No hypotheses → the cited registry has exactly nine rows. Proved by computation. | not printed (the cited tranche carries no proofs of its own, per the audit file) |
| `homes` | No hypotheses → every row of the registry names one of the two family homes. Proved by decision. | not printed |

## The cited tranche — 9 theses (statements carried here, proofs at their homes)

Pins read on 2026-11-18, as the cited file records them: the quantifiable home at a21c7c56 (full pin in the source file), the optimality home at 97a5d7f3 (full pin in the source file). Evidence states below are the states the repo itself assigns; this census did not re-verify the homes.

| Thesis (plain English) | Home | Evidence state as the repo states it |
|---|---|---|
| Finiteness of qualification: a qualification — named software, named criteria, the behavior intended under them — forms a finite problem space, as a consequence of what a qualification is, never as a hypothesis. Refuted only by producing a qualification whose intended set cannot be finitely enumerated even in principle. | the quantifiable home | proven |
| The fold laws at value level: the accounting is a pure fold over content-addressed witnesses; its value projection is order-free and duplication-free and exactly recomputable. Refuted by two feeds of the same witness set yielding different values. The three forms the home does not carry are proved natively in the fold module above. | the quantifiable home | proven (at value level) |
| Coloring under its side condition: the coloring computed as the least fixed point over ground rules is sound and complete against derivability, within the length of the universe. Side condition, never silently dropped: the snapshot universe names every conclusion the rules can produce. | the quantifiable home | proven, under the one stated side condition |
| Pareto at bounds: the computed frontier is exactly the assignments no other assignment dominates at the witnessed bounds; the frontier is nonempty; refining the bounds is monotone. | both homes | proven (at bounds; general form in the optimality home) |
| Per-execution dominance, as once hoped: a dominated schedule finishes worse on every single execution. | both homes | **refuted — DISPROOF.** The same counterexample in both homes: bounds 1 to 100 against 2 to 3, where the dominated schedule can realize 1 against 3. Dominance is about bounds, never about one execution. Carried as a disproof at full strength; it is the boundary the Pareto thesis is stated inside. |
| Coverage: every execution crosses the kernel boundary, so boundary sensing plus lifting yields a witness for every execution. Refuted by one execution of named software that produces a qualified behavior and leaves no boundary trace and no lifted state. | the quantifiable home | **premise** — carried as a named premise, taken as an argument by every coverage theorem there, never counted as proven. The register records the empirical half (one sensor, one host) as refuted by an adversarial pass; the premise as a statement about the protection model stands as the home carries it. |
| Incremental recomputation: incremental results equal full evaluation of the new snapshot, and the incrementally maintained frontier is exact. Scope printed at the home: a semantic refinement result, not a speed result. | the optimality home | proven |
| Closure, compounding, and withdrawal: the closure operator is extensive, least, monotone, and idempotent; finite families compound keeping cross-source consequences; withdrawal adds no support; unsupported cycles do not bootstrap. | the optimality home | proven |
| The regression gate: the gate accepts exactly the candidates that drop no qualified behavior. One adversarial shape stands outside its battery — a drop disguised as a merge — and stands in the future work file with its closing condition. | the quantifiable home | proven |

## The future work remainder — 16 entries (census-only; none counted as proved)

Each entry stands in the future work file with its evidence state and its closing condition. States below are the file's own, compressed to this census's vocabulary.

1. The sensor claim, empirical half. State: **refuted** for the sensor and host on record — an adversarial pass on 2026-11-17 produced executions with effects and no witness, and one whose witness fails independent verification. The premise form is unaffected and is carried in the cited tranche. Closes when the named repairs land and the adversarial battery passes at a named pin.
2. The engine saturation battery, remainder. State: implemented behavior, measured failing — fixed point only on the smallest subject, a depth condition that deadlocks, a node cap that truncates silently, one required merge blocked as written. The coloring thesis itself stands proven in the cited tranche.
3. The merge-disguised drop, remainder. State: proposed semantics. The gate thesis stands proven; this one adversarial shape stands outside its battery. Closes when the shape enters the battery and the gate refuses it by name, or the gate thesis is restated at the strength that survives.
4. The adversarial frontier shapes, remainder. State: verified behavior on the shapes run (a thirteen-instance ladder, a seeded sweep of forty, the real instance); the named adversarial shapes (ties everywhere, one dominant behavior, zero-cost tests) are unrun — proposed as the next rung.
5. Sensor completeness over the foreign battery. State: **refuted** on this host — of four adversarial programs, three evade; the original twelve-case battery still passes as executed and no longer supports a completeness reading.
6. The splice shape, remainder. State: verified behavior for three named shapes (corrupted witness, stale snapshot, cross-snapshot ordering); the splice of two internally clean snapshot halves is untested — proposed.
7. The resolution claim: the representation of the execution environment is the most robust and highest-resolution one the platform affords. State: settled intent, asserted as a requirement, never verified — claimed-not-proven. One live candidate refutation stands named (per-event content a tracer stop affords and the carried representation does not record).
8. Relevance of a metric to an intent composition, computed exactly over a step graph in reduced rationals with no tolerance. State: proposed semantics. One family home formalizes the measure's exactness over its own model; the register's closing condition (a hand-computed example reproduced exactly, one witnessed instance, an independent recomputation agreeing on all six quantities) is not yet discharged.
9. The whole-construction refutation conditions (four standing conditions: one wrong qualification decision on witnessed data; one real regression the gate accepts; one execution class provably unwitnessable by any boundary sensor on a named platform; one case where the recommended ordering measures worse than the incumbent under its own discharge). State: standing refutation conditions over the whole construction, not single theorems — premise-level guards carried so the census is complete.
10. The composed theorem as one object: the four parts (finiteness, coloring, fold invariance at value level, the frontier at bounds) holding together over one named snapshot under eight hypotheses. State: proposed semantics. Every part stands proven or discharged on its own; no single run has checked the composed statement as one object over one snapshot.
11. The coloring in rule form, joined to the closure. State: proposed semantics in part — the optimality home proves the equivalence of derivability and its closure operator, and snapshot agreement under the universe premise; the joined statement over the spec's own rule form is not yet carried.
12. The capacity generalization: no claim relies on capacity one; time is the longest path over the combined graph at any capacity vector. State: implemented behavior (the solver on disk takes capacity as a per-venue table and its battery ran capacities above one); no Lean form stands in any home — claimed-not-proven in Lean.
13. The foundation claim, remainder. The algebraic half is proved natively above. Two parts remain, both premise-level: the identification premise (the states of a given piece of software, under the checked equivalence, are faithfully represented by the classes of the merge module) and the state-machine half (nodes and transitions map to the configurations of that lattice, preserving transitions). State: settled intent as a directive; the developed answer is proposed semantics.
14. The topological thesis: improvement across the whole topology the two family homes imply — every proof point at its strongest reachable state, no dominated point left standing. State: proposed semantics, in flight under a directive of 2026-11-18.
15. The self-hosting claims: the compiler compiles itself end to end with no foreign intermediary in the release path. State: implemented behavior in part — the battery stands green on its home venue and the Linux native-route blocker stands closed, both at their pins in the release record; the macOS oracle legs are still owed, and the production compiler is still written in a foreign host language.
16. The expectation about least-chars forms: among semantically equivalent forms, the least-chars form yields at least equivalent performance, power, and composability. State: proposed semantics as a general claim; measured per application at the same contract wherever applied. It is an empirical thesis; no Lean proof can discharge it.

## Premises carried rather than proven (consolidated)

1. The identification premise of the foundation claim: that the states of a given piece of software, under the equivalence the machinery checks, are faithfully represented by the characteristic-function classes of the merge module. Named in the merge module itself and in the future work file; proved nowhere.
2. Coverage (cited tranche): a named platform premise at its home, taken as an argument by every coverage theorem there, never counted as proven.
3. The coloring side condition: the snapshot universe names every conclusion the rules can produce. The coloring thesis is proven only under it.
4. The cited tranche rests on its citations: statements, refutation conditions, and states are carried here; the proofs stand at the two homes at the pins recorded in the cited file, which this census did not re-verify.
5. The fold at full text strength, for the derivation on disk, stands as the register records it (discharged on 2026-11-17 by a closing re-run, all five feeds byte-identical) — an on-disk record carried by the fold module's header, not a theorem of this repo.

## Non-claims carried

- This repo does not re-prove any thesis whose strongest form already stands in a family home; a duplicate proof would be a second, weaker home, and the repo does not make those.
- Nothing in the future work file is counted as proved, and no entry there is silently dropped: an entry that is refuted keeps its refutation as its state.
- The algebraic half of the foundation claim is proved for the characteristic-function representation only; it is not a proof that any particular piece of software is faithfully represented by those classes, and it is not the state-machine half.
- No recorded check log stands in this repo: the gate's passing at this pin is not evidenced by a recorded run, and this census ran no build.
- The least-chars expectation is empirical; its presence here is as a falsifiable thesis with a closing condition, not as a Lean result.

## Watch delta — 2026-11-18, the hourly re-synthesis watch

The watch re-read the live head at ea7437acf90cbcb9a4cdc2e0d068b71d64dbc4a4, past this annex's census pin d207be6e, and shallow-cloned it. Mechanical count at the live head: 35 theorem or lemma declarations across 7 Lean files, no sorry token, no custom axiom declaration — the same declaration total the sweep census recorded at d207be6e. The prose placements above stand at d207be6e; a full re-census at ea7437ac is owed.
