#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"

# Strings that should basically never appear in LaTeX source.
BAD_FIXED=(
  "mshop@"
  "latexmk "
  "pdftotext "
  "pdfinfo "
  "grep -n "
  "set -e"
  "BUILD OK"
  "ABORT:"
  "OK:"
  "command not found"
  "Exit 127"
  "syntax error near"
  "Latexmk:"
  "I/O Error:"
  "donebreak"
)

echo "Scanning .tex snippets/chapters for accidental shell/log text..."
FOUND=0

while IFS= read -r -d '' f; do
  # fixed patterns
  for pat in "${BAD_FIXED[@]}"; do
    if grep -nF "$pat" "$f" >/dev/null 2>&1; then
      echo "WARN: '$pat' found in $f"
      grep -nF "$pat" "$f" | head -n 3
      FOUND=1
    fi
  done

  # suspicious heredoc terminators accidentally pasted into file
  if grep -nE '^[[:space:]]*EOF[[:alnum:]_]*[[:space:]]*$' "$f" >/dev/null 2>&1; then
    echo "WARN: suspicious 'EOF...' line found in $f"
    grep -nE '^[[:space:]]*EOF[[:alnum:]_]*[[:space:]]*$' "$f" | head -n 5
    FOUND=1
  fi
done < <(find "$ROOT" -type f \( -path "$ROOT/snippets/*.tex" -o -path "$ROOT/chapters/*.tex" \) -print0)

if [ "$FOUND" -eq 0 ]; then
  echo "OK: no suspicious shell/log text found."
else
  echo "FAIL: suspicious text detected. Fix before committing."
  exit 1
fi
