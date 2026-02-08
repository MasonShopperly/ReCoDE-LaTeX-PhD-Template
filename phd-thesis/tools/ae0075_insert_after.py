#!/usr/bin/env python3
from pathlib import Path
import sys, datetime

# Usage:
#   python3 tools/ae0075_insert_after.py <chapter.tex> "<anchor string>" "<text to insert>"
#
# Idempotent: if <text to insert> already exists, no change.

if len(sys.argv) != 4:
    print("Usage: ae0075_insert_after.py <file> <anchor> <insert_text>", file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1])
anchor = sys.argv[2]
insert_text = sys.argv[3]

s = path.read_text()

if insert_text in s:
    print("OK: insert already present (idempotent).")
    sys.exit(0)

k = s.find(anchor)
if k < 0:
    print(f"ABORT: anchor not found: {anchor}", file=sys.stderr)
    sys.exit(1)

bak = path.with_suffix(path.suffix + f".bak.{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}")
bak.write_text(s)

out = s[:k+len(anchor)] + insert_text + s[k+len(anchor):]
path.write_text(out)
print(f"OK: inserted after anchor; backup: {bak.name}")
