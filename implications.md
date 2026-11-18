# Structural implications

The full implications account of the qualification construction, carried from the reconciled records of 2026-11-17: the improvement-pass consolidation, the widening reconciliations (S1: the two accounts reconciled in 25 rows; S2: every claim traced in full form; S3: the claims audit), the design-implications record, and the live paper's own implications section. Every item states its consequence, what it follows from, and its evidence state in the state its source assigns — settled intent, proposed, implemented, verified, and for the proof material proven, premise, refuted, open. No state here sits higher than its source. The relayed external audit of 2026-11-18 adds one structural finding, carried at the end and marked relayed.

## Part 2 — Implications

### How to count this part

The reconciled, complete tracing is S2 (as consolidated by the
improvement pass): **17 base design claims (D1–D17) + 9 improvements
(21.1–21.9) + 9 consequence implications (22.A–22.I) = 35 traced
items**, each traced in S2 in the full form — (a) implementation
obligations with named artifacts, (b) consequences for Idol itself,
(c) consequences for the other six projects (idiom, idol-lib,
idol-model, idol-sites, idol-wide, idol-wsp — the seven-project set
of spec §13.4), (d) the monotonicity data layer, (e) the idol-sites
surfaces, (f) a concrete falsifier or a named definitional / premise
status. S1 reconciled the two earlier accounts against the landed
spec: **agreement on substance on all nine improvements and
throughout the implications**; the exceptions are listed at the end
of this part. The live paper's 14 audience implications (I-00–I-13)
are a presentation of the same material, not 14 additional claims;
they are listed separately because the paper assigns them its own
states.

### 2a. Base design claims D1–D17 — consequence, follows from, evidence state

1. **D1 Finiteness is derived from what a qualification is.**
   Consequence: the problem space is finite because a qualification
   is a finite presentation (named software, named criteria, finite
   named venues); every artifact is relative to a named snapshot and
   scope, and an artifact quoted without both is a claim defect; no
   question is ever asked about behavior outside the intended set,
   so the halting problem never enters. Follows from: spec §§20.0,
   16.2; Chris rulings 2026-11-17 16:10, 17:15, 18:15, 18:54 PST
   (finiteness is a necessary consequence of qualification, never a
   hypothesis). State: **settled intent; proven in Lean** (explicit
   enumeration, no finiteness hypothesis in the tree). Weakest link
   per S3: the Idol-native formalization is unbuilt (spec §20.5).
2. **D2 Witnessing is definitional — the witness effect.**
   Consequence: an execution carries its witness as part of its
   result (premises, state identity, venue, input digest, outcome,
   cost; seven parts — procedure, pin, venue, input digest, outcome,
   wall time, observed ranges — a part a run cannot record is named
   underivable in the witness itself); grain is the derivation step;
   hand-instrumentation of a program is a defect. Follows from:
   spec §§18.2–18.4; Chris 17:18 and 17:24 PST. State: **settled
   intent as a ruling; proposed as a mechanism** — the capability
   does not exist yet; it is a named work order in the shared graph
   engine, closing condition probe 11 (see O-list / S1 item 8).
   Until it lands, census surfaces append through producers as
   scaffolding under the envelope elimination rule.
3. **D3 One append-only ledger, with witness identity.**
   Consequence: every witness lands in one ledger, never modified or
   deleted; identity = source locator + project + pin + fact name;
   two records with one identity and different values are two
   witnesses (a repeated observation), never an edit; historical
   records enter by the same derivation applied to older inputs.
   Follows from: spec §17.2. State: **settled intent; implemented
   and verified over the standing store** (derivation, checker, and
   fold executed over the real store).
4. **D4 The accounting is a pure, stateless fold, independently checked.**
   Consequence: batches fold in recorded order with chained step
   hashes; the join is associative, commutative, idempotent over
   content-addressed witnesses, so any worker recomputes exactly,
   in any order, with no coordination state, watermarks, or cursors;
   an independent checker sharing no code recomputes and refuses on
   any mismatch; the ledger itself is the one non-stateless thing,
   named as data, not mechanism state. Follows from: spec §§17.8,
   18.8, 18.15; compounding clause, Chris 16:36 PST. State at S2
   time: **settled intent; proven for the construction (Lean);
   discharged at value level; refuted at full-text strength for the
   first derivation on disk** (shuffle changed 1 of 1,526 entries,
   evidence field only; duplication reworded 1,454 entries).
   **Superseded in the same improvement pass by lane C (verified):**
   both repairs implemented in derivation and checker (sorted
   distinct digests; dedup by witness identity before parts
   derivation), shuffle and duplication feeds byte-identical after,
   accounting moved f63a21d1 → **5fca02f3**, register F3 discharged
   at full-text strength for the repaired derivation; the refutation
   stands against the first derivation. Spec §§24.4/24.5 still lag
   this state — that lag is open item O4.
5. **D5 Equivalence is saturated under stated premises; classes join behavior.**
   Consequence: states shown equal under the same stated premises
   merge, every merge edge carrying its derivation and scope;
   transfer across lineages only with its check filed; values
   differing across environments are carried one entry per
   environment, values differing within one environment are carried
   contested — never silently winning, never dropped. Follows from:
   spec §§16.4, 17.4. State: **settled intent; implemented over
   recorded transition classifications and executed gate verdicts
   today** — classes stand on classifications until each project's
   committed saturated graph lands; every receipt says so.
6. **D6 Qualification and intent mappings are colorings of one joined graph.**
   Consequence: both mappings are derived views over the one store,
   recomputed by the fold, never separate stores; a state with no
   witness is an unoccupied state colored unresolved and occupies
   on its next execution; any component keeping a private mapping
   table that can disagree with the derived view is a defect.
   Follows from: spec §§18.8, 18.16; Chris rulings 17:15–17:24 PST.
   State: **settled intent; implemented in accounting form,
   checker-verified**; the rule form is D14, with its own state.
7. **D7 Quality facts are derived, four-part, bound-compared; unknown is its own value.**
   Consequence: every fact carries workload, environment,
   uncertainty, evidence, derived from the witness store's own
   provenance (§17.3 rules, three environment tiers); a part no
   rule derives is named underivable beside its entry and voids
   nothing; quantity facts compare as bounds (latency by upper
   bound, throughput by lower bound), never as point values dressed
   as bounds; per-venue difference is independently sufficient
   signal (an environment-dependence entry is derived from the
   difference alone, §17.6); unknown is never zero, never a loss,
   never a tie. Follows from: spec §§16.5, 17.3, 17.6; Chris
   16:10 PST. State: **settled intent; implemented and verified in
   part** — V-E in the paper verifies the per-venue signature (all
   six shared speed facts); named gaps remain per axis (paper
   G-01–G-07: effects, capability, build-cost, memory, correctness
   obligations, latency, uncertainty underivable on 254 entries).
8. **D8 The frontier is an exact procedure; completeness language is rationed.**
   Consequence: dominance only when evidence establishes no-worse
   on every required axis and better on at least one, under the
   same scope; incomparable alternatives are all kept, dropping one
   is a defect; the §16.10 procedure takes three named inputs and
   prints a blocked census (pairs tested / decided / blocked by
   first failing axis); the whole-saturated-space completeness
   phrase may be printed only on an exhaustive fixed point over a
   finite explicitly defined universe, and never implies the
   frontier beats every possible implementation; a budget stop is
   an exact partial record with the remainder marked unknown.
   Follows from: spec §§16.6, 16.8, 16.10. State: **settled intent;
   implemented** (frontier.py, hash-verified axis record or refuse);
   **verified over the derived accounting in its blocked form**
   (V-B: 67 alternatives, 908 pairs, 0 decided, 908 blocked —
   effects 597, capability 276, correctness-obligations 35).
9. **D9 The ordering theorem — a Pareto frontier over witnessed interval bounds.**
   Consequence: over a finite qualification set, finite venue set,
   and witnessed interval bounds for every run on every venue, the
   valid orderings are finite, their Pareto frontier is nonempty
   and computable, every emitted schedule is provably no worse than
   any named incumbent on time and compute simultaneously and
   measurably better wherever separation is strict; a claimed
   improvement is discharged only by incumbent + candidate + the
   two witnessed inequalities, mechanically checkable; refinement
   is monotone (adding witnesses only shrinks intervals, a schedule
   once proved dominated stays dominated); soundness is scale-free,
   completeness is budget-relative and receipted, never implied.
   Follows from: spec §20 (and §23 as executed). State: **proven at
   bounds in Lean; implemented; verified** — solver battery all
   five groups passed, plus the exact-frontier correction in
   Part 3 (the solver computes exactly; the defective layer was
   the real-instance runner's upper-point reduction).
10. **D10 Foreign software — lifting plus boundary sensing, with the runner envelope.**
    Consequence: any software, in any language, on any kernel, is
    covered: lifted into the semantic graph so its behavior space
    exists symbolically before observation (unobserved = unresolved,
    never absent); executions sensed at the kernel boundary (process
    lifecycle + syscall stream, the finest universally available
    grain); occupied states join the same store by the same fold —
    no second store; collection may use any foreign hook necessary
    (robust *across* foreign baggage, not free of it, Chris
    17:22 PST); the kernel sensor is the one irreducible foreign
    contact, kept thin, deciding nothing, lifted to Idol-symbolic
    form immediately; Idol-launched foreign executions run through
    an Idol-owned runner envelope appending a coarser envelope-grain
    witness, scaffolding with an elimination order. Follows from:
    spec §§18.5, 18.6, 18.16, 19. State: **settled intent for the
    scope; proposed for the mechanism** (S-08b in the paper);
    **premise for coverage universality** (complete mediation is
    the reference-monitor result, cited, with its falsification
    condition stated in §19.5); **implemented in part** (boundary
    sensor over the foreign battery, 12-of-12 in its battery);
    **empirical half refuted for this sensor on this host** by the
    adversarial pass — see H4 in §2e (register F9 pass → refuted;
    F2 premise untouched).
11. **D11 The environment representation must provably be the most robust, highest-resolution one.**
    Consequence: finite, determinable, at the highest physical
    resolution and highest-resolution temporal / ordering bounds
    the platform affords, collected once at the boundary so state
    is known by derivation without a second observation; each
    environment carries a stated resolution bound and ordering
    bound; a bound not shown to be the platform's finest is a named
    gap and witnesses taken coarser carry that bound in themselves;
    two records of one execution disagreeing about environment are
    a collection defect, never averaged, never sided with.
    Follows from: spec §§18.7, 18.14, 18.17; Chris 17:22–17:26 PST.
    State: **settled intent; proposed / open** — the resolution
    claim (register F12) stays **open**; the mechanism census
    (§18.17, D4 of the design lanes) is its falsification surface:
    seven mechanisms probed, one present and usable (the ptrace
    class), two refused, two absent as usable, one absent, one
    unprobed (hypervisor); one live candidate refutation named
    (arguments and return values afforded at ptrace stops are not
    carried). See O6.
12. **D12 Gates are three-valued; claim discipline governs every printed word.**
    Consequence: every verdict is proved / disproved / unresolved,
    and unresolved always names its boundary (exactly one boundary
    kind — budget, rules, or frontier, by stated priority); an
    execution is witnessed only when its witness stands in the
    store under the independent checker (a log line or lane report
    is provenance, never the witness); envelope-grain evidence is
    never quoted as derivation-grain evidence, and the grain of
    every quoted witness is stated with it. Follows from: spec
    §§1, 8, 12, 18.11. State: **settled intent; implemented in the
    engine / accounting verdict forms; verified in probes 6–10**
    (paper V-C: all mandated outcomes hold, exit 0).
13. **D13 The composed theorem — four parts over one named snapshot, under eight hypotheses.**
    Consequence: over one snapshot named and fixed before any part
    is computed (2,509 witnesses, 8,482 edges, 15 steps, 1,526
    entries; instance 209,952 assignments), finiteness, coloring,
    fold invariance, and frontier-at-bounds hold together, each
    only at the strength its own citation earned; per-execution
    strengthening is **disproven and excluded by name**.
    Follows from: spec §24.1–24.5 (design lane D1). State:
    **proposed as one composed object** — parts: finiteness proven
    (Lean) and discharged; coloring proven under the one universe
    side condition and discharged (180 of 180 pairs); fold entered
    at value level at entry time (superseded by lane C's closure;
    §24 text lag = O4); frontier at bounds proven and discharged
    (exact frontier 209,352, decided pairs 150,832, dominated 600,
    448 discharged against the incumbent; filed 23 kept as a
    distinguished subset only); coverage a **premise**. **The
    composition itself is not verified as one object — no joined
    check has run. That is O3.**
14. **D14 Coloring in rule form — ground rules, four states, four spaces, five-part receipt.**
    Consequence: the coloring is the least fixed point over ground
    rules on a named snapshot; a scoped subject has exactly one of
    four states (unknown, lawful, unlawful, conflict — conflict is
    its own state, never resolved by picking a side); four spaces
    are kept distinct (configurations, behaviors, support,
    coloring); the completeness receipt has five parts, each bound
    separately. Follows from: spec §§24.6–24.10 (design lane D2).
    State: **settled intent** (dictation-adopted, first spec entry
    here); **proposed in its new parts** (linear cost shape
    unproven and unmeasured; five-part receipt; four-state
    semantics); **implemented in part only** (no artifact computes
    the four states from ground rules or issues the five-part
    receipt); **verified in part only** (closure core proven in
    Lean; the Idol implementation is unbuilt).
15. **D15 Capacity is a per-venue parameter; capacity one is one instance value.**
    Consequence: a venue carries a capacity in slots, stated per
    venue; time is the longest path over the combined graph
    (precedence + slot-sequence edges), compute is the sum, at any
    capacity vector; capacity one is never a premise of the
    ordering theorem; a capacity above one may be used only where
    witnessed for that venue; the assignment-space shortcut is
    lawful only at capacity one with no precedence witnessed.
    Follows from: spec §25, scope note at §23.4 (design lane D5:
    ten sites listed — reliance scoped at three, implementation
    site named at one, six checked with no reliance or already
    scoped). State: **proposed / landed as spec text**; the
    real-instance runner is the one implementation site named.
16. **D16 Cost is defined by the ordering, in exact rational arithmetic.**
    Consequence: time = longest path (a maximum of sums, hence
    monotone, so endpoint evaluation soundly encloses every
    realization); the earlier placement / serial-simulation
    semantics is **unsound** (Graham list-scheduling anomaly: a
    shorter predecessor can move a successor out of a gap and
    increase the makespan) and is replaced; all bound arithmetic
    is exact rational arithmetic because float addition is not
    associative (two orderings of one schedule differed by
    5.7e-14 on a 358 ms bound and exact comparison called them
    unequal). Follows from: the ordering run — both defects found
    by execution (battery; real-instance run), not by inspection.
    State: **implemented and verified** (ordering semantics in all
    three evaluators; order-invariance assertions and the
    40,320-ordering probe are the standing controls, re-executed
    after the fix).
17. **D17 Relevance of a metric to an intent composition.**
    Consequence (as finally specified in spec §26 / register F13,
    superseding the three-factor form in which Chris ordered it at
    22:16 PST on 2026-11-17): relevance R = (D + C) / (1 + P) over
    the step-occurrence graph of one named snapshot — D the
    metric's filed weight as an immediate part of the composition
    (counted only when that step is settled, never defaulted),
    C counted influence along paths of length ≥ 2, P indirect
    pressure (influence from sources at path length ≥ 2, weighted
    by spread; F = P/(1+P)); shares are exact rationals summing to
    1 per step; mass through an unsettled step moves to a printed
    residue share, counted as neither contribution nor absence;
    the bound reading of P is claimed only where every step on
    every indirect path carries a stated non-expansive filing,
    otherwise P is exact as graph exposure only; cyclic influence
    is not computed at all. Worked probe, hand-computed: D = 3/5,
    C = 1/5, P = 1/4, F = 1/5, residue 0, R = 16/25. Follows from:
    spec §26; S4 lane. State: **proposed; implemented nowhere;
    verified nowhere.** Closing condition (§26.10): an
    implementation reproduces the worked example exactly, computes
    one witnessed instance, and an independent recomputation with
    no shared code path agrees digit-for-digit on all six
    rationals, at one named pin. What does not yet exist is named
    in S2's D17 trace: the intent composition as a stored object
    (today intent is only a coloring), per-metric contribution
    derivations, per-metric sensitivity records (the
    witnessed-spread shortcut refused by name: spread is not
    flakiness), an exact-rational storage form, and the independent
    recomputation control. The topology census (Part 3) adds a
    reconciliation: the Lean `MetricRelevance` profile (four exact,
    non-aggregated coordinates) is the checked design object; the
    §26 scalar is admissible only as a named projection of such a
    profile whose weights are filed in the snapshot itself.


### 2b. The nine improvements (spec §21) — all Proposed

State for all nine, in both accounts and in S2: **proposed**.
An improvement is closed only on executed evidence at a named pin;
a written improvement is a proposal, never a result. S1: the two
accounts agree on substance on all nine; two closing-condition
disagreements (21.3, 21.6) were resolved in favor of the first
account, on the second account's own rule that stronger conditions
govern and on the landed spec text.

1. **21.1 Witness minimality as an invariant.** Consequence: store
   growth is a function of distinct states, never execution count;
   a repeated execution of the same step produces the same
   content address and zero marginal symbolic storage (the
   ten-thousandth execution appends an occupation record and
   nothing else) — this is what makes a universal ledger
   affordable. Closing condition: two executions over the same
   state set, store's symbolic content grows by zero on the
   second, read back from the store, both occupation records
   present and distinguished.
2. **21.2 Implication closure as a derived object of the fold.**
   Consequence: entailment edges between gates (same premises,
   behavior superset) are derived and witnessed like any fact,
   each carrying its derivation; the fold reports every receipt's
   split into discharged-by-execution vs discharged-by-implication;
   the minimal execution set is a hitting set over the closure —
   the true floor under qualification cost; nothing may be skipped
   except through a derived edge (a hand-maintained skip list is
   the same defect class as hand-instrumentation); a wrong
   implication is a soundness bug, not an accounting error, and
   the checker recomputes the closure edge-for-edge. Closing
   condition: checker recomputation agrees edge-for-edge over the
   standing store, split report emitted with the frontier on
   every receipt.
3. **21.3 Regression as a per-step derived predicate.** Consequence:
   a step regresses iff the post-step frontier loses a previously
   frontier-or-dominated alternative on any required axis, or a
   gate in state PROVED becomes UNRESOLVED or DISPROVED, without
   a recorded premise change; the check runs over the step's
   changed set only (cost proportional to what changed); a
   non-regressing step carries its evaluation as a certificate in
   the step record. Closing condition: predicate evaluated over
   the standing step chain, agreeing with the checker's
   independent evaluation on every step, including a constructed
   negative-control step that regresses, which must be refused.
   (S1: first account right over the second on the exact predicate
   wording.)
4. **21.4 Benchmarks dissolved.** Consequence: any execution with a
   cost witness is a benchmark observation; a benchmark suite is
   a filter face over the ledger and nothing else; a number
   produced outside the ledger is unqualified measurement, citable
   nowhere; every number on any surface must resolve to witness
   identities; intervals span *all* witnesses for a fact, so a
   cherry-picked subset is not a derivable view — gaming is
   structurally excluded, not policed. Closing condition: every
   figure on the qualification surfaces resolves to witness
   identities by lookup, and a subset-interval request is refused
   by the derivation as underivable.
5. **21.5 Grain as a premise.** Consequence: grain (with workload
   and environment) is a component of the comparability premise;
   facts at different grains are incomparable until a witnessed
   grain-bridge derivation relates them; the comparability gate
   reads grain exactly as it reads environment; silent mixing
   manufactures precision neither side has, so the machinery
   refuses the pair with grain named as the reason. Closing
   condition: a cross-grain comparison with no bridge is refused
   by name, and one executed, witnessed bridge makes its
   comparison derivable. **Vocabulary split (open):** S1 found
   the second account right on the evidence of §§18.6/18.11 —
   the grains in force are derivation grain, boundary grain,
   **envelope grain** (a distinct mark the first account's list —
   derivation step, instruction trace, syscall stream — omits) —
   but §21.5 as landed follows the first account, so the live
   spec is internally split on this vocabulary. Owner named in
   S1 (spec landing lane, through the coordinator).
6. **21.6 Concurrency made operational.** Consequence: for a
   concurrent program the cost fact is a witnessed distribution
   summary (minimum, median, maximum over N witnessed executions,
   under a stated environment) with N part of the premise;
   dominance requires separation at the summary level, with the
   count named on both sides; a summary over 3 executions and one
   over 3,000 are different facts, never silently compared; the
   per-execution caveat (a dominated schedule can still finish
   first in one realization — disproven strengthening, D13)
   becomes a property of a defined object, not a hole in the
   claim. Closing condition: the solver consumes distribution
   summaries for a concurrent fixture and its verdicts match
   exhaustive simulation over the witnessed realizations.
   (S1: first account right over the second on this condition too.)
7. **21.7 Qualification transfer by premise cone.** Consequence:
   on change, only the change's premise cone re-derives and
   re-executes; every other qualification carries over, and the
   carryover is verified — the checker shows each carried
   qualification's premise set disjoint from the changed cone,
   and that disjointness check is the carryover's certificate,
   filed with the step; a qualification whose premises intersect
   the cone and was nevertheless carried is a defect with a named
   step. This is the incremental build's cone discipline applied
   to qualification, and it is what makes 21.3 affordable.
   Closing condition: over a recorded change, checker-verified
   disjointness for every carried qualification, plus a control
   change whose cone intersects a carried premise forcing
   re-derivation of exactly that qualification.
8. **21.8 The unresolved mass is a first-class figure.** Consequence:
   every receipt carries the full unresolved mass — per axis, how
   many pairs lack it (not only first-failing-axis counts, which
   understate the remainder); per gate, its unresolved boundary;
   per project, its unoccupied states — printed with the frontier,
   in the same record, under the same hash discipline; no surface
   may render a frontier without its blocked census beside it.
   The unresolved mass is the work queue, in the same units as
   the result. Closing condition: every frontier surface and
   receipt carries the census, checked by rendering each surface
   and reading the census back.
9. **21.9 Self-qualification.** Consequence: the fold, the checker,
   the ordering solver, and the sensor are inside the boundary —
   their executions witnessed, their gates ledger entries with the
   same three-valued verdicts, their defects found by the same
   disagreement discipline. First instance, **verified**: when the
   store reached 15 steps the independent checker refused step 15
   (its class formation under-joined against the spec — union over
   witnessed pins only, vs a 34-state transition path with 15
   witness-less intermediate states; 1,560 entries vs the
   derivation's 1,526) — found because two independent
   computations disagreed, not by inspection, user report, or a
   test written for the purpose; the fix takes the union over
   recorded states. Closing condition: the four components' gates
   stand as ledger entries with verdicts at a named pin, a defect
   introduced into any one is caught by the same disagreement
   mechanism as a control, and (second account form) a permanent
   regression probe for the step-15 defect class stands in the
   checker battery.

### 2c. The nine consequence implications (spec §22, A–I) — all Proposed as consequences

State for all nine, per S2 Part 3: **proposed** — "they describe
what follows if the design is built and verified, not the present
state of any running system." The second account presents the same
material as eight areas (regressions, benchmarks, redundant work,
certification, scheduling, foreign software, the Idol asymmetry,
organization) plus a boundaries section; the mapping is A=regressions,
B=benchmarks, C=redundant work, D=certification, E=scheduling,
F=foreign software, G=Idol asymmetry, H=boundaries (what it does
not imply), I=organization.

- **A. Regressions.** Follows from D2 + D4 + I3 (21.3), with I7
  (21.7) making it affordable. Inside the boundary the
  discovered-later regression category ceases to exist: breaks are
  refused at introduction by the per-step predicate, with axis and
  gate named; premise changes carry cone-scoped re-derivation;
  behavior outside the intended set is a new qualification
  question, not a regression. Regression testing as a later phase
  disappears — old witnesses never leave the store and every new
  step is checked against the positions they established; there is
  no suite to maintain, no nightly job, no bisection (the refused
  step *is* the location, its changed set the diff). Boundary:
  defects are not prevented; a wrong program whose wrongness no
  gate expresses is witnessed faithfully and qualified against a
  boundary that did not ask its question; unrecorded premise drift
  is invisible to the fold, which is why premise changes are
  recorded steps, not weather.
- **B. Benchmarks.** Follows from D4 + D7 + D9 + I4 (21.4).
  Performance stops being an event and becomes a continuously
  compounding property of the ledger: witnesses only shrink
  intervals, so the picture improves monotonically and never needs
  a benchmark event to refresh it; a system's performance at any
  moment is the frontier over everything ever witnessed about it.
  Under this standard most published benchmark claims are not
  well-formed (no workload / environment / uncertainty / evidence;
  subsets selected after the fact; speedups without the two
  witnessed inequalities = unresolved pairs wearing a conclusion's
  clothes). Prioritization becomes mechanical: widest unresolved
  intervals on required axes first; blocked pairs are the queue;
  environment signatures separate a property of the software from
  a property of the room.
- **C. Redundant work.** Follows from I2 (21.2) + I7 (21.7).
  Qualification effort is spent only on the non-entailed
  remainder: what is neither executed-and-witnessed nor discharged
  by implication is the whole work queue, and nothing else is run.
  Test suites shrink to their entailment basis by computation, not
  by someone deleting tests they judge redundant; CI becomes
  cone-scoped instead of a fixed liturgy re-run in full; skip
  lists, quarantine files, and "covered by that one" comments are
  replaced by derivations any checker can recompute. Honest cost:
  entailment edges become load-bearing — an organization skipping
  work on an implication is betting on that edge, which is why
  each edge carries its derivation and a wrong edge is a
  soundness bug, not a process slip.
- **D. Certification.** Follows from D4 + D8 + D13. A certificate
  becomes a receipt: the frontier, the fold hash, and the step
  chain at a pin, recomputable statelessly by any party to the
  identical accounting or a refusal; a release is qualified iff
  its receipt recomputes and its required gates stand proved at
  its pin (the release certificate Chris ruled yes on — the one
  answered question of the nine-question grilling session of
  2026-11-14 to 17 — is this receipt: **settled intent** for that
  identification). Auditing changes from re-running the vendor's
  tests to recomputation — cheap, exact, adversarial by
  construction (the tamper control refuses an altered accounting).
  Certification becomes continuous: the gap between the certified
  version and the running version is a diff of pins with a cone
  computation, not a recertification project. Boundary at S2 time:
  every certificate's fold half inherited H2 (value-level
  agreement only) until lane C's re-run — since closed, see D4.
- **E. Scheduling.** Follows from D9 + D15 + D16, routed through
  D1's finiteness derivation (a problem exists by being presented;
  a presentation is finite). The ordering result is not really
  about qualification: any finite task set with witnessed interval
  costs over a finite venue set and monotone cost composition —
  CI fleets, build farms, test matrices — admits the same Pareto
  frontier construction, sound at every budget, improving
  monotonically as witnesses compound; scheduling decisions stop
  being expertise and become bookkeeping (the expert's remaining
  work is choosing what counts as a task and a venue — boundary
  judgment). Boundary: the hypotheses are the whole claim; a
  workload whose costs are not witnessed has no frontier here,
  only unresolved pairs. Trace note (S2 U7): traced as a theorem
  consequence; **untraced as an empirical one** — no executed
  scheduling instance outside qualification ordering is on record.
- **F. Foreign software.** Follows from D10 + D6. Uncooperative
  software — closed, foreign, legacy, adversarial, or simply never
  instrumented for you — stands on the same witnessed footing as
  native software, because the footing is the kernel boundary, not
  the software's cooperation; comparative evaluation becomes
  receipts instead of bake-offs, and "incomparable, and here is
  exactly which axis is missing" is a complete verdict. Prototype,
  **verified**: the semi-persistent comparison (same scope, same
  gates, same pinned toolchain) first held both trees
  incomparable — fork better on capability and executed test
  gates, pristine better on verification, integration suites and
  performance unknown on both — and found a real defect by
  execution (a field-wise widening producing a non-reduced record,
  concrete counterexample over 8-bit words); after the fix, the
  counterexample as a permanent regression test, and proof
  authoring, the fork at its new head verifies with zero errors
  over a larger surface and **dominates on the measured scope**,
  with suite and performance unknowns still printed and unscored.
  The first verdict's value was the map and the defect, not a
  winner. Boundary: any foreign comparison whose witnesses come
  from the current sensor on this host inherits H4's adversarial
  bounds, and its receipts must state the caps where they bind.
- **G. The Idol asymmetry.** Follows from D2 + D10 + I5 (21.5).
  Idol software is witnessed at derivation-step grain by
  construction; foreign software at boundary grain — complete
  (mediation misses nothing) but coarse. Because grain is a
  premise, the asymmetry is a measurable fact inside the ledger,
  not a slogan: finer grain → smaller premise cones (cheaper
  re-qualification, via 21.7), more implication edges derivable
  where boundary evidence supports none (via 21.2), and no sensor
  at all for Idol's own derivations — the one irreducible foreign
  contact is a contact Idol software never makes. Self-denying
  clause, carried in full: where the advantage does not appear in
  the ledger, it does not exist under this design. Boundary
  (S2 U3): the structural route is fully traced; **every magnitude
  form is untraced / unmeasured**, because the witness effect (D2)
  does not exist yet and no Idol execution has ever been
  derivation-witnessed.
- **H. What this does not imply** — see §2e (the six standing
  boundaries, plus H1–H7 as corrected that night).
- **I. Organization.** Follows from A–H jointly. The scarce
  resource moves from compute to judgment: what belongs in the
  boundary — which behaviors are intended, which gates are
  required, which axes a scope declares, which artifact classes
  are worth lifters, which unresolved mass is worth closing next.
  The quality organization stops being a department that runs
  things and becomes custody of the intended set; the performance
  organization stops producing numbers and starts closing named
  unknowns; disputes about regressions and speed end because each
  is a computation over the ledger ending in a receipt, and
  receipts do not have opinions. What remains are disputes about
  the boundary, conducted in the open, in the units of the
  unresolved census — a queue that is finite (D1), ordered (B,
  21.8), and owned. Boundary (S2 U8): traced as a consequence
  statement; it makes no empirical claim about any actual team,
  and any reading of it as a measured organizational result is
  untraced. A team that intends the wrong behaviors receives
  impeccable, receipted qualification of the wrong behaviors.

### 2d. The live paper's audience implications (Paper I-00–I-13, §9)

The paper's own §9 states its rule: a direct logical consequence
is marked Settled intent; a practical consequence still needing a
ruling to enforce is marked Proposed. "If the proposal above is
true, then the following must also be true."

- **I-00 What changes, in one page — Settled intent.** The proposal
  replaces "we think it's better" with "here is the frontier, here
  are the witnesses, here is what is still unknown — recompute it
  yourself." Before/after, in the paper's table: better-than is
  frontier dominance on witnessed facts, not a score; evidence is
  a witness in the append-only ledger surviving independent
  re-check, not a screenshot or PR number; unknown is a first-class
  state blocking dominance, never zero / failure / dropped; the
  checker is checked by an independent checker; history enters by
  the same pure fold, no backfill jobs; foreign software is in
  scope by lifting + boundary sensing. Net effect: fewer, stronger
  claims — 908 of 908 pairs blocked in §4 is the system refusing
  to guess, and naming which witness would unblock each pair.
  For the author: you cannot hand-wave a win. For the reviewer:
  you review the frontier, not a vibe. For the team: no single
  score to game (improving one axis while regressing another
  produces incomparability, printed as such). For the reader
  later: claims stay recomputable (fold is associative,
  commutative, idempotent).
- **I-01 For anyone who writes or changes code — Settled intent.**
  Every execution you cause is a witness (test, gate, trivial
  local run), definitional to the execution, not a report filed
  afterwards; "it worked on my machine" becomes data, and a
  per-venue difference is kept as a split entry with an
  environment signature, not averaged away; you inherit
  qualifications (a landing is clean only if its failing set is a
  subset of the base's — you may not add failures and call it a
  wash); unfinished work stays visibly unfinished (missing
  effects / memory / build-cost witnesses read unknown and block
  dominance claims, printed next to the change); you do not have
  to run backfill jobs, file coverage reports, or coordinate
  ledger order (duplicates and arrival order change nothing).
- **I-02 For testing, CI, and landing changes — Settled intent.**
  CI stops being pass/fail: gates return PROVED / DISPROVED /
  UNRESOLVED, and UNRESOLVED names one boundary in priority order
  (budget → frontier → rules) — it is not a flaky failure to retry
  until green; overlapping gates are expected, not redundant, and
  the frontier rule stops overlapping verdicts being collapsed
  into one score; a gate that cannot name its premises cannot
  merge its result (a green run under different premises is a
  different fact); flakiness gets a precise meaning — disagreeing
  witnesses are contested or split, carried never dropped, and
  "re-run until it passes" destroys exactly that signal.
- **I-03 For performance work and benchmark claims — Settled intent.**
  Only proven bounds count (latency as a lower upper bound,
  throughput as a higher lower bound; a raw timing, a ratio
  without a corpus, a best-of-N with no spread all enter as
  unknown); every speed claim must name its corpus; environment
  is part of the measurement, not metadata (the certification
  environment's systematic slowness on all six shared facts is
  derived from the differences alone, V-E); uncertainty is not
  optional (251 idol-sites entries with underivable uncertainty
  cannot support a tight bound); consequently the cheapest way to
  "win" a comparison is often to witness the axis currently
  blocking the pair — §8 reads as a prioritized optimization
  backlog (effects for idol-lib 597 pairs, capability for
  idol-sites 276 pairs, build-cost everywhere with no witness).
- **I-04 For choosing between two implementations — Settled intent.**
  There is no total ranking: alternatives form a frontier, not a
  leaderboard, and keeping two incomparable implementations is a
  correct outcome, not indecision; "incomparable" is actionable
  (V-D names exactly what would move the pair); tie-breaks
  (content-ID, alphabetical, newest-first, author preference)
  order display only, never a quality result; cross-project pairs
  are never tested, so no cross-project speed claim is ever a
  frontier claim; choosing today under a blocked pair is choosing
  under *named* ignorance — the record shows which axis you are
  guessing about.
- **I-05 For releases, and for saying "done", "better", or
  "complete" — Proposed.** (Paper §9 entries I-05–I-13 were read
  by heading, state pill, and the section's own rule; the
  substance below follows those headings and the corresponding
  §22 / S2 consequences, which are the same material in fuller
  form.) A release snapshot is the unit of qualification —
  rule-set, term universe, evidence snapshot, premises, graph,
  and frontier committed together under typed roots; "which
  version was better?" is answerable only snapshot-to-snapshot,
  never floating-head to floating-head; a certificate is a
  receipt (see 22.D).
- **I-06 For foreign, legacy, and third-party software — Settled intent.**
  Same footing as native software via lifting + boundary sensing
  (see 22.F); comparative evaluation becomes receipts instead of
  bake-offs.
- **I-07 For venues, time, and compute cost — Proposed.** Scheduling
  generalizes past qualification (see 22.E); venue and cost
  decisions become frontier computations over witnessed interval
  costs rather than queue folklore.
- **I-08 For operations, incidents, and debugging — Proposed.**
  Every execution already carries its witness, so an incident is
  located to step, gate, and axis in the ledger rather than
  reconstructed from logs after the fact; the refused step is
  the location and its changed set is the diff that matters
  (see 22.A).
- **I-09 For audit, compliance, and anyone asked to trust a claim — Proposed.**
  Auditing becomes recomputation: the auditor recomputes the
  stateless fold with the independent checker and arrives at the
  identical accounting or a refusal, instead of re-running the
  vendor's tests and hoping they were representative (see 22.D).
- **I-10 For product, planning, and what to build next — Proposed.**
  The unresolved mass is the planning queue, in the same units as
  the results (see 21.8); resourcing consequence stated in the
  paper: instrumentation work (definitional witness emission) is
  not overhead beside the product work — it is what makes every
  other team's claims decidable, and deferring it defers every
  dominance decision that depends on it.
- **I-11 What becomes forbidden — Settled intent.** Direct
  negations of S-01–S-10: doing any of these is leaving the
  proposal — e.g. quoting a number without its witness set,
  converting unknown to zero / loss / pass, dropping an
  incomparable alternative, quoting envelope-grain evidence as
  derivation-grain, keeping a separate mapping store, running
  backfill jobs as a mechanism class.
- **I-12 Costs, risks, and what this does not promise — Gap (the
  paper's own pill).** Honest limits, stated in the paper:
  instrumentation must be built before it pays off (definitional
  witness emission and the symbolic profiler are not yet built,
  so witnessing is partial and many axes stay unknown — the
  proposal does not conjure witnesses for free); plus the six
  standing boundaries in §2e.
- **I-13 The closing test — five questions for any claim — Proposed.**
  In substance: (1) on which axes, under which scope? (2) which
  witnesses? (3) recompute it — does the fold agree? (4) what is
  the grain and are the premises the same? (5) what is still
  unknown, and what would close it? "If those five can be
  answered, you do not need to trust the claimant. You can
  recompute the frontier yourself. That — not a new dashboard,
  not a new score — is the implication of the whole proposal."


### 2e. Boundaries — what the design does not imply, and the corrected honest boundaries H1–H7

The six standing boundaries (both accounts agree on all six;
spec §22.H). Each is a limit on the implications above, not an
exception to them:

1. **No halting-problem escape.** A gate whose cost turns on an
   arbitrary program's halting has no witnessed interval bound and
   no theorem here gives it one; optimality is claimed only over
   the witnessed subspace; such runs stand named unknown, outside
   every decided pair, and every pair they touch stays undecided.
2. **Unobserved behavior is unqualified behavior.** Completeness
   is always relative to a named universe (the lifted behavior
   spaces plus observed occupations, for foreign software; the
   intended set, for the problem space); choosing that universe is
   a human act the machinery cannot perform or validate.
3. **First evidence is never eliminated.** A behavior must execute
   at least once, under premises someone chose, or be entailed by
   what has, before anything about it is witnessed. The design
   eliminates repetition, never first contact.
4. **Storage is bounded by distinct states, not executions — and
   some workloads have very many distinct states.** The minimality
   invariant promises the store never charges twice for the same
   state; it does not promise the world contains few states.
5. **Mediation proves witnessing, not understanding.** Semantics
   come from the lifted artifact; lifting is per-artifact-class
   work with its own closing conditions; an unlifted artifact is
   witnessed but not interpreted. Obfuscation and encryption
   change what a behavior means, never whether it crossed.
6. **The protection-model assumptions are load-bearing and
   falsifiable.** Exactly three: the sensor sits strictly below
   the observed software; the ledger is append-only from below;
   the platform's protection model holds. Exhibit one userland
   path to a visible effect or accounted resource with no
   kernel-mediated event and the foreign-completeness section
   falls — and nothing else falls with it, because native
   witnessing does not depend on the boundary argument.

S2's corrected boundaries H1–H7 (these govern every implication in
S2; any earlier text stating them more strongly is superseded):

- **H1 Exact frontier — verified.** Filed 23 = upper-point-minimal
  subset of the exact frontier of **209,352**, produced by a
  reduction unsound as a frontier method; 5 of the filed 23
  discharge against the incumbent; **448** over the exact frontier
  dominate the incumbent and all 448 were discharged individually.
  The solver computes exactly; the defective layer was the
  real-instance runner, fixed to the zero-dominator count, with a
  two-run counterexample standing as battery group six.
- **H2 Fold law.** As D4 above: proven for the construction,
  discharged at value level, refuted at full-text strength for
  the first derivation on disk, with both repairs named in the
  §§18.8/18.15 amendments. At S2's writing the closing re-run was
  still owed; lane C closed it in the same pass (D4).
- **H3 Lean record.** At head 37917a4195ef of the quantifiable
  repository: finiteness proven; fold proven at H2's strength;
  coloring proven under one stated side condition (the snapshot
  universe names every conclusion the rules can produce); Pareto
  at bounds proven; per-execution dominance **disproven** with a
  proven counterexample (bounds [1,100] against [2,3]);
  coverage carried as a **premise**, never counted proven. No
  claim in the Lean record is open.
- **H4 Sensor completeness — refuted on this host.** The earlier
  12-of-12 battery stands as a result over that battery only.
  Adversarial pass, four cases against the same sensor: behavior
  split (witness verifies, qualified behavior never runs while
  sensed — softer evasion); tracer kill (sensor died by signal 9,
  zero records written, effect file stands on disk with no
  witness); sequence grain (20,037 syscalls, stored sequence
  null, record fails standing verification); record-table grain
  (4,201 executions, 4,096 records, 105 executions with no
  record, root record also unverifiable). Three of four evade.
  Register F9 pass → refuted on this host; F2's premise stands,
  its empirical half is refuted for this sensor on this host at
  the kill route and the two caps named. Repairs named, none
  claimed: stream records to disk as they arrive; state the caps
  on the qualification itself where they bind; treat a tracer
  check by the observed program as a sensed event in its own right.
- **H5 Engine saturation battery (step 3.5) — open, failure
  measured.** A demonstrated fixed point (an actually run final
  empty round) only on the smallest subject (16 states). Failures:
  an unnamed 64-iteration ceiling firing silently with residue
  standing; a depth-rise condition deadlocking against the residue
  definition (no subject needing depth past 8 completes);
  equality-family throughput collapse (~1,650 states/s at size 5
  to ~2 states/s at size 11 in lane E's later reading; 600 s cap
  reaches roughly 500–800 states against a stated 100,000 node
  cap); the hidden equality probe's required commute merge blocked
  by the merge condition as written (14 states, 0 merges); cap
  mis-fires (generation cap overshot 56 over 50; merge cap binds
  per call, not per run — 12 merges under a cap of 5); and the
  most serious single defect in the pass — **the node cap
  truncates silently**: a 64-state subject cut at 20 presents
  residue 0, a verified fixed point, and an empty caps field, i.e.
  a truncated run that reads as complete.
- **H6 Standing numbers, with scopes.** Composed-theorem snapshot:
  2,509 witnesses, 8,482 join edges, 15 fold steps, 1,526 entries.
  Derived-accounting frontier over that store: 67 alternatives,
  908 pairs tested, none decided, all blocked (effects 597,
  capability 276, correctness-obligations 35), against a prior
  baseline of 205 candidate facts with none attachable and no
  alternatives in existence at all.
- **H7 The witness effect does not exist.** (Carried through S2
  as the boundary under D2/D17 and implication G: until the
  capability lands, no Idol execution has ever been
  derivation-witnessed, and every magnitude claim depending on it
  is unmeasured.)

### 2f. S1 reconciliation dispositions that change the implications reading

- Nine improvements: agreement on substance in all nine.
- Closing conditions 21.3 and 21.6: **first account right in
  both**, on the second account's own stronger-conditions-govern
  rule and on the landed spec text.
- Grain vocabulary (21.5): **second account right** on §§18.6 /
  18.11 evidence (envelope is a distinct mark), but §21.5 as
  landed follows the first account — the live spec is internally
  split; open item, owner named (see Part 3, S1 item 1).
- Implications: agreement throughout, with **two both-superseded
  dispositions** — §22.E and two sentences of §22.H were amended
  so finiteness is derived from presentation (spec §20.0; the
  18:15 and 18:54 PST rulings), not stated as a finite-set
  hypothesis. Verified mechanically: §§21–22 as landed are the
  first account's text verbatim (whitespace-normalized) except
  exactly those three places.
- Comparison prototype coverage: **second account right** — the
  closure record establishes the fork at its new head verifying
  with 0 errors and dominating on the measured scope; the first
  account is stale, not wrong about the first (incomparable)
  verdict.
- Second account's verified figures spot-checked exact at their
  snapshots; its one wrong figure is the first account's size
  (13,797 claimed; 13,748 bytes on disk).
- Staged merged spec: it did land by a single copy at 18:01 PST
  on 2026-11-17 (live spec verified at 131,284 B at that landing);
  the temporary staged copy no longer exists; the only staged
  content the live spec lacks is the superseded §22.E / §22.H
  wording above; nothing was carried in by S1.

### 2g. S3 claims audit — weakest links (14 headline claims)

Finiteness — Idol-native formalization unbuilt (§20.5).
Coverage — the executed control (empirical half refuted, H4).
Fold — the spec text (§§24.4/24.5 still record the re-run as
unexecuted; amendment owed, O4). Coloring — engine saturation
(H5). Pareto and solver — the receipt layer at audit time (since
closed by I2 in the same pass, Part 3). Per-execution dominance —
the design claim itself (disproven, correctly carried
everywhere). Regression rejection and tamper evidence — one
untested adversarial shape each (a drop disguised as a merge; a
snapshot splice — O10). Composed theorem as one joined object —
the executed control (no joined check ever run, O3). Resolution
claim — open, the census its falsification surface (O6).
Campaign executed check — verified at its scoped strength (one
round, one window; see Part 3, I6 figures).

### 2h. Untraced implications U1–U11 (S2, final count 11)

An item is untraced when a consequence is asserted, or follows
the report's shape, without an evidence route in the sources.
Listing is the disposition; none is smoothed over.

- U1 Per-project variation beyond the shared formats (per project:
  foreign tool censuses, skip/quarantine practice, step-chain
  filing state, premise recording grain, platform bound
  statements, exact-arithmetic tooling audits — none evidenced).
- U2 Sibling (S1) reconciliation pending at S2's writing —
  affected I5 directly; I3/I6 only if S1 reversed the
  stronger-conditions note. (S1 has since landed; see §2f.)
- U3 Idol-asymmetry magnitudes (every quantitative form of
  implication G unmeasured — the witness effect does not exist).
- U4 Resolution-claim downstream uses (any sentence using the
  highest-resolution property as a premise, rather than quoting
  it as an open requirement with its census, is untraced until
  F12 closes).
- U5 Composed-theorem and rule-form-coloring instances for the
  other six projects (constructions are project-generic; no
  §24.4-form snapshot or §24.6-form rule set exists for any of
  the six; per-project consequences are obligations, not results).
- U6 Linear cost shape of the closure (§24.7: proposed as a
  requirement; no measurement on disk; the proof bounds only the
  step count; any present-tense efficiency claim is untraced).
- U7 Scheduling beyond qualification, empirical half (no executed
  fleet / farm / matrix instance on record).
- U8 Organizational effects as observations (no before/after
  measurement of dispute rate, audit cost, or queue behavior).
- U9–U11 (added with D17) The relevance measure's: combination /
  storage points not in the definition as first received (since
  specified in §26 — see D17); the intent composition as a stored
  object; per-metric contribution derivations; per-metric
  sensitivity records; exact-rational storage form; independent
  recomputation control — in the improvement pass's summary,
  "the relevance measure implementation under its 26.10 closing
  condition, with its three untraced items (S2 U9–U11)" remains
  an open plus-item.

---


### Audit addition (relayed, unverified — 2026-11-18)

The relayed external audit (synthesis.md section 6) finds the proof family carries two opposite monotonicity directions with no stated rule for combining them: the composable/safe line requires the new release to show no behavior the old lacked (nothing new appears), while quantifiable requires the candidate to keep every qualified behavior (nothing qualified disappears). A release that adds a feature fails the first; a release that removes dead behavior can fail the second. Consequence: the release process needs one stated admission rule that composes both directions, or a stated choice between them, before either family's monotonicity theorems can govern a real gate. State: relayed finding; the underlying theorems are proven as stated at their pins; the combination is unbuilt.
