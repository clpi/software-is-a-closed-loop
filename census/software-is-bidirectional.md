# Census — software-is-bidirectional

## Pin and identity

- Census pin and live head (read in the twenty-third
  enumeration, 2026-11-19):
  b14fc92b77d27411775be1a6a64428ff8fad247a
- Visibility: public. Default branch: main.
- Description (the repo's own): "Contracts
  bidirectionally produce engineering and reengineering
  analysis for arbitrary qualifications: proved model
  and empirical campaign".
- Landed in this window: the repo stood empty at the
  twenty-second enumeration — no commits, no tree,
  accounted as carrying no provable results — and its
  first content landed in three commits at this head:
  the bidirectional model with its controls, the
  composition with the joined theorem, and the
  specification, definitions, and first census tranche.
- Toolchain: Lean 4.19.0, pinned in the proof folder's
  toolchain file. No Mathlib; the development is three
  Lean files in one proof folder, beside a check script,
  a recorded check log, and the toolchain file, with a
  readme, a specification file, a definitions file, and
  a census file at the root — ten files in the tree.
- Determination: proof-bearing by content — Lean
  sources and a recorded gate log stand in the tree,
  found by the content check on the enumeration that
  first saw its content, not by its name.

## Thesis, in plain English

Contracts — vanishingly, compoundingly small, possibly
independently derivable, with a search space that is
parametrically solvable, optimizable, and
synthesizable — bidirectionally produce, completely
equivalently or via an independent methodology, an
optimally and speculatively optimizable engineering
and reengineering analysis for any arbitrary set of
qualifications. The repo carries the proved model of
that claim: a system is recorded as facts, recorded
steps, and a behavior record; an analysis map derives
its contract and a synthesis map builds the canonical
system from a contract, and the two round trip. The
constructed measures across software — performance,
size, compression, scheduling, ordering, venue
selection, and the named measures of semantic mass,
velocity, redundancy, and suboptimal scheduling, venue
use, and parametric test sets — are solvable, with
upper and lower bounds found incrementally over the
compounding join-semilattice of possible states, and
the search space is finite with a computed size,
derived from the qualification's own finiteness. The
claim was directed by Chris on 2026-11-19; the repo's
specification states it in full, with its executable
twelve step method, its falsification protocols, its
gap register of ten owned gaps, and its measures, and
its definitions file states every term at implementer
resolution. The one premise the theorems cannot
discharge — that a real system's measures factor
through its derived contract — is carried as a named
premise and tested by the repo's empirical census arm.

## Theorem census — 73 declarations in three Lean files

Counted by the watch method in this census: every
theorem declaration in every Lean file at the pin. No
admitted-proof token stands in any file, by this
census's own scan. Axiom states are from the repo's
recorded check log, which prints 74 audited
declarations — the 73 theorems plus the optimum
decision definition, which the gate also prints; of
the printed 74, 19 depend on no axioms, 27 on
propositional extensionality only, and 28 on the
standard pair, and none on the classical choice axiom.
The decision definition is one of the 19 axiom-free
prints, so the theorems alone stand 18 axiom-free, 27
on propositional extensionality only, and 28 on the
standard pair.

### The core model — 52 theorems in the core file

- The hyperlattice (6): the join laws — commutativity,
  associativity, idempotence, the two unit-side
  membership facts, and join as least upper bound —
  over states taken up to membership equivalence,
  ordered by information.
- Derivability (3): closure under one recorded step,
  monotonicity in the state, and derivability through
  the recorded steps.
- The analysis map (1): additivity of the derived
  contract over joined records.
- Bidirectionality (3): analysis of synthesis is the
  identity on contracts; synthesis of analysis is
  qualification-equivalent to the system; and the
  reengineering round trip — analyze, synthesize,
  re-analyze — returns the contract.
- Independent derivability (1): the direct and chunked
  derivation routes agree whenever the chunks
  concatenate to the whole record.
- Smallness (5): the description bound (a contract's
  description is at most the record length plus the
  step count); the power bound and the vanishing
  result (any bound is vanishing against the power of
  two of the description); and smallness preserved
  under contract joins, with descriptions adding.
- Speculation (2): a speculative result is valid
  exactly while its premise cone is contained in the
  system's facts, and validity survives joins.
- Bounds (17): the fold bounds — minimum and maximum
  over a candidate list bound every member, are
  attained by members, and exist on any nonempty list,
  in both the fold and the value forms; every member
  of a candidate list lies inside the bounds and both
  bounds are attained; bounds over a join are the
  parts' minimum and maximum, in both forms; the best
  and the gap to any floor tighten monotonically under
  joins; and a best that meets a certified floor is a
  certified optimum.
- Finiteness and decidability (2 theorems beside the
  decision definition): the candidate grid's length is
  the computed product of the contract's two list
  lengths, and the candidate space is finite. The
  optimum question over the grid is decidable — stated
  as a definition in the core file and assembled into
  the joined theorem as the decided disjunction.
- The measures (9): semantic mass is conserved and
  monotone and joins additively; velocity is exactly
  mass change along a growing path, by the telescoping
  result and the last-step result; the one-step
  redundancy test is sound; and ordering optimality is
  the absence of adjacent descents, over the empty,
  single, and general cases.
- The suboptimality trio (3, in their own namespace):
  scheduling suboptimality is exactly the idle sum;
  venue suboptimality is the exact excess over the best
  candidate; test set suboptimality vanishes exactly at
  equal mass under containment.

### The composition — 17 theorems in the synthesis file

- The losses core, mirrored and discharged over
  definitions identical to its home's (14): the sum
  split over a join; additive recording; compositional
  projection; the gap split; gap freeness; composition;
  loss-free parts with a loss-free interaction
  composing to a loss-free whole; compounding;
  tightness at the no-surplus point; monotonicity;
  localization of every loss to a gap at a named site;
  finiteness of the contract space; and soundness of
  the axis checks, singly and over all axes.
- Discharged in this vocabulary (2): the persistence
  elimination result — adjoining derivable facts leaves
  the derivable set unchanged — proved over this
  model's derivability; and the recorded-state
  join-semilattice, which discharges for exactly that
  class the general join-semilattice premise the
  compilers repo carries as a label. No wider discharge
  is claimed: graph-shaped states in general are not
  recorded fact lists.
- The joined theorem (1): the whole method assembled
  for an arbitrary system under an arbitrary
  qualification, from this repo's theorems, the
  mirrored losses core, the two discharged results,
  and the family's restated hypotheses under the named
  premises below.

### Controls — 4 theorems in the controls file

Four standing controls, each a proved negation over a
concrete counterexample: smallness can fail; the two
derivation routes disagree on an incomplete recording;
a join inside the bounds tightens nothing; and the
content bound fails without injectivity. The first two
are axiom-free; the second two rest on the standard
pair.

## On named premises

The joined theorem carries six named premises, which
bind applicability and which no conjunct proof uses:
contract fidelity (the premise the empirical arm
tests), record fidelity and re-measure (carried from
the losses home), coverage (from the quantifiable
home), the spec authority premise (from the safe
home), and witness faithfulness (from the profiling
home). Its remaining inputs are restated hypotheses,
proved in their home repos at the pins the repo's
specification names: minimum existence over a nonempty
candidate list and frontier completeness, certificate
soundness and monotonicity (the persistence home);
baseline-free measurement and incremental equals full
(the profiling home); admission composition under the
interaction-closed side condition (the composable
home); checker soundness and cone exactness (the safe
home); fold exactness under retraction (the
traceability home); quotient recovery by carrying (the
compilers home); and bounds soundness and attainment
for the general measure interface (the optimality
home, whose list instance is proved natively here).

## Absent and proposed, at the repo's own states

- Proposed, not proved: the content bound under
  injectivity of the content map (the unconditional
  form is refuted, by the fourth control); the
  profiling visibility vector and time-varying
  re-solving; weighted and continuous axes and richer
  derivations in the losses mirror.
- The gap register stands in the specification at ten
  owned gaps, each with its closing route: the corpus
  minimum and its floor, with the witness-status
  ruling, the candidate completeness check, and the
  premise falsification runs it depends on; the
  visibility vector; one sibling gate log; contract
  fidelity as a standing premise discharged only
  empirically; unmeasured census subjects; the losses
  generality pass; and citation pin drift in two family
  repos.
- The empirical census arm is campaign evidence, never
  a theorem: its first tranche stands in the repo's
  census file — executed runs of the model's machinery
  over the three landed sibling inventories (losses,
  persistence, profiling, at their pins), round trips
  passing and bounds attained at both ends — and its
  subject rows for the library and the family stand
  unmeasured with their blocking steps named. One
  record note: the census file's own row for this repo
  still reads empty, as the file was written before the
  landing it shipped in; the proof content above is
  what this census records.

## Gate state

The check script stands in the proof folder in the
family gate form: an escape scan over every Lean file,
compilation with warnings as errors, and an axiom
audit. The recorded check log at the pin ends in its
axiom subset check passing, with the printed axioms
exactly propositional extensionality and quotient
soundness and no classical choice anywhere. This watch
ran no build; the gate state stands on the recorded
log.

## Placement

Placed in the synthesis at section 3.14, at this pin.
Its specification's provenance table cites the family
at named pins, among them this synthesis repo at its
then head; those citations are the repo's own record
and are carried here as stated.
