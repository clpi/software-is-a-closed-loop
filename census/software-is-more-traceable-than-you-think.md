# Census — software-is-more-traceable-than-you-think

Sweep re-census at the landed head. It supersedes the first census of
this repo, taken at pin 4420fb1e before the proof landed: that census
recorded the thesis as not landed, with only the invoice example in
tree. Between 4420fb1e and the current head the repo gained its
witness-store hypergraph, its grain map, its Lean proof of platform
independence with adversarial controls, and the range-ledger
bridge-repair example.

## Pin and identity

- Live head (local clone, branch master, in sync with origin/master): `8f6a128069d0e68e97c4a69d78689c84350b0d2f`
- Visibility: private; default branch master. Archive description: the historical witness hypergraph of software at symbol grain — exact time, order independent, with a Lean proof that it holds independent of operating system, software, and language.
- Toolchain pin: `proof/lean-toolchain` = `leanprover/lean4:v4.19.0`. The examples carry no toolchain file; their recorded transcripts also say Lean 4.19.0.
- Files at the pin: README.md; `hypergraph/` (build.py, REPORT.md, hypergraph.json — the 10.9 MB built hypergraph over the frozen snapshot); `returns/` (extract.py, GRAINMAP.md, results.json); `proof/` (Traceability.lean, Controls.lean, check.sh, CHECK.log, REPORT.md, platform-audit.py, PLATFORM-AUDIT.log, lean-toolchain); `examples/` (InvoiceTrace.lean, check.sh, README.md, verification.txt, range-ledger/ with BridgeRepair.lean, check.sh, mutation.patch, README.md, verification.txt). Four Lean files, 726 lines total. A sibling-repo division of labor is stated in the README: this repo proves the witness-stream level and platform independence; the fold at the accounting level lives in software-is-quantifiable, the incremental hypergraph semantics in software-optimality.
- This census read all four Lean files in full. No file is UNREAD.

## The thesis, one sentence

Every execution appends witnesses to an append-only ledger, the accounting is a pure fold, so the historical witness hypergraph is a function of the witness set alone — independent of arrival order and of time, at symbol grain refined to the derivation step where a provable return needs it — and a return is provable when the exact premise set of any witnessed outcome is derivable from the hypergraph alone, the construction holding independent of operating system, software, and language.

## The two evidence lanes

The repo's claim splits into an executed lane and a proven lane, and
the README says plainly which is which.

- Executed, not proven: the hypergraph establishment over the frozen witness store (2,509 witnesses, 8,482 recorded join edges in; 20,480 nodes, 9,356 hyperedges out; construction run four times with byte-identical output including a shuffled and a duplicated feed; 719 classes re-derived from the hypergraph alone, identical) and the grain map (1,526 accounting entries: 1,522 provable returns at symbol grain, 4 at derivation-step grain, none failing). These are verified by running Python over a snapshot; nothing in the Lean imports or touches the store. The README also concedes the store's records carry no timestamp field: exact time in this store is the batch and its step index.
- Proven: the witness-stream level — order independence, duplication independence, time independence, retraction exactness, and what the fold does and does not lose, quantified over arbitrary node, event, and time types and an arbitrary lifting; plus the invoice and range-ledger examples as checked worked instances. All 43 named theorems are listed below.

## Theorem census — 43 theorems, zero lemmas, four files

Strength columns: what each theorem concludes, what it assumes, and
whether any premise does the conclusion's work. A premise that
restates the conclusion is labeled PREMISE, per the family's
quantifiable claim-5 precedent. Axioms are as recorded in the repo's
committed gate log.

### proof/Traceability.lean — 20 theorems (the main construction)

Model: `Derivation Node` = a premise characteristic function plus a head, so a hyperedge carries its full premise set; `Graph Node` = node and derivation characteristic functions; `fold lift` = pointwise `join` over the stream under an arbitrary contribution assignment `lift : Ev → Graph Node`; `foldtimed` folds through the underlying events only, never reading time components.

| Theorem | Statement (one line) | Concludes / assumes / premise audit |
|---|---|---|
| bool_eq_of_agree | `(a = true ↔ b = true) → a = b` | Lemma-tool; assumes only the agreement. |
| graph_ext | pointwise node and edge agreement → `g = h` | Extensionality; no premises beyond the agreements. |
| join_assoc | `join (join a b) c = join a (join b c)` | Pure algebra; no premises. [Quot.sound] |
| join_comm | `join a b = join b a` | Pure algebra; no premises. [Quot.sound] |
| join_idem | `join a a = a` | Pure algebra; no premises. [Quot.sound] |
| join_empty_left | `join empty a = a` | Identity law; no premises. |
| join_empty_right | `join a empty = a` | Identity law; no premises. |
| fold_append | `fold lift (l₁ ++ l₂) = join (fold lift l₁) (fold lift l₂)` | Partition-recompute agreement; no premises. [propext, Quot.sound] |
| fold_nodes | node in fold ↔ some event of the stream contributes it | Losslessness, node face; no premises (quantified over arbitrary lift). [propext] |
| fold_edges | derivation in fold ↔ some event of the stream contributes it, premise set read off exactly as recorded | Losslessness, derivation face — the load-bearing theorem for premise-set recovery; no premises. [propext] |
| returns_head | `(fold lift l).nodes d.head = true → (∃ e, e ∈ l ∧ (lift e).edges d = true) → (fold lift l).edges d = true` | Concludes: a contributed derivation whose head is witnessed is present. Assumes: **PREMISE** — `contributed` restates the conclusion (presence of a contributed derivation is exactly fold_edges), and the proof is one line, `(fold_edges lift).mpr contributed`; the `_witnessed` hypothesis is not even read by the term. The "provable return" of a witnessed outcome is thus a corollary of losslessness, not an independent result. [propext] |
| fold_ext | `(∀ e, e ∈ l₁ ↔ e ∈ l₂) → fold lift l₁ = fold lift l₂` | **Order independence**: same membership (weaker than permutation) → equal hypergraphs; hypothesis is the intended grain. [propext, Quot.sound] |
| fold_perm | `l₁.Perm l₂ → fold lift l₁ = fold lift l₂` | Permutation independence; corollary of fold_ext. [propext, Quot.sound] |
| fold_append_self | `fold lift (l ++ l) = fold lift l` | Duplication independence; corollary. [propext, Quot.sound] |
| foldtimed_ext | timed streams with same underlying membership → equal timed folds | **Time independence, membership form**; time components never read. [propext, Quot.sound] |
| map_event | `(es.map fun e => Timed.mk e (t e)).map Timed.event = es` | Retraction identity; no premises. |
| foldtimed_retime | reassigning every time component (`f` vs `g`) leaves the fold unchanged | **Time independence, reassignment form**; no premises. [propext] |
| retract_nodes | node in filtered fold ↔ some surviving event contributes it | Retraction exactness, node face; no premises. [propext] |
| retract_edges | derivation in filtered fold ↔ some surviving event contributes it | Retraction exactness, derivation face; no premises. [propext] |
| retract_eq | `(∀ e, e ∈ s ↔ e ∈ l ∧ keep e = true) → fold lift (l.filter keep) = fold lift s` | Observables after retraction equal recomputation from survivors; hypothesis `h` defines `s` to be the survivor set, which is the theorem's meaning. [propext, Quot.sound] |

Independence reading: the theorems quantify over arbitrary `Node`,
`Ev`, `Time` and an arbitrary `lift`; no platform, language, OS or
mechanism is named in the proof terms (mechanically audited, see
hygiene below). The independence is real but thin: `lift` is
uninterpreted, so the theorems say the accounting is environment-free
*given* whatever the lifting records — not that real executions
produce informative witnesses.

### proof/Controls.lean — 12 theorems (adversarial controls, standing counterexamples)

Each weakens one axis of the construction and proves the weakened
claim false on kernel-checked concrete data; each `*_claim_fails`
theorem is a negation with a concrete witness.

| Theorem | Statement (one line) | Concludes / assumes / premise audit |
|---|---|---|
| count_once | `countfold [0] 0 = 1` | Control fixture; no premises. Kernel decide. |
| count_twice | `countfold ([0] ++ [0]) 0 = 2` | Control fixture; no premises. Kernel decide. |
| count_claim_fails | `¬∀ l, countfold (l ++ l) = countfold l` | **Duplication independence kills the counting join** (adds counts instead of union); counterexample `[0]`. Axiom-free. |
| swap_same_set | `x ∈ [0,1] ↔ x ∈ [1,0]` | Order-control fixture; premise for first_claim_fails. [propext] |
| first_claim_fails | `¬∀ l₁ l₂, same membership → firstfold ownlift l₁ = firstfold ownlift l₂` | **Order independence kills the first-event fold**; witnesses `[0,1]` vs `[1,0]`. [propext] |
| prem_differ | `fullprem ≠ noprem` | Grain-control fixture: same head, different premise sets. [propext] |
| grain_absent | `(fold grainlift [0]).edges noprem = false` | At exact grain the premise-less derivation is absent. [propext] |
| grain_coarse_present | `∃ d', present ∧ shares head with noprem` | At coarse (head) grain the same derivation reads present. [propext] |
| grain_claim_fails | `¬∀ d, (coarse presence) → exact presence` | **Symbol grain is necessary**: head-grain presence gives the wrong premise set; standing counterexample in-tree. [propext] |
| residue_survivor_absent | surviving fold lacks node 0 | Retraction-control fixture. [propext] |
| residue_present | residuefold has node 0 present | Retracted event leaves residue in the weakened variant. [propext] |
| residue_claim_fails | `residuefold ownlift keep [0,1] ≠ fold ownlift ([0,1].filter keep)` | **Retraction exactness kills the residue fold**; standing counterexample. [propext] |

### examples/InvoiceTrace.lean — 5 theorems (worked example: premise extraction from a fixed journal)

| Theorem | Statement (one line) | Concludes / assumes / premise audit |
|---|---|---|
| extraction_exact | `e ∈ evidence r events ↔ e ∈ events ∧ e ∈ needs r` | Extraction is exact filter; no premises. [propext, Quot.sound] |
| preserves_verdict | `supported r (evidence r events) = supported r events` | Evidence subset preserves the support verdict; no premises. [propext, Quot.sound] |
| least_support | `supported r alt = true → ∀ e ∈ evidence r journal, e ∈ alt` | Any alternative supporting list carries the extracted evidence; `ok` is load-bearing but legitimate (it is the meaning of "supports"). [propext, Quot.sound] |
| before_after | `journal.length = 8 ∧ evidence overridePath journal = [override,signature] ∧ evidence pricingPath journal = [quote,tax,currency]` | Checked before-and-after fixture. Axiom-free (kernel decide). |
| route_is_needed | `¬∃ f : Bool → List Event, ∀ r, f (supported r journal) = needs r` | **A route-free receipt cannot recover its premises** — the traceability of the example is necessary, not incidental. Axiom-free. |

### examples/range-ledger/BridgeRepair.lean — 6 theorems (restore tracing across disconnected telemetry islands)

Model: four ledger positions with independent unknown potential
offsets; wires observe pairwise differences; `blind ws` searches the
16 masks for a nontrivial potential making every observed wire read
zero.

| Theorem | Statement (one line) | Concludes / assumes / premise audit |
|---|---|---|
| returned_cut | `blind ws = some m → 0 < m ∧ m < 15 ∧ ∀ w ∈ ws, value (bit m) w = 0` | A returned cut is a genuine nontrivial cut; `found` does the work by hypothesis (it is the search's own output). [propext, Quot.sound] |
| cut_distinguishes | `0 < m.val ∧ m.val < 15 → ∃ i j, bit m i ≠ bit m j` | Every nontrivial cut separates positions. Kernel decide over the 16 masks. [propext, Quot.sound] |
| two_never_enough | `ws.length ≤ 2 → (blind ws).isSome = true` | Two wires never pin the offsets. [propext] |
| ambiguity | `ws.length ≤ 2 → ∃ p, (∀ w ∈ ws, value p w = 0) ∧ ∃ i j, p i ≠ p j` | **Disconnected telemetry leaves exact positions unrecoverable**; disjunction of the two above. [propext, Quot.sound] |
| three_suffice | `recover (value p ab) (value p bc) (value p cd) i = p i - p 0` | A spanning bridge chain restores every position exactly up to the global offset. [propext, Quot.sound] |
| bad_three | `(blind [ab,ac,bc]).isSome = true ∧ blind [ab,bc,cd] = none` | Not all three-wire sets work: the wrong middle bridge fails the decoder; checked against the must-fail mutation patch in-tree. Kernel decide. [propext] |

## Hygiene verdict — zero of each, with receipts

- **Zero `sorry`**: this census's word-boundary grep over all four Lean files: no hit. The committed `proof/CHECK.log` (`grep -Eq 'sorryAx|error:|warning:'` gate) contains none.
- **Zero custom axioms**: no `axiom` declaration in any file (the only `axiom` tokens are `#print axioms` audit commands). The gate's axiom-subset check receipt, quoted: `Axiom subset check passed: printed axioms are a subset of {propext, Classical.choice, Quot.sound}` / `Axioms printed: Quot.sound propext`. Across all 43 theorems the printed axioms are only `propext` and `Quot.sound`; the twelve control theorems include three axiom-free ones; `count_claim_fails` is axiom-free. Example files' transcripts print the same shape (`propext`, `Quot.sound`, or none).
- **Zero escapes**: no `native_decide`, no `implemented_by`, no `extern`, no `unsafe`, no `admit`, no `@and_all`-style attribute escapes in any of the four files (this census's scan plus the proof gate's own token scan). The `decide` occurrences (`before_after`, the control fixtures, `cut_distinguishes` over the 16 masks, `bad_three`) are kernel `decide`, not `native_decide` — allowed.
- **Mechanical platform audit**: `proof/platform-audit.py` + `PLATFORM-AUDIT.log` — 52 platform words (linux, windows, posix, java, rust, compiler…) scanned against every `#check`-printed statement, receipt: `Hits: 0` / `Platform audit: PASS`.
- PREMISE-labeled items: one, `returns_head`'s `contributed` (the hypothesis *is* fold_edges; the witnessed-head hypothesis is dead). Every other load-bearing hypothesis (`fold_ext` membership, `retract_eq` survivor-set definition, `least_support`'s `ok`, `returned_cut`'s `found`) is the theorem's intended grain, not a smuggled conclusion — recorded here as carried, not as defects.

## Gate verdict

- **Cover exists**: `proof/check.sh` is the widened family gate — escape-token scan, compile with `-DwarningAsError=true`, retry loop over deferred imports, failure on any `sorryAx|error:|warning:` in the log, and an axiom-subset check. **Coverage caveat**: it runs from `proof/`, so its recursive scan and enforcement reach only the two `proof/` files. The two example files are covered by `examples/check.sh` (compiles `InvoiceTrace.lean` with warnings as errors) and `examples/range-ledger/check.sh` (compiles `BridgeRepair.lean` with warnings as errors, then applies `mutation.patch` and asserts the mutated file *fails* to compile — a must-fail control that lands in-tree). Collectively every one of the four Lean files is compiled by some warnings-as-errors gate at the pin; the escape scan and axiom-subset enforcement apply to `proof/` only (this census's own scan closes that gap for the examples, at the cost of not being in the gate).
- **Result at the pin**: by the repo's committed receipts — `proof/CHECK.log`: version line `Lean (version 4.19.0, x86_64-unknown-linux-gnu, commit 6caaee842e94, Release)`, then 16 `Traceability` axiom print-outs, then 12 `Controls` print-outs, then the two closing PASS lines; `examples/verification.txt` and `examples/range-ledger/verification.txt`: same version line, per-theorem axiom lines, and `Rejected control:` lines showing the must-fail controls fired.
- **Receipt finding (minor)**: `examples/verification.txt` ends `Rejected control: omit the signature from an override trace (Lean exit 1).` — but the `examples/check.sh` at this head has no mutation step and no `mutation.patch` for the invoice example exists in tree (only range-ledger's does). That control line is un-reproducible from the tree as gated; either the control step or the receipt predates the current script.
- **Independent re-run**: NOT EXECUTED. No Lean toolchain exists in the census environment and toolchain download is network-blocked, so this census could not re-run the gates itself; the verdict above is the repo's recorded evidence at the pin, not a fresh green. This stands against the family bar's independent re-check requirement and is carried as an open verification-lane item, consistent with the idol-semi precedent (gate recorded green, re-run blocked on the environment).

## Name-overclaim judgment

The name claims: **software's history is more traceable than you think — the exact premise set of any witnessed outcome is recoverable from the fold of the witness stream, independent of platform, order, and time.**

Judgment: **the theorems prove a weaker statement; the name's full claim is proven modulo an unformalized premise and partly by execution.** What is proven at the pin: for an *arbitrary* contribution assignment, the fold of a stream loses nothing on either face (fold_nodes, fold_edges), is a function of the event *set* alone (fold_ext, fold_perm, fold_append_self), ignores time entirely (foldtimed_ext, foldtimed_retime), and survives retraction exactly (retract_nodes, retract_edges, retract_eq) — all platform-free by quantification, with three controls proving each independence non-vacuous against concrete weakened variants, and two worked examples showing traceability necessary and a minimal spanning restore. What the name passes to premise: (a) the lifting premise — the theorems hold for every lift precisely because they say nothing about which lift real executions produce; the "kernel-boundary sensing" story that would connect real executions to the stream is stated, never formalized; (b) the store-level facts — the 2,509-witness snapshot, the four identical construction runs, and the 1,526-entry grain map are verified by running Python, not by the Lean; (c) the acknowledged time gap — the store carries no timestamps, "exact time" is batch-and-step-index, a weaker time than the claim's narrative suggests. So: no dishonest overclaim (the README's evidence states are accurate), but the name's force ("more traceable than you think" about *software*, meaning real systems) is cashed out as an abstract-folk theorem plus executed snapshot evidence plus an open lifting premise.

## Ledger row

pin 8f6a1280 · 4 Lean files (all read, none UNREAD) · 43 theorems (0 lemmas; 20 construction + 12 controls + 5 invoice + 6 bridge-repair) · hygiene 0 sorry / 0 custom axioms / 0 escapes (1 PREMISE: returns_head's `contributed`; environment-free scan 0 hits) · gate green on committed receipts covering all 4 files warnings-as-errors, but independent re-run NOT EXECUTED (no Lean toolchain available) and the examples gate lacks the escape scan/axiom check (1 minor un-reproducible receipt line) · name: weaker statement proven — fold of an arbitrary witness stream is lossless, order/duplication/time-independent, retraction-exact, platform-free by universal quantification; store-level grain map execution-verified not proven; real-execution lifting a stated, unformalized PREMISE.

## Watch delta — 2026-11-21, the eighty-fifth hourly re-synthesis watch

The watch re-read this repo's live head at 2d35b503aa74b2ac2397d9cc6af0c4049c609b4e in the full enumeration and read the whole tree at that head (33 files, not truncated) and at the last recorded head 8f6a128069d0e68e97c4a69d78689c84350b0d2f (24 files). Mechanical count at the fresh head, by the watch method (every theorem or lemma declaration in every Lean file in the tree): 56 declarations across 5 Lean files, no sorry token and no custom axiom declaration in any file. The same method at the last recorded head counted 43 declarations across 4 Lean files. Name comparison, one mechanical method both times: 14 names gained and 1 lost. The count grew, so no proven-count regression is flagged; the one lost name is flagged here as a name loss at delta strength — the premise-carrying head theorem recorded in the ledger row above under the quoted foreign name "returns_head" no longer stands in the tree, and its premise must be re-traced against its replacements in the owed re-census. The movement is two commits deriving return contributors and constraining witnessed-head recovery, merged with standing counterexamples: nine files added — a new return controls Lean file carrying ten declarations, a receipts folder of recorded gate logs, an audit script, and a source hash record — and eight files changed, among them the main proof file, which gained three declarations, the readme, the check script, and the recorded check and audit logs. In plain terms the new results prove the contributor selection sound and order-sensitive, refuse a missing edge, and prove the failure forms — a head without a derivation, a derivation without a head, and that a witnessed head does not select its premises — beside the recorded-edge and recorded-head forms that replace the lost name. The gate evidence at the fresh head is the repo's recorded receipts, read firsthand and not re-run by this watch. The prose placements in this annex stand at the census pin 4420fb1e5422d965668c66f93d9d352cc3cec982; a full re-census at the fresh head is owed and the owed mark in the ledger stands.
