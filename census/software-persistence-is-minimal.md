# Census — software-persistence-is-minimal

## Pin and identity

- Census pin and live head (read in the twenty-second
  enumeration, 2026-11-19):
  eb01cf2e33a20bfbda5a03aba7a48c70fbd10741
- Visibility: public. Default branch: main.
- Description (the repo's own): none recorded in the
  listing.
- Created in this window: the repo is new since the
  twenty-first enumeration; three commits stand at the
  head — the proved core with its controls, the spec and
  definitions and readme, and the family synthesis.
- Toolchain: Lean 4.19.0, pinned in the proof folder's
  toolchain file. No Mathlib; the development is three
  Lean files in one proof folder, beside a check script,
  a recorded check log, and the toolchain file, with a
  readme, a spec file, and a definitions file at the
  root — nine files in the tree.
- Determination: proof-bearing by content — Lean sources
  and a recorded gate log stand in the tree, found by
  the content check on its first enumeration, not by
  its name.

## Thesis, in plain English

Persistent data admits a minimum representation, and
redundant computation over it is provable. A persistent
state is a store of facts and a list of recorded edges;
a fact is derivable when the edges produce it from the
store. A computation whose conclusion is already
derivable is redundant, and a certificate — the recorded
edges used, in order — proves it, checkably. A datum's
representations form a finite candidate space over the
qualification contract's alphabet, priced per axis; a
minimum is a candidate no other candidate dominates,
checked independently of its production and produced by
a fold when none is claimed. Versions are carried
semi-persistently: a version is readable exactly while
every part of it stays derivable, so nothing is dropped
while a live version reads through it. The model was
directed by Chris on 2026-11-19; the repo's spec file
states it in full, with its executable ten step method,
its falsification protocols, and its measures, and its
definitions file states every term at implementer
resolution.

## Theorem census — 53 declarations in three Lean files

Counted by the watch method in this census: every
theorem declaration in every Lean file at the pin. No
admitted-proof token stands in any file, by this
census's own scan (the one English word the scan first
surfaced is a prose word inside a comment in the
synthesis file, not a proof token). Axiom states are
from the repo's recorded check log, which prints 52 of
the 53 declarations; the one unprinted declaration is
the sum append helper in the synthesis file, marked as
such below.

### The core file — 26 declarations

Derivability and elimination:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| step closure | A recorded edge whose premises are all derivable has a derivable conclusion. | none |
| monotone in the store | Derivability is monotone in the stored facts: a derivation from a store holds in any larger store. | none |
| monotone in the edges | Derivability is monotone in the recorded edges: a derivation holds under any larger edge list. | none |
| elimination | Adjoining an already derivable fact to the store changes the derivable set not at all, in both directions. | propositional extensionality only |

Certificates:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| run soundness | A successful certificate run leaves only derivable facts in its final store. | the standard pair |
| run monotonicity | A successful run stays successful under a larger store, and its final store only grows. | the standard pair |
| certificate soundness | A certificate the checker accepts witnesses a genuine derivation of the target. | the standard pair |
| certificate monotonicity | A checked certificate stays checked as the recorded edges and the store grow. | the standard pair |
| certificate composition, run level | A successful first run composes with a second run started from its final store. | the standard pair |
| certificate composition, checker level | The same composition at the checker level: a checked second certificate extends to a checked composed certificate. | the standard pair |

Representations and minima:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| constant sum | The sum of a constant list is its length times the constant. | propositional extensionality only |
| constant sum, function form | The sum of a function that is constant on a list of lists is the length times the constant. | propositional extensionality only |
| finiteness | The candidate count is the alphabet size raised to the datum length — a computed power, finiteness derived from the contract. | propositional extensionality only |
| cost additivity | Cost is additive over append of data and representations, under segment length agreement. | none |
| domination bridge | The boolean domination check decides the domination proposition, in both directions. | the standard pair |
| minimality checker soundness | A candidate the minimality checker accepts is a minimum: it is a candidate and no candidate dominates it. | the standard pair |
| domination irreflexive | No representation dominates itself. | none |
| domination transitive | Domination is transitive, with strict-axis propagation through the middle candidate. | none |
| choice fold invariant | The fold invariant of the choice procedure: the result is the seed or a list member, no listed candidate dominates it except through the seed, and domination of the result propagates to the seed. | the standard pair |
| choice is minimum | The choice procedure's output is a member of any nonempty candidate list and is minimum there. | the standard pair |
| minimum exists | Every nonempty candidate list carries a minimum. | the standard pair |
| domination lifts | Domination of one segment lifts to the whole datum with the remaining segments held fixed, under length agreements. | propositional extensionality only |
| whole minimum has minimum parts | A minimum of the whole has minimum parts: no candidate for one segment dominates its segment when the rest is held fixed. | propositional extensionality only |

Semi-persistence:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| readability monotone | Readability of a version is monotone in the store. | none |
| version cost splits | The total version cost splits at the head of the version list. | none |
| kept premise | With the shared premise stored, the version deriving through the recorded edge stays readable — the concrete kept-premise instance. | propositional extensionality only |

### The controls file — 5 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| no derivation | From a single recorded edge whose premise list reaches outside the empty store, nothing at all is derivable from the empty store — the general fact the second control instantiates. | propositional extensionality only |
| first control | Axis relativity: a representation that is minimum on a restricted axis list is not minimum on the full list — minimality is relative to the named axes. | the standard pair |
| second control | An edge whose premise is outside the closure does not make its conclusion derivable: the concrete conclusion is not derivable from its single edge over the empty store. | the standard pair |
| third control | Naive per-version compression that drops the shared premise loses a still-readable version; keeping the premise restores its readability. | the standard pair |
| fourth control | A cross-part tradeoff dominates the append of part minima in the composed datum: part minima, each minimum on its own part, need not compose — the interaction must be recorded to be visible. | the standard pair |

### The synthesis file — 22 declarations

The family synthesis, assembled over this development's
own definitions. The losses core is mirrored and
discharged (the source's statements verbatim over
identical definitions, the proofs this development's
own); the profiling baseline and solved results and the
traceability fold results are likewise proved here; the
remaining family results enter the joined theorem as
restated hypotheses or named premises, recorded under
its own heading below.

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| sum append helper | The sum of an append of two lists of naturals is the sum of the two sums — the arithmetic fact the additive laws rest on. | not printed |
| additive | The derived contract level of a composition is the sum of the derived levels of its parts. | propositional extensionality only |
| projected | Projecting a composition onto an axis equals the sum of the projections of its parts, per axis. | propositional extensionality only |
| split | The three way form: a whole of two parts and their interaction projects to the sum of the three projections. | propositional extensionality only |
| gap reading | Gap zero and loss freeness are the same fact on every axis and every record. | propositional extensionality only |
| composed | Two parts loss free against their shares compose to a whole loss free against the sum of the shares. | propositional extensionality only |
| whole free | The structural fix theorem, three way form: both components and the recorded interaction loss free against their shares give the composition loss free against the sum of the shares. | propositional extensionality only |
| term bound helper | Any natural is at most its truncated difference from another plus that other — the arithmetic fact the compounding proof rests on. | propositional extensionality only |
| three way subadditivity | The shortfall of a sum of three required levels is at most the sum of the three shortfalls. | the standard pair |
| compound | The gap of a composition is at most the sum of the component gaps and the interaction gap, when the required level of the whole is the sum of the shares. | the standard pair |
| localizes | If a composition falls short of the sum of the shares, then some component falls short of its share, or the recorded interaction does — no fourth place for a loss to hide. | propositional extensionality only |
| sound | A passing per axis check verdict implies loss freeness in the model. | none |
| all sound | A passing full verdict over a finite list of axes implies loss freeness on every axis in the list. | the standard pair |
| grid length helper | The grid of two lists has length equal to the product of the two list lengths. | propositional extensionality only |
| space finite | The problem space of a qualification contract has size equal to the product of the sizes of its two finite discrete sets — finiteness derived from the contract, never assumed. | propositional extensionality only |
| gap zero under full check | Under a passing full verdict, every axis in the list has gap zero against the record. | the standard pair |
| baseline independence | The constructed measured form is a function of the overlap and the witnesses alone, invariant under any choice of external baseline — the profiling result, proved here by computation. | none |
| least cost exists | Every nonempty finite list has a least-cost member under any cost assignment — the profiling solved content in this development's vocabulary. | propositional extensionality only |
| fold membership | A value is in the traceability fold of a node list exactly when it is in some node's contribution. | the standard pair |
| retraction commutes | Filtering the node list before the fold keeps exactly the kept nodes' contributions — retraction commutes with the fold. | the standard pair |
| only carrying recovers | An artifact map that identifies two quotient-distinct programs admits no recovery of the quotient — recovery is possible only for derivation-carrying representations. | none |
| joined | The joined theorem assembling the method, stated in full under its own heading below. | the standard pair |

The joined theorem: given the five named premises as an
antecedent (below) and the restated hypotheses — frontier
completeness and bounds soundness with attainment from
the optimality development, incremental accounting equal
to full accounting, re-check equal to full check and
safety checker soundness from the safe development,
admission composition from the composable development,
and quotient recovery by carrying from the compilers
development — it concludes, in order: freedom of the
record on every checked axis; sound redundancy
elimination with the derivable set unchanged; existence
of a minimum representation; frontier completeness over
the candidate space; independent checkability of the
minimality verdict; readability of every version under
any growth of the store; baseline-free measurement;
incremental accounting equal to full accounting, for
measurement and for re-checking alike; derived bounds on
the workload list attained by its members; admission of
the composed record; safety from the safety checker's
acceptance; quotient recovery by carrying
representations; and the candidate count as a computed
power.

## Controls and gate evidence

- Four adversarial controls stand in the controls file,
  each a proved negation over concrete numbers, proving
  by execution that the condition it weakens is load
  bearing: the axis list, the recorded premise, the
  shared premise, and the recorded interaction. The
  general no-derivation result stands beside them as
  the lemma the second control instantiates.
- Gate: the check script in the proof folder compiles
  every Lean file in the tree with warnings as errors,
  rejects every proof escape token, prints axiom
  dependencies per theorem, and fails if any printed
  axiom lies outside the standard set. The recorded
  check log in the tree ends in its axiom subset check
  passing, with the 52 printed declarations' axioms all
  within the standard set: 11 printed theorems depend
  on no axioms, 19 on propositional extensionality
  only, and 22 on the standard pair; no printed theorem
  uses the choice axiom, and the log's own footer records
  the printed axioms as exactly the extensionality and
  quotient soundness pair. Gate state at the pin: green
  on the recorded log; this census ran no build of its
  own.

## Premises carried rather than proven

Campaign premises, named in the repo's spec, outside
the Lean development:

- Edge faithfulness: an edge recorded in the persistent
  list is faithful to a real derivation — the system
  actually produced the conclusion from those premises.
  The development proves everything from the recorded
  list; it cannot prove the list honest.
- Cost fidelity: a campaign's cost assignment tracks
  real costs — real bytes, real time, real retrieval
  effort. Optimality is proven relative to the axes
  named; which axes track reality is the campaign's
  evidence.

Named premises inside the joined theorem's antecedent,
each labeled a premise by its own source, uninterpreted
in the development: coverage (from the quantifiable
development), spec authority (from the safe
development), the general join-semilattice claim (from
the compilers development, proven there only for the
hypergraph instance), witness faithfulness (from the
profiling development), and record fidelity (from the
losses development).

## Absent and proposed, at the repo's own states

- Candidate completeness: the claim that a real
  campaign's representations are exhausted by the
  candidate space over its contract alphabet is
  proposed semantics, with its falsification run stated
  in the spec.
- The end-to-end methodology: the claim that the ten
  steps, run on a real corpus, eliminate exactly the
  redundant computations and reach a minimum
  representation of the whole stands proposed; its
  checker-produced form is the falsification protocol's
  run, and stands open.
- Inherited open items, named in the repo's synthesis
  record: the profiling development's visibility vector
  is proposed and open there, and re-solving as costs
  vary over time is open there; the joined method
  inherits both as open.
- One bounded application stands in the spec as an
  executed measurement, not a theorem: over the restart
  records corpus measured on 2026-11-19, the current
  representation is not minimum on the stored-size axis
  (an exhibited dictionary and columnar encoding stands
  strictly under it), and the full Pareto verdict over
  the qualification contract is unmeasured — no
  access-cost contract for the store has been fixed, and
  that is the named blocking step.

State: PROVEN at the pin for the 53 declarations above,
on the recorded gate log, with the two campaign
premises, the five named premises and the restated
hypotheses of the joined theorem, and the proposed
items carried at exactly the states the repo itself
states.
