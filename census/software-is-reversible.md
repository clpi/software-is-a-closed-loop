# Census — software-is-reversible

## Pin and identity

- Census pin and live head (read in the forty-sixth
  enumeration, 2026-11-20):
  984f1faf3d0f74116a4b38b550b11e7c56237faa
- Visibility: public. Default branch: master.
- Description (the repo's own): the reversible search
  space — theorem completion, guided candidate search
  over the one append-only hypergraph, recursive
  algorithms, and empirical reversibility validation of
  actions all the way backwards.
- Created in this window: the repo is new since the
  forty-fifth enumeration; its tree stands at forty-six
  files — two Lean developments, a program spec, the
  repo's own theorem census, the search space and
  recursive algorithm documents, the reversibility
  validation system with its executed first pass
  records, and the supporting harnesses.
- Toolchain: Lean 4.19.0, pinned in both toolchain
  files. No Mathlib; the developments import only the
  standard distribution.
- Determination: proof-bearing by content — Lean
  sources, check scripts, and a recorded axiom audit
  stand in the tree, found by the content check on its
  first enumeration, not by its name.
- Foundations, as the repo itself cites them: the
  canonical model home at its pin 37514fb7, the
  candidate space home at its pin 60f33193, and the
  pipeline proof lane's module at a local scratch pin —
  the pipeline module that citation names stands pushed
  in the candidate space home in this same window, at
  the fresh head recorded in that repo's annex delta in
  this pass.

## Thesis, in plain English

A search and action system built on the one append-only
hypergraph can be run backwards as well as forwards,
and the repo proves the model layer of that claim. A
plan on the Pareto frontier need not be selectable by
any positive weighting — the middle plan of the three
plan example is undominated and never selected, at two
scales. Reuse pays only when the avoided work exceeds
setup, validation, persistence, and restart combined.
The closure worklist's missing count is exact: zero
exactly when every premise is derived, bounded by the
premise count, positive while a named premise is
absent, and antitone as the derived set grows.
Appending one candidate updates the frontier exactly,
and retracting a fresh insert restores the prior
frontier at every other point. An action carried as a
structural map with a checked inverse restores its
starting state, and compositions restore in turn; an
action carried as the empty option has no restoration
claim at all. A threshold stop supports an
acceptability claim only, never an optimality claim —
the threshold control proves the first acceptable plan
can be the worse one — while a plan certified against
the whole remaining set is no worse than every plan in
it. And, in the scoped development, exact
reconstruction over a finite domain exists precisely
under injectivity: collisions are impossible under an
inverse, composed maps invert by composition, a
residual-carrying form inverts where a plain inverse
cannot, and the size of a fiber bounds what any
reconstruction must retain.

## Theorem census — 55 declarations in three Lean files

Counted by the watch method in this census: every
theorem or lemma declaration in every Lean file at the
pin, comments stripped. No escape token — no admitted
proof, no axiom declaration, no native evaluation
token — stands in any of the three files, by this
census's own scan.

### The root development — 38 declarations in one file

- Frontier before weights (6): the middle plan is not
  dominated by either rival or by itself; it stands on
  the frontier of the three plans; and no pair of
  positive weights ever selects it, at the first scale
  and at a second scale. These are the standing
  counterexample to selection by weighting, in concrete
  form.
- The break-even rule (4): reuse wins when the avoided
  work exceeds the four combined costs, and only then;
  the win is monotone in the avoided work and antitone
  in a cost component.
- The closure worklist (10): the missing count and the
  per-rule missing predicate — each zero exactly when
  every premise is derived, each bounded by the premise
  count, each positive while a named premise is absent,
  each antitone under growth of the derived set — and
  derivability as the least closure, monotone in its
  seed and persistent under append.
- Incremental reevaluation (2): the one-append update
  in place — the frontier of the grown space is exactly
  the old frontier filtered by the appended candidate,
  plus the appended candidate when nothing old
  dominates it — and compensation in place: retract
  after insert, for a fresh candidate, restores the
  prior frontier at every other point.
- Reversible actions (5): an action restores its
  starting state; a composition of actions restores;
  the field-setting and toggle instances restore; and
  the refusal form — an action carried as the empty
  option restores nothing and claims nothing.
- Stop soundness (5): the fuel loop over a signal that
  grows by one is sound and stops only when the signal
  is sufficient; the certificate form — a plan certified
  against the whole remaining set is no worse than
  every plan in it — with its concrete instance over
  the control's own plan set; and the threshold
  control, a proved refutation of threshold stop as an
  optimality claim.
- The subset oracle (2): the powerset count law — the
  number of subsets of a finite list is two to its
  length — with its eight element checkpoint instance.
- Tensor edits as overlays (4): an overlay protects the
  fields it does not touch and applies the fields it
  carries; an edit round-trips through its overlay; and
  tied readings are preserved under the stated tie
  relation.

Axiom evidence in the tree: the axioms file prints a
line for every one of the 38 declarations. The repo's
own census records the gate as a cold pass with every
printed set inside the three standard axioms and none
using the choice axiom; no recorded gate log file
stands in the tree, so that pass is carried here as the
repo's recorded claim, at the strength its census
states it, not as a log this census read.

### The scoped development — 17 declarations in one file

In the scoped reversal folder, over arbitrary types:

- The finite inverse theory (6): an inverse is
  injective on its domain; a collision under an inverse
  is impossible; a finite inverse is sound; over a
  finite domain an inverse exists exactly under
  injectivity; inverses compose; and the residual form
  — where a plain inverse cannot exist, an inverse
  carrying the residual reconstructs exactly.
- Fibers and rank (5): the fiber lower bound in its
  list form and its finite form — a reconstruction must
  retain enough to name the fiber — and the rank
  results: ranking recovers a member of a duplicate
  free list, the rank is below the length, and the rank
  fiber is attainable.
- The scoped trace form (1): a trace of actions with
  checked inverses inverts as a whole, at the scope the
  trace names.
- Helpers (5, two of them private): removing one
  element shortens a list by one and keeps every other
  member; a duplicate free sublist is no longer than
  its list; mapping an injective function keeps a list
  duplicate free; and every finite index stands in its
  range list.

Axiom evidence in the tree: a recorded audit file
prints lines for 12 of the 17 — the five helpers carry
no printed line, so their axiom state is unrecorded
there. Of the 12 printed: 4 depend on no axioms, 4 on
propositional extensionality only, and 4 on the
standard pair. The folder's check script recompiles
the file and compares the fresh audit byte for byte
with the recorded one, and compares its empirical
receipts the same way — a recorded audit stands in the
tree, and a fresh run of that comparison by this
census is unrecorded.

## Controls and gate evidence

- Standing controls proved in this repo: the threshold
  control above (threshold stop refuted as an optimality
  claim), and the two never-selected results (selection
  by positive weighting refuted as a frontier test).
  The repo's census carries five standing refuted
  controls across the system; the other three — ranking
  head alone, the uncompensated append, and the no
  progress step — stand proved at their cited homes.
- Gates: the root check script scans for escape tokens,
  compiles both root files with warnings as errors, and
  runs the axioms audit; the scoped check script is
  described above. Gate state at the pin: the root pass
  is claimed in the repo's own census with no log file
  in the tree; the scoped audit is recorded in the
  tree. This census ran no build of its own.
- Executed evidence beside the proofs: the validation
  system's first pass over its state model, the action
  model's executed generalization table, and the lane
  result files stand in the tree as executed records at
  their own states — evidence of the executed kind, not
  theorems, and counted nowhere in the proven column.

## Premises carried rather than proven

The repo's own premise register, carried at its stated
strengths: the canonical premise (the ruled model is
the model; its falsification route, the re-founding
disposition, has landed and confirms); witness honesty
and reading fidelity, inherited; extraction fidelity
and witness honesty at the pipeline layer; the meaning
of the score axes in the world (route: the measurement
campaign); threshold choice (the stop results hold for
every threshold); execution fidelity — reversibility at
the execution layer rests on it until the validation
system demonstrates the round trip per action on fresh
observed state, and that cell stands UNMEASURED in the
repo's own census; progress (stop completeness is
conditional on the caller's step raising the signal);
and counted cost standing for real cost.

## Absent and proposed, at the repo's own states

- The general symmetric form of the never-selected
  result — a plan whose coordinate sum strictly exceeds
  the rivals' shared sum, at the symmetric point, is
  never selected by positive weights — is stated and
  unproved: a named lemma found during the proof
  attempt, owned by the theorem completion lane, its
  closing route a two case argument on the weight order
  or a convexity lemma over the segment. The two
  concrete instances are proved above.
- The worklist equality in its canonical form — the
  queue algorithm's computed set equals the least full
  closure at every append prefix, against the exact
  view semantics of the canonical home — is stated and
  unproved: a named lemma owned by the theorem
  completion lane with the worklist lane. The count
  lemmas that are its engine are proved above; two
  worklist developments at other homes landed in this
  same window and prove their own forms against their
  own homes' semantics, recorded in their annex deltas
  in this pass — neither is this lemma at its stated
  home.
- The resolution algorithm's claims stand as its home
  carries them: two inherited in model form, the rest
  theorem-to-be in that home, its optimality cell
  UNMEASURED as a theorem, and its eight open
  specification gaps carried with owners.
- The break-even rule's empirical figures and the
  general subset agreement over arbitrary extracts are
  reported, not reproduced: UNMEASURED, with owners and
  closing routes in the repo's census.
- The guided search space, the recursive algorithm
  families, and the meta level stand in the repo as
  documents with executed first pass records: proposed
  and implemented at their own stated states, verified
  only where the census above says so.

State: PROVEN in source at the pin for the 55
declarations above, read in full in this census — the
scoped half on its recorded audit, the root half on the
repo's recorded gate claim with its full printed audit
in source — with the premise register carried at its
stated strengths, the execution layer cell UNMEASURED,
and the two named lemmas and the carried gaps standing
as named work at their owners.
