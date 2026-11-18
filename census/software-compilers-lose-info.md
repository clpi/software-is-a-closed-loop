# Census — software-compilers-lose-info

## Pin and identity

- Live head (gh API, read first): `f531e31a4e647461a28228e4b9d64f40d1782908`
- Clone head (full clone, history present): same — verified match.
- Visibility (gh API): private. Default branch: master (only branch). API description: the full proof of the topological thesis — conventional compilation provably loses the derivation structure; derivation-carrying compilation loses nothing.
- Toolchain pin (toolchain file): Lean 4, version 4.19.0.
- Files: a thesis document (118 lines), an implications document (89 lines), a readme (38 lines), six root Lean modules plus an audit module and an umbrella module, a check script, a recorded check log (14 lines), and an examples folder added at this head (one example module, its own readme, its own check script, a recorded verification transcript). No sums file in this repo. No Mathlib anywhere: the root modules import only each other; the example module imports the standard library only.
- History: four commits. The earlier reported head `e54db425ec890d2bf39e5f9fa6f2da18e3910cf7` is the third commit. The only change since that head is the fourth commit, which adds the examples folder (four new files, 86 lines, nothing else touched). Every proof module, the check script, and the recorded check log are byte-identical between the two heads, so the earlier report's theorem-level findings carry over unchanged; the axiom count correction in the controls section below applies to both heads.

## Thesis in plain English

Conventional compilation provably loses derivation structure, and derivation-carrying compilation loses nothing. A program is a derivation structure: a directed hypergraph whose nodes derive by a least fixed point closure. From a program two things are read off — its behavior (which nodes derive) and its topology (which nodes reach which, so each node's premise cone). The pair is the qualified quotient. The conventional compiler's artifact keeps the behavior and forgets the topology: two concrete programs with the same behavior and different premise cones share one artifact, and no function of that artifact can return each program's own quotient, so recovery is impossible in general, not merely unimplemented. The carrying compiler's artifact has the behavior and the topology as its own components: the quotient is read back off the artifact exactly, premise cones read from the artifact are the source's cones exactly, and the topology of a merge is exactly the transitive closure of the union of the two topologies. The halves meet: two programs have the same carried artifact if and only if they agree on the qualified quotient.

## Controls and zero-sorries evidence

- Gate evidence state: this census did not run the build. Everything in this section is the repo's own recorded log and scripts, read at the pin.
- Check script: scans every root-level Lean file and rejects any sorry, admit, axiom, or native-decide token (word-boundary scan, so the audit module's print-axioms lines and ordinary words like "admits" in comments do not trip it); compiles each module with warnings as errors; fails on any sorry-axiom, error, or warning output. The scan covers the root modules only — the examples folder is not covered by this script and has its own, weaker check script (compile with warnings as errors, no escape scan).
- This census's own word-boundary scan over every Lean file in the clone, examples included: no sorry, admit, axiom, or native-decide token anywhere.
- Recorded check log: 14 lines, one print-axioms line for each of the 14 audited headline results (the audit module's list). Of the 14: ten depend on no axioms at all, and four depend on propext and quotient soundness only. No audited result depends on classical choice, and none on any custom axiom. Correction to the earlier report: the brief for this census relayed "nine headline results axiom-free"; the recorded log at both heads shows ten axiom-free of fourteen. The log is the evidence; the count is ten.
- The remaining 19 named theorems are not in the audit module's print list, so the recorded log states no axiom dependencies for them: their axiom state from recorded evidence is unknown, not axiom-free.
- The example module has its own recorded verification transcript: Lean 4.19.0, the computed list of four carried quotes all folding to the same price with distinct origin pairs, print-axioms lines for its four theorems (three axiom-free, one on propext only), and a rejected control — a mutation discarding the independently chosen shipping origin is recorded as rejected with exit 1.

## Definitions carried

- Program (one token: `Hypergraph`): a root predicate and a family of hyperedges, each a premise list concluding in one node, over a node type. The family's existing form, restated here, not re-derived.
- Derivation: a node derives when it is a root or some hyperedge's premises all derive — the least fixed point of the positive Horn rules, as an inductive predicate.
- Reachability: one node reaches another when it occurs in a premise list on a chain of hyperedges concluding at the other, closed under reflexivity and transitivity. Firing a hyperedge still requires all premises; this relation is for scoping and provenance only.
- Premise cone of a node: the set of nodes reaching it.
- Qualified quotient (one token: `qual`): the pair of behavior and topology. Agreement of two programs is equality of their quotients.
- Forgetting compiler (one token: `forget`): the artifact is the behavior alone; the topology is discarded. This is the conventional compiler, modeled at exactly the quotient the loss is measured against.
- Carried artifact: a structure with behavior and topology as its own two components. Carrying compiler (one token: `carry`): the projection sending a program to the artifact whose components are its own behavior and topology. Recovery reading: the pair formed from an artifact's two components.
- Recoverable: a compiler and a quotient map are in this relation when some function of the artifact returns every source's own quotient.
- Merge: pointwise union of roots and of hyperedges. Information order: pointwise inclusion of roots and of hyperedges.
- Premise shape for a join semilattice: a structure bundling an order, a join operation, and the three join laws as fields. It is a premise shape, not a claim; see the premises section.
- Relation join: either of two relations holding, closed under transitivity — the transitive closure of the union of two relations.

## Theorem census — 33 named theorems in the root modules, plus 4 in the example

Token column quotes at most one load-bearing word per theorem. Axioms column gives the recorded check log where the theorem is in the audit list; theorems outside the audit list are marked as not printed in the recorded log.

### Basic module — order and merge (5 theorems, plus one construction)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `refl` | No hypotheses → every program is below itself in the information order. | not printed in the recorded log |
| `trans` | One program is below a second and the second below a third → the first is below the third. | not printed in the recorded log |
| `left` | No hypotheses → the first of two programs is below their merge. | not printed in the recorded log |
| `right` | No hypotheses → the second of two programs is below their merge. | not printed in the recorded log |
| `least` | A program is above both parts → it is above their merge. Merge is the least upper bound of its parts under the information order. | none |

Plus a construction, not a theorem: the premise shape for a join semilattice is instantiated for programs under the information order with merge as the join, from the three theorems above (left, right, least). Token: `join`.

### Loss module — the forgetting compiler loses the quotient (12 theorems)

The concrete universe has two nodes: a base and a top. In the first program both nodes are roots and there are no hyperedges; in the second the base is a root and the top derives through a hyperedge whose only premise is the base. Both programs have the same behavior (both nodes derive); their premise cones for the top differ.

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `loss` | General loss lemma: two sources share one artifact and their quotients differ → no recovery map exists for that compiler and quotient. **Negation theorem.** | none |
| `edge` | No hypotheses → the second program has the hyperedge from the base list to the top. Supporting fact. | not printed in the recorded log |
| `direct` | No hypotheses → every node derives in the first program. Supporting fact. | not printed in the recorded log |
| `base` | No hypotheses → the base derives in the second program. Supporting fact. | not printed in the recorded log |
| `top` | No hypotheses → the top derives in the second program, through the hyperedge. Supporting fact. | not printed in the recorded log |
| `linked` | No hypotheses → every node derives in the second program. Supporting fact. | not printed in the recorded log |
| `forget` | No hypotheses → the forgetting artifacts of the two programs are equal. The concrete distinguishing pair shares one artifact. | not printed in the recorded log |
| `reaches` | No hypotheses → in the second program the base reaches the top. Supporting fact. | not printed in the recorded log |
| `self` | A reachability fact in the first program → its endpoints are equal: nothing in the first program reaches anything but itself. Supporting fact. | not printed in the recorded log |
| `ne` | No hypotheses → the two programs' qualified quotients are unequal: the topology differs. **Negation result** — the pair genuinely disagrees on the quotient. | not printed in the recorded log |
| `injective` | No hypotheses → there exist two programs that do not agree on the quotient and whose forgetting artifacts are equal. Non-injectivity on the qualified quotient, stated as such. | propext, quotient soundness |
| `recovery` | No hypotheses → no recovery map exists for the forgetting compiler over this universe. **Negation theorem** — exact provenance is not a function of the conventional artifact. | propext, quotient soundness |

### Preservation module — the carrying compiler loses nothing (10 theorems)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `recovers` | No hypotheses → reading the quotient back off a carried artifact returns the program's own quotient, by definition. Recovery is a retraction on the quotient. | none |
| `recoverable` | No hypotheses → the carrying compiler admits recovery of the qualified quotient. The positive counterpart of the loss module's negation theorem. | none |
| `exact` | No hypotheses → the premise cone read from a carried artifact equals the source's premise cone, by definition. | none |
| `left` | A node derives in the first of two programs → it derives in their merge. One direction only, and stated so; see the open scoping in the non-claims. | not printed in the recorded log |
| `right` | A node derives in the second of two programs → it derives in their merge. One direction only. | not printed in the recorded log |
| `left` | One node reaches another in the first program → it reaches it in the merge. Reachability is monotone under merge, from either side. | not printed in the recorded log |
| `right` | One node reaches another in the second program → it reaches it in the merge. | not printed in the recorded log |
| `edges` | No hypotheses → the hyperedges of a merge are exactly the union of the parts' hyperedges, by definition. | not printed in the recorded log |
| `merge` | No hypotheses → reachability in a merge holds exactly when the relation join of the two reachabilities holds: the topology of a merge is exactly the transitive closure of the union of the two topologies. Both directions proven. | none |
| `commutes` | No hypotheses → the topology of carrying a merge equals the relation join of the carried topologies: merging first and compiling second yields the same topology as compiling first and joining second. Joins commute at the topology only. | propext, quotient soundness |

### Completeness module — the halves meet (2 theorems)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `iff` | No hypotheses → two programs have the same carried artifact if and only if their qualified quotients are equal. The carried artifact determines the source up to exactly the qualified quotient, in both directions. | none |
| `agree` | No hypotheses → two programs have the same carried artifact if and only if they agree on the qualified quotient. The same statement in the quotient's own terms. | not printed in the recorded log |

### Implications module — proven corollaries (4 theorems)

| Token | Hypotheses → conclusion | Axioms (recorded log) |
|---|---|---|
| `factor` | Premises: a compiler factors through a second map (some function of the second map's output gives the compiler's artifact for every source), and the second map admits no recovery of the quotient → the compiler admits no recovery either, whatever its artifact type. Any compiler factoring through a lossy one inherits the loss. **Negation theorem.** | none |
| `foreign` | Premise: an artifact map on programs factors through the behavior alone (some function of the forgetting artifact gives it for every source) → it admits no recovery of the qualified quotient. The impossibility direction for foreign toolchains. **Negation theorem.** | propext, quotient soundness |
| `certification` | No hypotheses → the qualified quotient is recoverable from the carried artifact (restated from the preservation module as the corollary it carries): a certificate over the quotient is checked against the artifact alone, never re-derived from source. | none |
| `cone` | No hypotheses → the premise cone read from a carried artifact equals the source's cone (restated from the preservation module): the cone a revalidation or a test selection runs over is available, exactly, from the artifact. | none |

### Example module — minimum provenance for a folded quote (4 theorems, added at this head)

A price has a tariff, a shipping charge, and two origin flags saying whether each came from an imported source. The emitted price is the sum; all four origin combinations in the fixture fold to the same emitted price. Evidence: the example's own recorded verification transcript, not the root check log.

| Token | Hypotheses → conclusion | Axioms (recorded transcript) |
|---|---|---|
| `loss` | No hypotheses → no decoder from the emitted price alone returns the origin pair for every price. **Negation theorem.** | none |
| `impossible` | For every freely chosen one-bit tag and every decoder from price and tag → the decoder does not return the origin pair for every price: even a one-bit side channel is insufficient on this output fiber. **Negation theorem.** | propext |
| `suffice` | No hypotheses → carrying the emitted price together with the origin pair returns both, for every price: two side bits suffice. | none |
| `origins` | No hypotheses → the four origin combinations carry to four distinct carried values (checked by computation). | none |

## Premises carried rather than proven (consolidated)

1. Cited family results, used as premises at their home pins and re-proven nowhere here (thesis document): the closure semantics and the hypergraph form, and the exactness of premise-cone-scoped revalidation over the hypergraph, from the optimality sibling at pin `78b7b99b26ca241ac7a8964f2a4848489978c727`; finiteness of the qualified space, the witness fold, and the coloring under its one side condition, from the quantifiable sibling at pin `a21c7c56fa028f32014dd795b35b14f688e8fdf1`. The compiler-level corollaries proven here are only that the cone and the quotient are available, exactly, from the carried artifact; the revalidation exactness itself stays at its stronger home.
2. The coverage premise of the quantifiable sibling — that sensing mediates every execution — is a named premise there and is untouched here; nothing in this repo discharges it.
3. The general foundation claim — the states of arbitrary software under the information order form a join semilattice with merge as the join — enters only as a labeled premise shape (a structure definition in the basic module). No theorem in this repo takes it as a hypothesis or depends on the general form. What is proven here is only the model-level instance: over hypergraphs under pointwise inclusion, merge is the least upper bound.
4. The thesis document's own split, carried exactly: the statement of the thesis is settled intent as a claim; its formalization is verified per the readme's evidence table (loss, preservation, and completeness each marked verified with the gate green). The implications document's split is likewise carried exactly in the next section.

## Non-claims carried

1. **Open scoping — merge behavior (flagged, one direction only).** The behavior of a merge is NOT the join of the behaviors. Derivation under merge is proven in one direction only (a node deriving in either part derives in the merge); a merge can derive more than either part, through hyperedges that mix the two, and its behavior is the closure of the merged graph, always read off the carried graph of the actual merged program, never synthesized from the parts' behaviors. Only the topology commutes with the join, exactly, in both directions.
2. The thesis is about information, not cost: it does not show carrying is cheap, that a carried artifact is small, or that any particular Idol build already emits carried artifacts.
3. A conventional artifact is not claimed useless: it determines the behavior exactly. The loss is measured against the qualified quotient and is exactly the topology.
4. Proven corollaries versus proposals (implications document, carried exactly): four implications are proven corollaries — cone-exact revalidation at the compiler level, test selection as premise cones (same citation split: cone exactness here, revalidation exactness at its stronger home), certification without reconstruction, and the foreign-toolchain impossibility. The rest are proposals with closing conditions, not theorems: that witnesses in the implementation are definitional rather than recovered (closes when a named build's emitted artifact is shown at a pin to carry the derivation records its surfaces read), and that debug and profile information are projections of the one graph rather than side channels (a design statement; closes when the implementation produces them as projections, checked at a pin). Neither proposal is asserted as an implementation fact.
5. The general join-semilattice claim over all software states remains an open spec point at its home in the monotonicity program's living spec; it is not closed here and no theorem here depends on it.
