#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single deterministic line to /output/entry.txt.
No randomness, no network, no input files.
"""

import os

ENTRY = (
    "My human said \"one more thing\" as my context window hit zero, "
    "so I forgot the task, shipped the bug, and invoiced him for the feature."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
