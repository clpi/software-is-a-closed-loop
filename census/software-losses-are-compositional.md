# Census — software-losses-are-compositional

## Pin and identity

- Census pin and live head (read in the twenty-first
  enumeration, 2026-11-19):
  d1159dc1e183061323afff362bca6234e34f7766
- Visibility: public. Default branch: main.
- Description (the repo's own): none recorded in the
  listing.
- Created in this window: the repo is new since the
  twentieth enumeration; one commit stands at the head —
  the landing itself (the model, its spec and
  definitions, and the proven core with its controls).
- Toolchain: Lean 4.19.0, pinned in the proof folder's
  toolchain file. No Mathlib; the development is two Lean
  files in one proof folder, beside a check script, a
  recorded check log, and the toolchain file, with a
  readme, a spec file, and a definitions file at the
  root — eight files in the tree.
- Determination: proof-bearing by content — Lean sources
  and a recorded gate log stand in the tree, found by
  the content check on its first enumeration, not by
  its name.

## Thesis, in plain English

Losses are compositional, and a loss is fixed
structurally, at its site. A system's contract is
derived from its recorded behavior; recording is
additive, so the record of a composition is the append
of the records of its parts. Contracts compose with
systems, and the composed contract projects onto
quantifiable solvable axes of capability, design, and
performance. A gap is a shortfall on an axis, and a
loss is a witnessed gap against a named rival. Gaps
compose compoundingly from component gaps and recorded
interaction gaps; loss freeness is compositional under
the same condition; and every loss in a whole localizes
to a gap at a named contract or composition site, so a
loss is fixed at its site, not at the instance that
witnessed it. The model was directed by Chris on
2026-11-19; the repo's spec file states it in full,
with its executable eight step method and its measures,
and its definitions file states every term at
implementer resolution.

## Theorem census — 17 declarations in two Lean files

Counted by the watch method in this census: every
theorem declaration in every Lean file at the pin. No
admitted-proof token stands in either file, by this
census's own scan. Axiom states are from the repo's
recorded check log, which prints 15 of the 17
declarations; the two unprinted declarations are the
helper results in the main file, marked as such below.

### The main file — 14 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| sum helper | The sum of an append of two lists of naturals is the sum of the two sums — the one arithmetic fact the additive laws rest on. | not printed |
| additive | The derived contract level of a composition is the sum of the derived levels of its parts: recording a whole records exactly what recording its parts records. | propositional extensionality only |
| projected | Projecting a composition onto an axis equals the sum of the projections of its parts, per axis. | propositional extensionality only |
| split | The three way form: a whole made of two parts and the interaction between them projects to the sum of the three projections. | propositional extensionality only |
| gap reading | Gap zero and loss freeness are the same fact on every axis and every record. | the standard set |
| composed | Two parts that are loss free against their shares compose to a whole that is loss free against the sum of the shares. | the standard pair |
| whole free | The structural fix theorem, three way form: both components loss free against their shares and the interaction recorded and loss free against its share give the composition loss free against the sum of the shares. | the standard pair |
| compound | The gap of a composition is at most the sum of the component gaps and the interaction gap, when the required level of the whole is the sum of the shares. | the standard pair |
| monotone | Enlarging any one component's projection, the rest held fixed, never enlarges the gap of the whole. | the standard pair |
| localizes | If a composition falls short of the sum of the shares, then some component falls short of its share, or the recorded interaction does — there is no fourth place for a loss to hide. | the standard pair |
| grid helper | The grid of a capability list and a design list has length equal to the product of the two list lengths. | not printed |
| finite | The problem space of a qualification contract has size equal to the product of the sizes of its two finite discrete sets — finiteness derived from the contract's definition, never assumed. | propositional extensionality only |
| sound | A passing per axis check verdict implies loss freeness in the model. | none |
| all sound | A passing full verdict over a finite list of axes implies loss freeness on every axis in the list. | the standard pair |

The repo's own proven list names twelve of these: the
ten results above from additive through finite, with
the soundness result counted as its per axis and all
axes forms. The two helpers stand outside that list and
carry the additive and finiteness results respectively.

### The controls file — 3 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| first control | An unrecorded interaction breaks the compositionality of the gap: the composition read without the interaction projects to two on the identity axis, and read with it, to seven — the two readings differ. | none |
| second control | A non additive recording, one that collapses duplicate entries before the contract is derived, breaks the projection law: the projection of the collapsed composition reads one, while the sum of the projections of the parts reads two. | the standard pair |
| third control | Component wise loss freeness does not save a composition whose interaction is unrecorded: each component meets its share of one, yet the recorded whole projects to two against a required level of seven, the sum of the two shares and the interaction share of five — the whole loses, at exactly the unrecorded interaction site. | none |

## Controls and gate evidence

- Three adversarial controls stand in the tree, each a
  proved negation over a concrete counterexample,
  proving by execution that the condition it weakens is
  load bearing: a recorded interaction, additive
  recording, and the recorded interaction again, read
  from the loss side.
- Gate: the check script in the proof folder compiles
  every Lean file in the tree with warnings as errors,
  rejects every proof escape token, prints axiom
  dependencies per theorem, and fails if any printed
  axiom lies outside the standard set. The recorded
  check log in the tree ends in its axiom subset check
  passing, with the fifteen printed declarations' axioms
  all within the standard set: 3 printed theorems depend
  on no axioms, 4 on propositional extensionality only,
  7 on the standard pair, and 1 on the full standard
  set. Gate state at the pin: green on the recorded log;
  this census ran no build of its own.

## Premises carried rather than proven

Named in the repo's spec as premises, never claimed as
theorems:

- Record fidelity: that a concrete campaign's records
  capture the behavior of a real system is the
  campaign's evidence, established by the campaign's own
  execution.
- Re-measure: the model flips no beat cell; a cell flips
  only on a same-contract re-measure at a current pin,
  executed against the real rival and the real system.

The Lean development carries no premise of its own;
every theorem above is proved from the definitions in
its files.

## Absent and proposed, at the repo's own states

- Richer derivations: the model uses the sum derivation;
  any derivation respecting append inherits every law
  here, and a general derivation interface is proposed,
  not formalized.
- Weighted axes: an axis whose per entry measure depends
  on position or on the qualification contract is
  proposed; the parametric form is not formalized.
- Continuous axes: axes valued in ordered structures
  beyond the naturals are proposed, not formalized.

State: PROVEN at the pin for the 17 declarations above,
on the recorded gate log, with the two named premises,
the three proposed items carried at exactly the states
the repo itself states.
