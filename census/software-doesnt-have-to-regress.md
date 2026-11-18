# Census — software-doesnt-have-to-regress

## Pin and identity

- Live head (gh API, read first): `24d36c13414867e59ae67ccf47f83cc250ce55af`
- Clone head (shallow clone, depth 1): same as live head — verified match.
- Visibility (gh API): private. Default branch: master (only branch).
- Toolchain pin: **none** — no lean-toolchain file exists.
- Contents at head (recursive tree, confirmed by API and clone): exactly one file, `README.md`, 2 lines. No Lean modules, no check script, no check log, no controls file.

## Thesis (as stated)

The README's single descriptive line, in plain English: a Lean 4 proof that a release process with per-symbol observed-behavior certification never has to regress. That is the entire stated claim. There is no further prose, no definitions, no scope statement.

## Theorem census

- Theorem / lemma count: **0**.
- There are no `.lean` files, so there are no theorems, lemmas, definitions, examples, or guards to census. Nothing in the repo formalizes "release process", "per-symbol", "observed behavior", "certification", or "regress".

## Evidence claims

- Zero-sorries claim: **none made, and none checkable** — there is no proof code in which a sorry could occur, and no check log or control asserting absence.
- Axiom dependencies: none stated anywhere (no print-axioms output, no README claim).
- Checksums / controls: none present.

## Flagged items

- DISPROOFS: none.
- PREMISES carried rather than proven: none stated — but note the whole thesis is itself an unbacked premise at this head: the certification process it conditions on is not defined, let alone proved sufficient.
- Side conditions: none stated.
- NON-CLAIMS / boundaries: **none stated**. The README does not say what the (absent) proof does not assert, what "regress" means, or what the certification must guarantee.

## Verdict

At the live head this is a title-and-one-line stub, not a proof repo. The headline result is absent: theorem count 0, no toolchain, no evidence.
