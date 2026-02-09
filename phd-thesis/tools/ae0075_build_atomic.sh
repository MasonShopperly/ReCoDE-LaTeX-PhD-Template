#!/usr/bin/env bash
set -euo pipefail

TEX="${1:-ae0075_only.tex}"
BASE="${TEX%.tex}"

OUTDIR="_build"
LOGDIR="_logs"
STAMP="$(date +%Y%m%d-%H%M%S)"
RUNLOG="$LOGDIR/latexmk.${BASE}.${STAMP}.log"

mkdir -p "$OUTDIR" "$LOGDIR"

# Clean outdir to avoid "previous invocation" poison / stale aux state
rm -rf "$OUTDIR"
mkdir -p "$OUTDIR"

echo "== build =="
echo "tex:   $TEX"
echo "out:   $OUTDIR/"
echo "log:   $RUNLOG"
echo

# Build in foreground, but log everything (no terminal spam). Timeout protects from hangs.
if ! timeout 300 latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$OUTDIR" -g "$TEX" >"$RUNLOG" 2>&1; then
  echo "BUILD FAILED"
  echo
  if [[ -f "$OUTDIR/$BASE.log" ]]; then
    echo "== first TeX error(s) =="
    grep -n '^!' "$OUTDIR/$BASE.log" | head -n 20 || true
    echo
    echo "== tail of TeX log =="
    tail -n 60 "$OUTDIR/$BASE.log" || true
  else
    echo "No TeX log found at $OUTDIR/$BASE.log"
  fi
  echo
  echo "== tail of latexmk run log =="
  tail -n 80 "$RUNLOG" || true
  exit 1
fi

SRC="$OUTDIR/$BASE.pdf"
DST="$BASE.pdf"

if [[ ! -f "$SRC" ]]; then
  echo "BUILD FAILED: no PDF produced at $SRC"
  tail -n 80 "$RUNLOG" || true
  exit 1
fi

# Atomic publish so viewers never see a half-written file
cp "$SRC" "$DST.new"
mv -f "$DST.new" "$DST"

echo "OK: published $DST"
stat -c 'PDF mtime: %y  %s bytes' "$DST"
