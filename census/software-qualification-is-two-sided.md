# software-qualification-is-two-sided — theorem census

Pin 6d68fbd81f45865050e0a7411a8e91a3919b6c5f. Public.
The listing description states its claim in one line.
Censused by the eighty-seventh hourly re-synthesis watch
(2026-11-21), which found the repo new in the full
enumeration and read its whole tree at the pin (7 files,
not truncated) firsthand through the gh route: the spec,
the readme, the three proof files, the gate script, and
the toolchain pin. The determination is by content
— Lean sources carrying proved results — never by the
name.

## The thesis, in plain English

Every qualified configuration has a dual unqualified
witness: a nearest configuration that fails the
qualification. The distance to that witness — the hinge
width — is a computable quantity, and width one holds
exactly at the qualification boundary.

## What is proved

Nineteen theorem declarations in three Lean files, at
the pinned toolchain named in the tree (a Lean release
in the estate usual family pin line), core only:

- The boundary result (rim): for a qualified
  configuration, in a space that holds a failing
  configuration, hinge width one holds exactly at the
  qualification boundary — a failing configuration one
  single-premise change away.
- The margin result: the margin, width minus one, is
  zero exactly at the boundary. The width is a distance,
  so it is one at the boundary and the margin is the
  quantity that vanishes there; the off-by-one between
  the two forms is stated in the repo, not hidden.
- The growth result (grow): width is monotone under
  premise strengthening, where strengthening enlarges
  the qualified set. The failing set only shrinks, so
  the least distance to it can only grow.
- The supporting lemmas: membership in the space is
  exactly the stated length; distance zero holds exactly
  at equality and distance is at most the length; the
  fold of minima attains its sentinel or a member, is at
  most every member, and is at least any common lower
  bound; the fold over a larger list is at most the fold
  over a sublist; and filtering by a weaker predicate
  yields a sublist of the filtering by a stronger one.
- A qualified configuration width is at least one: the
  only configuration at distance zero is itself, and it
  qualifies.

Axiom state, as the repo readme and its audit file
record at the pin: the boundary and margin results
depend on propositional extensionality, classical
choice, and quotient soundness; the growth result
depends on propositional extensionality and quotient
soundness; one control depends on propositional
extensionality only and the other two controls depend
on no axioms. Nothing is admitted by an escape token
in the tree as read.

State: PROVEN in source at the pin, at the recorded
strength below.

## Premises, named and not proved here

- The configuration space of the chosen subject is
  finite by the definition of qualification: to qualify
  is to pick out named configurations under named
  criteria. The model takes the space as an explicit
  list, so finiteness is by construction, derived from
  the definition and never stated as a hypothesis.
- Distance is counted in single-premise changes.
- Strengthening means the qualified set grows; a change
  that drops a previously qualified configuration is
  not a strengthening, and widths may fall under it.

## The instance

The measurement subject is the decidability frontier
standing instance, as the repo readme records: nine
witnessed runs over six venues, one venue chosen per
run, with the frontier and dominated counts and the
full width distribution stated there, computed two
independent ways with agreement on a sample of one
thousand. A companion tool in the frontier instrument
ordering home reports the width beside every verdict;
the tool is authored and its first run is pending a
named execution block recorded in the commissioning
record, so no per-verdict width table exists in the
store yet. The registered flip test is void on this
instance: the observed flip count across the last
three head changes is zero, so neither registered
outcome class is earned.

## Controls and gate

Three standing controls in their own file, each on
concrete data: with no failing configuration in the
space, a qualified configuration width is the sentinel
and it is not on the boundary, proving the failing
existence premise load-bearing; under a strengthening
at two premises, one configuration width grows
strictly, from one to two, proving the monotonicity
not vacuous; and under a change that is not a
strengthening, a width falls to zero, proving the
strengthening premise load-bearing. The gate script
compiles every file cold with warnings as errors,
scans for escape tokens, and fails on any printed
principle outside the allowed standard set. No
recorded gate log file stands in the tree, and this
watch did not re-run the gate, so the gate stands at
recorded strength.

## What is not claimed

- No predictive verdict on the hinge width: the
  registered test had no flips to predict on this
  instance, and the width is not adopted as a fragility
  measure on vacuous evidence.
- The theorems are about the boolean premise model of
  the spec. The instrument computes the same quantities
  on its own coordinate form; that computation is a
  measurement, not a theorem of this repo.
- No width figure is stated for any subject other than
  the frontier instance recorded in the readme.
