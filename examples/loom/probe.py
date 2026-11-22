import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 50

CELLS = ["gemm", "quest", "carry", "magnetar", "forge"]


def parse(text):
    if "/" in text:
        head, tail = text.split("/")
        return Decimal(head) / Decimal(tail)
    return Decimal(text)


def derive(fig):
    acc = parse(fig["start"])
    for pair in fig["ops"]:
        if pair[0] == "times":
            acc = acc * parse(pair[1])
        else:
            acc = acc / parse(pair[1])
    return acc


def figure(fig):
    quantum = Decimal(1).scaleb(-fig["places"])
    return format(derive(fig).quantize(quantum, rounding=ROUND_HALF_UP), "f")


def load(path):
    with open(path) as handle:
        return json.load(handle)


def check(src, dst):
    bad = 0
    for cell in CELLS:
        contract = load(os.path.join(src, cell + ".json"))
        rows = load(os.path.join(dst, cell, "row.json"))
        held = load(os.path.join(dst, cell, "held.json"))
        for fig in contract["figures"]:
            got = figure(fig)
            want = rows[fig["name"]]
            if got != want:
                bad = bad + 1
                print(cell + " " + fig["name"] + ": ROW MISMATCH probe=" + got + " generated=" + want)
            else:
                print(cell + " " + fig["name"] + ": row agrees at " + got)
            for case in held[fig["name"]]:
                twin = dict(fig)
                twin["start"] = case["start"]
                got = figure(twin)
                if got != case["expect"]:
                    bad = bad + 1
                    print(cell + " " + fig["name"] + " start=" + case["start"] + ": HELD MISMATCH probe=" + got + " generated=" + case["expect"])
        print(cell + ": held cases agree")
    if bad:
        print("probe: FAILED with " + str(bad) + " mismatches")
        sys.exit(1)
    print("probe: PASS")


check(sys.argv[1], sys.argv[2])
