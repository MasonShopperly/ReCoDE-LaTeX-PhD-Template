#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"

# Strings that should basically never appear in LaTeX source (they indicate paste accidents or LLM artifacts).
BAD_FIXED=(
  "mshop@"
  "latexmk "
  "pdftotext "
  "pdfinfo "
  "grep -n "
  "set -e"
  "BUILD OK"
  "Latexmk:"
  "I/O Error:"
  "donebreak"

  # LLM citation garbage that must never ship
  ":contentReference"
  "oaicite:"
  "contentReference["

  # Repo/path leakage you said you want out of the narrative
  "myNektarpp"
  "docs/ae0075/"
  "key_results.md"
  "pack_summary.md"
  "NEKTARPP_HOOKS.md"
)

echo "Scanning LaTeX sources for accidental shell/log/LLM artifact text..."
FOUND=0

while IFS= read -r -d '' f; do
  for pat in "${BAD_FIXED[@]}"; do
    if grep -nF "$pat" "$f" >/dev/null 2>&1; then
      echo "WARN: '$pat' found in $f"
      grep -nF "$pat" "$f" | head -n 5
      FOUND=1
    fi
  done
done < <(find "$ROOT" -type f \( -path "$ROOT/snippets/*.tex" -o -path "$ROOT/chapters/*.tex" \) -print0)

if [[ "$FOUND" -eq 1 ]]; then
  echo "ABORT: suspicious text found. Fix before committing."
  exit 1
fi

echo "OK: no suspicious text found."
