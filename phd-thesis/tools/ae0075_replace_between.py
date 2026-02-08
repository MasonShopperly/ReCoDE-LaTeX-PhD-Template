#!/usr/bin/env python3
from pathlib import Path
import sys, datetime

# Usage:
#   python3 tools/ae0075_replace_between.py <file> <start_anchor> <end_anchor> <replacement_text>
#
# Replaces inclusive block from start_anchor up to (but not including) end_anchor.
# Creates a timestamped backup. Fails if anchors not found in correct order.

if len(sys.argv) != 5:
    print("Usage: ae0075_replace_between.py <file> <start_anchor> <end_anchor> <replacement_text>", file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1])
start = sys.argv[2]
end   = sys.argv[3]
repl  = sys.argv[4]

s = path.read_text()

a = s.find(start)
b = s.find(end)
if a < 0 or b < 0 or a >= b:
    print("ABORT: anchors not found (or ordered incorrectly).", file=sys.stderr)
    sys.exit(1)

bak = path.with_suffix(path.suffix + f".bak.{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}")
bak.write_text(s)

out = s[:a] + repl + "\n\n" + s[b:]
path.write_text(out)
print(f"OK: replaced block; backup: {bak.name}")
