# Census — deterministic-llms

## Pin and identity

- Census pin and live head (read in the sixty-second
  enumeration, 2026-11-20):
  6151727a7ec67d15fdbb0fbfa48c2f305057aa69
- Visibility: public. Default branch: master.
- Description (the listing carries none; the repo's own
  readme names it): parametric deterministic language
  models — generation as a deterministic function of
  the content and a few named, meaningful weights,
  decided by a certified best-first rule and rewritable
  incrementally.
- The repo entered the census in the sixty-first
  enumeration as a long-tail row at its first commit,
  a tree holding a single ignore file and nothing
  else. In this window it landed its whole content in
  five commits: a specification, a claims ledger, a
  Python harness, frozen task contracts, recorded run
  outputs, and a Lean package. Its tree now stands at
  thirty-seven files.
- Toolchain: Lean 4.19.0, pinned in its toolchain
  file. No Mathlib; the package imports only the
  standard distribution.
- Determination: proof-bearing by content — Lean
  sources, a gate script, and a recorded gate log
  stand in the tree, found by the content check on
  this enumeration, not by its name. The repo is
  newly proof-bearing in this pass.

## Thesis, in plain English

Decoding is a total deterministic function of two
inputs only: the content so far and a short vector of
named weights, one per meaningful axis of the next
token (repetition, a repeated three-token run, a
banned word, a topic word, a sentence end, an
embedding direction, and a do-nothing axis). Each
candidate token is scored in exact integer arithmetic
— a base score from the model plus the weighted sum
of its axis features — and a certified best-first
rule picks the highest score, breaking ties by the
lowest token number, with a certificate whose margin
says by how much the pick beats every rival. A weight
change rewrites the run incrementally: the rescored
run is proved equal to the run recomputed from the
base scores. The model exercised is one small named
model at one named size, named in the repo's ledger;
every quality figure in that ledger is a small-sample
executed estimate, counted nowhere in the proven
column here.

## What stands at the pin — 54 theorems in four Lean files

Counted firsthand over the tree at the pin: 54
theorem declarations in four files, beside an
executable file and a package file carrying no
declarations. No sorry token and no custom axiom
declaration stands in any Lean file by this watch's
scan. The files group as the repo's own specification
groups them, restated here in plain terms:

- The core file (31): the strict order on candidates
  is transitive and irreflexive in both its plain and
  its negated forms; the one-pass pick is a candidate,
  nothing beats it, and the unbeaten candidate is
  unique; the pick and every generation are the same
  under any candidate order; certification is sound
  — a certified pick strictly beats every other
  token by at least the margin — and complete — a
  strictly best token is picked and certified;
  rescoring a scored list by a weight change equals
  recomputing the scores with the new weights, per
  step and per generation; inside the margin box the
  pick is unchanged without recompute; an axis that
  is zero on every candidate changes no score, no
  pick, and no generation, whatever its weight; a
  cache of base scores that is correct on its keys is
  invisible; outputs extend their content; cached
  lookup is correct; and the reweighted generation
  that reuses cached base scores equals the
  generation from scratch.
- The search file (19): the dominance and sum laws
  for vectors; the online archive holds exactly the
  Pareto front of what has arrived, after every
  arrival and in any arrival order; for an additive
  score over independent factors, the plan of
  per-factor minima is a plan and no plan scores
  lower; and Chebyshev weights aimed at a front point
  give that point its target score while every point
  that does not strictly dominate it scores at least
  as much, so every front point is a minimizer of
  some such weighting. By the repo's own statement
  this file is copied unchanged from the redundant
  compute repo's seventh pull request — a second
  home for the same content, counted here as this
  tree carries it and credited to its first home in
  the synthesis placement.
- The skipping file (2): tokens accepted from a
  drafted continuation are exactly the next tokens of
  the rule's own generation; and acceptance under a
  batched forward pass equals acceptance under
  per-step scoring when the two scorings agree —
  that agreement is an explicit premise of the
  theorem, not a hidden assumption.
- The sparse file (2): a list-membership helper, and
  the exact sparse rule — after a weight change the
  pick is the best of the candidates whose score
  moved together with the single best unmoved
  candidate, with no margin and no box required,
  exact whenever the moved set is known.

## Premises, absent set, and unmeasured cells

- On named premises: the batched-forward equality
  above, carried as a premise in the theorem's own
  statement and measured in the repo's run — bitwise
  equal at every one of 479 positions on the recorded
  configuration, an executed result at its own
  strength. The determinism of the float forward pass
  itself is not proved and is carried as measured;
  what an axis means and whether outputs are good
  are likewise measured, never proved, as the repo's
  own specification states.
- Refuted in the repo's own ledger, at executed
  strength: cross-history sharing of drafted work on
  its data (almost all reuse is a history repeating
  itself); unverified skipping as exact; the margin
  box as a frequent saver of recompute; the topic
  axis at its declared weight; and the decompiling
  hypothesis for embedding directions at the declared
  weight, on held-out words against a random-direction
  control. The broader decompiling claim — attention
  or other weight families, a whole model rewritten
  — stands unmeasured, as the repo prints.
- Absent and unmeasured, as the repo itself prints:
  any model other than the one small named model;
  quality judged by people; long outputs; determinism
  across machines, processor types, or runtime
  versions; native or Idol implementations; the exact
  cone region per step; and decompilation beyond the
  token embedding.

## Controls and gate state

- Controls in tree: two proved standing controls in
  the search file — an unsupported front point that
  aimed Chebyshev weights reach, proved by decision,
  and the companion result that no positive weighted
  sum picks that point. Beside them stand executed
  controls, counted as executed evidence and not as
  theorems: a clean three-step fixture that the gate
  replay must pass and a tampered copy that it must
  fail, both wired into the repo's continuous
  integration workflow; a do-nothing axis control
  that changes nothing across its three task sets;
  and gamed controls, labelled gamed in the ledger
  and never counted.
- Gate state: green at the pin by the repo's recorded
  log — the recorded check output in the tree shows
  the cold build completing, axiom lines printed for
  seventeen named theorems, every one inside the
  standard three (propositional extensionality,
  classical choice, quotient soundness, in subsets),
  and the check passing. The gate script builds the
  library and the executable with warnings as errors,
  scans for escape tokens and custom axioms, and
  fails closed on any axiom-check error — a recorded
  correction in the repo's ledger, whose tamper
  control (an inserted sorry) now fails the gate.
  Whether the integration workflow passes on the host
  is reported on the repo's pull request, not claimed
  here.

State: PROVEN in source at the pin for the 54
theorems, on the recorded gate log at the pin — the
batch acceptance result under its in-statement
premise, the search file carried as a copied second
home at the repo's own statement, the specification's
empirical ledger at its own executed verdicts
(verified, corrected, refuted, and unmeasured as it
prints them), and the unmeasured cells standing as
named above. The census pin is set to the fresh head
on this first proof census; the placements in the
synthesis and the ledger row are entered at the pin
in this same pass.

## Watch delta — 2026-11-20, the sixty-fourth hourly re-synthesis watch

The watch re-read this repo's live head at 8c4aa56af769ccba2b32e7a11c160cffc3f34227 in the full enumeration. Every Lean file is byte-identical between the census pin 6151727a7ec67d15fdbb0fbfa48c2f305057aa69 and that head, so the proven set is unchanged: 54 theorems in four files, the same name set at both pins, counted by the watch method over the tree at each pin. The movement between the pins is two commits of executed-layer growth: twelve files added — the architecture, density, and multi-model harness modules, their three frozen contracts, and their recorded reports and run output — and seven files changed, among them the claims ledger, the specification, and the readme, beside harness and recorded output files. That growth is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at 6151727a7ec67d15fdbb0fbfa48c2f305057aa69.
