import json
import os
import sys
from fractions import Fraction

CELLS = ["gemm", "quest", "carry", "magnetar", "forge"]
LADDER = ["-2", "-1", "-1/2", "1/2", "1", "2", "10"]


def parse(text):
    return Fraction(text)


def derive(fig):
    acc = parse(fig["start"])
    for pair in fig["ops"]:
        if pair[0] == "times":
            acc = acc * parse(pair[1])
        else:
            acc = acc / parse(pair[1])
    return acc


def rounded(value, places):
    scale = 10 ** places
    scaled = value * scale
    whole = scaled.numerator // scaled.denominator
    if scaled - whole >= Fraction(1, 2):
        whole = whole + 1
    return Fraction(whole, scale)


def render(value, places):
    scale = 10 ** places
    whole = int(value * scale)
    if places == 0:
        return str(whole)
    return str(whole // scale) + "." + str(whole % scale).zfill(places)


def plain(value):
    num = value.numerator
    den = value.denominator
    if den == 1:
        return str(num)
    places = 0
    scale = 1
    while scale % den != 0 and places < 12:
        scale = scale * 10
        places = places + 1
    whole = num * (scale // den)
    return str(whole // scale) + "." + str(whole % scale).zfill(places)


def figure(fig):
    return render(rounded(derive(fig), fig["places"]), fig["places"])


def describe(fig):
    text = fig["start"]
    for pair in fig["ops"]:
        text = text + " " + pair[0] + " " + pair[1]
    return text


def row(contract):
    parts = []
    figs = {}
    for fig in contract["figures"]:
        value = figure(fig)
        figs[fig["name"]] = value
        parts.append(fig["name"] + " bar " + value + " " + fig["unit"] + " (" + describe(fig) + ", round half up at " + str(fig["places"]) + " places)")
    return "[" + contract["cell"] + "] " + "; ".join(parts), figs


def held(contract):
    out = {}
    for fig in contract["figures"]:
        cases = []
        base = parse(fig["start"])
        for step in LADDER:
            start = base + parse(step)
            if start <= 0:
                continue
            twin = dict(fig)
            twin["start"] = plain(start)
            cases.append({"start": plain(start), "expect": figure(twin)})
        out[fig["name"]] = cases
    return out


TEMPLATE = '''import json
import sys
from fractions import Fraction

FIGS = __FIGS__


def parse(text):
    return Fraction(text)


def derive(fig):
    acc = parse(fig["start"])
    for pair in fig["ops"]:
        if pair[0] == "times":
            acc = acc * parse(pair[1])
        else:
            acc = acc / parse(pair[1])
    return acc


def rounded(value, places):
    scale = 10 ** places
    scaled = value * scale
    whole = scaled.numerator // scaled.denominator
    if scaled - whole >= Fraction(1, 2):
        whole = whole + 1
    return Fraction(whole, scale)


def render(value, places):
    scale = 10 ** places
    whole = int(value * scale)
    if places == 0:
        return str(whole)
    return str(whole // scale) + "." + str(whole % scale).zfill(places)


stated = json.load(open(sys.argv[1]))
holds = 0
for fig in FIGS:
    got = render(rounded(derive(fig), fig["places"]), fig["places"])
    want = stated[fig["name"]]
    mark = "HOLD"
    if got != want:
        mark = "NO-HOLD"
    else:
        holds = holds + 1
    print(fig["name"] + ": " + mark + " derived=" + got + " stated=" + want)
if holds == len(FIGS):
    print("verdict: VERIFIED")
elif holds == 0:
    print("verdict: FAILED")
else:
    print("verdict: PARTIAL")
'''


def script(contract):
    figs = []
    for fig in contract["figures"]:
        figs.append({"name": fig["name"], "start": fig["start"], "ops": fig["ops"], "places": fig["places"]})
    return TEMPLATE.replace("__FIGS__", json.dumps(figs, indent=2))


def load(src, cell):
    with open(os.path.join(src, cell + ".json")) as handle:
        return json.load(handle)


def emit(mode, src, dst):
    for cell in CELLS:
        contract = load(src, cell)
        home = os.path.join(dst, cell)
        os.makedirs(home, exist_ok=True)
        if mode in ("rows", "all"):
            text, figs = row(contract)
            with open(os.path.join(home, "row.txt"), "w") as handle:
                handle.write(text + "\n")
            with open(os.path.join(home, "row.json"), "w") as handle:
                json.dump(figs, handle, indent=2, sort_keys=True)
                handle.write("\n")
        if mode in ("scripts", "all"):
            with open(os.path.join(home, "harness.py"), "w") as handle:
                handle.write(script(contract))
        if mode in ("held", "all"):
            with open(os.path.join(home, "held.json"), "w") as handle:
                json.dump(held(contract), handle, indent=2, sort_keys=True)
                handle.write("\n")
        print(cell + ": " + mode + " written to " + home)


emit(sys.argv[1], sys.argv[2], sys.argv[3])
