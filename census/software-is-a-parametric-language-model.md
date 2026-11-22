# Census — software-is-a-parametric-language-model

## Pin and identity

- Census pin and live head (read in the forty-eighth
  enumeration, 2026-11-20):
  ca4ca2b39181bb93a717b3edbb58ab476761fa5c
- Visibility: public. Default branch: main.
- The repo is new since the forty-seventh enumeration;
  its tree stands at twelve files — a specification, a
  Lean proof core with its audit file and gate script, an
  empirical harness with its results record, the repo's
  own claim census, and its hypergraph registry extract.
- Toolchain: Lean 4.19.0, pinned in its toolchain file.
  No Mathlib; the core imports only the standard
  distribution.
- Determination: proof-bearing by content — Lean
  sources, a check script, and a recorded gate log stand
  in the tree, found by the content check on its first
  enumeration, not by its name.

## Thesis, in plain English

A language model whose behavior is a totally
deterministic function of its content and its
parameters, where the parameters are named, legible
axes a person tunes deliberately — never an obscure
weight vector — and where behavior is tailored by
rewriting parameters incrementally, not by retraining
or sampling. Generation runs by a certified best first
rule, with no sampling anywhere on the deterministic
path. The repo is the constructive counterpart of the
obscure weights line: decompiling obscure weights into
semantic meaning is how an existing model becomes one
of these.

## What stands at the pin — 40 theorems in one Lean file

Counted by the watch method over the tree at the pin:
40 theorem declarations, 40 distinct names, in the
proof core file, beside an audit file carrying no
declarations; no escape token stands in either file by
this watch's scan. The repo's own census groups them:

- Fraction arithmetic (13): equality and order by cross
  multiplication; equality reflexive, symmetric, and
  transitive under positive denominators; order
  reflexivity, transitivity, and compatibility with
  equality; multiplication congruence; the two unit
  laws; the inverse law; multiplication preserving
  order and positivity; and associativity up to
  fraction equality.
- Selection (7): the champion of a list under a total
  preorder exists where the list is nonempty, is a
  member, is maximal, and is the first maximal member;
  the specification — member, maximal, first — has at
  most one satisfier.
- The decoder (6): appending distinct tokens is
  injective; the completion enumeration extends every
  enumerated completion by a suffix; the enumeration is
  duplicate free under row well formedness, by its
  pairwise helper; the decoder's answer satisfies the
  specification where it answers; and the answer is
  the unique satisfier of the specification —
  determinism as a theorem.
- Certification (2): soundness — a certified answer's
  score is at least the score of every completion in
  the enumeration and at least every recorded frontier
  bound, under the coverage premise named below; and
  blocking — a frontier bound above the best complete
  score makes certification false, proved outright.
- The overlay (8): the inverse overlay's multiplier at
  a key is the inverse fraction; multipliers are
  positive where every recorded multiplier is, and an
  unedited key keeps its recorded multiplier; weight
  scores are congruent under equal weightings; the
  round trip restores every weight and every path score
  exactly; the empty overlay changes no score; and cone
  invariance — a path touching no edited key scores
  under the overlay exactly as on the recorded table.
- Route one (2): weightings agreeing on an axis list
  give equal scores over it; a reweighting at one axis
  leaves every score over a list excluding that axis
  exactly equal to its full recomputation.
- Standing controls (2), proved: greedy is not
  certified — on the control table greedy returns the
  completion scoring 9 while the decoder returns the
  one scoring 45, by computation; and an unresolved
  bound above the best complete score blocks
  certification.

## Premises, absent set, and measured cells

- On named premises: the coverage premise — every
  completion beneath a frontier prefix scores at most
  the bound recorded for that prefix. Where rows are
  probability rows and the bound is the prefix's own
  score, the premise holds by construction; for an
  arbitrary archived table it is a checkable condition,
  and the certification theorem is stated under it,
  never without it. Its falsification route stands
  named in the repo's census, and the harness's first
  fixture draft exercised it. The six pipeline premises
  carry over unchanged, with axis meaning the one this
  paradigm leans on hardest: a parameter whose name has
  no definition is refused.
- Measured in the repo, at fixture scale only: the
  certified score equals the exhaustive oracle maximum
  on every certified query on both seeds; the edit
  locality battery holds exactly off the edited cone;
  the route one batteries hold on every sampled
  weighting. These are executed results at fixture
  scale, counted nowhere in the proven column.
- Absent and unmeasured, as the repo itself prints:
  the real checkpoint cells are UNMEASURED — the
  standalone fixture repo is not on the machine that
  built this repo, a named access blocker standing
  since 2026-11-19; code generation beyond fixture
  scale, live serving latency and throughput, and the
  live demo surface's conformance are each UNMEASURED
  with their blockers named; the compression horizon
  is proposed, not implemented; and the canonical
  registry append of this repo's extract is owed, its
  append ready form standing in the tree.

## Controls and gate state

- Controls in tree: the two proved standing controls
  above, inside the core file.
- Gate state: green at the pin by the repo's recorded
  log — the gate script compiles every Lean file with
  warnings as errors, scans for escape tokens, and
  prints an axiom line for all 40 theorems, every set
  inside the three standard axioms, ending in its
  subset check passing. Of the 40: 9 depend on no
  axioms, the rest on subsets of the standard set, as
  the recorded log prints them.

State: PROVEN in source at the pin for the 40 theorems,
on the recorded gate log at the pin — certification
soundness under its named coverage premise, the
premise register carried, the measured cells at fixture
strength, and the unmeasured cells standing as named
work at their owners. The census pin is set to the
fresh head on this first census; the placements in the
synthesis and the ledger row are entered at the pin in
this same pass.

## Watch delta — 2026-11-22, the ninety-fourth hourly re-synthesis watch

The watch re-read this repo's live head at 2ed9a077e11f3fee024120ad5648c8f59dd204c0 in the full enumeration and read the whole tree at that head (16 files, not truncated) and at the last recorded head ca4ca2b39181bb93a717b3edbb58ab476761fa5c (12 files). No Lean file stands among the changed files between the heads, so the proven set is unchanged: the same forty declarations with the same name set at both, counted by the watch method over the tree at each pin, with no sorry token and no axiom declaration at the fresh head. The movement is five commits on incremental recomputation of certified best-first synthesis — lookup cones, deletions under the update and checker bar, early cutoff, and the resume rule — landing as executed harness work: four files added, the incremental harness folder with its gate, its synthesis module, and its readme, none of them Lean. That harness work is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at ca4ca2b39181bb93a717b3edbb58ab476761fa5c in the pins file's census record for this repo, with the placements at that pin.

## Watch delta — 2026-11-22, the hundred-sixth hourly re-synthesis watch

The watch re-read this repo's live head at aedf97ec908afb2957db91e512c13b06461cfab1 in the full enumeration and read the whole tree at that head (17 files, not truncated) and at the last recorded head 2ed9a077e11f3fee024120ad5648c8f59dd204c0 (16 files). Every Lean file is byte-identical between the heads, so the proven set is unchanged: the same forty declarations with the same name set at both, counted by the watch method over the tree at each pin, none gained and none lost. The movement is one commit of incremental synthesis work — a randomized differential check on a shared gate version — landing as executed harness work: one file added, a fuzz script in the incremental harness folder, and two files changed, its readme and its gate source, none of them Lean. That work is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at ca4ca2b39181bb93a717b3edbb58ab476761fa5c, with the placements at that pin.
