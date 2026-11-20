# Census — software-tensors-are-editable

## Pin and identity

- Census pin and live head (read in the fifty-fourth
  enumeration, 2026-11-20):
  9d7afd54bf8e7c8dbd335b6530d4cdc6b6d14d18
- Visibility: public. Default branch: main.
- Description (the repo's own): editable tensors and
  recursive semantic feedback — transition semantics and
  machine-checked proof for edits that land on actual
  model tensor bytes.
- The repo is new since the fifty-third enumeration;
  its tree stands at nine files — a specification, the
  repo's own claim census, a readme, and a proof folder
  carrying the Lean core, its audit file, its gate
  script, its recorded gate log, and its toolchain pin.
- Toolchain: Lean 4.19.0, pinned in its toolchain file.
  No Mathlib; the core imports only the standard
  distribution.
- Determination: proof-bearing by content — Lean
  sources, a check script, and a recorded gate log stand
  in the tree, found by the content check on its first
  enumeration, not by its name.

## Thesis, in plain English

A deterministic view of a model checkpoint is edited,
the edit lands on the actual tensor bytes of an editable
copy, the next view is constructed from the edited
state, and that view drives the next edit — both the
tensor state and the represented intelligence taking
part in the recurrence. This repo is the semantics and
proof home of that program; the executable edit loop,
the independent check, and the tensor ingest lanes are
separate lanes, staged elsewhere and counted nowhere
here. No behavioral claim is made in this repo: a
structural tensor result is only a structural result.

## What stands at the pin — 14 theorems in one Lean file

Counted firsthand over the tree at the pin: 14 theorem
declarations in the core file, beside an audit file
carrying no declarations and printing an axiom line for
each of the 14; no escape token stands in either file
by this watch's scan. The repo's own census groups
them, and this census restates the groups in plain
terms:

- The delta algebra (6): a coordinate a delta never
  mentions keeps its value; the empty delta is the
  identity; lookup over a joined delta is decided by
  the left part where it assigns and otherwise by the
  right; applying a second delta after a first is
  applying their join, second first; lookup in the
  recorded inverse gives the value the source state
  held where the delta assigns and silence where it is
  silent; and a successful lookup names an entry of
  the delta.
- Reversal exactness (1): a delta applied and then its
  recorded inverse applied restores the original state
  at every coordinate — the headline result, at the
  abstract tensor level.
- Admissibility (2): an admissible delta leaves every
  protected coordinate at its state value; and two
  admissible deltas compose to an admissible delta
  under exactly one side condition, stated in the
  theorem — cross agreement at tied coordinates, in
  both directions of the tie. Protection and range
  need no side condition, being per entry and state
  independent by construction.
- The view (3): the obscurity of a view — the declared
  universe's coordinates the evidence does not cover —
  depends on the universe and the evidence alone, never
  on the state; states agreeing on every evidenced
  coordinate have the same view; and the plain
  determinism form, the same state and evidence yielding
  the same view.
- Standing controls (2), proved as refutations of the
  unconditional forms: admissibility is not preserved
  under composition without the cross condition — two
  singly admissible deltas at tied coordinates whose
  join disagrees; and the state-dependent change
  condition is not preserved under composition, which
  is why admissibility in this core is state
  independent.

## Premises, absent set, and blocked cells

- On named premises: no theorem in the core rests on a
  premise register; the one load-bearing condition —
  cross agreement at tied coordinates — stands inside
  the composition theorem's own statement, and its
  unconditional form stands refuted by the first
  control. The overlay form's precedent at the
  parametric language model home is cited at its pin
  in the repo's census, never recomputed and counted
  nowhere here.
- Absent and owed, as the repo itself prints: transport
  of the abstract core — whose value type is the
  integers, the symbol layer — through a fixed nonzero
  per-tensor scale, or a restatement over exact
  rationals; the per-schema check that each category
  metric is a function of the found list and the
  declared bounds, owed with the first concrete schema;
  and a stated method for evidencing a tie claim about
  a concrete checkpoint, blocked with the fixtures
  below. The specification's further sections — policies
  and typed view edits, the recurrence step, and the
  receipt contract — stand at their labeled states in
  the specification, proposed with their proof
  obligations named, not proved in the core.
- Blocked and unknown, as the repo itself prints: the
  paired sign-flip behavioral claim and the causal mask
  reconstruction with its fixture benchmark receipt are
  blocked — the fixtures they need are not on the
  machine, verified by the repo's own search record;
  and every behavioral effect of every concrete delta
  stands unknown until proved under a stated model or
  verified against held-out evidence. The repo's census
  also records, as verified firsthand on disk at its
  own strength, a ternary checkpoint census with an
  executed byte-exact round trip on one matrix — an
  executed result, counted nowhere in the proven
  column here.

## Controls and gate state

- Controls in tree: the two proved standing controls
  above, inside the core file.
- Gate state: green at the pin by the repo's recorded
  log — the gate script compiles every Lean file with
  warnings as errors, scans for escape tokens, and
  prints an axiom line for all 14 theorems, ending in
  its subset check passing. Of the 14: one depends on
  no axioms, seven on propositional extensionality
  only, one on quotient soundness only, and five on
  that pair, as the recorded log prints them.

State: PROVEN in source at the pin for the 14 theorems,
on the recorded gate log at the pin — the composition
result under its in-statement side condition, the
specification's further sections at their labeled
proposed states, and the behavioral cells blocked or
unknown as named above. The census pin is set to the
fresh head on this first census; the placements in the
synthesis and the ledger row are entered at the pin in
this same pass.

## Watch delta — 2026-11-20, the fifty-fourth hourly re-synthesis watch

The watch re-read this repo's live head at eb0c79ae5c78f4d46f03d0baa5d3891e6d994300 in the full enumeration, against the last recorded head 9d7afd54bf8e7c8dbd335b6530d4cdc6b6d14d18, which is its census pin. One commit stands between the heads, and it changes only the repo's own census file; every other file in the tree is byte-identical between the heads, including both Lean files, the gate script, the recorded gate log, and the specification. The theorem count is therefore unchanged: 14 theorems in the core file, the same name set at both heads, with no name gained and none lost, counted by the watch method over the tree at each pin.

The one change is a census correction in the source repo. Its founding census missed a checkpoint held in a local model store, because the store's blobs carry no file extension and an extension-based search could not see them, and it wrongly recorded that no such store exists on disk. The corrected census records that checkpoint — a 1.5 billion parameter instruct checkpoint in the named store, in the named container format, at just under one billion bytes with 338 tensors, its full hash computed and matching its content-addressed name — as verified firsthand on disk at the repo's own strength, an executed census result counted nowhere in the proven column here. The correction states plainly that no blocked item depends on that checkpoint: it is not any blocked experiment's fixture. The paired sign-flip behavioral claim and the causal mask reconstruction with its fixture receipt therefore remain blocked on their own missing fixtures, the owed and proposed items stand as this annex records them, and every behavioral effect of every concrete delta remains unknown.

State at the fresh head stands as at the census pin: proven in source for the 14 theorems on the recorded gate log at the pin, the specification's further sections at their labeled proposed states, and the behavioral cells blocked or unknown as named above. A full theorem-level re-census at the fresh head is owed; this delta records the tree evidence and the source correction.
