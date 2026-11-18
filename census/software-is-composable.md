# Census — software-is-composable (clpi) — refresh draft

Census date: 2026-11-18, ~02:10–02:40 PST. Method: live head read first via the gh route, shallow clone (depth 1), clone head verified equal to the live head at clone time, every file read. Clones read only, never edited. This draft replaces the census of the older pin; what is still true is carried forward and every change is marked in the Delta section.

## Pins

- Old census pin: `033c12c01299a9b28983bee410c230641adc7d1e` (94 theorems in tree: 49 own, 45 copied, plus the imported finiteness result).
- Brief for this refresh named the head prefix `69bac724`; by clone time the live head had advanced one further commit. This census is of the clone head actually read.
- Live head (default branch `main`): `a3058ba676f82c1c21faf588b72acdc77fb73dc7`. Fresh shallow clone head matches exactly. Head commit subject, plainly: require the optimality sibling and pin the quantifiable sibling at a named commit (pull request 2).
- Visibility: private.
- Toolchain pin: Lean 4.19.0; the readme adds the compiler commit for its recorded run. Core Lean only, no large mathematics library. Two sibling repositories are now real pinned git dependencies (below) instead of in-tree copies.
- Files at head: a substantial readme, a check script, a recorded check log, a lakefile plus manifest, example inputs with expected output, a harness main file, the package library (root module plus 10 submodules, one of them new), and a worked-examples folder with one proved example. Theorem total in tree: **56** (52 in the package library, 4 in the worked example).

## Delta (old pin to this pin)

- **Copied modules removed (45 theorems leave the tree).** The five root-level byte copies of the optimality sibling's modules are gone, and the checksum file that verified them is gone with them. Those results now arrive through a pinned git dependency on the optimality sibling, and the build replays them from the dependency checkout. The in-tree theorem total therefore falls 94 to 56 while the proved surface the build sees does not shrink; the fall is a provenance change, not a loss of results.
- **Own library grows 49 to 52.** The 49 theorems of the old pin are all still present with the same names and the same headline roles (per-module counts unchanged: admission 13, composition 11, evidence 13, monotonicity 6, incremental 3, finiteness 1, examples 2). One new module, the bridge module, adds 3 theorems connecting this repo's admission relation to the quantifiable sibling's executable release acceptance and interface order (censused below).
- **Dependency boundary strengthened.** At the old pin the package required only the quantifiable sibling (finiteness module only) and stated that the sibling's other modules did not typecheck on this toolchain and were not imported. At this pin the package requires both siblings at named commits, and the readme's earlier exclusion note is superseded: the optimality modules are that package's own modules now, imported through the dependency. The finiteness result still comes from the quantifiable sibling.
- **Worked example added.** The examples folder gains a proved partition example (4 theorems, with its own recorded verification transcript and a rejected control). At the old pin the examples folder held only harness inputs.
- **Gate log is stale by exactly the bridge addition.** The recorded check log in the tree passes every stage (controls rejected, build completed, harness output matching, implications listing regenerated), but its axiom audit section records only the 19 headline theorems of the old pin. The audit module at this pin prints 22 theorems (the 19 plus the 3 bridge theorems); no recorded axiom lines for the 3 bridge theorems exist in the tree. Their evidence state is therefore one step below the headlines: proved in source, axiom set unknown from recorded evidence.
- **Evidence-module supporting lemmas changed.** The evidence module still holds 13 theorems and all its headline results are unchanged, but its supporting lemma set differs from the old pin (new list-splitting and disjointness lemmas support the same candidate-count results). No headline statement changed.

## Thesis (what the repo claims to prove) — carried forward, still true

Plain English: a new release is *admitted* over an old one exactly when, symbol by symbol, the new symbol keeps every old behaviour, keeps the same number of cost axes, never raises any cost upper bound, and both sides have valid (low ≤ high) bounds. Admission so defined is monotone and composes along chains; an incremental recheck that re-examines exactly the affected set (changed symbols plus everything downstream of them through caller edges) agrees with a full recheck; and the space of schedules and candidates involved is finite, with a fixed observation prefix leaving exactly 2 raised to the free count candidates. The readme's claims table (16 rows at this pin, covering the same 19 headline theorems) marks each proven, disproven, or premise — the disproven and premise rows are censused as such below, not as wins. New at this pin: the bridge prose adds that this repo's admission agrees, on a converted single-symbol case, with the quantifiable sibling's executable release acceptance, and that an empty submission is refused under the stated spec predicate.

## Headline census (axiom evidence from the recorded check log, per theorem)

The first 19 rows are carried forward from the old census; the recorded log at this pin reproduces exactly the same axiom set for each, so their evidence state is unchanged: **proven**.

| Claim (one quoted name) | State | What it proves, plainly | Axioms (recorded log) |
|---|---|---|---|
| `scheduleSpace_finite` | proven | For any qualification, the valid schedules form a finite space: some list contains every valid schedule. | standard three |
| `releaseAdmitted_iff` | proven | The executable boolean admission test on releases is true exactly when the propositional admission relation holds. | two of the standard three |
| `releaseAdmitted_trans` | proven | Admission composes along two admitted steps. | standard three |
| `symbolVerdict_admitted_iff` | proven | The executable per-symbol verdict says admitted exactly when the boolean symbol test passes. | one standard axiom |
| `qualifiedMono` | proven | Premise: an admitted step. Then every old behaviour is kept by the new symbol. | two of the standard three |
| `qualifiedTrans` | proven | The behaviour inclusion composes along two admitted steps. | standard three |
| `costNoRegression` | proven | Premise: an admitted symbol step; side condition: axes in range. Then the new symbol does not strictly dominate the old on upper bounds. | two of the standard three |
| `costTrans` | proven | Upper-bound non-regression composes across two admitted steps. | standard three |
| `not_per_execution` | refuted (disproof) | It is false that a bound-admitted step is no worse on every execution: bounds 1..100 to 2..3 admit, yet execution value 3 exceeds 1. The theorem proves the negation. | standard three |
| `moduleAdmission_compose` | proven | Per-module admission implies whole-release admission, under the named side condition that every call stays inside one module, plus module coverage and unique ids. | two of the standard three |
| `moduleAdmission_counterexample` | refuted (counterexample) | With one cross-module call and a stubbed callee, both modules admit separately yet the composed release does not. The side condition cannot be dropped. | one standard axiom |
| `evidence_remaining` | proven | Fixing a prefix of independent bits leaves exactly 2 raised to the free count candidates. | two of the standard three |
| `not_repeated_observation_shrinks` | refuted (disproof) | Observing the same bit twice does not shrink the candidate set again (size 2 either way, by computation). | none |
| `not_disqualification_empties` | refuted (disproof) | One disqualifying bit does not leave zero candidates (2 remain, by computation). | none |
| `determined_of_coverage` | premise | Given a total coverage observation (one boolean per symbol, supplied as a structure), filtering to that vector leaves exactly 1 candidate. The coverage object is the carried premise. | standard three |
| `inClosure_iff_affected` | proven | The locally defined caller closure of the changed set is exactly the upstream affected set, for an unchanged call edge set. | two of the standard three |
| `incrementalRecheck_iff` | proven | Headline incremental claim. Premises: old bounds all valid, and every symbol outside the affected set is literally unchanged. Then full admission holds exactly when every affected symbol passes its individual check. | standard three |
| `not_recheck_seed_only` | refuted (disproof) | Rechecking only the edited symbol is not enough: a concrete pair where the edited symbol passes, the whole release is refused, and a caller sits in the closure. | one standard axiom |
| `worse_refused` | proven | The worked example: symbol 1 admitted, symbol 7 refused for cost regression on axis 0, by computation. | none |

### New bridge theorems (3) — evidence state: proven in source; axiom set unknown from recorded evidence

The bridge module converts one symbol profile of this repo into the quantifiable sibling's prior-qualification and behaviour-submission records, then proves:

| Claim (one quoted name) | State | What it proves, plainly |
|---|---|---|
| `releaseAdmitted_iff_acceptsRelease` | proven (source); axioms unknown | Under stated side hypotheses (both releases are singletons, ids equal, both sides' bounds valid, cost lists equal in length, every paired upper bound non-increasing, candidate context equal to baseline context, and the out point no worse than the in point), this repo's release admission holds exactly when the sibling's executable release acceptance returns true on the converted records. |
| `not_bare_releaseAdmitted_acceptsRelease` | refuted (counterexample, in source) | Bare admission alone does not give spec acceptance: a concrete one-symbol release pair is admitted here, while the sibling acceptance on the converted records, with the stated points, computes to false. So the side hypotheses of the previous row cannot simply be dropped. |
| `nothing_below` | proven (source); axioms unknown | Two facts: the sibling interface's release order holds for the empty release against itself, and no prior qualification admits an empty submission under the spec predicate (an admitted empty submission would force a qualified behaviour to be both present and absent). |

### Worked example (4 theorems, own verification transcript)

The partition example models five services with calls checkout to invoice to tax, and search to index. It proves: the exhibited two-block partition is interaction-closed (one quoted name: `closed`); every interaction-closed partition keeps the three checkout services together, so the exhibited block is a least block; the composition theorem makes stubbed and linked evaluation agree under this partition; and a before-and-after computation showing the all-in-one rebuild block has 5 services, the exhibited block has 3, a singleton partition accepts a changed tax export under stubbing that the linked check refuses, and the exhibited partition refuses it. The example transcript records axiom sets within the standard set for the three printed theorems (the closure fact is not printed) and a rejected control (splitting invoice from its tax dependency fails).

## Full theorem census by module (52 library + 4 example)

- **Profile** (0 theorems): definitions only, unchanged in role — cost bounds, symbol profiles, releases, refusal reasons, verdicts, calls, and the two premise structures (interaction closure; total coverage).
- **Admission** (13): unchanged name set from the old census — behaviour-inclusion correctness, the symbol-admission relation and its boolean equivalence, zipped-list helpers, lookup helpers under unique ids, reflexivity under the bounds-validity premise, transitivity, release admission in both forms with their equivalence and transitivity, and the verdict equivalence.
- **Finiteness** (1): the headline finite schedule space result, still an application of the imported sibling finiteness theorem.
- **Monotonicity** (6): the five headline rows above plus the computed bound-tightening example.
- **Composition** (11): unchanged name set — stubbing lemmas under interaction closure, filter commutation, unique-id preservation, lookup survival, partition assembly under its premises, the headline composition theorem and its counterexample.
- **Evidence** (13): headline rows unchanged (candidate count, prefix filtering, the premise row, the two disproofs); supporting lemma set changed as noted in the Delta.
- **Incremental** (3): the closure equivalence, the recheck equivalence, and the seed-only disproof — now proved against the dependency's hypergraph module rather than an in-tree copy.
- **Examples** (2): the refusal example and the computed whole-release refusal, unchanged.
- **Bridge** (3): censused above. New at this pin.
- **Audit module** (0 theorems): one print-axioms command for each of the 22 theorems above (19 headlines plus 3 bridge). The recorded log reproduces only the first 19 outputs — see the Delta.
- **Root module and harness main** (0 theorems): the root imports the library including the bridge; the main file is the harness whose decision procedure is the verdict function; the recorded log shows its output matching the expected file.

Dependency-provided results (not counted in the tree total): the build replays the optimality sibling's five modules and the quantifiable sibling's modules from their pinned commits; the recorded log prints axiom lines for a subset of the optimality modules (every recorded set within the standard three or empty), exactly as the old census recorded for the in-tree copies.

## Premises and side conditions — consolidated flags (carried forward, still true)

- Premise claim (readme's own label): total coverage in the coverage row — the coverage structure is assumed, not produced.
- Carried premises: bounds validity; stability outside the affected set (symbols outside are assumed found unchanged — exactly what makes the incremental direction work); interaction closure plus module coverage plus unique ids (module composition); per-module admission (partition assembly).
- Side conditions: axis-in-range for the cost theorems; distinct bits for the prefix-drop lemma; unique ids for the lookup lemmas.
- New at this pin: the bridge agreement carries its own side hypotheses (singleton releases, equal contexts, the point condition), and its companion counterexample shows bare admission without them does not suffice.

## Zero-sorries and controls — evidence

- The check script source-guards the whole tree against the sorry, admit, axiom-declaration, and native-decision tokens; runs two negative controls (a scratch admitted proof, recorded rejected; a scratch proof that the regressed example is admitted, recorded failing by computation with the error quoted); builds with warnings as errors; runs the axiom audit; runs the harness and diffs against the expected output; and regenerates the implications listing. The recorded log in the tree shows all stages passing and the build completing successfully — for the pre-bridge tree, per the Delta note.
- This census independently re-ran the token search on the clone: no escape-hatch tokens anywhere in the tree. This census did not re-run the build (no long builds in this lane); build evidence is the repo's own recorded log, labelled as such, plus the example's own transcript.

## Explicit non-claims and boundaries (carried forward, updated)

- The readme's claims table itself marks four claims disproven and one premise — stated as boundaries of the result, censused above as such.
- At the old pin the readme excluded the quantifiable sibling's wider modules as not typechecking and not proved; that exclusion is superseded at this pin — those modules are now imported through pinned dependencies, and this census makes no claim about them beyond what the recorded build replay prints.
- The per-execution reading of cost bounds is explicitly disclaimed by the disproof row: admission controls upper bounds, not every individual execution value.
- The bridge agreement is a single-symbol, converted-record agreement under side hypotheses — not a claim that the two repos' admission notions coincide in general; the companion counterexample is the stated boundary.

## Watch delta — 2026-11-18, the hourly re-synthesis watch

The watch re-read the live head at 7d72fd08f758d9faea76abe9777226846d7d80aa, past this annex's census pin a3058ba6, and shallow-cloned it. Mechanical count at the live head: 66 theorem or lemma declarations across 15 Lean files, no sorry token, no custom axiom declaration. Same-method name comparison against the first census pin 033c12c0, run by the watch: the repo's own module directory carried 47 distinct theorem names at the first pin and carries 60 at the live head, with no own name lost; the 44 names absent from the whole tree are exactly the removed root-level copied modules, which confirms the de-duplication disposition recorded in the ledger. The prose placements above stand at a3058ba6; a full re-census at 7d72fd08 is owed.

## Watch delta — 2026-11-18, the second hourly re-synthesis watch

The watch re-read the live head at the enumeration head dce6564be7366ae3389e710b53a4623f497290b7 and shallow-cloned it. Mechanical count at that head, by the watch's own method (every theorem or lemma declaration in every Lean file in the tree): 70 declarations (67 distinct short names) across 16 Lean files, no sorry token and no custom axiom declaration in any file, 0 example declarations. The same method at the last recorded head 7d72fd08f758d9faea76abe9777226846d7d80aa counted 66 declarations (64 distinct short names). Name comparison, one mechanical method both times: 3 names gained, 0 lost. The prose placements in this annex stand at the census pin a3058ba676f82c1c21faf588b72acdc77fb73dc7; a full re-census at the new head is owed and the owed mark in the ledger stands.
