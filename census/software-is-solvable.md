# Census — software-is-solvable — refresh draft

Census date: 2026-11-18, ~02:10–02:40 PST. Method: live head read first via the gh route, shallow clone (depth 1), clone head verified equal, every file read; checksums verified in the clone; shared-module byte identity re-checked by checksum against the optimality sibling at its current head. Clone read only, never edited. This draft replaces the census of the older pin; changes are marked in the Delta section.

## Pin and identity

- Old census pin: `815e125f6c7fd982cd5a66c4c1f98aa0a4ea5d33` — 48 named theorems plus 35 kernel guards.
- Live head (default branch `master`): `5bbceee7e4270d838115dbfc8fb218ebee641638`. Clone head matches exactly. Head commit subject, plainly: add a checked before-and-after example for restore evidence.
- Visibility: private. Default branch: master.
- Toolchain pin: Lean 4.19.0. No external Lean dependency (imports are the repo's own modules plus the standard library).
- Files: the readme (unchanged length), the same five Lean modules, the check script, the recorded check log, the sums file — plus a new worked-examples folder. All sums in the sums file verified against the clone in this census (all OK). Theorem total in tree: **51** (48 library, unchanged; 3 in the new worked example).

## Delta (old pin to this pin)

- **The library is unchanged in substance.** Same five modules, same 48 named theorems with the same names and the same per-module counts (10, 13, 15, 10, and the guard module), same 35 kernel guards in the same split (29 in the test module, 6 in the executable-closure module), same recorded axiom lines in the check log, same readme. Every carried-forward section below therefore stands as written in the old census.
- **The only addition is a worked example.** A new examples folder carries one standalone proof file (3 theorems) applying the repo's closure machinery to a minimum-cost restore plan, with its own readme, runner, recorded verification transcript, and a rejected control. Censused at the end.
- **Shared-module byte identity re-checked at the new pins: still identical.** The two modules this repo shares with the optimality sibling were checksum-compared against that sibling's clone at its current head (`b52c3170a6e108345bd5ada44ca7355dae55b395` — the sibling's live head at clone time in this refresh; the refresh brief named an earlier prefix for it). Both files are byte-identical across the two repos at these pins (checksums equal, computed in this census). The old census's at-old-pin note is hereby refreshed, not merely carried.

## Thesis, in plain English — carried forward, still true

Witness-compounding search is solvable exactly, over a finite scoped behavioural hypergraph: admitted witness atoms are roots, finite-premise transfer and composition certificates are hyperedges, and the least finite-derivation closure is monotone under appends, compounds across premises (reclosing saturated views recovers mixed-premise consequences), yields an exact per-axis resolution count with exact marginal gain, merges commutatively, associatively, and idempotently, supports exact executable selection by a boolean gate over a finite catalogue, and projects withdrawals without creating new support. Saturation, qualification colours, matrices, and catalogues are derived views, not the authority.

## Controls and zero-sorries evidence — carried forward, re-verified

- Check script: greps the root modules and rejects any sorry, admit, axiom, or native-decision token, compiles each module with warnings as errors, and fails if the compiler output contains a sorry-axiom, error, or warning marker. (Scope note: the script greps the root-level modules; the worked example has its own runner.)
- Check log: records a successful run on Lean 4.19.0 ending in the pass line for all five modules, with per-theorem axiom lines (28 printed theorems; summary below in the census).
- Concrete controls: 35 kernel guards total — 29 in the test module, 6 in the executable-closure module — plus one evaluated closure example. Re-counted in this census; unchanged.
- This census independently re-ran the token search over the whole tree, examples included: no escape-hatch tokens anywhere.
- Global readme claim: no custom axioms and no admitted theorems; ordinary foundational dependencies only.

## Theorem census — 48 named theorems (carried forward; names re-verified in the clone)

Token column quotes at most one load-bearing word per theorem; the plain-English column is the identification. Axiom evidence: the check log's printed lines, where the module prints them.

### Module: Qualification (closure and soundness core; 10 theorems)

| Token | Hypotheses to conclusion | Axioms (check log) |
|---|---|---|
| `least` | Any set containing all roots and closed under the rules contains every derivable atom. The induction principle the rest use. | none |
| `closed` | The derivation set itself is closed under the rules. | not printed |
| `monotone` | Root set and rule set grow (pointwise implications supplied), so every derivation in the small system is a derivation in the large one. | none |
| `idempotent` | Deriving from already-derived atoms as roots gives exactly the original derivations (equivalence). | none |
| `compounding` | Deriving from the union of two root sets equals deriving from the union of their separate derivation sets, reclosed (equivalence). Cross-premise compounding. | none |
| `order` (order-independence) | Two candidate saturations that contain the roots, are rule-closed, and are each sound (contained in the true derivation set) agree on every atom. Premise: soundness of both candidates is assumed, not proved for an arbitrary procedure. | none |
| `soundness` | Premises carried: every root is semantically true, and the truth set is closed under the rules — then every derivable atom is true. Truth of roots and rules is assumed, never proved. | none |
| `withdrawal` (no new support) | Live roots and rules are the originals filtered by a withdrawn set, so every live derivation was already a historical derivation. Filtering creates nothing new. | none |
| `surviving` | Premises: a subsystem's roots and rules all remain live after withdrawal — then every subsystem derivation survives in the live system. | none |
| `no_bootstrap` | Disproof (impossibility). Side premise: every rule has at least one premise. With an empty root set, no atom is derivable — cycles alone cannot create support (the conclusion is a negation). | none |

Core definitions carried as premises throughout: the atom type is generic; roots are admitted atoms; rules are admitted finite-premise certificates, all premises conjunctive. Derivability is the least finite-derivation fixed point by construction of the inductive definition.

### Module: ExecutableClosure (exhaustive executable evaluator; 13 theorems)

Side condition on the module's main results: boundedness — every root is in the universe list and every rule head is in the universe list. Several theorems take this as explicit hypotheses; the checked wrapper enforces it.

| Token | Hypotheses to conclusion | Axioms (check log) |
|---|---|---|
| `subset` (members) | A list among the enumerated subsets of the universe has all its members in the universe. | not printed |
| `filter` (member) | Filtering the universe by any predicate yields one of its enumerated subsets. | not printed |
| `subsets` (count) | The number of enumerated subsets is 2 raised to the universe length (list entries counted). | one standard axiom |
| `ruleOK` (exact) | The boolean rule check is true exactly when: if all premises are in the candidate set, the head is too. | not printed |
| `modelOK` (exact) | The boolean model check is true exactly when the candidate contains all roots and is rule-closed in the propositional sense. | not printed |
| `close` (exact) | Boundedness premises, then membership in the executable closure list holds exactly when the atom is propositionally derivable. The bridge theorem. | standard three |
| `closed` (closure is closed) | Boundedness premises, then the executable closure set is rule-closed propositionally. | standard three |
| `contains` (roots) | Boundedness premises, then every root is in the executable closure. | standard three |
| `order` (order-independence) | Boundedness for both presentations, plus the two root lists and two rule lists extensionally equal — then closure membership is identical. | standard three |
| `monotone` (executable) | Boundedness for both, plus subset premises on roots and rules — then small closure membership implies large. Withdrawal is the subset case. | standard three |
| `boundedOK` (exact) | The boolean boundedness check is true exactly when the boundedness side condition holds. | two of the standard three |
| `admitted` (checked closure) | The checked wrapper returned some output, so boundedness holds and output membership is exactly propositional derivability. | standard three |
| `rejects` (checked closure) | The checked wrapper returns none exactly when boundedness fails. Malformed input is rejected, not vacuously qualified. A negative characterisation, not a disproof of a claim. | two of the standard three |

### Module: Hyperlattice (authority joins, resolution vector; 15 theorems)

Definitions carried: a graph is roots plus hyperedges over a generic atom type; joining graphs is pointwise-or of roots and of edges; knowledge is the Qualification derivation set of a graph; extension and sameness are pointwise.

| Token | Hypotheses to conclusion | Axioms (check log) |
|---|---|---|
| `join` (extends) | A graph extends into its join with any other graph. | not printed |
| `knowledge` (monotone) | Extension premise, then knowledge of the smaller graph is contained in knowledge of the larger. | not printed |
| `same` (knowledge) | Sameness premise, then the two graphs have identical knowledge (equivalence). | not printed |
| `join` (commutative) | Joining in either order gives same graphs. | not printed |
| `join` (associative) | Join association gives same graphs. | not printed |
| `duplicate` | Joining a graph with itself is same as the graph. Repeats add no support. | not printed |
| `compounding` | Knowledge of a join equals knowledge of the join of the two saturated graphs, reclosed (equivalence). Merely unioning old closures is not the claim and would lose mixed-premise consequences. Headline result. | none |
| `redundant` | Premises: every root of the appended graph is already known in the old graph, and old knowledge is closed under the appended graph's edges — then joining changes knowledge not at all (equivalence). | none |
| `count` (monotone) | Wherever the first classifier holds on the list, the second holds — then the first count is at most the second. | not printed |
| `count` (strict) | The monotonicity premise plus a novel-witness premise — then the first count is strictly below the second. | not printed |
| `count` (strict, exact form) | Monotonicity premise, then strict increase holds exactly when a novel witness exists in the list. | not printed |
| `count` (delta) | Monotonicity premise, then old count plus (new minus old) equals new count. Exact marginal gain. | not printed |
| `expansion` (vector) | Extension premise, plus the premise that both boolean classifiers are exact for their graphs — then every resolution coordinate is nondecreasing. | two of the standard three |
| `strict` (expansion) | Same premises, plus a novel-witness premise for the named axis — then that coordinate strictly increases. | two of the standard three |
| `live` (supported) | Knowledge of the live projection (roots and edges filtered by dead sets) is contained in knowledge of the original graph. Projection creates no support. | not printed |

Also defined, not theorems: the resolution function, exactness as a proposition, the live projection, and the qualification colour code (unknown 0, positive-only 1, negative-only 2, conflict 3).

### Module: WitnessExecutable (executable batches, catalogue, qualification; 10 theorems)

Definitions carried: a batch is a list of roots plus a list of edges; its authority graph is membership in those lists; appending batches concatenates the lists; classification of an atom is membership in the executable closure.

| Token | Hypotheses to conclusion | Axioms (check log) |
|---|---|---|
| `append` (exact) | The authority of an appended batch is same as the join of the two authorities. | not printed |
| `classifier` (exact) | Boundedness premises, then the executable classifier is exact for the batch's authority graph. | standard three |
| `append` (resolution) | Boundedness premises for the appended batch, then every resolution coordinate after append is at least the coordinate before. | standard three |
| `configuration` (count) | Catalogue length is 2 raised to the closure-list length (entries counted; distinct subsets only if the closure list has no duplicates). | one standard axiom |
| `count` (equals filter) | The recursive count of a predicate over a list equals the length of the filtered list. | not printed |
| `count` (congruence) | Premise: two predicates agree on every listed element — then their counts are equal. | not printed |
| `classified` (count) | Counting the classifier over the universe equals the closure-list length. | not printed |
| `catalogue` (compounding) | Boundedness premises, then catalogue entries after append equal entries before times 2 raised to the closure-length delta. Side condition: entry count before any qualification filter; a duplicate append has delta 0 and multiplier 1. | standard three |
| `qualification` (exact) | A configuration is in the qualified list exactly when it is in the catalogue and the named total boolean gate is true on it. The gate itself is a supplied premise (an arbitrary total boolean function); its correctness is not proved. | one standard axiom |
| `projection` (supported) | Knowledge under the live projection of a batch is contained in knowledge under the original batch. | one standard axiom |

Also defined, not theorems: incidence and interaction as boolean derived views.

### Module: WitnessTests (controls, 0 theorems) — carried forward

29 kernel guards by direct computation, covering: cross-premise synergy, rule-only append novelty, duplicate and already-derived appends changing nothing, per-axis resolution values before and after, catalogue sizes in the example and under duplicate append, gate filtering, negative support turning a positive colour into the conflict colour, a cycle collapsing to empty once its sole origin is projected out while the historical result is unchanged, an independent second origin preserving a conclusion after the first is withdrawn, removing a transfer retracting its downstream consequence, malformed domains rejected, a solitary cycle with no roots closing to empty, and qualification empty under an everywhere-false gate.

### Worked example: minimum-cost restore qualification (3 theorems) — new at this pin

A standalone example in the examples folder. An immutable snapshot is already recorded; a checksum plus the snapshot derives integrity; integrity plus replay evidence derives restorability. Three purchasable checks cost 3, 5, or 6 units; one combined run supplies both missing roots. It proves: the minimum cost of a successful plan is 6 units, checked by the kernel against every subset of the purchasable checks under the repo's bounded closure (one quoted name: `minimum`); the before-and-after computation (8 work units in two separate tests, down to 6 in one combined run, with the derived fact list as stated); and that reclosure matters — unioning the two precomputed closures misses the mixed-premise derivations, so a checksum alone cannot establish restorability. The example transcript records all three theorems with **no axiom dependencies**, and a rejected control (removing replay as a restore prerequisite fails). Its own scope note: the three prices and the transfer rules are declared fixture inputs; applying the conclusion to a real backup system requires justified rules, scoped receipts, and the actual test menu.

## Disproofs flagged — carried forward

- The no-bootstrap theorem in Qualification is the one named impossibility: under the side premise that every rule needs at least one premise, an empty root set derives nothing — self-supporting cycles are disproved as a source of support.
- No other named theorem is a disproof of an external claim. The checked-wrapper rejection theorem and the test guards (solitary cycle to empty, malformed to none) are negative characterisations and controls, flagged as such, not disproofs. The new example's reclosure fact is a boundary fact of the same kind.

## Premises carried rather than proven (consolidated) — carried forward, still true

1. Admission: roots and hyperedges are admitted — admission, authentication, and correct encoding are prerequisites (the readme trust boundary), not proved.
2. Atom binding: production atoms must bind content, lineage, scope, venue and environment, harness, premises, and polarity — required by contract, not enforced by the generic type.
3. Soundness premises: roots are true and rules preserve truth — assumed in the soundness theorem.
4. Exactness premises: resolution monotonicity and strictness assume the boolean classifiers are exact for their graphs; the executable classifier's exactness is proved only under boundedness.
5. Boundedness side condition for every executable-closure bridge result.
6. The qualification gate is supplied and arbitrary; only selection exactness is proved.
7. Withdrawal input is an already-resolved dead-root and dead-edge projection; authorisation, event-identity conflicts, and timestamp policy belong to admission (readme).
8. Probe discipline: probes are precisely specified support obligations; coordinate labels and probes must stay fixed across a comparison; new axis domains need an explicit embedding or comparison policy (readme). Repeated probes act as multiplicity weights.

## Explicit non-claims and boundaries (readme) — carried forward, still true

- The resolution vector is a lower bound on resolved support in the named probe scopes. It does not measure remaining runtime, probabilistic confidence, or a guaranteed count of feasible designs.
- The catalogue count is not a claim that every subset is executable, composable, qualified, or optimal; the gated result may shrink or be empty. No theorem assumes exponential growth on every append.
- A hash commitment can identify the hypergraph object; hashing is not itself a proof of semantic equivalence.
- Positive and negative colours are information statuses, not a numeric quality ordering. History is append-only; live eligibility is deliberately not monotone.
- Reference enumeration is executable and terminating but exponentially expensive; it is an oracle and specification for optimised worklists. No production performance win is claimed.
- Recording a claim does not make it true; semantic truth follows only from valid roots and truth-preserving rules.
- A native graph engine, ledger, database, compiler, telemetry adapter, external solver, or deployed release is not verified merely because it can emit this model.
- Two modules are stated as reused from a sibling project (the closure core and the exhaustive evaluator) — and at this pin they remain byte-identical to that sibling's copies, per the Delta.
