#!/usr/bin/env bash
set -euo pipefail

mkdir -p _logs

echo "[1/3] sanity scan (logged)..."
# syntax-check first so a broken script doesn't explode the session
bash -n tools/ae0075_sanity_scan.sh 2> _logs/sanity_scan.syntax.err || true
if [[ -s _logs/sanity_scan.syntax.err ]]; then
  echo "WARN: sanity scan script has bash syntax issues (see _logs/sanity_scan.syntax.err)"
else
  tools/ae0075_sanity_scan.sh . > _logs/sanity_scan.out 2>&1 || true
  if grep -q '^WARN:' _logs/sanity_scan.out; then
    echo "WARN: sanity scan flagged issues (showing first 20 lines):"
    sed -n '1,20p' _logs/sanity_scan.out
  else
    echo "OK: sanity scan clean"
  fi
fi

echo "[2/3] latexmk build (logged)..."
latexmk -pdf -interaction=batchmode -halt-on-error ae0075_only.tex > _logs/latexmk.log 2>&1 || true
RC=$?
echo "latexmk RC=$RC"
if [[ "$RC" -ne 0 ]]; then
  echo "BUILD FAIL: showing last 40 lines of _logs/latexmk.log"
  tail -n 40 _logs/latexmk.log
  exit "$RC"
fi

echo "[3/3] quick PDF text smoke test (small excerpt)..."
if [[ ! -f ae0075_only.pdf ]]; then
  echo "BUILD FAIL: ae0075_only.pdf not found"
  exit 2
fi

# keep output tiny to avoid crashing terminals
pdftotext -f 2 -l 3 ae0075_only.pdf - 2>/dev/null | \
  grep -n -E "Executive Summary|Introduction, problem formulation|Research aims, hypotheses|Operational definitions" \
  | head -n 40 || true

echo "BUILD OK"
