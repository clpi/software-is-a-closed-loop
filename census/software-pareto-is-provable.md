# Census — software-pareto-is-provable

## Pin and identity

- Census pin and live head (read in the ninety-fifth
  enumeration, 2026-11-22):
  426ac15dc381b3eadd8954145faf805a37704203
- Visibility: public. Default branch: main.
- Description (verbatim from the listing): a machine
  checked Pareto optimality repo — obligations over the
  general definitions, proved in Lean 4.19.0.
- The repo is new in this enumeration, entering the
  census here. Its tree stands at nine files.
- Toolchain: Lean 4.19.0, named in its readme and its
  gate script.
- Determination: proof-bearing by content — Lean
  sources, a gate script, and a recorded gate record
  stand in the tree, found by the content check on
  this enumeration, not by its name. The repo is
  newly proof-bearing in this pass.

## Thesis, in plain English

Pareto optimality, proved for the general definitions
of the Pareto proof methodology record of 2026-11-22:
a declared space of candidates and axes, a pinned
table of one value per axis for each candidate, the
weight-free dominance reading (at least as good on
every axis, strictly better on at least one), and the
receipt and version machinery that binds every table
cell to the instrument and pin that produced it. This
repo is the proof home for that program, named through
the decision route its readme records. Finiteness of
the qualification space is derived from the
declaration lists, never carried as a hypothesis.

## What stands at the pin — twenty theorems in the proof file

Counted firsthand over the tree at the pin: thirty
three theorem declarations in four Lean files — twenty
in the proof file, twelve in the test file, and one in
the control draft in the controls folder, which is the
standing control and is counted nowhere in the proven
column. No sorry token and no custom axiom declaration
stands in any Lean file by this watch's scan. The
twenty proven theorems discharge, in the repo's own
obligation numbering:

- Obligations one to five: the table enumeration and
  its uniqueness; the entry ledger over presentation
  logs; finiteness derived from the declaration lists;
  the change step; and the declared and timing results
  for usable axes.
- Obligation six: the binding of cells to their
  receipts, resting on two named premises of the
  methodology record's premise registry, carried
  explicit in the theorem's own statement.
- Obligation seven: the receipted form — a verdict
  cell with its receipt removed reads as unmeasured,
  naming that cell.
- Obligation eight: the fixed, versioned, and
  invalidated forms — a reversed axis direction
  invalidates exactly the receipts it touches.
- Obligation nine: the pairwise, cross-form, and
  agreement results over ordered candidate pairs, the
  agreement result resting on one named premise,
  carried explicit.
- Obligation fourteen: locality — the verdict for a
  pair is a function of the two rows alone, proved
  from the dominance and receipt definitions.
- Beside the obligations: the cover and edge
  characterizations of the dominance reading, and the
  swap lemma the pairwise results rest on.

## Premises, absent set, and unmeasured cells

- On named premises: the premise registry of the
  methodology record (four premises) is kept explicit
  and never discharged, as the repo's own header
  states; two of the premises appear in the binding
  and agreement theorems as named hypotheses.
- Absent and not claimed, as the repo itself prints:
  obligations ten to thirteen and fifteen to twenty
  are later lane work and are not claimed in this
  repo yet; and no instance claim is made here — the
  theorems are over the general definitions, and any
  claim about a concrete estate instance is later
  work at its own pin.

## Controls and gate state

- Controls in tree: one standing control — a draft in
  the controls folder that states finiteness as a
  hypothesis; the repo's hypothesis and naming audit
  must refuse it, and the gate runs that refusal as a
  required step. The test file carries twelve checked
  instances beside it, counted as executed evidence at
  their own strength.
- Gate state: green at the pin by the repo's recorded
  home record — the gate compiles both the proof and
  the test file cold with the placeholder scan, the
  axiom audit (every theorem on no axioms or on a
  subset of the standard three), the hypothesis and
  naming audit, and the control refusal, and its
  recorded output at the landing pin is compile exit
  zero, zero placeholders, audit control passed. The
  census did not re-run the build.

State: PROVEN in source at the pin for the twenty
theorems, on the recorded gate record at the pin —
the binding and agreement results under their named
premises, the premise registry carried explicit, the
remaining obligations standing as named unclaimed
work, and no instance claim made. The census pin is
set to the fresh head on this first proof census; the
placements in the synthesis and the ledger row are
entered at the pin in this same pass.

## Re-census — 2026-11-22, the ninety-fifth hourly re-synthesis watch

Re-censused at theorem level in full at the fresh head 5b45d5fd22e57e0bf9044d4efe4fbc1ed7bc1f00; the census pin moves from 426ac15dc381b3eadd8954145faf805a37704203 to that head in this pass. One commit stands between the pins, the second lane's landing. The first proof file, the first test file, and the control draft are byte-identical between the pins, so the twenty proven theorems of the first lane and its twelve checked test instances stand unchanged. Two files are new: a second proof file carrying 38 declarations and a second test file carrying 6 checked instances; the audit file, the readme, the audit script, and the gate script changed. Counted by the watch method over the whole tree, declarations grew from 33 to 77 and distinct short names from 29 to 67, with 38 names gained and none lost — no proven set shrank and no regression is flagged. No placeholder token stands in the new files by this watch's scan.

The 38 new declarations discharge, in the repo's own obligation numbering:

- Obligation ten: soundness of the computed frontier, proved from the frontier membership characterization over the pairwise verdicts.
- Obligation eleven: completeness and closure — a row outside the frontier has a dominator on the frontier, termination resting on the dominator count taken from the finite row list, with finiteness derived and never a hypothesis.
- Obligation twelve: checker identity — the checker frontier and the solver frontier have exactly the same members, beside its executed instance in the second test file.
- Obligation thirteen: the assembled optimality claim at exactly its proved strength, assembled from obligations ten, eleven, and twelve with no additional hypothesis.
- Obligation fifteen: the frontier cone scope and kept forms, beside its executed instance control.
- Obligation sixteen: reuse on certificate — membership, carry, and refusal, beside its executed controls for the unchanged and the one-cell-changed cones.
- Obligation seventeen: incremental equals full, by induction over the operation sequence through its join and drop step results and its uniqueness results, beside its executed walk control.
- Obligation eighteen: version binding and its changed form, beside the executed control that changes each of the four tuple components in turn.
- Obligation nineteen: the premise registry audit, carried in the audit script and run by the gate over all four sources — the recorded audit at the closing pin enumerates the assumption atoms of both lanes and matches each against the registry classes, finding none outside the registry.
- Obligation twenty: reopening scoped — the scope, kept-characterization, and partition results, beside the executed reopening control.
- Beside the obligations: the core development the frontier results rest on — the frontier membership characterization, the step lemmas for the cover, edge, and verdict relations, the self-verdict results, and the counting results the completeness proof terminates on.

Premises, absent set, and gate state at the fresh head:

- On named premises: the premise registry (four premises) is kept explicit and never discharged, exactly as at the first pin; the assembled claim carries them as inherited in content from its parts.
- Absent: no obligation of the twenty now stands unclaimed — obligations ten to thirteen and fifteen to twenty, named unclaimed work at the first pin, are discharged in this pass. No instance claim is made: the theorems are over the general definitions, and any claim about a concrete estate instance is later work at its own pin.
- Controls in tree: the standing control draft stands unchanged and must still be refused by the audit; the checked test instances grew from twelve to eighteen with the second test file.
- Gate state: green at the fresh head by the repo's recorded home record for the second lane — cold compile exit zero over all four sources, zero placeholders, 67 theorems axiom-audited with every one depending on no axioms or on a subset of the standard three, the hypothesis, naming, and premise audits passing over all four sources, and the finiteness control refused as required. The census did not re-run the build.

State: PROVEN in source at the fresh head for all twenty obligations, on the recorded gate record at the head — the premise registry carried explicit, and no instance claim made. The census pin is set to the fresh head in this pass, and the placements in the synthesis and the ledger row are restated at the pin in this same pass.
