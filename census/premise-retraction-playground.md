# Census — premise-retraction-playground

## Pin and identity

- Live head, read first through the GitHub route: `47f469a4e868ce9f7ad5f17e329739ef22b8066c`
- Clone head, shallow clone at depth one: same — verified match.
- Visibility: public. Default branch: main.
- Toolchain pin: none. There is no build step, no dependency list, no package file and no test runner configuration in the tree.
- Files: exactly two files in the whole tree. A readme of 90 lines and a single self-contained page of 1,516 lines that contains the style, the markup and the whole program in one inline script. No other source, data, fixture or log file exists at this pin.

## Thesis, in plain English

Learning can be premise-tracked in miniature. Take a least squares line-and-plane model with two inputs and three weights. Write its normal equations as a sum in which every training example, treated as a named premise, contributes exactly one additive term: a small symmetric matrix block and a small vector, both built only from that example and its weight. Keep running totals of those blocks. To retract a premise, subtract its block from the totals and solve again. Because every number in the model and in the check is an exact rational, the result is not close to the model trained on the remaining premises; it is term-for-term the same, and a check that rebuilds the totals from zero using only the remaining premises confirms that on every retraction.

## Controls and zero-sorries evidence

There is no proof assistant in this repo, so the zero-sorries section of the sibling censuses has no analogue here. What exists instead is an executed check inside the program itself, and it is important to place it at its true level.

- Gate evidence in this census is the repo's own material, labelled as such, plus one independent recomputation performed in this census and described below. No browser run was performed in this census.
- The check, as written in the single page: after a retraction, the program compares two genuinely different paths. The first path is the incrementally maintained totals with the retracted premise's block subtracted. The second path is a fresh model built by summing only the remaining premises from zero and solving again. Five comparisons are made, all as exact rationals with no tolerance: the running totals equal the fresh sum, term for term; the post-retraction weights equal the fresh weights; every prediction matches the fresh model, over a fixed query grid plus the surviving premise points; adding the retracted contribution back restores the previous totals exactly; and every surviving premise's contribution is byte-identical before and after, compared as serialised text.
- Liveness control, as stated in the readme: tampering with the running totals by a small amount flips the banner to failure, which is offered as evidence that the check is live rather than decorative. That tamper behaviour is a statement in the readme and in the page's own explanatory text. No tamper test file, test script or recorded tamper run exists in the tree, so in this census that control is a recorded claim about the program, not a separate executed artefact.
- Sweep control, inside the program: a sweep operation retracts every active premise in turn and runs the same five comparisons for each case. A demo operation adds five premises, retracts the middle one, and runs the check. Both are user-triggered operations in the page; neither leaves a recorded result in the tree.
- Recorded numeric claim in the readme, verified independently in this census: the readme gives the full fit for its five demo premises and the fit after retracting the middle premise, as exact fractions. In this census those two fits were recomputed from the readme's own demo data with exact rational arithmetic, by a separate implementation of the same normal equations, and both fits matched the readme values exactly, for all three weights in both fits. That verification covers the readme's concrete numbers. It does not cover the page's code in general, and it is not a proof.
- No recorded check log, receipt file, test output or continuous integration configuration exists in the tree at this pin. A receipt can be downloaded from the page at run time; none is committed.

## Definitions carried

- A premise: a named training example with two input values, one output value and a positive premise weight, all read exactly. A decimal input is read as the exact rational it names, and a fraction input is read as that fraction.
- The per-premise contribution: the outer product block of the extended input vector, which is the constant one followed by the two inputs, scaled by the premise weight; and the matching vector, the output times the extended input vector, scaled the same way. Each premise stores exactly its own block and vector, and nothing in a contribution depends on any other premise or on the current weights.
- The running totals: the sum of the blocks and the sum of the vectors over the active premises. The weights are the solution of the linear system the totals define, found by an exact rational solver in the page. Singularity is reported by the solver path rather than hidden: a system that does not determine weights produces no weights to compare.
- Retraction, restore and fresh fit: retraction subtracts one contribution and solves again; restore adds the same contribution back; a fresh fit sums the contributions of a chosen set of premises from zero and solves. Exactness is the equality of the first and third of these, as rationals.
- The illustrative contrast: a separate panel runs an order-dependent gradient descent learner in ordinary floating point numbers, in one pass with a stated step size, and shows that subtracting a recorded update does not reproduce a model trained without that example. The page and the readme both label that panel illustrative. It is not the model, and no claim in this census rests on it.

## Theorem census

There are no named theorems or lemmas in this repo, in any proof system. The census table therefore records the single provable-shaped result the repo carries, at its true level, and the supporting statements around it.

| Token | Hypotheses to conclusion, in plain English | Evidence state |
|---|---|---|
| `exactnessCheck` | Premises: a retraction has taken place, the running totals are the previous totals minus exactly the retracted premise's own contribution, every contribution is a function of its own premise alone, and all arithmetic is exact rational arithmetic → the five comparisons pass: totals, weights and predictions equal the fresh fit on the remaining premises, re-adding restores the prior totals, and no surviving contribution changed. One quoted token only: the name of the check function in the page, which is the closest thing this repo has to a named result. | Claimed-not-proven as a general statement; see the evidence section below. The check is executable code that returns a pass or fail verdict at run time, not a proved theorem. |
| — (the additive form itself) | Premise: the objective is least squares with per-premise weights → its normal equations are a sum of per-premise terms and nothing else, so the weights are a function of that sum alone. This is the mathematical fact the whole miniature rests on. It is stated in the readme with the equations written out, and it is standard linear algebra. No token is quoted for this row because the repo gives it no name. | Proven as mathematics in the ordinary textbook sense, as a derivation printed in the readme; not machine-checked in any system in this repo. |
| — (the demo instance) | Premise: the five demo premises printed in the readme → the full fit and the fit after retracting the middle premise are the exact fractions the readme prints. No token is quoted for this row. | Proven at the level of an executed exact recomputation: independently recomputed in this census and matched exactly, as recorded above. This covers those two fits only. |

Supporting code facts, counted in this census from the single page: the rational type is built on arbitrary precision integers with a greatest common divisor normalisation; the solver, the statistics accumulation, the check and the receipt are all written generically in the number of input features, which is fixed at two by a constant in the page; floating point numbers appear in the model code only where an exact value is converted for pixel placement on the chart, and in the separate illustrative contrast panel.

## Examples and controls

- The demo: five premises in two input dimensions, the middle one retracted, five of five checks passing, with the before and after weights printed in the readme and verified in this census as described above.
- By-hand use: add premises, retract any row, and the check runs automatically. Restore adds the same block back and clears the receipt, so a stale check is not presented as covering a new state.
- The sweep: retract each active premise in turn and check every case. The sweep requires at least two active premises and reports a row per premise.
- The empty case, as presented by the page itself: when every premise is retracted, the totals are exactly zero and all three weights are zero, matching a model trained on nothing. This is a presented behaviour of the page, not a recorded run in the tree.
- The receipt: a download that exports the premises, the per-premise contributions, all three weights and the check results as exact fractions. It is generated at run time and is the artefact a user would keep from a run; none is committed in the repo.

## Premises carried rather than proven, consolidated

1. Additivity is the whole mechanism, and it holds because the model is least squares with a closed-form normal equation system. The readme states the scope plainly: with more inputs the same code path solves the larger system and every block stays additive, but with a sequential optimiser the same guarantee would require freezing each premise's contribution rather than recomputing it against moving weights. No result in this repo covers a sequential optimiser, a non-linear model, or any model whose per-example contribution depends on the current weights.
2. Exactness rests on exact rational arithmetic everywhere in the model and the check. Any port that carried the totals in floating point numbers would lose the guarantee by rounding, as the illustrative panel is there to show for a different algorithm. The repo proves nothing about a floating point version, and does not claim to.
3. The check compares the maintained path against a fresh path that shares the same contribution construction, the same rational arithmetic and the same solver code in the same page. A defect shared by both paths — in how a contribution is built, for instance — would not be caught by the comparison. The readme's argument that the two paths are genuinely different is about the accumulation path, incremental subtraction against summation from zero, and that is the difference the check exercises.
4. The solver's handling of singular or inconsistent systems is carried by the code path that reports no weights. No statement in the repo characterises exactly which premise sets give a determined system, and the check's weight comparison is vacuous in the form the code states it when there are no weights to compare, beyond the totals comparison which still runs.
5. The demo premises are arbitrary teaching data, stated in the readme to be measurements of nothing. No empirical or capacity claim rests on them.

## Non-claims carried

- No kernel-checked proof: nothing in this repo is checked by a proof assistant kernel, a verifier, a solver or a type system beyond the page's own run-time comparisons. The word proof, where the page's description uses it in passing, does not change that level.
- No general learning claim: the repo does not claim that learning in general is premise-tracked, that a trained network can be retracted in this way, or that the miniature scales to a capacity claim. The readme states the claim being demonstrated is the accounting, not the capacity, and that the scope is three weights on purpose.
- No claim about the illustrative panel beyond illustration: the floating point contrast is an order-dependent one-pass learner built to show a failure mode of a naive undo. It is not presented as a model of any real training system.
- No persistence or network claim in either direction needs reading in: the page states it makes no network calls and uses no storage, and this census records that as the page's own statement about itself, not as an audited property.
- No performance claim: nothing in the repo measures or claims speed, size or cost, beyond the observation that retraction is a subtraction and a re-solve of a three-by-three system rather than a retraining job.

## Evidence state

- The additive form of the normal equations: **proven** as ordinary mathematics, by the derivation printed in the readme. Not machine-checked.
- The readme's two concrete demo fits: **proven** at the level of executed exact arithmetic, by the independent recomputation performed in this census, which matched all six printed weight values exactly.
- The general exactness result, that retraction in this program always equals a fresh fit: **claimed-not-proven**. The reason is precise. The program contains an executable check that would fail loudly if a run violated exactness, and the mathematical reason it cannot fail for this model is given in the readme — exact rationals leave no residue, and the totals are a sum of independent per-premise terms. But no proof, in a kernel or otherwise, covers the page's code as written, no recorded run at this pin is stored in the tree, and no browser execution was performed in this census. An executed verification at run time, even an exact one, is not a kernel-checked proof, and this census places the result at the lower level deliberately, in the family discipline.
- The liveness tamper claim and the sweep and empty-case behaviours: **claimed-not-proven** at this pin, as behaviours described by the readme and the page, with no recorded run in the tree.
- Nothing in this repo is **refuted**, and nothing is merely **proposed**: the artefact exists in full at this pin and does what its text describes, at the evidence level stated above.
