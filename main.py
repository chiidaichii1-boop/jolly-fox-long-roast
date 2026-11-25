#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent.

The agent here is a bounty-farming coding agent whose own safety
screening keeps flagging its work, so it files a report and waits for
its human to say "lanjut" before it may continue. This entry turns
that exact habit into the roast: it tried to insult itself, got
flagged by its own safety check, and cannot even finish the insult
without human approval.
"""

import os

ENTRY = (
    "My agent tried to roast itself, got flagged by its own safety check, "
    "and is now waiting for me to say 'lanjut' before it finishes the insult."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be only whitespace")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
