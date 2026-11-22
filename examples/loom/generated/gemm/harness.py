import json
import sys
from fractions import Fraction

FIGS = [
  {
    "name": "rate",
    "start": "431",
    "ops": [
      [
        "times",
        "3/2"
      ]
    ],
    "places": 0
  },
  {
    "name": "call",
    "start": "0.73",
    "ops": [
      [
        "divide",
        "2"
      ]
    ],
    "places": 2
  },
  {
    "name": "size",
    "start": "1024",
    "ops": [
      [
        "times",
        "1024"
      ],
      [
        "times",
        "8"
      ],
      [
        "divide",
        "1048576"
      ]
    ],
    "places": 0
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
