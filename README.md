# software-is-a-closed-loop

A continuous synthesis of the clpi software proof estate, the
live paper of the qualification of software, the structural
implications of the construction, and the ordered next steps —
kept current by machinery, not by intention.

Created 2026-11-18 under Chris's directive: "Create
software-is-a-closed-loop synthesizing all of the software*
proofs continuously and hosting the live paper and all
structural implications and next steps." The scope widened the
same night to all of the repos: every repo in the estate
appears in the census, and the nine landed software proof
repos (plus a tenth announced) receive theorem-level
synthesis.

## The closed loop, in one paragraph

Named software and named criteria are the only external
inputs. Qualification colors the finite behavior space the
names determine. Executions append witnesses to an append-only
ledger. A fold — associative, commutative, idempotent —
accounts the witnesses, so the accounting is a pure function
of the surviving witness set. Bounds and a Pareto frontier are
derived from the accounting. Improvement candidates are
generated, qualified under the same criteria, and measured
against the frontier. An accepted improvement re-enters as the
named software at a new pin and is requalified. Every stage's
inputs are the previous stage's outputs; the loop closes
because requalification is the same qualification, applied to
the new pin. The full statement, with every theorem of the
proof estate placed at its stage, is in synthesis.md.

## What is in this repo

- README.md — this file: what the repo is, its evidence
  discipline, and the synthesis pins.
- synthesis.md — the closed loop stated precisely, and every
  theorem of the proof repos placed in it: name, statement,
  pin, axiom dependencies, loop stage. Duplicated claims cite
  the stronger home. The composed claim is stated as a
  composed claim, with its parts' states, never above its
  evidence.
- census/ — the theorem-level census files the synthesis was
  built from, one per proof repo, carried verbatim as the
  evidence annex.
- census.md — the estate census: all 558 repos of the clpi
  estate, each with what it is, its role in the loop, its head
  pin, and its evidence state. Unexamined repos are colored
  unknown — the construction applied to the estate itself.
- paper.html — the live paper, "a proposal for the
  qualification of software", hosted verbatim from its source
  of record with a host note. PAPER-SYNC.md names the source,
  its revision, and the sync rule.
- implications.md — the structural implications: every
  consequence the proofs and the construction carry, each with
  what it follows from and its evidence state.
- next-steps.md — the open work, ordered, each step with an
  owner and a closing condition. Nothing is listed without a
  closing condition.
- resynthesis.md — the synthesis procedure: how a
  re-synthesis is produced when a source head moves.
- proof-strength.md — the proof-strength ledger for the
  proof family: per repo at its current pin, claims proven,
  claims on named premises, claims absent, controls in tree,
  and gate state — refreshed on every re-synthesis, with two
  defect rules (a shrinking proven set, or a pin that moves
  without the ledger moving, is flagged in the run record).
- synthesis-pins.json — the machine-readable pins: every
  censused repo's head at this synthesis, and for the proof
  repos the pin the census was read at. The continuous job
  diffs live heads against this file.

## Evidence discipline

Four states, never blurred: settled intent, proposed,
implemented, verified. Inside the proof estate the working
words are: proven (a Lean-checked proof at a named pin, with
axiom dependencies named), premise (named and carried as an
argument, never counted proven), proposed (a stated design
with no proof yet), refuted (disproven, with the disproof
checked or executed), asserted (a claim with neither spec nor
proof — a work order, not a result), and unknown (unexamined).
A claim sits no higher than its evidence. Where a source repo
states a boundary — a non-claim — the synthesis carries the
boundary with the claim.

Pins: every placement names the pin it was read at. Heads
moved repeatedly on the night this synthesis was made; where
a repo's head at synthesis differs from the pin its census was
read at, both are recorded, and the difference is the
continuous job's first re-synthesis input.

## Synthesis pins (2026-11-18, first synthesis)

Proof repos — census pin / head at synthesis:

- software-is-quantifiable (public, Lean 4.15.0): census
  37917a4195efb1d0423a422ee954d767a9be1cd3 / head
  ba27febf48c85bccaaccbace7cc3faba5eff879c
- software-optimality (private, Lean 4.19.0): census
  0ea4626b7806e9c53e9e742fde6a7d542fb85ee3 / head
  aab49084e30757f39c7f9d7e4403522abf5ce46f
- software-is-composable (private, Lean 4.19.0): census and
  head 033c12c01299a9b28983bee410c230641adc7d1e
- software-is-incrementally-certifiable (private): census and
  head f3b9f896ac76a95e7104c98af66e41413e7e5b2d (readme only
  at head; see synthesis.md)
- software-is-incrementally-safe (private, Lean 4.19.0):
  head 9466135815aa80e714d2a6999fd0aa8807375ff3 (toolchain
  file only at head); proof content censused on the unmerged
  pull-request branch at
  5c1006a6ae6ee41a4bc19247db3a95589f5a3e9e
- software-doesnt-have-to-regress (private): census and head
  24d36c13414867e59ae67ccf47f83cc250ce55af (readme only)
- software-doesnt-need-review (private): census and head
  ae5f3918f7689267d07044a00e6a11b071510bba (readme only)
- software-is-solvable (private, Lean 4.19.0): census and
  head 815e125f6c7fd982cd5a66c4c1f98aa0a4ea5d33
- software-frontier-is-solvable (private, Lean 4.19.0):
  census and head c7ffc6d03e8bc4f795afcae983ee6bb3533a4e69
- software-is-more-traceable-than-you-think: announced
  2026-11-18, not yet landed when this synthesis was made
  (read back 2026-11-18 01:32 PST: no such repo). It enters
  the census on the continuous job's next re-enumeration.

Estate: 558 repos enumerated completely (249 public, 309
private) through the authenticated listing, past the 300-repo
public cap; every head read individually. Full pins in
synthesis-pins.json; placements in census.md.

Sweep update (2026-11-18, later the same night): the estate
was re-enumerated at 565 repos (251 public, 314 private) and
swept by content for provable results, under the ruling that
the accounting is estate-wide and determined by content, not
by name. Twenty repos are proof-bearing and censused in the
annex: the nine above at refreshed pins (quantifiable
f3709926, optimality b52c3170, composable a3058ba6,
certifiable c9ffd49a, safe head 8ad1dd26, regress c36829da,
review 40b1e885, solvable 5bbceee7, frontier 6a41c7be), plus
software-compilers-lose-info f531e31a,
software-is-more-traceable-than-you-think 4420fb1e,
idol-theses d207be6e, software-testing-is-redundant 66f65b6f,
software-fuzzing-is-suboptimal 18d9569b,
software-benchmarking-is-redundant-and-suboptimal 4314a181,
idol-semi and semi-persistent 508d7c66 (one tree, one pin),
premise-retraction-playground 47f469a4, idol 561cf395
(proof-bearing content only), and this repo at d8047804 (its
own checked example). The other 465 non-empty repos are
determined proof-free by the content check named in
census.md; the 80 empty repos carry none. Five repos moved
again during the sweep (optimality, composable, traceability,
idol-theses, idol); their live heads are recorded in
census.md and synthesis-pins.json, and re-census is owed.

## Keeping current

A scheduled job under the idol-autonomous-work-loop goal
re-enumerates the estate, diffs every censused head against
synthesis-pins.json, and on any movement runs the procedure
in resynthesis.md and commits the result with both pins named
in the commit message. It is silent when nothing moved and
reports only a landed re-synthesis or a failure. Its job id
is recorded in the lane record,
~/workspace/research/software-closed-loop-2026-11-18.md.

Second watch update (2026-11-18, later the same night): the
estate was re-enumerated a third time at 565 repos, every
head read individually with no errors. Twenty repos had
moved, none were new or gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. Fifteen proof repos moved and every
one gained declarations with no name lost: the certifiable
repo landed its library at its head (fresh head 36901673,
census pin c9ffd49a, re-census owed), the safe repo landed
its library at its head (enumeration head dafd79a4, census
pin 8ad1dd26, re-census owed), a coordinated range example
landed across eleven proof repos and in this repo, and the
optimality, frontier, quantifiable, and theses repos gained
library modules beside it. This repo's own census pin moved
to d558669b on a full re-census of its new range example
(its proven count is now eleven). All other census pins
stand with re-census owed at the fresh heads recorded in
the pins file.

Third watch update (2026-11-18, later the same night): the
estate was re-enumerated a fourth time at 565 repos, every
head read individually with no errors. Thirty-six repos had
moved, none were new or gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. Five proof repos moved: the
optimality repo gained eleven Lean files and 52 names with
none lost (fresh head 95df5fb7, census pin b52c3170,
re-census owed); the safe repo gained 17 names with none
lost (fresh head 23a22552, census pin 8ad1dd26, re-census
owed); the composable repo held its count and its name set,
its movement a dependency re-pin (fresh head 7b174646,
census pin a3058ba6); the idol repo's frontier file is
unchanged, while a release tools Lean development in its
tree grew by nine declarations across two files (fresh head
2f44b4fe, census pin 561cf395, a full census of that
development owed); and this repo's own eleven theorems stand
unchanged at the head the second watch landed. All census
pins stand with re-census owed at the fresh heads recorded
in the pins file.

Fourth watch update (2026-11-18, later the same night): the
estate was re-enumerated a fifth time at 565 repos, every
head read individually with no errors. Eighty-eight repos
had moved, none were new or gone, and the paper source hash
was unchanged at the value recorded in the sync note, so no
paper re-sync was owed. Three proof repos moved: the safe
repo gained three names with none lost and discharged its
string cone hypothesis by proof (fresh head 97e55d28,
census pin 8ad1dd26, re-census owed); the idol repo gained
a new Lean development of ten theorems in its solver
benchmarks while its frontier and release tools files stand
byte-identical (fresh head 107e52a9, census pin 561cf395, a
full census of the new development owed); and this repo's
own eleven theorems stand unchanged at the head one ledger
addendum past the third watch landing. All census pins
stand with re-census owed at the fresh heads recorded in
the pins file.

Fifth watch update (2026-11-18, later the same night): the
estate was re-enumerated a sixth time at 565 repos, every
head read individually with no errors. Six repos had
moved, none were new or gone, and the paper source hash
was unchanged at the value recorded in the sync note, so
no paper re-sync was owed. Two proof repos moved without
any change to their proof content: the idol repo's
movement is compiler and gate work with every Lean file
byte-identical (fresh head 586ff5a1, census pin 561cf395,
re-census owed), and the semi repo gained ten files of
analysis and parity tooling with every Lean and Rust
file unchanged (fresh head 238717ba, census pin 508d7c66,
re-census owed) — its mirror did not move, so the two
heads have diverged while their proof content remains
identical. Three further idol-family repos moved and
remain proof-free by the named check, and this repo's
own eleven theorems stand unchanged at the head the
fourth watch landed. All census pins stand with
re-census owed at the fresh heads recorded in the pins
file.

Sixth watch update (2026-11-18, later the same night): the
estate was re-enumerated a seventh time at 565 repos,
every head read individually with no errors. Two repos
had moved, none were new or gone, and the paper source
hash was unchanged at the value recorded in the sync
note, so no paper re-sync was owed. One proof repo
moved: this repo itself, whose head moved only by the
fifth watch landing — its four commits carry no Lean
change, so its own eleven theorems stand unchanged
(fresh head 97d26e80, census pin d558669b). One further
idol-family repo moved, the compiler port, and remains
proof-free by the named check (fresh head c374ef1c).
All census pins stand with re-census owed at the fresh
heads recorded in the pins file.

Seventh watch update (2026-11-18, later the same night): the
estate was re-enumerated an eighth time at 565 repos,
every head read individually with no errors. Three repos
had moved, none were new or gone, and the paper source
hash was unchanged at the value recorded in the sync
note, so no paper re-sync was owed. One proof repo
moved: this repo itself, whose head moved only by the
sixth watch landing — its four commits carry no Lean
change, so its own eleven theorems stand unchanged
(fresh head b07314d3, census pin d558669b). Two further
idol-family repos moved, the compiler port and the
relay, and remain proof-free by the named check (fresh
heads e3d52654 and 49c2e75d). All census pins stand
with re-census owed at the fresh heads recorded in the
pins file.

Eighth watch update (2026-11-18, later the same night): the
estate was re-enumerated a ninth time at 565 repos, every
head read individually with no errors in the final reads.
Four repos had moved, none were new or gone, and the paper
source hash was unchanged at the value recorded in the
sync note, so no paper re-sync was owed. One proof repo
moved: this repo itself, whose head moved only by the
seventh watch landing — its four commits carry no Lean
change, so its own eleven theorems stand unchanged (fresh
head 22957bf6, census pin d558669b). Three further
idol-family repos moved, the compiler port, the relay, and
the sites repo, and remain proof-free by the named check
(fresh heads 656d8e83, 7dfc975e, and 210289e7); the paper
page file in the sites repo is unchanged between its two
heads. All census pins stand with re-census owed at the
fresh heads recorded in the pins file.

Ninth watch update (2026-11-18, later the same night): the
estate was re-enumerated a tenth time at 565 repos, every
head read individually with no errors. Two repos had
moved, none were new or gone, and the paper source hash
was unchanged at the value recorded in the sync note, so
no paper re-sync was owed. One proof repo moved: this
repo itself, whose head moved only by the eighth watch
landing — its four commits carry no Lean change, so its
own eleven theorems stand unchanged (fresh head 2fe3ad5f,
census pin d558669b). One further idol-family repo moved,
the compiler port, and remains proof-free by the named
check (fresh head 2962acdf). All census pins stand with
re-census owed at the fresh heads recorded in the pins
file.

Tenth watch update (2026-11-18, later the same night): the
estate was re-enumerated an eleventh time at 565 repos,
every head read individually with no errors. Three repos
had moved, none were new or gone, and the paper source
hash was unchanged at the value recorded in the sync note,
so no paper re-sync was owed. One proof repo moved: this
repo itself, whose head moved only by the ninth watch
landing — its four commits carry no Lean change, so its
own eleven theorems stand unchanged (fresh head 10a786e7,
census pin d558669b). Two further idol-family repos moved,
the compiler port and the relay, and both remain
proof-free by the named check (fresh heads cbd2f797 and
673b7781). All census pins stand with re-census owed at
the fresh heads recorded in the pins file.

Eleventh watch update (2026-11-18, later the same night): the
estate was re-enumerated a twelfth time at 565 repos,
every head read individually with no errors. Three repos
had moved, none were new or gone, and the paper source
hash was unchanged at the value recorded in the sync note,
so no paper re-sync was owed. One proof repo moved: this
repo itself, whose head moved only by the tenth watch
landing — its four commits carry no Lean change, so its
own eleven theorems stand unchanged (fresh head ba9a0763,
census pin d558669b). Two further idol-family repos moved,
the compiler port and the relay, and both remain
proof-free by the named check (fresh heads 0f176306 and
9b20b353). All census pins stand with re-census owed at
the fresh heads recorded in the pins file.

Twelfth watch update (2026-11-18, later the same night): the
estate was re-enumerated a thirteenth time at 565 repos,
every head read individually (three first reads failed and
were re-read individually: two to matching heads, one to
its recorded empty state). Two repos had moved, none were
new or gone, and the paper source hash was unchanged at
the value recorded in the sync note, so no paper re-sync
was owed. One proof repo moved: this repo itself, whose
head moved only by the eleventh watch landing — its four
commits carry no Lean change, so its own eleven theorems
stand unchanged (fresh head 8050b17f, census pin d558669b).
One further idol-family repo moved, the compiler port, and
it remains proof-free by the named check (fresh head
868a4044). All census pins stand with re-census owed at
the fresh heads recorded in the pins file.

Thirteenth watch update (2026-11-18, later the same night): the
estate was re-enumerated a fourteenth time at 565 repos,
every head read individually with no read errors. Three
repos had moved, none were new or gone, and the paper
source hash was unchanged at the value recorded in the
sync note, so no paper re-sync was owed. One proof repo
moved: this repo itself, whose head moved only by the
twelfth watch landing — its four commits carry no Lean
change, so its own eleven theorems stand unchanged (fresh
head 6a0c90d3, census pin d558669b). Two further
idol-family repos moved, the compiler port and the relay,
and both remain proof-free by the named check (fresh
heads e2e72ce5 and 21dd9105). All census pins stand with
re-census owed at the fresh heads recorded in the pins
file.

Fourteenth watch update (2026-11-18, later the same night): the
estate was re-enumerated a fifteenth time at 565 repos,
every head read individually with no read errors. Two
repos had moved, none were new or gone, and the paper
source hash was unchanged at the value recorded in the
sync note, so no paper re-sync was owed. One proof repo
moved: this repo itself, whose head moved only by the
thirteenth watch landing — its four commits carry no Lean
change, so its own eleven theorems stand unchanged (fresh
head 97920cbd, census pin d558669b). One further
idol-family repo moved, the compiler port, and it remains
proof-free by the named check (fresh head c797c1b8). All
census pins stand with re-census owed at the fresh heads
recorded in the pins file.

Fifteenth watch update (2026-11-18, later the same night): the
estate was re-enumerated a sixteenth time at 566 repos,
every head read individually (one first read failed on a
transport error and was re-read to its recorded empty
state). Three repos had moved, one was new, none were
gone, and the paper source hash was unchanged at the value
recorded in the sync note, so no paper re-sync was owed.
One proof repo moved: this repo itself, whose head moved
only by the fourteenth watch landing — its four commits
carry no Lean change, so its own eleven theorems stand
unchanged (fresh head fe96c58f, census pin d558669b). The
new repo is a proof repo, the profiling proof repo, entered
and censused at theorem level at its head (a53c4bf5, its
census pin): twenty declarations, three controls, and a
recorded gate log passing at the head, with one carried
premise and its proposed and open items at its own stated
states. Two further idol-family repos moved, the compiler
port and the relay, and both remain proof-free by the named
check (fresh heads 12110aae and 08af9acc). All other census
pins stand with re-census owed at the fresh heads recorded
in the pins file.

Sixteenth watch update (2026-11-18, later the same night): the
estate was re-enumerated a seventeenth time at 566 repos,
every head read individually with no read errors. Two
repos had moved, none were new or gone, and the paper
source hash was unchanged at the value recorded in the
sync note, so no paper re-sync was owed. One proof repo
moved: this repo itself, whose head moved only by the
fifteenth watch landing — its five commits carry no Lean
change, so its own eleven theorems stand unchanged
(fresh head c0356504, census pin d558669b). One further
idol-family repo moved, the compiler port, and it remains
proof-free by the named check (fresh head e86c5e3e). All
census pins stand with re-census owed at the fresh heads
recorded in the pins file.

Seventeenth watch update (2026-11-18, later the same night):
the estate was re-enumerated an eighteenth time at 566
repos, every head read individually with no read errors.
Three repos had moved, none were new or gone, and the paper
source hash was unchanged at the value recorded in the sync
note, so no paper re-sync was owed. One proof repo moved:
this repo itself, whose head moved only by the sixteenth
watch landing — its four commits carry no Lean change, so
its own eleven theorems stand unchanged (fresh head
a7be4e02, census pin d558669b). Two further idol-family
repos moved, the compiler port and the relay, and both
remain proof-free by the named check (fresh heads 2bcabb50
and ebd89b3f). All census pins stand with re-census owed at
the fresh heads recorded in the pins file.

Eighteenth watch update (2026-11-18, later the same night):
the estate was re-enumerated a nineteenth time at 566
repos, every head read individually with no read errors.
Two repos had moved, none were new or gone, and the paper
source hash was unchanged at the value recorded in the sync
note, so no paper re-sync was owed. One proof repo moved:
this repo itself, whose head moved only by the seventeenth
watch landing — its four commits carry no Lean change, so
its own eleven theorems stand unchanged (fresh head
30513d21, census pin d558669b). One further idol-family
repo moved, the compiler port, and it remains proof-free
by the named check (fresh head 763765c6). All census pins
stand with re-census owed at the fresh heads recorded in
the pins file.

Nineteenth watch update (2026-11-19): the estate was
re-enumerated a twentieth time at 566 repos, every head
read. Three repos had moved, none were new or gone, and
the paper source hash was unchanged at the value recorded
in the sync note, so no paper re-sync was owed. One proof
repo moved: this repo itself, whose head moved only by
the eighteenth watch landing — its four commits carry no
Lean change, so its own eleven theorems stand unchanged
(fresh head 2aac8180, census pin d558669b). Two further
idol-family repos moved, the compiler port and the relay,
and both remain proof-free by the named check (fresh heads
c2fa1ada and 2ab0e5bd). All census pins stand with
re-census owed at the fresh heads recorded in the pins
file.

Twentieth watch update (2026-11-19): the estate was
re-enumerated a twenty-first time at 567 repos, every head
read individually, no read errors. Two repos had moved, one
was new, none were gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. One proof repo moved: this repo
itself, whose head moved only by the nineteenth watch
landing — its four commits carry no Lean change, so its own
eleven theorems stand unchanged (fresh head ec47f7e, census
pin d558669b). The new repo is a proof repo, the losses
proof repo, entered and censused at theorem level at its
head (d1159dc1, its census pin): seventeen declarations,
three controls, and a recorded gate log passing at the
head, with two named premises and its proposed items at its
own stated states. One further idol-family repo moved, the
compiler port, and it remains proof-free by the named check
(fresh head 4411fbe4). All census pins stand with re-census
owed at the fresh heads recorded in the pins file.
Twenty-first watch update (2026-11-19): the estate was
re-enumerated a twenty-second time at 569 repos, every head
read individually, no read errors. Four repos had moved,
two were new, none were gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. Two proof repos moved: this repo
itself, whose head moved only by the twentieth watch
landing — its five commits carry no Lean change, so its own
eleven theorems stand unchanged (fresh head f2c3b6d, census
pin d558669b); and the losses repo, which gained one
theorem, the tightness of its compounding bound, with no
name lost — re-censused in full at its fresh head in this
pass (fresh head 12ee66e9, its new census pin). One new
repo is a proof repo, the persistence proof repo, entered
and censused at theorem level at its head (eb01cf2e, its
census pin): fifty-three declarations, four controls
beside a general no-derivation result, and a recorded gate
log passing at the head, with two campaign premises and
its proposed items at its own stated states. The second
new repo, the bidirectional repo, stands empty at its
first enumeration, accounted as carrying no provable
results and colored unknown. Two further idol-family repos
moved, the compiler port and the relay, and both remain
proof-free by the named check (fresh heads ba59a3e6 and
c560a390). All other census pins stand with re-census owed
at the fresh heads recorded in the pins file.
Twenty-second watch update (2026-11-19): the estate was
re-enumerated a twenty-third time at 569 repos, every head
read individually, no read errors. Seven repos had moved,
none were new, none were gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. Three proof repos moved: this repo
itself, whose head moved only by the twenty-first watch
landing — its six commits carry no Lean change, so its own
eleven theorems stand unchanged (fresh head 3baddd4, census
pin d558669b); the theses repo, which gained fourteen
theorems and lost none — two new native modules of
composition glue and a rewrite composer, a third cited group
growing its cited tranche from seventeen theses to
thirty-four, and a campaign document (fresh head b6e810c);
and the frontier repo, which gained thirty-eight theorems
and lost none, all in one new search module proving the
general search layer of its bounded technique, with a
recorded check log at its fresh head (fresh head cdeae4a).
One repo that stood empty at the last enumeration landed
its first content and is a proof repo, the bidirectional
proof repo, entered and censused at theorem level at its
head (b14fc92b, its census pin): seventy-three theorems,
four controls, and a recorded gate log passing at the head,
with six named premises under its joined theorem and its
proposed items at its own stated states. Three further
idol-family repos moved, the library, the relay, and the
sites repo, and all remain proof-free by the named check
(fresh heads f01da7a, 4fdbf2e, and 4de6ab6). All other census
pins stand with re-census owed at the fresh heads recorded
in the pins file.
Twenty-third watch update (2026-11-19): the estate was
re-enumerated a twenty-fourth time at 569 repos, every head
read individually, no read errors. Five repos had moved,
none were new, none were gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. One proof repo moved: this repo
itself, whose head moved only by the twenty-second watch
landing — its five commits carry no Lean change, so its own
eleven theorems stand unchanged (fresh head b0fd67d, census
pin d558669b). One moved repo carries proof content for the
first time, the library repo, which landed the Redundant
campaign in ten commits — a 25-theorem proof kernel with a
recorded, hash-bound kernel-checked receipt and five
recorded negative controls, a 13-theorem atlas development,
and six witness examples checked by decision — entered and
censused at theorem level at its head (ad22a681, its census
pin), its tree at the last recorded head re-verified
proof-free in this pass. Three further idol-family repos
moved, the compiler port, the relay, and the sites repo, and
all remain proof-free by the named check (fresh heads
d4622612, 7f5bd08b, and 4544afac). All other census pins
stand with re-census owed at the fresh heads recorded in the
pins file.
Twenty-fourth watch update (2026-11-19): the estate was
re-enumerated a twenty-fifth time at 569 repos, every head
read individually, no read errors. Three repos had moved,
none were new, none were gone, and the paper source hash was
unchanged at the value recorded in the sync note, so no
paper re-sync was owed. Two proof repos moved: this repo
itself, whose head moved only by the twenty-third watch
landing — its five commits carry no Lean change, so its own
eleven theorems stand unchanged (fresh head 91adf89, census
pin d558669b); and the library repo, which landed its Pareto
release condition in three commits — a new 27-theorem proof
package proving Pareto unimprovability in its abstract
models, with a recorded, hash-bound kernel-checked receipt
and five recorded negative controls, its source and checker
hashes verified firsthand by this watch — re-censused at
theorem level at its head (4dee2311, its new census pin),
for sixty-five theorems in total with its earlier thirty-eight
unchanged. One further idol-family repo moved, the compiler
port, and it remains proof-free by the named check (fresh
head fc5d20bf). All other census pins stand with re-census owed
at the fresh heads recorded in the pins file.

Twenty-fifth watch update (2026-11-19): the estate was re-enumerated a twenty-sixth time at 569 repos, every head read individually, no read errors. Three repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the twenty-fourth watch landing — its five commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 52daadf5, census pin d558669b). Two further idol-family repos moved, the compiler port and the relay, and both remain proof-free by the named check (fresh heads 29d0b879 and 238d1f05). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Twenty-sixth watch update (2026-11-19): the estate was re-enumerated a twenty-seventh time at 569 repos, every head read individually, no read errors. One repo had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the twenty-fifth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 3d3bffdd, census pin d558669b). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Twenty-seventh watch update (2026-11-19): the estate was re-enumerated a twenty-eighth time at 569 repos, every head read individually, no read errors. Four repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the twenty-sixth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 4b801137, census pin d558669b). Three further idol-family repos moved, the compiler port, the relay, and the sites repo, and all remain proof-free by the named check (fresh heads 5d06bfd9, 7669d68e, and 3b6fc879); the paper page file in the sites repo is unchanged between its two heads. All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Twenty-eighth watch update (2026-11-19): the estate was re-enumerated a twenty-ninth time at 569 repos, every head read individually. Six first reads failed on transport stream errors; each was re-read individually and matched its last recorded head, or its recorded empty state, so the final reads carry no errors. Two repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the twenty-seventh watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head b2a74028, census pin d558669b). One further idol-family repo moved, the compiler port, and it remains proof-free by the named check (fresh head 079727c3). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Twenty-ninth watch update (2026-11-19): the estate was re-enumerated a thirtieth time at 569 repos, every head read individually, no read errors. Three repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the twenty-eighth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 47a30a1c, census pin d558669b). Two further idol-family repos moved, the compiler port and the relay, and both remain proof-free by the named check (fresh heads 133d7649 and ca5b9492). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirtieth watch update (2026-11-19): the estate was re-enumerated a thirty-first time at 569 repos, every head read individually, no read errors. Two repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the twenty-ninth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 4e9d508a, census pin d558669b). One further idol-family repo moved, the compiler port, and it remains proof-free by the named check (fresh head 24f96bd4). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-first watch update (2026-11-19): the estate was re-enumerated a thirty-second time at 569 repos, every head read individually, no read errors. Two repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the thirtieth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 2eee5466, census pin d558669b). One further idol-family repo moved, the relay, and it remains proof-free by the named check (fresh head b0a12620). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-second watch update (2026-11-19): the estate was re-enumerated a thirty-third time at 569 repos, every head read individually, no read errors. Two repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the thirty-first watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 5cc9c826, census pin d558669b). One further idol-family repo moved, the compiler port, and it remains proof-free by the named check (fresh head 207b6ac6). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-third watch update (2026-11-19): the estate was re-enumerated a thirty-fourth time at 569 repos, every head read individually, no read errors. One repo had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the thirty-second watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 4b34e16b, census pin d558669b). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-fourth watch update (2026-11-19): the estate was re-enumerated a thirty-fifth time at 570 repos, every head read individually, no read errors. Three repos had moved, one was new, none were gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. Two proof repos moved or entered: this repo itself, whose head moved only by the thirty-third watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head ab1531f9, census pin d558669b); and a new proof repo, the redundant compute repo, entered at its head 1ea28648, its census pin — thirty-seven theorems in four Lean files proving the redundancy measure monotone under expansion-only growth, superadditive over joins with a strict overlap unit, and witnessed redundancy persistent, with six standing controls, the universal form refuted in its tree, and a recorded gate log passing at the pin. Two further idol-family repos moved, the compiler port and the relay, and both remain proof-free by the named check (fresh heads 2a477f59 and 9811b46a). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-fifth watch update (2026-11-19): the estate was re-enumerated a thirty-sixth time at 572 repos, every head read individually, no read errors. Four repos had moved, two were new, none were gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. Three proof repos moved: this repo itself, whose head moved only by the thirty-fourth watch landing — its five commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 2df09d7b, census pin d558669b); and the frontier repo, which landed its candidate space in one commit — one new Lean file of twenty-three declarations with none lost, the solved set under a weighting epoch proved exactly the nondominated qualified set under that epoch's measures, with a recorded check log at its fresh head whose build ends in success (fresh head 60f33193, census pin standing with re-census owed). Two new repos are proof repos, entered and censused at theorem level at their heads, which are their census pins: the certification repo (4539760e) — nineteen theorems proving chain evidence covers the full check and a certificate checker honest about regression, one assembled control refuting endpoint-only comparison, and its first certificate artifact reading not certified; and the equivalence repo (14992281) — the redundant compute program re-founded on the canonical model, carried at skeleton strength: its specification and eight proposed claims stand at their stated states, its proof tree holds one seed declaration, and its recorded gate log passes at the pin. Two further idol-family repos moved, the perception harness repo and the relay, and both remain proof-free by the named check (fresh heads 036df3b3 and 769ad839). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-sixth watch update (2026-11-19): the estate was re-enumerated a thirty-seventh time at 572 repos, every head read individually, no read errors. Three repos had moved, none were new, none were gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the thirty-fifth watch landing — its seven commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head f93c5fcc, census pin d558669b). Two further idol-family repos moved, the compiler port and the relay, and both remain proof-free by the named check (fresh heads ab34a836 and 0b9328b5). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-seventh watch update (2026-11-19): the estate was re-enumerated a thirty-eighth time at 572 repos, every head read individually, no read errors. Three repos had moved, none were new, none were gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. Two proof repos moved: this repo itself, whose head moved only by the thirty-sixth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 944a8a13, census pin d558669b); and the equivalence repo, which landed its rebuild in five commits — the canonical model implemented in Lean, all eight claims of its specification proved, its five standing controls proved over concrete data, 217 declarations in eight Lean files, a recorded gate log at the fresh head passing its axiom subset check, beside an algorithm specification and case register carried as proposed and a built registry carried as measured — re-censused at theorem level at its head (37514fb7, its new census pin), with one flagged name loss: the skeleton seed fact is not restated, replaced by the model's own development as its annex records. One further idol-family repo moved, the compiler port, and it remains proof-free by the named check (fresh head 84209e99). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-eighth watch update (2026-11-19): the estate was re-enumerated a thirty-ninth time at 572 repos, every head read individually, no read errors. Three repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. Two proof repos moved: this repo itself, whose head moved only by the thirty-seventh watch landing — its five commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head 8a230cf9, census pin d558669b); and the semi repo, which moved by seventeen commits of dependency updates, a native Idol publication projection with refusal controls, a native role incidence view with replay controls, and a parity outcome folder — all 156 of its Lean files byte-identical between its census pin, its last recorded head, and its fresh head, and no Rust source file changed, so its proven set stands unchanged at 1,865 declarations by the watch method, with a passing gate at the fresh head still claimed, not proven (fresh head 0d730e5b, census pin standing with re-census owed). One further idol-family repo moved, the compiler port, and it remains proof-free by the named check (fresh head 94d2d852). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.

Thirty-ninth watch update (2026-11-19): the estate was re-enumerated a fortieth time at 572 repos, every head read individually, no read errors. Three repos had moved, none were new or gone, and the paper source hash was unchanged at the value recorded in the sync note, so no paper re-sync was owed. One proof repo moved: this repo itself, whose head moved only by the thirty-eighth watch landing — its four commits carry no Lean change, so its own eleven theorems stand unchanged (fresh head c123715b, census pin d558669b). Two further idol-family repos moved, the compiler port and the relay, and both remain proof-free by the named check (fresh heads 3bb939f2 and bb1bfac5). All other census pins stand with re-census owed at the fresh heads recorded in the pins file.
