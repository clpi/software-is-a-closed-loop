# Census — idol-lib (its proof-bearing content)

## Pin and identity

- Census pin and live head (read in the twenty-fourth
  enumeration, 2026-11-19):
  ad22a681a497599fbe2ce96f96f48e17484439af
- Visibility: private. Default branch: master.
- Description (the repo's own): "Daily graph-native Idol
  rewrites of major open source codebases: one per day,
  minimum lines, minimum syntax, highest performance,
  proven against the incumbent."
- This repo is the library ports line of the Idol family
  and keeps that placement; this annex censuses only its
  proof-bearing content, which is new in this window.
- Landed in this window: at every earlier enumeration the
  repo was proof-free by the named check, and this pass
  re-verified that state by tree read at the last recorded
  head (f01da7ad) — no proof-assistant source stands in
  that tree. Ten commits then landed the Redundant
  empirical reconstruction campaign at the fresh head:
  behavioral hypergraphs for the libraries, per-symbol
  contract extraction with two-way search, the campaign
  itself with its checked proof kernel, and the measured
  reconstruction atlas with its witnesses. The movement
  adds 159 files and changes one (the readme); no file
  was removed. The tree stands at 1,152 files (was 993),
  115 of the added files under the campaign folder,
  including the three Lean files censused below.
- Toolchain: Lean 4.19.0, pinned in the campaign proof
  folder's toolchain file. The campaign kernel imports
  only the standard distribution; the atlas file imports
  the kernel. No Mathlib stands in the tree, and no Rust
  file stands in the tree, so no second proof system is
  present.
- Determination: proof-bearing by content — Lean sources,
  a checker, recorded receipts, and recorded gate logs
  stand in the tree, found by the content check on the
  enumeration that first saw them, not by the repo's
  name.

## Thesis, in plain English

The campaign turns optimization claims about open-source
software into inspectable source, contract, trace, proof,
and cost records: a claim is carried at its evidence
state — measured, constructed, proved, falsified, or
unknown — and never higher. Its Lean content proves the
abstract obligations the campaign's method rests on:
that reconstruction from retained evidence is faithful
only under a round trip, that intent axes preserve
observations only when observations factor through them,
that rewrites compose only under per-step preservation,
that a keyed ledger replays safely and refuses
collisions, that certified cost bounds compose into a
robust economic bound, that hypergraph derivations from
sound seeds and sound full-premise rules are sound and
stay reusable while their premises are retained, and
that selection over a finite declared candidate list is
optimal for that list and no larger universe. The repo's
own trust boundary, stated in the kernel's readme, is
part of the thesis as carried here: the theorems concern
the abstract model, and no theorem in the tree
establishes that an existing compiler, extracted symbol,
observed profile, effect summary, or monetary estimate
implements the model.

## Theorem census — 38 declarations in two Lean files, plus six checked examples

Counted by the watch method in this census: every
theorem declaration in every Lean file at the pin. No
admitted-proof token, no axiom declaration, and no
native-evaluation token stands in any of the three Lean
files, by this census's own scan.

### The campaign kernel — 25 theorems

One Lean file in the campaign proof folder (16,362
bytes), with a printed axiom audit for every theorem in
the file itself:

- Reconstruction (2): a decode-after-encode round trip
  makes the encoding injective; and the history
  obstruction — two different histories with identical
  retained evidence cannot both be uniquely recovered by
  one deterministic reconstructor (a proved negation).
- Intent axes (1): equal extracted axes give equal
  observations, when the observation factors through the
  axes.
- State space (2): a forward simulation carries every
  finite concrete execution to an abstract execution;
  safety of all abstract reachable states transfers to
  concrete reachable states.
- Effects (1): a union of observed effects stays below
  the union of their proved upper bounds.
- The rewrite composer (2): a finite plan of rewrites,
  each preserving the invariant and the observation on
  invariant states, preserves both as a whole; per-step
  non-increasing modeled cost composes the same way.
- Ordering (1): an adjacent swap inside a plan preserves
  the final state when the two transformations commute.
- Idempotence (3): two commuting idempotent
  transformations compose idempotently; each of the two
  concrete three-state transformations is idempotent;
  and the disproof — two idempotents need not compose
  idempotently without a compatibility condition, by the
  three-state counterexample (a proved negation, the
  kernel's standing control result).
- The keyed ledger (4): a keyed write reads back at its
  key; a keyed write preserves every other key; replay
  of an accepted keyed event is a no-op; a conflicting
  payload under an occupied key is rejected.
- Economics (2): weighted cost over a fixed axis list
  preserves componentwise domination; and the robust
  economic bound — a candidate under its certified upper
  bound, plus overhead, stays under a baseline above its
  certified lower bound, when the certificate inequality
  holds.
- Contract cover (1): a selected contract set implies
  every enumerated requirement, when each requirement
  has a selected provider and each provision derives the
  requirement.
- Hypergraph derivation (2): every derivation from sound
  seeds and sound full-premise rules is sound; a
  derivation stays valid when its seeds and rules are
  retained in a larger context.
- Finite optimization (3): the executable minimum over a
  nonempty finite list is a member of the list and costs
  no more than any member; if every member is feasible
  the minimum is feasible; if the list covers a declared
  universe, the minimum is optimal for that universe and
  that scalar objective.

Recorded evidence at the pin: the proof folder carries
its checker script, its raw run logs, and its receipt.
The receipt records kernel-checked status on Lean
4.19.0 with exit 0, the full 25-name inventory present
with none missing and none unexpected, the axiom audit
complete — 15 theorems depending on no axioms and 10 on
propositional extensionality only, with no other axiom
anywhere — the source gate clean, and no
native-evaluation axioms. This census verified the
binding firsthand: the receipt's recorded source hash
equals the hash of the kernel file in the tree at the
pin, and its recorded checker hash equals the hash of
the checker script in the tree at the pin.

### The atlas proofs — 13 theorems

One Lean file in the atlas folder (8,594 bytes),
importing the kernel:

- Gathering and composition (2): a lookup in the emitted
  table returns the per-key value for any key in the
  work order, under a faithful venue realization; the
  batch composer — a covering job list read through the
  gathered table returns the full output vector, in
  order and multiplicity.
- Work lower bound (1): a duplicate-free covering list
  is no longer than any covering list — deduplicated
  work uses the least possible number of evaluations
  among covering key lists, for opaque per-key contracts.
- Frontier exactness (1): membership in the computed
  frontier is exactly membership in the rows with no
  dominator among them.
- State abstraction (2): states with equal groupings
  keep equal observations under every continuation, when
  the grouping respects the observation and is stable
  under steps; and the distinguishing lower bound — a
  distinguishing continuation forces any such grouping to
  separate the two states.
- Scoring and break-even (2): the score update identity;
  and the break-even equivalence between a setup cost
  bound and the ceiling-division volume bound.
- The Adler development (3): the shifted scan law for
  the two unreduced accumulators; concatenation of two
  scans in closed form; and the modular residue
  arithmetic the extracted formula uses.
- Adaptive policy (2): the Bellman lower bound — any
  bound function satisfying the terminal and step
  conditions lower-bounds every policy's budget; and the
  minimax certificate pairing a witness policy at the
  bound with that lower bound over all budgets.

Axiom states from the recorded check text in the atlas
evidence folder, which prints 10 of the 13: 2 depend on
no axioms (sufficient state; the distinguishing lower
bound), 1 on propositional extensionality only (the
minimax certificate), 5 on propositional
extensionality and quotient soundness (the batch
composer, frontier exactness, the score update, and the
two Adler closed forms), and 2 on the full standard set
(the work lower bound; the break-even equivalence). The
remaining three (gathering, the shifted scan, the
Bellman lower bound) carry no printed audit in the
recorded text; their axiom states are unrecorded there.

### The witness file — six checked examples

One Lean file in the atlas evidence folder (6,738
bytes), generated and byte-compared by the atlas gate:
no theorems, and six examples each proved by decision —
for each of the two recorded snapshots, the frontier of
the 96 recorded rows is the single named plan, the
observation list has length 96, and the distinguishing
signatures of all 96 states are pairwise distinct.
These are kernel-checked finite witnesses at the
recorded data, counted as checked examples, not as
theorems.

## Premises and the absent set

- On named premises: the Lean developments carry no
  premise beyond their stated hypotheses. The campaign
  as a whole carries the kernel readme's trust boundary
  as its standing premise: every concrete application
  must supply the named hypotheses — the round trip, the
  factorization, the simulation, the per-step
  preservation and commutation witnesses, the effect
  upper bounds, the cost certificates — plus an
  implementation-to-model refinement witness.
- Absent: that refinement. No theorem in the tree
  connects the abstract model to the library's Idol
  ports, to the extracted upstream programs, or to the
  measured systems; the atlas readme states the same
  boundary from the measurement side. The campaign's
  wider program in its specification — the Ocean
  execution and economic model carried end to end, and
  the public campaign surface at its intended hostname —
  stands proposed at the repo's own states: the campaign
  readme states the addition does not deploy the domain
  and does not claim the full product is implemented.
  The atlas measurements are measured and constructed
  evidence at their recorded scopes, not proofs, and
  their unmeasured cells (human hours, power, peak
  memory, actual spend, remote venue performance) stand
  recorded as unmeasured in the atlas readme.

## Controls and gate state

- Controls in tree: five recorded negative controls for
  the kernel gate, each rejected as required — an empty
  proof file, a missing effect-bound family, a missing
  axiom audit, an admitted proof hole, and a custom
  axiom asserting falsity — recorded with their mutated
  source hashes in the gate controls record beside the
  receipt. The atlas gate carries its own controls
  script and receipt-mutation checks; the recorded
  campaign check log lists keyed error replay, refusal,
  state distinction, three economic boundaries, and four
  receipt mutations among its passed lines.
- Gate state: the kernel gate is green on its recorded
  receipt at the pin (kernel-checked, exit 0, hashes
  verified by this census as above). The atlas gate
  script compiles the kernel and the atlas file with
  warnings as errors on the pinned toolchain, regenerates
  the witness file and its verified record and compares
  both byte-for-byte with the recorded files, compiles
  the witness, scans the combined output for admitted
  proofs, warnings, and errors, and runs its native
  checks, its controls, and a clarification comparison;
  a recorded campaign check log stands in the tree. This
  census ran no build: a fresh gate run at this head by
  this watch is unrecorded, and the gate state stands on
  the recorded evidence in the tree.

State: PROVEN in source at the pin, on the recorded and
hash-bound evidence, for the 38 theorems at the axiom
states named above; the six witness examples CHECKED by
decision at the recorded data; the model-to-program
refinement ABSENT — an obligation the repo itself names,
not a result; the wider campaign program PROPOSED at the
repo's own states.
