# Census — software-redundant-compute-expands

## Pin and identity

- Census pin and live head (read in the thirty-fifth
  enumeration, 2026-11-19):
  1ea286488cd4fecb7edb7f5debe407db04456b88
- Visibility: public. Default branch: main.
- Description (the repo's own): redundant compute under
  expansion-only hypergraph growth — measure
  monotonicity, join compounding, and the touch kernel,
  proved in Lean.
- Created in this window: the repo is new since the
  thirty-fourth enumeration; one commit stands at the
  head, carrying the whole development.
- Toolchain: Lean 4.19.0, pinned in the proof folder's
  toolchain file. No Mathlib; the development is four
  Lean files in one proof folder, beside a check script
  and a recorded check log, with a readme, a spec file,
  and a definitions file at the root — eleven files in
  the tree.
- Determination: proof-bearing by content — Lean sources
  and a recorded gate log stand in the tree, found by
  the content check on its first enumeration, not by
  its name.

## Thesis, in plain English

Under expansion-only growth of a behavioral hypergraph —
nodes and hyperedges appended, nothing removed —
redundant compute, once witnessed, never disappears.
The redundancy measure of a graph counts the non-first
occurrences in its node list and in its incidence list
(every hyperedge flattened to its premises followed by
its conclusion). The measure splits exactly over append,
is superadditive over joins, and gains one further unit
wherever the joined parts share a node or an incidence
value, so redundancy can appear at a join of two parts
that each carry none. A graph's measure is positive
exactly when an explicit duplicate witness exists, and
a computation whose conclusion is already derivable —
the persistence home's redundancy criterion, mirrored
here — stays derivable under every expansion. Witness
reconstruction from an overlap is carried by the touch
kernel: enlarging the sample or expanding the graph
never un-touches a hyperedge, and the hyperedges fully
inside a sample are always among the touched ones. The
model was directed by Chris on 2026-11-19 as the growth
half of the universal behavioral hypergraph campaign;
the repo's spec file states the claim in full, with its
executable six step method, its premise labels, and its
falsification protocols.

## Theorem census — 37 declarations in four Lean files

Counted by the watch method in this census: every
theorem declaration in every Lean file at the pin. No
admitted-proof token stands in any file, by this
census's own scan. Axiom states are from the repo's
recorded check log, which prints all 37 declarations:
2 depend on no axioms, 4 on propositional
extensionality only, and 31 on the standard pair.

### The core file — 19 declarations

The counter and the measure:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| counter append split | The duplicate counter over a joined list is the count over the first part plus the count over the second part against the first part as seen list. | the standard pair |
| counter monotone | The counter is monotone in the seen list: a larger seen list counts at least as much over the same list. | the standard pair |
| counter positive | A seen element that occurs in the list is counted at least once. | the standard pair |
| counter witness | A positive count over any seen list yields a split of the list at an occurrence whose value lies in the seen list joined with the part before it. | the standard pair |
| first split | A list splits at the first occurrence of any of its elements, the head part free of it. | propositional extensionality only |
| measure append split | The measure of a joined list is the measure of the first part plus the count of the second part against the first. | the standard pair |
| measure left | The measure of the first part never exceeds the measure of the joined list. | the standard pair |
| measure right | The measure of the second part never exceeds the measure of the joined list. | the standard pair |
| measure sum | Superadditivity: the measure of a joined list is at least the sum of the measures of its parts. | the standard pair |
| measure strict | An element occurring in both parts adds one further unit to the joined measure, beyond the sum of the parts. | the standard pair |
| measure appear | An element shared by two parts makes the joined list redundant even when each part alone carries no redundancy. | the standard pair |
| measure witness | The measure is positive exactly when an explicit duplicate witness exists. | the standard pair |

Derivability, mirrored from the persistence home at its
pin, with the proofs this development's own:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| derivability in the store | Derivability is monotone in the store: a larger store derives at least as much. | none |
| derivability in the edges | Derivability is monotone in the recorded edges: recording more edges derives at least as much. | none |

Graphs and expansion:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| graph growth | The graph measure is monotone under expansion: appended nodes and hyperedges never decrease it. | the standard pair |
| graph witness | Witnessed redundancy persists under expansion: a graph carrying a duplicate witness carries one at every expansion. | the standard pair |
| expansion transitive | Expansion is transitive: expansions compose into an expansion. | propositional extensionality only |
| chain monotone | Along any expansion chain the measure is non-decreasing, in the two step form from which every finite chain follows. | the standard pair |
| derivability under expansion | A derivable fact stays derivable under expansion: a computation witnessed redundant stays redundant at every later step. | propositional extensionality only |

### The join file — 11 declarations

Joining:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| join incidence | The incidence list of a join is the append of the incidence lists of the parts. | propositional extensionality only |
| join measure | The measure of a join, in components: the measure of the joined node lists plus the measure of the joined incidence lists. | the standard pair |
| join left | The measure of the first part never exceeds the measure of the join. | the standard pair |
| join right | The measure of the second part never exceeds the measure of the join. | the standard pair |
| join sum | Compounding: the measure of the join is at least the sum of the measures of the parts. | the standard pair |
| join strict by node | A node occurring in both parts adds one further unit to the joined measure, beyond the sum of the parts. | the standard pair |
| join strict by incidence | A value occurring in the incidence of both parts adds one further unit to the joined measure. | the standard pair |

The touch kernel of witness reconstruction:

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| filter monotone | Filtering with a weaker predicate keeps at least as many elements: the filtered length is monotone in the predicate. | the standard pair |
| touch monotone | Enlarging the sample never un-touches a hyperedge: the touched count is monotone in the sample. | the standard pair |
| touch growth | Expanding the graph never un-touches a hyperedge at a fixed sample. | the standard pair |
| touch bound | Every hyperedge fully inside a sample is touched by it: the inside count never exceeds the touched count. | the standard pair |

### The controls file — 6 declarations

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| zero control | A graph with no redundancy at all exists in the model: its measure is zero and it is not witnessed redundant. | the standard pair |
| universal control | The universal existence claim is false in the model: not every graph is witnessed redundant. | the standard pair |
| shrink control | Removal destroys redundancy: the list with a duplicate has measure one, the same list with the duplicate removed has measure zero. | the standard pair |
| free control | With no overlap the strict compounding gain is absent: two single-node graphs on distinct nodes join to measure zero, and the sum-plus-one bound fails. | the standard pair |
| exact control | Touching is not containing: the sample node touches the single hyperedge, yet no hyperedge is fully inside the sample. | the standard pair |
| sample control | The empty sample touches nothing in the sample graph: sample growth is necessary for the touch results. | the standard pair |

### The synthesis file — 1 declaration

| Token | Hypotheses to conclusion | Axioms (recorded log) |
|---|---|---|
| joined | The joined theorem: along an expansion chain the measure never decreases; witnessed redundancy persists to the end of the chain; a computation redundant at the start stays redundant at the end; the first two graphs of the chain compound into their join at least additively, and strictly by one further unit where they share the named node; and the touch kernel holds at the first graph — a larger sample touches at least as much, and what is fully inside a sample is always among what it touches. Its only unproved antecedent is the named empirical yield premise below; no conjunct's proof uses it. | the standard pair |

## Controls and gate evidence

- Six standing controls stand in the controls file,
  each a proved statement over concrete data, proving
  by execution that the condition it weakens is load
  bearing: the zero graph (the closed loop analogue —
  the family subject with zero duplicate groups under
  the campaign protocol), the refuted universal form,
  removal destroying redundancy, the absent strict gain
  without overlap, touching not containing, and the
  empty sample touching nothing.
- Gate: the check script in the proof folder compiles
  every Lean file in the tree with warnings as errors,
  rejects every proof escape token, prints axiom
  dependencies per theorem, and fails if any printed
  axiom lies outside the allowed set of propositional
  extensionality, classical choice, and quotient
  soundness. The recorded check log in the tree ends in
  its axiom subset check passing, with all 37 printed
  declarations' axioms within the standard set: 2
  depend on no axioms, 4 on propositional
  extensionality only, and 31 on the standard pair; no
  printed theorem uses the choice axiom. Gate state at
  the pin: green on the recorded log; this census ran
  no build of its own.

## Premises carried rather than proven

Three premises, all outside the Lean development, named
in the repo's spec:

- Yield, an empirical rate: the touched yield of a
  random overlap compounds at a measured multiplier of
  about two and a half at a fifth overlap, on the
  traceability hypergraph at its named pin. Campaign
  evidence at a pin, not a theorem; the development
  proves the proved skeleton only — monotonicity and
  the inside bound — and no rate above one is claimed
  in Lean. The joined theorem carries this premise as
  an explicit antecedent. Its falsification route is
  stated in the spec.
- Listing, a modeling premise: growth is read in append
  order. The development does not prove the measure
  invariant under re-listing, so a reading of a real
  system's growth as expansion rests on the recorded
  order being the growth order.
- Mirror fidelity, a reading premise: the derivability
  definition and its two monotonicity theorems are the
  persistence home's definitions and statements at its
  pin, mirrored and proved again here; only the claim
  that the mirror is faithful rests on reading.

## Absent and proposed, at the repo's own states

- Universal existence — any software is redundant — is
  refuted, twice over: by the closed loop subject under
  the campaign protocol, and in the model by the
  universal control. It is not a claim of this
  development in any form; the surviving form is the
  witnessed form the theorems state.
- A rate for compounding of the measure itself — for
  example, that joined redundancy grows by a fixed
  factor per shared element beyond the first — is not
  claimed. The proved strict form is one unit per join
  per shared component kind; the faster question is
  empirical, for the campaign's next round.
- Premise-closed reconstruction — a sample closed under
  premises reconstructs exactly — is proposed by the
  empirical lane as its next protocol: not run there
  and not formalized here, with its closing condition
  stated in the spec.

State: PROVEN at the pin for the 37 declarations above,
on the recorded gate log, with the three named premises
carried at exactly the states the repo itself states,
the universal form refuted in the tree, and the two
further forms carried as not claimed and proposed.

## Watch delta — 2026-11-19, the fortieth hourly re-synthesis watch

The watch re-read the live head at 559f308b5b2d6ed3cf5c16f306ef9bbe5c01f266 in the full enumeration and read the tree at that head in full. The movement since the census pin is five commits, one merge and four landings: a held list-form extension, the canonical layer, the premise-closed sample kernel, and the gate log for the resulting tree. Nine Lean files were added and one file changed, the recorded check log; nothing was removed and no tree read was truncated. The four files this census records are byte-identical between the census pin and the fresh head, so every result above stands unchanged, and the proven set grew by addition only: counted by the watch method with comments stripped (the same method reads 37 at the census pin, as above), the tree now carries 194 declarations in thirteen files — the canonical hypergraph file (24), the coloring file (32), the re-listing file (27), the units file (21), the re-basing file (18), the resolution file (12), the join and intent files (11 and 10), the case file (9), and the sample file (4), beside the original four. No name was lost.

What the new files prove, at the strength their own headers state. The canonical file founds the program on one record log: the derivability and hypergraph definitions mirrored from the optimality home at its named pin and proved again, with an equivalence of terms at each resolution level. The re-basing file restates this repo's own measure on that log, as a count of redundant support, and proves it monotone. The re-listing file discharges the listing premise carried above: the counter depends on its seen list only through membership and is invariant under every permutation, so the measure is invariant under every re-listing and expansion needs no order. The sample file proves the premise-closed reconstruction this census carried as proposed: a premise-closed sample loses no derivation of any of its atoms, with the non-closed case standing as its control; the measured protocol run itself remains outside the repo, as the file states. The resolution file states the resolution algorithm and proves it total and Pareto optimal over its stated objective set, returning an explicit unmeasured outcome rather than a silent coarse answer when the budget cannot afford the symbol level. The coloring, intent, case, and units files carry the append-only coloring of uniquely witnessed configurations, intent composition on the one hypergraph, the append-only case hierarchy, and the further measurement units tied to the graph measure by theorem.

Gate evidence at the fresh head: the recorded check log in the tree was read in full in this watch. It prints axiom lines for 189 of the 194 declarations — 15 depending on no axioms, 32 on propositional extensionality only, 118 on the standard pair, and 24 on the full standard set — and ends in its axiom subset check passing; five counted declarations carry no printed line in the log, among them the canonical file's three equivalence properties, so their axiom state is unrecorded from this log. No proof escape token, no admitted proof, and no axiom declaration stands in any of the thirteen files by the watch scan. Premises restated: the yield premise and the mirror fidelity premise stand as above; the listing premise is discharged, as recorded here; and the census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88 with a full theorem-level re-census at the fresh head owed.

## Watch delta — 2026-11-20, the forty-fourth hourly re-synthesis watch

The watch re-read the live head at 05e0584eb5f0f7f43bd2274a92d5dcfde1122e16 in the full enumeration and read the tree at that head in full. The movement since the last recorded head 559f308b5b2d6ed3cf5c16f306ef9bbe5c01f266 is two commits adding exactly one Lean file, the candidate impact file, built on this repo's own canonical layer; the other thirteen Lean files are byte-identical between the two heads, so every result above stands unchanged, and the proven set grew by addition only: counted by the watch method with comments stripped, the tree now carries 202 declarations in fourteen files, where the last recorded head carries 195 in thirteen — 154 distinct names against 147, seven gained and none lost.

What the new file proves. Over a two-seed joint rule — a conclusion derivable from the two seeds together and from neither alone — it proves reachability is not qualification: the joint rule's premises are reachable from each seed; each seed is necessary unless the conclusion is already a root; the qualification form is exact — the conclusion is derivable precisely when it is itself a seed or both joint premises are seeds; the complementarity result, that neither seed alone derives the conclusion and the two together do; the agreement of the canonical log view with the direct form; and that the appended joint consequence stands in the log view. The file's last three results carry their own print lines in the file. The watch scan found no proof escape token in the file. The recorded check log in the tree predates this file — it stands unchanged in this movement — so a recorded gate run covering the new file is not in the tree; its gate state rests on the file's own print lines and this watch's reading.

Premises restated: the yield premise and the mirror fidelity premise stand as above. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88 with a full theorem-level re-census at the fresh head owed.

## Watch delta — 2026-11-20, the forty-fifth hourly re-synthesis watch

The watch re-read the live head at 4da720a704151c92c7ee28278ba8538703638271 in the full enumeration and read the tree at that head in full. The movement since the last recorded head 05e0584eb5f0f7f43bd2274a92d5dcfde1122e16 is six commits in three landings: a certified action selection development with its measured joint witness search, an append-only canonical closure with its waiter index test, and a checkpointed convergence development for incremental intelligence. Eighteen files were added and none changed or removed; the fourteen Lean files of the last recorded head are byte-identical at the fresh head, so every result above stands unchanged, and the proven set grew by addition only: counted by the watch method with comments stripped, the tree now carries 240 declarations in seventeen files, where the last recorded head carries 201 in fourteen by the same method — 192 distinct names against 153, thirty-nine gained and none lost. The forty-fourth watch's record reads the last recorded head one declaration higher, at 202; the file identity evidence governs, and the one count difference stands noted here rather than absorbed.

What the new files prove. The action selection file (13 declarations), built on this repo's canonical layer: an action's prerequisites, its checked inverse, and its metric readings are each certified exactly by their checks; dominance and the frontier over scored actions are exact; a selected action is certified and stands at the best rank; the cost sum bound holds; dominance lowers the unit rank; and the stop results — an exact stop with its no eligible form, invariant under a scoring-only reweighting, with dispatch invariant under permutation of the candidate list. Its companion document states the gate discipline: proposals and weights cannot pass the proof and authority gate on their own, and the executable companions carry no machine-checked refinement to the Lean model. The closure worklist file (15 declarations): the projected records are exactly the canonical view's edges; the distinct missing machinery is exact, with its update form; readiness is exact; the run is sound, its ready set is empty exactly when the view is closed, a ready step spends one, and the drained run is closed — the closure form, the drained worklist computing exactly the canonical closure; and the resume forms, the canonical and plain resume results exact. The intelligence join file (11 declarations): the join of event sets is associative, commutative, and idempotent; two replicas converge at a delivered cut; a missing prefix is detected exactly, with its iff form; no detector can see an uncheckpointed tail; an append represents the union of its parts; projections of the same delivered set agree; and reconstruction from a delivered set is exact, including at a join of two sets. The two companion folders carry executed Python replays with recorded outputs — the closure replay over growing oracle comparisons and the intelligence replay over arrival permutations — executed evidence at their own states, each readme stating the replay is a reference, not a verified refinement of the Lean model.

Gate evidence at the fresh head: each new file carries its own print lines in source — the closure and join files print every declaration they carry, and the action file prints twelve of its thirteen, the cost sum bound helper carrying no line. The recorded check log in the proof folder is byte-identical between the two heads and predates all three files, so no recorded gate run covering them stands in the tree; their gate state rests on the files' own print lines and this watch's reading, as the candidate impact file's did in the last pass. Premises restated: the yield premise and the mirror fidelity premise stand as above. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88 with a full theorem-level re-census at the fresh head owed.

## Watch delta — 2026-11-21, the seventieth hourly re-synthesis watch

The watch re-read this repo's live head at 1c794e29c897053658ce47e7a42cac6a712621f2 in the full enumeration and read the whole tree at that head (67 files, not truncated) and at the last recorded head 4da720a704151c92c7ee28278ba8538703638271 (39 files). The proven set grew between the heads and lost nothing: 335 theorem declarations at the fresh head against 240 at the last recorded head — 287 distinct names against 192 — counted by the watch method over the tree at each pin, with ninety-five names gained, none lost, and no sorry and no axiom declaration at either head. The growth is three new files in the proof folder: the worklist development (fifty declarations, proving the counter-based worklist closure equal to the least closure at every append prefix), the closure development (twenty-six declarations), and the algorithm search development (nineteen declarations) — beside three new data files in the worklist examples folder carrying no declarations. The movement is five commits: twenty-eight files added, including the algorithm search example folder with its claims, objectives, recorded reports, and search and decision scripts, and the worklist example folder with its claims, data files, and recorded run output; and two files changed, the readme and the recorded check log in the proof folder, which grew at the fresh head. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88 with a full theorem-level re-census at the fresh head owed; the fresh counts stand here at delta strength.

## Watch delta — 2026-11-21, the eighty-fifth hourly re-synthesis watch

The watch re-read this repo's live head at 84eb1cd954dcc7b927c5dd42b96caa62a8784e1e in the full enumeration and read the whole tree at that head (80 files, not truncated) and at the last recorded head 1c794e29c897053658ce47e7a42cac6a712621f2 (67 files). Mechanical count at the fresh head, by the watch method (every theorem or lemma declaration in every Lean file in the tree): 362 declarations across 25 Lean files, no sorry token and no custom axiom declaration in any file. The same method at the last recorded head counted 335 declarations across 23 Lean files. Name comparison, one mechanical method both times: 27 names gained, 0 lost, so no regression is flagged. The movement is three commits landing an admission development — the claim that claims on the log need premises bound to recorded behavior: thirteen files added, two Lean files in the proof folder carrying the admission development and its controls, and an admission example folder with an Idol kernel, its controls and mutants, two replay scripts, a runner, and its recorded receipts — and one file changed, the recorded check log in the proof folder, with no file removed. In plain terms the new theorems prove the admission claims sound over grounded facts, the honest replay and reach forms, and the refusal forms by name — the fast but wrong run, the tuned-after-reveal run, the unmeasured peak, the unregistered run, the name match, and the weak comparator each fail admission for their named reason. The Idol kernel and its replays are executed evidence at their own states, not a machine-checked refinement of the Lean model. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88, with a full re-census at the fresh head owed and the fresh counts standing here at delta strength.

## Watch delta — 2026-11-22, the ninety-fourth hourly re-synthesis watch

The watch re-read this repo's live head at edbcb2a0f6c9fc9be5bb44955cf1ec96782ab628 in the full enumeration and read the whole tree at that head (93 files, not truncated) and at the last recorded head 84eb1cd954dcc7b927c5dd42b96caa62a8784e1e (80 files). The proven set grew between the heads and lost nothing: 375 theorem declarations at the fresh head against 363 at the last recorded head, counted by the watch method over the tree at each pin, with twelve names gained, none lost, and no sorry token and no axiom declaration at either head. The growth is one new Lean file in the incremental recomputation example, the cone development, carrying the twelve new theorems — the cone rule, the resume form, the withdrawal and join forms for frontiers, the pair counts, and the premise form for a missing row — beside a second new Lean file, the audit cone file, carrying no declarations, and every earlier file unchanged in its count. The movement is five commits landing incremental recomputation as a system beside the deletions, early cutoff, and resume work: thirteen files added, the whole incremental recomputation example with its specification, results record, frontier and gate modules, fixtures, receipts, and the two Lean files, with no file changed or removed. The example's recorded gate receipts are executed evidence at their own strength. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88, with a full theorem-level re-census at the fresh head owed and the fresh counts standing here at delta strength.

## Watch delta — 2026-11-22, the ninety-seventh hourly re-synthesis watch

The watch re-read this repo's live head at 2a27f6cb29f0e43e85ff5b8aa8e7722ddcd813e4 in the full enumeration and read the whole tree at that head (108 files) and at the last recorded head edbcb2a0f6c9fc9be5bb44955cf1ec96782ab628 (93 files). The proven set grew between the heads and lost nothing: 417 declarations at the fresh head against 375 at the last recorded head, counted by the watch method over the tree at each pin, with 42 names gained, none lost, and no sorry token and no axiom declaration at either head. The growth is two new Lean files in a new monotone synthesis example: the core file carrying 31 declarations and its controls file carrying 11 — the append-only admission loop development: monotonicity of the run and its steps, reachability soundness and its characterization through closure, the admission and replacement soundness forms, the refusal of retirement without cover, saturation exactness and persistence, and order independence of the reach set. The movement is four commits (two landing commits and two merges): fifteen files added — the whole example with its two Lean files, gate, generator, loop, runner, readme, and its receipts folder — and two files changed in the incremental recomputation example, its gate and its Lean check script, with no file removed. The example's recorded gate receipts are executed evidence at their own strength. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88, with a full theorem-level re-census at the fresh head owed and the fresh counts standing here at delta strength.

## Watch delta — 2026-11-22, the hundred-sixth hourly re-synthesis watch

The watch re-read this repo's live head at f13fa381fc45fa650d7f8dec5e43c0033cb18641 in the full enumeration and read the whole tree at that head (109 files, not truncated) and at the last recorded head 2a27f6cb29f0e43e85ff5b8aa8e7722ddcd813e4 (108 files). Every Lean file is byte-identical between the heads, so the proven set is unchanged: the same declaration set with the same name set at both, counted by the watch method over the tree at each pin, none gained and none lost, at the strength the earlier deltas in this annex record. The movement is one commit of incremental gate work — a shared gate version and a randomized frontier check — landing as executed work: one file added, a fuzz script in the incremental recomputation example, and two files changed, that example's readme and gate source, none of them Lean. That work is executed evidence at its own strength, counted nowhere in the proven column. The census pin stands at 1ea286488cd4fecb7edb7f5debe407db04456b88, with a full theorem-level re-census at the fresh head owed and the fresh counts standing here at delta strength.
