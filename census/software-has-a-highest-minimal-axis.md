# Census — software-has-a-highest-minimal-axis

## Pin and identity

- Census pin and live head (read in the sixty-fifth
  enumeration, 2026-11-20):
  63d9d3fdce1f81c81cd5cda2bd9850b0c1494646
- Visibility: public. Default branch: main.
- Description (verbatim from the listing): The highest
  minimal axis theorem for qualified parametric systems,
  proved in Lean 4.19.0
- The repo entered the census in the sixty-fifth
  enumeration as a new repo. Its tree stands at eight
  files: a readme, a specification, and a proof folder
  holding three Lean files, a gate script, a recorded
  gate log, and a toolchain file.
- Toolchain: Lean 4.19.0, pinned in its toolchain
  file. The proof uses no library beyond the Lean
  core, by its core file's own header.
- Determination: proof-bearing by content — Lean
  sources, a gate script, and a recorded gate log
  stand in the tree, found by the content check on
  this enumeration, not by its name. The repo is
  newly proof-bearing in this pass, as a new repo.

## Thesis, in plain English

A qualified parametric system — named axes, a contract
of allowed configurations, a behavior function on
finite components, and a hypergraph joining the
components — always has a highest minimal axis vector:
a smallest axis set whose variation inside the contract
already produces the full emergent live interacting
structure, and among those smallest sets one whose
refinement vector (the emergence measure first, the
live count second) is maximal. Sufficiency is stated
against the full axis set: an axis set is sufficient
when its emergence measure, the weight sum over the
hyperedges its live set engages, equals the full set's.
The induced transformation from variations of that
minimal vector to behavior variations loses no engaged
hyperedge.

## What stands at the pin — 58 theorems in two Lean files

Counted firsthand over the tree at the pin: 58
theorem declarations in two files, beside an audit
file carrying no declarations — it prints the
foundational principles of every theorem for the gate.
No escape token and no custom axiom declaration stands
in any Lean file by this watch's scan. The files group
as the repo's own specification groups them, restated
here in plain terms:

- The core file (42): the finite list machinery
  (filter, sum, subset, and cardinality laws);
  monotonicity — under a subset of axes the live set,
  the emergence measure, and the live count all grow;
  structure forcing — a sufficient axis set engages
  exactly the hyperedges the full axis set engages,
  with the positivity of the hyperedge weights load
  bearing through a strict sum step; existence — every
  instance has a highest minimal axis set, by descent
  on axis count and ascent on the refinement
  coordinate; minimality — every proper subset of a
  highest minimal set has its emergence measure
  strictly below the full measure; maximality and
  uniqueness — a highest minimal set stands over every
  minimal sufficient set in the refinement order, and
  any two highest minimal sets share the same
  refinement vector; functoriality — variations
  compose, the induced transformation respects identity
  and composition, and it preserves the engaged
  structure exactly; the degenerate characterization —
  no proper subset of the full axis set is sufficient
  exactly when every highest minimal set is the full
  axis set, with its empty and singleton contract
  corollary, under which the unique highest minimal
  vector is the empty set; and the corrected dead axis
  facts below.
- The controls file (16): the enumeration of the eight
  axis sets of a three axis instance, and the standing
  controls on the specification's three named
  instances, all checked by kernel decision — the
  first instance's values, live sets, and engaged
  structure, both of its minimal sets, its highest set,
  its dead axis facts, and its full set not minimal;
  the degenerate instance's values, its no proper
  subset result, its answer, and its full set highest;
  and the empty and singleton contract instance's
  values and its two highest results.

## Premises, absent set, and refuted forms

- On named premises: the weight of every hyperedge of
  size at least two is positive — a field of the
  instance itself, carried in every statement that
  needs it, and load bearing for structure forcing, as
  the specification states. Finiteness is derived from
  what qualification is in the specification, never
  imposed as a bound.
- Refuted in the tree, by standing control: the
  stronger dead axis sentence — that a dead axis
  belongs to no minimal sufficient set. In the first
  named instance one axis is emergent-dead and its
  singleton is nevertheless minimal sufficient; the
  proved form is that removing a dead axis is already
  sufficient, so a dead axis makes the full axis set
  non-minimal. The same instance refutes the reading
  that every minimal sufficient set is highest: its
  two minimal sets carry different refinement vectors,
  and only one is highest. Structure preservation
  wider than the engaged structure is likewise false
  on this instance, as the specification states; the
  proved form covers the engaged structure exactly.
- Absent: the solver the specification contracts for —
  a deterministic search over the finite subset space
  returning one highest minimal vector with the full
  minimal list and per-axis dispositions — stands in
  the specification as a contract with named validation
  bars and no implementation in this tree. State:
  proposed, not implemented in-repo. The arena instance
  the specification names as a validation case is
  likewise absent from the tree.

## Controls and gate state

- Controls in tree: the sixteen standing controls
  above, proved by kernel decision only — the gate
  bars the native decision form, as the specification
  records, because it would add a principle outside
  the allowed set.
- Gate state: green at the pin by the repo's recorded
  log — the recorded check output in the tree shows
  the Lean 4.19.0 build, axiom lines printed for all
  58 theorems, every one inside the standard three
  (propositional extensionality, classical choice, and
  quotient soundness, in subsets), and the subset
  check passing. The gate script is the widened family
  form: it scans every Lean file for escape tokens,
  compiles with warnings as errors, and fails closed
  if any printed principle lies outside the allowed
  set.

State: PROVEN in source at the pin for the 58
theorems, on the recorded gate log at the pin — the
dead axis correction and the non-vacuity of highest
carried by the standing controls, the solver standing
proposed with no implementation in the tree. The
census pin is set to the fresh head on this first
proof census; the placements in the synthesis and
the ledger row are entered at the pin in this same
pass.

## Watch delta — 2026-11-21, the eighty-fifth hourly re-synthesis watch

The watch re-read this repo's live head at b12fdb2411f23df33c02f4695f0b2d8c09ecaa89 in the full enumeration and read the whole tree at that head (19 files, not truncated) and at the last recorded head 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646 (8 files). No Lean file changed between the heads, so the proven set is unchanged: the same 58 theorems with the same name set at both, counted by the watch method over the tree at each pin, with no sorry token and no axiom declaration. The movement is two commits landing a deterministic finite solver for the axis problem beside the proof: eleven files added, all in a new solver folder — the solver, its model, an independent checker, a validation script, a Lean check script, four fixtures, a readme, and a validation record — and two files changed, the proof folder's check log and check script, with no file removed. The state recorded above at the census pin, that the solver stood proposed with no implementation in the tree, no longer holds at the fresh head: an implementation now stands in the tree, recorded here at delta strength from the tree and commit reads; its validation record is the repo's own, read firsthand and not re-run by this watch. The census pin stands at 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646, with a full re-census at the fresh head owed.

## Watch delta — 2026-11-22, the ninety-seventh hourly re-synthesis watch

The watch re-read this repo's live head at 04d5069362a8508485dd18eaee995811397dd962 in the full enumeration and read the whole tree at that head (26 files) and at the last recorded head b12fdb2411f23df33c02f4695f0b2d8c09ecaa89 (19 files). The proven set grew between the heads and lost nothing: 67 declarations at the fresh head against 58 at the last recorded head, counted by the watch method over the tree at each pin, with nine names gained, none lost, and no sorry token and no axiom declaration at either head. The growth is two new Lean files in a new incremental solver folder beside the solver the eighty-fifth watch recorded: a join development carrying the nine new theorems — the join and scoped liveness forms, the scoped measure and its deletion form, the deletion liveness form, the agreement characterization over the difference set, and the witness monotonicity and survival forms — and an audit file carrying no declarations. The movement is five commits (four landing commits and a merge) adding the whole incremental folder, seven files in all: the two Lean files and their check script, beside the solver, its gate, and a readme, with no file changed or removed. The incremental gate and its records are the repo's own, read firsthand and not re-run by this watch. The census pin stands at 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646, with a full re-census at the fresh head owed.

## Watch delta — 2026-11-22, the hundred-sixth hourly re-synthesis watch

The watch re-read this repo's live head at bdf1ab45e0782eb495865e1e3dcd7da6f2dddda0 in the full enumeration and read the whole tree at that head (27 files, not truncated) and at the last recorded head 04d5069362a8508485dd18eaee995811397dd962 (26 files). Every Lean file is byte-identical between the heads, so the proven set is unchanged: 67 declarations, the same name set at both, counted by the watch method over the tree at each pin, none gained and none lost. The movement is one commit of bounded search work — a refused join batch leaves the carried state unchanged — landing as executed solver work: one file added, a fuzz script in the incremental solver folder, and three files changed, its readme and the solver and gate sources, none of them Lean. That work is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646, with a full re-census at the fresh head owed.

## Watch delta — 2026-11-23, the hundred-twenty-ninth hourly re-synthesis watch

The watch re-read this repo's live head at 143f057f5d221c7f5228975808d8ad9667e84786 in the full enumeration and read the whole tree at that head (83 files, not truncated) and at the last recorded head bdf1ab45e0782eb495865e1e3dcd7da6f2dddda0 (27 files). The proven set grew between the heads and lost nothing: 337 declarations at the fresh head against 67 at the last recorded head, counted by the watch method over the tree at each pin, with 267 distinct names gained, none lost, and no sorry token and no axiom declaration at either head. The growth is thirteen new Lean files in the proof folder, carrying 270 new declarations: the graph, finite check and frontier, exponential, qualification, incremental and incremental counts, hypergraph incremental, executable witness and closure, certified table and replay, and certificate materialization developments — the deterministic solver standing in agreement with its Lean definitions, incremental hypergraph witnesses with a reconstructible replay, and materialized witness updates, beside a recorded check log in the tree at the fresh head that this watch read as the repo's own record and did not re-run. The movement is four commits (three landings and a merge): fifty-six files added, the thirteen Lean files beside the solver's certified execution, arena, incremental, instance, and result files and the proof gate files, and nine files changed, the readme, the check log and script, and solver sources and records, with no file removed. The state recorded above at the census pin, that the solver stood proposed, is further superseded at the fresh head: a certified execution now stands in the tree, recorded here at delta strength. The census pin stands at 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646, with a full re-census at the fresh head owed.

## Watch delta — 2026-11-23, the hundred-thirty-fifth hourly re-synthesis watch

The watch re-read this repo's live head at 0ffbabf42b84ffbda9d4fa5943d01d0001a2ee41 in the full enumeration and read the whole tree at that head (120 entries, not truncated) and at the last recorded head 143f057f5d221c7f5228975808d8ad9667e84786 (94 entries). The proven set grew between the heads and lost nothing: 580 declarations at the fresh head against 337 at the last recorded head, counted by the watch method over the tree at each pin, with 233 distinct names gained, none lost, and no sorry token and no axiom declaration at either head. The growth is eleven new Lean files in the proof folder, carrying 243 new declarations: the parametric Pareto development (70), the Pareto policy development (48), the optimal controller development (39), the incremental control development (20), the online policy development (16), the reasoning controls (15), the Pareto development beside the core (14), the controller refinement development (8), the online axis and online Pareto developments (6 each), and the online controller development (1) — parametric Pareto policies and incremental autonomous execution, in the landing commit's own terms. Fifteen further files were added beside them: a parametric reasoning record, six solver check and source files, and eight result records. Seven files changed: the workflow, the readme, the recorded check log, the gate script, and the solver's certified execution, readme, and validation records, with no file removed. The movement is two commits: one landing and its merge. The recorded check log in the tree at the fresh head ends in a pass covering the original proof baseline, the online development, the complete Pareto frontiers and parameter regions, the incremental adaptive policy certificates, the globally optimal bounded controllers, and the empirical autonomous qualification, read here as the repo's own record and not re-run by this watch; the axiom print lines counted by the watch scan stand at 101 at both heads. The census pin stands at 63d9d3fdce1f81c81cd5cda2bd9850b0c1494646, with a full re-census at the fresh head owed.
