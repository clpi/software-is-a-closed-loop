import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS = ["gemm", "quest", "carry", "magnetar", "forge"]
bad = 0


def note(ok, line):
    global bad
    if not ok:
        bad = bad + 1
    print(("PASS " if ok else "FAIL ") + line)


def load(path):
    with open(path) as handle:
        return json.load(handle)


def run(args):
    done = subprocess.run(args, capture_output=True, text=True)
    return done.stdout


def verdict(cell, stated):
    path = os.path.join(HERE, "slice.json")
    with open(path, "w") as handle:
        json.dump(stated, handle)
    out = run(["python3", os.path.join(HERE, "generated", cell, "harness.py"), path])
    lines = out.strip().split("\n")
    word = lines[-1].split(": ")[1]
    return word, lines


standing = load(os.path.join(HERE, "standing.json"))
corrected = load(os.path.join(HERE, "corrected.json"))

print("== regenerate ==")
print(run(["python3", os.path.join(HERE, "loom.py"), "all", os.path.join(HERE, "contracts"), os.path.join(HERE, "generated")]).strip())

print("== registered check 1: harnesses reproduce the standing verdicts ==")
for cell in CELLS:
    word, lines = verdict(cell, standing[cell]["figures"])
    for line in lines[:-1]:
        print(cell + " " + line)
    note(word == standing[cell]["verdict"], cell + " verdict " + word + " against recorded " + standing[cell]["verdict"])

print("== registered check 2: regenerated rows match the corrected standing rows ==")
for cell in CELLS:
    rows = load(os.path.join(HERE, "generated", cell, "row.json"))
    want = corrected[cell]["figures"]
    note(rows == want, cell + " row figures " + json.dumps(rows, sort_keys=True) + " against corrected " + json.dumps(want, sort_keys=True))

print("== held-out validation: independent decimal path over rows and held cases ==")
done = subprocess.run(["python3", os.path.join(HERE, "probe.py"), os.path.join(HERE, "contracts"), os.path.join(HERE, "generated")], capture_output=True, text=True)
print(done.stdout.strip())
note(done.returncode == 0, "probe exit " + str(done.returncode))

print("== control a: a drifted stated figure is refused (forge raw 836 to 835) ==")
mutant = dict(standing["forge"]["figures"])
mutant["raw"] = "835"
word, lines = verdict("forge", mutant)
note(word == "PARTIAL", "forge verdict under drift " + word + " (must not be VERIFIED)")

print("== control b: the corrected matrix multiply figure verifies (gemm rate 646 to 647) ==")
mutant = dict(standing["gemm"]["figures"])
mutant["rate"] = "647"
word, lines = verdict("gemm", mutant)
note(word == "VERIFIED", "gemm verdict under the corrected figure " + word)

print("== control c: the row is a projection of the contract (carry start 3.83 to 3.84) ==")
src = os.path.join(HERE, "contracts")
dst = os.path.join(HERE, "mutant")
shutil.rmtree(dst, ignore_errors=True)
shutil.copytree(src, dst)
path = os.path.join(dst, "carry.json")
contract = load(path)
contract["figures"][0]["start"] = "3.84"
with open(path, "w") as handle:
    json.dump(contract, handle, indent=2)
out = os.path.join(HERE, "mutantout")
run(["python3", os.path.join(HERE, "loom.py"), "rows", dst, out])
rows = load(os.path.join(out, "carry", "row.json"))
note(rows["speed"] == "4.80", "mutated carry row speed " + rows["speed"] + " (projection moved with the contract)")

if bad:
    print("battery: FAILED with " + str(bad) + " failures")
    sys.exit(1)
print("battery: PASS")
