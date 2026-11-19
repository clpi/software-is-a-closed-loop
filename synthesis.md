# The synthesis — software is a closed loop

First synthesis, 2026-11-18. Sources: the nine landed software
proof repos at the pins named in README.md, the decidability
spec through section 26, the improvement-pass record of
2026-11-17, the frontier reduction check, and the topology
census of 2026-11-18. Every theorem is placed below by name,
with its statement in plain English, its pin, its axiom
dependencies where the source states them, and its stage in
the loop. The census annex (census/) carries the full
per-theorem census each placement was drawn from. States use
the discipline of README.md: proven, premise, proposed,
refuted, asserted, unknown. A claim sits no higher than its
evidence.

## 1. The loop, stated precisely

The loop has eight stages. Each stage's inputs are the
previous stage's outputs. The only external inputs are the
two named at stage 0.

Stage 0 — Entry. Inputs: named software (a repo at a pin)
and named criteria (the qualification's intent, policy, and
metric definitions). Nothing else enters. An instance of the
loop is identified by exactly these names together with the
observation snapshot, the venue model, the candidate
generator, and the equivalence rules — the instance identity
the certificate design calls K (proposed as a single linked
object; its parts exist and are checked separately).

Stage 1 — Finiteness. The named software and criteria
determine a finite behavior space: runs and venues are lists,
schedules are lists over a finite alphabet, profiles are
Boolean vectors of named dimension. Finiteness is derived
from the definitions, never assumed. Governed by
software-is-quantifiable's finiteness theorems and
software-optimality's finite qualification enumeration
(stage placements in section 2).

Stage 2 — Qualification. Ground rules over the finite space
derive what holds: the least closure under the named roots
and rules. The coloring of a configuration — unknown, lawful,
unlawful, conflict — is computed from evidence, never
assigned by hand. Governed by the closure semantics of
software-optimality (axiom-free core), the coloring fixed
point of software-is-quantifiable (proven under one side
condition), and the fail-closed executable bridge between
them.

Stage 3 — Witnessing. Executions of the named software
append witnesses to an append-only ledger. Coverage — every
execution witnessed — is a named premise of the platform
(sensor strictly below the observed software, append-only
ledger, complete mediation), never counted proven; its exact
falsification condition is itself a theorem. Receipts bind
witnesses to obligations under scope keys at this stage.

Stage 4 — Accounting. The ledger folds to an accounting: a
pure fold, associative, commutative, idempotent, so the
accounting equals recomputation from the surviving witness
set in any order, and retraction is exact — observables after
a withdrawal equal recomputation from what survives. The
hypergraph is the source of truth at this stage; every other
graph (dependency, invalidation, interaction) is a derived
view, reproducible from it, and incremental recomputation
over the views is proven equal to full recomputation of the
new snapshot.

Stage 5 — Bounds and frontier. From the accounting, bounds
on each named axis and the Pareto frontier of the named
candidate set are derived. Dominance is decided on bounds
with three outcomes; the frontier is exactly the
non-dominated set of the supplied population — finite,
membership decidable, complete over that population, and
never claimed over populations not supplied. Per-execution
dominance is refuted at this stage and excluded by name.

Stage 6 — Eligibility and admission. Before any ranking, a
hard gate: a candidate is admitted only with evidence for
every obligation — feasibility, observed behavior, timing
receipts present and within limits. Missing evidence is a
distinct state from failure. A rejected candidate cannot be
optimal; an admitted dominator refutes a certificate.

Stage 7 — Improvement. Candidates are generated, qualified
through stages 2–6, and measured; the solve returns the
non-dominated eligible set with a certificate a separate
checker can verify. Schedules are the worked form: complete
enumeration of a named finite model, feasibility by exact
membership, a certified optimum over the enumerated set.

Stage 8 — Re-entry. An accepted improvement becomes the
named software at a new pin and re-enters at stage 0.
Requalification is incremental by construction: witnesses
join, derivations re-derive over their premise cones,
verdicts carry; there is no batch mode underneath. The
regression gate at this stage accepts exactly the candidates
that drop no qualified behavior. The loop closes here: the
output of stage 8 is an input of stage 0 of the same form as
the loop's only external input.

## 2. The composed claim, at its evidence

The composed claim (spec section 24; open item O3): over one
named snapshot, finiteness, coloring, fold accounting,
frontier at bounds, and the exclusion of per-execution
dominance hold together as one joined statement. State:
composed in the spec with eight hypotheses and part-by-part
citations; the parts are proven where section 3 places them;
the composition as one joined theorem object is PROPOSED —
no single checked run of the composed statement exists in
either repo. The topology program's phase 2, item 8 owns its
formal half. Nothing in this synthesis claims it higher.

The practical instance stands separately and is verified:
the nine-run, six-venue ordering instance of spec section 23
was recomputed exactly — the exact frontier is 209,352 of
209,952 assignments, the filed 23 all genuinely undominated
but only the upper-point-minimal subset, 448 assignments of
the exact frontier discharging against the incumbent, bounds
recomputed in exact rationals and reproduced digit for digit
(bound-map hash e4ded389). That is an executed verification
of one instance, not the composed theorem.

## 3. Placements by repo

### 3.1 software-is-quantifiable — census pin 37917a41, Lean 4.15.0

Axiom posture (repo README, recorded build 2026-11-17):
headline theorems depend only on the standard axioms
(propext, Classical.choice, Quot.sound); zero sorries, zero
added axioms; modules compiled directly with the Lean
executable, exit 0. No per-theorem axiom lists are stated in
the sources; the coverage theorem is stated to depend on no
axioms at all. 46 theorems and lemmas in five modules.

Stage 1 — Finiteness module (4 theorems). The qualification
is a structure of two lists (runs, venues); one theorem
exhibits an explicit enumerating list of every schedule of
run-count length over the presentation, and a second
restricts it to every valid ordering. Two supporting lemmas
carry the list machinery. PROVEN. Finiteness by construction;
no finiteness hypothesis appears anywhere in the repo.

Stage 4 — Fold module (12 theorems). The accounting state is
the characteristic function of the recorded witness set; join
is pointwise union. Proven: join associative, commutative,
idempotent; the identity laws; the fold over an append
records exactly the appended set; two accountings with the
same membership are the same accounting; the accounting is
invariant under permutation and under self-append, and
conses agree. PROVEN at value level. This is the fold law of
the loop's accounting stage in its value projection; the
stronger inductive form lives in software-optimality
(section 3.2) and is the stronger home (section 4).

Stage 2 — Coloring module (19 theorems). Ground Horn rules
over a finite universe; the step and iteration functions and
the coloring are defined executably. Proven: a fixed point
is reached within universe-length steps; the coloring is a
fixed point; the coloring is sound and complete against the
inductive derivability relation. PROVEN under one side
condition: every rule's conclusion is a member of the
universe list. The condition is required for termination,
the fixed point, and completeness — notably not for
soundness. In software-optimality the same condition becomes
an executable gate (section 4).

Stage 5 — Pareto module (9 theorems). Bounds are intervals
over the natural numbers on two axes (time, compute). Proven:
the separation test is sound — separation implies dominance
under every realization inside the bounds; refinement of
bounds is monotone for separation; every finite nonempty
candidate list has an undominated element; a frontier output
is never dominated by an in-set incumbent; the regression
gate accepts exactly the candidates that drop no qualified
behavior. One DISPROOF: per-execution dominance is false,
proven by the counterexample of bounds [1, 100] against
[2, 3] with compute 0, where the dominated schedule can
realize 1 against 3. The disproof is a result of this repo
and sits at stage 5 as the exclusion the composed claim
cites.

Stage 3 — Coverage module (2 theorems). The platform premise
structure names three assumptions: the sensor sits strictly
below the observed software, the ledger is append-only, and
mediation is complete. The coverage theorem is the
projection of the mediation field from a premise passed as
an argument — PREMISE, never counted proven. Its companion
states the exact falsification condition: coverage holds if
and only if no execution is unwitnessed. Axioms: none.

### 3.2 software-optimality — census pin 0ea4626b, Lean 4.19.0

Fourteen root modules, no Mathlib, no custom axioms, no
sorry admissions; the check script rejects custom axioms and
sorries and treats warnings as errors. Axiom dependencies
below are the repo's own printed audits.

Stage 2 — the Qualification module. The least rooted
derivation semantics: the closure is least, closed, monotone,
idempotent; compounding is exact — the closure of a union
equals the closure over the two closures, retaining
cross-source consequences, explicitly not the union of the
closures; any two sound exhaustive saturations agree (order
independence); soundness is conditional on valid roots and
rules; withdrawal creates no new support; the surviving
subsystem is characterized; cycles alone bootstrap nothing
when every rule needs a premise. All nine printed theorems
carry EMPTY axiom lists — the strongest axiom posture in the
estate. This module is the semantic core of stage 2 and the
stronger home of the fold's compounding content (section 4).

Stage 2 — the ExecutableClosure module. An exhaustive
sublist-and-intersection algorithm: the powerset enumeration
has exactly 2-to-the-universe-size entries (proven), and
under roots and rule heads bounded by the universe, the
algorithm's membership is exactly the derivability relation.
The checked face is fail-closed: a some result is bounded
and exactly the derivable set; a none result holds exactly
when the bounds fail — both proven. The raw function outside
its preconditions can return the whole universe vacuously
and must not be exposed; the README directs all use to the
checked face. PROVEN, standard axioms. The algorithm is a
deliberately exponential reference, not a worklist — the
efficient saturation proven equal to it is an open point
(next-steps.md, from topology point (b)).

Stage 1 — the FiniteQualification module. All Boolean
profiles of dimension n: the count is 2-to-the-n (proven),
completeness holds by exact membership rather than by
counting, and filtering under a supplied total Boolean
evaluator is exact. The evaluator is an input, not assumed
to decide arbitrary semantics. PROVEN.

Stage 5 — the FiniteFrontier module. The frontier of a
supplied list under a supplied dominance predicate is
exactly its non-dominated members; the strict Pareto
comparator over integer costs is exactly componentwise
no-worse with one axis strict. The four-way coloring
(unknown, lawful, unlawful, conflict) is a function of two
evidence Booleans, with exactness theorems for the conflict
and unknown cases — and, a small dominated point the
topology census found, no characterization theorems for the
lawful and unlawful cases. PROVEN; the frontier is relative
to the supplied list only — no claim that candidates cover
all implementations.

Stage 7 — the FiniteSchedules module. Complete start-tick
enumeration of a named model: enumeration completeness is
exact membership (proven); feasibility (size, placement
bounds, pairwise non-overlap on capacity-one venues,
precedence) filters the enumeration to exactly the feasible
schedules; a certificate designates a feasible schedule with
no strict Pareto dominator among all schedules of the
enumerated model; the external queue form has its own
exactness theorem; an accepted improvement is conditional on
a supplied preservation checker being sound. PROVEN within a
deliberately literal model, whose boundaries the repo states
and the synthesis carries: durations are natural numbers and
positive durations are not enforced in the model (a
zero-duration dependency cycle satisfies the non-strict
precedence inequalities); acyclicity is directed to be
enforced separately; venues are homogeneous; shared or
external resources are not modeled; the horizon bounds start
ticks, never completion times.

Stage 7 — the ForeignCampaign module. 120 distinct
two-worker queue candidates, metrics recomputed from
durations; the chosen assignment's costs [6991879848,
10280231762] strictly improve the baseline's [9006285993,
13775558659], and the exact frontier of the 120 is four
named schedules — all by kernel decision, several theorems
axiom-free. PROVEN for the imported catalogue only: no
completeness for the external queue generator, no future
speedup. Physical timings are imported constants; their
provenance is evidence, not proof.

Stage 6 — the EligibleSchedules module. The hard gate before
ranking: admission requires a positive required count, the
exact receipt count, and every timing present and within its
limit (equality passes; missing, over-limit, and zero-round
are rejected) — characterized exactly. A rejected candidate
cannot be optimal; an admitted dominator refutes a
certificate. PROVEN, standard axioms.

Stage 6 and 7 — the EligibleCampaign module. The three-plan
pilot (three paired rounds, caps equal to the baseline plan's
times): all admitted; the second plan is the singleton
frontier (its maximum 6240471073 ns against 10769189848 and
9146680841); a synthetic one-nanosecond-over control is
rejected. Most theorems axiom-free. Boundaries carried:
receipt flags are imported inputs; the objective was
corrected mid-run, not preregistered; caps are a
paired-baseline, not a service-level agreement; no causality
or forecast is claimed.

Stage 3 and 6 — the ScopedEvidence module. Scoped
qualification: nonempty requirements; unique scope and round
keys and receipt identifiers; equal counts; scopes tied to
the named policy; exactly one matching receipt per
obligation; witness extraction; duplicate and wrong-scope
rejection — all proven as the acceptance contract. The
boundaries are explicit and carried: identifiers are opaque;
cryptographic authenticity, parser correctness, and the
policy digest-to-bytes binding are NOT proven; dedupe by
receipt identity must happen before the selected set is
constructed; no cross-lineage transfer is inferred; a
suite's elapsed time is not a per-job elapsed time.

Stage 7 — the LinearSelection module. Single-axis minimum
selection with exactly n−1 comparisons (proven); the count
excludes gate evaluation and cost computation and is not a
runtime benchmark. The set-valued all-ties form is exact and
membership order-independent; the internal one-winner form
is not order-invariant, and no serialization is claimed.
PROVEN.

Stage 6 — the ScopedSelection module. The bridge: the
selection gate is scoped qualification itself. A certified
scoped optimum yields witnesses for every winner obligation
and has no qualified dominator. PROVEN, standard axioms.
Boundary carried: the selector does not prove candidates
share an intent or metric contract — ingestion must enforce
compatibility (topology point (f): closable as a checked
admission precondition).

Stage 6 and 7 — the ScopedCampaign module. The concrete
bridge on the pilot: all scoped-admitted; the second plan's
certificate; singleton selection with reordered-catalogue
agreement; reused-round and foreign-configuration rejection.
All axiom-free except witness extraction. Not a transport
layer; dedupe, digest authenticity, and authorization remain
ingestion obligations.

Stage 9 — the MetricRelevance module. Relevance as exact
nonaggregated profiles: no weights, no scalar score is
manufactured anywhere in the module. Direct single-metric
exactness; composition irreducibility over proper subgroups;
exact unreduced fractions (empty evidence is none, not
zero); the indirect rate's denominator restricted to
admitted, matched-context records; permutation invariance.
PROVEN over synthetic fixtures — the fixtures are not
probabilities, utilities, or causal estimates. Reconciliation
with the spec's section 26 scalar (topology point (i)): the
nonaggregated profile is the design — it is what a checker
can verify without inventing weights; the scalar
R = (D + C)/(1 + P) stands PROPOSED exactly as the spec
states it, admissible only as a named projection of a
profile whose weights are filed in the snapshot, with its
residue printed beside it.

Stage 4 and 8 — the HypergraphIncremental module (the head
commit of the census pin). One authoritative hypergraph;
dependency, incidence, and interaction views are derived,
and the interaction view is proven equal to complete
regeneration from the hypergraph. Incremental recomputation
— reuse the unaffected, rebuild the affected, over the old
and new topology together — is proven exactly equal to full
recomputation, and agrees with the exhaustive closure on
admitted finite lists. A retracted cycle cannot bootstrap;
a withdrawn dominator's candidate returns to the frontier;
typed matrix cells equal complete regeneration. PROVEN,
mostly the three standard axioms, the matrix theorems
propext only. Non-claims carried: this is a semantic theorem,
not a fast-worklist or sparse performance proof; raw list
counts carry multiplicity; dedupe, identity, and withdrawal
precedence are upstream; remove-and-add is not a tombstone
protocol. This module is the loop's incrementality made
theorem: stage 8's requalification is stage 2's qualification
because the incremental and full answers are proven equal.

Proposed, not checked (the repo's own design document marks
these "not claimed as checked"; the synthesis places them as
PROPOSED): the linked-certificate principal theorem over the
instance identity K (checker acceptance implying
qualification, preservation for exactly K's scope,
feasibility under K's model, and no admitted dominator, as
one theorem); the coverage-certificate upgrade from a
catalogue frontier to a generator frontier; typed transfer
edges with checked cross-lineage reuse (the checked default
today is the opposite: reuse is never inferred); the product
decomposition theorem (removing a locally dominated
alternative cannot remove every representative of a globally
nondominated vector — with the document's own non-claim that
not every product of local-frontier members is globally
nondominated); and the certificate forms (feasible
improvement, catalogue optimum, generator optimum, with
certified branch pruning).

### 3.10 Placements from the estate-wide content sweep (2026-11-18)

Chris's ruling of 2026-11-18 01:59 PST: the accounting is
estate-wide, by content, not by name. A sweep of all 565 repos
then in the estate (method and counts in census.md) found
proof-bearing content in eleven repos the first synthesis had
not theorem-censused. Their placements follow; the annex files
in census/ carry the full per-theorem censuses. The nine
original family placements (sections 3.1 to 3.8) were refreshed
in the same sweep at new pins: quantifiable now 186 theorems
at f3709926 (toolchain moved to Lean 4.19.0; coverage still a
premise, restated as an abbreviation of the premise's own
mediation field); optimality 412 declarations across 33 root
modules at b52c3170 (the two general Pareto obligations
discharged; the five design items proven in fenced forms or
disproven where the design document warned); composable at
a3058ba6 (its copied modules became pinned dependencies; its
own theorems grew 49 to 52); the two claim shells landed full
proof packages (regress: 131 theorems at c36829da; review: 82
at 40b1e885); solvable 51 at 5bbceee7 and frontier 18 at
6a41c7be, both by example-only additions; certifiable and safe
remain claimed-not-proven at their heads, each with a worked
example landed and the safe branch still unmerged. Five repos
moved again while the sweep ran — optimality, composable,
traceability, idol-theses, and idol — and their placements
stand at the census pins named here with the live heads
recorded in census.md; re-census is owed on each and is the
continuous job's next input.

Stage 2 and 4 — idol-semi, census pin 508d7c66 (the identical
tree stands at the same pin as semi-persistent; one census
covers both). The largest proof tree in the estate: 156 Lean
files and 2,053 named theorems on a Lean and Mathlib pin of
version 4.35.0, proving soundness, completeness, and fidelity
results for a congruence-closure and e-matching engine
(saturation modulo the theory, flattened views, environment
and step semantics), plus a conformance development of
executable generators with 200 fixtures per family, and, on
the Rust side of the same tree, Verus proofs in the abstract
domains, verified containers, anti-unification, and engine
crates. Nine disproofs are flagged in its census (among them
delta incompleteness and an off-spine unsoundness family).
State: PROVEN as source statements at the pin, with a clean
admitted-proof token scan in this census; no recorded check
log sits in the tree, so a passing gate at this exact head is
CLAIMED, NOT PROVEN — its status file's passing-build claim
stands at an earlier date. One internal discrepancy (the
trusted-body marker count) is recorded in its annex as
unknown, not resolved. In loop terms this tree is a second,
independent formalization of the closure and fidelity content
of stages 2 and 4, built for a different engine; no import
joins it to the family modules, and the synthesis asserts no
equivalence between the two developments.

Stage 4 — premise-retraction-playground, census pin 47f469a4.
Premise-tracked retraction exactness for a small least-squares
model: the normal equations are a sum of per-premise blocks,
retraction subtracts one block and re-solves in exact rational
arithmetic. The general additive form is proven as ordinary
mathematics in its readme (not machine-checked); the two demo
fits were independently recomputed in this census and matched
exactly; the page's run-time check is an executed verification.
State: executed-arithmetic evidence — below kernel-checked
proof in this ledger, placed at stage 4 as the retraction law
in miniature.

Stages 2, 4, and 5 — software-compilers-lose-info, census pin
f531e31a. 33 theorems: a general loss lemma and a concrete
distinguishing pair prove that no recovery map exists for a
forgetting compiler (exact provenance is not a function of the
conventional artifact); preservation proves recovery as a
retraction on the qualified quotient, premise cones read from
the carried artifact exactly, and merge reachability exactly
the transitive closure of the union of the topologies;
completeness proves same carried artifact exactly when same
qualified quotient. Of the 14 audited headline results, 10 are
axiom-free and 4 rest on propext and quotient soundness only.
Carried openly: the behavior of a merge is not the join of the
behaviors (derivation growth is proven one direction only);
the general join-semilattice claim over all software states
is a labeled premise, with only its hypergraph instance
proven. State: PROVEN at the pin on the repo's recorded log.

Stages 3 and 4 — software-is-more-traceable-than-you-think,
census pin 4420fb1e. At this pin the repo carries a readme and
an invoice example (5 theorems, fixture scale, PROVEN on its
recorded transcript). The thesis content — the historical
witness hypergraph over the real witness store, the grain
determination, and the Lean proof of platform independence —
is recorded in the repo's own readme as implemented in a lane
and not yet landed in the repository. State in this repo:
CLAIMED, NOT PROVEN for the thesis; the grain map PROPOSED.
The placement stands so the gap is accounted, not hidden;
the lane's own record is the place its evidence will land
from, and the repo enters full census when the content does.

All stages — idol-theses, census pin d207be6e. The Idol
program's falsifiable theses formalized in Lean: 35 native
theorems (a merge development of 20, the fold 5, the frontier
8 plus a helper, a cited-registry module 2), a cited tranche
of 9 theses carried from their family homes at their stated
strengths (6 proven with their side conditions, the
per-execution dominance thesis REFUTED, coverage a PREMISE),
and a 16-entry future-work remainder stated as named work,
including 2 further refuted entries. State: PROVEN as the
repo states it for the native tranche; its check script
enforces full coverage and prints axioms for 14 theorems,
but no recorded check log sits in the repo, so a passing run
at this pin is not evidenced in-repo.

Stage 2 and 7 — software-testing-is-redundant, census pin
66f65b6f. 22 theorems over a copied qualification foundation:
an exact redundancy criterion (a test is redundant exactly
when its outcome is entailed by the retained set) and its
consequences, with a recorded gate log passing and 15 of 18
printed theorems axiom-free. The unrestricted slogan of its
name is REFUTED in-repo by a finite counterexample; the
general form that survives is a strict-growth theorem for
novel witnesses. State: PROVEN at the pin on the recorded log.

Stage 7 — software-fuzzing-is-suboptimal, census pin
18d9569b. 15 theorems: contract-bound strict dominance of an
adaptive policy over fixed plans, proven; and the blanket
reading REFUTED in-repo — every fixed two-query plan misses a
world of a three-world oracle while the feedback policy
succeeds in all three, and the converse dominance holds once
the target is justified. Recorded gate log passing. State:
PROVEN at the pin on the recorded log, the pair standing as
the countermodel against any unconditional reading.

Stage 5 and 7 — software-benchmarking-is-redundant-and-
suboptimal, census pin 4314a181. 10 new theorems over
foundation modules verified byte-identical to the testing
repo's at its pin: conditional redundancy of benchmark runs
and Pareto dominance of the retained set, proven in source;
several stronger readings REFUTED in-repo (strict savings
composing under parallel span, equal output implying equal
cost, and two others). Its check script's run is not recorded
in the repo, so the gate verdict at this pin is unknown from
recorded logs and the readme's no-axioms statement is carried
as claimed. State: PROVEN in source, gate unrecorded.

Stage 5 — idol, census pin 561cf395 (proof-bearing content
only; the repo's full placement is its family entry in
census.md). One Lean file in the compiler tree carries 7
theorems of the elaboration frontier: certain dominance
between bound assignments holds exactly when every pair of
realizations dominates; possible dominance exactly when some
pair does; a certified candidate with a complete cover
premise is cost-undominated by every eligible catalogue
member; and the demand closure is least and distributes over
unions. The file's own header carries the premises
(qualification relative to the supplied catalogue, observer,
and axes; measurement truth and coverage external). State:
PROVEN as Lean source at the pin; no recorded check log
covers the file. The same repo's checked-evidence tree is
executed machine-checked evidence at its own named pins —
4,918 controls across eleven batteries at its attributed pin,
in its own words test controls, not independent proved
theorems — and its polyglot fixture samples are test data,
determined not results. Both are accounted in its annex.

This repo — software-is-a-closed-loop, census pin d8047804.
Its own proof-bearing content is one checked example: a
four-point tuning space in which one step preserves
feasibility and never raises cost, the bounded loop's winner
is a feasible fixed point no feasible rival beats on cost,
and the before-and-after trace computes as stated — 3
theorems, all axiom-free, with the run recorded in the tree
and a rejected control. State: PROVEN at the pin. The theorem
statements this repo carries in its annex are other repos'
results and are counted at their homes, never here.

### 3.11 Placement from the fifteenth watch (2026-11-18) — a new proof repo

Stage 3, 5, and 7 — software-profiling-is-synthesizable,
census pin a53c4bf5. A new repo, entered on the sixteenth
enumeration and censused at theorem level on its first
sighting, by content: the measurement proof model for
software profiling, dictated by Chris on 2026-11-18. Twenty
theorem declarations in three Lean files on Lean 4.19.0:
baseline independence (the constructed measure is a function
of the overlap and the certified witnesses alone, invariant
under any choice of external baseline); finiteness derived
from the contract (the configuration count is the product of
the venue and ordering counts); witness compounding (the
assignments of that many witness positions number exactly
two to that power), distinctness, and combinatorial
sufficiency, with freedom at one coordinate; incremental
accounting equal to full accounting; idempotence and the
swapping of commuting effects; elimination of a step inert
on every state; the optimum and solved results (a least-cost
configuration exists over a nonempty finite configuration
set under any cost assignment); standing carried under
subsets and killed by one falsifying witness; and invariance
of comparisons under relabeling, with verdicts parametric in
the contract. Three adversarial controls stand in the tree,
each proving a weakened condition load bearing: baseline
dependence, non-idempotence, and witness dependence. The
recorded gate log at the pin ends in its axiom subset check
passing, with 9 of the 19 printed theorems axiom-free and
the rest on subsets of the standard set. Carried at the
repo's own states: one premise (facts about a runtime or a
job enter only as certified witness states; the Lean
development carries none of its own), the campaign bridge
and the visibility vector as proposed, and re-solving over a
sequence of cost assignments as open. State: PROVEN at the
pin on the recorded log, for the core above. The full census
stands in its annex file.

### 3.12 Placement from the twentieth watch (2026-11-19) — a new proof repo

Stage 3, 5, and 7 — software-losses-are-compositional,
census pin d1159dc1. A new repo, entered on the
twenty-first enumeration and censused at theorem level on
its first sighting, by content: the constructive proved
model of structural loss fixing, directed by Chris on
2026-11-19. Seventeen theorem declarations in two Lean
files on Lean 4.19.0: additive recording (the derived
contract level of a composition is the sum of the levels
of its parts); compositional projection, per axis, with
its three way form over part, interaction, and part; the
gap reading (gap zero is loss freeness); composition of
loss freeness, in two part form and in the three way
structural fix form (components loss free against their
shares, and the interaction recorded and loss free
against its share, give the whole loss free against the
sum of the shares); compounding (the gap of a composition
is at most the sum of the component gaps and the
interaction gap); monotonicity of the gap in each
component; localization (a gap in a whole is a gap in a
component or in the recorded interaction — no fourth
place for a loss to hide); finiteness derived from the
qualification contract (the problem space size is the
product of the two list sizes); and method soundness, per
axis and over a finite axis list. Three adversarial
controls stand in the tree, each a proved negation over a
concrete counterexample: an unrecorded interaction breaks
the compositionality of the gap, a non additive recording
breaks the projection law, and component wise loss
freeness does not save a composition whose interaction is
unrecorded. The recorded gate log at the pin ends in its
axiom subset check passing, with 3 of the 15 printed
theorems axiom-free, 4 on propositional extensionality
only, 7 on the standard pair, and 1 on the full standard
set; the two helper results are not printed in the log,
so their axiom states are unrecorded there. Carried at
the repo's own states: two named premises (record
fidelity, the evidence of a concrete campaign; and
re-measure — the model flips no beat cell), and three
proposed items (richer derivations, weighted axes, and
continuous axes), none formalized. State: PROVEN at the
pin on the recorded log, for the core above. The full
census stands in its annex file.

### 3.13 Placement from the twenty-first watch (2026-11-19) — a new proof repo

Stage 3, 5, and 7 — software-persistence-is-minimal,
census pin eb01cf2e. A new repo, entered on the
twenty-second enumeration and censused at theorem level
on its first sighting, by content: the proved model of
redundant computation and Pareto-optimal compression of
persistent data to its minimum representation, directed
by Chris on 2026-11-19. Fifty-three theorem declarations
in three Lean files on Lean 4.19.0: derivability from
persistent state (step closure, monotonicity in the
store and in the edges, and elimination of the already
derivable with the derivable set unchanged in both
directions); certificates for redundancy (run soundness
and monotonicity, checker soundness and monotonicity,
and composition at the run and checker levels); finite
candidate spaces (the candidate count a computed power
of the alphabet size); cost additivity over segments;
the domination bridge and the minimality checker's
soundness; minima by construction (the choice fold's
invariant, its output a minimum, existence in any
nonempty candidate list), with domination of a segment
lifting to the whole and a minimum of the whole having
minimum parts; and semi-persistence (readability
monotone in the store, version cost splitting, the kept
premise). Four adversarial controls stand in the tree
beside a general no-derivation result: axis relativity
of minimality, the unrecorded premise, the dropped
shared premise, and the cross-part tradeoff that part
minima need not compose. A synthesis file assembles the
family over the same definitions: the losses core
mirrored and discharged, baseline independence and
least cost from the profiling development proved here,
fold membership and retraction from the traceability
development proved here, and a joined theorem carrying
the remaining family results as restated hypotheses and
five named premises. The recorded gate log at the pin
ends in its axiom subset check passing, with 11 of the
52 printed theorems axiom-free, 19 on propositional
extensionality only, and 22 on the standard pair; the
one unprinted declaration is the sum append helper, its
axiom state unrecorded there. Carried at the repo's own
states: two campaign premises (edge faithfulness and
cost fidelity), candidate completeness and the
end-to-end methodology as proposed, and one executed
application whose full Pareto verdict stands unmeasured
with its blocking step named. State: PROVEN at the pin
on the recorded log, for the core above. The full
census stands in its annex file.

### 3.14 Placement from the twenty-second watch (2026-11-19) — a new proof repo

Stage 0 through 9 — software-is-bidirectional, census
pin b14fc92b. A repo that stood empty at the
twenty-second enumeration, entered on the twenty-third
and censused at theorem level on the first sighting of
its content, by content: the proved model of the
bidirectionality claim directed by Chris on 2026-11-19
— contracts, vanishingly and compoundingly small and
possibly independently derivable, bidirectionally
produce an optimally and speculatively optimizable
engineering and reengineering analysis for any set of
qualifications. Seventy-three theorem declarations in
three Lean files on Lean 4.19.0: the core model
(states up to equivalence as a join-semilattice, the
hyperlattice; derivability closure over recorded
steps; the analysis and synthesis maps with both round
trips and the reengineering round trip; independent
derivability of the contract by two routes under a
complete recording; smallness against the power of
two; speculation tracked by premise cones; bounds over
candidate lists, attained at both ends, compounding
and tightening monotonically under joins, with
certified optima at certified floors; the finite
candidate grid with its computed size and the decidable
optimum question; and every named measure with its
characterization — semantic mass, velocity as exact
mass change, the sound one-step redundancy test,
ordering optimality as the absence of descents, and
the exact suboptimality forms for scheduling, venue,
and test sets); the composition (the losses core
mirrored and discharged over identical definitions,
the persistence elimination result discharged in this
vocabulary, the recorded-state lattice discharging for
its class the general join-semilattice premise, and
the joined theorem assembling the whole method from
this model's theorems and the family's restated
hypotheses under six named premises); and four
standing controls (smallness can fail, the two routes
disagree on an incomplete recording, a join inside the
bounds tightens nothing, the content bound fails
without injectivity). The recorded gate log at the pin
ends in its axiom subset check passing: 74 audited
declarations printed — the 73 theorems plus the optimum
decision definition — 19 axiom-free, 27 on propositional
extensionality only, 28 on the standard pair, and no
classical choice anywhere. Carried at the repo's own
states: contract fidelity as the standing premise its
empirical census arm tests row by row (its first
tranche executed over three sibling inventories, round
trips passing), the content bound under injectivity,
the visibility vector, and time-varying re-solving as
proposed, and a ten-entry gap register, each gap owned
with its closing route. State: PROVEN at the pin on
the recorded log, for the model above. The full census
stands in its annex file.

### 3.15 Placement from the twenty-third watch (2026-11-19) — a repo newly proof-bearing

Stage 3 and 5 — idol-lib, census pin ad22a681. A repo
of the Idol family (the library ports) that stood
proof-free at every earlier enumeration, entered in the
proof family on the twenty-fourth enumeration and
censused at theorem level on the first sighting of its
proof content, by content: the Redundant empirical
reconstruction campaign landed in its tree in ten
commits, carrying a checked proof kernel and a measured
reconstruction atlas. Thirty-eight theorem declarations
in two Lean files on Lean 4.19.0, plus six checked
witness examples: the campaign kernel (25 theorems —
reconstruction injectivity under a round trip and the
history obstruction, intent axes under a factorization,
simulation and safety transfer, the joined effect
bound, the rewrite composer for contract and budget,
the commuting swap, idempotence composing under
commutation with the unconditional reading disproven by
a three-state counterexample, the keyed ledger quartet,
weighted cost monotonicity and the robust economic
bound, contract cover soundness, hypergraph derivation
soundness and witness reuse under retention, and the
finite minimum with its feasibility and declared-
universe optimality), and the atlas proofs (13 theorems
— gathering and the batch composer, the deduplicated
work lower bound, frontier exactness, sufficient state
and the distinguishing lower bound, the score update
and break-even laws, the Adler scan laws, and the
Bellman lower bound with its minimax certificate),
beside a generated witness file whose six examples are
checked by decision over the two recorded snapshots.
The kernel's recorded receipt at the pin is green and
hash-bound: 15 of its theorems depend on no axioms and
10 on propositional extensionality only, and this
census verified the receipt's source and checker hashes
against the tree. The atlas file's recorded axiom text
prints 10 of its 13 theorems (2 axiom-free, 1 on
propositional extensionality only, 5 on propositional
extensionality and quotient soundness, 2 on the full
standard set); the other three are unprinted there.
Five recorded negative controls stand rejected for the
kernel gate. Carried at the repo's own states: the
trust boundary as its standing premise — the theorems
concern the abstract campaign model, and every concrete
application owes the named hypotheses plus an
implementation-to-model refinement witness, which is
absent from the tree — and the wider campaign program
(the Ocean execution model carried end to end, the
public surface) as proposed, with the atlas
measurements standing as measured and constructed
evidence at their recorded scopes. State: PROVEN at the
pin on the recorded, hash-bound evidence, for the
theorems above. The full census stands in its annex
file.

Restated by the twenty-fourth watch (2026-11-19) at the
new census pin 4dee2311: the campaign landed its Pareto
release condition in three commits — a new proof package
of 27 theorems in one Lean file, proving Pareto
unimprovability in its abstract models (the strict
relation, the global witness and its coverage forms, the
weighted score results, five standing counterexamples
among them the zero-weight and composition negations,
bounded uncertainty, and the retention model with its
concrete optimal instance), with its recorded receipt
kernel-checked and hash-bound, its source and checker
hashes verified firsthand by that watch, and five
recorded negative controls rejected. The 38 theorems at
the first pin stand unchanged, every earlier Lean file
byte-identical at the new head, so the repo now carries
65 theorems in three theorem files beside the six
checked witness examples. Carried at the repo's own
states: the abstract-model scope as its premise, and
actual-software release admission under the new
requirement as open — the model certificates satisfy
their named obligations and the release command refuses
admission. State: PROVEN at the new pin on the recorded,
hash-bound evidence. The re-census stands in its annex
file.

## 4. Duplication and stronger homes

From the topology census, carried as rulings:

- Fold and compounding: software-optimality is the stronger
  home (inductive derivability with exact compounding and
  order independence, axiom-free) over
  software-is-quantifiable's value-level fold. The value-level
  fold remains the accounting's presentation form.
- Coloring: software-optimality is the stronger home — the
  side condition of the quantifiable coloring becomes the
  checked face's executable gate. The quantifiable fixed
  point and its counting bound remain its own.
- Pareto: NEITHER repo dominates. The interval-bounds
  separation and the per-execution disproof exist only in
  software-is-quantifiable; the n-axis integer frontier only
  in software-optimality. The ruling is a join, not a pick:
  one Pareto theory with both halves is a closure item.
- Metric relevance: the nonaggregated Lean profile is the
  design; the spec section 26 scalar stays proposed (section
  3.2, stage 9).
- Pure duplication: software-is-solvable's closure and
  executable-closure modules are byte-identical to
  software-optimality's files of the same names (verified by
  diff at census time) — two homes, one content, drift risk
  only; a dominated point of the purest form. Its unique
  content is placed in section 3.5. software-is-composable
  likewise carries 45 byte-copied upstream modules from
  software-optimality, checksum-verified in its own repo,
  under its 49 own theorems (section 3.3).
- Toolchain split: quantifiable stands on Lean 4.15.0, the
  rest of the proof family on 4.19.0. Porting the
  quantifiable results to 4.19, or proving they follow from
  the 4.19 homes, is a closure item (topology item 7).

### 3.3 software-is-composable — census pin 033c12c0, Lean 4.19.0

Evidence-state note (2026-11-18, relayed audit): an external
audit relayed the same night audited this repo at the earlier
pin 929d8e35 — the skeleton — and states it holds no Lean
proof, claimed-not-proven. That verdict is true at the pin
the audit names; the proof below landed after it, at the
census pin. The audit is relayed and unverified, a
verification lane is reproducing its executable core, and
until that lane reports this repo's state is carried at the
lower of the two readings wherever they conflict. See
section 6.

This repo moved during its census: at first read it was a
skeleton (readme and toolchain, zero code); its pull request
landed the full proof the same hour and this census is of the
landed head. 94 theorems: 49 its own, 45 byte copies from
software-optimality (checksum-verified in-repo), plus one
import — only the finiteness module — from
software-is-quantifiable. Its own check script runs two
negative controls and treats warnings as errors; its recorded
log gives per-theorem axiom lists for all 19 headline claims
(subsets of the three standard axioms, several empty). The
census did not re-run the build; the build evidence is the
repo's recorded log, labelled as such.

Thesis: release admission, symbol by symbol — a new release
is admitted over an old one exactly when every old symbol is
present, keeps every behaviour, keeps the same number of cost
axes, never raises a cost upper bound, and both sides have
valid bounds. Admission is monotone and composes; an
incremental recheck of exactly the affected set agrees with
a full recheck.

Stage 8 — the Incremental module (3 theorems), the headline.
The caller closure of the changed set is exactly the
hypergraph module's affected set. The recheck equivalence:
under two carried premises — the old release's bounds are all
valid, and every symbol outside the affected set is literally
unchanged — full release admission holds if and only if every
affected symbol passes its individual check. And a DISPROOF:
rechecking only the edited symbol is not enough (a concrete
pair where the edited symbol passes, its caller is in the
closure, and the whole release is refused).

Stage 8 — the Admission module (13 theorems). The executable
admission test is true exactly when the propositional
admission relation holds; symbol admission is reflexive given
valid bounds (a carried premise) and transitive; release
admission composes along chains; the per-symbol verdict's
admitted case is characterized exactly (refusal-reason
correctness is not part of that theorem).

Stage 8 — the Monotonicity module (6 theorems). An admitted
step keeps every qualified behaviour of every old symbol, and
the inclusion composes along two steps; an admitted step does
not strictly dominate the old symbol on upper bounds (side
condition: axes in range), and non-regression composes. One
DISPROOF, the repo's own: per-execution cost monotonicity is
false — bounds 1..100 admitted to 2..3 yet an execution value
3 exceeds 1. This is the composable form of the per-execution
exclusion placed at stage 5 from quantifiable.

Stage 2 — the Composition module (11 theorems). Per-module
admission implies whole-release admission under a named side
condition — interaction closure: every call stays inside one
module — plus module coverage and unique identifiers. And a
counterexample DISPROOF: with one cross-module call and a
stubbed callee, both modules are admitted separately while
the composed release is not — the side condition cannot be
dropped.

Stage 1 and 3 — the Evidence module (13 theorems) and
Finiteness (1). Fixing a prefix of independent bits leaves
exactly 2-to-the-free-bits candidates; the candidate set is
duplicate-free; filtering to one member gives the singleton.
Two DISPROOFS by computation: observing the same bit twice
does not shrink the candidate set again, and one
disqualifying bit does not empty it. One PREMISE, the repo's
own label: given a total coverage observation (one Boolean
per symbol, supplied as a structure), filtering leaves
exactly one candidate — coverage is carried, not produced;
the same premise as stage 3's platform premise, in
per-symbol form. The schedule space is finite, by direct
application of the imported finiteness theorem.

Stage 7 — the Examples module (2 theorems): the worked pair
computes exactly "symbol 1 admitted; symbol 7 refused for
cost regression on axis 0", and the pair's admission test
computes false.

Non-claims carried: platform execution coverage is not
imported and not proved (the sibling's Pareto and Coverage
modules at the import pin do not typecheck on Lean 4.19.0 and
are excluded); the copied modules are acknowledged as another
repo's bytes; admission controls upper bounds, not every
individual execution value.

### 3.4 software-is-incrementally-certifiable — census pin f3b9f896

Theorem count at the live head: 0. The repo at its pin is a
single readme sentence asserting a finished Lean 4 proof
that incremental monotonic certification is extensive and
yields Pareto-optimal dominance across releases. No Lean
code, no toolchain pin, no check log. State: CLAIMED, NOT
PROVEN — a claim with neither spec nor proof in the repo,
hence a work order, not a result. (The relayed external
audit concurs at this pin; section 6.)

Its intended content exists as a stand-in module (14
theorems) on software-is-incrementally-safe's unmerged
branch, censused there and placed here as an annex, not as
this repo's theorems: the certification closure is extensive,
monotone, and idempotent; the componentwise cost order is
reflexive and transitive; dominance implies the order; one
DISPROOF — dominance is irreflexive; admission is
definitionally closure membership plus a componentwise cost
bound (both inputs); admission is downward closed. Five of
the fourteen are interface obligations that hold by
definition. The stand-in proves no existence or maximality
theorem, so the readme's "Pareto-optimal" wording is
stronger than anything the stand-in states. The stand-in
carries equivalence obligations so a real dependency could
replace it if this repo ever exports the same operations.

### 3.5 software-is-solvable — census pin 815e125f, Lean 4.19.0

48 named theorems plus 35 kernel guards; the check script
bans sorry, admission, axiom, and native-decision tokens and
compiles with warnings as errors; the check log prints axiom
dependencies per theorem (many empty; the executable bridge
theorems carry the standard three). Thesis: witness-compounding
search over a finite behavioral hypergraph is exactly
solvable — least closure is append-monotone, compounds across
premises, and yields exact resolution and catalogue
accounting. Saturation, colors, matrices, and catalogues are
derived views, not the authority — the stage 4 discipline in
this repo's own statement.

Duplication, stated plainly: its closure core (10 theorems)
and executable closure (13) are byte-identical to
software-optimality's modules of the same names (section 4).
The placements below are its unique content.

Stage 4 — the Hyperlattice module (15 theorems). Joining
graphs is pointwise on roots and edges; knowledge (the
derivation set) is monotone under extension and equal for
equal graphs; join is commutative, associative, idempotent.
The headline compounding: knowledge of a join equals
knowledge of the join of the two saturated graphs, reclosed —
merely unioning old closures is explicitly not the claim.
Redundancy: appending only already-known roots under closed
knowledge changes nothing. The resolution vector (per-axis
counts of supported probes) has exact accounting: counts are
monotone, strictly increase exactly when a novel witness
exists, and the marginal gain telescopes exactly. Resolution
expansion per coordinate is proven under a carried premise —
both Boolean classifiers are exact for their graphs. The live
projection (withdrawal) creates no support.

Stage 2 and 7 — the WitnessExecutable module (10 theorems).
Appending batches is exactly joining their authority graphs;
the executable classifier is exact for a batch's graph under
the boundedness side condition (roots and edge heads inside
the universe); resolution after an append is coordinatewise
no smaller; the catalogue has exactly 2-to-the-closure-length
entries; after an append, catalogue entries multiply by
exactly 2-to-the-closure-length-delta (a duplicate append has
delta zero) — counted before any qualification filter; the
qualified list is exactly the catalogue filtered by a supplied
total Boolean gate, whose correctness is a premise, not a
theorem.

Stage 2 — its one DISPROOF is the shared no-bootstrap:
under the side premise that every rule has at least one
premise, an empty root set derives nothing — cycles alone
create no support.

Premises carried (consolidated): admission and authentication
of roots and edges are prerequisites, not proved; semantic
truth of roots and truth preservation of rules are assumed by
the soundness theorem; classifier exactness as above;
boundedness for every executable bridge; the qualification
gate is supplied; withdrawal input is an already-resolved
projection. Non-claims carried: the resolution vector is a
lower bound on resolved support in the named probe scopes —
not remaining runtime, not confidence, not a count of feasible
designs; the catalogue count does not claim every subset is
executable or optimal; hashing is not semantic equivalence;
colors are information statuses, not a quality ordering; the
reference enumeration is exponential and no production
performance win is claimed; an external system is not verified
merely because it can emit this model.

### 3.6 software-frontier-is-solvable — census pin c7ffc6d0, Lean 4.19.0

14 named theorems, every one with a printed axiom line in
the check log (standard axioms or none), plus 15
kernel-reduced examples. Thesis: exact finite Pareto
frontiers are computable from supplied eligibility and
integer cost views, with exact insertion and retraction
updates. A standalone companion that introduces no second
graph or evidence store.

Stage 5 — the Frontier module (all 14). Dominance is
irreflexive and transitive, and equal cost vectors never
dominate (three negation theorems). The insertion equation:
under irreflexivity, frontier membership after inserting a
candidate is exactly "old member not dominated by the new
one, or the new one dominated by no old eligible candidate".
The retraction equation, the headline: after removing a set,
a survivor is on the frontier exactly when it is eligible,
not removed, and every former eligible dominator of it was
removed — all dominators accounted for. A frontier member
survives a retraction that spares it; a live dominator blocks
resurrection (negation theorem). Frontiers defined by
pointwise-equal eligibility and dominance views coincide —
storage layout is irrelevant. The executable evaluator's
membership is exactly the propositional frontier; the Boolean
finite-axis comparison is exactly "no worse on every listed
axis and strict on one" (an empty axis list makes everyone
tie). Existence: under a strict partial order, any nonempty
candidate list has a frontier member. The baseline guard: a
guarded-frontier member is no worse than the baseline on
every selected objective and is globally nondominated, and
the guarded frontier is nonempty while the baseline stays in
the list and eligible.

Two DISPROOFS by concrete counterexample, the repo's own:
Pareto membership does not imply no regression against a
baseline (a frontier member strictly worse than the baseline
on the first axis) — membership alone is not a regression
guarantee, which is what the separate guard is for; and
frontier-only storage loses information exact retraction
needs (two populations with the same frontier whose
post-retraction frontiers differ) — dominated candidates, or
equivalent source data, must be retained. This second
disproof is the frontier form of stage 4's accounting law:
the fold keeps the witness set, not its frontier projection,
for exactly this reason.

Premises carried: eligibility, costs, and the dominance
relation are supplied by the caller; generator completeness
is not proved; identity normalization is upstream.
Non-claims carried: no runtime measurements; the evaluator
is a full-scan reference oracle of order m-squared-times-a,
not an optimized runtime; no global optimum beyond the
supplied population.

### 3.7 software-is-incrementally-safe — head 94661358; content on branch 5c1006a6

At the live head: one file, the toolchain pin (Lean 4.19.0).
Theorem count at head: 0, no readme — the repo states
nothing at its pin; its thesis lives in the repo description:
safety preserved incrementally across releases, with
noninterference and monotone capability shrinkage, built on
software-is-composable. State at head: CLAIMED, NOT PROVEN
(the relayed external audit concurs at this pin; section 6).

All proof content is on the unmerged pull-request branch
(open pull request 1), censused at branch pin 5c1006a6 and
placed here as branch content, never as head results: 54
theorems in its own five modules, plus 32 in two stand-in
modules (the composable stand-in, 18; the certifiable
stand-in, 14, placed in section 3.4). Evidence caveat,
stated once: the branch has no check log and no printed
axiom audit in the repo; no sorry token was found by search;
the build and axiom claims rest on the pull-request body's
quoted log — labelled as such, not independently re-run.
Strength caveat, equally binding: the theorems of this
section are carried at exactly the strength the relayed
external audit states — section 6, findings F1–F5 — and
nowhere above it.

Stage 8 — the Increment module (6 theorems), the headline:
given a safe base release and the closure hypothesis for a
delta (every symbol in the delta's dependency cone is
inspected — a named premise, assumed throughout), cone
acceptance of the delta holds if and only if the applied
release is safe from scratch. Checking the cone is exactly as
good as rechecking everything. Chain forms: stepwise
incremental acceptance of a chain is equivalent to every
release in the chain being safe from scratch (under per-step
closure hypotheses), and the composed delta of a whole list
bridges the two.

Stage 8 — the Safety module (13 theorems). A safety property
is a fixed point of the certification closure, equivalently a
downward-closed property; per-symbol safety is equivalent to
trace safety for a release; safety descends along the release
order; allowed traces are prefix-closed.

Stage 8 — the Security module (9 theorems). Cone acceptance
preserves the capability bound (every reachable observation
within its symbol's allowance), in single and chain form;
monotone capability shrinkage — a delta monotone in the
composable sense preserves allowance without the closure
hypothesis, monotonicity substituting for checking;
noninterference is preserved (low symbols' reachable
observations stay not-high), in single and chain form;
forbidden-symbol emptiness is preserved. One DISPROOF: under
the policy premise that a forbidden symbol's allowance is
empty, a delta that activates a forbidden symbol cannot be
cone-accepted — the negation is proved.

Stage 6 — the Checker module (24 theorems). The executable
checker is characterized exactly on both sides: it accepts
exactly when no cone symbol is uninspected, none is a
forbidden hit, none has an unsafe reachable observation, and
the cost test passes; it refuses naming the first failure in
a fixed priority order, and the refusal is correctly named.
The executable cone and the observation collection are proven
SOUND only — every computed cone member is a true cone
member, every collected observation truly reachable — with
no completeness converse anywhere; the census flags this
twice and the synthesis carries it. Side condition: the
executable cost test uses one number for both the time and
compute bounds. The Example module (2 theorems) computes the
two verdicts: a delta activating the designated forbidden
symbol is refused by that symbol's name; a benign delta is
accepted.

Premises carried (branch, consolidated): the closure
hypothesis and cone acceptance per delta; base-release
safety, noninterference, and forbidden-emptiness are assumed,
never established for a concrete release in the abstract
modules; the empty-allowance policy premise; the
monotonicity premise where it substitutes for checking.

### 3.8 The two claim shells — regress and review

software-doesnt-have-to-regress (pin 24d36c13) and
software-doesnt-need-review (pin ae5f3918) each contain a
two-line readme and nothing else: no Lean files, no toolchain
pin, no check log. Theorem count 0 in both. States: CLAIMED,
NOT PROVEN (the relayed external audit concurs at these pins;
section 6).

- doesnt-have-to-regress claims a release process with
  per-symbol observed-behavior certification never has to
  regress. Its proven content today lives elsewhere and is
  partial: the regression gate exactness of
  software-is-quantifiable (stage 5), the baseline guard of
  software-frontier-is-solvable (stage 5), and the admission
  monotonicity of software-is-composable (stage 8) each prove
  a component; the release-level statement itself — a
  per-symbol certified release process whose every step is
  monotone across releases — is proven nowhere. The topology
  census names this the monotonicity family's genuine open
  point: the family (composable, certifiable, safe, regress)
  is one claim family at different scopes, to be stated once
  at its strongest scope with each shell dispositioned
  against it.
- doesnt-need-review claims a proof of when manual review is
  redundant given per-symbol certification, plus a proposal
  to replace it. A different claim — a sufficiency statement
  about review, not a monotonicity statement. Its proven
  content today is zero and its design content is one line;
  it stands as its own open point. The settled boundary from
  the wider record applies: there is a feasible path to
  eliminating routine human review within a defined scope,
  and no sound general guarantee that humans will never need
  to review contracts, exceptions, or consequences of
  arbitrary software — any future proof here sits inside that
  boundary or refutes it, and the synthesis presumes neither.

### 3.9 The tenth repo — announced, not landed

software-is-more-traceable-than-you-think was announced
2026-11-18 01:30 PST (a historical witness hypergraph at
symbol grain, with a Lean proof that the construction holds
independent of operating system, software, and language —
which, when landed and checked, places at stages 3 and 4:
witnessing and accounting, at the finest grain). Read back at
01:32 PST it did not yet exist. It is carried in the census
as an announced entry, colored unknown, and enters at census
depth on the continuous job's next re-enumeration after it
lands. (Sweep update: it has since landed and is placed in
section 3.10 at its census pin.)

## 6. Evidence-state update — relayed external audit (unverified)

An external audit of the nine proof repos was received from
Chris on 2026-11-18 01:35 PST and is saved in the workspace
(~/workspace/research/software-family-audit-2026-11-18.md).
Status of everything in this section: RELAYED, UNVERIFIED at
receipt. A verification lane is reproducing the audit's
executable core (its counterexample file, kernel-checked at
the audited pins); where this section and a firsthand census
in section 3 conflict, the claim is carried at the lower
state until the lane reports. The audit tied every verdict
to a named pin and noted repos were being pushed during the
audit; several of its pins are earlier than this synthesis's
census pins, and the differences are recorded, not smoothed.

Hygiene (relayed): across the family at the audited pins, no
sorries, no admissions, no custom axioms, no
kernel-skipping constructs — the only hits were two harmless
resource options in one campaign module; every printed axiom
set is a subset of the three standard axioms; all five
buildable repos compile with warnings as errors. "The
theorems are true as stated. The questions are what they
state and what they assume."

The four claimed-not-proven repos: the audit states
software-is-composable (at its audited pin 929d8e35),
software-is-incrementally-certifiable (f3b9f896),
software-doesnt-need-review (ae5f3918), and
software-doesnt-have-to-regress (24d36c13) hold no Lean proof
at their default heads. For the last three this synthesis's
firsthand census concurs exactly (sections 3.4 and 3.8,
states updated to CLAIMED, NOT PROVEN). For composable the
audit's pin predates the landing its census here records
(section 3.3 carries both readings and the lower-state rule).
The audit adds one deflation that applies to the composable
content wherever it lives: the admission model's composition
holds inside interaction closure — the model rules out
emergent interaction by construction rather than checking
it. This synthesis's census records the same boundary from
the other side (the counterexample showing the side condition
cannot be dropped).

software-is-quantifiable (relayed): audited at ba27febf —
this synthesis's head-at-synthesis pin — with 63 theorems
and a passing lake build (the census here read 46 theorems
at the earlier pin 37917a41; the growth is the topology
lane's landed work between the two reads, and is the
continuous job's re-synthesis input). The audit confirms the
coverage claim is a named premise by the repo's own README:
the coverage theorem is literally the premise structure's
mediation field restated, and the sensor-below field is an
arbitrary proposition that can be True. Section 3.1 already
carries coverage as PREMISE; the audit concurs, and adds
that the premise as stated is weaker than its name suggests.

software-optimality (relayed): audited at af23f5d with 26
files and 172 theorems, build passing (census here: 14
modules at 0ea4626b; the repo grew between reads). Verdict:
proven as stated; the name overclaims — "optimal" means
nondominated within a supplied finite candidate list under a
supplied integer cost model, which is exactly the boundary
section 3.2 carries. Behavior preservation in the accepted-
improvement theorem is a supplied soundness hypothesis passed
straight through — carried here as the premise it is.

software-is-solvable and software-frontier-is-solvable
(relayed): proven as stated at the census pins. The audit
confirms the byte-identity of solvable's two core modules
with optimality's by hash. For frontier-is-solvable it adds:
the repo does not import the hypergraph it says it is derived
from — that link is by convention only.

software-is-incrementally-safe — its theorems are carried at
exactly this strength (relayed findings F1–F5, audited on the
unmerged branch at de1b3071, an earlier branch pin than this
census's 5c1006a6; the findings are about the model's
definitions and so read across the branch's movement):

- F1. Its "safety" is per-event allow-list membership. Traces
  are lists, but the verdict asks only whether each element
  is allowed; order is invisible. An ordering property —
  never open before stop — cannot be expressed. Its safety-
  property notion is downward closure of observation sets,
  which coincides with allow-lists.
- F2. Its "noninterference" is taint reachability: a low
  symbol never reaches an observation tagged high. It is not
  the pair-of-runs hyperproperty the name usually denotes;
  two systems, one outputting a secret bit and one outputting
  noise, can have identical profiles and are treated the
  same. Timing channels and implicit flows are outside the
  model.
- F3. Every abstract preservation theorem rests on the
  closure hypothesis — a complete and correct dependency
  relation, static between symbols, which must include every
  path by which behavior can change (data, configuration,
  shared state, timing, hardware). Given sound dependencies,
  the headline equivalence is the right theorem.
- F4. The executable checker is not connected to the abstract
  theorems: no theorem takes a checker acceptance to release
  safety or to the NI property; the computed cone is proven
  sound, not complete. The checker trusts the submitter: the
  delta carries its own dependency edges, inspection set,
  high/low labels, and both budgets, and the audit's
  counterexamples show the same change refused with an honest
  delta and accepted after dropping one edge, unlabelling one
  observation, or raising one budget. Its change cost counts
  observation-list lengths and calls them time and compute
  (this synthesis's census records the same one-number fact
  as a side condition).
- F5. Nothing in the model requires liveness: the release
  with no behavior satisfies every allow-list, every NI
  condition, and the monotonicity premise. Doing nothing is
  maximally safe in this model; liveness and availability are
  out of scope.

Cross-repo findings carried as structural facts (relayed):
the family's two monotonicity directions point opposite ways
— in the composable/safe line, the new release's behaviors
must be a subset of the old (nothing new appears); in
quantifiable, the candidate must contain every qualified
behavior (nothing qualified disappears) — and no repo states
which a release process should enforce or how they combine.
And the safe branch pins its siblings at commits that hold
no Lean code (composable 929d8e3, certifiable f3b9f89), with
its quantifiable pin already behind that repo's head.

What the auditor could not check (relayed): the Python
experiments and evidence bundles behind the campaign timing
claims were not opened — those claims stand unverified
beyond the Lean arithmetic; four unmerged branches were not
audited.

## 7. Watch update — 2026-11-18, the second hourly re-synthesis

The second watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors. Twenty
repos had moved since the sweep pins, none were new, none
were gone, and the paper source hash was unchanged, so no
paper re-sync was owed. Fifteen of the twenty are proof
repos, four are other idol-family repos, and one is this
repo itself. The annex watch deltas carry the mechanical
counts at the fresh heads; the placements in section 3 stand
at their census pins, with re-census owed at the new heads,
except where this section records a change of kind.

Two repos changed in kind at the head. The certifiable repo,
whose thesis stood claimed and not proven at its head, now
carries a full library at its head: certification closure
modules with a recorded check log ending in a pass, a claims
table marking the closure results proven and one union
reading disproven, and five named premises. The safe repo,
whose head likewise carried only a worked example with its
branch content unmerged, now carries a full library at its
head: model, cone, check, and increment modules with an
audit folder, and a claims table marking its first findings
proven; no recorded check log stands in its head tree. Both
state changes are recorded here at the strength the trees
themselves state; a full theorem-level census of each at
its new pin is owed before their section 3 placements move.

The remaining movement is growth in place: a coordinated
range example landed in eleven proof repos and in this
repo; the frontier repo gained five library files beside
its example; the optimality repo gained eight root modules
beside its example; the quantifiable repo gained its range
example and one verification controls file; the theses repo
gained a solver dominance file. The mechanical name
comparison, one method at both heads, found no lost name in
any moved proof repo: every proven set grew or held. The
idol repo's one Lean file is byte-identical at its census
pin and at the fresh head, so its proof-bearing content is
unchanged. This repo's own proven count grew from three
theorems to eleven with its range example, re-censused in
full in its annex at the new pin.

## 8. Watch update — 2026-11-18, the third hourly re-synthesis

The third watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors.
Thirty-six repos had moved since the last recorded heads,
none were new, none were gone, and the paper source hash
was unchanged, so no paper re-sync was owed. Five of the
thirty-six are proof repos, two are other idol-family
repos, and twenty-nine are long-tail repos. The annex
watch deltas carry the mechanical counts at the fresh
heads; the placements in section 3 stand at their census
pins, with re-census owed at the new heads, except where
this section records a change of kind.

The optimality repo grew in place: eleven new Lean files —
a root module on the executable incremental form, and
composition developments on axiom audit, exhaustive edits,
identity and representation, and incremental selection —
taking its mechanical count from 557 declarations to 684,
with no name lost. The safe repo grew in place in its
model, cone, check, and ordered increment modules, from
131 declarations at the last recorded cloned head to 148,
with no name lost. The composable repo did not change in
content: its count and its name set stand as recorded,
and its movement is a dependency re-pin in its lake file.

One change of kind is small but real. The idol repo's
frontier file is unchanged, but a release tools Lean
development that landed after the sweep census grew in
this window: its retention file gained four declarations
and a new qualification file with five declarations stands
beside it, both free of sorry tokens by the watch scan and
neither covered by a check log this watch read. It is
placed in the idol annex delta at that strength; a full
census of it is owed.

The remaining movement is pin movement only. The two other
idol-family repos and the twenty-nine long-tail repos were
read by tree at their fresh heads; no proof-assistant
source was found in them, with one stated limit: one
long-tail tree was large enough that its read came back
truncated, and no proof-assistant source stood in the
returned portion — its proof-free determination stands
from the sweep, and the truncated read is recorded here
rather than hidden. This repo's own head moved only by
the second watch landing itself; its eleven theorems
stand unchanged.

## 9. Watch update — 2026-11-18, the fourth hourly re-synthesis

The fourth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors.
Eighty-eight repos had moved since the last recorded heads,
none were new, none were gone, and the paper source hash
was unchanged, so no paper re-sync was owed. Three of the
eighty-eight are proof repos, two are other idol-family
repos, and eighty-three are long-tail repos. The annex
watch deltas carry the mechanical counts at the fresh
heads; the placements in section 3 stand at their census
pins, with re-census owed at the new heads, except where
this section records a change of kind.

The safe repo grew in place and discharged a premise: one
merged change added a module proving the natural-number
text representation injective, and the merge record states
the string cone hypothesis is discharged by that proof.
Its count rose from 148 declarations to 151, with three
names gained and none lost; no recorded check log stands
in its head tree.

The idol repo gained a third Lean development: a history
file in the solver benchmarks incidence folder, carrying
ten theorems on witnessed derivation histories and finite
solver costs, landed at the head's merge. Its frontier
file and both release tools files are byte-identical at
the last recorded head and the fresh head, so the
proof-bearing content the earlier censuses recorded is
unchanged. No check log covering the new file was read in
this watch; its gate state is unknown and a full census
of it is owed.

The remaining movement is pin movement only. The two other
idol-family repos and the eighty-three long-tail repos
were read by tree at their fresh heads; no proof-assistant
source was found in them, and no tree read was truncated
this watch. The one apparent hit, a long-tail repo whose
tree carries many files with a proof-assistant extension,
is the V-language example set the sweep already resolved
as not Coq; it remains proof-free by the named check. This
repo's own head moved by one ledger addendum commit from
another lane; its eleven theorems stand unchanged.

## 10. Watch update — 2026-11-18, the fifth hourly re-synthesis

The fifth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors.
Six repos had moved since the last recorded heads,
none were new, none were gone, and the paper source
hash was unchanged, so no paper re-sync was owed.
Three of the six are proof repos and three are other
idol-family repos; there was no long-tail movement
this watch. The annex watch deltas carry the tree
evidence at the fresh heads; the placements in
section 3 stand at their census pins, with re-census
owed at the new heads.

Both moved proof repos moved without touching their
proof content. In the idol repo every Lean file is
byte-identical between the two heads — the frontier
file, both release tools files, and the solver history
file all stand at the same blobs — and the movement
is compiler and gate work. In the semi repo the
movement is addition only: ten new files of analysis
and parity tooling, with every Lean and Rust file
unchanged, so the largest proof tree in the estate
stands at the fresh head with its content and its
gate state exactly as the sweep census recorded them.
One placement fact does change: the semi repo's mirror
did not move, so the two no longer stand at one head;
their proof content remains identical, and the
divergence is recorded in the annex delta and the
ledger.

The three other idol-family repos — the compiler port,
the library, and the relay — were read by tree at
their fresh heads; no proof-assistant source was
found in any of them and no tree read was truncated,
so they remain proof-free by the named check. This
repo's own head moved only by the fourth watch
landing itself; its eleven theorems stand unchanged.

## 11. Watch update — 2026-11-18, the sixth hourly re-synthesis

The sixth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors.
Two repos had moved since the last recorded heads,
none were new, none were gone, and the paper source
hash was unchanged, so no paper re-sync was owed.
One of the two is a proof repo — this repo itself —
and the other is an idol-family repo; there was no
long-tail movement this watch. The annex watch delta
carries the tree evidence at the fresh head; the
placements in section 3 stand at their census pins,
with re-census owed at the new head.

This repo's own head moved only by the fifth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The other moved repo — the compiler port — was read
by tree at its fresh head: the tree stands at the same
count of files as at its last recorded head, with no
file added or removed and two files changed, a slices
record and one Idol source file. No proof-assistant
source was found in its tree and the tree read was
not truncated, so it remains proof-free by the named
check. Its movement changes its pin only, not its
placement.

## 12. Watch update — 2026-11-18, the seventh hourly re-synthesis

The seventh watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors.
Three repos had moved since the last recorded heads,
none were new, none were gone, and the paper source
hash was unchanged, so no paper re-sync was owed.
One of the three is a proof repo — this repo itself —
and the other two are idol-family repos; there was no
long-tail movement this watch. The annex watch delta
carries the tree evidence at the fresh head; the
placements in section 3 stand at their census pins,
with re-census owed at the new head.

This repo's own head moved only by the sixth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
the tree stands at the same count of files as at its
last recorded head, with no file added or removed and
two files changed, a slices record and one Idol source
file. The relay was read by tree at its fresh head:
one file added, a dated coordination note, and no file
changed or removed. No proof-assistant source was
found in either tree and neither tree read was
truncated, so both remain proof-free by the named
check. Their movement changes their pins only, not
their placements.

## 13. Watch update — 2026-11-18, the eighth hourly re-synthesis

The eighth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors in the
final reads. Four repos had moved since the last recorded
heads, none were new, none were gone, and the paper source
hash was unchanged, so no paper re-sync was owed. One of
the four is a proof repo — this repo itself — and the
other three are idol-family repos; there was no long-tail
movement this watch. The annex watch delta carries the
tree evidence at the fresh head; the placements in
section 3 stand at their census pins, with re-census owed
at the new head.

This repo's own head moved only by the seventh watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
eighteen commits stand between the two heads, its tree
gained one file, a semantic checker source, and two files
changed, a slices record and a graph lowering source. The
relay was read by tree at its fresh head: one file added,
a dated audit note, and no file changed or removed. The
sites repo was read by tree at its fresh head: seventy
files added, a new prompt board space with its audits,
and four files changed; the paper page file stands at the
same tree entry at the two heads, which is the tree
evidence behind the unchanged paper hash. No
proof-assistant source was found in any of the three
trees and no tree read was truncated, so all three remain
proof-free by the named check. Their movement changes
their pins only, not their placements.

## 14. Watch update — 2026-11-18, the ninth hourly re-synthesis

The ninth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors. Two
repos had moved since the last recorded heads, none were
new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the two
is a proof repo — this repo itself — and the other is an
idol-family repo; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the eighth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
ten commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a semantic checking source. No proof-assistant
source was found in its tree and the tree read was not
truncated, so it remains proof-free by the named check.
Its movement changes its pin only, not its placement.

## 15. Watch update — 2026-11-18, the tenth hourly re-synthesis

The tenth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors. Three
repos had moved since the last recorded heads, none were
new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the three
is a proof repo — this repo itself — and the other two are
idol-family repos; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the ninth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
seven commits stand between the two heads — the
enumeration read caught the repo mid-movement at an
intermediate head, and the individual verification read
at the fresh head recorded here governs — no file was
added or removed, and two files changed, a slices record
and a semantic checking source. The relay was read by
tree at its fresh head: two commits stand between the
two heads, two files were added, a dated relay note and
a dated audit note, and no file changed or removed. No
proof-assistant source was found in either tree and
neither tree read was truncated, so both remain
proof-free by the named check. Their movement changes
their pins only, not their placements.

## 16. Watch update — 2026-11-18, the eleventh hourly re-synthesis

The eleventh watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors. Three
repos had moved since the last recorded heads, none were
new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the three
is a proof repo — this repo itself — and the other two are
idol-family repos; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the tenth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
eight commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a semantic checking source. The relay was read by
tree at its fresh head: one commit stands between the
two heads, one file was added, a dated relay note, and
no file changed or removed. No proof-assistant source
was found in either tree and neither tree read was
truncated, so both remain proof-free by the named check.
Their movement changes their pins only, not their
placements.

## 17. Watch update — 2026-11-18, the twelfth hourly re-synthesis

The twelfth watch re-enumerated the estate completely: 565
repos, every head read individually. Three first reads
failed; each was re-read individually — two matched their
last recorded heads and one proved empty, matching its
recorded empty state — so the final reads carry no errors.
Two repos had moved since the last recorded heads, none
were new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the two
is a proof repo — this repo itself — and the other is an
idol-family repo; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the eleventh watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
twelve commits stand between the two heads, one file was
added, a type checking source, and two files changed, a
slices record and a semantic checking source, with no
file removed. No proof-assistant source was found in its
tree and the tree read was not truncated, so it remains
proof-free by the named check. Its movement changes its
pin only, not its placement.

## 18. Watch update — 2026-11-18, the thirteenth hourly re-synthesis

The thirteenth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors. Three
repos had moved since the last recorded heads, none were
new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the three
is a proof repo — this repo itself — and the other two are
idol-family repos; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the twelfth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
thirty-four commits stand between the two heads, six
files were added, all checking sources, and two files
changed, a slices record and a checking source, with no
file removed. The relay was read by tree at its fresh
head: two commits stand between the two heads, two files
were added, a dated audit note and a dated relay note,
and no file changed or removed. No proof-assistant
source was found in either tree and neither tree read
was truncated, so both remain proof-free by the named
check. Their movement changes their pins only, not their
placements.

## 19. Watch update — 2026-11-18, the fourteenth hourly re-synthesis

The fourteenth watch re-enumerated the estate completely: 565
repos, every head read individually, no read errors. Two
repos had moved since the last recorded heads, none were
new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the two
is a proof repo — this repo itself — and the other is an
idol-family repo; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the thirteenth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
sixteen commits stand between the two heads, four files
were added, all checking sources, and one file changed,
a slices record, with no file removed. No proof-assistant
source was found in its tree and the tree read was not
truncated, so it remains proof-free by the named check.
Its movement changes its pin only, not its placement.

## 20. Watch update — 2026-11-18, the fifteenth hourly re-synthesis

The fifteenth watch re-enumerated the estate completely: 566
repos, every head read individually. One first read failed
on a transport error; it was re-read individually and proved
empty, matching its recorded empty state, so the final reads
carry no errors. Three repos had moved since the last
recorded heads, one was new, none were gone, and the paper
source hash was unchanged, so no paper re-sync was owed. One
of the moved repos is a proof repo — this repo itself — the
new repo is a proof repo, and the other two moved repos are
idol-family repos; there was no long-tail movement this
watch. The annex files carry the evidence at the fresh
heads; the placements in section 3 stand at their census
pins, with re-census owed at the new head of this repo, and
the new repo's placement stands in section 3.11 at its
census pin, which is its head.

This repo's own head moved only by the fourteenth watch
landing itself: the four commits between the two heads are
that watch's annex, placement, ledger, and pins commits, and
no Lean file changed among them, so its eleven theorems
stand unchanged at the fresh head.

The new repo, the profiling proof repo, was read in full at
its head and censused at theorem level in its annex: twenty
declarations, three controls, a recorded gate log passing
at the head, one carried premise, and its proposed and open
items at the states its own spec states. It is
proof-bearing by content, found on its first enumeration.

The compiler port was read by tree at its fresh head: ten
commits stand between the two heads, two files were added,
the lowering and code generation sources, and one file
changed, the slices record, with no file removed. The relay
was read by tree at its fresh head: one commit stands
between the two heads, one file was added, a dated relay
note, and no file changed or removed. No proof-assistant
source was found in either tree and neither tree read was
truncated, so both remain proof-free by the named check.
Their movement changes their pins only, not their
placements.

## 21. Watch update — 2026-11-18, the sixteenth hourly re-synthesis

The sixteenth watch re-enumerated the estate completely: 566
repos, every head read individually, no read errors. Two
repos had moved since the last recorded heads, none were
new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the two
is a proof repo — this repo itself — and the other is an
idol-family repo; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the fifteenth watch
landing itself: the five commits between the two heads
are that watch's census, annex, placement, ledger, and
pins commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
sixteen commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a code generation source. No proof-assistant
source was found in its tree and the tree read was not
truncated, so it remains proof-free by the named check.
Its movement changes its pin only, not its placement.

## 22. Watch update — 2026-11-18, the seventeenth hourly re-synthesis

The seventeenth watch re-enumerated the estate completely:
566 repos, every head read individually, no read errors.
Three repos had moved since the last recorded heads, none
were new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the three
is a proof repo — this repo itself — and the other two are
idol-family repos; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the sixteenth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
eight commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a code generation source. The relay was read by tree
at its fresh head: one commit stands between the two
heads, one file was added, a dated relay note, and no
file changed or removed. No proof-assistant source was
found in either tree and neither tree read was truncated,
so both remain proof-free by the named check. Their
movement changes their pins only, not their placements.

## 23. Watch update — 2026-11-18, the eighteenth hourly re-synthesis

The eighteenth watch re-enumerated the estate completely:
566 repos, every head read individually, no read errors.
Two repos had moved since the last recorded heads, none
were new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the two
is a proof repo — this repo itself — and the other is an
idol-family repo; there was no long-tail movement this
watch. The annex watch delta carries the tree evidence
at the fresh head; the placements in section 3 stand at
their census pins, with re-census owed at the new head.

This repo's own head moved only by the seventeenth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
eight commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a code generation source. No proof-assistant source
was found in its tree and its tree read was not
truncated, so it remains proof-free by the named check.
Its movement changes its pin only, not its placement.

## 24. Watch update — 2026-11-19, the nineteenth hourly re-synthesis

The nineteenth watch re-enumerated the estate completely:
566 repos, every head read, none new, none gone, and the
paper source hash was unchanged, so no paper re-sync was
owed. Three repos had moved since the last recorded heads.
One of the three is a proof repo — this repo itself — and
the other two are idol-family repos; there was no long-tail
movement this watch. The annex watch delta carries the tree
evidence at the fresh head; the placements in section 3
stand at their census pins, with re-census owed at the new
head.

This repo's own head moved only by the eighteenth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The compiler port was read by tree at its fresh head:
six commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a code generation source. The relay was read by tree
at its fresh head: one commit stands between the two
heads, and its tree gained one file, a dated relay note,
with no file changed or removed. No proof-assistant source
was found in either tree and neither tree read was
truncated, so both remain proof-free by the named check.
Their movement changes their pins only, not their
placements.

## 25. Watch update — 2026-11-19, the twentieth hourly re-synthesis

The twentieth watch re-enumerated the estate completely:
567 repos, every head read individually, no read errors.
Two repos had moved since the last recorded heads, one
was new, none were gone, and the paper source hash was
unchanged, so no paper re-sync was owed. One of the moved
repos is a proof repo — this repo itself — the new repo
is a proof repo, and the other moved repo is an
idol-family repo; there was no long-tail movement this
watch. The annex files carry the evidence at the fresh
heads; the placements in section 3 stand at their census
pins, with re-census owed at the new head of this repo,
and the new repo's placement stands in section 3.12 at
its census pin, which is its head.

This repo's own head moved only by the nineteenth watch
landing itself: the four commits between the two heads
are that watch's annex, placement, ledger, and pins
commits, and no Lean file changed among them, so its
eleven theorems stand unchanged at the fresh head.

The new repo, the losses proof repo, was read in full at
its head and censused at theorem level in its annex:
seventeen declarations, three controls, a recorded gate
log passing at the head, two named premises, and its
proposed items at the states its own spec states. It is
proof-bearing by content, found on its first enumeration.

The compiler port was read by tree at its fresh head:
six commits stand between the two heads, no file was
added or removed, and two files changed, a slices record
and a code generation source. No proof-assistant source
was found in its tree and its tree read was not
truncated, so it remains proof-free by the named check.
Its movement changes its pin only, not its placement.
## 26. Watch update — 2026-11-19, the twenty-first hourly re-synthesis

The twenty-first watch re-enumerated the estate
completely: 569 repos, every head read individually, no
read errors. Four repos had moved since the last
recorded heads, two were new, none were gone, and the
paper source hash was unchanged, so no paper re-sync
was owed. Two of the moved repos are proof repos — this
repo itself and the losses repo — one of the new repos
is a proof repo, and the other two moved repos are
idol-family repos; there was no long-tail movement this
watch. The annex files carry the evidence at the fresh
heads; the placements in section 3 stand at their
census pins, with re-census owed at the new head of
this repo, the losses placement restated at its new
census pin in this pass, and the new repo's placement
standing in section 3.13 at its census pin, which is
its head.

This repo's own head moved only by the twentieth watch
landing itself: the five commits between the two heads
are that watch's census, annex, placement, ledger, and
pins commits, and no Lean file changed among them, so
its eleven theorems stand unchanged at the fresh head.

The losses repo moved by one commit past its census
pin: a single theorem was added, the tightness of the
compounding bound — at the no-surplus point the gap of
a composition is exactly the sum of the component and
interaction gaps — and the repo's own counts were
restated to match. The watch re-read both Lean files
and the recorded log in full at both heads: eighteen
declarations at the fresh head against seventeen at the
census pin, one gained and none lost, the controls file
byte-identical, and the recorded log at the fresh head
ending in its axiom subset check passing. Its census
pin moves to the fresh head on this re-census, recorded
in its annex.

The new proof repo, the persistence repo, was read in
full at its head and censused at theorem level in its
annex: fifty-three declarations, four controls beside
a general no-derivation result, a recorded gate log
passing at the head, two campaign premises, and its
proposed items at the states its own spec states. It
is proof-bearing by content, found on its first
enumeration.

The second new repo, the bidirectional repo, stands
empty at its first enumeration: no commits, no tree,
accounted as carrying no provable results and colored
unknown, with the standing note that an empty repo for
a named project is a defect. Its listing description
announces a proved model and an empirical campaign for
the bidirectional claim; at this head there is no
in-repo content to census, and it enters the proof
family on the enumeration that first sees its content.

The compiler port was read by tree at its fresh head:
four commits stand between the two heads, no file was
added or removed, and two files changed, a slices
record and a code generation source. The relay was
read by tree at its fresh head: two commits stand
between the two heads, two files were added, a dated
minimax note and a dated grok audit note, and no file
changed or removed. No proof-assistant source was
found in either tree and neither tree read was
truncated, so both remain proof-free by the named
check. Their movement changes their pins only, not
their placements.
## 27. Watch update — 2026-11-19, the twenty-second hourly re-synthesis

The twenty-second watch re-enumerated the estate
completely: 569 repos, every head read individually, no
read errors. Seven repos had moved since the last
recorded heads, none were new, none were gone, and the
paper source hash was unchanged, so no paper re-sync
was owed. Three of the moved repos are proof repos —
this repo itself, the theses repo, and the frontier
repo — one moved repo is a repo that stood empty at the
last enumeration and now carries proof content for the
first time, and the other three moved repos are
idol-family repos; there was no long-tail movement this
watch. The annex files carry the evidence at the fresh
heads; the placements in section 3 stand at their
census pins, with re-census owed at the new heads of
the theses and frontier repos, and the newly
proof-bearing repo's placement standing in section 3.14
at its census pin, which is its head.

This repo's own head moved only by the twenty-first
watch landing itself: the six commits between the two
heads are that watch's census, re-census, delta,
placement, ledger, and pins commits, and both Lean
files are byte-identical between the heads, so its
eleven theorems stand unchanged at the fresh head.

The theses repo moved by four commits, the landing of
the synthesis pass of 2026-11-19 in its own tree: two
new native modules (composition glue and a rewrite
composer, fourteen theorems between them, none lost),
a third cited group growing the cited tranche from
seventeen theses to thirty-four at the pins the pass
read back, a campaign document carrying the composed
synthesis, and a future work section holding the
composed claims that landed neither way at proposed
state. Its census stands in its annex delta; no
recorded check log stands in its tree yet.

The frontier repo moved by one commit, the bounded
search layer: one new library module of thirty-eight
theorems (none lost) proving the general search layer
of the structural bounded technique — join laws,
least saturation, compounding and tightening bounds,
the exact nondominated qualified frontier, premise-
tracked speculation, and order-independent weighting —
with three new controls, specified in a new search
document. Its recorded check log stands at the fresh
head. Its census stands in its annex delta.

The bidirectional repo, which stood empty at the last
enumeration with its thesis announced and no in-repo
content, landed its full content in three commits: the
proved model, the composition, and the specification
with its first census tranche. It is proof-bearing by
content and was censused at theorem level in full at
its head in this pass: seventy-three theorems, four
controls, a recorded gate log passing at the head, six
named premises under its joined theorem, and its
proposed items and ten-entry gap register at its own
stated states. Its placement stands in section 3.14.

The library repo moved by one commit, the ninth day's
first slot: a flatbuffer reader and verifier port slice
of seventeen added files and its ledger entry. The
relay moved by one commit, a dated follow-up note on
the library's third slot. The sites repo moved by two
commits, cataloguing the redundancy campaign surfaces:
thirty-seven files added, five changed, and the paper
page file byte-identical between the heads. All three
were read by tree at their fresh heads; no
proof-assistant source was found in any of them and no
tree read was truncated, so all three remain proof-free
by the named check. Their movement changes their pins
only, not their placements.
## 28. Watch update — 2026-11-19, the twenty-third hourly re-synthesis

The twenty-third watch re-enumerated the estate
completely: 569 repos, every head read individually, no
read errors. Five repos had moved since the last
recorded heads, none were new, none were gone, and the
paper source hash was unchanged, so no paper re-sync
was owed. One of the moved repos is a proof repo — this
repo itself — and one moved repo, the library repo of
the Idol family, carries proof content for the first
time; the other three moved repos are idol-family
repos. The annex files carry the evidence at the fresh
heads; the placements in section 3 stand at their
census pins, with the newly proof-bearing repo's
placement standing in section 3.15 at its census pin,
which is its head.

This repo's own head moved only by the twenty-second
watch landing itself: the five commits between the two
heads are that watch's census, annex, placement,
ledger, and pins commits, and both Lean files are
byte-identical between the heads, so its eleven
theorems stand unchanged at the fresh head.

The library repo moved by ten commits, the Redundant
campaign landing in its tree: behavioral hypergraphs
for the libraries in joined and universal forms,
per-symbol contract extraction with two-way search, the
campaign with its checked proof kernel, and the
measured reconstruction atlas with certified witnesses —
159 files added and one changed, its readme. Its tree
at the last recorded head carried no proof-assistant
source, re-verified by tree read in this pass; at the
fresh head it carries three Lean files under the
campaign folder — a 25-theorem kernel with a recorded,
hash-bound kernel-checked receipt and five recorded
negative controls, a 13-theorem atlas development, and
a generated witness file with six examples checked by
decision. It is proof-bearing by content and was
censused at theorem level in full at its head in this
pass; its placement stands in section 3.15.

The compiler port moved by four commits, two slice
landings and their merges: its tree stands at the same
file count as at its last recorded head, with no file
added or removed and two files changed, a slices record
and a code generation source. The relay moved by one
commit, a dated minimax note. The sites repo moved by
one commit, cataloguing a new Muse Dash space:
twenty-one files added and four changed, and the paper
page file byte-identical between the heads. All three
were read by tree at their fresh heads; no
proof-assistant source was found in any of them and no
tree read was truncated, so all three remain proof-free
by the named check. Their movement changes their pins
only, not their placements.

## 29. Watch update — 2026-11-19, the twenty-fourth hourly re-synthesis

The twenty-fourth watch re-enumerated the estate
completely: 569 repos, every head read individually, no
read errors. Three repos had moved since the last
recorded heads, none were new, none were gone, and the
paper source hash was unchanged, so no paper re-sync
was owed. Two of the moved repos are proof repos — this
repo itself and the library repo — and the third is an
idol-family repo. The annex files carry the evidence at
the fresh heads; the placements in section 3 stand at
their census pins, with the library placement restated
at its new census pin in section 3.15 in this pass.

This repo's own head moved only by the twenty-third
watch landing itself: the five commits between the two
heads are that watch's census, annex, placement,
ledger, and pins commits, and both Lean files are
byte-identical between the heads, so its eleven
theorems stand unchanged at the fresh head.

The library repo moved by three commits, the Pareto
release condition landing in its campaign: a new proof
package requiring proved Pareto unimprovability for a
qualified optimal release, with its specification
section, its release record, and its views — twenty-eight
files added and seventeen changed, none removed. Its
three earlier Lean files are byte-identical at the
fresh head, so its 38 theorems and six checked witness
examples stand unchanged, and the one added Lean file
carries 27 new theorems: the strict domination
relation, the global witness with its finite, cone,
normalization, and cell-cover forms, the weighted score
results, the standing counterexamples (a zero-weight
scalar minimum that is not Pareto optimal, an omitted
alternative, and component optima that need not
compose), bounded uncertainty, and the retention model
proved optimal with its concrete instance. Its recorded
receipt at the fresh head is kernel-checked and
hash-bound — 14 theorems on no axioms, 2 on
propositional extensionality only, 10 on propositional
extensionality and quotient soundness, and 1 on the full
standard set — and this watch verified its source and
checker hashes against the tree firsthand. Five
recorded negative controls for the new package stand
rejected. It was re-censused at theorem level in full
at its fresh head in this pass, and its census pin
moves to the fresh head, recorded in its annex.

The compiler port moved by two commits, one slice
landing and its merge: its tree stands at the same file
count as at its last recorded head, with no file added
or removed and two files changed, a slices record and a
code generation source. It was read by tree at its
fresh head; no proof-assistant source was found in it
and its tree read was not truncated, so it remains
proof-free by the named check. Its movement changes its
pin only, not its placement.

## 30. Watch update — 2026-11-19, the twenty-fifth hourly re-synthesis

The twenty-fifth watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the twenty-fourth watch landing itself: the five commits between the two heads are that watch's re-census, delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by two commits, one slice landing and its merge: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.
