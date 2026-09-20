#!/usr/bin/env python3
from pathlib import Path
import os

home = Path.home()
src = Path(os.environ.get("RNN_PROJECT_ROOT", home/"Projects/ResearchNodeNetwork")) / "vibe" / "global_AGENTS_block.md"
dst_dir = Path(os.environ.get("VIBE_HOME", home/".vibe"))
dst = dst_dir / "AGENTS.md"
begin = "<!-- BEGIN ResearchNodeNetwork bootstrap -->"
end = "<!-- END ResearchNodeNetwork bootstrap -->"

block_body = src.read_text(encoding="utf-8").strip()
block = f"{begin}\n{block_body}\n{end}\n"

dst_dir.mkdir(parents=True, exist_ok=True)
if dst.exists():
    original = dst.read_text(encoding="utf-8")
else:
    original = ""

if begin in original and end in original:
    before = original.split(begin, 1)[0]
    after = original.split(end, 1)[1]
    merged = before.rstrip() + "\n\n" + block + after.lstrip()
else:
    merged = original.rstrip()
    if merged:
        merged += "\n\n"
    merged += block

dst.write_text(merged, encoding="utf-8")
print(dst)
