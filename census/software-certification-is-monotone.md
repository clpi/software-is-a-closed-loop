# Census — software-certification-is-monotone

## Pin and identity

- Census pin and live head (read in the thirty-sixth
  enumeration, 2026-11-19):
  4539760e0589fdcb3327d7b6ded90bb71af3a808
- Visibility: public. Default branch: main.
- Description (the repo's own): monotonic certification
  pipeline: certificates between two states over semantic
  dimensions, from incremental evidence that provably
  covers the full check.
- Created in this window: the repo is new since the
  thirty-fifth enumeration; one commit stands at the
  head, carrying the whole development.
- Toolchain: Lean 4.19.0, pinned in the toolchain file.
  No Mathlib; the development is three Lean files beside
  an axiom audit file and a lakefile, with a check
  script, a specification, a readme, and the first
  certificate artifact with its own checker and its
  recorded checker output — thirteen files in the tree.
- Determination: proof-bearing by content — Lean sources
  stand in the tree, found by the content check on its
  first enumeration, not by its name.

## Thesis, in plain English

A subject is certified over a fixed set of dimensions.
Evidence for a transition between two states is a chain
of recorded increments, each step carrying the recorded
outcome of its incremental check. A certificate is a
single checkable artifact between the two states: its
checker requires chain evidence behind every certified
verdict, and it recomputes the endpoint values, so a
dimension whose value regressed can carry no verdict but
regressed in an accepted certificate. Chain evidence
proves the endpoint comparison, and chains compose, so
incremental evidence provably covers the full check at
transition grain and at chain grain — the pipeline is
the monotonicity half of the closed loop's stage three
witnessing, stated as a general construction over any
qualified subject. Its first subject is the perception
harness repo, which is its first subject, not its home.
The specification composes with the standing release
monotonicity living spec (its certificate form,
projection rule, baseline read, and cone-carried
verdicts are reused, with the pipeline's additions
flagged as extensions) and cites the frontier repo's
search results by name where the dimension definitions
use them, re-proving none of them.

## Theorem census — 19 declarations in two Lean files

Counted by the watch method in this census: every
theorem declaration in every Lean file at the pin. No
admitted-proof token stands in any file, by this
census's own scan. Axiom states are as the repo's own
specification and readme record them at the landing pin,
from the axiom audit file's prints: the two chain
results depend on no axioms; the checker results and
the assembled control depend on propositional
extensionality and quotient soundness only. No recorded
build log file stands in the tree, so a passing gate at
this pin rests on the specification's recorded cold pass
statement, carried at that strength.

### The core file — 9 declarations

The dimension set and its membership fact:

| Token | Hypotheses to conclusion | Axioms (repo record) |
|---|---|---|
| dimensions membership | Every dimension of the fixed seven dimension set is a member of the set's list. | not printed |

Chain evidence:

| Token | Hypotheses to conclusion | Axioms (repo record) |
|---|---|---|
| chain sound | A chain of recorded increments between two states proves the later value is at least the earlier value on its dimension: the incremental covers full property at transition grain. | none |
| chain join | Chain evidence over consecutive increments composes to chain evidence over their join: the property at chain grain. | none |

The certificate checker:

| Token | Hypotheses to conclusion | Axioms (repo record) |
|---|---|---|
| check clause | In an accepted certificate, every dimension's checker clause holds. | not printed |
| check sound | If the checker accepts a certificate and a dimension's verdict certifies, that dimension's value at the later state is at least its value at the earlier state, through the chain evidence the checker required. | the standard pair |
| check honest | In an accepted certificate, a dimension whose value regressed carries the regressed verdict and no other. | the standard pair |
| check not certified | Corollary: a regressed dimension's verdict does not certify in an accepted certificate. | the standard pair |
| check chain | Two accepted certificates over consecutive increments, each certifying a dimension, certify that dimension between the outer endpoints. | the standard pair |
| certified sound | A certificate under the overall certified reading is sound on every dimension. | the standard pair |

### The control file — 10 declarations

The standing control subject: the successor increment
relation, and readings that fall at the middle state of
a three state transition and recover at the end state.

| Token | Hypotheses to conclusion | Axioms (repo record) |
|---|---|---|
| bad zero | The control reading at the start state is ten. | not printed |
| bad one | The control reading at the middle state is zero. | not printed |
| bad two | The control reading at the end state is ten. | not printed |
| interior | The middle state is worse than the start state: the interior regression. | not printed |
| endpoint | The endpoint comparison passes: the end value is at least the start value. | not printed |
| cut | A chain between two states under the successor relation cuts at every state between them. | not printed |
| no chain | No chain evidence covers the control transition: a cut at the middle state would contradict the interior regression by chain soundness. | not printed |
| naive accepts | The endpoint-only checker accepts the control transition. | not printed |
| rejected | The pipeline's checker rejects the matching claim, which carries a certifying verdict and no evidence. | not printed |
| control | The assembled control: the endpoint-only checker accepts, the interior regresses, no chain evidence exists, and the pipeline's checker rejects. Endpoint-only comparison is refuted as a certification method. | the standard pair |

## The first certificate

The tree carries the pipeline's first issuance, for the
perception harness repo between its 2026-11-06 baseline
pin and the head the previous enumeration recorded. Its
overall reading is not certified, recomputed and printed
consistent by the artifact's own checker, whose recorded
output stands in the tree: no dimension regressed;
coverage, fidelity, and reconversibility improve, each
with its coverage discharge stated on the artifact;
setup is flat; solvability, reweightability, and speed
are unmeasured, each with its gap and closing route
named on the artifact. The artifact is executed
evidence at its own strength, not a theorem, and is
counted nowhere in the proven column.

## Premises carried rather than proven

The specification names four premises about the world,
each with its falsification route:

1. The measure is a function of state: a dimension's
   value is a function from states to readings.
2. The increment relation is the subject's recorded
   history: a chain in the model is a chain in the
   history, and a missing step makes coverage
   unprovable, never silently true.
3. A step's recorded outcome is an executed check: the
   premise binds the producer outside the model; a
   false step cannot be constructed inside it.
4. Orientation: every dimension's value is oriented
   larger is better, by its measure rule.

## Gate state

The check script stands in the tree: it rejects proof
escape tokens, builds under warnings as errors with the
axiom audit printed, and runs the certificate checker
over the first certificate. The specification records a
family gate cold pass at the landing pin; no build log
file stands in the tree, so the gate verdict at this
pin is carried at the specification's recorded strength,
not as a log witnessed in this census. This census ran
no build of its own.
