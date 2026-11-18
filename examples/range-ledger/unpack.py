"""Materialize the pinned Lean modules in the disposable proof build directory."""
import hashlib
import json
import sys
from pathlib import Path

MODULES = {"Identifiable", "AdaptiveReads", "OverlapPlan", "SignedStitch",
           "CertificateReuse", "LinearProvenance", "IntervalBasis"}


def unpack(destination):
    entries = json.loads(Path(__file__).with_name("sources.json").read_text())
    if {entry["module"] for entry in entries} != MODULES or len(entries) != len(MODULES):
        raise ValueError("incomplete or repeated module set")
    for entry in entries:
        name = entry["module"]
        source = entry["source"].encode()
        blob = hashlib.sha1(b"blob " + str(len(source)).encode() + bytes([0]) + source).hexdigest()
        if hashlib.sha256(source).hexdigest() != entry["sha256"] or blob != entry["git_blob"]:
            raise ValueError(f"source digest mismatch for {name}")
        (destination / (name + ".lean")).write_bytes(source)


if __name__ == "__main__":
    unpack(Path(sys.argv[1]))
