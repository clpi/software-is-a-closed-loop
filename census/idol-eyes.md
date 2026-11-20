# idol-eyes — theorem census

Pin 1dc24f4fcd8240ab6fbc9056dba7726e5c62bd98. Private. The
repo's own description: Idol-native computer perception,
control, and interface work — graph-owned semantics,
verified outcomes, and measured parity and dominance
against the incumbent perception tool it names, carried
as release gates.

Censused by the forty-fourth hourly re-synthesis watch
(2026-11-20), which read the tree at the pin in full
through the gh route (124 files, no read truncated) and
the four proof files with it, and read the tree at the
last recorded head 036df3b3e9b10e78938e5b54b82750ad6a1cae40
in the same pass (102 files, no read truncated): that
head carried no proof-assistant source at all, so this
repo is newly proof-bearing in this window, and the
determination rests on the content read at both heads,
never on the name. The movement
between the heads is thirteen commits: twenty-two files
added and one changed, the makefile, none removed.

## The thesis, in plain English

The repo founds its campaign on one canonical record
log and proves the certification law over that log. A
candidate build is admitted over its predecessor exactly
when, on every registered dimension, both states are
measured and every candidate reading is at least every
predecessor reading; an unmeasured dimension refuses
admission, and a regression, once present, refuses
forever. Meeting the union of the incumbents is exactly
admission over each incumbent one by one, and exactly
domination of the pooled peak list — so the campaign's
release gate is a theorem, not a convention.

## Theorem census — 61 declarations in four Lean files

The canonical file — 24 declarations. It restates the
derivability and hypergraph definitions mirrored from
the optimality home at its named pin, the optimality
repo's last recorded head before this watch, and proves
them again from the definitions: derivability is the
least closure, monotone in the edge set, with roots as
the empty-premise edges. It then states the
resolution-chain model for the first time in the estate:
terms identified by a total equivalence at each
resolution level, the levels forming a finite chain,
analysis admitted only at the symbol level or finer, and
one append-only record log as the only source of truth —
and proves the view laws over that log: the equivalences
nest along the chain, projections between levels
compose, the view is invariant under reordering of the
log, appending only ever adds edges, colors, and
derivations, the join of two views is their union, and
appending a record already present changes nothing.

The certification file — 23 declarations. The gate over
the canonical log: the executable decision computes
exactly the admission relation; admission is invariant
under permutation of either log and passes to sublists;
a regression refuses, and the refusal survives every
later append, in both the plain and the appended form;
an unmeasured dimension refuses; every admission
carries, for each registered dimension, a measured
witness reading in the candidate view; admission is
transitive and composes over consecutive steps, with the
pairwise and endpoint forms equal; the registered
dimension set only shrinks along a certified chain; and
a strict beat on every dimension implies admission,
while a tie is not a beat and a loss is not a beat.

The union file — 14 declarations. Meeting the union of
the incumbents: the executable decision computes
exactly the meeting relation; meeting the union is
exactly admission over each incumbent and exactly
domination of the pooled peak list; an unmeasured
incumbent refuses the meeting; and the ceiling form —
where an incumbent already sits at a declared maximum,
beating the union is beating the ceiling reading — with
the union beat results and regression finality for the
union gate.

The axioms file — no declarations. It prints axiom
lines for twenty-nine of the sixty-one theorems,
sixteen from the certification file and thirteen from
the union file. The canonical file's twenty-four
theorems carry no printed line there, so their axiom
state is unrecorded from that file.

## Controls and gate evidence

No dedicated controls file stands in the tree. The
refusal results stand as proved controls inside the
developments themselves: regression finality in both
files, the unmeasured refusals, and the tie and loss
results in the certification file. A check script
stands in the proof folder: it requires the named Lean
version, rejects the proof escape tokens in the three
proof files, compiles them in order, and runs the
axioms file. No recorded run of that script stands in
the tree at the pin, so a passing gate at the pin is
unrecorded — the gate state is unknown from recorded
evidence, not green. The watch scan found no escape
token in the three proof files, the same scan the
script itself performs. The campaign results record in
the bench folder is executed evidence about the
perception campaign; it stands outside the proof
folder and is not a theorem.

## Premises — named in the files, carried, not proved

- Score normalization at ingest is faithful: the
  direction and unit of each dimension survive
  normalization. Stated in the certification file's
  header.
- A measurement record states what was measured, under
  the campaign's same-contract rules. Stated in the
  certification file's header.
- The declared maximum is the true maximum of the
  dimension's normalized score, and a failed run is
  ingested with score zero on every cost dimension.
  Stated in the union file's header.
- Mirror fidelity: the canonical file's definitions are
  restated from the optimality home at its named pin;
  their faithfulness rests on the reading recorded
  here, as with every mirrored definition in the
  estate.

## Absent and proposed

Nothing further is claimed in the proof folder. The
repo's wider parity and dominance claims, named in its
description as release gates, are campaign claims: they
stand on the executed campaign record, not on these
theorems, and no theorem in the tree measures a run.

State: PROVEN at the pin for the sixty-one declarations
above, as Lean source read in full by this watch, with
the four named premises carried at exactly the states
the files themselves state, the canonical file's axiom
state unrecorded, and the gate's passing run at the pin
unrecorded.
