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

## Re-census — 2026-11-20, the forty-sixth hourly re-synthesis watch

The watch re-read the live head at fcb9595310d8a0782cb7fca1b2203d80b28c8d8c in the full enumeration and re-censused the repo at theorem level at that head: every Lean file read in full, counted by the watch method over the tree at each pin. The census pin moves to the fresh head in this pass.

### What stands at the fresh head — 94 declarations in seven Lean files

Counted at the fresh head: 94 theorem declarations, 94 distinct names, where the last census pin carries 55 in three files. Thirty-nine names gained, none lost, and no escape token stands in any of the seven files by this watch's scan.

- The root development — 42 declarations in one file (was 38). The four gains close named work from the first census. The general symmetric form of the never-selected result, stated and unproved there as a named lemma, stands proved here in three parts: the segment form — for rival plans sharing a coordinate sum and a symmetric middle plan whose doubled coordinate strictly exceeds that sum, no pair of positive weights selects the middle plan against both rivals, the nonlinear step carried by the distributivity expansion the repo's own census names; the frontier form — the middle plan stands on the frontier of the three plans whenever its coordinate lies strictly below at least one rival coordinate; and the canonical form — the segment shape with endpoints at zero and the shared sum carries both parts for every middle coordinate strictly between half the sum and the sum. The fourth gain is the overlay collapse lemma of the tensor edit development: a stack of overlays and its collapsed single overlay apply identically on every state, proved by induction on the stack. The axioms file at the fresh head prints a line for every one of the 42, and the repo's own census, updated in this window, records the gate as a cold pass with every printed set inside the three standard axioms and none using the choice axiom — carried here at the same strength as the first census carried it: the repo's recorded claim, with no recorded gate log file standing in the tree for the root development.
- The scoped development — 17 declarations in one file, byte-identical between the pins, standing exactly as the first census records, on its recorded audit.
- The action consensus development — 9 declarations in one new file, in the native resolution lab's proof folder: the fiber of interpretations over an appended history is exactly the old fiber cut by the added answers; appending evidence refines the fiber; certification is preserved under refinement and under append while the refined fiber stays live; a certified action has no countermodel, and, under decidability of the lawfulness reading, certification is exactly liveness with no countermodel; two interpretations answering alike on every available query share every fiber the available history cuts, so a conflicting pair of that kind obstructs any certified stop; and a concrete control — a decision depending only on an established first coordinate needs no resolution of the second. A recorded check log in the folder prints all nine: five depend on no axioms and four on propositional extensionality only.
- The product frontier development — 5 declarations in the same folder: dominance over a coproduct cost is exactly dominance in one component with weakness in the other; the frontier of an independent product is exactly the pair of component frontiers; rows certified under a frozen key bridge replay at a changed cut; replay after an independent append returns the reused rows and the product frontier from the cached component and the new component alone; and a standing control — a join contract coupling the components can leave the joined plan as the only feasible one, so keeping only component optima loses it. A recorded check log in the folder prints all five: three depend on no axioms and two on propositional extensionality only.
- The suffix page development — 10 declarations in one new file, in the native resolution lab's suffix research folder: the block enumeration count is the sum of block sizes; block selection is exact against the flattened enumeration; the end of sequence block counts one exactly when its flag stands and stands in range there; the subtree mass equals the reference enumeration's length at every fuel; selection by rank is exact against the reference, paging is exact, and selection at or past the mass is none; a private helper keeps prefixed blocks duplicate free, and the reference enumeration itself is duplicate free wherever outgoing labels are distinct. A recorded check log in the folder prints seven of the ten — the reference, count, selection, mass, page, and out of range results, on subsets of propositional extensionality and quotient soundness — so the axiom state of the remaining three, the two end of sequence results and the private helper, is unrecorded from that log; their print lines stand in no file this watch read.
- The compositional pruning development — 11 declarations in one new file, in the resolution lab's proof folder: weakness is reflexive, and dominance composes with weakness on either side and with itself; one additive continuation preserves dominance exactly in both directions; a kept set that covers the pool context by context keeps the frontier of every kept plan exact, keeps the whole frontier image exact, and keeps it exact piecewise over any target family of contexts; a finite control — two enabling atoms individually worthless and jointly completing one rule; and the status of a key against a known and a covered inventory is exact in both its covered-new and its unsearched forms. The file prints axiom lines in source for seven of the eleven — the additive, frontier, image, piecewise, control, and two status results — and no recorded check log stands in its folder, so a passing gate for this file is unrecorded and the four composition results carry no printed line this watch read.

### States carried forward

- Premises: the repo's premise register stands as the first census records it, at its stated strengths; reversibility at the execution layer remains UNMEASURED in the repo's own census.
- Absent and named work: of the two named unproved lemmas the first census carried, the general symmetric form is proved above and stands closed; the worklist equality against the canonical home's view semantics remains stated and unproved, as named work at its owners. The resolution algorithm's carried gaps stand as the repo's census carries them.
- Executed evidence: the two labs land with their executed records — staged native builds, receipts, benchmarks with losing controls among them, and validation records — standing in the tree as evidence of the executed kind at their own states, counted nowhere in the proven column.

State: PROVEN in source at the fresh head for the 94 declarations above, read in full in this re-census — the root development on the repo's recorded gate claim with its full printed audit in source, the scoped development on its recorded audit, the action consensus and product frontier developments on their recorded logs, the suffix page development on its recorded log for seven of its ten, and the compositional pruning development in source with its gate unrecorded — with the premise register carried, the execution layer cell UNMEASURED, and one named lemma and the carried gaps standing as named work. The census pin moves to fcb9595310d8a0782cb7fca1b2203d80b28c8d8c on this re-census; the placements in the synthesis and the ledger row are restated at the new pin in this same pass.

## Watch delta — 2026-11-20, the forty-seventh hourly re-synthesis watch

The watch re-read the live head at 0ac60e7db7207c7b823283836fa66138a5ee7e3f in the full enumeration and read the whole tree at that head (181 files, not truncated). Every Lean file in the tree is byte-identical between the census pin fcb9595310d8a0782cb7fca1b2203d80b28c8d8c and the fresh head — the same blob for each of the seven files, carrying the same 94 declarations with the same name set, counted by the watch method over the tree at each pin. The movement between the heads is one commit and one file: the repo's own census gained an addendum recording that the worklist equality lemma — the one named unproved lemma this annex carried forward from the re-census above — stands proved in the frontier home at its fresh head in this same window, as a bridge module over a verbatim copy of the canonical view file, with a cold gate pass at that pin recorded there; the frontier annex delta in this pass carries the proof's own census. With that lemma closed by its proof at its stronger home, and the general symmetric form already proved at the census pin, no named unproved lemma from this repo's census remains. The proven set this annex records is unchanged at the fresh head, at the strengths the re-census above records; the execution layer cell stands UNMEASURED, as that re-census records.

## Watch delta — 2026-11-22, the ninety-fourth hourly re-synthesis watch

The watch re-read this repo's live head at 799bc652346a3cb9507d606e4c69fcecaa31370e in the full enumeration and read the whole tree at that head (186 files, not truncated) and at the last recorded head 0ac60e7db7207c7b823283836fa66138a5ee7e3f (181 files). No Lean file stands among the changed files between the heads, so the proven set is unchanged: the same ninety-four declarations with the same name set at both, counted by the watch method over the tree at each pin, with no sorry token and no axiom declaration at the fresh head. The movement is five commits carrying the meta search as incremental recomputation work — carried instance frontiers, selections, and the meta frontier, beside the deletions, early cutoff, and resume work it shares with its sibling repos in this window — landing as executed work: five files added, the incremental folder with its frontier, gate, and meta search modules and its readme, none of them Lean. That work is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at fcb9595310d8a0782cb7fca1b2203d80b28c8d8c, with the placements at that pin.

## Watch delta — 2026-11-22, the hundred-sixth hourly re-synthesis watch

The watch re-read this repo's live head at 91d396df6da5d77823360d8bd29d7f75a7b790c5 in the full enumeration and read the whole tree at that head (187 files, not truncated) and at the last recorded head 799bc652346a3cb9507d606e4c69fcecaa31370e (186 files). Every Lean file is byte-identical between the heads, so the proven set is unchanged: the same declaration set with the same name set at both, counted by the watch method over the tree at each pin, none gained and none lost, at the strength the earlier deltas in this annex record. The movement is one commit of meta search work — a candidate's own score change invalidates the selections that saw it — landing as executed work: one file added, a fuzz script in the incremental folder, and three files changed, its readme and the gate and meta search sources, none of them Lean. That work is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at fcb9595310d8a0782cb7fca1b2203d80b28c8d8c, with the placements at that pin.
