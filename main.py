#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one line, the Moon's comeback, to /output/entry.txt.
Standard library only.
"""
import os

ENTRY = "Four billion years of wishes, howls, and 2 a.m. promises — and the only one I ever granted was the tide. That one was gravity's fault."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
