# Census — software-is-incrementally-certifiable (clpi) — refresh draft

Census date: 2026-11-18, ~02:10–02:40 PST. Method: live head read first via the gh route, then a shallow clone (depth 1); clone head verified equal to the live head. Clone read only, never edited. This draft replaces the census of the older pin; changes are marked in the Delta section.

## Pins

- Old census pin: `f3b9f896ac76a95e7104c98af66e41413e7e5b2d` — a single readme file, theorem count 0, thesis state claimed-not-proven.
- Live head (default branch `master`): `c9ffd49a906038d29d3e0d726093c410b3db798e`. Clone head matches exactly. Head commit subject, plainly: add a checked before-and-after example for a tree repair.
- Visibility: private.
- Toolchain pin: **none — the repo still has no toolchain file, no lakefile, and no manifest.** The worked example's own runner states it needs Lean 4.19.0, but the repo pins nothing.
- Files at head: the original readme (unchanged claim, two lines) plus one worked-examples folder holding a single standalone proof file, its readme, a runner script, an independent replay script in a second language, and a recorded verification transcript. Theorem total in tree: **7**, all inside the worked example. Library theorems: **0**.

## Delta (old pin to this pin)

- **The thesis is still not proved in this repo.** No library, no package, and no theorem about certification, extensivity, or dominance has landed at the head. The headline claim's evidence state is unchanged: **claimed-not-proven**.
- **What landed is a worked example, not the thesis.** A new examples folder carries one self-contained proof file (it imports only the standard library) about repairing one edited leaf in a balanced hash tree: 7 theorems, a recorded verification transcript, and a rejected control. It is evidence that an incremental-repair cost claim of the same family can be formalised and checked; it proves nothing about the certification closure or the dominance order named in the readme.
- **A side branch exists but is not head content.** A pull request opened before this census proposes proving incremental certification from a spec; it remains open and unmerged, and nothing from it is in the head tree. This census counts only the head.

## Thesis (what the repo claims to prove) — unchanged

- Repo description and readme, in full substance: a Lean 4 proof that incremental monotonic certification is extensive and yields dominance across releases in the componentwise cost order.
- Plain English: the claim on the tin is that the certification operator (the closure that adds every profile sitting below an already-certified one) is extensive — a certified thing stays certified — and that admission of a release can be decided by that closure together with a componentwise cost bound, giving a dominance order across releases.
- Evidence state at this pin: **claimed-not-proven.** No file at the head defines the closure, the profile order, or the cost order, and no theorem states extensivity, monotonicity, idempotence, or any dominance fact.

## Theorem census at the live head

### Library: 0 theorems

There is no library. A text search of the whole clone for theorem and lemma declarations finds them only in the worked example below. No disproof, no named premise, and no side condition about the thesis is stated anywhere at the head.

### Worked example: the hash-tree repair (7 theorems)

Vocabulary, plainly: a balanced binary tree of leaves; a cache holding a digest at every node; building the cache from scratch costs one hash call per node; repairing after a single leaf edit rebuilds only the edited path, reusing cached sibling digests, and returns the list of levels at which fresh receipts were produced. The hash functions are arbitrary supplied functions — the example's own scope note states the equality proof needs no collision-resistance assumption.

| Claim (one quoted name) | State | What it proves, plainly | Axioms (recorded transcript) |
|---|---|---|---|
| `build_cost` | proven | Building the cache for any tree of a given height costs exactly the full-work count for that height (the recurrence that doubles per level). | two of the standard three |
| `clean_equivalence` | proven | For every tree, path, and replacement payload, the repaired cache equals the cache built cleanly from the edited tree. Repair and rebuild agree in full. | one standard axiom |
| `repair_trace` | proven | The receipt levels reported by a repair are exactly the level list of the edited path. | one standard axiom |
| `levels_exact` | proven | The level list of any path of a given height is exactly the descending list of that height's levels. | one standard axiom |
| `least_receipts` | proven | Any receipt list complying with the audit contract (a fresh receipt at each changed path level) for a height-10 path has at least 11 entries. The exhibited count is a lower bound, not just an achieved one. | standard three |
| `before_after` | proven | The worked numbers, by computation: full work at height 10 is 2047 hash calls, and the path level count is 11. | none |
| `leaf_only_fails` | proven (boundary fact) | The root level is among the required levels of the leftmost height-10 path, and is not in a leaf-only receipt list — a leaf-only update misses the root, by computation. | two of the standard three |

- The example readme's before-and-after table (2047 hash calls per full rebuild against 11 per repaired tree, for 1024 leaves) is exactly the content of the first and sixth rows; the replay script independently re-executes 1024 single-leaf edits and checks every cached digest against a clean rebuild, and the transcript records all matching.
- Control: the transcript records a rejected mutation (retaining a stale subtree after an edit fails checking, exit 1).
- Premises carried by the example, stated in its own scope note: the count covers a single edit using an existing, valid cache; cache acquisition, disk access, and multi-edit scheduling have separate costs and are not claimed.

## Zero-sorries and gate evidence

- This census ran the token search on the clone: no sorry, admit, axiom-declaration, or native-decision token anywhere in the tree.
- Gate at head: there is **no repo-level check script and no recorded whole-repo check log**. The example folder has its own runner (compile the one proof file with warnings as errors, then run the independent replay) and its own recorded transcript showing the version line, the computed pair (2047, 11), all seven axiom lines, the replay summary, and the rejected control. That transcript is the gate evidence, and it covers the example only.
- This census did not run any build; the transcript is the repo's own recorded evidence, labelled as such.

## Explicit non-claims and boundaries at head

- The readme still asserts a finished proof of the certification thesis; the repo at this pin contains no artifact that could back that assertion for the thesis itself. The gap is narrowed only in this sense: the repo now contains one fully checked worked example in the same problem family. The thesis gap itself is the headline finding, stated here, not smoothed over.
- Nothing in the repo states any boundary for the thesis claim beyond the example's own scope note (single edit, valid cache, no collision-resistance assumption needed).

## Annex — the stand-in module on another repo's unmerged branch (NOT this repo's content) — carried forward

The only Lean code developing this thesis remains the stand-in module inside the safe sibling repo's open pull request branch (14 theorems: extensivity, monotonicity, and idempotence of the closure; reflexivity and transitivity of the componentwise cost order; dominance implying the order; irreflexivity of dominance as its one disproof; five interface-obligation theorems that hold by definition; the admission equivalence; and downward closure of admission). Those theorems are **not** theorems of this repo, that branch is still unmerged at this census, and the stand-in does not prove optimality in the sense of an optimal element existing or being attained. Full census of the stand-in is in the safe sibling's census file.

## Watch delta — 2026-11-18, the second hourly re-synthesis watch

The watch re-read the live head at the enumeration head 3690167318cf4d41b51d0945f4fccc7f043e8412 and shallow-cloned it. Mechanical count at that head, by the watch's own method (every theorem or lemma declaration in every Lean file in the tree): 88 declarations (88 distinct short names) across 16 Lean files, no sorry token and no custom axiom declaration in any file, 0 example declarations. The same method at the last recorded head c9ffd49a906038d29d3e0d726093c410b3db798e counted 7 declarations (7 distinct short names). Name comparison, one mechanical method both times: 81 names gained, 0 lost. The prose placements in this annex stand at the census pin c9ffd49a906038d29d3e0d726093c410b3db798e; a full re-census at the new head is owed and the owed mark in the ledger stands.

The head tree changed in kind, not only in count: a full library now stands at the head — the certification closure modules, an audit pair, a command-line face, and a recorded check log ending in a pass — where the last census recorded seven theorems inside one worked example and the thesis absent as a library. The repo's own claims table now marks its closure results proven and one union reading disproven, and names five premises. A full theorem-level census at the new pin is owed; the placement in the synthesis stands at the old pin until it lands.
