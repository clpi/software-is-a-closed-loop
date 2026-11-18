# The re-synthesis procedure

How this repo stays current by machinery. The scheduled job
(next section) runs this procedure; a human or a lane running
it by hand follows the same steps. The procedure's invariant:
the synthesis never claims a pin it did not read, and a
re-synthesis touches only the placements the movement
affects.

## Inputs

- synthesis-pins.json in this repo: every censused repo's
  head at the last synthesis, and the proof repos' census
  pins.
- PAPER-SYNC.md: the paper source's path and MD5 at the last
  sync.
- The gh route (authenticated as the estate owner) for all
  GitHub reads.

## Steps

1. Re-enumerate the estate completely: the authenticated
  owner listing, paginated past the public cap, then every
  repo's head read individually — the same method as
  census.md. New repos enter the census here; a repo that
  vanished is recorded as vanished, never silently dropped.
2. Diff the fresh heads against synthesis-pins.json. Three
  sets: moved (head differs), new (no pin recorded), gone.
  Also recompute the paper source's MD5 against
  PAPER-SYNC.md.
3. If moved, new, and gone are all empty and the paper MD5
  is unchanged: stop. Say nothing. The job is silent when
  nothing moved.
4. For each moved or new PROOF repo — determined by content,
  never by name (Chris's ruling, 2026-11-18 01:59 PST): any
  repo carrying Lean sources, other proof-assistant sources,
  proof scripts, or machine-checked result artifacts, found
  by the content check named in census.md's sweep section —
  re-census it at theorem level at its new head —
  theorems, axioms, disproofs, premises, side conditions,
  non-claims — replace its census annex file, and update
  only its placements in synthesis.md (its section, the pins
  table in README.md, its census.md family entry). A proof
  repo whose head moved but whose census is not yet redone
  is marked in synthesis.md as "head moved past census pin —
  re-census owed", never silently left at the old pin's
  claims.
5. For each moved IDOL-family repo: update its census.md row
  and pin. Its placement text changes only when a lane's
  record changes the role or state; movement alone changes
  the pin, not the placement.
6. For each moved or new LONG-TAIL repo: update its census
  row (description verbatim from the listing, head, last
  push, flags) and its pin. Depth stays at listing depth —
  unknown — unless a lane examines it; examination, when it
  happens, is recorded in the row.
7. Refresh the proof-strength ledger (proof-strength.md) in
  the same pass: for every proof repo, restate its row at its
  new pin — proven set, premise set, absent set, controls,
  gate state — from the fresh census. Two defect rules: a
  proven set that shrank since the last refresh is flagged
  in the run record as a regression; a proof repo whose pin
  moved while its ledger row did not is a synthesis defect,
  flagged in the run record. Neither is silently absorbed.
8. Paper: if the source MD5 changed, re-copy the page
  verbatim with the host note, and update PAPER-SYNC.md
  (size, MD5, revision markers) per its sync rule.
9. Bump synthesis-pins.json to the fresh heads and the new
  census pins. Commit per piece, as the first synthesis did.
  The final commit of a re-synthesis names, in its message,
  both pins — old and new — of every proof repo that moved,
  and the paper's old and new MD5s if it moved. Push, and
  read the remote head back after the push.
10. Report only: a landed re-synthesis (what moved, old pin
  to new pin, what placements changed) or a failure (what
  step failed and what state the repo was left in). Nothing
  else is reported.

## The scheduled job

A cron job under the idol-autonomous-work-loop goal runs
this procedure hourly: enumerate, diff, and on any movement
re-synthesize and commit as above; silent when nothing
moved; reporting only a landed re-synthesis or a failure.
Its job id is recorded in the lane record,
~/workspace/research/software-closed-loop-2026-11-18.md,
where this repo's creation is recorded.
