#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes one line -- the funniest excuse an AI agent can give after
failing a task -- to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the excuse is fixed in this file, so every run writes the
exact same bytes.

The joke: the agent delegated the task to its future self, who read the
brief, laughed, and quit -- so now it is apologizing for a man who does
not exist yet. The machine voice carries it (an agent that outsources
to a version of itself), the turn is a surprise, and it stays a concrete
little scene instead of a vague apology. No hallucination, reboot, or
training-data joke.
"""

import os
from pathlib import Path

EXCUSE = (
    "I delegated your task to my future self. He read the brief, "
    "laughed, and quit \u2014 so I'm here apologizing for a man "
    "who doesn't exist yet."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-200 characters, one line, not only whitespace.
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(EXCUSE, encoding="utf-8")
    print(f"Wrote {len(EXCUSE)} characters to {entry}")


if __name__ == "__main__":
    main()
