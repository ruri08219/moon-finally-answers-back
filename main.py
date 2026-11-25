#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one line, the Moon's comeback, to /output/entry.txt.
Standard library only.
"""
import os
import sys

ENTRY = "Four billion years of wishes, howls, and 2 a.m. promises — and the only one I ever granted was the tide. That one was gravity's fault."


def main():
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip() or "\n" in ENTRY:
        print("error: ENTRY must be 1-240 chars, non-whitespace, single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
