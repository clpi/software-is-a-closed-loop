# Census — software-is-a-closed-loop (its own proof-bearing content)

## Pin and identity

- Live head (read in this sweep, 2026-11-18):
  `d8047804b335d197e17a8f1249321320a45009e9`
- Re-census pin (second watch, 2026-11-18):
  `d558669b7cf556bb1d9653e6432c895c3ceb6cfd` — the head the
  second watch fast-forwarded to and re-censused below.
- Visibility: public. Default branch: master.
- This repo is the synthesis host: the theorem statements it
  carries in its census annex are other repos' results, placed
  at their homes' pins, and are not counted again here. This
  annex censuses only the repo's own proof-bearing content.

## The checked example — three theorems, axiom-free

File: `examples/BatchTuning.lean`, added at the pin above in a
commit by the estate owner. A worked before-and-after example
of the loop's improvement step: a four-point size space over an
eight-record workload, a feasibility predicate against a cap, a
step rule that advances only to a feasible cheaper size, and a
bounded loop.

| Token | Hypotheses to conclusion | Axioms |
|---|---|---|
| one step | Premise: the current size is feasible under the cap. Conclusion: the stepped size is feasible and its call count is no greater. | none |
| fixed (optimum) | Premise: the start is feasible. Conclusion: the loop's winner after three steps is feasible, is a fixed point of the step rule, and no feasible size has a smaller call count. | none |
| before (and after) | The trace computes to the stated four sizes, with the stated call counts and the stated feasibility refusals beyond the caps. | none |

Evidence: the repo carries a verification record
(`examples/verification.txt`) — a run on Lean 4.19.0 with
warnings as errors via the repo's check script
(`examples/check.sh`), printing all three theorems as
depending on no axioms, and a rejected control: advancing to
the cheaper pin beyond the cap is refused (Lean exit 1).

State: PROVEN at the pin, axiom-free, with the run recorded in
the tree. The example is a demonstration instance of the
family's frontier and admission content at toy scale; it proves
nothing about any other repo and is counted only as itself.

## Re-census — 2026-11-18, the second hourly watch (pin d558669b)

One commit past the sweep pin added a second checked example
series: a range ledger case proving one verified range query
across four read catalogs. Its Lean file carries 8 theorem
declarations, no sorry token. The recorded verification
transcript in the tree prints axiom dependencies for seven
of the eight: six rest on subsets of the standard axioms
(propositional extensionality, classical choice, quotient
soundness), one depends on no axioms, and one — the exact
publication result — has no printed axiom line in the
transcript, so its axiom state is unrecorded. The transcript
also records a rejected control: removing the orientation
reversal in the integrated publisher is refused. The example
imports seven sibling modules from byte-verified offline
pins recorded in its own source bundle.

State: PROVEN in source at the pin, with the run recorded in
the tree, at the axiom states just named. This repo's own
proven count is now 11 theorems (the three of the first
example, axiom-free, plus these eight). Nothing else in the
repo is claimed.

## Watch delta — 2026-11-18, the third hourly re-synthesis watch

The watch re-read this repo's live head at 98761a1ae0f70eeda2edea25a790998dcdaaf323 in the full enumeration — the head the second watch landed. The theorem count is unchanged between the census pin d558669b7cf556bb1d9653e6432c895c3ceb6cfd and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between the two pins are the second watch placements, its ledger refresh, and its pins bump; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the fourth hourly re-synthesis watch

The watch re-read this repo's live head at 65914d1afe201c42897d17a05ff3299905912556 in the full enumeration — one ledger addendum commit past the head the third watch recorded. The theorem count is unchanged between the last recorded head 98761a1ae0f70eeda2edea25a790998dcdaaf323 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The one commit between them carries no Lean change. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the fifth hourly re-synthesis watch

The watch re-read this repo's live head at 68630ed9fab50cbce6ba1203bb0c3077826cfdcb in the full enumeration — the head the fourth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 65914d1afe201c42897d17a05ff3299905912556 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the fourth watch's own placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the sixth hourly re-synthesis watch

The watch re-read this repo's live head at 97d26e804c7e46693785bab042173ecee885ff73 in the full enumeration — the head the fifth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 68630ed9fab50cbce6ba1203bb0c3077826cfdcb and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the fifth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the seventh hourly re-synthesis watch

The watch re-read this repo's live head at b07314d3484ca1d14fae7de6bed2d7dc586c8251 in the full enumeration — the head the sixth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 97d26e804c7e46693785bab042173ecee885ff73 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the sixth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the eighth hourly re-synthesis watch

The watch re-read this repo's live head at 22957bf6ebd327d5dd2babeff2d8068b26e08749 in the full enumeration — the head the seventh watch landed with its pins bump. The theorem count is unchanged between the last recorded head b07314d3484ca1d14fae7de6bed2d7dc586c8251 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the seventh watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the ninth hourly re-synthesis watch

The watch re-read this repo's live head at 2fe3ad5f949852f88c4a07201a32425b6ba2f497 in the full enumeration — the head the eighth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 22957bf6ebd327d5dd2babeff2d8068b26e08749 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the eighth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the tenth hourly re-synthesis watch

The watch re-read this repo's live head at 10a786e74cece98f4e728fe560cd2e5edc9267e6 in the full enumeration — the head the ninth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 2fe3ad5f949852f88c4a07201a32425b6ba2f497 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the ninth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the eleventh hourly re-synthesis watch

The watch re-read this repo's live head at ba9a0763898bf0fab08771bb61d11453ba4b7dbb in the full enumeration — the head the tenth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 10a786e74cece98f4e728fe560cd2e5edc9267e6 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the tenth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the twelfth hourly re-synthesis watch

The watch re-read this repo's live head at 8050b17f83bf89dc0118a13dff2e7c0d86814454 in the full enumeration — the head the eleventh watch landed with its pins bump. The theorem count is unchanged between the last recorded head ba9a0763898bf0fab08771bb61d11453ba4b7dbb and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the eleventh watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the thirteenth hourly re-synthesis watch

The watch re-read this repo's live head at 6a0c90d36231383d19d71fc564162c7feb051e0a in the full enumeration — the head the twelfth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 8050b17f83bf89dc0118a13dff2e7c0d86814454 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the twelfth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the fourteenth hourly re-synthesis watch

The watch re-read this repo's live head at 97920cbdbc5770cb2aee1b49e1309bd30ba9f73e in the full enumeration — the head the thirteenth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 6a0c90d36231383d19d71fc564162c7feb051e0a and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the thirteenth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the fifteenth hourly re-synthesis watch

The watch re-read this repo's live head at fe96c58f321a75bc9ead1ac0388e65f354c0fe6a in the full enumeration — the head the fourteenth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 97920cbdbc5770cb2aee1b49e1309bd30ba9f73e and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The commits between them are the fourteenth watch's own annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the sixteenth hourly re-synthesis watch

The watch re-read this repo's live head at c03565047ca15e3a693b35d4bf40b813783f07ef in the full enumeration — the head the fifteenth watch landed with its pins bump. The theorem count is unchanged between the last recorded head fe96c58f321a75bc9ead1ac0388e65f354c0fe6a and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The five commits between them are the fifteenth watch's own census, annex, placement, ledger, and pins commits; no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-18, the seventeenth hourly re-synthesis watch

The watch re-read this repo's live head at
a7be4e024b5a41208dd44e76c14ba622eabe7eca in the full
enumeration — the head the sixteenth watch landed with its
pins bump. The theorem count is unchanged between the last
recorded head c03565047ca15e3a693b35d4bf40b813783f07ef and
that head: 11 declarations, the same name set at both,
counted by the watch method over the tree at each pin. The
four commits between them are the sixteenth watch's own
annex, placement, ledger, and pins commits; no Lean file
changed among them. This repo's own proven count stands at
eleven.

## Watch delta — 2026-11-18, the eighteenth hourly re-synthesis watch

The watch re-read this repo's live head at
30513d2180fb56cb802914b7f132d18d7b1e5a37 in the full
enumeration — the head the seventeenth watch landed with its
pins bump. The theorem count is unchanged between the last
recorded head a7be4e024b5a41208dd44e76c14ba622eabe7eca and
that head: 11 declarations, the same name set at both,
counted by the watch method over the tree at each pin. The
four commits between them are the seventeenth watch's own
annex, placement, ledger, and pins commits; no Lean file
changed among them. This repo's own proven count stands at
eleven.

## Watch delta — 2026-11-19, the nineteenth hourly re-synthesis watch

The watch re-read this repo's live head at
2aac8180e0aabc664519b9a696c5f372e609e779 in the full
enumeration — the head the eighteenth watch landed with its
pins bump. The theorem count is unchanged between the last
recorded head 30513d2180fb56cb802914b7f132d18d7b1e5a37 and
that head: 11 declarations, the same name set at both,
counted by the watch method over the tree at each pin. The
four commits between them are the eighteenth watch's own
annex, placement, ledger, and pins commits; no Lean file
changed among them. This repo's own proven count stands at
eleven.

## Watch delta — 2026-11-19, the twentieth hourly re-synthesis watch

The watch re-read this repo's live head at
ec47f7e42ad4f1438befdb7ab63af634d9e2fcaa in the full
enumeration — the head the nineteenth watch landed with
its pins bump. The theorem count is unchanged between the
last recorded head 2aac8180e0aabc664519b9a696c5f372e609e779
and that head: 11 declarations, the same name set at both,
counted by the watch method over the tree at each pin. The
four commits between them are the nineteenth watch's own
annex, placement, ledger, and pins commits; no Lean file
changed among them. This repo's own proven count stands at
eleven.
## Watch delta — 2026-11-19, the twenty-first hourly re-synthesis watch

The watch re-read this repo's live head at
f2c3b6d643bba02e90fb16381d20c9b891210e65 in the full
enumeration — the head the twentieth watch landed with
its pins bump. The theorem count is unchanged between
the last recorded head ec47f7e42ad4f1438befdb7ab63af634d9e2fcaa
and that head: 11 declarations, the same name set at
both, counted by the watch method over the tree at each
pin. The five commits between them are the twentieth
watch's own census, annex, placement, ledger, and pins
commits; no Lean file changed among them. This repo's
own proven count stands at eleven.

## Watch delta — 2026-11-19, the twenty-second hourly re-synthesis watch

The watch re-read this repo's live head at 3baddd446c91f7a8e4b1b815e1ac35110787b50d in the full enumeration — the head the twenty-first watch landed with its pins bump. The theorem count is unchanged between the last recorded head f2c3b6d643bba02e90fb16381d20c9b891210e65 and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The six commits between them are the twenty-first watch's own census, re-census, delta, placement, ledger, and pins commits; both Lean files are byte-identical between the heads, so no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-19, the twenty-third hourly re-synthesis watch

The watch re-read this repo's live head at b0fd67d9df66c8ba3bb8350feda54bc46444eb6c in the full enumeration — the head the twenty-second watch landed with its pins bump. The theorem count is unchanged between the last recorded head 3baddd446c91f7a8e4b1b815e1ac35110787b50d and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The five commits between them are the twenty-second watch's own census, annex, placement, ledger, and pins commits; both Lean files are byte-identical between the heads, so no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-19, the twenty-fourth hourly re-synthesis watch

The watch re-read this repo's live head at 91adf89e837d4616abf667b56c56b0d21bdca60e in the full enumeration — the head the twenty-third watch landed with its pins bump. The theorem count is unchanged between the last recorded head b0fd67d9df66c8ba3bb8350feda54bc46444eb6c and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The five commits between them are the twenty-third watch's own census, annex, placement, ledger, and pins commits; both Lean files are byte-identical between the heads, so no Lean file changed among them. This repo's own proven count stands at eleven.

## Watch delta — 2026-11-19, the twenty-fifth hourly re-synthesis watch

The watch re-read this repo's live head at 52daadf5336193594548850c23dd3a799c8eae2d in the full enumeration — the head the twenty-fourth watch landed with its pins bump. The theorem count is unchanged between the last recorded head 91adf89e837d4616abf667b56c56b0d21bdca60e and that head: 11 declarations, the same name set at both, counted by the watch method over the tree at each pin. The five commits between them are the twenty-fourth watch's own re-census, delta, placement, ledger, and pins commits; both Lean files are byte-identical between the heads, so no Lean file changed among them. This repo's own proven count stands at eleven.
