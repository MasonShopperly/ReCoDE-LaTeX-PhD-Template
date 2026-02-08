#!/usr/bin/env python3
from pathlib import Path
import re, sys, datetime

if len(sys.argv) != 3:
    print("Usage: ae0075_move_input_to_end.py <file> <literal_input_line>", file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1])
ins  = sys.argv[2]

s = path.read_text()

bak = path.with_suffix(path.suffix + f".bak.{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}")
bak.write_text(s)

# Remove ALL occurrences of the exact input line (tolerate surrounding whitespace/newlines).
pat = re.compile(r"[ \t]*" + re.escape(ins) + r"[ \t]*\n", re.M)
s2 = re.sub(pat, "", s)
s2 = re.sub(r"\n{3,}", "\n\n", s2).rstrip() + "\n"

# Insert once at end (prefer right before final \endgroup if present).
k = s2.rfind(r"\endgroup")
if k != -1:
    out = s2[:k].rstrip() + "\n\n" + ins + "\n\n" + s2[k:]
else:
    out = s2.rstrip() + "\n\n" + ins + "\n"

path.write_text(out)
print(f"OK: moved to end; backup: {bak.name}")
