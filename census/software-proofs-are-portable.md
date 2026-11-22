# software-proofs-are-portable — theorem census

Pin d2dd570c01a94304f34bb2a7c49bb4f56b28a5d0. Public.
No description stands in the listing; the repo's own
readme states its claim. Censused by the eighty-fifth
hourly re-synthesis watch (2026-11-21), which found the
repo new in the full enumeration and read its whole tree
at the pin (17 files, not truncated) firsthand through
the gh route: the spec, the readme, the one proof file,
the axioms audit file, the gate script, and the recorded
gate output. The determination is by content — Lean
sources carrying proved results — never by the name.

## The thesis, in plain English

A release artifact can carry its own certificate as a
derived part of the artifact itself, so checking the
artifact and checking its proof are one act with one
hash, and a forged or detached certificate cannot verify
against a different artifact. The construction answers
the forged qualification flag class: a detached flag,
flipped by whoever holds the file, admitted an
unqualified action. The spec demonstrates that class on
this repo's own instance first — the issuing checker's
own run accepts a forgery made of flag edits alone —
before the construction is stated.

## What is proved

The proof file carries four theorems over an abstract
digest, and all four depend on no axioms at all; the
axioms audit file prints that audit and the recorded
build carries it:

- Soundness: verification of the combined artifact
  implies the certified property of the artifact alone.
- The transplant bound: where the genuine combined
  artifact verifies, a transplant of its certificate
  over a different artifact verifies only if the two
  artifacts share a digest.
- The refusal: under the same hypothesis, any artifact
  whose digest differs refuses with that certificate,
  with no further premise.
- Sameness: under one named premise — the digest
  separates the two artifacts in question — a verifying
  transplant is the same artifact.

State: PROVEN in source at the pin, on the recorded
gate evidence below.

## Premises, named and not proved here

- Collision resistance: the digest separates distinct
  artifacts on the byte ranges in question. The sameness
  theorem takes this as an explicit hypothesis for the
  pair it speaks about; the refusal needs only digest
  inequality, which the verifier computes. Nothing in
  the repo proves a digest collision resistant.
- The underlying certificate is valid as issued: the
  issuing pipeline's own soundness results stand in its
  repo at its pin, and the reading carried is the
  reading it issued.

## The instance

The one certified release transition in the estate: the
monotonic certification pipeline's first issuance, over
the perception repo's tree between its two named pins.
The artifact is the subject tree archive at the later
pin; the certificate is the issued certificate file,
byte for byte. Its reading, exactly as issued, is not
certified — three dimensions stand unmeasured and block
certification. The construction binds that certificate
to its artifact so the reading cannot be flipped by
editing the carried file; it does not upgrade the
reading, and no verification of this instance accepts a
certified reading. The anchors — the artifact digest,
the issued certificate digest, the earlier tree digest,
and the issuer's checker digest — are recorded in the
spec and the manifest, each re-derivable from the
pinned repos named there. The combined bundle digest
names the artifact and its proof together.

## Controls and gate

The check script runs an escape scan, a cold Lean build
with warnings as errors, and the standing attack
battery. The battery runs six checks and fails closed
on the first disagreement: determinism (two builds
byte-identical), the honest bundle (verifies, reading as
issued), a flip in the artifact (refused), a flip in the
certificate (refused), a transplant onto the earlier
tree (refused), and the forgery assembled over the
genuine artifact (refused). The recorded run stands in
the instance folder and prints its pass. The detached
form's fall to the same forgery is the executed control
recorded in the spec. Gate state: recorded pass at the
pin, read firsthand by this watch and not re-run.

## What is not claimed

- No issuer authentication beyond the anchored digests:
  anyone can assemble a bundle, and only a bundle whose
  components hash to the anchored digests verifies.
  Whoever can rewrite the anchors themselves is outside
  the construction's scope.
- The archive bytes of a tree at a pin are whatever the
  archiving tool produces; the anchor is the digest.
- The remaining releases of the issuing gate are not
  re-issued here; this instance is the first issuance,
  and re-issuing the rest is a next step, not a result.

The census pin is set to the fresh head on this first
proof census; the placements in the synthesis and the
ledger row are entered at the pin in this same pass.
