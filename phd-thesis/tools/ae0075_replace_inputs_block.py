#!/usr/bin/env python3
from pathlib import Path
import sys, datetime

# Replace a contiguous range of \input lines with a single \input.
# Usage:
#   python3 tools/ae0075_replace_inputs_block.py <file> <start_line_literal> <end_line_literal> <replacement_line>

if len(sys.argv) != 5:
    print("Usage: ae0075_replace_inputs_block.py <file> <start> <end> <replacement>", file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1])
start = sys.argv[2]
end   = sys.argv[3]
repl  = sys.argv[4]

s = path.read_text()

a = s.find(start)
b = s.find(end)
if a < 0 or b < 0 or a > b:
    print("ABORT: start/end anchors not found in order.", file=sys.stderr)
    sys.exit(1)

b2 = b + len(end)

bak = path.with_suffix(path.suffix + f".bak.{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}")
bak.write_text(s)

out = s[:a].rstrip() + "\n" + repl + "\n" + s[b2:].lstrip()
path.write_text(out)
print(f"OK: replaced inputs block; backup: {bak.name}")
