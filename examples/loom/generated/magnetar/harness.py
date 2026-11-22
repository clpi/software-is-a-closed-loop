import json
import sys
from fractions import Fraction

FIGS = [
  {
    "name": "rate",
    "start": "12.8",
    "ops": [
      [
        "times",
        "2"
      ]
    ],
    "places": 1
  },
  {
    "name": "floor",
    "start": "8.7",
    "ops": [
      [
        "times",
        "2"
      ]
    ],
    "places": 1
  }
]


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
