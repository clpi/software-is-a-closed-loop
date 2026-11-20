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

## Re-census — 2026-11-19, the twenty-fourth hourly re-synthesis watch (pin 4dee2311)

Three commits past the census pin ad22a681 landed the
campaign's Pareto release condition: a new proof package
requiring proved Pareto unimprovability for a qualified
optimal release, its specification section, its release
record, and its views. The watch read the trees at both
heads in full and compared every file: twenty-eight
files added, seventeen changed, none removed, and the
tree stands at 1,180 files (was 1,152). Of the three
Lean files at the census pin, every one is byte-identical
at the new head, so the thirty-eight theorems and the
six checked witness examples of the census above stand
unchanged; the kernel receipt and its controls record
were re-recorded in this window at a fresh time stamp
with the same source and checker hashes and the same
kernel-checked status. One Lean file was added, censused
in full below, and the census pin moves to the new head
on this re-census.

### The Pareto package — 27 theorems in one new Lean file

One Lean file in the campaign's Pareto folder (20,192
bytes, Lean 4.19.0, importing only the standard
distribution), with a printed axiom audit for every
theorem in the file itself. Its subject is Pareto
unimprovability: a candidate is optimal when it is
feasible and no feasible alternative is no worse on
every declared cost axis and strictly better on one.

- The strict relation (2): no candidate dominates
  itself, and domination cannot run in both directions
  between two candidates.
- The global witness (2): a feasible candidate with a
  certificate excluding every feasible dominator is
  optimal; and the per-alternative form, where each
  alternative is excluded by a worse axis or by equality
  on every axis.
- Coverage forms (4): optimality transfers from a
  finite enumeration when every feasible alternative
  stands in it; from an enumeration covering only the
  dominance cone, the alternatives no worse everywhere;
  from normal forms, when every feasible concrete
  alternative maps to a feasible normal form at no
  greater cost and the candidate's costs are preserved
  exactly; and from a finite cell cover, when every
  feasible alternative belongs to a cell and each cell
  excludes domination, in its direct form and in its
  lower-bound form, where valid cell lower bounds
  separate the candidate from every member.
- The weighted score (3): a weighted score over a
  finite axis list is monotone in the values; it is
  strict when every listed weight is positive and one
  value strictly improves; and a global minimum of such
  a score, over a list covering every axis with every
  weight positive, is Pareto optimal.
- The standing counterexamples (5, proved results at
  the strength stated): a scalar minimum under a zero
  weight exists by decision, yet that minimum is not
  Pareto optimal, because the ignored axis carries the
  domination (a proved negation, with the combined
  counterexample beside it: a singleton list internally
  free of domination whose candidate is still not
  optimal, its dominator omitted); and a standalone
  choice is optimal while the component optima need not
  compose — the jointly fused alternative dominates the
  composed candidate under the coupled cost (a proved
  negation).
- Bounded uncertainty (2): valid candidate upper bounds
  and competitor lower bounds that separate exclude
  domination; and a certificate for every admitted
  scenario proves optimality scenario by scenario.
- The retention model (8): normalization of a retention
  plan — dropping its extra evaluations and extra slots —
  stays feasible, is no worse on every axis (work,
  retained values, and the linear tariff), and its
  normal form stands in the finite representative list;
  a competitor no worse in both primary resources is
  the normal form itself, so the normal form is Pareto
  optimal in the model, with the concrete instance
  proved optimal at its exact recorded costs; the
  feasible domain carries arbitrary redundancy — plans
  with any extra work at all are feasible and distinct —
  so the domain is no finite search box; and the single
  batch case is a proved negation: with one batch the
  full retention plan can be dominated, so repeated use
  is load bearing.

Recorded evidence at the new pin: the package carries
its checker, its recorded receipt, its raw run output,
and its controls record. The receipt records
kernel-checked status on Lean 4.19.0 with exit 0, the
full twenty-seven name inventory present with none
missing and none unexpected, the axiom audit complete —
14 theorems depending on no axioms, 2 on propositional
extensionality only, 10 on propositional extensionality
and quotient soundness, and 1, the interval exclusion,
on the full standard set — the source gate clean, and
no native-evaluation axioms. This census verified the
binding firsthand: the receipt's recorded source hash
equals the hash of the Pareto file in the tree at the
pin, and its recorded checker hash equals the hash of
the package's checker script in the tree at the pin.
Five recorded negative controls for this package's gate
stand rejected as required: an empty proof file, a
missing robust scenario family, a missing axiom audit,
an admitted proof hole, and a custom axiom.

### Premises and the absent set, restated at the new pin

- On named premises: the package's own scope line is
  its standing premise — its theorems concern the
  natural-valued abstract models only, and no software
  or measured-cost refinement is proved there. Its
  retention results rest on the model's stated premises
  (a stationary retention discipline, at least two
  batches, the recorded cost equations), carried in its
  readme as model premises, not derived from any
  operational trace.
- Absent, at the repo's own states: the release
  admission of actual software under the new requirement
  stands open in the repo — its readme states the model
  certificates satisfy their named model obligations
  while actual-software release admission remains open
  and the release command refuses it. The refinement
  absence of the census above stands unchanged: no
  theorem connects any of these models to the library's
  ports or the measured systems.

State: PROVEN in source at the new pin, on the recorded
and hash-bound evidence, for 65 theorems in total across
the repo's three theorem files (the 38 of the census
above, unchanged, plus these 27), at the axiom states
named; the six witness examples CHECKED by decision, as
above; the model-to-program refinement and the
actual-software release admission ABSENT — obligations
the repo itself names, not results. The census pin
moves to the new head,
4dee23111e7d356c79958bd69e77c775faeecfbb, on this
re-census; the placements in the synthesis and the
ledger row are restated at the new pin in this same
pass.

## Watch delta — 2026-11-19, the fortieth hourly re-synthesis watch

The watch re-read the live head at 0052f16e6883620a77ab3cab067b8cdaf96ebdb1 in the full enumeration and read the tree at that head in full. The movement since the census pin is five commits: a realization route that runs five hash batteries without the compiler, a new entry for one further hash with its generator, its vectors, and its verifier, added edge coverage for one battery, and hardening that rejects a short transcript and an unrun differential. Twelve files were added and one changed, none removed; no tree read was truncated. Every one of the four Lean files is byte-identical between the census pin and the fresh head, blob for blob across the whole tree read, so the proof content this census records — the campaign kernel, the atlas development, the Pareto package, and the witness examples — stands unchanged at the fresh head: 65 declarations, the same name set at both heads, no name gained and none lost, counted by the watch method. The added files are realizations in a systems language, their supporting scripts, and a dated port note, and the one changed file is the ledger; none of them carries proof content beyond the four Lean files already censused. Premises, the absent set, and gate state stand as the census above records; a full census at the fresh head adds nothing while the proof files stand identical, and the census pin stands at 4dee23111e7d356c79958bd69e77c775faeecfbb with the fresh head recorded here.

## Re-census — 2026-11-20, the forty-fifth hourly re-synthesis watch (pin 578b8b3a)

Six commits past the last recorded head 0052f16e
landed a new proof package beside the campaign: the
space development — Lean proofs and falsifications
over the behavioral hypergraphs the repo carries for
its fourteen witnessed libraries. The watch read the
trees at both heads in full and compared every file:
twenty-five files added, none changed, none removed,
and the tree stands at 1,217 files (was 1,192). Every
one of the four Lean files at the last recorded head
is byte-identical at the new head, so the sixty-five
theorems and six checked witness examples of the
censuses above stand unchanged. Sixteen Lean files
were added under the space folder — two generated data
files, a core definitions file, ten theorem files, an
axioms audit file, and the package's build files —
censused in full below, and the census pin moves to
the new head on this re-census.

### The space package — 55 theorems in ten Lean files

One package on Lean 4.19.0, importing only the
standard distribution. Its data files are generated
from the repo's hypergraph records by the package's
own generators: the level two file carries the current
source projections of the fourteen libraries, and the
level one file carries the earlier version's graphs
frozen, so the two levels can be reconciled in the
kernel rather than by reading. Most data theorems are
proved by kernel decision over that generated data.
No escape token stands in any theorem file, by this
census's own scan; the data files' name strings are
data, as the package's check script itself records.

- The level two witnessed file (10): the filter chain
  nests — qualified inside measured inside source — at
  the definition level and at the count level; every
  node is a source record; nothing anywhere is
  measured or qualified, and no library carries an
  execution or proof receipt; the definition count,
  444 definitions over the fourteen libraries; one
  named library's 133 definitions stand none of them
  measured or qualified; 70 names are shared between
  libraries, 26 of them with an identical body in two
  or more homes and 44 with a different body in every
  home; and the joined graph is exactly the disjoint
  sum of its libraries, its counts the sums of theirs.
- The level one witnessed file (9): the same chain at
  the earlier level, with qualification read as
  observed plus the gate; qualification is exactly
  observation under the gate; 155 definitions are
  observed, 9 of them on substring matches only; the
  named library has no directly observed definition
  while its qualified node count stands at 1,320; 56
  names are shared and every one differs in shape
  across its homes; and 14 names leaked qualification
  through the old joined graph.
- The reconciliation file (8): the two levels carry
  the same library list and the level two names extend
  the level one names, within the packing bound the
  file states; the 155 definitions qualified at level
  one are all present at level two and all unqualified
  there — level two admits qualification only from a
  receipt, so the earlier status is retracted by the
  level change itself; 318 of the 321 level one keys
  are kept and 106 keys are new, the three missing keys
  recorded in the package readme as compiler evidence
  fixtures outside the source manifest; 29 level two
  definitions are nested bindings, and the named
  library's only one is its loop-local binding.
- The observer file (4): a reading is determined by a
  battery exactly when it factors through the battery's
  observations, in general; the helper of an observed
  root is not determined — a proved refutation; an
  unrecorded input of an observed root is not
  determined — a proved refutation carrying the
  coverage premise; and the observed root on its
  recorded input is determined.
- The host file (4): in the joined graph with host
  edges, a host change reaches every library; reach in
  the per-library relation alone forces the host
  itself, that relation being empty; the joined
  semantics is local; and the falsification package —
  per-library graphs miss the host: a quality reading
  that holds of the old host semantics and is preserved
  along per-library reach fails at the named symbol
  under the new host, while the joined reach stands.
- The merging file (4): the toy semantics is local;
  merging by name is unsound — a proved refutation;
  merging by identical body is unsound — a proved
  refutation, the callees differing; and merging by
  whole dependency closure is sound, given the
  locality premise the file names.
- The effects file (3): derived effects are monotone
  in the dependency relation; a symbol is free of an
  effect exactly when no symbol in its closure owns it;
  and joining effects over a list is order free, the
  joined reading invariant under permutation.
- The economics file (6): a constructed dominance
  transfers to a measured one when our constructed
  bounds stand above our measurements and theirs below
  theirs; the wrong direction fails — a proved
  refutation by decision; a serial pipeline's total is
  bounded below by the kept stages' costs under the
  stated keeping condition; every stage's cost is
  bounded by the total; money is monotone in the
  amount; and one named rewrite's measured loss — its
  own recorded readings are slower on every run, a
  measured loss printed as a loss and proved by
  decision over the record.
- The temporal file (3): an appended verdict stays at
  its recorded position — history is append only; no
  monotone verdict law holds — a pass followed by a
  failure history exists, a proved refutation; and a
  verdict carries to a later snapshot only when the
  closure is unchanged, under the locality premise.
- The realized file (4): the realized batteries pass
  on their receipts — 307 passed lines over five homes
  with no oracle or differential mismatch, the
  differential running for three of the homes; the
  realized counts and the cover of the library list
  are as recorded; and a realized run qualifies
  nothing — it executes a foreign implementation of
  the contract, not the library source, proved over
  the same data that shows nothing measured or
  qualified anywhere.

### Premises, gate, and the absent set at the new pin

- On named premises: the locality premise — a
  definition depends only on its declared closure —
  carried as a named hypothesis where the merging and
  temporal results use it, and unproven for the
  repo's graphs, whose edges are a name scan, as the
  package readme itself states; battery coverage; the
  price of compute; and which fields of an observation
  are public. Each enters as a named hypothesis in the
  files that use it.
- Gate evidence: the package's check script
  regenerates both data files and fails on any drift,
  builds with warnings as errors, and runs an axioms
  file printing lines for 44 of the 55 theorems — the
  eleven unprinted are the general helpers and model
  results the audit does not name. No recorded run of
  the script stands in the tree, so a passing gate at
  this pin is unrecorded; the receipts file in the
  package records the realized batteries' executed
  runs (five homes, every line passed, exit zero), which
  is executed evidence for those batteries, not a Lean
  gate log.
- Absent, at the repo's own states: per-symbol
  profiles and bottlenecks stand UNMEASURED — only
  whole-library benchmarks exist; the per-symbol
  contract extraction scaffolding is constructed and
  unexecuted, and this package does not read it. The
  refinement absence of the earlier censuses stands
  unchanged.

State: PROVEN in source at the new pin, on this
re-census's full reading, for 120 theorems in total
across the repo (the 65 of the earlier censuses,
unchanged, plus these 55), at the axiom states the
package's audit file names in source; the six witness
examples CHECKED by decision, as above; the gate at
this pin UNRECORDED — one step below the kernel and
Pareto packages' recorded, hash-bound strength; the
locality premise CARRIED as named; per-symbol profiles
UNMEASURED. The census pin moves to the new head,
578b8b3a7e212082bf0d1f8a5a582cca63af3a19, on this
re-census; the placements in the synthesis and the
ledger row are restated at the new pin in this same
pass.
