#!/bin/sh
set -eu
cd "$(dirname "$0")"
lean_bin=${LEAN:-lean}
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
python3 unpack.py "$tmp"
export LEAN_PATH="$tmp"
for module in Identifiable AdaptiveReads OverlapPlan SignedStitch CertificateReuse LinearProvenance IntervalBasis; do
  (cd "$tmp" && "$lean_bin" -DwarningAsError=true -o "$module.olean" "$module.lean") >/dev/null
done
"$lean_bin" --version
"$lean_bin" -DwarningAsError=true Settlement.lean
patch -s -o "$tmp/Changed.lean" Settlement.lean < mutation.patch
if "$lean_bin" -DwarningAsError=true "$tmp/Changed.lean" >"$tmp/control.log" 2>&1; then
  echo "Modified claim passed unexpectedly" >&2
  exit 1
fi
grep -q 'Changed.lean:.*error:' "$tmp/control.log"
echo "Rejected control: remove the orientation reversal in the integrated publisher."
python3 replay.py
