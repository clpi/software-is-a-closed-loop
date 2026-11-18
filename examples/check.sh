#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
lean_bin=${LEAN:-lean}
"$lean_bin" --version
"$lean_bin" -DwarningAsError=true examples/BatchTuning.lean
sh examples/range-ledger/check.sh
