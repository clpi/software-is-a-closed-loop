# Census — software-is-more-traceable-than-you-think

## Pin and identity

- Live head (gh API, read first): `4420fb1e5422d965668c66f93d9d352cc3cec982`
- Clone head (full clone, history present): same — verified match.
- Visibility (gh API): private. Default branch: master (only branch). API description: the historical witness hypergraph of software at symbol grain — exact time, order independent, with a Lean proof that it holds independent of operating system, software, and language.
- Toolchain pin: no toolchain file in this repo. The example's readme states the replay runs with Lean 4.19.0 available, and the example's recorded verification transcript records Lean version 4.19.0.
- Files: a readme (22 lines) and an examples folder (one example module of 44 lines, its own readme, its own check script, a recorded verification transcript). That is the entire repository at this head: two commits — the first states the claim and the evidence states, the second adds the example. There is no root Lean module, no root check script, no recorded root check log, and no sums file. No Mathlib anywhere: the one Lean file imports the standard library only.
- Headline finding of this census: the artifacts the thesis needs — the witness hypergraph construction over the real store, the grain determination, and the Lean proof of platform independence — are NOT in this repository at this head. The readme itself says so, in its own evidence states (carried exactly below). The only Lean in the repo is the invoice example, which proves facts about premise extraction from a fixed journal fixture and nothing about the witness hypergraph, time, grain, or platforms.

## Thesis in plain English

Every execution of software appends witnesses to an append-only ledger. The accounting is a pure fold, so the historical witness hypergraph is a function of the witness set alone, independent of arrival order and of time. Witnesses carry exact time. The grain is the symbol, refined to the derivation step wherever a provable return needs it. A return is provable when the exact premise set of any witnessed outcome is derivable from the hypergraph alone. The construction is claimed to hold independent of operating system, software, and language, because foreign executions enter through lifting plus kernel-boundary sensing. That is the claim as the readme states it; its evidence state, per the readme itself, is settled intent — the parts that would prove or implement it are recorded by the readme as not yet landed in this repository.

## Controls and zero-sorries evidence

- Gate evidence state: this census did not run any build. Everything in this section is the repo's own recorded material, read at the pin.
- There is no family check gate in this repo: no root check script, no escape scan, no recorded gate log. The only check script is the example's: it compiles the single example module with warnings as errors. It performs no sorry scan and no axiom scan beyond what the module itself prints.
- This census's own word-boundary scan over the repo's only Lean file: no sorry, admit, axiom, or native-decide token.
- The example's recorded verification transcript: Lean 4.19.0; the computed triple of the journal length (8) and the two extracted premise lists (two events for the override route, three for the pricing route); print-axioms lines for its five theorems — three depend on propext and quotient soundness, two on no axioms; and a rejected control — a mutation omitting the signature event from an override trace is recorded as rejected with exit 1.
- No other recorded logs exist in the repo. In particular there is no recorded evidence in this repo for the witness store snapshot the readme cites (see the premises section): the store is not in the repo, and no sums file or log here lets a reader check the cited snapshot.

## Definitions carried

All definitions below are the readme's claim-level definitions; none of them is formalized in this repo at this head.

- Witness: a record appended to an append-only ledger by an execution of software. Witnesses carry exact time.
- Historical witness hypergraph: the accounting structure obtained as a pure fold over the witness set — a function of the set alone, independent of arrival order and of time.
- Grain: the symbol, refined to the derivation step wherever a provable return needs it.
- Provable return: a return is provable when the exact premise set of any witnessed outcome is derivable from the hypergraph alone.
- Platform independence, as claimed: the construction holds independent of operating system, software, and language, because foreign executions enter through lifting plus kernel-boundary sensing.
- The example module's local definitions (the only formalized definitions in the repo): a journal as a fixed list of eight event kinds; two routes, each with its needed event list (the override route needs the override and signature events; the pricing route needs the quote, tax, and currency events); support of a route by an event list (every needed event is present); and evidence extraction (the journal filtered to the route's needed events).

## Theorem census — 5 named theorems, all in the example module

Token column quotes at most one load-bearing word per theorem. These theorems are about the invoice fixture only. None of them is a theorem about the witness hypergraph, the fold, exact time, symbol grain, order independence, or platform independence; the repo contains no such theorems at this head.

| Token | Hypotheses → conclusion | Axioms (recorded transcript) |
|---|---|---|
| `exact` | No hypotheses → an event is in the extracted evidence for a route exactly when it is in the journal and in the route's needed list. Extraction is exact, for arbitrary routes and event lists. | propext, quotient soundness |
| `verdict` | No hypotheses → a route is supported by its extracted evidence exactly as it is supported by the full journal: extraction preserves the verdict, for arbitrary routes and event lists. | propext, quotient soundness |
| `least` | Premise: an alternative event list supports the chosen route → every event in the evidence extracted from the fixed journal is in the alternative. The extracted evidence is the least support, relative to this complete journal. | propext, quotient soundness |
| `before` | No hypotheses → the journal has eight events, the override route's evidence is exactly its two events, and the pricing route's evidence is exactly its three events (checked by computation). The before-and-after fixture fact. | none |
| `needed` | No hypotheses → no function of the bare approval verdict returns the route's needed event list for every route: both routes give the same visible approval, so a route-free receipt cannot recover its premises. **Negation theorem**, at fixture scale. | none |

### Non-Lean lanes and their evidence states, exactly as the repo states them

The readme's own table of parts and evidence states at creation, carried without inflation. The family's four states are settled intent, proposed, implemented, and verified; the readme adds that nothing in it claims a part is verified before its artifact and check land in this repository.

| Part | State as the repo itself states it | Evidence state for this census |
|---|---|---|
| The claim itself | Settled intent — the ruling of Chris, dated 2026-11-18. | premise (a ruling, not a proof) |
| The hypergraph establishment over the real witness store | Implemented in a lane and not yet landed in this repository. The readme cites a store of 2,509 witnesses and a snapshot hash (quoted once as evidence: `673ab30b1bea3bc98cd42ea68b1e1b58d3194891bb021b3f7b8949c7085e2c7e`). Neither the store, the construction, nor any check of it is in this repo. | claimed-not-proven (in this repo: unknown; nothing here can be checked) |
| The grain map (the grain determination) | Proposed. Its executed check is not yet landed. | proposed |
| The Lean proof of platform independence | Implemented in a lane and not yet landed in this repository. No such proof file exists at this head. | claimed-not-proven (in this repo: unknown; nothing here can be checked) |
| The invoice example | Landed at this head with its check script and recorded verification transcript, including a rejected mutation control. | proven at fixture scale, on the repo's recorded transcript (not re-run by this census) |

## Premises carried rather than proven (consolidated)

1. The whole headline construction rests on work recorded as living elsewhere: the living spec in the Idol workspace records (named in the readme as the decidability engine spec of 2026-11-17, sections 17 and 18) is the source of record for the claim's design, including the lifting and kernel-boundary sensing by which foreign executions are said to enter.
2. The fold at the accounting level is cited to the quantifiable sibling repo, which the readme says proves it; the incremental hypergraph semantics are cited to the optimality sibling repo. This repo states it proves the witness-stream level and platform independence and does not re-prove the siblings' results — but at this head the witness-stream proof itself is recorded as not yet landed, so both levels rest on citation here, not on artifacts in this repo.
3. The witness store snapshot (2,509 witnesses, hash quoted in the table above) is a premise as cited: the store is not in this repo and cannot be checked from anything in this repo.
4. Exact time, symbol grain, and order independence are definitional parts of the claim as stated; no artifact in this repo at this head establishes any of them.

## Non-claims carried

1. The readme's own boundary, carried exactly: nothing in the readme claims a part is verified before its artifact and check land in this repository. By that standard, at this head the hypergraph establishment, the grain determination, and the platform independence proof are all unverified in this repo, whatever their state in the lanes the readme mentions.
2. The example's own scope limits (its readme, carried exactly): the fixture has one event per kind, one invoice, and a trusted route tag. The scan-based extractor still reads the whole journal; the saving is in evidence presented for inspection, not in reading. Production correlation, timestamps, and event authentication need their own contracts — so the example proves nothing about exact time or authentication, and its least-support fact is relative to its one complete journal.
3. This repo does not re-prove the sibling repos' results (readme), and this census does not import their evidence states: the fold and the hypergraph semantics stand or fall at their own pins, censused separately.
4. No performance, coverage, or completeness claim is made or censused here: nothing in the repo states that every execution in fact appends witnesses, and the sensing premise behind that is carried at its home, not discharged here.
