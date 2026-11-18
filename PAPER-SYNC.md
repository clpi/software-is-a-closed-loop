# Paper sync note

The live paper is "a proposal for the qualification of
software — living spec", hosted in this repo as paper.html.

## Source of record

- Source path: ~/workspace/idol-sites/muse/a-proposal-for-the-
  qualification-of-software/index.html — the presented paper
  page in the idol-sites repo (head 12b61b6d at sync time;
  the page entered that repo in its commit 4ff3306).
- Source size: 94,663 bytes. Source MD5:
  f5d709743cac11d937e7716b7f39c056.
- The page's own revision markers: "Revision 2026-11-17 ·
  Idol / all projects"; build snapshot clpi/idol at 0387b214;
  built over sections 1–17 of its underlying text, with a
  57-entry axis record.
- Underlying text of record: the decidability spec,
  ~/workspace/research/spec-decidability-engine-2026-11-17.md
  (208,118 bytes at census time), from which the page was
  built.
- Synced: 2026-11-18, by verbatim copy. paper.html is the
  source bytes preceded by one host-note comment marking it
  as the live copy; nothing else was added, removed, or
  rewritten.

## A named drift, carried openly

The underlying text has grown past the page's build: the
spec now runs through section 26, and the page has not been
rebuilt over sections 18–26. paper.html is therefore the
latest revision OF THE PAPER as published, and it lags its
own text of record by nine sections. The rebuild of the page
over the full spec is a next step (next-steps.md), owned by
the idol-sites surface lane; until it lands, this note is the
record of the drift, and the continuous job re-checks the
source MD5 on every run — a rebuilt page changes the MD5 and
is re-synced by the same procedure as any other movement.

## Sync rule

On any re-synthesis (resynthesis.md): recompute the source
MD5. If it differs from the MD5 recorded here, re-copy the
page verbatim with the host note, update this note's source
size, MD5, and revision markers, and name the old and new
MD5s in the commit message.
