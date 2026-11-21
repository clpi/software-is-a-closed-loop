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
