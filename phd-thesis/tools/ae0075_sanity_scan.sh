#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BAD_PATTERNS=(
  "mshop@"
  "BUILD OK"
  "set -e"
  "pdftotext "
  "latexmk "
  "pdfinfo "
  "grep -n "
  "donebreak"
  "---- occurrences"
  "ABORT:"
  "OK:"
)

echo "Scanning .tex snippets/chapters for accidental shell/log text..."
FOUND=0

while IFS= read -r -d '' f; do
  for pat in "${BAD_PATTERNS[@]}"; do
    if grep -nF "$pat" "$f" >/dev/null 2>&1; then
      echo "WARN: '$pat' found in $f"
      grep -nF "$pat" "$f" | head -n 3
      FOUND=1
    fi
  done
done < <(find "$ROOT" -type f \( -path "$ROOT/snippets/*.tex" -o -path "$ROOT/chapters/*.tex" \) -print0)

if [ "$FOUND" -eq 0 ]; then
  echo "OK: no suspicious shell/log text found."
else
  echo "FAIL: suspicious text detected. Fix before committing."
  exit 1
fi
