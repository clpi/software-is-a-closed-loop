# Census — software-is-incrementally-safe (clpi) — refresh draft

Census date: 2026-11-18, ~02:10–02:40 PST. Method: live head read first via the gh route, then a shallow clone (depth 1); clone head verified equal to the live head. Clone read only, never edited. This draft replaces the census of the older pin; changes are marked in the Delta section. As instructed, this census is of the **new head's own content**; the former branch is treated only as the merger question below.

## Pins — live head

- Old census head pin: `9466135815aa80e714d2a6999fd0aa8807375ff3` — one file only (the toolchain pin), theorem count 0.
- Live head (default branch `master`): `8ad1dd2624c41023919ab7c41a285de15b3ce673`. Clone head matches exactly. Head commit subject, plainly: add a checked before-and-after example for a policy migration.
- Visibility: private.
- Toolchain pin: Lean 4.19.0 (the repo's toolchain file, carried from the old pin). No lakefile, no manifest, and still **no readme at the head**.
- Files at head: the toolchain file plus one worked-examples folder holding a single standalone proof file, its readme, a runner script, and a recorded verification transcript. Theorem total in tree: **6**, all inside the worked example. Library theorems: **0**.

## Delta (old pin to this pin)

- **The former branch content has NOT merged.** The old census found all proof content on an unmerged branch (86 theorems: 54 in this repo's own five modules, 32 in two stand-in modules). The head tree at this pin is the evidence: it contains no library modules at all — no safety, increment, security, checker, or example module of that development, no lakefile, no package. The pull request carrying that branch is still open at this census. The thesis content therefore remains absent from the head, exactly as at the old pin.
- **What landed at the head is a worked example, not the thesis.** A new examples folder carries one self-contained proof file (it imports only the standard library) about requalifying a release after a policy rewrite: 6 theorems, a recorded verification transcript, and a rejected control. It proves a cache-reuse exactness result in the same family (reuse a cached verdict only when the rule and everything it reads are unchanged); it proves nothing about incremental safety preservation, noninterference, or capability shrinkage.
- **Head theorem count moves 0 to 6, all example theorems.** The thesis evidence state at the head is unchanged: **claimed-not-proven** (the claim lives only in the repo description field; the head itself states nothing).

## Thesis (what the repo claims to prove) — unchanged

- The repo itself states nothing: there is still no readme at the live head.
- Repo description: a Lean 4 proof that safety is preserved incrementally across releases, with security consequences (noninterference, monotone capability shrinkage), built on the composable sibling.
- Plain English: the claimed thesis is that if a release is safe, and each change is checked only on the symbols it touches plus their dependency cone, then the changed release is still safe — and the same incremental check preserves noninterference (low observers never see high data), keeps every symbol's reachable observations inside its allowance (capabilities only shrink), and respects the componentwise cost allowance.
- Evidence state at this pin: **claimed-not-proven** at the head. The development that addresses it exists only on the unmerged branch (annex in the old census; merger status above).

## Theorem census at the live head

### Library: 0 theorems

There is no library and no package at the head. A text search of the whole clone for theorem and lemma declarations finds them only in the worked example below.

### Worked example: requalifying after a policy rewrite (6 theorems)

Vocabulary, plainly: an acceptance policy is a list of rules; each rule is a boolean expression over numbered facts (a single fact, a conjunction, or a disjunction). Each rule's read set is derived from its shape. A cached verdict for a rule may be reused when the rule itself is unchanged and every fact it reads has the same value in the new snapshot; otherwise the rule is freshly evaluated. The patch procedure walks the old cache against the new rule list positionally.

| Claim (one quoted name) | State | What it proves, plainly | Axioms (recorded transcript) |
|---|---|---|---|
| `frame` | proven | Frame property: if two snapshots agree on every fact a rule reads, the rule evaluates the same under both. | one standard axiom |
| `same_as_clean` | proven | A single refreshed verdict (reuse when reusable, recompute otherwise) equals a clean evaluation of the new rule under the new snapshot. | two of the standard three |
| `all_rows_exact` | proven | For arbitrary old and new rule lists, including additions and removals, the patched verdict list equals the clean rebuild's verdict list, position by position. | two of the standard three |
| `before_after` | proven | The worked numbers, by computation: the old verdict vector, the recomputed-slot pattern, and the new verdict vector are exactly the stated boolean lists (two of four slots recomputed, both of which flip). | none |
| `necessary_replacements` | proven | Any strategy that reuses old slot values must replace at least the two slots whose verdicts actually flip; the exhibited two fresh evaluations are a lower bound, not just an achieved one. | one standard axiom |
| `value_only_is_unsafe` | proven (counterexample fact) | Holding all source values fixed can still change a verdict when the rule itself is rewritten: the stated rule evaluates differently under the two rule versions at the same snapshot facts it reads. Rule equality is a real reuse condition, not a formality. | none |

- The example readme's before-and-after table (4 rule evaluations in a clean rebuild against 2 fresh evaluations plus 2 valid cached values) is the content of the fourth and fifth rows.
- Control: the transcript records a rejected mutation (reusing a value across a rule-only edit fails checking, exit 1).
- Premises carried by the example, stated in its own scope note: rows are positional; reuse requires a correct original cache and pure evaluations of the declared facts; work units are fresh rule evaluations, and the equality checks and cache reads also cost work that the headline count does not claim to cover.

## Zero-sorries and gate evidence

- This census ran the token search on the clone: no sorry, admit, axiom-declaration, or native-decision token anywhere in the tree.
- Gate at head: there is **no repo-level check script and no recorded whole-repo check log**. The example folder has its own runner (compile the one proof file with warnings as errors) and its own recorded transcript showing the version line, all six axiom lines, the computed verdict vectors, and the rejected control. That transcript is the gate evidence, and it covers the example only.
- This census did not run any build; the transcript is the repo's own recorded evidence, labelled as such.

## The merger question (head tree is the evidence)

- Question posed for this refresh: has the former branch content (old census: branch head `5c1006a6ae6ee41a4bc19247db3a95589f5a3e9e`, 86 theorems) merged into the head?
- Answer: **no.** The head tree contains none of that development's files (listed in the Delta). The branch's pull request (the first pull request of this repo, opened 2026-11-18) is still open at this census, and the branch still exists alongside a second, draft pull request on a different branch; neither is head content and neither is censused here beyond this note.
- Consequence for the estate census: every theorem count, premise flag, and disproof recorded for that branch in the old census remains branch-only evidence. Nothing about the head's state has changed except the addition of the worked example.

## Explicit non-claims and boundaries at head

- At the live head the repo claims nothing in its own files — no readme — so the thesis above is a description-field claim about a proof that, at the head's pin, is not in the repo. The worked example states its own boundaries (positional rows, correct-cache premise, uncounted check costs) and claims nothing about safety preservation, noninterference, or capabilities.

## Watch delta — 2026-11-18, the hourly re-synthesis watch

Branch listing read by the watch at its run, supplementing the merge answer above: the default head 8ad1dd26, plus two side branches — the cursor branch at 4a17787aadba1d023b10029cd52a20b7a23146ce (11 Lean files; 87 theorem or lemma declarations in this repo's own modules and 32 more in the two carried stand-in files) and the full-snapshot admission audit branch at c53eafe3698729a5158b3df89f9af3718606317d (13 Lean files; 112 declarations in its own modules and the same 32 in the stand-ins). The branch name that carried the first census pin 5c1006a6 no longer appears in the listing. Counts are the watch's mechanical declaration counts. Neither branch is merged into the head; the head state recorded above stands.
