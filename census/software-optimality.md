# Theorem census — software-optimality (Lean repo)

## Clone state, read as-is

- Clone head, as read (no edit, no pull performed for this census):
  - `0ea4626` — Prove hypergraph-derived incremental qualification and interaction views
  - `f2be60a` — Add checked exact metric relevance profiles and fail-closed proof runner
  - `6746b0c` — Add audited scoped qualification-to-selection bridge and proof design
- Toolchain pinned in the clone: Lean 4.19.0. The readme says: checked with Lean 4.19.0 (release commit beginning 6caaee), no external packages, no Mathlib library, and "These are not proofs of an unrelated production implementation."
- Sources read for this census: the readme, the checker log, the checker-controls note, the hypergraph scope note, the proof-design document in docs, and all 14 root Lean modules listed below.
- Checker discipline, in substance from the readme and the controls note: the check script rejects source admissions and custom axioms, treats warnings as errors, checks each compiler exit, and rejects admitted-axiom and error diagnostics; exit zero is required and the full captured output is in the checker log. The controls note records two negative controls on a separate temporary copy: a deliberately admitted proof (a false theorem proved by an admission) was rejected with nonzero exit before compilation, and an injected reference to a nonexistent name was rejected with nonzero exit on the compiler error. It also records that matching hashes alone never establishes proof success, after an earlier rejected archive masked a compiler failure behind a later successful packaging step.
- Global trust boundary, in substance from the readme: no admission, no custom axioms, and no native-decision shortcut occur anywhere. Some finite-reference proofs use the standard Lean foundational axioms — propositional extensionality, classical choice, and quotient soundness — through library lemmas, as disclosed by the axiom prints in the checker log. Classical reasoning is used in proofs, not to implement the executable algorithms.
- Global non-claims, in substance from the readme's trust section: "Not proved here: runtime instrumentation fidelity, cryptographic hash binding, external policy authorization, complete language lowering, arbitrary test termination, universal behavior preservation, numerical confidence of measurements, efficient worklist refinement or tight complexity bounds, an incremental provenance/deletion implementation, or globally optimal software performance. These are distinct obligations, not concealed assumptions of the proved closure/qualification results."
- Also global: policies, scopes, lineages, opposite polarities and evidence identities can be encoded in atoms; their validation is an explicit input obligation, not supplied by set closure. Runtime receipts are not automatically universal semantic proofs. Old evidence does not itself qualify a changed release; a current support or a valid transfer derivation is required. Withdrawal filters live roots and rules and recomputes, preserving historical events; the current projection is not monotone when withdrawals occur.

## How axiom lists are reported here

Per module, the census lists the axiom dependencies printed in the checker log for the theorems that log prints. "Empty" means the log line reads "does not depend on any axioms". "Standard" means some subset of the three standard foundational axioms named above: propositional extensionality, classical choice, quotient soundness. Theorems present in a file but not printed in the checker log are noted as not printed, where that matters.

---

## 1. Qualification — general derivation semantics

### Purpose in plain English
The language-independent core. Exact scoped support atoms and finite-premise inference and transfer rules define rooted derivations: an atom is supported if it is a root, or if a rule whose premise list is admitted derives it from premises that are themselves derived. Everything else in the repo builds on this least-derivation semantics.

### Headline theorems
- Leastness (`least`): any set that contains all roots and is closed under all rules contains every derived atom. This is induction on derivations.
- Monotonicity (`monotone`): enlarging the root set and enlarging the rule set (pointwise) preserves every derivation.
- Idempotence (`idempotent`): deriving from the already-derived set as roots, with the same rules, derives exactly the original set — membership in the twice-closed set is equivalent to membership in the once-closed set.
- Compounding (`compounding`): closing the union of two root sets equals closing the union of their separate closures, as a pointwise membership equivalence. Hypotheses: two root predicates and one shared rule relation. Conclusion retains new cross-source consequences.
- Order independence (`order_independent`): any two sound, exhaustive saturations — sets containing the roots, closed under the rules, and contained in the derivation set — agree pointwise.
- Soundness (`soundness`): if every root is true under a chosen truth predicate and that predicate is closed under the rules, then every derived atom is true. Semantic soundness is conditional on valid roots and rules.
- Withdrawal containment (one theorem, quoted token `withdrawal` in substance): a derivation from live roots and live rules (roots and rules with withdrawn items filtered out) is also a derivation from the original roots and rules — withdrawal creates no new support.
- Surviving subsystem (`surviving` in substance): any derivation inside a subsystem whose roots and rules are all still live survives withdrawal elsewhere, as a derivation in the live-filtered system.
- No unsupported cyclic bootstrap (`no` bootstrap in substance): if every rule has at least one premise, then from the empty (everywhere-false) root set nothing is derivable.
- Also in the file, not separately printed in the log: the derivation set itself is closed under its rules.

### Axiom dependencies
All nine printed theorems in this module have EMPTY axiom lists in the checker log: leastness, monotonicity, idempotence, compounding, order independence, soundness, withdrawal containment, surviving subsystem, and no-bootstrap. The file header states: "No additional axioms or admissions."

### Explicit non-claims and boundaries
- The compounding identity is the closure-of-closures form above. In the readme's exact substance: it "does not claim" that closing a union equals the union of the two closures; "new cross-source consequences are retained."
- Soundness is conditional only: truth follows only under the hypotheses that roots are valid and rules preserve truth. The module supplies no validation of any particular roots or rules.
- Atoms are "exact scoped support atoms, including lineage and polarity" per the file header; encoding policies, scopes, lineages and polarities into atoms is allowed, but their validation is an explicit input obligation, not supplied by closure (readme trust section).
- Withdrawal is filtering of live roots and rules; "no historical fact is deleted" (file comment). The current projection after withdrawal is not claimed monotone.

---

## 2. ExecutableClosure — executable saturation with exact refinement

### Purpose in plain English
A deliberately exhaustive executable version of the core closure: enumerate every sublist of a finite universe, keep those that contain the roots and are closed under all rules, and return the intersection of those models. It provides the checked bridge between the executable reference algorithm and the inductive derivation semantics of module 1, plus a fail-closed public face.

### Headline theorems
- Exact refinement (`close` exactness in substance): under decidable equality of atoms, every root in the universe, and every admitted rule head in the universe, an atom is in the executable result if and only if it is inductively derivable. Rule premises need not be bounded: an outside premise cannot acquire support because all roots and heads are bounded.
- Subset count: the enumeration produces exactly 2 raised to the length of the universe enumerated subset candidates, "with positional multiplicity if [the universe] contains duplicates" (readme).
- The executable result is closed under the rules, and it contains every (live) root — both under the same boundedness hypotheses.
- Order independence of the executable result: reordered or duplicated equivalent roots and rules (same membership) give exactly the same result membership, under boundedness for both presentations.
- Executable monotonicity: if one root set and rule set are included in another, the first executable result is included in the second. Withdrawal is the reverse-inclusion case.
- Bounded-check exactness: the Boolean boundedness check is true exactly when every root and every rule head lies in the universe.
- Checked face admitted case: whenever the checked function returns a value, the bounds hold and the returned list has exactly the inductively derivable members.
- Checked face rejection case: the checked function returns no value if and only if those bounds fail.
- Supporting lemmas in the file, not all printed in the log: every member of an enumerated sublist is a member of the universe; the filtered universe is among the enumerated sublists; the per-rule and per-model Boolean checks are exact against the propositional closedness definition.
- Executable guards in the file cover both out-of-universe roots and out-of-universe heads, a cross-source consequence case, a withdrawn-support case, and an unsupported cycle case.

### Axiom dependencies
No printed theorem here is empty. From the checker log:
- Subset count: propositional extensionality only.
- Bounded-check exactness and checked-face rejection: propositional extensionality and quotient soundness.
- Checked-face admitted case, executable monotonicity, exact refinement, closedness, root containment, and order independence: all three standard axioms.

### Explicit non-claims and boundaries
- Raw function unsafe outside preconditions — verbatim in substance from the readme: "Use [the checked function] at runtime, not raw [close]." The checked function "validates that every root and rule head belongs to the named universe and returns [none] when invalid." Raw close "is a mathematical implementation under explicit preconditions: outside them its model list can be empty and its intersection vacuously return the entire universe, so it must not be exposed as a fail-closed API."
- Deliberately exponential: "This is a deliberately exponential reference algorithm, not an optimized worklist. Its purpose is a complete executable specification with a checked bridge to the general derivation semantics. No unproved iteration cap or saturation heuristic is used." (readme)
- All executable functions terminate by structural recursion (readme).

---

## 3. FiniteQualification — exact qualification enumeration

### Purpose in plain English
Exhaustive enumeration of all Boolean profiles of a given dimension, and exact filtering of them by a supplied total Boolean evaluator.

### Headline theorems
- Count: the candidate list for dimension n has length exactly 2 raised to n.
- Completeness by membership: a Boolean list is among the candidates for dimension n if and only if its length is exactly n. The readme stresses: "Completeness is a membership theorem, not inferred merely from counting candidates."
- Filtering exactness: a profile is in the filtered qualification list if and only if its length is n and the supplied evaluator returns true on it.

### Axiom dependencies
- Count: propositional extensionality only.
- Membership completeness and filtering exactness: all three standard axioms.

### Explicit non-claims and boundaries
- The evaluator is an input, in the file's own substance: the evaluator "is executable and total. It is an input, not assumed to decide arbitrary semantics." No claim that the evaluator captures any real qualification semantics beyond what the caller supplies.

---

## 4. FiniteFrontier — Pareto selection and coloring

### Purpose in plain English
Executable nondominated filtering over a named finite candidate list under a supplied dominance predicate, a checked strict Pareto comparator over integer costs, and a four-way support coloring.

### Headline theorems
- Frontier exactness: a candidate is in the filtered frontier if and only if it is in the named candidate list and no candidate in that list dominates it (the dominance predicate is false for every listed candidate against it).
- Pareto comparator exactness (`pareto` in substance): the strict Pareto Boolean is true if and only if the first candidate is no worse on every named axis (componentwise integer costs, less-or-equal) and strictly better on at least one named axis.
- Conflict characterization: the coloring is the conflict value if and only if both the positive and the negative Boolean inputs are true.
- Unknown characterization: the coloring is the unknown value if and only if both inputs are false.
- The four-way coloring distinguishes unknown, lawful, unlawful, and conflict (readme).

### Axiom dependencies
- Frontier exactness and Pareto exactness: propositional extensionality and quotient soundness.
- Conflict and unknown characterizations: EMPTY axiom lists.

### Explicit non-claims and boundaries
- Relative frontier only, verbatim in substance from the readme: "The frontier theorem is relative to the supplied candidate universe and measurements. It does not assert that enumerated candidates include every possible implementation, or that the reference algorithm itself is Pareto optimal."
- "Costs and finite axes are inputs; an axis to maximize must be normalized accordingly." (readme)
- The dominance predicate is a supplied, chosen total comparison predicate; the frontier is the Pareto frontier only when that predicate represents strict Pareto dominance (file comment).

---

## 5. FiniteSchedules — test ordering and parallel schedules

### Purpose in plain English
Finite enumeration and exact feasibility checking for start-tick schedules (one venue and one start tick per job, up to a horizon), for per-venue ordered queue schedules used by external test runners, and for certificates of optimality and of behavior-preserving improvement within that finite model.

### Headline theorems
- Tuple enumeration exactness: a list is among the enumerated tuples of a given length over a choice list if and only if it has that length and every element is in the choice list.
- Enumeration exactness: a schedule is enumerated if and only if its length equals the job count and every placement has venue below the venue count and start at or below the horizon. Completeness is "proved by exact membership, not by assuming a generator sampled everything" (readme).
- Feasibility exactness: the Boolean feasibility check is true if and only if the propositional feasibility holds: correct list size, placement bounds, nonoverlap for each pair of jobs on the same capacity-one venue, and every listed dependency including endpoint bounds.
- Feasible-filter exactness: a schedule is in the filtered feasible list if and only if it is feasible in the propositional sense above.
- Certificate exactness for a supplied finite list: the certificate Boolean is true if and only if the schedule is in the list and no listed candidate dominates it.
- Certified optimality (`certified` in substance): an accepted certificate designates a feasible schedule with no strict Pareto dominator among all schedules of this enumerated model, on the named axes and the supplied total integer cost function.
- Queue feasibility exactness: the queue check is true if and only if the queue count matches the venue count, every queued job is below the job count, and every job below the count occurs exactly once in the flattened queues — "every numbered job occurs exactly once, there are no extra job ids, and the queue count matches the venue count" (readme).
- Improvement certificate exactness: the improvement Boolean is true if and only if the new schedule is feasible, the preservation checker accepts the pair, and the new schedule strictly Pareto-dominates the old on the named axes.
- Accepted improvement (`accepted` in substance): feasibility, strict Pareto improvement, and behavioral preservation follow when a supplied preservation-certificate checker is sound — preservation is concluded only under the explicit hypothesis that the supplied checker implies actual preservation.

### Axiom dependencies
- Propositional extensionality and quotient soundness only: queue feasibility exactness, improvement certificate exactness, accepted improvement, feasibility exactness, certificate exactness.
- All three standard axioms: tuple enumeration exactness, schedule enumeration exactness, feasible-filter exactness, certified optimality.

### Explicit non-claims and boundaries
- Horizon scope: "Durations are nonnegative integer inputs; the horizon bounds start times, not completion times." (readme)
- Homogeneous venues: "Venues are homogeneous in this model; shared/external resources need additional constraints." (readme)
- Zero-duration literalness: "The pairwise ordering predicate treats zero-duration jobs literally and does not model every empty-interval convention; zero-duration dependency cycles can satisfy its non-strict precedence inequalities. Positive durations and acyclic dependencies should be enforced separately when required by a deployment." (readme)
- External lists: the generic certificate "can also certify any supplied finite candidate list, but completeness of an externally generated candidate list must be established separately." (readme)
- Queues: the queue theorem "does not assert arbitrary queue ordering preserves side effects." (readme)
- Preservation is conditional: accepted improvement holds "when a supplied preservation certificate checker is sound. This makes the separate preservation obligation explicit for test rewrites/reordering; lower measured times alone never discharge it." (readme and file comment)
- Foreign scope: "These theorems apply to schedules of foreign software tests without lowering their programs into an IR. They do not prove the foreign tests' semantic independence, their completeness as program specifications, or the empirical durations' future stability. Physical benchmark measurements and external queue enumeration remain separately qualified evidence." (readme)

---

## 6. ForeignCampaign — concrete foreign test-campaign certificate

### Purpose in plain English
A concrete, materialized instance: four foreign test jobs with imported nanosecond durations, 120 supplied ordered two-worker queue candidates with expected metric rows, all materialized as Lean data and checked by the kernel, with a chosen queue proved to improve on a baseline and to be nondominated, and the computed frontier proved equal to four supplied frontier schedules.

### Headline theorems and checked facts
- There are exactly 120 candidates, they are pairwise distinct (erasing duplicates leaves 120), and every candidate is queue-feasible for 4 jobs on 2 venues.
- Receipt metrics match: every supplied metric row equals a fresh model calculation from the duration constants, for both modeled axes — makespan (maximum per-queue duration sum) and sum of all jobs' completion times.
- Chosen queues (in the readme's description, packaging alone on one queue; tomli, attrs, click on the other) have modeled costs 6,991,879,848 and 10,280,231,762, versus baseline costs 9,006,285,993 and 13,775,558,659 for the single-queue baseline in original order.
- The chosen candidate is accepted by the certificate checker over the supplied list; equivalently it is in the list and no listed candidate strictly Pareto-dominates it.
- Strict Pareto improvement of the chosen candidate over the baseline is proved exactly: no worse on both named axes and strictly better on at least one.
- Complete-list frontier: the computed frontier of the supplied list under the modeled dominance predicate equals exactly the four supplied frontier schedules, including worker swaps (readme).
- Input durations, in nanoseconds, as recorded in the readme and the file: the four jobs at 1,033,599,117; 687,668,287; 293,138,741; and 6,991,879,848. The source campaign snapshot hash is recorded in the module.

### Axiom dependencies
- EMPTY axiom lists: chosen accepted, receipt metrics match, complete-list frontier.
- Propositional extensionality and quotient soundness: chosen nondominated, modeled improvement exactness.
- Several concrete facts in the file (candidate count, distinctness, all feasible, the two cost equalities, the raw dominance Boolean) are proved by kernel decision and are not separately printed in the checker log.

### Explicit non-claims and boundaries
- Decision method: "The concrete calculation proofs use [kernel decision], checked by Lean's kernel, not [native decision]." (readme) Durations "are input observations, not facts proved by Lean" (file comment).
- Scope of the ranking: "This proves arithmetic, feasibility and ranking for the imported candidate list and cost model. The generic start-tick enumeration theorem does not establish completeness of the separate queue-list generator." (readme)
- Observations are not consequences: "Physical runs, timing medians, process isolation, and semantic equivalence of foreign test suites are independently collected observations, not consequences of the Lean ranking proof. In particular the measured parallel wall-clock percentage must not be described as a proven future speedup." (readme)

---

## 7. EligibleSchedules — hard observed admission before optimization

### Purpose in plain English
A hard admission gate that runs before any cost ranking: a candidate must be feasible, must satisfy a provided observed-behavior predicate, and must pass every required timing check against its own declared limit. Only admitted candidates can be optimal.

### Headline theorems
- Timing check exactness: a single timing check passes if and only if a measured value is present and is at most the declared limit. A missing timing is not a pass (file comment: "absent measurement is not a pass"); equality at the limit is accepted; "no hidden tolerance is applied" (readme).
- Timed admission exactness (`timedAdmission` in substance): admission holds if and only if the required count is positive, exactly that many receipts (checks) exist, and every elapsed value is present and no greater than its declared per-receipt limit. "A missing timing, empty zero-round campaign, or even one over-limit result is rejected." (readme)
- Eligibility exactness: the combined gate is true if and only if feasibility holds, the observed predicate holds, and timed admission holds with all its conjuncts.
- Optimum certificate exactness: the certificate is true if and only if the selected candidate is in the catalogue and passes the gate, and no admitted candidate in the catalogue strictly Pareto-dominates it on the chosen axes.
- Rejected cannot be optimal: if the gate is false for a candidate, its optimum certificate is false — "a faster cost score [cannot override] a failed gate" (readme paraphrase of the theorem's role; file framing: "Optimality is ONLY over eligible candidates; cost cannot override rejection.").
- Dominator refutes certificate: an admitted candidate that strictly dominates the claimed optimum constructively invalidates the certificate — the certificate Boolean is false.

### Axiom dependencies
All six printed theorems — single timing exactness, timed admission exactness, eligibility exactness, optimum certificate exactness, rejected-cannot-be-optimal, and dominator-refutes-certificate — depend on propositional extensionality and quotient soundness. None is empty; none uses classical choice.

### Explicit non-claims and boundaries
- Recorded cases only: "The theorem checks the recorded cases and does not predict unseen runs." (readme)
- Ceiling naming: "Timing inputs can represent fixed ceilings or paired observed-baseline ceilings; the choice must be named by the policy." And: "A paired-baseline experiment is not presented as a user-authored absolute SLA." (readme; the readme uses the abbreviation for service-level agreement.)
- Observed predicate is an input: "The observed-behavior Boolean is a policy input; validation of its underlying receipt contents is separate from treating it as evidence of universal behavior preservation." (readme)

---

## 8. EligibleCampaign — measured pilot and tested alternate

### Purpose in plain English
The concrete measured pilot as Lean data: three plans (original tests on one worker; original tests on two workers; reverse-collected tests on the same two-worker plan), three paired rounds, per-round hard caps taken from the one-worker plan's observed wall times, receipt flags as imported Booleans, and kernel-checked admission, ranking, and frontier for the three-plan catalogue on the single wall-time objective.

### Headline theorems and checked facts
- All three plans have exactly three recorded rounds; all receipt-flag conjunctions pass; all hard timing checks pass; all three plans are admitted by the gate. In the readme's emphasis: "none of these observed candidates is gate-rejected."
- The two-worker original plan is a qualified optimum: its optimum certificate over the admitted catalogue on the single axis is true, with the exact semantics that it is admitted and no admitted candidate strictly dominates it.
- Exact eligible frontier: the frontier of the admitted catalogue is the singleton list containing only the two-worker original plan.
- Exact costs (maximum observed wall time): one-worker plan 10,769,189,848 ns; two-worker plan 6,240,471,073 ns; reversed plan 9,146,680,841 ns. Per-round caps are the one-worker times 10,769,189,848, 7,296,152,413, and 7,966,428,370; the two-worker observations are 5,429,128,102, 6,128,442,901, 6,240,471,073; the reversed observations are 9,146,680,841, 6,480,720,115, 6,777,395,883 (readme).
- The reversed alternate is admitted but is not an optimum; the two-worker plan strictly dominates it; and the two-worker plan is faster in every recorded paired round.
- A synthetic negative control exceeding one cap by one nanosecond is proved rejected.
- The linear selector of module 10 agrees on this pilot, returning the two-worker plan (cross-checked in that module's entry).

### Axiom dependencies
- EMPTY axiom lists: linear selector agreement, all admitted, chosen qualified optimum, exact eligible frontier, counterfactual (reversed plan) admitted, chosen beats counterfactual, counterfactual not optimum, every paired counterfactual slower, and the synthetic one-nanosecond-over-cap rejection.
- Optimum semantics: propositional extensionality and quotient soundness.
- The remaining concrete facts are kernel-decision proofs not separately printed in the log.

### Explicit non-claims and boundaries
- Imported, not proved: "This module checks imported observations, not their measurement/instrumentation truth." (file comment) "All three plans' imported per-job receipt flags report identical collected ids and phase/outcome/skip records plus successful exits; these Boolean receipt comparisons are inputs whose underlying raw files are audited separately." (readme)
- Worker capacity "is a constraint, not a quality axis" (readme); in the file: worker slots are a feasibility constraint, "NEVER an invented quality axis." The sole objective is maximum observed wall-clock nanoseconds across three paired rounds.
- No causality or forecast: the reversed-plan comparison "is not a proof of physical causality or a forecast." (readme)
- Preregistration boundary, verbatim in substance: "The hard gate was specified before the runs; the objective was corrected during the run before analysis to wall time only, preserving the earlier policy revision in the empirical artifacts. Do not describe the corrected objective as preregistered before all execution, or the paired-baseline caps as an absolute SLA provided by the user." (readme; abbreviation as in the source.)
- Publication clarification (readme): the pilot timing gate is whole-suite wall time only — 8 of 12 two-worker subprocess times were slower than paired one-worker times; three paired rounds and recorded inputs do not establish future or per-test no-regression; the reversed plan was admitted but dominated, not rejected; policy revision chronology has no signed precommit or independently authenticated timestamp.

---

## 9. ScopedEvidence — identified evidence and policy-bound scope

### Purpose in plain English
A stricter evidence checker that fixes a gap in the generic timing-list interface: receipts are identified and scoped, so duplicated or mis-scoped receipts cannot count as independent observations. A scope key explicitly includes artifact, configuration, lineage, venue, harness, intent, policy, and metric identity; each obligation names its scope, its round, and a policy-supplied limit; receipts carry their own unique identity, scope, round, observed-pass flag, and optional measured elapsed time, and cannot choose their own cap.

### Headline theorems
- Per-requirement check exactness: a requirement is satisfied if and only if exactly one receipt matches its scope and round, that receipt's observed-pass flag is true, and its elapsed value is present and at most the requirement's limit.
- Accepted receipt is scoped: any accepted requirement yields an actual receipt in the list with matching scope and round, passing flag, and a measured value within the limit.
- Qualification exactness (`qualify` in substance): the qualification Boolean is true if and only if all of: the requirement set is nonempty; scope/round requirement keys are unique; every required scope is tied to the named policy; requirement and evidence counts are equal; receipt identities are unique; and exactly one matching receipt satisfies every requirement.
- Witness extraction (`qualification` witnesses in substance): successful qualification exposes, for each obligation, an actual matching receipt and its measured bound.
- Duplicate rejection: matching conflicting duplicates are rejected even if one receipt reports success — a filter result with two or more matching receipts makes the per-requirement check false.
- Wrong-scope rejection: if every receipt's scope differs from the requirement's scope, the check is false. "Wrong-scope receipt sets and conflicting matching duplicates are proved rejected." (readme)
- Soundness relative to validation: if a supplied validation step turns every witnessed, scoped, passing, in-limit receipt into a stated holding property for its requirement, then qualification implies that property for every required obligation. Semantic interpretation is an explicit validation premise.
- Synthetic executable controls in the file cover: missing receipt, duplicate round (repeated identity), repeated identity, wrong metric, wrong policy, and one-unit over-limit evidence (readme list); the file's guards also cover the plain success case and a conflicting duplicate match.

### Axiom dependencies
- Propositional extensionality and quotient soundness: per-requirement exactness, accepted-receipt-is-scoped, qualification exactness, witness extraction, wrong-scope rejection, relative soundness.
- Duplicate-match rejection: propositional extensionality only.
- None printed is empty.

### Explicit non-claims and boundaries
- Opaque identifiers, authenticity not proven — verbatim in substance from the readme: "These are opaque canonical identifiers: equality checking is proved, but cryptographic authenticity, parser correctness, whether a supplied policy ID really commits to its bytes, and observation instrumentation remain separate obligations." The file header says the same: "Equality binds claims; it does not prove hash authenticity."
- No scope transfer: "The suite-elapsed metric scope must not be transferred to per-job elapsed: the recorded pilot contains individual subprocess slowdowns even though the admitted suite elapsed improves." (readme)
- No inferred cross-lineage reuse: "Cross-lineage reuse requires an explicit independently checked transfer; this checker never infers it from shared content alone." (readme)
- Observed-pass is not universal correctness: the relative-soundness theorem "makes semantic interpretation an explicit validation premise rather than assuming observed-pass means universal correctness." (readme)

---

## 10. LinearSelection — efficient scalar optimum, not all-pairs search

### Purpose in plain English
For a single declared scalar objective, an eligible-list argmin that replaces all-pairs dominance checking, with a proved comparison count, plus a public set-valued version that returns all tied minima.

### Headline theorems
- Single-winner specification: the recursive winner is a member of the head-plus-tail input and its cost is at most the cost of every member.
- Selected minimum: whenever selection returns a winner, the winner is in the input list and its cost is at most every listed candidate's cost.
- Selected eligible minimum: when selection runs over the gate-filtered list, the winner is in the original list, passes the gate, and its cost is at most that of every gated candidate. "Eligibility is filtered before any comparison, never traded against the objective." (file comment)
- Counted refinement (`counted` in substance): an instrumented version of the same recursion returns the same winner and performs exactly one comparison per tail element — that is, n minus 1 comparisons on a nonempty n-candidate input, since the instrumented count equals the tail length.
- All-minima exactness (`allMinima` in substance): a candidate is in the all-ties result if and only if it is in the input and its cost is at most every input candidate's cost.
- All-minima order independence: membership in the all-ties result is unchanged under any reordered or duplicated equivalent input catalogue (same membership both ways).

### Axiom dependencies
- Propositional extensionality and quotient soundness: all-minima exactness, all-minima order independence, single-winner specification, selected minimum, selected eligible minimum.
- Counted refinement: propositional extensionality only.
- None printed is empty.

### Explicit non-claims and boundaries
- Count scope: "This count excludes gate evaluation, cost computation and data loading; it is not a physical runtime benchmark." (readme)
- Tie handling split: "The internal one-winner helper retains the earlier candidate on equal costs and therefore is not identity-order-invariant. The public set-valued [all-ties function] instead returns all tied scalar minima." (readme) The file comment says the same: equal costs keep the earlier candidate.
- Serialization not claimed: "Output list serialization is not claimed identical; canonical serialization is a separate concern." And for the tie-preserving method: it "adds a linear filter/equality pass after the [n minus 1]-comparison minimum pass." (readme)
- Scalar only: "It is a scalar optimum set, not a general multi-axis Pareto frontier." (readme)

---

## 11. ScopedSelection — the integration bridge, selection side

### Purpose in plain English
The bridge that makes the final selection entry point use the scoped evidence checker of module 9 directly as its gate, so no unbound observed-pass Boolean can bypass scoped evidence validation, and connects optimum certificates and efficient all-ties selection to actual scoped witnesses.

### Headline theorems
- Certified scoped optimum (`certified` in substance): an accepted optimum certificate over the scoped gate implies the candidate is in the catalogue, its scoped qualification passes, every one of its obligations has an actual witness receipt (matching scope and round, passing, in limit), and no scoped-qualified candidate strictly dominates it on the named axes.
- Selected scoped minimum: a winner returned by the scoped-gated linear selection is in the catalogue, passes scoped qualification, and costs at most every scoped-qualified candidate.
- Selected-all exactness: membership in the all-ties scoped selection is equivalent to: in the catalogue, scoped-qualified, and cost at most every scoped-qualified candidate.
- Selected-all order independence: that membership is invariant under any equivalent (same-membership) reordering or duplication of the catalogue.

### Axiom dependencies
All four printed theorems depend on propositional extensionality and quotient soundness. None is empty; none uses classical choice.

### Explicit non-claims and boundaries
- Shared-contract obligation at ingestion: "The generic selector receives per-candidate policies and a numeric cost function; it does not itself prove those candidates share the same intent/metric/comparison contract. Ingestion must restrict a comparison catalogue to compatible policies and units. The concrete pilot does so by its single documented wall-time policy." (readme)
- This module is the selection bridge only; the transport, deduplication, and authenticity boundaries stated for the pair of bridge modules are recorded under module 12.

---

## 12. ScopedCampaign — the integration bridge, concrete pilot side

### Purpose in plain English
The concrete instantiation of the bridge on the recorded three-plan pilot: identified, round-keyed obligations and receipts are constructed from the pilot data, including capacity and exact per-round job flags, and the kernel checks scoped admission, the optimum certificate, the singleton selection, reordered-catalogue agreement, and witness extraction; cross-configuration reuse is concretely rejected.

### Headline theorems and checked facts
- All scoped admitted: every plan in the catalogue passes scoped qualification against its constructed policy and receipts.
- Scoped optimal certificate: the certificate for the two-worker plan over the catalogue, under the scoped policies and receipts, on the single axis, is true.
- Scoped selection: the final all-ties entry point on the catalogue returns exactly the singleton list with the two-worker plan.
- Scoped selection reordered: the same entry point on the reordered catalogue (reversed, one-worker, two-worker) returns the same singleton list.
- Selected obligations have witnesses: every obligation of the two-worker plan's policy has a matching witness receipt in its receipt list, with matching scope and round, passing flag, and an in-limit measured value — obtained through the certified scoped optimum theorem of module 11.
- Reused round rejected: remapping all of the two-worker plan's receipts to round zero makes qualification false.
- Foreign configuration rejected: presenting the reversed plan's receipts against the two-worker plan's policy (its configuration) makes qualification false.

### Axiom dependencies
- EMPTY axiom lists: all scoped admitted, scoped optimal certificate, scoped selection, scoped selection reordered, reused round rejected, foreign configuration rejected.
- Selected obligations have witnesses: propositional extensionality and quotient soundness.

### Explicit non-claims and boundaries
- Identifier nature: "Its policy ID is the imported policy digest represented as a natural number; the other scope IDs identify the pinned campaign fixture." (readme) In the file: the policy identifier is the imported policy hash interpreted as a natural number, and the other identifiers "name the one pinned campaign fixture, not extra observations."
- Selected-evidence checker, not transport — verbatim in substance from the readme: "This is a selected-evidence checker, not the raw append-only transport layer. Identical duplicate delivery must be deduplicated by receipt identity before constructing its selected evidence set."
- Authenticity and liveness not claimed: "Policy digest authenticity, digest-to-content binding and current authorization/liveness still require trusted or separately checked ingestion. For example, changing a cap while reusing the same opaque policy identifier is not detected solely by identifier equality; the ingestion bridge must validate the committed policy bytes. No cryptographic correctness or live-policy lookup theorem is claimed here." (readme)

---

## 13. MetricRelevance — exact nonaggregated relevance profiles

### Purpose in plain English
Exact relevance profiles that keep separate per-intent-part coordinates — direct contrast, composed-result change, admissible indirect mutation sensitivity, and observed outcome variability — assembled without inventing weights or a scalar quality score, with exact unreduced fractions and scope-disciplined denominators.

### Headline theorems
- Direct exactness (`direct` in substance): the direct-relevance Boolean is true if and only if the metric is among the named metrics, only that metric may change among the named metric coordinates, that metric does change, and the chosen intent part changes. In the readme's words it "identifies single-metric contrasts in the supplied deterministic model: only that metric may change among the named metric coordinates, and the chosen intent part changes."
- Composition irreducibility: if the composition Boolean holds for a group (at least two distinct named metrics, a changed chosen part under the group change, only group coordinates changing), then for every proper subgroup and every alternative state in the named states, a subgroup-only change from the before state to that alternative does not change the chosen part. The check is "a finite search over proper subgroups and states" (file comment).
- Helper exactness in the file: the only-chosen-changed predicate is exact against its pointwise statement, and the admitted-sensitivity predicate is exact: same scope, same context, mutation admitted, and values differ.
- Exact rate specification (`exactRate` in substance): when the rate function returns a fraction, its numerator is exactly the count of true events, its denominator is exactly the event-list length, the denominator is positive, and the numerator is at most the denominator. Fractions are "exact unreduced natural numerator/positive-denominator pairs, not floating estimates" (readme); empty evidence returns no value, not zero.
- Indirect rate specification: the denominator is restricted to admitted mutation records in the requested comparison scope and matched context, with unique comparison identities; the returned fraction counts exactly the value-changing admitted records over exactly the admitted count, with positive denominator and numerator bound. "Confounded/unadmitted rows do not dilute the denominator, other scopes do not leak into it, and duplicate identities reject." (readme)
- Observed failure rate specification: the same exact-count, positive-denominator, numerator-bound discipline for the scope-filtered observations, with duplicate observation identities rejected (the function returns no value).
- Permutation invariance: the exact rate is invariant under permutation of the event list, and the observed failure rate is invariant under permutation of the observation list; scoped failure counts are "proved permutation invariant" (readme).
- Rational equality exactness: the fraction-equality Boolean is true if and only if both denominators are positive and cross-multiplication agrees; zero denominators are rejected.
- Profile assembly: the profile builder assembles the separate coordinates; model-pair catalogues are "deduplicated and filtered by an explicit per-part admissibility predicate before computing denominators" (readme).
- Synthetic fixtures, all kernel-checked and all with EMPTY axiom lists unless noted below: for the intent "(latency at most 10 AND correct) OR fallback" over four named contexts, direct latency-clause change is 4 of 4 for the 8-to-12 change, but composed-root pivotality is 1 of 4. A shared-dependency factorization — (m AND a) OR (m AND b) equals m AND (a OR b) — is proved for all Boolean cases, and changing the shared factor changes the root in 3 of 4 named contexts, "without double-counting its two syntax occurrences" (readme). A separately named admitted mutation catalogue yields 1 of 2. Five same-scope observations yield failure 2 of 5 and unordered-pair disagreement 6 of 10. The full fixture profile equals exactly those separate coordinates. Further fixture theorems cover a direct contrast and a composition in a four-state two-metric model, mixed outcomes present, missing scope returning no value, duplicate identities rejected, a controlled sensitivity accepted, and a confounded sensitivity rejected.

### Axiom dependencies
- EMPTY axiom lists: shared factorization, shared-dependency pivotal rate, fixture disagreement, fixture profile exactness, fixture indirect rate, direct leaf rate, composed root pivotal rate, fixture direct, fixture composition, fixture failure rate, fixture controlled, fixture confounded rejected.
- Propositional extensionality only: fraction equality exactness, observed failure rate specification, admitted sensitivity exactness, exact rate specification.
- Propositional extensionality and quotient soundness: indirect rate specification, exact rate permutation, observed failure rate permutation, direct exactness, composition irreducibility.
- None printed uses classical choice.

### Explicit non-claims and boundaries
- Nonaggregated stance, verbatim in substance: a profile "retains separate per-intent-part coordinates" and is assembled "without inventing weights or a scalar quality score" (readme); the file header for the profile structure: "Keep every intent part and attribution coordinate separate. No scalar weighting."
- Model-relative claims: direct and composition results "are claims about the named model/functions, not proofs that every relevant real-world variable has been modeled or that hidden physical causes are absent." (readme)
- Attribution is not physical control: "Context matching is recorded comparison attribution, not proof that all physical nuisance variables were controlled." (readme)
- Synthetic only: "All new examples are synthetic, distinct from the foreign-code campaign." (readme) The fixture sampling measure boundary: "Counting each named context once is the fixture sampling measure, not an imposed user preference weight." (readme)
- Not statistics: the retained figures "are not population probabilities, weighted utility or a causal-effect estimate." (readme) Denominators and attribution types are retained separately.
- Identity roles distinguished: "Observation IDs identify repeats, whereas deduplicated model pairs identify model edges, not additional independent trials." (readme) Mixed labels are no-value "for absent/conflicting evidence" (readme); empty evidence returns no value, not zero (file comment on the fraction type).
- Not claimed, verbatim in substance: "No generic permutation theorem for pair-disagreement enumeration, normalization theorem for reduced rationals, or general statistical uncertainty theorem is claimed." (readme)

---

## 14. HypergraphIncremental — hypergraph-derived incremental qualification and interaction views

### Purpose in plain English
A single authoritative directed hypergraph from which dependency, incidence, and interaction views are derived; exact semantic incremental recomputation under root and topology changes, proved equal to full recomputation and to the existing executable exhaustive closure; typed matrix cells counting supporting live records; and deterministic frontier projection, including resurrection of a candidate when its dominator is withdrawn.

### Headline theorems
- Interaction is derived: the interaction predicate (co-participation retaining the actual hyperedge and both directed port roles) is exactly the conjunction of the two incidence statements. Incidence retains premise position versus head.
- Unaffected exactness: if an atom is not in the affected region, it is derivable from the old hypergraph if and only if it is derivable from the new one. The underlying lemma re-derives an unaffected old derivation in the new hypergraph.
- Incremental exactness (`incremental` in substance): the incremental construction — reuse unaffected old derivations as roots, and rebuild affected derivations from new roots using only new rules whose heads are affected — derives exactly the atoms derivable by full recomputation from the new hypergraph. Affected closure includes changed root membership, changed edge membership (including empty-premise edges), and dependencies from both old and new hypergraphs (scope note).
- Agreement with the executable closure: the incremental answer for a hypergraph built from admitted finite lists agrees with the existing executable exhaustive closure of module 2, under the same boundedness hypotheses (roots and rule heads in the universe).
- Retracted cycles do not bootstrap: if the new hypergraph has no roots and every rule has at least one premise, the incremental construction derives nothing — "unsupported cycles cannot bootstrap after withdrawal" (readme).
- Patched interaction exactness: the patched interaction view (old view where the edge row is unchanged, new view otherwise) equals the new interaction view exactly, including role and position.
- Patched dominance exactness (auxiliary lemma in the file): the patched dominance predicate equals dominance computed from the new profiles.
- Incremental frontier exactness: the executable pair-update frontier (using patched dominance) equals fresh frontier computation from the new profiles; "withdrawn dominators resurrect retained candidates" (scope note) — the file's examples show the frontier before as only the cheaper candidate, and the incremental frontier after its dominator's eligibility is withdrawn as only the previously dominated candidate.
- Qualified frontier exactness: any deterministic profile projection of the incremental qualification gives the same frontier as projecting the full (new) answer — "Deterministic qualification/profile projection preserves the full frontier result, including resurrection after withdrawal of a dominator." (readme)
- Matrix update exactness: the retained-plus-added support count for a typed cell (counting live records by edge kind and both port roles and positions) equals complete regeneration of the cell count over the edited record list; the Boolean cell version (count greater than zero) is likewise exact.
- Record-derived relation: the semantic edge relation is derived existentially from currently live, kind-admitted records, and is exact by definition; the file's examples show an implication surviving withdrawal of one of two supporting records and disappearing when both are withdrawn.
- Joint premises remain conjunctive: the file's control shows a two-premise edge whose second premise is underivable does not derive its head — "incidence alone is not inference" (file comment).

### Axiom dependencies
- Propositional extensionality only: matrix update exactness, matrix Boolean update exactness.
- Propositional extensionality and quotient soundness: incremental frontier exactness.
- All three standard axioms: agreement with the executable closure, qualified frontier exactness, unaffected exactness, incremental exactness, retracted cycles do not bootstrap, patched interaction exactness.
- None printed is empty.

### Explicit non-claims and boundaries
From the readme, verbatim in substance: "This is a semantic refinement theorem, not a fast executable worklist or sparse-matrix performance proof. The raw record list counts multiplicity. Unique receipt identity, deduplication, scoped admission and withdrawal precedence must be enforced before the live snapshot is supplied. The same-ID remove-and-add operation permits reintroduction; it is not a permanent tombstone protocol." (The readme uses the hyphenated identifier form for the same-identity operation; rendered here in plain words.)
From the hypergraph scope note, "Not claimed" section, verbatim in substance:
- "No deployed ingestion, cryptographic authenticity checker, withdrawal authorization mechanism, or production incremental worklist is verified by this module."
- The hypergraph and affected definitions "are proposition-level semantics. The exact closure theorem is not a performance bound. The affected region may include all atoms."
- "Matrix update theorem recomputes support counts on retained records; it does not establish an optimized sparse-matrix cache implementation or complexity bound."
- "Pair update computes the old dominance predicate when descriptors are unchanged; it is not a verified mutable cache/count data structure."
- "Profile projection is supplied deterministically; the theorem does not validate how timings are measured, sampled, or predicted."
- "Receipt IDs are exact [natural-number] keys in this model. Unique assignment, scoped identity encoding, hash collision resistance, and construction of admitted edge kinds remain adapter obligations. The semantic relation intentionally collapses duplicate implications only AFTER live receipt selection."
- "The relation has positive conjunctive inference. Nonmonotone qualification decisions can be deterministic projections AFTER closure; arbitrary recursive negation is not included."
- Cell counting "counts list-record multiplicity, not distinct witness identities. A canonical authoritative receipt set must be deduplicated/admission-normalized before this view if unique-witness counts are intended." The edit operation "is the ordered operation remove-selected-old-records then append-added-records: it does not itself enforce ID freshness, withdrawal precedence, or an idempotent ledger join. Those are upstream live-snapshot admission obligations. Duplicate implication examples use DISTINCT receipt IDs."
Also from the scope note's proven section, the limiting clause on agreement: the semantic incremental answer agrees with the executable exhaustive closure "for admitted finite lists. This is not an implementation of a fast incremental worklist." And: "Binary dependencies are a derived invalidation view; premise conjunction remains the inference rule."

---

## Proof-design document: independently checked versus proposed

Source: the proof-design document in docs. Its own framing, verbatim in substance: "This document distinguishes independently checked v9 results from proposed extensions. All twelve v9 Lean modules were independently replayed successfully. Proposed theorems below are not claimed as checked." Note the count: the v9 set is twelve modules; the clone at this head has fourteen root modules, the metric-relevance and hypergraph modules having been added in the two later commits at the top of the log.

### What the document calls independently checked

- Checked in the earlier version it calls v7 (its section 9): rooted closure and compounding; exact executable closure under checked bounds; Boolean profile enumeration; nondominated filtering; fixed schedule-model enumeration and feasibility; admission-before-ranking; concrete foreign model and measured-catalogue frontier arithmetic. In module terms: modules 1–8 above, as characterized in their entries.
- Independently machine-checked in v9 (its section 9): the scoped evidence module validates typed scope, unique obligations and receipt identities, exact required count, per-round matching, observed-pass and timing gates; the scoped selection module directly gates eligible optimum selection through that checker; the scoped campaign module instantiates the actual pilot and, in the document's words, tests missing and failed chosen evidence with fallback to the reversed plan; the linear selection module proves scalar argmin and exactly n minus 1 scalar comparisons for nonempty input — with the document's own caveat that this "is not a total-runtime bound" — and the all-ties function returns all scalar minima with membership permutation invariance, while "serialization order and duplicate multiplicity are retained. Canonical serialization needs a separate normalization step."
- The document's summary of the v9 bridge: "The v9 bridge closes the modeled scoped-qualification-to-selection gap."
- The document also treats as already available (section 3): the exact compounding identity of module 1, withdrawal by filtering live roots and authorized premise-valid rules with least rooted closure, and the exhaustive frontier filter of module 4 as "an excellent reference oracle."
- External obligations the document states even for the checked results: "Exact ID comparison does not authenticate the referenced policy or receipt bytes. Policy authorization, liveness, raw-observation ingestion, compatible cross-policy cost definitions and semantic truth of imported pass bits remain external obligations. Repeated transport duplicates must be normalized upstream when ledger idempotence is desired; the selected-receipt checker rejects duplicate IDs."
- What the foreign experiments establish, per the document (section 7): the three-plan pilot across the pinned suites with three observed rounds; all three meet the declared paired whole-suite timing caps and observed identity and outcome checks; on the sole axis, maximum observed suite wall time, the checked catalogue frontier is the two-worker plan alone, with the three maxima as in module 8. "It does not demonstrate source-rewrite certification yet. Whole-suite acceleration also does not establish per-job timing preservation: 8 of 12 [two-worker] subprocess durations increased relative to [the one-worker plan]. The scope must remain exactly whole-suite timing unless a new per-job invariant is actually measured and admitted."

### Proposed extensions — not checked

The document's standing disclaimer applies to every item below: proposed theorems "are not claimed as checked."

#### P1. The linked-certificate principal theorem
- Statement in plain English (document section 1): replace one large optimality claim with a linked certificate. A qualification and optimization instance has an immutable identity built from artifact and configuration roots, intent, policy, observation snapshot, venue model, candidate generator, equivalence rules, and objective definitions. The result is a chain — instance identity, then evidence admission, then behavior-preserving alternatives, then legal schedules, then costs, then frontier, then selected plan — where each arrow has its own checker and receipt. The principal theorem should have this shape: for a fixed instance identity, if the checker accepts a candidate with its certificate, then (1) the candidate meets every required qualification and hard timing constraint; (2) its behavior-preservation evidence is valid for precisely that instance's scope; (3) it is feasible under that instance's dependencies, venues, and interference constraints; and (4) no admitted candidate in the declared alternative space strictly dominates it on the declared axes.
- What is unproven about it, exactly: the document presents this as the shape the principal theorem "should have"; it is listed among the proposed extensions that are "not claimed as checked." No single checked theorem in the fourteen modules links all the arrows into this one acceptance-implies-all-four-conclusions statement for a fixed instance identity; the checked modules prove the separate links (admission, scoped qualification, feasibility in the schedule model, frontier and optimum certificates) without the unifying principal theorem, and without the document's requirement that source identity, empirical result, semantic equivalence, and authorization remain distinct types sharing one graph and aggregate root.

#### P2. The coverage-certificate upgrade
- Statement in plain English (document sections 1 and 5): an additional coverage certificate upgrades a supplied-catalogue frontier to the complete frontier of the declared generator. "Optimization coverage concerns alternatives, not exhaustive program behavior." In certificate terms: frontier completeness means coverage of admitted alternatives, nondomination of retained entries, and a retained dominator for every omitted admitted alternative; a generator-optimum certificate means exhaustive coverage or certified branch pruning, with each omitted region carrying a sound objective lower bound showing it cannot dominate the selected candidate.
- What is unproven about it, exactly: no checked coverage certificate, generator-optimum certificate, or frontier-completeness theorem appears in the modules. The checked results are catalogue-relative: module 4's frontier is relative to the supplied list, module 5's certified optimality is complete only over its own enumerated schedule model, module 6 expressly does not establish completeness of its separate queue-list generator, and the readme for module 5 states completeness of an externally generated candidate list "must be established separately." The document's next-proof-additions list begins with "General multi-axis frontier coverage and a certified pruning interface" as not yet checked, and its pruning discipline is stated as a requirement, not a result: a bound used for pruning "must be an actual bound in the named model. A learned estimate can prioritize search but cannot justify dropping a region."

#### P3. Typed transfer edges
- Statement in plain English (document section 2, derivation and transfer layer): typed hyperedges carry a premise set, a conclusion, a rule or checker identity, and a scope. Cross-lineage reuse is automatic when a checked transfer is applicable; lineage alone neither grants nor forbids reuse. A transfer must preserve the qualifications actually claimed, including relevant environment, effect, and harness assumptions. The same retained evidence can support several claims; reusing evidence does not multiply independent empirical samples or authorize consuming a stateful resource twice.
- What is unproven about it, exactly: the checked modules contain no typed-transfer theorem and no automatic cross-lineage reuse. Module 9's boundary is the opposite default: cross-lineage reuse "requires an explicit independently checked transfer; this checker never infers it from shared content alone," and module 1's soundness is conditional on rules being valid, with validation an explicit input obligation. The document frames typed edges and automatic applicable-transfer reuse as part of the proposed design (the three-layer evidence design of section 2), not among the v7 or v9 checked lists in its section 9.

#### P4. The product decomposition theorem
- Statement in plain English (document section 4): let feasible joint alternatives be the Cartesian product of local alternative sets. Suppose joint objective aggregation is coordinatewise monotone in every local objective vector, and every cross-component constraint has already been accounted for. Then removing a locally dominated alternative cannot remove every representative of a globally nondominated objective vector. Reason given: replace a dominated local choice by a no-worse one while holding all other choices fixed; feasibility is preserved by the product assumption, monotonic aggregation preserves no-worse joint costs, and repeating the replacement obtains a joint alternative from the product of local frontiers.
- What is unproven about it, exactly: the document introduces it with "propose the following reusable decomposition theorem" and lists "Separable composition of local objective-frontier representatives with coupling interfaces" among the next proof additions that are "not yet checked." No module contains this theorem. The document itself fences it: "Do NOT claim every product of local-frontier members is globally nondominated: global comparison is still required. Non-strict aggregation can collapse a local strict improvement to a tie, so preserve representatives and distinguish vector coverage from identity coverage." And: "If venues, setup state, queues or effects couple components, carry their interface state into the decomposition or solve the coupled block jointly. This is the exact criterion that makes decomposition a theorem rather than an optimization guess." The same section's behavioral-composition half is also unproved as a general theorem: behavioral composition requires a compatibility judgment, and an invalid composition (the document's two-passing-operations-on-one-balance example) "is rejected before ranking" only under admitted compatibility cases such as disjoint effects, explicitly threaded state, or a checked joint pre- and postcondition — none of which is a checked theorem in the modules.

#### P5. Certificate forms
- Statement in plain English (document section 5): production search need not reproduce the exhaustive reference filter literally, provided its outputs pass cheaper checked certificates of these proposed forms — (a) feasible improvement: candidate admission plus a checked strict-dominance vector against the baseline; (b) catalogue optimum: admission plus checked comparisons against each admitted catalogue member; (c) generator optimum: exhaustive coverage or certified branch pruning with a sound lower bound per omitted region (see P2); (d) frontier completeness: coverage, nondomination of retained entries, and a retained dominator for every omitted admitted alternative (see P2). The section adds a proposed useful theorem: for a finite strict Pareto order, a fully computed frontier dominates every excluded candidate through a descending chain ending at a frontier member, producing concise exclusion explanations.
- What is unproven about it, exactly: the forms are introduced as "Proposed certificate forms," and the descending-chain statement as "a useful additional theorem" — neither is in the checked lists. What is checked today is narrower: module 5 has a finite-list certificate checker and an enumerated-model optimum, module 7 has an admitted-catalogue optimum certificate, and module 11 connects that certificate to scoped witnesses; there is no checked generic certificate-form framework, no checked pruning interface, and no checked descending-chain exclusion theorem. The section's own closing direction is prospective: "Use a verified worklist as a refinement of the current closure specification; keep the exponential reference as a small-case differential oracle" — and the next-proof-additions list includes "Performant worklist refinement of closure, including deletion/recomputation semantics" and "Canonical serialized output refinement and authenticated import-to-model binding" as not yet checked.

#### Also proposed or prospective in the document, for completeness
- Next engineering additions (not proof claims): a canonical receipt importer with schema and version, policy and source hashes, and exact per-test requirements where the policy calls for them; durable raw traces and an independently reproducible import-to-model manifest; broader foreign campaigns with unchanged declared axes and hard invariants, reporting rejected alternatives as such; and one actual certified source rewrite, only after its preservation adapter exists. The document's closing judgment: "The strongest next engineering deliverable is a replayable authenticated raw-observation-to-model importer; modeled pass bits remain supplied evidence, not kernel-authenticated physical facts."
- Empirical discipline stated as design, not theorem (section 6): the three test families (admitted counterfactual, gate mutation, checker differential) are a proposed testing discipline; "Do not confuse an empirical counterfactual comparison with a causal effect estimate. If causal attribution is wanted, preregister the compared factor and balance/randomize nuisance order. Optimality of the recorded admissible catalogue does not itself require a causal attribution claim."
- Generality framing (section 8): source rewriting is "an extension at the preservation boundary, not a prerequisite"; a language-specific equivalence or translation-validation certificate is to be added "only when such alternatives are proposed." A deterministic display total order "must not be confused with Pareto dominance."

---

## Cross-cutting strongest results, for orientation

- The only module whose every printed theorem is axiom-free is module 1; its compounding identity and least-closure semantics are the load-bearing core for modules 2 and 14.
- The strongest executable bridge is module 2's exact refinement under explicit boundedness, paired with its fail-closed checked face and proved rejection condition.
- The strongest end-to-end concrete chain is modules 9, 11, and 12: scoped qualification with witness extraction, a certified scoped optimum that yields witnesses for every obligation of the winner, and a concrete pilot where admission, the optimum certificate, and the singleton selection are all proved with empty axiom lists (witness extraction itself uses the two standard axioms).
- The strongest incremental result is module 14's incremental exactness: reuse of unaffected derivations plus affected-only rebuilding equals full recomputation, for cyclic hypergraphs as well, and agrees with the exhaustive executable closure on admitted finite lists — as a semantic theorem only, with no performance claim.
