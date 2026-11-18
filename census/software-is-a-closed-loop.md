# Census — software-is-a-closed-loop (its own proof-bearing content)

## Pin and identity

- Live head (read in this sweep, 2026-11-18):
  `d8047804b335d197e17a8f1249321320a45009e9`
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
