# Census — software-redundancy-is-equivalence

## Pin and identity

- Census pin and live head (read in the thirty-eighth
  enumeration, 2026-11-19):
  37514fb760ae8457bd4b75514b2dbcc4fbdccfef
- First census pin: 14992281af87ae924f6832cdb8de7ecacc5d9a92
  (the thirty-sixth enumeration), at which the repo was a
  specification and a proof skeleton. This census replaces
  that census in full: the head moved by five commits, and
  every file below was read in full at both pins by this
  watch.
- Visibility: public. Default branch: main.
- Description (the repo's own): redundant compute,
  re-founded on the canonical hypergraph: redundancy as
  equivalence of terms at symbolic resolution.
- Toolchain: Lean 4.19.0, pinned in the proof folder's
  toolchain file. No Mathlib. The tree is twenty-two
  files: the specification, a definitions record, and a
  readme at the root, unchanged at both pins; a proof
  folder of nine Lean files with a check script and a
  recorded gate log; and three new parts beside them —
  a resolution algorithm specification, a case register,
  and a built registry folder.
- Determination: proof-bearing by content, as at its
  first census. Its proven content at this pin is the
  full development below, stated at exactly the strength
  its files state.

## Thesis, in plain English

The redundant compute program, re-founded on the
canonical model. There is one hypergraph: the total
equivalence graph of equivalent terms, whose edges are
sets of equivalent symbolic expressions at the minimum
resolution, the symbol being the finest grain. Resolved
information is appended only, so drift is excluded by
construction. Redundancy, on this model, is a property
of equivalence classes: a term is redundant when its
edge holds at least one other term distinct from it by
spelling, and the excess of a graph is its count of
collected terms minus its count of edges. Colorings,
qualifications, and every proof of the program are
constructed from this one graph and from nothing else.
At the first pin this model stood as a specification at
settled intent with its claims proposed and a skeleton
proof tree. At this pin the rebuild has landed: the
model is implemented in Lean and every claim of the
specification's claims section is proved in the tree,
at the states recorded below.

## What landed between the pins

Five commits: the algorithm specification and its case
register seeded; the theory rebuilt on the canonical
model; the two branches merged; and the registry built
on the model with its second epoch solved. Fifteen
files changed: thirteen added and two modified — the
core proof file, rewritten and grown, and the recorded
gate log. The specification, the definitions record,
and the readme are byte-identical at both pins: the
claims proved are the claims the first census carried
as proposed, word for word the same specification.

## Theorem census — 217 declarations in eight Lean files

Counted by the watch method in this census: every
theorem or lemma declaration in every Lean file at the
pin, comments excluded, one method at both pins. At the
first pin the same method counts one declaration, the
seed fact. At this pin: the core file 35, the growth
operations file 72, the claims file 63, the registry
file 39, the derived views file 3, and the controls
file 5 — 217 in total, every name distinct. The audit
file and the premises file carry no theorems: the first
holds the printed axiom audit, the second the two
premise definitions. No admitted-proof token, no axiom
declaration, and no native-decision token stands in any
Lean file, by this census's own scan of every file.

The development, by part:

- The core file implements the specification's model
  sections: symbols and terms with decidable spelling
  equality; the three scopes and their nesting; the one
  lattice of states; the one hypergraph with its
  validity predicate; equivalence of terms; resolution
  levels; the finite resolved upper bound — a state of
  the lattice, the least saturated state above a level's
  state, and finite; the view; and redundancy as excess,
  with the counting facts the claims rest on (excess as
  the sum over edges of size minus one, and the witness
  fact that a graph of excess at least one holds two
  distinct terms standing together).
- The operations file implements append-only growth:
  the four operations (enter a term, join two terms,
  record a level, paint a color) and nothing else builds
  a graph. Each operation appends its entry to the log,
  preserves validity, and grows the graph under the
  growth relation; the file proves the operations'
  edge, excess, and collection readings, the reach and
  chain facts of the growth relation, and the run form
  over a list of operations.
- The claims file proves the specification's claims,
  each under the single-word name the specification
  assigns it, as the claims section below records.
- The registry file implements the registry of the
  specification's registry section: configurations taken
  up to configuration equivalence, the five fixed content
  measures, the deterministic score as a weighted sum
  over those measures, the append-only registry with
  exactly one entry per witnessed class, epoch appends
  as the only reweighting, and the registry invariant
  with its preservation under any list of witnessings.
- The views file carries the one derived layer the
  specification obliges: derived steps and derivability
  over them — derivability monotone in the collected
  terms, monotone in the recorded steps, and the
  elimination fact that adjoining an already derivable
  term changes the derivable reading not at all.
- The controls file carries the five standing controls,
  each now a proved statement over concrete data, as
  the controls section below records.
- The premises file states the two inherited premise
  labels as explicit premise definitions, each with its
  falsification route, as the premises section below
  records.

## The claims — all eight proven at this pin

The specification's claims section listed eight claims
as proposed semantics at the first pin. Each is proved
in the tree at this pin, from the model's definitions,
under the family gate:

- Monotonicity under expansion: every equivalent pair
  stays equivalent under growth; witnessed redundancy
  persists; and excess never decreases — the counting
  heart proved first (when every old edge is covered
  jointly by one new edge, the summed excess cannot
  grow), then the claim in its operation, run, and
  witness forms.
- Compounding: for two appends to a common graph, in
  either order — the excess after both is at least the
  excess after each alone, and is exactly the common
  graph's excess plus the count of effective joins in
  the two appends together, a join effective only in
  the combined appends counted exactly once. No additive
  claim over shared content is stated, as the
  specification directs. The proof builds a twin
  relation between the two orders and carries it through
  every operation.
- Appearance: a cross join between the two appends
  raises the excess at least one above the common
  graph's; and the control direction — under the
  separateness premise stated in the development (no
  cross join and no shared term joining the appends),
  the combined excess is exactly the sum of the two
  appends' separate deltas.
- Coloring: color union is commutative, associative,
  and idempotent up to membership; painting keeps every
  existing color; and the two-filter rule as a theorem
  about the derived mark — the intended mark is present
  exactly where both an observation entry and an intent
  entry for that qualification are present, with the
  painting discipline carried as the stated premise of
  the development's filter definitions.
- Bounds: the bound of a level is a state of the one
  lattice, the least saturated state above the level's
  state, and finite; under growth the bound as a reading
  only grows, while the recorded bound in the log never
  changes — the two halves proved of the two different
  objects, the reading and the record, kept apart by
  name as the specification directs.
- Reconciliation: appending two levels in either order
  yields final graphs whose standing-together reading
  agrees, whose edge content matches edge for edge in
  both directions with the same terms and the same
  colors, which both grow from the starting graph, and
  whose logs hold both record entries, each with the
  bound as taken at its own append moment.
- Scope: a growing run keeps every collected term
  collected with the same spelling, and every old edge
  grows — some later edge holds all its terms and all
  its colors; the scope nesting itself (the trivial
  scope inside the first scope, the full scope at the
  top) stands in the core file.
- Registry: uniqueness and provenance exact — after any
  witnessings from the founding registry, every
  witnessed configuration class has exactly one entry,
  every entry's provenance is exactly the witnessings
  of its class in append order, and every entry's
  configuration was witnessed; determinism — the color
  a noting records is the epoch and the score of the
  witnessed configuration under that epoch's scheme, a
  function of content alone, the same for equivalent
  configurations; and the epoch clauses — an epoch
  append appends exactly one epoch, earlier schemes are
  untouched, and colors recorded under earlier epochs
  stand as the entry's color list only grows.

## Controls — the five standing controls, proved

Each control is a proved statement over concrete data
in the controls file, and each is printed in the gate
log's audit:

- Zero: a valid graph with excess zero and at least one
  edge exists — two singleton edges. It refutes the
  universal redundancy claim, which is stated nowhere.
- Split: growth from a witnessed redundant concrete
  graph is witnessed redundant. It refutes the claim
  that redundancy can be split away by growth.
- Free: two appends with no cross join and no shared
  term produce no appearance, on a concrete instance.
- Order: two spellings differing only in argument order
  stand in distinct edges in a concrete graph until an
  equivalence entry joins them. It refutes silent
  identification of spellings.
- Filter: on a concrete graph, an edge painted observed
  only carries no intended mark, and an edge painted
  wanted only carries none either.

## Premises — the two inherited labels, stated

The premises file states both inherited labels as
explicit premise definitions in Lean form: witness
honesty (for a subject-supplied verification predicate,
every join entry of a graph's log carries a witness the
predicate verifies) and reading fidelity (for a
subject-supplied reading, every external fact a subject
names holds of its reading among the term facts named).
Each carries its falsification route in its own text.
The file states, and the development's structure
carries, that no theorem depends on either: they bind
where the model is applied, not what its theorems say.
State: premises, named and carried — never counted
proven.

## A flagged name loss — the seed fact

Defect-rule record, flagged rather than absorbed: the
name comparison between the pins, one mechanical method
at both, finds one lost name — the seed fact, the single
declaration of the first pin (two propositions joined by
a two way implication are equal, on propositional
extensionality only). The rewritten core file does not
restate it. Its disposition, on the record of the first
census: the seed was a fact of the logic, not of the
model, standing only so the family gate had a compiled
development with a printed audit to check, and the file
that carried it now carries the model itself, whose
audit prints thirty-eight theorems. The proven set as a
whole grew from one declaration to 217, and no theorem
of the program was lost — the lost name is the skeleton
placeholder the rebuild replaced. The loss is flagged
here and in the run record, not silently absorbed.

## The three new parts beside the proof

- The resolution algorithm specification: a specification
  document at settled intent about the algorithm's shape,
  by its own status line not implemented and not verified
  — no code and no proof in its lane implements it, and
  its claims stand as proposed semantics at the states its
  own claim lines give (theorem to be, premise, or open
  gap, the gaps named with owners). This census carries it
  at exactly that strength: a specification, not a result.
- The case register: the algorithm specification's case
  accounting, append-only by its own rules — eighty-three
  seed cases generated by crossing its named dimensions,
  each entered as accounted (a named rule and claim cover
  it, the claim at its own proposed state) or as a named
  gap. No case in the register is verified behavior, by
  the register's own state rule.
- The built registry: measured behavior at its named
  pins, by its own readme — fifteen entries, one per
  unique witnessed configuration, over 321 witnessed
  terms from the library extract at its named pin, every
  configuration at symbolic grain, excess and colored
  edges zero in every configuration (no record in the set
  witnesses an equivalence between distinct terms, stated
  there as a finding about the set). Two epochs stand:
  the founding unit scheme, and a solved second scheme
  found by exhaustive enumeration of one hundred thousand
  schemes by the registry's builder — executed evidence,
  at exactly the strength its record states: the best
  scheme over the searched set, no bound over schemes
  outside it claimed. The excess and colored weights are
  unidentifiable on this set, a gap its record owns. The
  builder is a foreign scaffolding program beside the
  data, named as such in its record.

## The predecessor, dispositioned

Unchanged from the first census: the repo's readme —
byte-identical at both pins — dispositions its
predecessor, the expands repo at its pin 1ea28648, as
founded on a list counting construction whose theorems
are not a foundation here; that predecessor's census and
ledger rows stand at their pins as the record of what it
proved about its construction. The disposition is carried
as the repo's own recorded ruling, relayed from its
readme until a firsthand check of the program record
replaces it.

## Gate state

The recorded gate log stands in the proof folder at the
pin: Lean 4.19.0; thirty-eight axiom prints — the audit
file's thirty-three named theorems and the five
controls — of which four depend on no axioms, two on
propositional extensionality only, and the rest on
subsets of the standard three; and the axiom subset
check passing, the allowed set being exactly those
three. The check script stands in the tree in its
widened form: it scans every Lean file for the banned
escape tokens, compiles every file with warnings as
errors, and fails on any printed axiom outside the
allowed set. Gate state: green at the census pin by the
repo's recorded log. This census ran no build of its own.
