# Census — software-profiling-is-synthesizable

## Pin and identity

- Census pin and live head (read in the sixteenth
  enumeration, 2026-11-18): a53c4bf5aa83e8677ecb66571d61ed4c11e2d88d
- Visibility: public. Default branch: master.
- Description (the repo's own): the measurement proof model
  for software profiling — no baseline, incrementally
  provable, witness compounding, venue and ordering solved
  for.
- Created in this window: the repo is new since the fifteenth
  enumeration; two commits stand at the head — the first
  landing (the model, its spec and plan, and the proven core)
  and a completion pass (a definitions file, six further
  theorems, and the dependence control).
- Toolchain: Lean 4.19.0, pinned in the proof folder's
  toolchain file. No Mathlib; the development is three Lean
  files in one proof folder, beside a check script, a recorded
  check log, a readme, a spec file, and a definitions file.
- Determination: proof-bearing by content — Lean sources and
  a recorded gate log stand in the tree, found by the content
  check on its first enumeration, not by its name.

## Thesis, in plain English

Software profiling is synthesizable: an incrementally
provable proof system in which constructed runtime measures
are established from a vanishingly small set of certified
witness states, with no baseline for any execution, and in
which venue and ordering are discrete, finite, and solved
for under the qualification contract at play. Redundant
compute, suboptimal ordering, and suboptimal venue use are
eliminable inside the system, with economic calculation and
measurement over time, and a visibility vector over the
measured software. The model was dictated by Chris on the
voice call of 2026-11-18; the repo's spec file states it in
full, with its plan, and its definitions file states every
term at implementer resolution.

## Theorem census — 20 declarations in three Lean files

Counted by the watch method in this census: every theorem
declaration in every Lean file at the pin. No admitted-proof
token and no custom axiom declaration stands in any file, by
this census's own scan. Axiom states are from the repo's
recorded check log, which prints 19 of the 20 declarations;
the one unprinted declaration is the grid length helper in
the main file, marked as such below.

### The main file — 11 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| baseline | Any two external baselines give the same constructed measure, the value being a function of the overlap and the certified witnesses alone. | none |
| grid length (helper) | The grid of a venue list and an ordering list has length equal to the product of the two list lengths. | not printed |
| finiteness | A contract's configuration count is the product of its venue count and its ordering count — finiteness derived from the contract, never assumed. | propositional extensionality only |
| compounding | The assignments of truth values to a given number of witness positions number exactly two to that power. | the standard pair |
| distinctness | Those assignments are pairwise distinct, so the compounding count counts distinct constructed measures. | the standard pair |
| incremental | Accounting a sequence of effects in two stages, carrying the state across the seam, equals accounting the whole sequence from the start. | none |
| idempotence | An idempotent effect applied twice in a row contributes exactly what it contributes once, at any position the fold has reached. | none |
| elimination | A step inert on every state may be removed at any position in a sequence, and every accounted measure is preserved. | none |
| optimum | Any nonempty finite list of costs has a least element. | propositional extensionality only |
| solved | A contract with a nonempty configuration set has a least-cost configuration under any cost assignment. | the standard pair |
| falsification | A falsifying witness in the certified set kills the standing of the measure. | none |

### The completion file — 7 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| complete | Every truth assignment of the given length occurs among the assignments of that many witness positions — combinatorial sufficiency. | the standard pair |
| free | Any value at a witness position, with any assignment of the remaining positions, is a combined state — independence at one coordinate. | the standard pair |
| carried | Standing under a certified set implies standing under any subset of it, so verdicts are carried, not recomputed. | none |
| relabeled | A comparison of two measured values is unchanged under any strictly increasing relabeling — no absolute origin enters a verdict. | the standard pair |
| parametric | The order of two configurations flips between two cost assignments, so a verdict exists only relative to the contract at play. | none |
| swap | Two sequential effects that commute may be exchanged in the sequence, and the accounting is unchanged. | none |
| third control | A locked family of two witness positions forced to agree has two combined states, fewer than the compounded count of four, and every state in it has its two positions equal — dependence collapses the count. | the standard pair |

### The controls file — 2 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| first control | A baseline-dependent variant of the measure provably fails baseline independence: two baselines give two values at the same overlap and witnesses. | propositional extensionality only |
| second control | A non-idempotent effect provably fails reapplication invariance: the successor effect applied twice accounts a different value than applied once. | none |

## Controls and gate evidence

- Three adversarial controls stand in the tree (the first
  and second in their own file, the third in the completion
  file), each proving by a concrete counterexample that the
  condition it weakens is load bearing: baseline dependence,
  non-idempotence, and witness dependence respectively.
- Gate: the check script in the proof folder compiles every
  Lean file with warnings as errors, rejects every proof
  escape token, prints axiom dependencies per theorem, and
  fails if any printed axiom lies outside the standard set.
  The recorded check log in the tree ends in its axiom subset
  check passing, with only propositional extensionality and
  quotient soundness printed across the 19 printed theorems:
  9 printed theorems depend on no axioms, 3 on propositional
  extensionality only, and 7 on the standard pair. Gate state
  at the pin: green on the recorded log; this census ran no
  build of its own.

## Premises carried rather than proven

- One premise, labeled in the repo's spec as a rule of the
  model: facts about a runtime or a job enter the system only
  as certified witness states. The Lean development carries
  no premise of its own; every theorem above is proved from
  the definitions in its files.

## Absent and proposed, at the repo's own states

- The bridge that reads a concrete profiling campaign's run
  facts as certified witness states: proposed semantics in
  the spec, discharged per campaign; the independence of a
  given campaign's witness facts is that campaign's evidence
  to bring.
- The visibility vector — the projection of the certified
  state each stakeholder class sees: proposed, with no
  formalization yet; the spec records the obstruction (no
  projection form chosen that is provably a function of the
  certified state alone).
- Economic calculation over time: proven at one cost
  assignment (the optimum and solved theorems); re-solving
  over a sequence of cost assignments with carried verdicts
  is not yet formalized and stands open in the spec.

State: PROVEN at the pin for the 20 declarations above, on
the recorded gate log, with the one premise, the two proposed
items, and the open items carried at exactly the states the
repo itself states.
