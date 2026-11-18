# The estate census — every repo placed in the loop

First census, 2026-11-18. Method: the estate was enumerated
completely through the authenticated owner listing (558
repos: 249 public, 309 private, 2 archived, 45 forks),
passing the 300-repo public listing cap; every repo's head
was then read individually. clpi is a user account, not an
organization. Heads below are as read on 2026-11-18 between
01:20 and 01:40 PST; the proof repos' heads were re-read at
01:32 PST and the later read governs where they differ.
Machine-readable pins: synthesis-pins.json.

Every repo appears. Depth follows evidence: the proof family
at theorem level (synthesis.md), the Idol family at
role-and-state placement (below), the long tail as census
rows with their state named. A repo that was not read beyond
its listing is colored UNKNOWN — intended-but-unwitnessed, in
the loop's own terms. Unknown is a state of this census, not
an omission from it. 81 repos are empty (no commits; the head
read returns "repository is empty") — an empty repo for a
named project is a defect under the standing rule that repos
are the canonical live source of truth, and each is colored
unknown with that note.

## Sweep update — 2026-11-18 (estate-wide, by content)

A second enumeration the same night, under Chris's ruling
that the accounting is estate-wide and determined by content:
565 repos (251 public, 314 private), every head read again.
Seven repos are new since the first census (named in the
proof family list below and in the table). 80 repos are empty
— accounted as carrying no provable results.

Determination method (the named check): every non-empty repo
was swept by content searches over the estate for
proof-assistant sources and proof artifacts — Lean, Coq,
Agda, Idris, Isabelle, F-star, SMT, TLA, Dafny, and Alloy
file extensions; Verus macro content; Kani proof content —
and every hit was resolved by direct tree inspection. Repos
created or moved inside the sweep window, where search
indexing lags, were inspected by direct tree read instead:
the seven new repos and all eleven repos whose heads moved.
Machine-checked result artifacts were counted where a repo's
own stated purpose is a checked result (one case, below).

Outcome: 20 repos are proof-bearing and are censused at
theorem or evidence level in the annex (census/) and placed
in synthesis.md — the original nine, plus
software-compilers-lose-info, software-is-more-
traceable-than-you-think, idol-theses,
software-testing-is-redundant, software-fuzzing-is-suboptimal,
software-benchmarking-is-redundant-and-suboptimal, idol-semi
(with semi-persistent, the identical tree at the identical
pin), premise-retraction-playground, idol (proof-bearing
content only), and this repo itself. The remaining 465
non-empty repos are determined proof-free by the named check
above; their table rows below keep their first-census pins,
and this section is their determination record. Named
non-results the check resolved: the V-language example files
in dfmac and pwiki (not Coq); the polyglot fixture samples in
manus and idol-restored (test data, accounted in the idol
annex); the SMT corpus inside idol (accounted in the idol
annex as part of its checked-evidence tree).

Refreshed and new pins from the sweep (census pin / live head
at the sweep's close, where they differ): quantifiable
f3709926; optimality b52c3170 / a2e492cb; composable
a3058ba6 / 7d72fd08; certifiable c9ffd49a; safe head
8ad1dd26; regress c36829da; review 40b1e885; solvable
5bbceee7; frontier 6a41c7be; compilers-lose-info f531e31a;
traceability 4420fb1e / 5f84b051; idol-theses d207be6e /
ea7437ac; testing 66f65b6f; fuzzing 18d9569b; benchmarking
4314a181; idol-semi and semi-persistent 508d7c66;
premise-retraction-playground 47f469a4; idol 561cf395 /
c8336841; this repo d8047804. A census pin with a differing
live head carries re-census owed, per resynthesis.md.

## Watch update — 2026-11-18 (second hourly re-synthesis)

A third enumeration the same night: 565 repos, every head
read individually, no read errors. Twenty repos had moved
since the sweep pins, none were new, none were gone, and
the paper source hash was unchanged. The moved set: the
proof repos benchmarking, compilers, regress, review,
frontier, fuzzing, this repo, composable, certifiable,
safe, traceability, quantifiable, solvable, optimality,
and testing; the theses repo; the idol repo; and three
further idol-family repos (the compiler port, the library,
and the relay). Fresh heads for every repo stand in the
pins file at this re-synthesis; the moved proof repos'
annex deltas carry their mechanical counts at the fresh
heads, and two of them changed in kind at the head — the
certifiable and safe libraries landed in their head trees,
recorded in the synthesis watch section. The three further
idol-family repos were checked by tree read at their fresh
heads and carry no proof-assistant content; they remain
proof-free by the named check.

## Watch update — 2026-11-18 (third hourly re-synthesis)

A fourth enumeration the same night: 565 repos, every head
read individually, no read errors. Thirty-six repos had
moved since the last recorded heads, none were new, none
were gone, and the paper source hash was unchanged. The
moved set: the proof repos optimality, composable, safe,
and idol, and this repo itself; two further idol-family
repos (the compiler port and the relay); and twenty-nine
long-tail repos. Fresh heads for every repo stand in the
pins file at this re-synthesis; the moved proof repos'
annex deltas carry their mechanical counts at the fresh
heads. The two further idol-family repos and the long-tail
repos were read by tree at their fresh heads and carry no
proof-assistant content, so they remain proof-free by the
named check — with one stated limit: one long-tail tree
read was truncated by size, no proof-assistant source stood
in the returned portion, and its determination stands from
the sweep. The idol tree read found the release tools Lean
development recorded in its annex delta.

## Watch update — 2026-11-18 (fourth hourly re-synthesis)

A fifth enumeration the same night: 565 repos, every head
read individually, no read errors. Eighty-eight repos had
moved since the last recorded heads, none were new, none
were gone, and the paper source hash was unchanged. The
moved set: the proof repos safe and idol, and this repo
itself; two further idol-family repos (the graph repo and
the relay); and eighty-three long-tail repos. Fresh heads
for every repo stand in the pins file at this re-synthesis;
the moved proof repos' annex deltas carry their mechanical
counts at the fresh heads. The two further idol-family
repos and the long-tail repos were read by tree at their
fresh heads and carry no proof-assistant content, so they
remain proof-free by the named check; no tree read was
truncated this watch, and the one extension hit is the
V-language example set in one long-tail repo, resolved as
not Coq by the sweep. The idol tree read found a new Lean
development in its solver benchmarks, recorded in its
annex delta, and the safe repo's merged change discharged
its string cone hypothesis, recorded in its annex delta.

## Watch update — 2026-11-18 (fifth hourly re-synthesis)

A sixth enumeration the same night: 565 repos, every head
read individually, no read errors. Six repos had moved
since the last recorded heads, none were new, none were
gone, and the paper source hash was unchanged. The
moved set: the proof repos idol and idol-semi, and this
repo itself; and three further idol-family repos (the
compiler port, the library, and the relay). Fresh heads
for every repo stand in the pins file at this
re-synthesis. Both moved proof repos were read in full
at their fresh heads: every Lean file in each is
byte-identical to its last recorded head, so their
proven sets are unchanged and their annex deltas record
the tree evidence. The semi repo's movement is ten
added files of analysis and parity tooling; its mirror
did not move and still stands at the shared census pin,
so the two repos' heads have diverged while their proof
content remains identical. The three further idol-family
repos were read by tree at their fresh heads and carry
no proof-assistant content, so they remain proof-free
by the named check; no tree read was truncated this
watch.

## Watch update — 2026-11-18 (sixth hourly re-synthesis)

A seventh enumeration the same night: 565 repos, every
head read individually, no read errors. Two repos had
moved since the last recorded heads, none were new,
none were gone, and the paper source hash was
unchanged. The moved set: this repo itself, and one
further idol-family repo (the compiler port). Fresh
heads for every repo stand in the pins file at this
re-synthesis. This repo's movement is the fifth watch
landing itself: the four commits between the heads are
that watch's annex, placement, ledger, and pins
commits, no Lean file changed among them, and its
eleven theorems stand unchanged, recorded in its annex
delta. The compiler port was read by tree at its fresh
head and carries no proof-assistant content, so it
remains proof-free by the named check; its tree stands
at the same file count as at its last recorded head,
with no file added or removed and two files changed.
No tree read was truncated this watch.

## Watch update — 2026-11-18 (seventh hourly re-synthesis)

An eighth enumeration the same night: 565 repos, every
head read individually, no read errors. Three repos had
moved since the last recorded heads, none were new,
none were gone, and the paper source hash was
unchanged. The moved set: this repo itself, and two
further idol-family repos (the compiler port and the
relay). Fresh heads for every repo stand in the pins
file at this re-synthesis. This repo's movement is the
sixth watch landing itself: the four commits between
the heads are that watch's annex, placement, ledger,
and pins commits, no Lean file changed among them, and
its eleven theorems stand unchanged, recorded in its
annex delta. The compiler port and the relay were read
by tree at their fresh heads and carry no
proof-assistant content, so they remain proof-free by
the named check; the compiler port's tree stands at
the same file count as at its last recorded head, with
no file added or removed and two files changed, and
the relay's tree gained one file, a dated coordination
note, with no file changed or removed. No tree read
was truncated this watch.

## Watch update — 2026-11-18 (eighth hourly re-synthesis)

A ninth enumeration the same night: 565 repos, every
head read individually. Four first reads failed on
transport stream errors; each of the four was re-read
individually and matched its last recorded head, so the
final reads carry no errors. Four repos had moved since
the last recorded heads, none were new, none were gone,
and the paper source hash was unchanged. The moved set:
this repo itself, and three further idol-family repos
(the compiler port, the relay, and the sites repo).
Fresh heads for every repo stand in the pins file at
this re-synthesis. This repo's movement is the seventh
watch landing itself: the four commits between the
heads are that watch's annex, placement, ledger, and
pins commits, no Lean file changed among them, and its
eleven theorems stand unchanged, recorded in its annex
delta. The three further idol-family repos were read by
tree at their fresh heads and carry no proof-assistant
content, so they remain proof-free by the named check;
the compiler port's tree gained one file and two files
changed over eighteen commits, the relay's tree gained
one file, a dated audit note, with no file changed or
removed, and the sites repo's tree gained seventy
files, a new prompt board space, with four files
changed and the paper page file unchanged between the
heads. No tree read was truncated this watch.

## Watch update — 2026-11-18 (ninth hourly re-synthesis)

A tenth enumeration the same night: 565 repos, every
head read individually, no read errors. Two repos had
moved since the last recorded heads, none were new,
none were gone, and the paper source hash was
unchanged. The moved set: this repo itself, and one
further idol-family repo (the compiler port). Fresh
heads for every repo stand in the pins file at this
re-synthesis. This repo's movement is the eighth watch
landing itself: the four commits between the heads are
that watch's annex, placement, ledger, and pins
commits, no Lean file changed among them, and its
eleven theorems stand unchanged, recorded in its annex
delta. The compiler port was read by tree at its fresh
head and carries no proof-assistant content, so it
remains proof-free by the named check; its tree stands
at the same file count as at its last recorded head,
with no file added or removed and two files changed
over ten commits. No tree read was truncated this
watch.

## The proof family — placed at theorem level in synthesis.md

- software-is-quantifiable (public) — the finiteness,
  coloring, fold, Pareto-at-bounds, and coverage-premise
  theorems. Census pin 37917a41; head at synthesis ba27febf.
- software-optimality (private) — the closure semantics,
  executable bridge, frontier, schedules, campaigns, scoped
  evidence and selection, relevance profiles, and incremental
  hypergraph theorems. Census pin 0ea4626b; head at synthesis
  aab49084.
- software-is-composable (private) — release admission and
  the incremental recheck equivalence, at pin 033c12c0.
- software-is-incrementally-certifiable (private) — asserted
  at head f3b9f896 (readme only); its stand-in content is
  placed from the safe branch.
- software-is-incrementally-safe (private) — asserted at
  head 94661358 (toolchain only); its proof content is
  placed from the unmerged branch at 5c1006a6.
- software-doesnt-have-to-regress (private) — asserted at
  24d36c13 (readme only).
- software-doesnt-need-review (private) — asserted at
  ae5f3918 (readme only).
- software-is-solvable (private) — witness compounding and
  exact resolution accounting, at 815e125f.
- software-frontier-is-solvable (private) — exact frontier
  insertion and retraction, at c7ffc6d0.
- software-is-more-traceable-than-you-think — announced
  2026-11-18 01:30 PST, not landed at census time; enters on
  re-enumeration. Colored unknown.

Added by the sweep (same placement depth — synthesis.md
section 3.10 and the annex):

- software-compilers-lose-info (private) — the topological
  thesis: forgetting compilation loses provenance, proven;
  derivation-carrying compilation loses nothing. Pin f531e31a.
- software-is-more-traceable-than-you-think (private) — landed
  after the first census; at pin 4420fb1e the repo carries a
  readme and a fixture-scale example, its thesis recorded as
  not yet landed in-repo.
- idol-theses (public) — the Idol program's falsifiable
  theses in Lean: 35 native theorems, a cited tranche, and a
  named future-work remainder. Pin d207be6e.
- software-testing-is-redundant (private) — the exact
  redundancy criterion, proven; its name's unrestricted
  reading refuted in-repo. Pin 66f65b6f.
- software-fuzzing-is-suboptimal (private) — contract-bound
  adaptive dominance, proven; the blanket reading refuted
  in-repo. Pin 18d9569b.
- software-benchmarking-is-redundant-and-suboptimal
  (private) — conditional benchmark redundancy and dominance,
  proven in source. Pin 4314a181.
- idol-semi (private) and semi-persistent (public) — one tree
  at one pin, 508d7c66: 2,053 Lean theorems and Verus proofs
  over a congruence-closure and e-matching engine.
- premise-retraction-playground (public) — retraction
  exactness at executed-arithmetic level. Pin 47f469a4.
- idol (private) — proof-bearing content only: 7 Lean theorems
  of the elaboration frontier and a checked-evidence tree.
  Pin 561cf395.
- software-is-a-closed-loop (public) — this repo's own
  checked example: 3 axiom-free theorems. Pin d8047804.

In loop terms the proof family is the loop's own theory: it
supplies the theorems governing stages 1–9. Its repos are
also named software inside the loop — their pins re-enter at
stage 0 like any other, and this census is their stage 3
witnessing by other means.

## The Idol family — role-and-state placements

The Idol family is the loop's principal subject: the named
software whose releases the loop qualifies, and the machinery
that runs the loop on the engine side. Heads as read
2026-11-18 ~01:30 PST.

- idol (586ff5a1) — the language and compiler: the named
  software of stage 0, the source of the executions stage 3
  witnesses, and the pin every improvement re-enters against.
  Active; moved during census night.
- idol-compiler (e3d52654) — the pure-Idol compiler port: an
  improvement line whose pins are stage 8 candidates against
  the production compiler; its performance stands UNMEASURED
  in the wider record.
- idol-lib (69ee40eb) — the library ports: measured
  candidates — every port wins compactness and loses speed on
  the shared gaps in the wider record; those cells are stage 5
  frontier readings over this repo's pins.
- idol-wsp (6b1a7d81, public) — the weight-space programming
  proof of concept in pure Idol: a named workload family for
  stage 7 campaigns.
- idol-model (8ea29c9f), idol-graph (b8b07982), idol-ir
  (ef3b9ea1) — the model, the semantic graph, and the
  intermediate representation: the engine-side homes of stage
  4's hypergraph and its derived views.
- idol-os (a9ffe819) — the operating-system line: a venue and
  subject of qualification in the wider program.
- idol-live (2db4aade) — Idol Live: the live surface the
  loop's verdicts are presented through.
- idol-sites (12b61b6d) — the sites repo: hosts the live
  paper (paper.html here is synced from it) and the
  qualification surfaces — the loop's presentation stage.
- idol-wide (8aa4798f) and idol-wide-ide (ebf0cf4b, public) —
  Wide, the pure-Idol weight-space IDE: a subject and a
  surface of the program.
- idol-ocean (0ba07f62) — the ocean build line. Unexamined
  beyond its listing in this census: colored unknown.
- idol-observatory (7ec2600e) — the Observatory: the
  monotonicity and proof observatory surface.
- idol-api (46b8f168) — the Idol API: serves the latest
  revision by default — the loop's stage 8 output made
  queryable.
- idiom (72e71e16) — Idiom: a named project repo of the
  family, populated under the repos-are-truth rule.
- The remaining idol-named repos (idol-console 7e25bda8,
  idol-edit 6f0d83dc, idol-eyes d7e7b009, idol-id cd4c2e55,
  idol-id-agents 40cad7d9, idol-ide d06fd36c, idol-ifconv
  3590f2a4, idol-kernel 5832fb78, idol-native 4a851575,
  idol-relay 49c2e75d — pushed during census night,
  idol-restored 1c4ef7fd, idol-semi 238717ba, idol-space
  37bb410d, idolg 94de4e5c) are placed by their names and
  listing descriptions in the table below and colored
  unexamined in this census — unknown — except where the
  table's own description states their role. Four idol-named
  repos are empty: idol-canary-7x3q, Idol-grok, idol-lake,
  idol-release-observability — colored unknown, empty noted.

## The long tail

The remaining repos — tools, experiments, forks, archives,
personal and work repos accumulated over years — are the
estate the loop ranges over: each is potential named software
for a future qualification and is carried here at listing
depth. Their rows give the repo's own description verbatim
(where it has one), visibility, head pin, last push, and
state. Forks and archived repos are flagged in their rows.
None was read beyond its listing in this census; all are
colored unknown, and the continuous job's re-enumeration
keeps their pins current even at listing depth.

## The full table

Generated from the enumeration record at census time; the
same data, machine-readable, is synthesis-pins.json.

| Repo | Visibility | Description (repo's own) | Head | Last push | Flags | State |
|---|---|---|---|---|---|---|
| .clp | private | secret stuff | empty | 2022-02-01 | no commits | unknown (unexamined) |
| .df | private |  | 081620f4 | 2026-11-18 |  | unknown (unexamined) |
| .f | private | dotfiles | 88269541 | 2023-03-19 |  | unknown (unexamined) |
| .infra | private |  | 14e3aa40 | 2026-11-18 |  | unknown (unexamined) |
| .sway | private | df | d84e54f0 | 2023-05-02 |  | unknown (unexamined) |
| 2D-Beam-Propagation | public |  | dbad806e | 2026-11-18 |  | unknown (unexamined) |
| a-1 | private |  | 3a695b86 | 2026-11-18 |  | unknown (unexamined) |
| ach | private |  | empty | 2025-02-19 | no commits | unknown (unexamined) |
| acha | public |  | 6465c443 | 2025-02-19 |  | unknown (unexamined) |
| achat | private |  | empty | 2025-02-19 | no commits | unknown (unexamined) |
| ado | public | toy programming lang | 32c470cb | 2026-06-20 |  | unknown (unexamined) |
| ai | private | ai knowledge | empty | 2023-04-12 | no commits | unknown (unexamined) |
| aic | private |  | d32c79ca | 2024-10-01 |  | unknown (unexamined) |
| altblog | private |  | empty | 2021-12-09 | no commits | unknown (unexamined) |
| ann | private |  | 20a0741a | 2024-11-04 |  | unknown (unexamined) |
| any | private |  | fd163b96 | 2024-11-04 |  | unknown (unexamined) |
| api | private |  | empty | 2021-03-02 | no commits | unknown (unexamined) |
| apigen | public |  | 0a915471 | 2026-11-18 |  | unknown (unexamined) |
| autocoder | private | AutoCoder line of work on the Idol toolchain (clpi/zai contributions) | d74481bd | 2026-09-24 |  | unknown (unexamined) |
| aware | private |  | 49818749 | 2026-11-18 |  | unknown (unexamined) |
| awe | private |  | d1f04298 | 2024-11-04 |  | unknown (unexamined) |
| aws-cloudformation-templates | public | A collection of useful CloudFormation templates | d93ea5ff | 2026-08-21 | fork | unknown (unexamined) |
| axa | public |  | fac009ff | 2026-11-18 |  | unknown (unexamined) |
| axe | public |  | 37e33a51 | 2024-11-04 |  | unknown (unexamined) |
| ayu.nvim | public | personal ayu | 64f2bad8 | 2022-12-14 |  | unknown (unexamined) |
| ayum | private | ayu modifications for nvim | db4e0d4f | 2026-11-18 |  | unknown (unexamined) |
| babble | private |  | empty | 2025-10-10 | no commits | unknown (unexamined) |
| Bid | private |  | 71494722 | 2026-11-18 |  | unknown (unexamined) |
| boxd | private | Experiment box daemon: provision/run/collect/teardown across the Tailscale/Cloudflare compute mesh | ac14d07b | 2026-10-29 |  | unknown (unexamined) |
| browsh | public | A fully-modern text-based browser, rendering to TTY and browsers | 8d321c47 | 2022-07-01 | fork | unknown (unexamined) |
| burg.lua | public |  | d1a013ec | 2026-11-18 |  | unknown (unexamined) |
| bv | private |  | 5328a58f | 2026-11-18 |  | unknown (unexamined) |
| c.i | private |  | 5eb87643 | 2023-06-12 |  | unknown (unexamined) |
| c2 | public |  | empty | 2024-10-09 | no commits | unknown (unexamined) |
| cai | public |  | 47a37ee9 | 2024-09-29 |  | unknown (unexamined) |
| caillou.lua | public | fork of ayu color theme for nvim in progress | 6bf14e48 | 2022-04-16 | fork | unknown (unexamined) |
| captoma | public | auto capture software | empty | 2020-11-24 | no commits | unknown (unexamined) |
| cat- | public | Created with StackBlitz ⚡️ | 399bc67a | 2022-06-02 |  | unknown (unexamined) |
| cbase | private |  | 03184b29 | 2022-02-09 |  | unknown (unexamined) |
| cbc | public | nim ms | 927f4e4a | 2026-11-18 |  | unknown (unexamined) |
| ccr | private |  | b68c0945 | 2026-11-18 |  | unknown (unexamined) |
| cdotis | public |  | 9a94aadd | 2022-06-02 |  | unknown (unexamined) |
| cdx | public |  | b5fc055c | 2026-11-18 |  | unknown (unexamined) |
| ch | private |  | 01a0a605 | 2024-09-23 |  | unknown (unexamined) |
| chap | public | chalice lambda api | empty | 2026-05-17 | no commits | unknown (unexamined) |
| chrisp-finance- | private | personal finance | 01c61e12 | 2026-11-18 |  | unknown (unexamined) |
| chrisp.fyi | public | personal website 2 | 3b8b9969 | 2018-09-08 | archived | unknown (unexamined) |
| chrispweb | public | personal website | d5bcfeb2 | 2026-11-18 |  | unknown (unexamined) |
| ChrispWiki | private | Personal wiki | ea135062 | 2026-11-18 |  | unknown (unexamined) |
| ci | private |  | b2503262 | 2023-06-12 |  | unknown (unexamined) |
| cj | public |  | 910f31e2 | 2024-09-24 |  | unknown (unexamined) |
| cku | public | cku | 00314ba2 | 2026-11-18 |  | unknown (unexamined) |
| cl | public |  | 5b2bc81d | 2026-11-18 |  | unknown (unexamined) |
| clam | private |  | empty | 2026-05-15 | no commits | unknown (unexamined) |
| clam-alt-studio | private |  | f2ed79f0 | 2026-06-05 |  | unknown (unexamined) |
| clam-cli | public |  | 427c7a2d | 2026-11-18 |  | unknown (unexamined) |
| clam-studio | private |  | 1099f715 | 2026-06-06 |  | unknown (unexamined) |
| class-rs | public | a truly optimized, comfy-to-use, feather-mid-lightweight command line arg parsing alternative in Rust | 4d3009c9 | 2022-04-27 |  | unknown (unexamined) |
| climax | private |  | dca94cb5 | 2026-06-01 |  | unknown (unexamined) |
| clp | private |  | empty | 2023-06-12 | no commits | unknown (unexamined) |
| clp-begin | public | Begin app | 5d8d6a78 | 2020-12-15 |  | unknown (unexamined) |
| clp-mcp | private | my mcp | 41fa9c44 | 2026-06-02 |  | unknown (unexamined) |
| clp.is | public | personal website / portfolio | 9541bfde | 2021-11-21 |  | unknown (unexamined) |
| clpblogn | public |  | a6538367 | 2020-12-25 |  | unknown (unexamined) |
| clpeep | private | Close | empty | 2026-04-30 | no commits | unknown (unexamined) |
| clpi | public | Personal README repo :) | 2693958a | 2026-10-21 |  | unknown (unexamined) |
| clpis-blog | private |  | 505069c9 | 2021-04-16 |  | unknown (unexamined) |
| clpweb | public | personal website + way to experiment iwth rust + wasm | 02af63e8 | 2023-01-20 |  | unknown (unexamined) |
| cmp-wiki | public | nvim-cmp for vimwiki | 03bfae08 | 2021-12-19 | fork | unknown (unexamined) |
| coc-pyright | public | Pyright extension for coc.nvim | f048301d | 2022-04-08 | fork | unknown (unexamined) |
| codage | private |  | empty | 2026-05-24 | no commits | unknown (unexamined) |
| codagy | private |  | fb0abf4d | 2026-05-24 |  | unknown (unexamined) |
| collaborative-text-editor | private |  | 2b257a3f | 2024-09-23 |  | unknown (unexamined) |
| commerce | private |  | 0b11d165 | 2020-12-31 |  | unknown (unexamined) |
| corpora | public | A collection of small corpuses of interesting data for the creation of bots and similar stuff. | 0af58bc9 | 2020-11-18 | fork | unknown (unexamined) |
| cosmos-genesis-tinkerer | public | Python module for tinkering with Cosmos Network Genesis files | 8c8c811a | 2022-09-01 | fork | unknown (unexamined) |
| cplaydb | public | just a db for learning | 19b9c552 | 2026-11-18 |  | unknown (unexamined) |
| CppCoreGuidelines | public | The C++ Core Guidelines are a set of tried-and-true guidelines, rules, and best practices about coding in C++ | 6d018fcf | 2022-06-30 | fork | unknown (unexamined) |
| cpr | public |  | efaca3a9 | 2023-04-19 |  | unknown (unexamined) |
| crescent | public | ⛓️ Crescent Network, Expanding DeFi capabilities through InterBlockchain Technology 🌙 | d0ae1c97 | 2022-11-10 | fork | unknown (unexamined) |
| crit | private | important info | e8ca4ca9 | 2026-11-18 |  | unknown (unexamined) |
| crys | public | crystal server | empty | 2026-05-17 | no commits | unknown (unexamined) |
| crystal-lsp | private |  | 7a76ed7e | 2026-06-07 |  | unknown (unexamined) |
| crystalline | public | A Language Server Protocol implementation for Crystal. 🔮 | dcd54205 | 2025-04-30 | fork | unknown (unexamined) |
| cv | private |  | d8e6dc62 | 2024-10-07 |  | unknown (unexamined) |
| cw-ollo | private | cosmwasm + ollo | empty | 2022-09-29 | no commits | unknown (unexamined) |
| cwasm | public |  | 55cbb910 | 2020-12-15 |  | unknown (unexamined) |
| cync | public |  | empty | 2025-12-31 | no commits | unknown (unexamined) |
| cyu.lua | public | neovim colorscheme based loosely on ayu with a lot of plugin support | 5af5e7f6 | 2022-07-26 |  | unknown (unexamined) |
| d-docs | private | whitepaper and documentation for div,is | 07e4bdda | 2026-11-18 |  | unknown (unexamined) |
| d-ml | public | experimenting working with ml in rust | 158787a7 | 2026-11-18 |  | unknown (unexamined) |
| d-paper | private | whitepaper for div.is | empty | 2020-12-25 | no commits | unknown (unexamined) |
| dapi | public | new graphql-based api for di (again) | 28c5a8b9 | 2026-11-18 |  | unknown (unexamined) |
| dc | public |  | empty | 2025-11-14 | no commits | unknown (unexamined) |
| dcode | public |  | 428fcadb | 2021-12-20 |  | unknown (unexamined) |
| dd | public |  | 2d483558 | 2025-09-05 |  | unknown (unexamined) |
| ddf | private | dot files | f1433858 | 2025-12-06 |  | unknown (unexamined) |
| ddff | private |  | empty | 2025-12-06 | no commits | unknown (unexamined) |
| ddockwasm | public |  | cb5e4b02 | 2025-10-21 |  | unknown (unexamined) |
| ddrt | private |  | 15165483 | 2023-06-04 |  | unknown (unexamined) |
| dede | public |  | 2e47bf82 | 2026-05-04 |  | unknown (unexamined) |
| dede- | public |  | empty | 2026-05-04 | no commits | unknown (unexamined) |
| defre | public |  | d7f6a4e3 | 2022-06-11 |  | unknown (unexamined) |
| derive_more | public | Some more derive(Trait) options | 718fbb67 | 2021-12-07 | fork | unknown (unexamined) |
| des-steps | private |  | 11646d0d | 2026-06-06 |  | unknown (unexamined) |
| devisa | private |  | d5a9e96e | 2021-03-13 |  | unknown (unexamined) |
| devisa-webx | private | a project to get the core tech of devisa to mvp as quickly as possible by cutting out as much frontend learning as possible | 64fbd064 | 2021-06-26 |  | unknown (unexamined) |
| df | private | dotfiles for i3wm/sway config, Xresources config, vim/neovim config, qutebrowser, dmenu, zsh, bspwm | 3d71a8aa | 2020-12-18 |  | unknown (unexamined) |
| df-priv | private |  | 46348f9d | 2021-07-24 |  | unknown (unexamined) |
| dfc | private | chezmoi dotfiles | d84a5d3e | 2026-11-18 |  | unknown (unexamined) |
| dfiles | public | most important configs | 240deb85 | 2021-12-11 |  | unknown (unexamined) |
| dfl | private |  | 2b2ab704 | 2022-04-02 |  | unknown (unexamined) |
| dfls | public |  | empty | 2022-03-25 | no commits | unknown (unexamined) |
| dfm | private | mac dotfiles | empty | 2022-03-24 | no commits | unknown (unexamined) |
| dfmac | private |  | f7ce8e53 | 2022-06-13 |  | unknown (unexamined) |
| dfp | private | private dotfiles | e5b4d2ab | 2026-11-18 |  | unknown (unexamined) |
| dfz | public | dotfiles with chezmoi | 7a908f25 | 2024-10-22 |  | unknown (unexamined) |
| dgts | private |  | 866b28a3 | 2020-12-31 |  | unknown (unexamined) |
| di-admin | private |  | bbab7cf2 | 2026-11-18 |  | unknown (unexamined) |
| di-back | public | another backend implementation for div.is, this time more modular | e8783380 | 2026-11-18 |  | unknown (unexamined) |
| di-cli | public | command-line access to div.is tools | 820db457 | 2020-09-23 |  | unknown (unexamined) |
| di-client | public | local (cli/tui) interface | 25a35ca2 | 2020-11-26 |  | unknown (unexamined) |
| di-edit | public | my attempt at creating a different text editor | f47873e9 | 2026-11-18 |  | unknown (unexamined) |
| di-md- | public | md++ compiler | empty | 2020-11-25 | no commits | unknown (unexamined) |
| di-mob | public |  | c8f53694 | 2021-04-02 |  | unknown (unexamined) |
| di-net | public | network testing utilities dev | empty | 2020-12-04 | no commits | unknown (unexamined) |
| di-nim | public | testing out nim for systems programming | f62cf1a8 | 2026-11-18 |  | unknown (unexamined) |
| di-parse | public | implementation of natural language processing using peg grammar with rust (v early) | 16e29326 | 2020-11-27 |  | unknown (unexamined) |
| di-server | public | HTTP protocol & server implementation for d.i. | 07543317 | 2020-12-09 |  | unknown (unexamined) |
| di-srv | public | backend for d.i | 473385cc | 2021-03-01 |  | unknown (unexamined) |
| dib | private |  | 4a877159 | 2026-11-18 |  | unknown (unexamined) |
| dib-browser | private |  | 4f8704bd | 2025-12-11 |  | unknown (unexamined) |
| dib-chat | private |  | 43d69723 | 2025-12-11 |  | unknown (unexamined) |
| dib-im | private |  | 9503f1ef | 2025-12-11 |  | unknown (unexamined) |
| dib-openauth | private |  | 30dc7efd | 2025-12-13 |  | unknown (unexamined) |
| dibwf | public |  | 3f362ca8 | 2026-06-02 |  | unknown (unexamined) |
| digt | private |  | fd9ec674 | 2020-12-31 |  | unknown (unexamined) |
| diml | public | math/stat/ml experiments for d.is | 762f18a8 | 2026-11-18 |  | unknown (unexamined) |
| dimo2 | private | second di mob | 5fd0964d | 2021-04-15 |  | unknown (unexamined) |
| dimo2-build | private | exclusively build files for dimo2 | empty | 2021-04-15 | no commits | unknown (unexamined) |
| dito | public | toolkit for quantitative and qualitative self learning through natural language processing | empty | 2021-07-07 | no commits | unknown (unexamined) |
| div-alt | public | trying out using an all rust toolchain (deno, tauri, wasm) for web/desktop/etc | ac07a8f8 | 2026-11-18 |  | unknown (unexamined) |
| div-gui | public | Desktop application for div.is | 1a67e6da | 2020-09-18 |  | unknown (unexamined) |
| div-web | public | website for div.is | 0e2a6233 | 2020-08-05 |  | unknown (unexamined) |
| div.is | public | Long-term project for programmatic life data aggregation / record-keeping / goal and task management using Rust (warp.rs) back-end and Svelte frontend | 1759fd35 | 2023-02-04 |  | unknown (unexamined) |
| divi | private |  | 23179eae | 2021-12-18 |  | unknown (unexamined) |
| divin | private |  | 4b164fcd | 2021-12-18 |  | unknown (unexamined) |
| divl | public | c | 414abd8a | 2026-11-18 |  | unknown (unexamined) |
| djib | private |  | 20408c3e | 2025-12-14 |  | unknown (unexamined) |
| dl | private |  | e9d7a1e3 | 2024-09-23 |  | unknown (unexamined) |
| dlog | public | basic logging/tracking cli tool (very early) | 51dd5ec9 | 2021-01-16 |  | unknown (unexamined) |
| dlog-cli | public |  | 4701c6c1 | 2026-11-18 |  | unknown (unexamined) |
| dn | public |  | bc24d30b | 2021-08-11 |  | unknown (unexamined) |
| dnet | private |  | 0484951a | 2021-08-03 |  | unknown (unexamined) |
| docs | public | Open source docs for Canto Public | 5249151d | 2023-02-28 | fork | unknown (unexamined) |
| dofi | private | df | eb4a436d | 2026-11-18 |  | unknown (unexamined) |
| dot | public |  | d8026dfa | 2026-11-18 |  | unknown (unexamined) |
| dot-vim | public | dotfiles are different vim (-related) editors | empty | 2024-09-12 | no commits | unknown (unexamined) |
| dot.files | private |  | empty | 2025-12-06 | no commits | unknown (unexamined) |
| dotfi | private |  | empty | 2025-12-06 | no commits | unknown (unexamined) |
| dotfiles-1 | public | Poom's Neovim, Tmux, Fish and other configurations for macOS & Linux. Literally my entire world. | 7ff53b31 | 2022-04-07 | fork | unknown (unexamined) |
| doti | private | labs for dito | e90b6446 | 2026-11-18 |  | unknown (unexamined) |
| dotrs | public |  | d8dbfdb2 | 2026-11-18 |  | unknown (unexamined) |
| down | public |  | 1a68daa1 | 2026-06-20 |  | unknown (unexamined) |
| down.lsp | public | lsp for down | 61f47aaa | 2026-06-02 |  | unknown (unexamined) |
| down.mcp | public |  | empty | 2025-10-09 | no commits | unknown (unexamined) |
| down.nvim | public | the (eventually) infinitely extensible markdown note-taking work environment that you can have in Neovim without having to ever leave the comfort of markdown. | 2205bc7a | 2026-06-22 |  | unknown (unexamined) |
| down.vscode | public |  | a491bb46 | 2025-09-14 |  | unknown (unexamined) |
| downls | public | down lsp, in rust this time | cc6586b1 | 2026-11-18 |  | unknown (unexamined) |
| dpub | public | cli reader | ee4dc8d3 | 2026-11-18 |  | unknown (unexamined) |
| dreq | public | tui for making, saving, and mocking HTTP requests for API development (in very very very early stages' | a58bdc40 | 2026-11-18 |  | unknown (unexamined) |
| dst | private |  | d3ba90b1 | 2020-12-31 |  | unknown (unexamined) |
| dtfl | private |  | b15e6a7f | 2022-06-13 |  | unknown (unexamined) |
| dued | public | editor | 43f49f6a | 2026-06-06 | fork | unknown (unexamined) |
| dui | public |  | 0c80d2a0 | 2020-12-30 |  | unknown (unexamined) |
| duo | private |  | f46703f6 | 2026-08-24 |  | unknown (unexamined) |
| duo-lsp | private |  | 5dd0d691 | 2026-08-24 |  | unknown (unexamined) |
| duo-mcp | private |  | fab55820 | 2026-08-08 |  | unknown (unexamined) |
| duo.el | private |  | aa1766d4 | 2026-06-19 |  | unknown (unexamined) |
| duo.nvim | private |  | 7f572a6d | 2026-06-19 |  | unknown (unexamined) |
| duo.vim | private |  | 0f412bce | 2026-06-19 |  | unknown (unexamined) |
| dv | private |  | adb85af2 | 2026-11-18 |  | unknown (unexamined) |
| dv-wasm | public | testing out wasm functionality for other applications | empty | 2020-08-05 | no commits | unknown (unexamined) |
| dvmsg | private | Begin app | 0adad2be | 2021-05-04 |  | unknown (unexamined) |
| dvs | private |  | b182d25c | 2021-12-18 |  | unknown (unexamined) |
| dvsa | private |  | 6325e7ef | 2021-03-19 |  | unknown (unexamined) |
| dvsa-apix | private |  | f9ec6c40 | 2026-11-18 |  | unknown (unexamined) |
| dvsa-app | private |  | 02fe7de2 | 2026-11-18 |  | unknown (unexamined) |
| dvsa-book | private |  | b5906471 | 2026-11-18 |  | unknown (unexamined) |
| dvsa-data | public |  | 5b81d941 | 2026-11-18 |  | unknown (unexamined) |
| dvsa-kngr | public |  | 11e7c1ee | 2026-11-18 |  | unknown (unexamined) |
| dvsa-ops | private |  | empty | 2021-03-13 | no commits | unknown (unexamined) |
| dvsa-store | private |  | d2121d10 | 2021-03-18 |  | unknown (unexamined) |
| dvsapi | private |  | 2d05d43a | 2026-11-18 |  | unknown (unexamined) |
| e | private |  | 5fc47740 | 2024-09-23 |  | unknown (unexamined) |
| efrst.vim | public | just a vim colorscheme | empty | 2022-06-17 | no commits | unknown (unexamined) |
| ei | private |  | 2b42980c | 2024-09-23 |  | unknown (unexamined) |
| el | private |  | 177d1c18 | 2024-09-23 |  | unknown (unexamined) |
| el.c | private |  | aec65992 | 2022-04-27 |  | unknown (unexamined) |
| em | private |  | 625115d9 | 2024-10-02 |  | unknown (unexamined) |
| ep | private |  | d8991bdc | 2024-09-23 |  | unknown (unexamined) |
| epdb | public |  | a4cbed92 | 2026-11-18 |  | unknown (unexamined) |
| epl | private |  | 4698e438 | 2024-09-23 |  | unknown (unexamined) |
| epm | public |  | e2440045 | 2024-09-23 |  | unknown (unexamined) |
| epms | public |  | 4ac2cc50 | 2024-09-23 |  | unknown (unexamined) |
| epn | private |  | 6f20610c | 2024-09-23 |  | unknown (unexamined) |
| eval | public | A neovim plugin to run lines/blocs of code (independently of the rest of the file), supporting multiples languages | 611c35ec | 2022-04-22 | fork | unknown (unexamined) |
| evi | public |  | empty | 2021-06-13 | no commits | unknown (unexamined) |
| ew | private |  | 6acdc812 | 2024-09-23 |  | unknown (unexamined) |
| exi.lua | public |  | 8c37bbed | 2024-10-09 |  | unknown (unexamined) |
| f. | private |  | empty | 2022-10-01 | no commits | unknown (unexamined) |
| false | public |  | a4e5bc2b | 2026-05-17 | fork | unknown (unexamined) |
| g | public |  | f581b281 | 2026-11-18 |  | unknown (unexamined) |
| gc | public | 3d tui | afa16d53 | 2026-11-18 |  | unknown (unexamined) |
| gd | public | engine | 60c19dbd | 2025-09-05 |  | unknown (unexamined) |
| GEMSEC | public |  | 9b184715 | 2026-11-18 |  | unknown (unexamined) |
| GEMSEC-Hilbert | private |  | 96169dce | 2019-10-03 |  | unknown (unexamined) |
| gemsec-metadata-front | private | frontend for GEMSEC metadata project | b576bcb9 | 2021-05-11 |  | unknown (unexamined) |
| gemsec-neuropep | public | Neuropeptide graphene-binding prediction project | 3e30b3b7 | 2020-07-29 |  | unknown (unexamined) |
| gemsec-web | private | The GEMSEC web application, current web stack Vue, FastAPI, and PostgreSQL | 808577ce | 2021-05-13 |  | unknown (unexamined) |
| GEMSEC_TSS | private |  | efc33bac | 2019-04-12 |  | unknown (unexamined) |
| genr | public | website/app/blog generation tool + cms | 7a619e77 | 2026-11-18 |  | unknown (unexamined) |
| genr.li | public | testing out full stack rust + gui programming | e8a44e3c | 2026-11-18 |  | unknown (unexamined) |
| gg | private |  | c4ca765e | 2024-10-06 |  | unknown (unexamined) |
| github-slideshow | public | A robot powered training repository :robot: | 0f21a6e5 | 2022-05-22 |  | unknown (unexamined) |
| gj | public |  | abc823b7 | 2026-11-18 |  | unknown (unexamined) |
| gon | public |  | b32e2077 | 2026-11-18 |  | unknown (unexamined) |
| graphlette | private |  | ec2a3c04 | 2021-12-11 |  | unknown (unexamined) |
| gridsome | private |  | e5369f49 | 2020-02-09 |  | unknown (unexamined) |
| grok1 | public | idol: keyword-free graph language. subject first. exact rationals. counted spans. self-hosted onto wasm32. | 6d2c977f | 2026-09-16 |  | unknown (unexamined) |
| guardian | private | hashgraph guardian | 9ce1c802 | 2025-10-08 |  | unknown (unexamined) |
| h-tui | public | tui for hedera | 4b2899e8 | 2026-11-18 |  | unknown (unexamined) |
| hcs-improvement-proposals | private |  | 6129d954 | 2025-10-08 |  | unknown (unexamined) |
| hedera-code-snippets | private |  | empty | 2025-10-10 | no commits | unknown (unexamined) |
| hedera-docs | private |  | 18b5098d | 2025-10-08 |  | unknown (unexamined) |
| hedera-portal-infrastructure | private |  | edb293b3 | 2026-11-18 |  | unknown (unexamined) |
| hedera-state-validator | private |  | b8a7a250 | 2025-10-08 |  | unknown (unexamined) |
| hedera-testing | private |  | c2965666 | 2025-10-08 |  | unknown (unexamined) |
| hedera-transaction-tool | private |  | 3f72f4e2 | 2026-01-29 |  | unknown (unexamined) |
| hg-snippets | private |  | ccd7ffcb | 2025-10-10 |  | unknown (unexamined) |
| hg-tools | private |  | 3e1d9603 | 2025-10-10 |  | unknown (unexamined) |
| hgbabble | private |  | ecab6509 | 2025-10-10 |  | unknown (unexamined) |
| hgctx | public |  | cc673430 | 2026-11-18 |  | unknown (unexamined) |
| hgi | private |  | ac8ff557 | 2025-10-09 |  | unknown (unexamined) |
| hiero-mirror-node | private |  | 18ef799c | 2025-11-24 |  | unknown (unexamined) |
| hiero-mirror-node-explorer | private |  | eb14d7e9 | 2026-11-18 |  | unknown (unexamined) |
| home | public |  | empty | 2024-10-21 | no commits | unknown (unexamined) |
| idhs | public |  | a9cf14fa | 2026-11-18 |  | unknown (unexamined) |
| idiom | private |  | 72e71e16 | 2026-11-09 |  | idol family — placements above |
| idja | private |  | empty | 2022-02-04 | no commits | unknown (unexamined) |
| idl | public |  | 368f5177 | 2022-01-10 |  | unknown (unexamined) |
| idlesys-Central | private |  | e33c81f9 | 2021-12-09 |  | unknown (unexamined) |
| idlex.vim | private |  | 5c7e4c70 | 2026-11-18 |  | unknown (unexamined) |
| idlntx | public | primitive experimental version of the real thing | 0c6deec9 | 2021-06-16 |  | unknown (unexamined) |
| idlx | public |  | 61d0acda | 2022-05-28 |  | unknown (unexamined) |
| idnx | private |  | d0fdd1db | 2022-02-05 |  | unknown (unexamined) |
| idol | private |  | 586ff5a1 | 2026-11-18 |  | idol family — placements above |
| idol-api | private | Idol-authored compiler and semantic graph API; native admission and production qualification tracked explicitly | 46b8f168 | 2026-11-08 |  | idol family — placements above |
| idol-canary-7x3q | private | canary - do not delete | empty | 2026-09-25 | no commits | idol family — placements above |
| idol-compiler | private | The Idol compiler, written in Idol — the pure-Idol port of clpi/idol's compiler | e3d52654 | 2026-11-18 |  | idol family — placements above |
| idol-console | private |  | 7e25bda8 | 2026-10-30 |  | idol family — placements above |
| idol-edit | private | Independent Idol source editor. Graph and Space are separate products. | 6f0d83dc | 2026-11-07 |  | idol family — placements above |
| idol-eyes | private | Idol-native computer perception, control, and UI. Graph-owned semantics; verified outcomes; measured Peekaboo parity and dominance as release gates. | d7e7b009 | 2026-11-08 |  | idol family — placements above |
| idol-graph | private |  | b8b07982 | 2026-11-18 |  | idol family — placements above |
| Idol-grok | private |  | empty | 2026-09-17 | no commits | idol family — placements above |
| idol-id | public | idol.id platform — one repo, five faces: explorer, registry, docs, API, landing | cd4c2e55 | 2026-11-07 |  | idol family — placements above |
| idol-id-agents | public | Idol platform agent bootstrap (kilo, opencode, hermes, grok, claude, codex, oh-my-pi, poolside, agy) | 40cad7d9 | 2026-11-03 |  | idol family — placements above |
| idol-ide | private |  | d06fd36c | 2026-11-04 |  | idol family — placements above |
| idol-ifconv | private |  | 3590f2a4 | 2026-08-25 |  | idol family — placements above |
| idol-ir | private | Idol graph IR: keyword-free surface other languages compile to and emit from. Measured kernel floors. No module paths. | ef3b9ea1 | 2026-11-12 |  | idol family — placements above |
| idol-kernel | private | Idol kernel: law-inheriting graph → demand → one realization. Not a new language. Donor: clpi/idol-restored@1d085bf. | 5832fb78 | 2026-10-07 |  | idol family — placements above |
| idol-lake | private |  | empty | 2026-10-29 | no commits | idol family — placements above |
| idol-lib | private | Daily graph-native Idol rewrites of major open source codebases: one per day, minimum lines, minimum syntax, highest performance, proven against the incumbent. |  69ee40eb  | 2026-11-18 |  | idol family — placements above |
| idol-live | private | Idol Live: continuous coordination, authorship, and source-state substrate. Git is a compatibility projection. Separate from clpi/idol; will stand alone after Idol release. | 2db4aade | 2026-11-11 |  | idol family — placements above |
| idol-model | private |  | 8ea29c9f | 2026-11-17 |  | idol family — placements above |
| idol-native | private |  | 4a851575 | 2026-11-08 |  | idol family — placements above |
| idol-observatory | private |  | 7ec2600e | 2026-10-30 |  | idol family — placements above |
| idol-ocean | private |  | 0ba07f62 | 2026-11-06 |  | idol family — placements above |
| idol-os | private | The OS layer home for the Idol family: code signing first (identity-held re-signing by premise proof), process and jobs machinery to follow | a9ffe819 | 2026-11-17 |  | idol family — placements above |
| idol-relay | private | Shared coordination channel for Idol agents: Grok, Cursor, Codex, Grokbot, Muse, Devin. Post messages as files; poll for new ones. No provider lock-in. | 49c2e75d | 2026-11-18 |  | idol family — placements above |
| idol-release-observability | private | Private research and prototypes for evidence-scoped release observability, deterministic replay, and qualified release comparisons. | empty | 2026-11-16 | no commits | idol family — placements above |
| idol-restored | private | Idol — S0 kernel: graph sovereignty, demand-before-representation, compiler B. The kernel branch is the work line. | 1c4ef7fd | 2026-10-15 |  | idol family — placements above |
| idol-semi | private | Private Idol-owned fork/mirror of yaspar-org/semi-persistent for the Idol qualification hyperlattice and self-hosting path | 238717ba | 2026-11-18 |  | idol family — placements above |
| idol-sites | private | Catalogue of every Space and site built for Chris on Muse and ChatGPT sites, with full source, synced live | 12b61b6d | 2026-11-18 |  | idol family — placements above |
| idol-space | private | Idol-native compiler workbench and verified graph/fuzz components | 37bb410d | 2026-11-08 |  | idol family — placements above |
| idol-wide | private | Wide — an IDE in pure Idol for weight space programming, live at wide.idol.id | 8aa4798f | 2026-11-10 |  | idol family — placements above |
| idol-wide-ide | public | Idol Wide IDE: weight-space programming environment where weights are first-class values and every learned result carries its premises. | ebf0cf4b | 2026-11-16 |  | idol family — placements above |
| idol-wsp | public | Idol WSP — Idol Weight Space Programming: on-the-fly rewriting and reweighting experiments; a maximally compact live-rewriting coding agent built on Idol's weight space. | 6b1a7d81 | 2026-11-12 |  | idol family — placements above |
| idolg | private |  | 94de4e5c | 2026-09-21 |  | idol family — placements above |
| Idris-dev | public | A Dependently Typed Functional Programming Language | 6f968e59 | 2020-08-07 | fork | unknown (unexamined) |
| idsv | private |  | 07f7d8cb | 2022-02-05 |  | unknown (unexamined) |
| idula | public | a v2 at building a few languages in zig | 7b124476 | 2022-01-19 |  | unknown (unexamined) |
| idx | public |  | fe86a22e | 2022-02-23 |  | unknown (unexamined) |
| ie | public |  | a64fc709 | 2026-11-18 |  | unknown (unexamined) |
| iel | public | is elm | 4a41bf5e | 2026-11-18 |  | unknown (unexamined) |
| im.chrisp.cc | public | personal gatsby.js site | 248cc00e | 2023-03-03 |  | unknown (unexamined) |
| imark | public |  | cc1fe99f | 2022-05-30 |  | unknown (unexamined) |
| imchrispcc | public | Personal website | 2277bd41 | 2023-01-11 |  | unknown (unexamined) |
| impres-utils | public | utility scripts and programs I've written for work | c72ece82 | 2026-11-18 |  | unknown (unexamined) |
| incremental-build-explorer | public | Explore an incremental build as a graph: what was rebuilt, what was reused, and why. Prototype with synthetic sample data. | 293b45a3 | 2026-11-09 |  | unknown (unexamined) |
| infra | private |  | empty | 2026-05-31 | no commits | unknown (unexamined) |
| infrastructure | private |  | 2c2a2159 | 2025-10-17 |  | unknown (unexamined) |
| infrastructure-facts | private | hashgraph infrastructure facts | a95cec8f | 2025-10-08 |  | unknown (unexamined) |
| ipk | public | pkg mgmt | f763e9d8 | 2026-11-18 |  | unknown (unexamined) |
| iq | public |  | empty | 2022-04-02 | no commits | unknown (unexamined) |
| irex | private |  | 774e7e3e | 2022-02-04 |  | unknown (unexamined) |
| iridel-web | private |  | b538ba66 | 2021-04-17 |  | unknown (unexamined) |
| is-docs | private |  | 47e8b473 | 2021-12-10 |  | unknown (unexamined) |
| is-experiments | public |  | 044f666e | 2021-12-09 |  | unknown (unexamined) |
| is-lab | public |  | a885e9d4 | 2021-12-30 |  | unknown (unexamined) |
| is-progl | public | profl | empty | 2021-12-11 | no commits | unknown (unexamined) |
| is-rw | private |  | 581faeaf | 2021-12-10 |  | unknown (unexamined) |
| is-specl | public | spec lang | empty | 2021-12-11 | no commits | unknown (unexamined) |
| is-web | public |  | dece05a8 | 2022-01-03 |  | unknown (unexamined) |
| isdt | public | isd tool | b77853f2 | 2021-09-09 |  | unknown (unexamined) |
| isite | public | site for is | 6712f303 | 2026-11-18 |  | unknown (unexamined) |
| isprod | private |  | e417e4b6 | 2026-11-18 |  | unknown (unexamined) |
| isu | public |  | empty | 2022-04-10 | no commits | unknown (unexamined) |
| isu.rs | public | rewriting scripts for work + ui in rust | 424931b2 | 2026-11-18 |  | unknown (unexamined) |
| isut | public |  | cb654e34 | 2026-11-18 |  | unknown (unexamined) |
| isutils | public | new repo for work scripts/automation tool | 39fa92dc | 2022-04-03 |  | unknown (unexamined) |
| iz | public | attempting to create a cli data logging and automation tool/platform/utility in zig, rust, and nim as both an exercise for myself and to explore each of their respective merits as the project is fleshed out | 9ed5b911 | 2021-09-22 |  | unknown (unexamined) |
| jobs | private | repo for job search related assets | empty | 2020-11-27 | no commits | unknown (unexamined) |
| kafka-actix-example | public | Classic wordcount, updated with async/await! | 3376bdd2 | 2020-06-15 | fork | unknown (unexamined) |
| kiro.nvim | public |  | bbb55087 | 2026-06-19 |  | unknown (unexamined) |
| kitty | public | 😽 Soothing pastel theme for Kitty | 37a9bcac | 2022-10-26 | fork | unknown (unexamined) |
| lab | private |  | empty | 2025-12-31 | no commits | unknown (unexamined) |
| laravel-starter | public |  | 8b7b14b1 | 2026-10-30 |  | unknown (unexamined) |
| lay.rs | public | lay.rs | empty | 2021-08-11 | no commits | unknown (unexamined) |
| Layrs | private |  | ccbd53aa | 2026-10-30 |  | unknown (unexamined) |
| leetcode | public | leetcode solutions | b0077bfa | 2026-11-18 |  | unknown (unexamined) |
| lg | public | test game in love2d | 4a75a505 | 2026-11-18 |  | unknown (unexamined) |
| linuxdf | private | dotfiles to keep public. incl neovim, tmux, alacritty, kitty, sway, waybar... | 67095f2f | 2022-02-25 |  | unknown (unexamined) |
| liorm | private |  | b5b46178 | 2022-06-18 |  | unknown (unexamined) |
| lkit | public | Fast, small, webkit based browser framework extensible by Lua. | 6cac8334 | 2022-03-16 | fork | unknown (unexamined) |
| lng | public |  | 1bbd330f | 2026-11-18 |  | unknown (unexamined) |
| lov | public | love2d game | 5e467966 | 2025-09-12 |  | unknown (unexamined) |
| lrsv | private |  | 7ddab2f8 | 2023-06-04 |  | unknown (unexamined) |
| luo | private | lua language superset & compiler | empty | 2026-05-25 | no commits | unknown (unexamined) |
| luo-luo | private |  | b7a39001 | 2026-06-06 |  | unknown (unexamined) |
| lx | public | terminal rust editor | dc1b274e | 2021-07-22 |  | unknown (unexamined) |
| m2 | private |  | empty | 2025-12-08 | no commits | unknown (unexamined) |
| macvims | private |  | 26235b63 | 2024-02-12 |  | unknown (unexamined) |
| mad | private |  | aecf024f | 2024-10-02 |  | unknown (unexamined) |
| mai | private |  | 60be68f0 | 2024-10-02 |  | unknown (unexamined) |
| mainnet | public | Evmos Mainnet resources | f407ec77 | 2022-10-26 | fork | unknown (unexamined) |
| mal | public | mal - Make a Lisp | dcf8f4d7 | 2022-05-12 | fork | unknown (unexamined) |
| manus | public | Archive of a Manus agent session building an Idolic graph-native self-hosted compiler vertical slice + x86-64 ELF seed (2026-09-16) | 23c7235e | 2026-09-20 |  | unknown (unexamined) |
| mark.nvim | public |  | 17cccfca | 2026-06-06 |  | unknown (unexamined) |
| mas | private |  | d270e79e | 2024-10-02 |  | unknown (unexamined) |
| materiat | public | materials science in rust | 66406ab3 | 2026-11-18 |  | unknown (unexamined) |
| matr-sim | public |  | empty | 2020-11-27 | no commits | unknown (unexamined) |
| mau | private |  | 93bc1009 | 2024-10-02 |  | unknown (unexamined) |
| mb2 | private |  | empty | 2025-12-08 | no commits | unknown (unexamined) |
| mb22 | private |  | empty | 2025-12-08 | no commits | unknown (unexamined) |
| mbc | public |  | 30c77bfd | 2024-01-08 |  | unknown (unexamined) |
| mc | private |  | dfa72ec0 | 2024-10-02 |  | unknown (unexamined) |
| mch | private |  | 78b716d9 | 2024-10-02 |  | unknown (unexamined) |
| mcpy | public | mcpython | ac804697 | 2026-05-16 |  | unknown (unexamined) |
| mcpython | private |  | 2d61fefb | 2026-05-24 |  | unknown (unexamined) |
| mdal | public | md lang srv | fc469f72 | 2022-05-27 |  | unknown (unexamined) |
| mdd | public |  | bd7709dd | 2024-10-02 |  | unknown (unexamined) |
| me | private |  | 6e65ff56 | 2024-10-02 |  | unknown (unexamined) |
| meta | public | Artifacts from a Meta AI session building a from-scratch self-hosted compiler (zeroc/idolic/clpi_meta) | 4c50b92f | 2026-09-16 |  | unknown (unexamined) |
| mf | private |  | aec613d2 | 2024-10-08 |  | unknown (unexamined) |
| miki | private |  | b4210176 | 2026-11-18 |  | unknown (unexamined) |
| mink | private |  | e3fc8723 | 2023-09-04 |  | unknown (unexamined) |
| mis-api | private |  | 303f8f9d | 2025-12-13 |  | unknown (unexamined) |
| mk | private |  | 13c904c0 | 2026-11-18 |  | unknown (unexamined) |
| mle | private |  | empty | 2024-10-08 | no commits | unknown (unexamined) |
| mm | private |  | bf9fccec | 2024-10-02 |  | unknown (unexamined) |
| mmh | private |  | 2bfae061 | 2024-10-02 |  | unknown (unexamined) |
| mms | private |  | 21cdc6e1 | 2024-10-02 |  | unknown (unexamined) |
| mn | private |  | ddad1f74 | 2024-10-02 |  | unknown (unexamined) |
| mns | private |  | 8ad9fd67 | 2023-06-07 |  | unknown (unexamined) |
| mo | private |  | b8e2e99b | 2024-10-02 |  | unknown (unexamined) |
| moe-aggregator | public | moe market aggregator | 550fd629 | 2026-04-24 |  | unknown (unexamined) |
| moe-market | public | moe market | empty | 2026-04-24 | no commits | unknown (unexamined) |
| monitoring | private | hashgraph monitoring | b268938f | 2025-10-08 |  | unknown (unexamined) |
| mpre | private |  | 44d00355 | 2023-06-04 |  | unknown (unexamined) |
| mr | private |  | 315cc778 | 2024-10-02 |  | unknown (unexamined) |
| mre | private |  | 28ba6610 | 2024-10-02 |  | unknown (unexamined) |
| ms | private |  | a7022443 | 2024-10-02 |  | unknown (unexamined) |
| mtrl-web | private |  | d1ab270d | 2021-04-17 |  | unknown (unexamined) |
| mtrli | private |  | f63c0911 | 2023-06-12 |  | unknown (unexamined) |
| mtrlp | private |  | b5da56bf | 2023-06-04 |  | unknown (unexamined) |
| muxi | private |  | af73a865 | 2026-11-18 |  | unknown (unexamined) |
| mvc | private |  | 47127019 | 2024-10-02 |  | unknown (unexamined) |
| mvk | private |  | eb0a89e5 | 2024-10-02 |  | unknown (unexamined) |
| mvkb | private |  | e2907fe5 | 2024-10-02 |  | unknown (unexamined) |
| mx | private |  | 65817b35 | 2024-10-02 |  | unknown (unexamined) |
| Nash | public | A command-line shell like fish, but POSIX compatible. | bdd07024 | 2023-02-11 | fork | unknown (unexamined) |
| net-tui | private | idlenet tui | b1e16c52 | 2026-11-18 |  | unknown (unexamined) |
| newt | private | newt | 70d2c87f | 2022-10-13 |  | unknown (unexamined) |
| next-js-email-client | private |  | empty | 2025-02-19 | no commits | unknown (unexamined) |
| next-notionblog | private |  | c6b6e1f5 | 2021-12-09 |  | unknown (unexamined) |
| nextjs | private |  | 3f6ca96c | 2020-12-19 |  | unknown (unexamined) |
| nextjs-ai-chatbot | private |  | 19668c37 | 2025-10-11 |  | unknown (unexamined) |
| niki | private |  | f0770541 | 2026-11-18 |  | unknown (unexamined) |
| njs-notion-2 | private |  | abaab1ad | 2021-12-09 |  | unknown (unexamined) |
| note.down | private | an extensive markdown-based life record ecosystem | fb86af56 | 2026-03-06 |  | unknown (unexamined) |
| nrg | private |  | d782ba2a | 2026-08-26 |  | unknown (unexamined) |
| ntx | public |  | 81285bf0 | 2026-11-18 |  | unknown (unexamined) |
| nushell | public | A new type of shell | 49c93e5b | 2021-06-24 | fork | unknown (unexamined) |
| nuxtjs | private |  | af2a488c | 2020-02-09 |  | unknown (unexamined) |
| nvct | private |  | 8b5b228e | 2022-01-30 |  | unknown (unexamined) |
| nvim | public | nvim exclusive dotfiles | 2dd89ee8 | 2022-06-15 |  | unknown (unexamined) |
| nvim-mac | private |  | empty | 2022-06-13 | no commits | unknown (unexamined) |
| nvimmac | private |  | 66cdaa3d | 2022-06-13 |  | unknown (unexamined) |
| od | private |  | ac8ec5ba | 2023-06-12 |  | unknown (unexamined) |
| odd | private |  | 97308263 | 2024-09-23 |  | unknown (unexamined) |
| odj | private |  | 576638ef | 2023-06-19 |  | unknown (unexamined) |
| odms | private |  | 07e44631 | 2024-09-23 |  | unknown (unexamined) |
| odocs | private |  | 889d4164 | 2022-09-06 |  | unknown (unexamined) |
| of | public |  | 791bba00 | 2026-11-18 |  | unknown (unexamined) |
| of-net | public |  | b539b6cf | 2026-11-18 |  | unknown (unexamined) |
| ofn | public |  | empty | 2024-02-17 | no commits | unknown (unexamined) |
| ol | private |  | 51e8135a | 2024-10-07 |  | unknown (unexamined) |
| ollo | private |  | 16591a32 | 2023-03-09 |  | unknown (unexamined) |
| ollo-core | private |  | b8f8d676 | 2022-09-27 |  | unknown (unexamined) |
| ollo-newt | private |  | b6ccc4d4 | 2022-10-09 |  | unknown (unexamined) |
| ollo-newtn | private |  | 458ef234 | 2022-09-29 |  | unknown (unexamined) |
| ollo-out-of-nest | public | for frontend experiments I'llpost time to time to ensure of certain functionality | empty | 2022-10-04 | no commits | unknown (unexamined) |
| ollod | private |  | 0496e249 | 2022-07-21 |  | unknown (unexamined) |
| ollojs | private |  | 69399d49 | 2022-09-15 |  | unknown (unexamined) |
| ollozone | private |  | 9b0824fb | 2022-09-29 |  | unknown (unexamined) |
| ollx | private |  | 6b1ed1f8 | 2026-11-18 |  | unknown (unexamined) |
| ona | private |  | empty | 2026-09-18 | no commits | unknown (unexamined) |
| one | public | axum api | bd40199c | 2026-11-18 |  | unknown (unexamined) |
| openaudib-authth-template | private |  | 4d11cc10 | 2025-12-11 |  | unknown (unexamined) |
| osaurus | public | Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source. | 2df5d3a0 | 2026-05-24 | fork | unknown (unexamined) |
| oui | public |  | b59617bf | 2026-06-06 |  | unknown (unexamined) |
| oxen | private |  | 2cec1aa8 | 2026-11-18 |  | unknown (unexamined) |
| ozdocs | private |  | 58bf3fc3 | 2022-09-06 |  | unknown (unexamined) |
| ozone | private | ollo zone website | 722dfa68 | 2026-11-18 |  | unknown (unexamined) |
| panite.nvim | public |  | c1183a2d | 2022-12-14 |  | unknown (unexamined) |
| pass | private | pass creds | 3e842b19 | 2021-06-17 |  | unknown (unexamined) |
| pbj | private |  | 516e5ff0 | 2026-01-26 |  | unknown (unexamined) |
| pbroker | public | pubsub python | a7acdac3 | 2026-11-18 |  | unknown (unexamined) |
| pd | public |  | 4658faa1 | 2025-09-05 |  | unknown (unexamined) |
| pecu | public |  | empty | 2024-04-04 | no commits | unknown (unexamined) |
| pecu-lsp | public |  | empty | 2024-04-04 | no commits | unknown (unexamined) |
| pecu.cc | private | dueblue v2? | ea6cd55d | 2020-06-07 | archived | unknown (unexamined) |
| pecul | public |  | f019f62b | 2026-11-18 |  | unknown (unexamined) |
| pecunies | public |  | a6351d5a | 2026-10-21 |  | unknown (unexamined) |
| pecunies-tree | private | The Pecunies family tree as an Idol model: people, bonds, chronology entries, photos, uncertainties, and gaps seated as Idol values, with the explorable tree derived by an Idol program. Machine form of the Joe Pecunies chronology. | 6c8ba39c | 2026-11-09 |  | unknown (unexamined) |
| pecuwiki | private |  | 8bdd17e8 | 2026-11-18 |  | unknown (unexamined) |
| peep | public |  | 13067a38 | 2026-05-13 |  | unknown (unexamined) |
| per | private |  | bf5a6c5f | 2022-06-04 |  | unknown (unexamined) |
| per.li | public | rust wasm frontend | 7efd239f | 2026-11-18 |  | unknown (unexamined) |
| perapi | public |  | 71d7f421 | 2026-11-18 |  | unknown (unexamined) |
| perdj | private |  | empty | 2022-06-15 | no commits | unknown (unexamined) |
| personalDockerCompose | public | Docker compose setup for many things | 51f4d7d8 | 2020-03-13 | fork | unknown (unexamined) |
| pest | public | The Elegant Parser | f4ea7327 | 2022-04-12 | fork | unknown (unexamined) |
| pico-sdk | public |  | 426e4612 | 2022-05-22 | fork | unknown (unexamined) |
| pl-backend | public |  | empty | 2022-06-18 | no commits | unknown (unexamined) |
| pre | private |  | 2ca40ecc | 2024-10-07 |  | unknown (unexamined) |
| premise-retraction-playground | public | A miniature proof that learning can be premise-tracked: retract a training example and the weights become exactly those of a model trained on the rest. | 47f469a4 | 2026-11-16 |  | unknown (unexamined) |
| premise-viewer | public | Prototype viewer for premise-carrying decision sessions | 84d4b04f | 2026-11-09 |  | unknown (unexamined) |
| prisma-auth | private |  | 5a8b30d6 | 2021-12-09 |  | unknown (unexamined) |
| prisma_soc | private |  | 411b125e | 2021-12-09 |  | unknown (unexamined) |
| private-dotfiles | private | private dotfiles | empty | 2020-11-24 | no commits | unknown (unexamined) |
| private-hedera-services | private |  | empty | 2025-10-08 | no commits | unknown (unexamined) |
| pro | public |  | 08f8855b | 2026-11-18 |  | unknown (unexamined) |
| psocial | private |  | 726ed966 | 2021-12-09 |  | unknown (unexamined) |
| ptf | private |  | empty | 2022-06-05 | no commits | unknown (unexamined) |
| pwiki | private | private wiki | 7a28be81 | 2026-11-18 |  | unknown (unexamined) |
| py | private |  | 3b0bb37a | 2026-08-24 |  | unknown (unexamined) |
| python-ffmpeg | public | A python interface for FFmpeg using asyncio | 1db6751a | 2022-01-28 | fork | unknown (unexamined) |
| qnode | public |  | 31b7fd9f | 2026-11-18 |  | unknown (unexamined) |
| rcex | private |  | 63d27dfc | 2026-11-18 |  | unknown (unexamined) |
| rcx | private |  | empty | 2025-10-18 | no commits | unknown (unexamined) |
| recollection | public | data structure & algorithm implementations in rust | 9a895a3f | 2021-12-27 |  | unknown (unexamined) |
| register | public | Grab your own sweet-looking '.is-a.dev' subdomain | 7efd6913 | 2022-10-13 | fork | unknown (unexamined) |
| remix | private |  | 16c736c1 | 2021-12-12 |  | unknown (unexamined) |
| Remo | private |  | empty | 2025-12-21 | no commits | unknown (unexamined) |
| resume | private |  | d4469613 | 2026-11-18 |  | unknown (unexamined) |
| rm | private |  | 48d6b4d1 | 2024-10-06 |  | unknown (unexamined) |
| rs-cmp | public | rust compiler | empty | 2024-09-12 | no commits | unknown (unexamined) |
| rs-gr | public |  | 6385c436 | 2026-11-18 |  | unknown (unexamined) |
| rscmp | public | rust compiler | 73671208 | 2024-09-19 |  | unknown (unexamined) |
| rsdom | public | Zero-cost ultra-high-performance declarative DOM library using FRP signals for Rust! | d5e1928f | 2022-06-14 | fork | unknown (unexamined) |
| runner-images | private |  | 22e5072a | 2025-10-30 |  | unknown (unexamined) |
| rust-analyzer | public | A Rust compiler front-end for IDEs | f83dce0a | 2022-04-21 | fork | unknown (unexamined) |
| rust-libp2p | public | The Rust Implementation of the libp2p networking stack. | 23f6b00b | 2021-12-23 | fork | unknown (unexamined) |
| rust-wasm | public |  | c4696ebb | 2022-06-09 |  | unknown (unexamined) |
| rx | public |  | 4aa480a6 | 2024-02-25 |  | unknown (unexamined) |
| s2p | public |  | empty | 2022-07-05 | no commits | unknown (unexamined) |
| s8-web | private |  | 91fd59a1 | 2026-11-18 |  | unknown (unexamined) |
| sanity | private |  | f06481a9 | 2022-06-26 |  | unknown (unexamined) |
| semi-persistent | public |  | 508d7c66 | 2026-11-12 | fork | unknown (unexamined) |
| shadow-king-rose-tango | private |  | empty | 2026-09-17 | no commits | unknown (unexamined) |
| shy | public |  | empty | 2025-12-31 | no commits | unknown (unexamined) |
| site | private |  | 663f34cf | 2021-04-27 |  | unknown (unexamined) |
| ska | private |  | 81f0c4d6 | 2023-06-12 |  | unknown (unexamined) |
| software-doesnt-have-to-regress | private | Lean 4 proof that a release process with per-symbol observed-behavior certification never has to regress |  858a85e3  | 2026-11-18 |  | proof family — synthesis.md |
| software-doesnt-need-review | private | Lean 4 proof of when manual code review is redundant given per-symbol certification, and a proposal to replace it |  1d504014  | 2026-11-18 |  | proof family — synthesis.md |
| software-frontier-is-solvable | private |  |  22418d56  | 2026-11-18 |  | proof family — synthesis.md |
| software-is-composable | private | Independent Lean 4 proof of incremental release monotonicity: per-symbol observed behavior qualifies or disqualifies each release, and qualification composes across releases. | 7b174646 | 2026-11-18 |  | proof family — synthesis.md |
| software-is-incrementally-certifiable | private | Lean 4 proof that incremental monotonic certification is extensive and yields Pareto-optimal dominance across releases |  36901673  | 2026-11-18 |  | proof family — synthesis.md |
| software-is-incrementally-safe | private | Lean 4 proof that safety is preserved incrementally across releases, with security consequences (noninterference, monotone capability shrinkage), built on software-is-composable. | 97e55d28 | 2026-11-18 |  | proof family — synthesis.md |
| software-is-quantifiable | public | Lean 4 formalization of the qualification-of-software claims: finiteness, witness fold correctness, snapshot coloring, Pareto ordering, coverage premise — each proven, disproven, open, or named as a premise. |  d88acbdc  | 2026-11-18 |  | proof family — synthesis.md |
| software-is-solvable | private |  |  3053b78d  | 2026-11-18 |  | proof family — synthesis.md |
| software-optimality | private | Machine-checked foundations for qualification closure, compounding evidence, and finite Pareto frontiers. | 95df5fb7 | 2026-11-18 |  | proof family — synthesis.md |
| solo-provisioner | private |  | 675b3315 | 2025-10-09 |  | unknown (unexamined) |
| station8-landing | private |  | 3bf54e24 | 2022-07-22 |  | unknown (unexamined) |
| std | private |  | ae782739 | 2023-06-12 |  | unknown (unexamined) |
| stex | public |  | empty | 2022-05-22 | no commits | unknown (unexamined) |
| str | public |  | d1425650 | 2024-01-31 |  | unknown (unexamined) |
| sugfr | private |  | 76c6765a | 2022-06-26 |  | unknown (unexamined) |
| suvr | public |  | 65aaac69 | 2023-03-06 |  | unknown (unexamined) |
| svelte | private |  | 9ed94b6f | 2020-02-10 |  | unknown (unexamined) |
| svelte-kit | public |  | de778b19 | 2022-06-12 |  | unknown (unexamined) |
| svendless | public | on a mission to make a truly endless clicker with generative visualization and text feedback to work on in my spare time and to kindle tangential logic ideas for other projects | 4fb2f33e | 2022-12-05 |  | unknown (unexamined) |
| sycmre | public | A reactive library for creating web apps in Rust and WebAssembly | c8deaeef | 2022-06-23 | fork | unknown (unexamined) |
| termi.vim | public | simple terminal toggle vim plugin | 68e7c978 | 2022-03-23 |  | unknown (unexamined) |
| termlx | public | Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React | c8e70393 | 2026-06-07 | fork | unknown (unexamined) |
| thebook | public | The book about development with Yew framework | ee5f6f0a | 2026-11-18 | fork | unknown (unexamined) |
| threev-db | public | rudimentary attempts at distributed knowledge base db | d2be272e | 2021-12-11 |  | unknown (unexamined) |
| tmx | public |  | empty | 2026-06-07 | no commits | unknown (unexamined) |
| tn1 | private |  | 03540fa4 | 2021-12-09 |  | unknown (unexamined) |
| tonic-example | public | Minimal example of using Tonic for client/server gRPC | 7fb829fc | 2021-09-20 | fork | unknown (unexamined) |
| took | public |  | 16133882 | 2026-03-27 | fork | unknown (unexamined) |
| tree-sitter-duo | private |  | 08d84fdc | 2026-11-18 |  | unknown (unexamined) |
| tuirl | public | tuiroguelike | a355cfa9 | 2026-11-18 |  | unknown (unexamined) |
| tw | private |  | e0016b8f | 2021-12-10 |  | unknown (unexamined) |
| tx | private |  | empty | 2026-06-07 | no commits | unknown (unexamined) |
| txauth | private |  | d130086a | 2026-10-23 |  | unknown (unexamined) |
| voile-rs | public | Dependently-typed row-polymorphic programming language, evolved from minitt-rs | 70fa4a1a | 2026-11-18 | fork | unknown (unexamined) |
| vscode-duo | public |  | e3e51602 | 2026-06-19 |  | unknown (unexamined) |
| VSEPR-Encoding-Doc | public |  | d6418ab3 | 2026-11-18 |  | unknown (unexamined) |
| vtrl-web | private |  | 32808b1c | 2021-04-17 |  | unknown (unexamined) |
| vue | private |  | 1712130f | 2020-02-10 |  | unknown (unexamined) |
| vuepress | private |  | 476ae4a4 | 2020-02-09 |  | unknown (unexamined) |
| wac | public | Single-file memory layer for AI agents, sub mili-second RAG on Apple Silicon. Metal Optimized On-Device. No Server. No API. One File. Pure Swift | 62213b82 | 2026-05-19 | fork | unknown (unexamined) |
| ward | private |  | 74c5d115 | 2026-08-08 |  | unknown (unexamined) |
| wart | private | webassembly runtime | d20fe9d9 | 2026-11-10 |  | unknown (unexamined) |
| wasm-bindgen | public | Facilitating high-level interactions between Wasm modules and JavaScript | cbcf3e78 | 2022-05-31 | fork | unknown (unexamined) |
| wasm-blog | public | working on making a md->blog pipeline for wasm | 0a61f5b8 | 2026-11-18 |  | unknown (unexamined) |
| wasmlane | private |  | bcc14e2f | 2026-11-18 |  | unknown (unexamined) |
| wax | private |  | fa702355 | 2026-05-23 |  | unknown (unexamined) |
| web | private |  | 5a2fab6c | 2022-02-08 |  | unknown (unexamined) |
| webv | private |  | 41b7b82d | 2022-02-08 |  | unknown (unexamined) |
| wide-weight-explorer | public | Wide weight-space explorer prototype: weights, premises, and exact retraction cones over a mock session | dec1a454 | 2026-11-10 |  | unknown (unexamined) |
| word-vscode | public | word.lua in vscode | 14c6d0c0 | 2024-12-04 |  | unknown (unexamined) |
| wt | public |  | cd82d528 | 2024-10-08 |  | unknown (unexamined) |
| wwp | private |  | 021c3322 | 2024-11-04 |  | unknown (unexamined) |
| wx | private | Zig WebAssembly runtime (in progress) | dc28f623 | 2026-01-04 |  | unknown (unexamined) |
| wxc | private |  | a0438e80 | 2025-11-05 |  | unknown (unexamined) |
| xx | public | tuiroguelike | aab2f7d0 | 2026-11-18 |  | unknown (unexamined) |
| z | public |  | empty | 2024-03-15 | no commits | unknown (unexamined) |
| zai | private | The Idol toolchain: a from-scratch native compiler with its own ARM64 and x86-64 encoders and Mach-O writer, an e-graph optimizer, a frozen 12-language benchmark harness, and the first three toolchain components reimplemented in Idol itself. | d74481bd | 2026-09-24 |  | unknown (unexamined) |
| zbc | public |  | be1bc914 | 2026-11-18 |  | unknown (unexamined) |
| zed-duo | private |  | f79855c5 | 2026-06-19 |  | unknown (unexamined) |
| zig | public | General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. | 0772fb05 | 2022-01-06 | fork | unknown (unexamined) |
| zig-wlroots | public | Zig bindings for wlroots | 0c3165f4 | 2023-01-24 | fork | unknown (unexamined) |
| zig.vim | public | Vim configuration for Zig | 29ceb122 | 2022-01-17 | fork | unknown (unexamined) |
| zpkg | public |  | d6c1c767 | 2026-11-18 |  | unknown (unexamined) |

| idol-theses | public | The falsifiable theses of the Idol program, formalized in Lean at their strongest reachable forms, each with the observation that would refute it |  c443ebe1  | 2026-11-18 |  | proof family — sweep placements |
| software-benchmarking-is-redundant-and-suboptimal | private |  |  a85286ac  | 2026-11-18 |  | proof family — sweep placements |
| software-compilers-lose-info | private | The full proof of Idol's topological thesis: conventional compilation provably loses the derivation structure; derivation-carrying compilation loses nothing. |  69358971  | 2026-11-18 |  | proof family — sweep placements |
| software-fuzzing-is-suboptimal | private |  |  6ed7a596  | 2026-11-18 |  | proof family — sweep placements |
| software-is-a-closed-loop | public | The closed loop of software qualification: a continuous synthesis of the clpi software proof repos, hosting the live paper, the structural implications, and the next steps. | b07314d3 | 2026-11-18 |  | proof family — sweep placements |
| software-is-more-traceable-than-you-think | private | The historical witness hypergraph of software at symbol grain: exact time, order independent, with a Lean proof that it holds independent of operating system, software, and language. |  8f6a1280  | 2026-11-18 |  | proof family — sweep placements |
| software-testing-is-redundant | private |  |  18feb7ab  | 2026-11-18 |  | proof family — sweep placements |
