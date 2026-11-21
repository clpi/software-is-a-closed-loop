# software-emergence-is-decidable — theorem census

Pin ee3086521932c19f4ed0a054d4362cf21d525972. Public. The
repo's own description: emergence from actor interactions
as a parametric, solvable, optimizable vector over any
qualified system — spec, program record, and
machine-checked certificates.

Censused by the seventy-sixth hourly re-synthesis watch
(2026-11-21), which read the tree at the pin in full
through the gh route and read the tree at the last
recorded head 192df382cf5752bd9eccda819cea664d42f99e78
in the same pass: that head carried three files only — a
ladder specification, a program record, and a readme —
and no proof-assistant source at all, so this repo is
newly proof-bearing in this window, and the determination
rests on the content read at both heads, never on the
name. The movement between the heads is one commit:
twenty-one files added and one changed, the readme, none
removed. The enumeration read caught the repo
mid-movement; the later individual read at the head
recorded here governs.

## The thesis, in plain English

The repo carries the emergence ladder: emergence from
actor interactions as a parametric quantity over any
qualified system, solvable by a decision procedure and
optimizable by search. This movement executes rung 3 of
the ladder, composition — emergent groups as actors, with
second-order interaction — and proves the verification
stack under the rung in Lean, while its capability claim
is falsified in its own record, below.

## Theorem census — 22 theorems in one Lean file

The rung 3 Lean file (Lean 4.19.0, core only) carries 22
theorem declarations, counted by the watch over the file
at the pin, disposing of seven of the rung's eight stated
obligations:

- The tally algebra: the componentwise tally addition is
  a commutative monoid — four theorems (left and right
  identity, commutativity, associativity).
- Obligation 3.1, proved: the group formation graph is
  defined from the level-1 projection of the cut alone,
  is deterministic in the cut, and first-reach facts are
  stable under appends, so a partition formed at a cut
  cannot be changed by later records — three theorems,
  beside the fold composition law and the tally cons law.
- Obligation 3.2, proved: replay and restart exactness of
  the fold, and the state at a formation tick is a
  function of the log prefix alone — two theorems.
- Obligation 3.3, proved: the freeze transformation
  preserves length, leaves a log unchanged when no record
  is in the frozen class, and maps a log pointwise to its
  frozen sources when every record is in the class —
  three theorems.
- Obligation 3.4, proved: over a partition of the actor
  list, the summed member-step count of one group step
  over all blocks is exactly the actor count — one
  theorem.
- Obligation 3.5, proved in conditional form: if the
  joint view's engaged family contains a level view's
  engaged family as a sublist with weights carried, then
  that level's measure is at most the joint measure —
  two theorems. The engaged-inclusion antecedent is
  discharged by the view construction, not in the file;
  the monotonicity core is proved.
- Obligation 3.6, proved: the joint tally is the
  componentwise sum of the two filtered tallies for any
  record predicate, at every cut — one theorem.
- Obligation 3.7, proved: counts of any predicate are
  preserved under a permutation of a tick's records and
  under a readdressing that preserves the predicate,
  composed in the shuffle marginals theorem — three
  theorems.

## Premise, absent set, and the refuted claim

- Obligation 3.8 stands as a named premise: a proposition
  definition in the file, not proved, not an axiom, and
  depended on by no theorem. It is discharged, if ever,
  only by the rung 6 certificate's general form.
- Absent at the pin: any in-repo proof of rungs 2, 4, 5,
  or 6, the endgame interfaces, and the optimization
  problem beyond its stated form — all proposed in the
  repo's specification, none proved in its tree.
- Refuted in-repo: the rung 3 capability claim itself.
  The rung record at the pin prints the decision in both
  registered families — no win in either, under the
  registered per-arm rule and under the global delta rule
  alike — because the joint system failed to beat the
  level-1 arm beyond its spread. The loss stands in the
  repo's own record until a same-contract re-measure at a
  current pin says otherwise.

## Controls and gate state

The rung record at the pin carries the execution
evidence: an independent checker re-implementing
generation, the fold, the tally, and formation verified
336 runs, every one replay-exact — 2352 of 2352
append-cut agreements, 672 of 672 restart agreements,
336 of 336 tally pair compositions, with formation
agreement and budget shape on every run — and zero
load-bearing blocks in both families' ablations. The
same record states the Lean gate at the pin: a cold
compile clean, with an axiom audit printing only the
standard set for the audited theorems and no sorry
anywhere. That gate state is recorded in the repo's own
tree at the pin; the watch read the file and the record
firsthand and did not re-run the compile, so the gate
stands at recorded strength, not watch-verified strength.
