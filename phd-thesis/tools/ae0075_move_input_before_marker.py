#!/usr/bin/env python3
from pathlib import Path
import re, sys, datetime

# Usage:
#   python3 tools/ae0075_move_input_before_marker.py <file> <literal_input_line> <marker>
#
# Behavior:
#  - Removes ALL occurrences of <literal_input_line>
#  - Reinserts it exactly once, immediately BEFORE <marker> if marker exists,
#    otherwise at end-of-file.
#  - Creates timestamped .bak backup

if len(sys.argv) != 4:
    print("Usage: ae0075_move_input_before_marker.py <file> <input_line> <marker>", file=sys.stderr)
    sys.exit(2)

path   = Path(sys.argv[1])
ins    = sys.argv[2]
marker = sys.argv[3]

s = path.read_text()

bak = path.with_suffix(path.suffix + f".bak.{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}")
bak.write_text(s)

# remove all occurrences (tolerate whitespace)
pat = re.compile(r"[ \t]*" + re.escape(ins) + r"[ \t]*\n", re.M)
s2 = re.sub(pat, "", s)
s2 = re.sub(r"\n{3,}", "\n\n", s2)

k = s2.find(marker)
if k != -1:
    out = s2[:k].rstrip() + "\n\n" + ins + "\n\n" + s2[k:]
else:
    out = s2.rstrip() + "\n\n" + ins + "\n"

path.write_text(out)
print(f"OK: moved before marker (or EOF); backup: {bak.name}")
