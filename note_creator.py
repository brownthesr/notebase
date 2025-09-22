#!/usr/bin/env python3
import os
import re
from collections import defaultdict

# Regex for tags
TAGS = ["TODO", "FIXME", "NOTE"]
pattern = re.compile(rf"\b({'|'.join(TAGS)})\b", re.IGNORECASE)

# Collect matches grouped by directory
matches = defaultdict(list)

for root, _, files in os.walk("."):
    for fname in files:
        if fname.startswith(".") or "git" in root:  # skip hidden/git files
            continue
        path = os.path.join(root, fname)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for lineno, line in enumerate(f, start=1):
                    if pattern.search(line):
                        rel_path = os.path.relpath(path, ".")
                        subsystem = os.path.dirname(rel_path) or "."
                        matches[subsystem].append((rel_path, lineno, line.strip()))
        except Exception:
            pass  # skip binary or unreadable files

# Write markdown
with open("TODOs.md", "w", encoding="utf-8") as md:
    md.write("# Project TODO / FIXME / NOTE Summary\n\n")
    for subsystem in sorted(matches):
        md.write(f"## {subsystem}\n\n")
        for file, lineno, text in matches[subsystem]:
            if text == "":
                text = "(empty line)"
            md.write(f"- **{file}:{lineno}** — `{text}`\n")
        md.write("\n")  # ensure extra newline between subsystems

print("✅ TODOs.md created.")
