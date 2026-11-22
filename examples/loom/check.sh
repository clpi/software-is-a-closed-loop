#!/bin/sh
set -eu
cd "$(dirname "$0")"
lean_bin=${LEAN:-lean}
"$lean_bin" --version
"$lean_bin" -DwarningAsError=true Loom.lean
tmp=$(mktemp -d ./work.XXXXXX)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
cp -r contracts generated standing.json corrected.json loom.py probe.py tally.py "$tmp"/
(cd "$tmp" && python3 tally.py)
diff -r generated "$tmp/generated"
echo "loom: PASS"
