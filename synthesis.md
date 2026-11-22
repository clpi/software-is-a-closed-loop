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

Restated by the forty-fifth watch (2026-11-20) at the
new census pin 578b8b3a: the repo landed a second new
proof package in six commits — the space development,
55 theorems in ten Lean files over the behavioral
hypergraphs of its fourteen witnessed libraries, every
earlier Lean file byte-identical at the new head. The
two generated data levels are reconciled in the
kernel: the filter chain nests at both levels, nothing
at the current level is measured or qualified, the 155
definitions qualified at the earlier level stand
retracted at the current one by the level change
itself, and 318 of 321 earlier keys are kept with 106
new. A battery determines exactly the readings that
factor through it, with the helper and unseen input
forms refuted; merging by name and by identical body
is refuted, merging by whole closure is sound under
the named locality premise; per-library graphs are
refuted as capturing host dependencies while the
joined graph's host cone spans; constructed dominance
transfers only in the proved direction, with the wrong
direction refuted and one named rewrite's measured
loss proved over its own record; and the realized
batteries pass on their receipts while qualifying
nothing. Its check script regenerates the data and
fails on drift and prints axioms for 44 of the 55, but
no recorded run stands in the tree, so its gate at the
pin is unrecorded — one step below the earlier
packages' hash-bound strength. The repo now carries
120 theorems beside the six checked witness examples.
State: PROVEN in source at the new pin on the
re-census's full reading; the locality premise
CARRIED; per-symbol profiles UNMEASURED. The
re-census stands in its annex file.

### 3.16 Placement from the thirty-fourth watch (2026-11-19) — a new proof repo

Stage 3, 5, and 7 — software-redundant-compute-expands,
census pin 1ea28648. A new repo, entered on the
thirty-fifth enumeration and censused at theorem level
on its first sighting, by content: the proved model of
redundant compute under expansion-only growth of a
behavioral hypergraph, directed by Chris on 2026-11-19
as the growth half of the universal behavioral
hypergraph campaign. Thirty-seven theorem declarations
in four Lean files on Lean 4.19.0: the redundancy
measure of a list and of a graph (the exact append
split, monotonicity in the seen list, superadditivity,
the strict unit gained wherever the parts share an
element, appearance of redundancy at a join of
irredundant parts, and positivity exactly when an
explicit duplicate witness exists); derivability under
expansion (the persistence criterion mirrored at its
pin and proved again here — monotone in the store and
in the recorded edges — with the graph measure monotone
under expansion, witnessed redundancy persistent,
expansion transitive, and the measure non-decreasing
along every chain); compounding into joined structures
(the joined measure at least the sum of the parts, and
one unit more wherever the parts share a node or an
incidence value); and the touch kernel of witness
reconstruction (the touched count monotone in the
sample and under expansion of the graph, the inside
count never above the touched count), assembled in one
joined theorem whose only unproved antecedent is the
named empirical yield premise. Six standing controls
stand in the tree: the zero graph, the refuted
universal form, removal destroying redundancy, the
absent strict gain without overlap, touching not
containing, and the empty sample. The recorded gate
log at the pin ends in its axiom subset check passing,
with all 37 declarations printed: 2 axiom-free, 4 on
propositional extensionality only, and 31 on the
standard pair. Carried at the repo's own states: three
named premises (the empirical yield rate, the listing
reading of growth, and mirror fidelity), the universal
form refuted in the tree and carried as no claim, a
compounding rate beyond the proved bound as not
claimed, and premise-closed reconstruction as
proposed. State: PROVEN at the pin on the recorded
log, for the core above. The full census stands in its
annex file.

### 3.17 Placement from the thirty-fifth watch (2026-11-19) — a new proof repo

Stage 3 — software-certification-is-monotone, census
pin 4539760e. A new repo, entered on the thirty-sixth
enumeration and censused at theorem level on its first
sighting, by content: the monotonic certification
pipeline, a general construction that certifies a
qualified subject as monotone over a fixed set of
semantic dimensions by a single checkable artifact
between two named states, from incremental evidence
that provably covers the full check. Nineteen theorem
declarations in two Lean files on Lean 4.19.0: chain
evidence between two states proves the endpoint
comparison (the incremental covers full property at
transition grain, axiom-free), and chains over
consecutive increments compose to chain evidence over
their join (the property at chain grain, axiom-free);
the artifact's checker requires chain evidence behind
every certified verdict and recomputes the endpoint
values, so an accepted certificate's certified
dimension is monotone between its states, a regressed
dimension can carry no verdict but regressed and never
reads certified, two accepted certificates over
consecutive increments certify the outer endpoints,
and a certificate under the overall certified reading
is sound on every dimension. One standing control
stands in the tree, assembled from ten declarations:
the endpoint-only checker accepts a three state
transition whose interior regresses, no chain evidence
for it exists, and the pipeline's checker rejects the
matching claim — endpoint-only comparison refuted as a
certification method. The tree also carries the
pipeline's first issuance, for the perception harness
repo between its baseline pin and its previous head:
an artifact whose recomputed reading is not certified,
consistent by its own checker, with three dimensions
improving under stated discharges, one flat, and three
unmeasured with their gaps named — executed evidence
at its own strength, counted nowhere as proof. Carried
at the repo's own states: four named premises about
the world (the measure as a function of state, the
increment relation as the recorded history, a step's
record as an executed check, and orientation), each
with its falsification route. Axiom states stand as
the repo's specification and readme record them from
the audit file's prints — the chain results
axiom-free, the checker results and the control on
propositional extensionality and quotient soundness
only — and the gate verdict at the pin rests on the
specification's recorded cold pass statement, no build
log file standing in the tree. State: PROVEN at the
pin on the repo's recorded evidence, for the core
above. The full census stands in its annex file.

### 3.18 Placement from the thirty-fifth watch (2026-11-19) — a new proof repo, at skeleton strength

Stage 3 and 5 — software-redundancy-is-equivalence,
census pin 14992281. A new repo, entered on the
thirty-sixth enumeration and censused at theorem level
on its first sighting, by content: the redundant
compute program re-founded on the canonical model —
the one hypergraph of equivalent terms at symbolic
resolution, resolved information appended only, and
redundancy as a property of equivalence classes, the
excess of a graph being its collected terms minus its
edges. At this pin the repo carries the model as a
specification at settled intent, its eight claims
(monotonicity under expansion, compounding as
accumulation of effective joins, appearance at a cross
join, coloring, bounds, reconciliation, scope, and
the registry clauses) and its five standing controls
as proposed semantics, two inherited premise labels
(witness honesty and reading fidelity), and a proof
tree holding a bare skeleton only: one Lean
declaration, a seed fact of the logic itself — two
propositions joined by a two way implication are
equal, on propositional extensionality only — standing
so the family gate has a compiled development to
check, and no definition of the model and no theorem
of the program implemented yet, at the repo's own
stated strength. The recorded gate log at the pin
prints the seed fact and ends in its axiom subset
check passing. The repo's readme dispositions its
predecessor, the expands repo at 1ea28648, as founded
on a list counting construction whose theorems are not
a foundation here; that predecessor's census and
ledger rows stand at their pins as the record of what
it proved about its construction, and the disposition
is carried here as the repo's own recorded ruling,
relayed until a firsthand check of the program record
replaces it. State: the seed fact PROVEN at the pin on
the recorded log; the model and its claims PROPOSED,
none proven. The full census stands in its annex
file.

Restated by the thirty-seventh watch (2026-11-19) at
the new census pin 37514fb7: the rebuild landed in
five commits — the canonical model implemented in
Lean (the core, growth operations, registry, and
derived views files), all eight claims of the
specification proved in the claims file under the
names the specification assigns (monotonicity under
expansion, compounding as accumulation of effective
joins, appearance with its control direction, coloring
with the two-filter rule, bounds with the reading and
the record kept apart, reconciliation in either order,
scope widening as growth only, and the registry
clauses), the five standing controls proved over
concrete data, and the two inherited premise labels
stated as explicit premise definitions that no theorem
depends on — 217 declarations in eight Lean files,
with a recorded gate log at the pin printing
thirty-eight axiom audits, all within the standard
three, its subset check passing. The specification,
definitions record, and readme are byte-identical at
both pins, so the claims proved are the claims the
first placement carried as proposed. Beside the proof:
a resolution algorithm specification and its case
register, carried as proposed at their own stated
states, and a built registry carried as measured —
fifteen entries over 321 witnessed terms, its second
epoch solved by exhaustive search over the searched
set alone. One name loss is flagged in the annex: the
seed fact is not restated in the rewritten core file,
a skeleton placeholder replaced by the model's own
development, the proven set growing from one
declaration to 217. State: PROVEN at the new pin on
the recorded log, for the claims above; the algorithm
specification and register PROPOSED; the built
registry MEASURED at its named pins. The re-census
stands in its annex file.

### 3.19 Placement from the forty-fifth watch (2026-11-20) — a new proof repo

Stages 3, 5, and 8 — software-is-reversible, census
pin and head 984f1faf, public, Lean 4.19.0. A new
repo, entered in the proof family on the forty-sixth
enumeration and censused at theorem level on its first
sighting, by content: 55 theorem declarations in three
Lean files. The root development (38) proves the
reversibility theory of the search and action system:
the frontier before weights counterexample — the
middle plan of the three plan example is undominated,
stands on the frontier, and is selected by no positive
weighting, at two scales (stage 5: a frontier reading
is never replaceable by a weighted score); the
break-even rule in full cost form (stage 7); the
closure worklist's missing count laws and the least
closure beneath them (stages 4 and 8); the one-append
frontier update in place and compensation in place
(stage 8); the reversible action structure — an action
with a checked inverse restores, compositions restore,
and the empty option claims nothing (stage 8); stop
soundness in its two faces, the acceptable face proved
and the threshold form refuted as an optimality claim,
with the certificate form proved against the whole
remaining set (stages 5 and 9); the powerset count law
beneath the subset oracle (stage 3); and tensor edits
as overlays that protect untouched fields and
round-trip (stage 8). The scoped development (17)
proves the finite inverse theory: an inverse exists
over a finite domain exactly under injectivity,
collisions are impossible under one, inverses compose,
the residual form reconstructs where a plain inverse
cannot, and fiber sizes bound what reconstruction must
retain — with a recorded axiom audit in its tree
printing 12 of the 17 (4 axiom-free, 4 on propositional
extensionality only, 4 on the standard pair). The root
development's axioms file prints all 38 in source; its
gate pass is recorded as a claim in the repo's own
census, with no log file in the tree. Carried at the
repo's own states: its premise register (the canonical
premise, extraction and execution fidelity, witness
honesty, axis meaning, threshold choice, progress,
counted cost), with reversibility at the execution
layer UNMEASURED until its validation system
demonstrates the round trip per action; and two named
unproved lemmas — the general symmetric form of the
never-selected result, and the worklist equality
against the canonical home's view semantics — standing
as named work at their owners, beside the resolution
algorithm's carried gaps. State: PROVEN in source at
the pin for the 55 declarations, the scoped half on its
recorded audit; the named lemmas and gaps at their
stated states. The full census stands in its annex
file.

Restated by the forty-sixth watch at pin fcb95953: the root development stands at forty-two declarations — the general symmetric form named above, carried there as an unproved lemma, stands proved in three parts (the segment form, the frontier form, and the canonical form), and the overlay collapse lemma joins the tensor edit results — with its axioms file printing all forty-two and the repo's own census recording a cold gate pass at that count, carried at the same strength as before. Four example developments join the tree beside the unchanged scoped development: an action consensus development (nine theorems, recorded log: five axiom-free, four on propositional extensionality only), a product frontier development (five, recorded log: three axiom-free, two on propositional extensionality only), a suffix page development (ten, recorded log printing seven on subsets of the standard pair, the remaining three unprinted), and a compositional pruning development (eleven, print lines in source for seven, gate unrecorded). The worklist equality lemma and the execution layer cell stand at their stated states. State: PROVEN in source at the new pin for the ninety-four declarations, at the per-development strengths its annex re-census records.

### 3.20 Placement from the forty-seventh watch (2026-11-20) — a new proof repo

software-is-a-parametric-language-model (public, Lean
4.19.0) — census pin ca4ca2b3, its head at entry. A
language model whose behavior is a totally
deterministic function of its content and its
parameters, the parameters being named, legible axes
rather than an obscure weight vector, and behavior
tailored by rewriting parameters incrementally instead
of retraining or sampling. Its Lean core carries 40
theorems in one file: the fraction arithmetic the
scores run on; the selection machinery, whose champion
specification has at most one satisfier; the decoder,
whose answer is the unique satisfier of its
specification — determinism as a theorem; certification
soundness under its named coverage premise, with the
blocking direction proved outright; the overlay round
trip restoring every weight and path score exactly,
with cone invariance off the edited keys; route one
locality for single axis reweighting; and two standing
controls, greedy uncertified on its control table and
an unresolved bound blocking certification. Of the 40,
9 depend on no axioms and the rest on subsets of the
standard three, as its recorded gate log prints them;
the gate stands green at the pin on that log. Carried
at the repo's own states: the coverage premise, named
with its falsification route; the six pipeline premises
carried over; the fixture scale measurements, executed
results counted nowhere in the proven column; and the
unmeasured cells — the real checkpoint cells under a
named access blocker, code generation beyond fixture
scale, live serving, and the demo surface's conformance
— standing as named work, with the compression horizon
proposed and the registry append of its extract owed.
State: PROVEN in source at the pin for the 40 theorems,
at the strengths its annex census records. The full
census stands in its annex file.
### 3.21 Placement from the fifty-third watch (2026-11-20) — a new proof repo

software-tensors-are-editable (public, Lean 4.19.0) —
census pin 9d7afd54, its head at entry. The semantics
and proof home of the editable tensors program: a
deterministic view of a model checkpoint is edited, the
edit lands on the actual tensor bytes of an editable
copy, the next view is constructed from the edited
state, and that view drives the next edit. Its Lean
core carries 14 theorems in one file: the delta
algebra of the overlay form; reversal exactness — a
delta applied and then its recorded inverse applied
restores the original state at every coordinate;
admissibility, protecting every protected coordinate
and composing under exactly one side condition, cross
agreement at tied coordinates, with the unconditional
form refuted by a standing control, as is the
state-dependent change condition; and the view, whose
obscurity depends on the universe and the evidence
alone and which two states agreeing on the evidenced
coordinates share. Of the 14, one depends on no
axioms, seven on propositional extensionality only,
one on quotient soundness only, and five on that pair,
as its recorded gate log prints them; the gate stands
green at the pin on that log. Carried at the repo's
own states: the specification's further sections —
policies and typed view edits, the recurrence step,
and the receipt contract — proposed with their proof
obligations named; the scale transport, the per-schema
check, and the tie evidence method owed or blocked as
its census names them; and every behavioral effect of
every concrete delta unknown, with two fixture-bound
behavioral cells blocked on fixtures not on the
machine. State: PROVEN in source at the pin for the
14 theorems, at the strengths its annex census
records. The full census stands in its annex file.

### 3.22 Placement from the sixty-first watch (2026-11-20) — a repo newly proof-bearing

deterministic-llms (public, Lean 4.19.0) — census
pin 6151727a, its head at entry. The proof home of
the parametric deterministic language model in its
decoding form: generation as a deterministic
function of the content and a few named weights,
decided by a certified best-first rule over exact
integer scores and rewritable incrementally. Its
Lean package carries 54 theorems in four files: the
core (31) — the pick laws and the uniqueness of the
unbeaten candidate, determinism under any candidate
order for picks and for whole generations,
certification sound and complete, rescoring and
reweighting equal to recompute per step and per
generation, the margin cone, axis locality, cache
invisibility, and the prefix law; the skipping file
(2) — drafted acceptance is exactly the rule's own
generation, and batched acceptance equals per-step
acceptance under an explicit premise, the equality
of the two scorings, which the repo measures
bitwise on its recorded run; the sparse file (2)
— the exact sparse rule, the best moved candidate
together with the best unmoved one, needing no
margin; and the search file (19) — the archive
holding exactly the Pareto front in any arrival
order, per-factor minima plans, and Chebyshev
weights reaching every front point, with two proved
standing controls (an unsupported point the aimed
weights reach and no positive weighted sum picks).
The search file is, by the repo's own statement,
copied unchanged from the redundant compute repo's
seventh pull request: a second home for the same
content, with its first home in the redundant
compute family. Of the gate: the recorded log in
the tree shows the cold build completing and axiom
lines for seventeen named theorems, every one
inside the standard three, ending in the check
passing; the gate script fails closed on any
axiom-check error after its recorded correction.
Carried at the repo's own states: its empirical
ledger stands at executed strength with its own
verified, corrected, refuted, and unmeasured
verdicts — cross-history sharing refuted on its
data, unverified skipping refuted as exact, the
decompiling hypothesis refuted for embedding
directions at the declared weight on held-out
words and unmeasured beyond the token embedding;
and any other model, human quality judgment, long
outputs, cross-machine determinism, and native or
Idol implementations unmeasured. State: PROVEN in
source at the pin for the 54 theorems, at the
strengths its annex census records. The full
census stands in its annex file.

### 3.23 Placement from the sixty-fourth watch (2026-11-20) — a new proof repo

software-has-a-highest-minimal-axis (public, Lean
4.19.0) — census pin 63d9d3fd, its head at entry.
The proof home of the highest minimal axis theorem
for qualified parametric systems: a smallest axis
set whose variation inside the contract already
produces the full emergent live interacting
structure, chosen among the smallest by the maximal
refinement vector, the emergence measure first and
the live count second. Its Lean package carries 58
theorems in two files beside an audit file: the
core (42) — the finite list machinery; monotonicity
of the live set, the emergence measure, and the
live count under subsets; structure forcing, a
sufficient set engaging exactly the full set's
hyperedges with the positive weights load bearing;
existence of a highest minimal set for every
instance; strict fall of the measure on every
proper subset of a highest minimal set; maximality
over every minimal sufficient set with uniqueness
of the refinement vector; functoriality of the
induced transformation with exact preservation of
the engaged structure; the degenerate
characterization with its empty and singleton
contract corollary; and the corrected dead axis
facts — and the controls (16), the standing checks
on the specification's three named instances,
proved by kernel decision. Refuted in the tree by
standing control: the stronger dead axis sentence
(a dead axis can belong to a minimal sufficient
set, and the proved form is that its removal is
already sufficient) and the reading that every
minimal sufficient set is highest. Of the gate:
the recorded log in the tree prints axiom lines
for all 58 theorems, every one inside the standard
three, and its subset check passes; the gate
script is the widened family form, failing closed
on any principle outside the allowed set. Carried
at the repo's own states: the solver its
specification contracts for stands proposed, with
no implementation in this tree. State: PROVEN in
source at the pin for the 58 theorems, at the
strengths its annex census records. The full
census stands in its annex file.

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

## 31. Watch update — 2026-11-19, the twenty-sixth hourly re-synthesis

The twenty-sixth watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the twenty-fifth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 32. Watch update — 2026-11-19, the twenty-seventh hourly re-synthesis

The twenty-seventh watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. Four repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other three are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the twenty-sixth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by two commits, one slice landing and its merge: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The sites repo moved by two commits, the source updates of two spaces: its tree gained twelve files, two dated audit folders of six files each, and twenty-two files changed, and the paper page file is byte-identical between the heads. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 33. Watch update — 2026-11-19, the twenty-eighth hourly re-synthesis

The twenty-eighth watch re-enumerated the estate completely: 569 repos, every head read individually. Six first reads failed on transport stream errors; each was re-read individually and matched its last recorded head, or its recorded empty state, so the final reads carry no errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the twenty-seventh watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by two commits, one slice landing and its merge: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 34. Watch update — 2026-11-19, the twenty-ninth hourly re-synthesis

The twenty-ninth watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the twenty-eighth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by four commits, two landings and their merges: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 35. Watch update — 2026-11-19, the thirtieth hourly re-synthesis

The thirtieth watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the twenty-ninth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by two commits, one slice landing and its merge: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 36. Watch update — 2026-11-19, the thirty-first hourly re-synthesis

The thirty-first watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirtieth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 37. Watch update — 2026-11-19, the thirty-second hourly re-synthesis

The thirty-second watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-first watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by two commits, one slice landing and its merge: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 38. Watch update — 2026-11-19, the thirty-third hourly re-synthesis

The thirty-third watch re-enumerated the estate completely: 569 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-second watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 39. Watch update — 2026-11-19, the thirty-fourth hourly re-synthesis

The thirty-fourth watch re-enumerated the estate completely: 570 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself and, by its first sighting, the new repo placed in section 3.16 — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-third watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The new repo, the redundant compute repo, landed in one commit at its head, which is its census pin: four Lean files, thirty-seven theorem declarations, six standing controls, and a recorded gate log in its tree — entered in the proof family, censused at theorem level in its annex, and placed in the synthesis in section 3.16.

The compiler port moved by two commits, one slice landing and its merge: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 40. Watch update — 2026-11-19, the thirty-fifth hourly re-synthesis

The thirty-fifth watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Four repos had moved since the last recorded heads, two were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Three of the moved repos are proof repos — this repo itself, and the frontier repo — beside two new proof repos entered at their first sighting and placed in sections 3.17 and 3.18, and the other moved repos are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-fourth watch landing itself: the five commits between the two heads are that watch's census, delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The frontier repo moved by one commit, the candidate space landing: one new Lean file, the candidate module, carrying 23 declarations with none lost — the candidate record and its structural measures, the gap as a first-class object with its exact scan, the solved set under a weighting epoch proved exactly the nondominated qualified set under that epoch's measures, weighting independence given the axes, exact update forms for qualified and disqualified appends, joins, and retraction, and two proved refutation controls on a named demo space. A recorded check log stands at the fresh head, its build ending in success, printing axioms for 21 of the 23 new declarations. Its census pin stands with re-census owed at the fresh head recorded in the pins file.

The new certification repo landed in one commit at its head, which is its census pin: three Lean files beside an audit file, nineteen theorem declarations, one assembled standing control refuting endpoint-only comparison, and its first certificate artifact with a recorded consistent checker output — entered in the proof family, censused at theorem level in its annex, and placed in the synthesis in section 3.17.

The new equivalence repo landed in one commit at its head, which is its census pin: a specification of the canonical model at settled intent, eight claims and five controls as proposed semantics, and a proof skeleton of one seed declaration with a recorded gate log passing at the pin — entered in the proof family, censused at theorem level in its annex, and placed in the synthesis in section 3.18, at skeleton strength.

The perception harness repo moved by two commits, a harness semantic layer landing and its merge: its tree gained four files, the harness document, its protocol source, and its two test files, with two files changed, its makefile and its readme. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 41. Watch update — 2026-11-19, the thirty-sixth hourly re-synthesis

The thirty-sixth watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-fifth watch landing itself: the seven commits between the two heads are that watch's census, delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by four commits, two slice landings and their merges: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 42. Watch update — 2026-11-19, the thirty-seventh hourly re-synthesis

The thirty-seventh watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself, and the equivalence repo, re-censused in full at its fresh head and restated in section 3.18 — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the restated equivalence placement.

This repo's own head moved only by the thirty-sixth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The equivalence repo moved by five commits past its census pin: the theory rebuilt on the canonical model, the resolution algorithm specified with its case register seeded, and the registry built on the model with its second epoch solved. Its specification, definitions record, and readme are byte-identical at both pins, and the claims its first census carried as proposed stand proved in the tree at the fresh head — 217 declarations in eight Lean files, the five standing controls proved over concrete data, and a recorded gate log at the fresh head with thirty-eight axiom prints, all within the standard three, its subset check passing. It was re-censused at theorem level in full in its annex, and its census pin moves to the fresh head in this pass. One name loss is flagged in its annex and in the ledger, not absorbed: the seed fact of the skeleton pin, a fact of the logic that stood only so the gate had a compiled development to check, is not restated in the rewritten core file, whose audit now prints the model's own theorems.

The compiler port moved by four commits, two slice landings and their merges: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, a slices record and a code generation source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 43. Watch update — 2026-11-19, the thirty-eighth hourly re-synthesis

The thirty-eighth watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself, and the semi repo — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-seventh watch landing itself: the five commits between the two heads are that watch's re-census, delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The semi repo moved by seventeen commits past its last recorded head: dependency updates across its integration workflows and Rust manifests, a native Idol publication projection with refusal controls, a native role incidence view with replay controls, and a parity outcome folder — fifteen files added and twenty changed, none removed. It was read by tree in full at its fresh head, with no read truncated: every one of its 156 Lean files is byte-identical between its census pin, its last recorded head, and its fresh head, and no Rust source file changed, so its proven set stands unchanged at the fresh head — 1,865 declarations and 1,736 distinct names by the watch method, no name gained and none lost. Its mirror did not move and still stands at the shared census pin, so the two heads stand further apart while their proof content remains identical. A passing gate at the fresh head remains claimed, not proven, as its annex records.

The compiler port moved by fourteen commits, seven slice landings and their merges: its tree gained three files, all lowering sources, and one file changed, its slices record. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 44. Watch update — 2026-11-19, the thirty-ninth hourly re-synthesis

The thirty-ninth watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-eighth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by nine commits: its tree gained one file, a lowering source, and one file changed, its slices record, with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit: its tree gained one file, a dated minimax note, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 45. Watch update — 2026-11-19, the fortieth hourly re-synthesis

The fortieth watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Six repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Three of the moved repos are proof repos — this repo itself, the library repo, and the redundant compute repo — and the other three are the compiler port, the operating system repo, and one long-tail repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the thirty-ninth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The library repo moved by five commits, a realization route that runs five hash batteries without the compiler, with a new entry for one further hash and hardening against short and unrun transcripts: twelve files added and its ledger changed, none removed. It was read by tree in full at its fresh head, with no read truncated: every one of its four Lean files is byte-identical between its census pin and its fresh head, so its proven set stands unchanged at the fresh head — 65 declarations, the same name set, no name gained and none lost. Its census pin stands with the fresh head recorded in its annex.

The redundant compute repo moved by five commits and grew by addition only: nine new Lean files beside its original four, which are byte-identical between its census pin and its fresh head, and its recorded check log replaced. Counted by the watch method with comments stripped, its tree now carries 194 declarations in thirteen files, where its census pin carries 37; no name was lost. The canonical layer founds the program on one record log, the re-basing file restates the measure on that log, and the re-listing file discharges the listing premise its census carried — the measure is invariant under every re-listing, so expansion needs no order. The sample file proves the premise-closed reconstruction its census carried as proposed, in kernel form; the measured protocol run remains outside the repo. Its recorded check log at the fresh head, read in full by this watch, prints axiom lines for 189 of the 194 declarations, all within the standard set, and ends in its axiom subset check passing; five counted declarations carry no printed line, so their axiom state is unrecorded from the log. A full theorem-level re-census at the fresh head is owed, and its census pin stands.

The compiler port moved by three commits, one slice landing and its merge beside a record correction: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, its slices record and one emission source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The operating system repo moved by one commit, recording its boot image as built at the compiler pin: two files changed, its readme and its signing spec, with no file added or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The one long-tail repo, the personal site repo, moved by one commit staging a minimal two-view personal journal: four files added, its front page, its routes, its journal styling, and a front test, and one file changed, its index page. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 46. Watch update — 2026-11-19, the forty-first hourly re-synthesis

The forty-first watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fortieth watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 47. Watch update — 2026-11-19, the forty-second hourly re-synthesis

The forty-second watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the forty-first watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by nineteen commits: its tree gained two files, both lowering sources, and two files changed, its slices record and a code generation source, with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 48. Watch update — 2026-11-20, the forty-third hourly re-synthesis

The forty-third watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the forty-second watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by twenty-eight commits: its tree gained three files, all lowering sources, and two files changed, its slices record and a register allocation coloring source, with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 49. Watch update — 2026-11-20, the forty-fourth hourly re-synthesis

The forty-fourth watch re-enumerated the estate completely: 572 repos, every head read individually, no read errors. Eight repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Six of the moved repos are proof repos — this repo itself, the safe repo, the library repo, the redundant compute repo, the compiler repo, and the eyes repo, which is newly proof-bearing in this window — and the other two are the compiler port and the relay. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the forty-third watch landing itself: the four commits between the two heads are that watch's delta, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The safe repo moved by two commits and grew by a whole new development beside the four this synthesis places: a family development of eight modules and six worked examples — necessary dominance and the least sound cone, dataflow locality, an executable cone checker with its closure results, partition fineness as key occupation, saturation, and an exact parallel unknown result — with an audit file printing axiom lines for forty-seven of its names. Every earlier Lean file is byte-identical between the last recorded head and the fresh head, so the growth is by addition only: 277 declarations where the last recorded head carries 151, ninety-seven distinct names gained and none lost. No recorded check log stands at the fresh head, so its gate there is unrecorded, and a full theorem-level re-census at the fresh head is owed; its census pin stands with the fresh head recorded in its annex.

The library repo moved by three commits, and the movement is an oracle slice and portable evidence, not library growth: thirty-one files added, none changed or removed, and no library file among them — every Lean file the census records is byte-identical between the last recorded head and the fresh head, so its proven set stands unchanged. The mechanical count rose by eight names, and all eight stand in new oracle fixture files: six kernel fixture theorems proven at fixture strength with recorded evidence — five depending on no axioms, one on propositional extensionality only — beside two planted controls that are not proven results at all, a false statement proven by an admitted proof and a conditional result on a planted false axiom, each with its dependence recorded in the tree. The oracle script asserts each expected outcome, and its own readme states the slice is a noncompeting read-only inventory, not an implementation or a parity certificate. The two portable evidence additions each carry a recorded check log of nine tests passing. Its census pin stands with a full re-census at the fresh head owed.

The redundant compute repo moved by two commits adding exactly one Lean file, built on its own canonical layer: over a two-seed joint rule it proves reachability is not qualification — each seed necessary, the qualification form exact, neither seed alone deriving the conclusion and the two together deriving it, with the canonical log view agreeing. The other thirteen Lean files are byte-identical, so the growth is by addition only: 202 declarations where the last recorded head carries 195, seven gained and none lost. The recorded check log in the tree predates the new file, so its gate rests on the file's own print lines and this watch's reading. Its census pin stands with a full re-census at the fresh head owed.

The compiler repo moved by twenty-two commits of compiler and gate work, the wholesale directive ratchet landing among them: three files added and twenty-one changed, none of them Lean. Every one of its five Lean files is byte-identical between the last recorded head and the fresh head, read by tree in full with no read truncated, so the proof-bearing content this synthesis records — the frontier file, the two release tools files, and the solver history file — stands unchanged at the fresh head, and the proof data sample remains test data counted nowhere. The full census of the release tools and solver developments remains owed. Its movement changes its pin only, not its placement.

The eyes repo is newly proof-bearing, and it enters the proof family in this watch. At its last recorded head its tree carried no proof-assistant source at all; at its fresh head it carries four Lean files with sixty-one declarations, read in full by this watch. Its canonical file restates the derivability and hypergraph definitions mirrored from the library repo at its named pin and states the resolution-chain model for the first time in the estate — terms identified by a total equivalence at each resolution level, one append-only record log as the only source of truth — with the view laws proven over that log. Its certification file proves the campaign gate: a candidate is admitted over its predecessor exactly when every registered dimension is measured on both sides and no candidate reading falls below its predecessor, an unmeasured dimension refuses, admission is transitive and carries witnesses, and a regression refuses forever. Its union file proves meeting the union of the incumbents is exactly admission over each incumbent and exactly domination of the pooled peak list, with the ceiling form for an incumbent already at a declared maximum. Its axioms file prints axiom lines for twenty-nine of the sixty-one theorems; the canonical file's twenty-four carry no printed line, so their axiom state is unrecorded. A check script stands in its proof folder and no recorded run of it stands in the tree, so a passing gate at the fresh head is unrecorded. Its premises are named in its own headers and carried, not proved: faithful score normalization at ingest, measurement records that state what was measured under the campaign's same-contract rules, the declared maximum as the true maximum, and a failed run ingested at zero on every cost dimension. Placement: the eyes repo joins the proof family as the loop's certification law for its perception campaign — the gate its release claims must pass is now a theorem over the canonical log, at the strength just stated. Its census pin is its fresh head, recorded in its new annex.

The compiler port moved by thirty-six commits: six new lowering sources added and its slices record changed, nothing removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by two commits adding one dated fleet note. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 50. Watch update — 2026-11-20, the forty-fifth hourly re-synthesis

The forty-fifth watch re-enumerated the estate completely: 573 repos, every head read individually, no read errors. Seven repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Four of the moved repos are proof repos — this repo itself, the frontier repo, the redundant compute repo, and the library repo — beside one new proof repo entered at its first sighting and placed in section 3.19, and the other three moved repos are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the restated library placement in section 3.15 and the new placement in section 3.19.

This repo's own head moved only by the forty-fourth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The frontier repo moved by two commits and grew by addition only: two new library modules beside its twelve earlier files, byte-identical but for the build file's two added lines — the pipeline module, proving the derivation to action core (determinism, the selected action's frontier standing, incremental reevaluation equal to full, compensation restoring the solved set, and stop soundness in both faces, with three proved refutation controls and six labeled premises), with a recorded check log at the fresh head printing all 28 of its declarations; and the worklist module, proving the indexed closure is exactly the least full closure at every append prefix, with four closing controls and a recorded check log printing 13 of its 51 declarations. Counted by the watch method, the tree now carries 206 declarations where the last recorded head carries 127 — 79 gained and none lost. Its census pin stands with a full re-census at the fresh head owed.

The redundant compute repo moved by six commits and grew by addition only: three new Lean files beside its fourteen earlier files, byte-identical — a certified action selection development over its canonical layer, a closure worklist proving its drained run computes exactly the canonical closure with its resume forms, and an intelligence join development proving convergence at a delivered cut and exact reconstruction from a delivered set, with two executed replay folders beside them. Counted by the watch method, the tree now carries 240 declarations where the last recorded head carries 201 by the same method — 39 gained and none lost; the one count difference against the last watch's record for that head stands noted in its annex, with file identity governing. The recorded check log in its proof folder predates all three files, so their gate rests on the files' own print lines and this watch's reading. Its census pin stands with a full re-census at the fresh head owed.

The library repo moved by six commits landing a wholly new proof package, the space development: 55 theorems in ten Lean files over the behavioral hypergraphs of its fourteen witnessed libraries — the two data levels reconciled in the kernel with the earlier level's qualified set retracted by the level change, determination exactly factorization through a battery with its two refutations, name and body merging refuted and closure merging sound under the named locality premise, the host cone spanning in the joined graph, constructed dominance transferring only in the proved direction with one named rewrite's measured loss proved over its own record, and the realized batteries passing on their receipts while qualifying nothing. Every earlier Lean file is byte-identical at the fresh head, so its 65 earlier theorems stand unchanged and its total is now 120. It was re-censused at theorem level in full in its annex, and its census pin moves to the fresh head in this pass; its gate at the fresh head is unrecorded, as its annex states.

The new repo is a proof repo, the reversible search space repo, entered and censused at theorem level at its head, which is its census pin: 55 declarations in three Lean files — the reversibility theory of the search and action system in the root development, with the frontier before weights counterexample at two scales, and the finite inverse theory in the scoped development, on a recorded axiom audit — with its premise register carried at its stated strengths, its execution layer cell UNMEASURED, and its two named unproved lemmas standing as named work. Its placement stands in section 3.19.

The compiler port moved by twenty-two commits: three files added, all lowering sources, and its slices record changed, with nothing removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The sites repo moved by two commits, a new frontier before weights space and an algorithm demo: sixty-seven files added and four changed, none removed, and the paper page file is unchanged between its two heads. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 51. Watch update — 2026-11-20, the forty-sixth hourly re-synthesis

The forty-sixth watch re-enumerated the estate completely: 573 repos, every head read individually, no read errors. Nine repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Six of the moved repos are proof repos — this repo itself, the compiler repo, the eyes repo, the library repo, the reversible repo, and the equivalence repo — and the other three are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the restated reversible placement in section 3.19.

This repo's own head moved only by the forty-fifth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler repo moved by two commits of compiler work: four files changed and none added or removed, none of them Lean, and all five of its Lean files are byte-identical between the heads, so its recorded proof-bearing content stands unchanged — the frontier file with its 7 declarations, the release tools files with their 20 and 5, and the solver history file with its 10. Its census pin stands with the full census of the release tools and solver developments still owed.

The eyes repo moved by two commits of harness evidence work: one evidence file added and its harness document changed, and all four of its Lean files are byte-identical between the heads, so its sixty-one theorems stand unchanged at the fresh head. Its census pin stands; the gate's passing run at the fresh head is unrecorded, as its annex delta records.

The library repo moved by two commits landing a protocol buffers port slice: thirteen files added, all of the one port, and two files changed, none of them Lean, and all twenty of its Lean files are byte-identical between the heads, so its one hundred twenty theorems stand unchanged at the fresh head. Its census pin stands at the head the forty-fifth watch re-censused, with its gate at that pin unrecorded.

The reversible repo moved by thirteen commits and grew by addition and completion: its root development gained four declarations — the general symmetric form of the never-selected result, a named lemma standing unproved at its census pin, now proved in three parts, and the overlay collapse lemma — for forty-two, with its axioms file printing all of them and the repo's own census recording a cold gate pass at that count; four new example developments landed beside it — an action consensus development of nine theorems on its recorded log, a product frontier development of five on its recorded log, a suffix page development of ten with a recorded log printing seven, and a compositional pruning development of eleven with its gate unrecorded — and its scoped development stands byte-identical. Counted by the watch method, the tree now carries 94 declarations where the census pin carries 55 — thirty-nine gained and none lost. It was re-censused at theorem level in full in its annex, and its census pin moves to the fresh head in this pass.

The equivalence repo moved by two commits of registry and approach space work: six files added and four changed, none of them Lean, and all nine of its Lean files are byte-identical between the heads, so its 217 declarations stand unchanged at the fresh head. Its census pin stands at the head the thirty-seventh watch re-censused, proven there on its recorded log.

The compiler port moved by two commits: its slices record and its demand source changed, with no file added or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated muse note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The sites repo moved by three commits, the frontier before weights space sources and real wasm modules for four demos: thirty-six files added and thirteen changed, none removed, and the paper page file is unchanged between its two heads. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 52. Watch update — 2026-11-20, the forty-seventh hourly re-synthesis

The forty-seventh watch re-enumerated the estate completely: 574 repos, every head read individually, no read errors. Eleven repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Seven of the moved repos are proof repos — this repo itself, the compiler repo, the library repo, the reversible repo, the review repo, the frontier repo, and the certifiable repo — beside one new proof repo entered at its first sighting and placed in section 3.20, and the other four moved repos are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the new placement in section 3.20.

This repo's own head moved only by the forty-sixth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler repo moved by four commits of compiler and gate work: one evidence file added and four files changed, none of them Lean, and all five of its Lean files are byte-identical between the heads, so its recorded proof-bearing content stands unchanged — the frontier file with its 7 declarations, the release tools files with their 20 and 5, and the solver history file with its 10. Its census pin stands with the full census of the release tools and solver developments still owed.

The library repo moved by eight commits extending the realization route to every verifier home: twelve files added and three changed, none of them Lean, and all twenty of its Lean files are byte-identical between the heads, so its one hundred twenty theorems stand unchanged at the fresh head. Its census pin stands at the head the forty-fifth watch re-censused, with its gate at that pin unrecorded.

The reversible repo moved by one commit, its own census addendum: no file but that census changed, and all seven of its Lean files are byte-identical between the heads, so its 94 declarations stand unchanged at the fresh head. The addendum records that the worklist equality lemma — the one named unproved lemma its re-census carried — stands proved in the frontier home at its fresh head in this same window, so no named unproved lemma from its census remains. Its census pin stands at the head the forty-sixth watch re-censused.

The review repo moved by two commits landing a statement package in its own isolated build beside its byte-identical legacy library: the three original propositions, unchanged as definitions, now stand inhabited — the full closure, relevant, and omission claims proved axiom-free, with the exact absorption characterization, the stronger prospective core and application forms, the redundancy characterizations, and the finite checker correctness — 23 new non-control theorems — beside 18 standing counterexample theorems, ten retained and eight new. Counted by the watch method, the tree now carries 126 declarations where the last recorded head carries 86 — 42 gained and 2 lost, the lost pair being the planted admitted proof controls, renamed out of the Lean inventory into non-Lean fixture files where they stand as explicit rejection controls, flagged in its annex delta as controls leaving the inventory, not proven results lost. A recorded publisher log at the fresh head states the gate passed there over both packages; the independent exact pin recheck its verification record requires stands owed. Its census pin stands with a full re-census owed.

The frontier repo moved by one commit landing the canonical bridge: two new files — the canonical view file, carrying the canonical definitions verbatim from their home with the resolution level chain stated and proved, 24 declarations, and the bridge file, 10 declarations, proving the worklist equality lemma the reversible home carried as named work, in its stated bridge form, with the append form at every prefix and a non-vacuity control. Counted by the watch method, the tree now carries 240 declarations where the last recorded head carries 206 — 34 gained and none lost. A recorded check log at the fresh head ends in a successful build and prints axiom lines for all 10 bridge declarations and 20 of the 24 canonical ones. Its census pin stands with a full re-census owed.

The certifiable repo moved by two commits landing a proof and falsification duet: the historical model recovered from the safe home's audited branch pin under a documented namespace transformation, its bridge to the canonical interface, the legacy sequence results — the unrestricted thesis refuted by a checked counterexample, then repaired exactly: adjacent nonregression exactly equivalent to all pairs nonregression, strict improvement exactly witnessed, and the guarded step form under a fixed requirement set — the canonical release sequence results, and 26 standing control theorems. Counted by the watch method, the tree now carries 187 declarations where the last recorded head carries 89 — 99 gained and 1 lost, the lost name being the planted admitted proof control, renamed out of the Lean inventory into a non-Lean fixture file, flagged in its annex delta as a control leaving the inventory, not a proven result lost. Its new gate contract stands in the tree with no recorded run at the fresh head, and its duet record names the five application premises and the correction that temporal nonregression replaces unqualified global optimality. Its census pin stands with a full re-census owed.

The new repo is a proof repo, the parametric language model repo, entered and censused at theorem level at its head, which is its census pin: 40 theorems in one Lean file — the fraction arithmetic, the selection machinery and the decoder's determinism, certification soundness under its named coverage premise with blocking proved outright, the overlay round trip and cone invariance, route one locality, and two standing controls — on a recorded gate log passing at the pin, its measured cells at fixture strength, and its unmeasured cells standing as named work. Its placement stands in section 3.20.

The api repo moved by four commits finishing its pure Idol rewrite on the pinned compiler: five files changed and none added or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The compiler port moved by four commits, two demand slices: its slices record and its demand source changed, with no file added or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The operating system repo moved by two commits hardening its signing judgement: one tool file added and five files changed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 53. Watch update — 2026-11-20, the forty-eighth hourly re-synthesis

The forty-eighth watch re-enumerated the estate completely: 574 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself and the compiler repo — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the forty-seventh watch landing itself: the five commits between the two heads are that watch's annex, placement, ledger, correction, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler repo moved by four commits of compiler, library, and gate work: ninety-three files changed and none added or removed, none of them Lean, and all five of its Lean files are byte-identical between the heads, so its recorded proof-bearing content stands unchanged — the frontier file with its 7 declarations, the release tools files with their 20 and 5, and the solver history file with its 10. Its census pin stands with the full census of the release tools and solver developments still owed.

The relay moved by one commit, a dated minimax note: its tree gained one file, with no file changed or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 54. Watch update — 2026-11-20, the forty-ninth hourly re-synthesis

The forty-ninth watch re-enumerated the estate completely: 574 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself and the compiler repo — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the forty-eighth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler repo moved by two commits of specification and compiler work: three files added and five changed, none of them Lean, and all five of its Lean files are byte-identical between the heads, so its recorded proof-bearing content stands unchanged — the frontier file with its 7 declarations, the release tools files with their 20 and 5, and the solver history file with its 10. Its census pin stands with the full census of the release tools and solver developments still owed.

The compiler port moved by six commits, three demand slices: its slices record and its demand source changed, with no file added or removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 55. Watch update — 2026-11-20, the fiftieth hourly re-synthesis

The fiftieth watch re-enumerated the estate completely: 574 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the forty-ninth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by ten commits, five slices of projection, walk, and scan work: its tree gained one file, a new projection lowering source, and its slices record changed, with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 56. Watch update — 2026-11-20, the fifty-first hourly re-synthesis

The fifty-first watch re-enumerated the estate completely: 574 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fiftieth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by eight commits of observer and tail work: its tree gained one file, a new observer lowering source, and three files changed — its slices record, its demand source, and its projection source — with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

The sites repo moved by two commits updating two space sources: its tree gained eighteen files, three dated audit folders, and twenty-two files changed, with no file removed, and the paper page file is byte-identical between its heads. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 57. Watch update — 2026-11-20, the fifty-second hourly re-synthesis

The fifty-second watch re-enumerated the estate completely: 574 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex files carry the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-first watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 58. Watch update — 2026-11-20, the fifty-third hourly re-synthesis

The fifty-third watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — beside one new proof repo entered at its first sighting and placed in section 3.21, and the other moved repo is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the new placement in section 3.21.

This repo's own head moved only by the fifty-second watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The new repo is a proof repo, the editable tensors repo, entered and censused at theorem level at its head, which is its census pin: 14 theorems in one Lean file — the delta algebra, reversal exactness for the overlay form, admissibility under its one cross-tie side condition with the two unconditional forms refuted as standing controls, and view determinism in its agreement form — on a recorded gate log passing at the pin, its specification's further sections proposed, and its behavioral cells blocked or unknown as named. Its placement stands in section 3.21.

The compiler port moved by eight commits, four tail slices: its tree gained two files, the tail model and tail result lowering sources, and three files changed — its slices record, its demand source, and its observer source — with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 59. Watch update — 2026-11-20, the fifty-fourth hourly re-synthesis

The fifty-fourth watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself and the editable tensors repo — and the other moved repo is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-third watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The editable tensors repo moved by one commit changing only its own census file, so its fourteen theorems stand unchanged at the fresh head on the recorded gate log at its census pin. That commit is a census correction: a checkpoint in a local model store, missed at the founding census because the store's blobs carry no file extension, is now recorded as verified firsthand on disk in the source census, with the plain statement that no blocked item depends on it. Its blocked behavioral cells therefore remain blocked on their own missing fixtures, its proposed sections stand as placed in section 3.21, and every behavioral effect remains unknown as named there.

The compiler port moved by twelve commits: its tree gained one file, a native backend source, and one file changed, its slices record, with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 60. Watch update — 2026-11-20, the fifty-fifth hourly re-synthesis

The fifty-fifth watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other moved repo is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-fourth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by two commits: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, its slices record and its native backend source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 61. Watch update — 2026-11-20, the fifty-sixth hourly re-synthesis

The fifty-sixth watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other moved repo is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-fifth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by ten commits: its tree gained one file, an x86 backend source, and two files changed, its slices record and its native backend source, with no file removed. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 62. Watch update — 2026-11-20, the fifty-seventh hourly re-synthesis

The fifty-seventh watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-sixth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 63. Watch update — 2026-11-20, the fifty-eighth hourly re-synthesis

The fifty-eighth watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-seventh watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 64. Watch update — 2026-11-20, the fifty-ninth hourly re-synthesis

The fifty-ninth watch re-enumerated the estate completely: 575 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-eighth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 65. Watch update — 2026-11-20, the sixtieth hourly re-synthesis

The sixtieth watch re-enumerated the estate completely: 576 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The new repo is a long-tail repo with no proof content, entered in the census at listing depth. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the fifty-ninth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The new repo stands at its first commit, the repository initialization, with a single ignore file in its tree. It was read by tree at its head; no proof-assistant source was found in it and its tree read was not truncated, so it is proof-free by the named check and carries no provable results. Its census state is unknown at listing depth, as its census row records.

## 66. Watch update — 2026-11-20, the sixty-first hourly re-synthesis

The sixty-first watch re-enumerated the estate completely: 576 repos, every head read individually, no read errors. Four repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Three of the moved repos are proof repos — this repo itself, the compiler repo, and the library repo — and the fourth is a repo newly proof-bearing in this window, entered and placed in section 3.22. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the new placement in section 3.22.

This repo's own head moved only by the sixtieth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler repo moved by one commit changing one file, its Wasm source, and the library repo moved by twenty-one commits landing a new native port and its evidence, seven files added and eight changed. Both were read by tree at their fresh heads; every Lean file in each is byte-identical between the last recorded head and the fresh head, so their proven sets stand unchanged — the compiler repo's forty-two counted declarations beside its test-data sample, and the library repo's one hundred twenty theorems.

The newly proof-bearing repo is the deterministic language models repo, entered and censused at theorem level at its fresh head, which is its census pin: fifty-four theorems in four Lean files — the certified best-first core, draft acceptance under its named premise, the exact sparse rule, and the reused search development with its two standing controls — on a recorded gate log passing at the pin, its empirical ledger at executed strength with its refuted and unmeasured cells standing as named. Its placement stands in section 3.22.

## 67. Watch update — 2026-11-20, the sixty-second hourly re-synthesis

The sixty-second watch re-enumerated the estate completely: 576 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-first watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The sites repo moved by one commit updating the frontier before weights space sources: its tree gained six files, one dated audit folder with its document text, probe record, report, and screenshots, and eleven files changed — its catalogue entry, its harness and build records, its probe records, its deploy and build manifests and built pages, and the space source itself — with no file removed, and the paper page file is byte-identical between its heads. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 68. Watch update — 2026-11-20, the sixty-third hourly re-synthesis

The sixty-third watch re-enumerated the estate completely: 576 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-second watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The sites repo moved by one commit updating the frontier before weights space sources: its tree gained six files, one dated audit folder with its document text, probe record, report, and screenshots, and eleven files changed — its catalogue entry, its harness and build records, its probe records, its deploy and build manifests and built pages, and the space source itself — with no file removed, and the paper page file is byte-identical between its heads. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 69. Watch update — 2026-11-20, the sixty-fourth hourly re-synthesis

The sixty-fourth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Four repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself and the deterministic language models repo — and the new repo is a proof repo, entered at theorem level in section 3.23. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins except where this watch sets a new one.

This repo's own head moved only by the sixty-third watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The deterministic language models repo moved by two commits of executed-layer growth — twelve files added, the architecture, density, and multi-model harness modules with their frozen contracts and recorded reports, and seven files changed, among them its claims ledger and specification — with every Lean file byte-identical between its census pin and its fresh head, so its fifty-four theorems stand unchanged and its census pin stands.

The new repo is the highest minimal axis proof repo, public, at 63d9d3fd: fifty-eight theorems in two Lean files — the monotonicity, structure forcing, existence, minimality, maximality, functoriality, and degenerate results of its specification, with the corrected dead axis facts — beside sixteen standing controls on its three named instances and a recorded gate log passing at the head, which is its census pin.

The compiler port moved by four commits landing a divisor slice and its re-judged frontier record: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, its slices record and its native backend source. The sites repo moved by one commit updating the frontier before weights space sources: its tree gained six files, one dated audit folder with its document text, probe record, report, and screenshots, and eleven files changed, with no file removed, and the paper page file is byte-identical between its heads. Both were read by tree at their fresh heads; no proof-assistant source was found in either and no tree read was truncated, so both remain proof-free by the named check. Their movement changes their pins only, not their placements.

## 70. Watch update — 2026-11-20, the sixty-fifth hourly re-synthesis

The sixty-fifth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-fourth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The sites repo moved by one commit updating the frontier before weights space sources: its tree gained six files, one dated audit folder with its document text, probe record, report, and screenshots, and twelve files changed, with no file removed, and the paper page file is byte-identical between its heads. It was read by tree at its fresh head; no proof-assistant source was found in it and no tree read was truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 71. Watch update — 2026-11-20, the sixty-sixth hourly re-synthesis

The sixty-sixth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-fifth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 72. Watch update — 2026-11-21, the sixty-seventh hourly re-synthesis

The sixty-seventh watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-sixth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 73. Watch update — 2026-11-21, the sixty-eighth hourly re-synthesis

The sixty-eighth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-seventh watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

## 74. Watch update — 2026-11-21, the sixty-ninth hourly re-synthesis

The sixty-ninth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo — this repo itself — and the other two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

This repo's own head moved only by the sixty-eighth watch landing itself: the four commits between the two heads are that watch's annex, placement, ledger, and pins commits, and both Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The compiler port moved by four commits landing a wide compare slice and its re-judged frontier record: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, its slices record and its native backend source. The sites repo moved by one commit updating the frontier before weights space sources: its tree gained six files, one dated audit folder with its document text, probe record, report, and screenshots, and eleven files changed, with no file removed, and the paper page file is byte-identical between its heads. Both were read by tree at their fresh heads; no proof-assistant source was found in either and no tree read was truncated, so both remain proof-free by the named check. Their movement changes their pins only, not their placements.

## 75. Watch update — 2026-11-21, the seventieth hourly re-synthesis

The seventieth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Eight repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Five of the moved repos are proof repos and three are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

Two proof repos grew at their fresh heads and none shrank. The deterministic language models repo gained five theorems in one new Lean file, the loop development — the admission, rejection, and scope soundness results and the two architecture coverage results — for fifty-nine in total, landing with its self-improving, scope-solving Pareto loop. The redundant compute repo gained ninety-five declarations in three new proof files — the worklist development proving the counter-based worklist closure equal to the least closure at every append prefix, the closure development, and the algorithm search development — for three hundred thirty-five in total, with its recorded check log grown at the fresh head. Two proof repos moved with every Lean file byte-identical, so their proven sets stand unchanged: the eyes repo, whose movement is a dated claims audit folder of scripts, raw outputs, and recorded check outputs, and the library repo, whose movement is one new data format port. This repo's own head moved by the sixty-ninth watch landing and by one further lane's re-census of the traceability repo inside this repo, landed by merge; both of its Lean files are byte-identical between the heads, so its eleven theorems stand unchanged at the fresh head.

The three idol-family repos moved without proof content: the compiler port, by four commits landing a register allocation slice and its re-judged frontier record, its tree at the same file count with two files changed; the relay, by one commit adding one dated rotation note; and the sites repo, by one commit refreshing the audit pointer files of three spaces, with the paper page file byte-identical between its heads. All three were read by tree at their fresh heads; no proof-assistant source was found in any of them and no tree read was truncated, so all three remain proof-free by the named check. Their movement changes their pins only, not their placements.

## 76. Watch update — 2026-11-21, the seventy-first hourly re-synthesis

The seventy-first watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Five repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Three of the moved repos are proof repos and two are idol-family repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

One proof repo grew at its fresh head and none shrank. The library repo gained eight theorems in one new Lean file, the level three development of its space package — the counts of the definitions qualified from Idol execution receipts at level three, their receipt facts, and the passing of the recorded runs — for one hundred twenty-eight in total, with its axioms, root, and data files extended beside it and no name lost. Two proof repos moved with every Lean file byte-identical, so their proven sets stand unchanged: the idol repo, whose movement is gate hygiene and frontier benchmark record work in one commit, and this repo itself, whose head moved only by the seventieth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The two idol-family repos moved without proof content: the compiler port, by six commits landing a new slice and its re-judged frontier record, its tree at the same file count with two files changed, its slices record and its native backend source; and the sites repo, by one commit adding two dated audit folders for the frontier before weights space — screenshots, document text, probe and report records — seventy-eight files added and twelve changed, with the paper page file byte-identical between its heads. Both were read by tree at their fresh heads; no proof-assistant source was found in either and no tree read was truncated, so both remain proof-free by the named check. Their movement changes their pins only, not their placements.

## 77. Watch update — 2026-11-21, the seventy-second hourly re-synthesis

The seventy-second watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-first watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 78. Watch update — 2026-11-21, the seventy-third hourly re-synthesis

The seventy-third watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo and one is an idol-family repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-second watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The one idol-family repo moved without proof content: the compiler port, by four commits landing a new slice and its re-judged frontier record, its tree at the same file count with two files changed, its slices record and its native backend source. It was read by tree at its fresh head; no proof-assistant source was found in it and no tree read was truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 79. Watch update — 2026-11-21, the seventy-fourth hourly re-synthesis

The seventy-fourth watch re-enumerated the estate completely: 577 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo and one is an idol-family repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-third watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The one idol-family repo moved without proof content: the compiler port, by four commits landing a new slice and its re-judged frontier record, its tree at the same file count with two files changed, its slices record and its native backend source. It was read by tree at its fresh head; no proof-assistant source was found in it and no tree read was truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.


## 80. Watch update — 2026-11-21, the seventy-fifth hourly re-synthesis

The seventy-fifth watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo and two are idol-family repos. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-fourth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The two idol-family repos moved without proof content: the compiler port, by four commits, its tree at the same file count with two files changed, its slices record and its native backend source; and the sites repo, by two commits adding two dated audit folders for the dash and frontier sweep spaces — twelve files added and twenty-four changed, with the paper page file byte-identical between its heads. Both were read by tree at their fresh heads; no proof-assistant source was found in either and no tree read was truncated, so both remain proof-free by the named check. Their movement changes their pins only, not their placements.

The new repo is the emergence program repo, public, founded this morning at 192df382: three files only — a ladder specification, a program record, and a readme — and no proof-assistant source or machine-checked artifact in its tree, so by the named check it is not proof-bearing in-repo at its founding head. What it carries is proposed: a spec whose twenty-seven theorem obligations for its upper rungs are stated as unproved in its own readme, building on proved work housed in other repos of the family. It enters the census as a new repo at listing depth with that state named; it takes a proof family placement only when proof content lands in its own tree.


## 81. Watch update — 2026-11-21, the seventy-sixth hourly re-synthesis

The seventy-sixth watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Both moved repos are proof repos — this repo itself, and one repo newly proof-bearing in this window, entered and placed in section 3.23. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, beside the new placement in section 3.23.

No proof repo shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-fifth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The newly proof-bearing repo is the emergence program repo, entered and censused at theorem level at its fresh head, which is its census pin: twenty-two theorems in one Lean file — the tally algebra, formation from the level-1 projection alone with first-reach stability under appends, restart exactness, the freeze laws, the exact group-step exchange, the joint tally as the componentwise sum of the level tallies, and the shuffle marginal laws — with the measure monotonicity obligation proved in conditional form and the no-free-capability obligation standing as a named premise, unproved and depended on by no theorem. Its rung 3 capability claim is refuted in its own record at the pin: no win in either registered family under either decision rule. Its placement stands in section 3.23.

## 3.23 The emergence program repo — rung 3 composition, proved stack, refuted claim

The emergence program repo (software-emergence-is-decidable, public) entered the census at the seventy-fifth watch as a proposed repo: a ladder specification, a program record, and a readme, with no proof content in its tree. At this watch's fresh head, ee308652, it carries its rung 3 execution: one Lean file of twenty-two theorems proving the verification stack under composition — emergent groups as actors — beside the rung record, its registration, its harness and independent checker, and its result artifacts. Seven of the rung's eight obligations are proved, one of them in conditional form with its antecedent discharged by the view construction rather than in the file; the eighth stands as a named premise for the rung 6 certificate. The rung's capability claim is falsified in the repo's own record at the pin, and that refutation is part of its placement: the synthesis carries the proved stack at proven strength, the conditional form at its stated premise, the eighth obligation as premise, and the capability claim as refuted — never higher.


## 82. Watch update — 2026-11-21, the seventy-seventh hourly re-synthesis

The seventy-seventh watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two of the moved repos are proof repos — this repo itself, and the emergence program repo, re-censused at theorem level in this pass and restated in section 3.23 below — and the other is an idol-family repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins except where this watch moves one.

No proof repo shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-sixth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The emergence program repo landed rungs 4, 5, and 6 in three commits: forty-five files added and one changed, its readme, with no file removed, and its earlier Lean file byte-identical between the heads. Three new Lean files carry forty-one new theorems, for sixty-three theorems in four files in total, and no name was lost. Its placement is restated at its fresh head, which is its new census pin.

The compiler port moved by four commits landing two slice judgments: its tree stands at the same file count as at its last recorded head, with no file added or removed and two files changed, its slices record and its native backend source. It was read by tree at its fresh head; no proof-assistant source was found in it and its tree read was not truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 3.23 restated — the emergence program repo at the seventy-seventh watch

The emergence program repo stands restated at cddf398a, its new census pin. Its rung 3 placement stands as written above. Rung 4, transfer, adds fourteen theorems: five of its six obligations proved, the transfer bound standing as a named premise, and its capability claim refuted in its own record, the measured transfer effect exactly zero in both registered pairs under both decision rules. Rung 5, compounding over time, adds ten theorems: four of its six obligations proved, one standing as a premise by construction review and one as a named premise, and its capability claim refuted in its own record, the field gain below the frozen control spread and the region gain matched by the frozen control. Rung 6, the certificate, adds seventeen theorems: four obligations proved and reweighting stability proved in scoped form only, with soundness and completeness standing as named premises; its decision procedure stands built and verified in the record, and its governing precondition fails there — the earlier records do not separate, the needed threshold does not exist, and all twenty-five instances stand not certified, in agreement with every battery outcome. The synthesis carries the proved obligations at proven strength, the scoped form at its stated scope, the premises as premises, and every falsified capability claim as refuted — never higher.

## 3.23 restated — the emergence program repo at the eighty-first watch

The emergence program repo stands restated at 8eb2906b, its new census pin. Its rungs 3 to 6 placement stands as written above: the four rung Lean files are byte-identical between the heads, so their sixty-three theorems stand unchanged. The premise audit landed in two commits and adds one Lean file of five theorems in a new audit folder, discharging the accumulation monotonicity premise for the concrete measure — the total weight of a cut's engaged edges — in conditional form, under one named hypothesis, a duplicate-free edge family, which the audit record states is constructional in the rung 5 instrument. The remaining three carried premises stay premises, each traced in the audit record to the exact missing link: the no-free-capability premise and the transfer bound hang from the certificate soundness theorem, whose threshold does not exist because the earlier records do not separate, and the no-forgetting premise, its content verified on the persisted artifacts, awaits the endgame derivation machinery for its discharge. Premise debt stands at three of the original four. The synthesis carries the discharged premise at proved strength in its stated conditional form, the three remaining premises as premises, and every falsified capability claim as refuted — never higher.


## 83. Watch update — 2026-11-21, the seventy-eighth hourly re-synthesis

The seventy-eighth watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-seventh watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 84. Watch update — 2026-11-21, the seventy-ninth hourly re-synthesis

The seventy-ninth watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo and one is an idol-family repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-eighth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The one idol-family repo moved without proof content: the compiler port, by four commits landing a second fusion group slice and a re-judged slice record, its tree at the same file count with two files changed, its slices record and its native backend source. It was read by tree at its fresh head; no proof-assistant source was found in it and no tree read was truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 85. Watch update — 2026-11-21, the eightieth hourly re-synthesis

The eightieth watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the seventy-ninth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 86. Watch update — 2026-11-21, the eighty-first hourly re-synthesis

The eighty-first watch re-enumerated the estate completely: 578 repos, every head read individually. One first read failed on a transport stream error; it was re-read individually and matched its last recorded head, so the final reads carry no errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Both moved repos are proof repos — this repo itself, and the emergence program repo, re-censused at theorem level in this pass and restated in section 3.23 above. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins except where this watch moves one.

No proof repo shrank at its fresh head. The emergence repo's proven set grew by five theorems and lost none: its premise audit discharged the accumulation monotonicity premise for the concrete measure, and its premise debt falls from four carried premises to three. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eightieth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 87. Watch update — 2026-11-21, the eighty-second hourly re-synthesis

The eighty-second watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eighty-first watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 88. Watch update — 2026-11-21, the eighty-third hourly re-synthesis

The eighty-third watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One of the moved repos is a proof repo and one is an idol-family repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eighty-second watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

The one idol-family repo moved without proof content: the compiler port, by four commits landing a single-register arithmetic slice and a re-judged slice record, its tree at the same file count with two files changed, its slices record and its native backend source. It was read by tree at its fresh head; no proof-assistant source was found in it and no tree read was truncated, so it remains proof-free by the named check. Its movement changes its pin only, not its placement.

## 89. Watch update — 2026-11-21, the eighty-fourth hourly re-synthesis

The eighty-fourth watch re-enumerated the estate completely: 578 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo — this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eighty-third watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 90. Watch update — 2026-11-21, the eighty-fifth hourly re-synthesis

The eighty-fifth watch re-enumerated the estate completely: 579 repos, every head read individually. The empty repos were each confirmed empty on a second read, so the final reads carry no errors. Eight repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Every moved repo is a proof repo, and the one new repo is a proof repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins except the new repo's, entered below at its head.

No proof repo shrank in count at its fresh head. The library repo and the highest minimal axis repo moved with every Lean file byte-identical, so their proven sets stand unchanged — the library's one hundred twenty-eight theorems, and the axis repo's fifty-eight, whose solver stood proposed at its census pin and now stands implemented in its tree at the fresh head, recorded at delta strength. The non-regression repo grew by sixty-six names and lost none, its new audit package proving the replacement characterizations and the conjunct refusal forms. The composable repo grew by seventy-nine names and lost none, its audited interaction model landing with its recorded gate receipts. The emergence repo grew by nine names and lost none, its indexed scan closing the fold form of its scan gap and leaving the system-level replay form as that gap's remaining content; its three carried premises stand. The redundant compute repo grew by twenty-seven names and lost none, its admission development binding claims on the log to recorded behavior. The traceability repo grew by fourteen names and lost one: the premise-carrying head theorem named in its annex no longer stands, replaced by the recorded-edge and recorded-head forms — flagged in its annex and in the ledger as a name loss at delta strength, its premise owed a re-trace in the full re-census. This repo itself moved only by the eighty-fourth watch landing, its eleven theorems unchanged.

### 3.25 Placement from the eighty-fifth watch (2026-11-21) — a new proof repo

- software-proofs-are-portable (public) — the twin construction: a release artifact carrying its own certificate as a derived part of itself, so checking the artifact and checking its proof are one act with one hash. Four theorems over an abstract digest, depending on no axioms: soundness, the transplant bound, the refusal, and sameness under the named separation premise, which stands as a premise and is not proved. Its one instance is the monotonic certification pipeline's first issuance, carried exactly as issued — its reading not certified, its three unmeasured dimensions standing as blockers — and its standing attack battery refuses the flip, transplant, and forgery forms while the detached form's fall to the same forgery is the executed control. Pin d2dd570c, which is its census pin. Placed in the loop at the admission stage's edge: it is the estate's first construction for how a proved result travels with the thing it certifies, and it upgrades no reading it carries.

## 91. Watch update — 2026-11-21, the eighty-sixth hourly re-synthesis

The eighty-sixth watch re-enumerated the estate completely: 581 repos, every head read individually, no read errors. One repo had moved since the last recorded heads, two were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is this repo itself, and both new repos are proof repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins except the new repos, entered below at their heads.

No proof repo shrank at its fresh head. This repo itself moved with no Lean file changed, so its proven set stands unchanged: its head moved only by the eighty-fifth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

### 3.26 Placement from the eighty-sixth watch (2026-11-21) — two new proof repos

- software-checking-is-choral (public) — the choral checking model: checking split across independent checkers by derivation cone, with the verdicts joined, accepts exactly what the whole check accepts, and the joined audit is the whole audit. Fourteen theorem declarations: the cone point result, the joined verdict over a covering family of three cones in both directions, and the audit point and join results, beside their fuel and fold lemmas, on three named premises — a rank witnessing acyclicity, a boundary agreeing with the whole check outside the cone, and an audit reading only the module and its dependencies — with two standing controls proving the boundary and coverage premises load-bearing. The audit states recorded at the pin name only the standard principles. Its instance is the verified cone partition of the semi development at two successive heads. Placed in the loop at the qualification stage: it is the estate first proved route to splitting one cold gate across checkers without changing its verdict, and the split run itself, with any speed figure, stands unclaimed and unrun. Pin f1ce1cb4, which is its census pin.
- software-estate-is-censused (public) — the incremental estate accounting: the estate-wide provable-result accounting maintained as an incremental derivation, a count re-derived only when its own pin moves and carried otherwise, proven exact against the from-scratch census for one step and for every append sequence, with an untouched repo keeping its pin and its count. Five theorem declarations, three of them headline, over an opaque counting function, on the declaration-counting basis premise and the append-only premise, with the registered three-run agreement evidence, a fourth confirmatory run, and one named uncountable entry carried as an exclusion, not an agreement. Placed in the loop at the accounting stage: it is the proved form of this synthesis own maintenance, and the watch switch to it stands as the development route remainder, not a landed change. Pin 1a67fef4, which is its census pin.

## 92. Watch update — 2026-11-21, the eighty-seventh hourly re-synthesis

The eighty-seventh watch re-enumerated the estate completely: 582 repos, every head read individually, no read errors. Three repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Every moved repo is a proof repo, and the new repo is a proof repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins except the new repo, entered below at its head.

No proof repo shrank at its fresh head. The non-regression repo grew from 203 declarations across 17 Lean files to 385 across 27, with no name lost, landing its dynamic release process in two commits. The traceability repo grew from 56 declarations across 5 Lean files to 284 across 20, with no name lost, landing its cumulative incremental hypergraph pipeline in six commits; the one name lost at its previous head stays flagged at that delta strength, and this movement neither restores it nor loses another. This repo itself moved with no Lean file changed, so its proven set stands unchanged: its head moved only by the eighty-sixth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

### 3.27 Placement from the eighty-seventh watch (2026-11-21) — one new proof repo

- software-qualification-is-two-sided (public) — the hinge width model: every qualified configuration has a dual unqualified witness, a nearest configuration that fails the qualification, and the distance to that witness is a computable quantity. Nineteen theorem declarations: the boundary result, that width one holds exactly at the qualification boundary; the margin result, that width minus one is zero exactly there; and the growth result, that width is monotone under premise strengthening — beside their space, distance, and fold lemmas, on the premises named in its annex, with three standing controls proving the failing existence and strengthening premises load-bearing and the monotonicity not vacuous. The audit states recorded at the pin name only the standard principles. Its instance is the decidability frontier standing instance, whose width distribution is recorded in the repo; the registered flip test is void on that instance, with zero observed flips, so no predictive verdict is claimed or placed. Placed in the loop at the qualification stage: it is the estate first proved measure of how far a qualified configuration sits from failing, and its adoption as a fragility measure stands unclaimed. Pin 6d68fbd8, which is its census pin.

## 93. Watch update — 2026-11-21, the eighty-eighth hourly re-synthesis

The eighty-eighth watch re-enumerated the estate completely: 582 repos, every head read individually. One first read failed on a transport stream error; it was re-read individually and matched its last recorded head, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eighty-seventh watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 94. Watch update — 2026-11-21, the eighty-ninth hourly re-synthesis

The eighty-ninth watch re-enumerated the estate completely: 582 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eighty-eighth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 95. Watch update — 2026-11-21, the ninetieth hourly re-synthesis

The ninetieth watch re-enumerated the estate completely: 582 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. One moved repo is a proof repo; the other is the compiler port, read by tree at its fresh head and carrying no proof-assistant content, so it remains proof-free by the named check. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the eighty-ninth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 96. Watch update — 2026-11-22, the ninety-first hourly re-synthesis

The ninety-first watch re-enumerated the estate completely: 582 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Nine repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Every moved repo is a proof repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, with a full theorem-level re-census at the fresh heads owed where the annex deltas say so.

Six proof repos grew at their fresh heads with no name lost: the perception repo by thirty-six declarations, the regression repo by forty-nine, the frontier repo by twenty-three, the safe repo by four, the traceability repo by twenty-three, and the optimality repo by sixty-eight. The library repo stands unchanged, every Lean file byte-identical, its movement a new kernel evidence folder only. This repo itself moved only by the ninetieth watch landing, its eleven theorems unchanged. One regression is flagged: the solvable repo was restructured, its total count fell by one, and twenty-two names present at its last recorded head are absent at its fresh head against twenty-two gained; that flag stands in the ledger refresh and is not absorbed here.

## 97. Watch update — 2026-11-22, the ninety-second hourly re-synthesis

The ninety-second watch re-enumerated the estate completely: 582 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the ninety-first watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 98. Watch update — 2026-11-22, the ninety-third hourly re-synthesis

The ninety-third watch re-enumerated the estate completely: 582 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

No proof repo grew or shrank at its fresh head. This repo itself moved with every Lean file byte-identical, so its proven set stands unchanged: its head moved only by the ninety-second watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged at the fresh head.

## 99. Watch update — 2026-11-22, the ninety-fourth hourly re-synthesis

The ninety-fourth watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Seven repos had moved since the last recorded heads, one was new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Six of the moved repos are proof repos and one is an idol-family repo, the relay, read by tree at its fresh head and proof-free by the named check. The new repo is a proof repo. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, except the new repo's, entered at its head in this pass.

The new proof repo is the Pareto proof home, public, at 426ac15d: twenty theorems in its proof file proving obligations one to nine and fourteen of the Pareto proof methodology record over the general definitions — finiteness derived from the declaration lists, receipt binding and pairwise agreement under their named premises, locality of the verdict in the two rows — beside twelve checked test instances and one standing control, the draft that states finiteness as a hypothesis and must be refused by the repo's audit, with its gate record standing in its readme at the pin. Obligations ten to thirteen and fifteen to twenty stand as named unclaimed work, and no instance claim is made. It is placed in the family at its head, which is its census pin.

Three proof repos grew at their fresh heads with no name lost: the deterministic models repo (84 declarations, fresh head 97829523), the redundant compute repo (375 declarations, fresh head edbcb2a0), and this repo itself (17 theorems, fresh head 7faf4d0c, the six new loom theorems axiom-free on the verification record in its tree). Three proof repos stand unchanged with no Lean file among their changed files: the library repo (fresh head 4ff0c5d2), the parametric language model repo (fresh head 2ed9a077), and the reversible repo (fresh head 799bc652). No proven set shrank and no regression is flagged.

## 100. Watch update — 2026-11-22, the ninety-fifth hourly re-synthesis

The ninety-fifth watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Both moved repos are proof repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins, except the Pareto repo's, restated at its fresh head in this pass.

The Pareto proof repo grew at its fresh head 5b45d5fd with no name lost: its second lane landed in one commit — a second proof file of 38 declarations discharging obligations ten to thirteen and fifteen to twenty, beside six new checked test instances — so all twenty obligations of the Pareto proof methodology record now stand proved over the general definitions, the premise registry carried explicit and no instance claim made. It was re-censused at theorem level in full in its annex, and its census pin moves to 5b45d5fd in this pass. This repo itself moved only by the ninety-fourth watch landing — its five commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head 1bf2ddc9. No proven set shrank and no regression is flagged.

## 101. Watch update — 2026-11-22, the ninety-sixth hourly re-synthesis

The ninety-sixth watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo: this repo itself. The annex files carry the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo itself moved only by the ninety-fifth watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head dac376cb. No proven set shrank and no regression is flagged.

## 102. Watch update — 2026-11-22, the ninety-seventh hourly re-synthesis

The ninety-seventh watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Four repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. All four moved repos are proof repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

Three moved proof repos grew with no name lost. The highest minimal axis repo gained nine declarations at its fresh head 04d50693 — an incremental solver development beside the solver recorded earlier: the join and scoped liveness forms, the deletion forms, and the witness forms, in a new Lean file beside an audit file carrying no declarations. The quantifiable repo gained 38 declarations at its fresh head 68e90c47 — the closure group of the update and checker spine, obligations ten to twenty-one, in one new Lean file. The redundant compute repo gained 42 declarations at its fresh head 2a27f6cb — a monotone synthesis example whose core and controls files carry the append-only admission loop development. This repo itself moved only by the ninety-sixth watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head 1122701a. No proven set shrank and no regression is flagged.

## 103. Watch update — 2026-11-22, the ninety-eighth hourly re-synthesis

The ninety-eighth watch re-enumerated the estate completely: 583 repos, every head read individually. One first read failed on a transport stream error; it was re-read individually and matched its last recorded head, so the final reads carry no errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Both moved repos are proof repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

The idol repo moved at its fresh head a70fa9e9 with its proof-bearing content unchanged: every Lean file is byte-identical between its heads, and its movement is specification, gap record, and compiler work — the equational rewriting spec, the circuit producer spec carried as spec-first with no producer in the tree, eight gap records for unfiled zero-loss capabilities, and the carried relations walk descending into descriptor declarations. This repo itself moved only by the ninety-seventh watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head ff3e64c4. No proven set shrank and no regression is flagged.

## 104. Watch update — 2026-11-22, the ninety-ninth hourly re-synthesis

The ninety-ninth watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Three repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Two moved repos are proof repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

The idol repo moved at its fresh head e4d293ef with its proof-bearing content unchanged: every Lean file is byte-identical between its heads, and its movement is compiler work — overload selection gaining a record fit tier and a next method chain face, with zero-field records admitted as scalar operands, application results, and C construction regions, beside its recorded checker and backend controls. The sites repo moved at its fresh head d90871c8 with two dated audit folders added for two spaces and the paper page file byte-identical between its heads. This repo itself moved only by the ninety-eighth watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head e87e19ec. No proven set shrank and no regression is flagged.

## 105. Watch update — 2026-11-22, the hundredth hourly re-synthesis

The hundredth watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo: this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo itself moved only by the ninety-ninth watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head 4d7d81ff. No proven set shrank and no regression is flagged.

## 106. Watch update — 2026-11-22, the hundred-first hourly re-synthesis

The hundred-first watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. Two repos had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. Both moved repos are proof repos. The annex files carry the evidence at the fresh heads; the placements in section 3 stand at their census pins.

The quantifiable repo moved at its fresh head 4e98484d with the remaining groups of its update and checker spine landed — the delta group (obligations one to nine), the coverage group (obligations twenty-two to thirty-two), and the end-to-end group (obligations thirty-three and thirty-four), joining the closure group landed at the last recorded head — its declarations growing from 246 to 363 with no name lost. This repo itself moved only by the hundredth watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head dbcc122c. No proven set shrank and no regression is flagged.

## 107. Watch update — 2026-11-22, the hundred-second hourly re-synthesis

The hundred-second watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo: this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo itself moved only by the hundred-first watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head c709725e. No proven set shrank and no regression is flagged.

## 108. Watch update — 2026-11-22, the hundred-third hourly re-synthesis

The hundred-third watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo: this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo itself moved only by the hundred-second watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head 9fc62855. No proven set shrank and no regression is flagged.

## 109. Watch update — 2026-11-22, the hundred-fourth hourly re-synthesis

The hundred-fourth watch re-enumerated the estate completely: 583 repos, every head read individually; the eighty empty repos returned no branch, matching their recorded empty state, so the final reads carry no errors. One repo had moved since the last recorded heads, none were new, none were gone, and the paper source hash was unchanged, so no paper re-sync was owed. The one moved repo is a proof repo: this repo itself. The annex file carries the evidence at the fresh head; the placements in section 3 stand at their census pins.

This repo itself moved only by the hundred-third watch landing — its four commits carry no Lean change, so its own seventeen theorems stand unchanged at the fresh head 9da5096a. No proven set shrank and no regression is flagged.
