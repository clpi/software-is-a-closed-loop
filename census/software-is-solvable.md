# Census — software-is-solvable

## Pin and identity

- Live head (gh API, read first): `815e125f6c7fd982cd5a66c4c1f98aa0a4ea5d33`
- Clone head (shallow clone, depth 1): same — verified match.
- Visibility (gh API): private. Default branch: master (only branch). API description: none.
- Toolchain pin (lean-toolchain file): Lean 4, version 4.19.0. No Mathlib or external Lean dependency (README; imports are only the repo's own modules plus the standard library).
- Files: README (50 lines), five Lean modules (below), a check script, a check log, a sums file. All sums in the sums file verified against the clone in this census (all OK).

## Thesis, in plain English

Witness-compounding search is solvable exactly, over a finite scoped behavioral hypergraph: admitted witness atoms are roots, finite-premise transfer/composition certificates are hyperedges, and the least finite-derivation closure is monotone under appends, compounds across premises (reclosing saturated views recovers mixed-premise consequences), yields an exact per-axis resolution count with exact marginal gain, merges commutatively/associatively/idempotently, supports exact executable selection by a Boolean gate over a finite catalogue, and projects withdrawals without creating new support. Saturation, qualification colors, matrices and catalogues are derived views, not the authority.

## Controls and zero-sorries evidence

- Check script: greps all modules and rejects any sorry / admit / axiom / native-decide token, compiles each module with warnings as errors, and fails if the compiler output contains a sorry-axiom, error or warning marker.
- Check log: records a successful run on Lean 4.19.0 with per-theorem print-axioms lines (quoted below in summary form) and a final PASS line for all five modules.
- Axiom evidence source per theorem below: the check log's print-axioms lines, where the module prints them. "Not printed" means the module contains no print-axioms statement for that theorem and the log carries no line for it — no dependency is asserted here for those.
- Concrete controls: 35 kernel guards total — 29 in the test module, 6 in the executable-closure module — plus one evaluated closure example. They are executable checks, not named theorems.
- Global README claim: no custom axioms and no admitted theorems; ordinary foundational dependencies only.

## Theorem census — 48 named theorems

Token column quotes at most one load-bearing word per theorem; the plain-English column is the identification.

### Module: Qualification (closure / soundness core; 10 theorems)

| Token | Hypotheses → conclusion | Axioms (check log) |
|---|---|---|
| `least` | Any set containing all roots and closed under the rules contains every derivable atom → derivation implies membership in any such closed superset. This is the induction principle the rest use. | none |
| `closed` | No extra hypotheses → the derivation set itself is closed under the rules. | not printed |
| `monotone` | Root set grows and rule set grows (pointwise implications supplied) → every derivation in the small system is a derivation in the large one. Append preservation at this level. | none |
| `idempotent` | No extra hypotheses → deriving from already-derived atoms as roots gives exactly the original derivations (iff). | none |
| `compounding` | Two root sets under the same rules → deriving from their union equals deriving from the union of their separate derivation sets, reclosed (iff). Cross-premise compounding. | none |
| `order` (order-independence) | Two candidate saturations both contain the roots, are rule-closed, and are each sound (contained in the true derivation set) → they agree on every atom (iff). PREMISE: soundness of both candidates is assumed, not proved for an arbitrary procedure. | none |
| `soundness` | PREMISES carried: every root is semantically true, and the truth set is closed under the rules → every derivable atom is true. Truth of roots/rules is assumed, never proved. | none |
| `withdrawal` (no new support) | Live roots/rules are the originals filtered by a withdrawn set → every live derivation was already a historical derivation. Filtering creates nothing new. | none |
| `surviving` | PREMISES: a subsystem's roots and rules all remain live after withdrawal → every subsystem derivation survives in the live system. | none |
| `no_bootstrap` | **DISPROOF / impossibility.** SIDE CONDITION (premise): every rule has at least one premise. With an empty root set, no atom is derivable — cycles alone cannot create support (conclusion is a negation). | none |

Core definitions carried as premises throughout: the atom type is generic; roots are *admitted* atoms; rules are *admitted* finite-premise certificates, all premises conjunctive. Derivability is the least (finite-derivation) fixed point by construction of the inductive definition.

### Module: ExecutableClosure (exhaustive executable evaluator; 13 theorems)

Side condition on the whole module's main results: the universe list, root list and rule list must satisfy boundedness — every root is in the universe and every rule head is in the universe. Several theorems take this as explicit hypotheses; the checked wrapper enforces it (below).

| Token | Hypotheses → conclusion | Axioms (check log) |
|---|---|---|
| `subset` (members) | A list is among the enumerated subsets of the universe → each of its members is in the universe. | not printed |
| `filter` (member) | No hypotheses → filtering the universe by any predicate yields one of its enumerated subsets. | not printed |
| `subsets` (count) | No hypotheses → the number of enumerated subsets is 2 to the power of the universe length. Counts list entries. | propext only |
| `ruleOK` (exact) | No hypotheses → the Boolean rule check is true exactly when: if all premises are in the candidate set, the head is too. | not printed |
| `modelOK` (exact) | No hypotheses → the Boolean model check is true exactly when the candidate contains all roots and is rule-closed in the propositional sense. | not printed |
| `close` (exact) | Boundedness premises (roots and rule heads in universe) → membership in the executable closure list holds exactly when the atom is propositionally derivable. This is the bridge theorem. | standard three: propext, classical choice, quotient soundness |
| `closed` (closure is closed) | Boundedness premises → the executable closure set is rule-closed propositionally. | standard three |
| `contains` (roots) | Boundedness premises → every root is in the executable closure. | standard three |
| `order` (order-independence) | Boundedness for both presentations, plus premises that the two root lists and two rule lists are extensionally the same → closure membership is identical. Duplicates/reordering change nothing. | standard three |
| `monotone` (executable) | Boundedness for both, plus subset premises (small roots ⊆ large roots, small rules ⊆ large rules) → small closure membership implies large closure membership. Withdrawal is the subset case. | standard three |
| `boundedOK` (exact) | No hypotheses → the Boolean boundedness check is true exactly when the boundedness side condition (roots and heads in universe) holds. | propext, quotient soundness |
| `admitted` (checked closure) | The checked wrapper returned some output → boundedness holds and output membership is exactly propositional derivability. | standard three |
| `rejects` (checked closure) | No hypotheses → the checked wrapper returns none exactly when boundedness fails. Malformed/out-of-universe input is rejected, not vacuously qualified. Negative characterization, not a disproof of a claim. | propext, quotient soundness |

### Module: Hyperlattice (authority joins, resolution vector; 15 theorems)

Definitions carried: a graph is roots plus hyperedges over a generic atom type; joining graphs is pointwise-or of roots and of edges; knowledge is the Qualification derivation set of a graph; one graph extends another when roots and edges grow pointwise; two graphs are "same" when roots and edges are pointwise iff.

| Token | Hypotheses → conclusion | Axioms (check log) |
|---|---|---|
| `join` (extends) | No hypotheses → a graph extends into its join with any other graph. | not printed |
| `knowledge` (monotone) | Extension premise → knowledge of the smaller graph is contained in knowledge of the larger. | not printed |
| `same` (knowledge) | Sameness premise → the two graphs have identical knowledge (iff). | not printed |
| `join` (commutative) | No hypotheses → joining in either order gives same graphs. | not printed |
| `join` (associative) | No hypotheses → join association gives same graphs. | not printed |
| `duplicate` | No hypotheses → joining a graph with itself is same as the graph. Idempotence of merge; repeats add no support. | not printed |
| `compounding` | No hypotheses → knowledge of a join equals knowledge of the join of the two *saturated* graphs (each graph's roots replaced by its knowledge), **reclosed** (iff). Merely unioning old closures is not the claim and would lose mixed-premise consequences. Headline result. | none |
| `redundant` | PREMISES: every root of the appended graph is already known in the old graph, and old knowledge is closed under the appended graph's edges → joining changes knowledge not at all (iff). | none |
| `count` (monotone) | Pointwise premise: wherever the first classifier holds on the list, the second holds → first count ≤ second count. | not printed |
| `count` (strict) | Monotonicity premise plus a novel-witness premise (some listed element newly true under the second classifier) → first count < second count. | not printed |
| `count` (strict iff) | Monotonicity premise → strict increase holds exactly when a novel witness exists in the list. | not printed |
| `count` (delta) | Monotonicity premise → old count plus (new minus old) equals new count. Exact marginal gain / telescoping. | not printed |
| `expansion` (vector) | Extension premise, plus PREMISE that both Boolean classifiers are *exact* for their graphs (true exactly on knowledge) → every resolution coordinate (count of supported probes per axis) is nondecreasing. | propext, quotient soundness |
| `strict` (expansion) | Same extension + exactness premises, plus a novel-witness premise for the named axis (a probe newly known after extension) → that coordinate strictly increases. | propext, quotient soundness |
| `live` (supported) | No extra hypotheses → knowledge of the live projection (roots/edges filtered by dead sets) is contained in knowledge of the original graph. Projection creates no support. | not printed |

Also defined, not theorems: the resolution function (per-axis probe counts), exactness as a proposition, the live projection, and the qualification color code (unknown 0, positive-only 1, negative-only 2, conflict 3, by adding 1 for positive and 2 for negative support).

### Module: WitnessExecutable (executable batches, catalogue, qualification; 10 theorems)

Definitions carried: a batch is a list of roots plus a list of edges; its authority graph is membership in those lists; appending batches concatenates the lists; classification of an atom is membership in the executable closure.

| Token | Hypotheses → conclusion | Axioms (check log) |
|---|---|---|
| `append` (exact) | No hypotheses → the authority of an appended batch is same as the join of the two authorities. | not printed |
| `classifier` (exact) | Boundedness premises (batch roots and edge heads in universe) → the executable classifier is exact for the batch's authority graph (true exactly on knowledge). | standard three |
| `append` (resolution) | Boundedness premises for the appended batch → every resolution coordinate after append is ≥ before. Executable form of append preservation, including rule-only novelty. | standard three |
| `configuration` (count) | No hypotheses → catalogue length is 2 to the power of the closure-list length. Counts entries; distinct subsets only if the closure list has no duplicates. | propext only |
| `count` (equals filter) | No hypotheses → the recursive count of a predicate over a list equals the length of the filtered list. | not printed |
| `count` (congruence) | Premise: two predicates agree on every listed element → their counts are equal. | not printed |
| `classified` (count) | No hypotheses → counting the classifier over the universe equals the closure-list length. | not printed |
| `catalogue` (compounding) | Boundedness premises for the appended batch → catalogue entries after append equal entries before times 2 to the power of the closure-length delta. Exact append multiplier; a duplicate append has delta 0 and multiplier 1. SIDE CONDITION: this is entry count *before* any qualification filter. | standard three |
| `qualification` (exact) | No hypotheses → a configuration is in the qualified list exactly when it is in the catalogue and the named total Boolean gate is true on it. The gate itself is a supplied premise (arbitrary total Boolean function); its correctness is not proved. | propext only |
| `projection` (supported) | No hypotheses → knowledge under the live projection of a batch (dead roots/edges filtered out) is contained in knowledge under the original batch. | propext only |

Also defined, not theorems: incidence (a premise atom occurs in an edge) and interaction (two atoms co-occur in some edge's premises) — Boolean derived views.

### Module: WitnessTests (controls, 0 theorems)

29 kernel guards by direct computation, covering: cross-premise synergy (atoms derivable only from the combined batch), rule-only append novelty, duplicate/already-derived appends changing nothing, per-axis resolution values before/after, catalogue sizes 2 → 16 in the example and unchanged under duplicate append, gate filtering (8 of the catalogue pass the example gate), negative support turning a positive color 1 into conflict color 3, a cycle collapsing to empty once its sole origin is projected out while the historical result is unchanged, an independent second origin preserving a conclusion after the first is withdrawn, removing a transfer retracting its downstream consequence, malformed domains rejected (checked wrapper returns none), a solitary cycle with no roots closing to empty, and qualification empty under an everywhere-false gate.

## Disproofs flagged

- The `no_bootstrap` theorem in Qualification is the one named impossibility/disproof: under the side premise that every rule needs ≥1 premise, an empty root set derives nothing — self-supporting cycles are disproved as a source of support.
- No other named theorem is a disproof of an external claim. The checked-wrapper rejection theorem and the test guards (solitary cycle → empty, malformed → none) are negative characterizations/controls, flagged as such above, not disproofs.

## Premises carried rather than proven (consolidated)

1. Admission: roots and hyperedges are *admitted* — admission, authentication and correct encoding are prerequisites (README trust boundary), not proved.
2. Atom binding: production atoms must bind content, lineage, scope, venue/environment, harness, premises and polarity — required by contract, not enforced by the generic type.
3. Soundness premises: roots are true and rules preserve truth — assumed in the soundness theorem.
4. Exactness premises: resolution monotonicity/strictness assume the Boolean classifiers are exact for their graphs; the executable classifier's exactness is proved only under boundedness (roots/heads in universe).
5. Boundedness side condition for every executable-closure bridge result (see above).
6. The qualification gate is supplied and arbitrary; only selection exactness is proved.
7. Withdrawal input is an already-resolved dead-root/dead-edge projection; authorization, event-identity conflicts and timestamp policy belong to admission (README).
8. Probe discipline: probes are precisely specified support obligations; coordinate labels/probes must stay fixed across a comparison; new axis domains need an explicit embedding/comparison policy (README). Repeated probes act as multiplicity weights, distinct probes for cardinality.

## Explicit NON-CLAIMS / boundaries (README)

- The resolution vector is a lower bound on resolved support in the named probe scopes. It does **not** measure remaining runtime, probabilistic confidence, or a guaranteed count of feasible software designs.
- The catalogue count is not a claim that every subset is executable, composable, qualified or optimal; the gated result may shrink or be empty. No theorem assumes exponential growth on every append.
- A Merkle commitment can identify the hypergraph object; hashing is **not** itself a proof of semantic equivalence.
- Positive/negative colors are information statuses, not a numeric quality ordering. History is append-only; live eligibility is deliberately not monotone.
- Reference enumeration is executable and terminating but exponentially expensive; it is an oracle/specification for optimized worklists. **No production performance win is claimed.**
- Recording a claim does not make it true; semantic truth follows only from valid roots and truth-preserving rules.
- A native egraph, ledger, database, compiler, telemetry adapter, external solver or deployed release is **not** verified merely because it can emit this model.
- Two modules are stated as reused from a sibling project (the closure/soundness core and the exhaustive evaluator).
