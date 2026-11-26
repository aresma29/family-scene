#!/usr/bin/env python3
"""Print the entry line from entry.txt exactly as written."""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    # sys.stdout.write, not print: print would append an extra newline
    # and the output would no longer match entry.txt byte for byte.
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
