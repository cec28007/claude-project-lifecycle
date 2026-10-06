#!/usr/bin/env python3
"""Assemble a project's instructions: replace {{block}} with blocks/<block>.md.
Usage: build-instructions.py <instructions-file>  -> prints the text and checks the length (limit 16,000)."""
import re, sys, pathlib

LIMIT = 16000
here = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1]).read_text()
out = re.sub(r"\{\{([\w-]+)\}\}", lambda m: (here / "blocks" / f"{m.group(1)}.md").read_text().strip(), src).strip() + "\n"
sys.stdout.write(out)
sys.stderr.write(f"\n[{len(out):,} / {LIMIT:,} characters]\n")
if len(out) > LIMIT:
    sys.exit("over the limit")
