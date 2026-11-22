# Loom — contracts woven once, checked everywhere

A beat cell's contract is written once as an executable pattern: the
point figures the cell rests on, and the derivation that turns them into
the cell's bars. The loom generates three artifacts from that one
source — the cell's ledger row, its harness, and its held-out validation
set — so the three can never drift apart. That drift is a measured
defect class: in the dense matrix multiply cell, the stated rate bar is
the floor of the bar its own description derives, and the hand-kept row
carried the weaker figure until an external check caught it.

Each contract states its operands and its operations only. The derived
figures exist nowhere in the source; the row is a projection of the
contract value, the harness enforces the same projection, and the
held-out set is the same derivation at fresh operand values. The proof
companion states the agreement as a theorem over any pattern: the
generated row always passes the generated harness, a figure that differs
from the derivation is refused, and a held-out case states the same
figure the row states at that value. Two concrete instances carry the
matrix multiply cell: its generated rate bar at the recorded floor is
647, the figure its standing row fails to state, and its generated
call-cost bar in hundredths is 37, the figure its standing row states.

Run `sh examples/loom/check.sh` from the repository root. The gate
recompiles the proof with warnings as errors, regenerates every
artifact in a scratch copy and requires byte-identical regeneration,
reproduces the standing verdict of each of the five cells with its
generated harness, requires each regenerated row to equal the corrected
standing row figure for figure, confirms every row figure and every
held-out case through an independent decimal checker that shares no
code with the generator, and runs the drift controls: a stated figure
moved by one is refused, the corrected matrix multiply figure verifies,
and a contract operand moved by one hundredth moves the generated row
with it.

| Cell | Figures woven | Standing verdict, reproduced | Regenerated row |
|---|---|---|---|
| dense matrix multiply | rate, call cost, operand size | partial: the stated rate bar fails its own derivation | states the corrected rate bar, 647 |
| QuestDB write amplification | rate bar | verified | matches the standing row |
| rejected-state carryover | speedup bar | verified | matches the standing row |
| zero-knowledge proving | rate bar, lower threshold | verified | matches the standing row |
| distributed forge | raw bar, real-branch bar | verified | matches the standing row |

Premises, as registered: the five cells' standing verdicts are as
recorded in the zero-loss ledger and its claim-verification annotations;
the projection is over the contract value only, never over measured
results. The corrected standing row for the matrix multiply cell is the
standing row with the verification annotation's correction applied: the
rate bar is 647, the round-half-up value of one and a half times the
verified floor of 431, where the row as filed states 646, its floor.
