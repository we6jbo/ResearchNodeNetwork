#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
problems = []

for p in root.rglob("*"):
    if not p.is_file():
        continue
    rel = p.relative_to(root)
    if any(part in {".git", "build", "__pycache__"} for part in rel.parts):
        continue
    name = p.name.lower()
    if name in {".env", "id_rsa", "id_ed25519", "t14_to_pi"} or name.endswith((".pem",".key",".p12",".pfx")):
        problems.append(f"credential-like file must not be committed: {rel}")

required = {
    "PUBLICATION_POLICY.md": ["`Mom`", "`Grandma`", "`Grandpa`"],
    "AGENTS.md": ["`Mom`", "`Grandma`", "`Grandpa`"],
}
for fn, needles in required.items():
    text = (root/fn).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            problems.append(f"{fn} is missing private-layer rule for {needle}")


semantic_file = root / "vibe" / "semantic_triggers.json"
if not semantic_file.exists():
    problems.append("vibe/semantic_triggers.json is missing")
else:
    try:
        semantic = __import__("json").loads(semantic_file.read_text(encoding="utf-8"))
        if semantic.get("matching_mode") != "semantic":
            problems.append("semantic trigger matching_mode must be semantic")
        if len(semantic.get("concepts", [])) < 16:
            problems.append("semantic trigger list must contain at least 16 concepts")
    except Exception as e:
        problems.append(f"semantic trigger config invalid: {e}")

if problems:
    print("PUBLICATION CHECK FAILED")
    for x in problems:
        print(" -", x)
    sys.exit(1)

print("PUBLICATION CHECK PASS")
print("TG identifiers and named public genealogy data are publication-safe by project policy.")
print("Mom, Grandma, and Grandpa remain protected labels.")
