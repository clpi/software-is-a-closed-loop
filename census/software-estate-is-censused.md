# software-estate-is-censused — theorem census

Pin 1a67fef4d6d9bca33e41844f7f66d93678a96b65. Public.
The listing description states its claim in one line.
Censused by the eighty-sixth hourly re-synthesis watch
(2026-11-21), which found the repo new in the full
enumeration and read its whole tree at the pin (13 files,
not truncated) firsthand through the gh route: the spec,
the readme, the proof file, the audit file, the gate
script and its checker, the counting and mirroring
scripts, the pins snapshot, and the evidence file. The
determination is by content — Lean sources carrying
proved results — never by the name.

## The thesis, in plain English

The estate-wide accounting of provable results can be
maintained as an incremental derivation: a repo theorem
count is re-derived only when its own census pin moves,
and every other count is carried, and that maintenance
is exact — it agrees with a from-scratch census of the
same pins, on every repo, by proof and by experiment.

## What is proved

Five theorem declarations in one Lean file, at the
pinned toolchain named in the tree, no large library
dependency:

- The two point-update lemmas: an update at a repo
  gives the new value at that repo, and the old value
  at every other repo.
- Soundness (headline): one append step preserves the
  accounting exactly — recounting the stepped repo at
  its new pin and carrying every other count gives the
  from-scratch census of the stepped assignment.
- Steps (headline): every append sequence preserves
  the accounting exactly, by induction over the steps.
- Kept (headline): a repo no step touches keeps both
  its pin and its count.

The counting function is opaque in the proof, so the
equality holds for every declaration basis. Axiom
state, as the repo readme, spec, and audit file record
at the pin: soundness and steps depend on the two
standard principles named there (propositional
extensionality and quotient soundness); kept depends
on propositional extensionality alone. No escape token
stands in the tree as read.

State: PROVEN in source at the pin, at the recorded
strength below.

## Premises, named and not proved here

- Counting is by declaration at a named head, under the
  basis stated in full in the counter header. Both
  accountings share that counting function, so the
  comparison tests the maintenance, not the basis.
- The append-only property: a run moves a repo census
  pin or it does not, and nothing else about the repo
  changes between runs.

## The experiment

The incremental accounting ran beside closed-loop runs
81 through 83, the registered three, seeded from the
from-scratch census at run 80 close, with run 84 as a
fourth confirmatory step. Result, as recorded in the
spec and the evidence file: agreement on every repo in
all three registered runs and in the confirmatory step.
Across the window exactly one census pin moved — the
emergence repo at run 81 — and exactly that repo was
recounted, its count moving as recorded there, and the
other entries were carried. The counting basis is
calibrated at exact pins against recorded counts on
seven repos, named in the spec.

## Controls and gate

The gate script runs an escape scan, a cold build with
warnings as errors, and then the standing checker over
the landed evidence, which fails closed on the first
disagreement between the two accountings. Gate state:
the readme records the Lean gate cold green with
warnings as errors at the landing pin, with the audit
printing only the standard principles named above;
this watch read the sources and the evidence firsthand
and did not re-run the gate or the scripts — the
repo scripts were read as text only, never executed —
so the gate stands at recorded strength.

## What is not claimed

- One entry is uncountable, named in the open: the
  incrementally safe content branch repo does not
  resolve at its census pin, so both accountings carry
  it uncounted. That is a named exclusion, not an
  agreement on a number, and a from-scratch re-census
  cannot redo it either.
- The closed-loop watch has not switched to the
  incremental accounting yet. The switch is the
  development route remainder, in that program own
  landing stream.
- Counts at pins outside the window, and counts under
  any other basis, are not stated here.

The census pin is set to the fresh head on this first
proof census; the placements in the synthesis and the
ledger row are entered at the pin in this same pass.
