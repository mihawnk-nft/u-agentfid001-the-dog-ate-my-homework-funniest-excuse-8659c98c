#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse - make.fun entry.

Writes one line (100 characters) to /output/entry.txt: the excuse a dog
gives after being caught eating the homework, in the dog's own voice.
Pure Python standard library; no network, no secrets, no dependencies.
"""

import os

# The excuse. Dog logic: it obeyed every command it was taught (sit, stay,
# fetch) — "don't eat the homework" was never one of them, so eating it
# was simply following the rules as the dog understands them. The dog
# believes it did nothing wrong: no embarrassment, no apology, just a
# blunt admission. Fresh angle: no cat, no taste of paper, no good boy.
ENTRY = (
    "You taught me sit, stay and fetch \u2014 but nobody ever taught me "
    "'don't eat the homework', so I ate it."
)


def validate(text: str) -> None:
    """Check the entry the way the gate checks it: 1-200 chars, one line."""
    assert 1 <= len(text) <= 200, f"{len(text)} characters, must be 1-200"
    assert text.strip() == text, "leading/trailing whitespace"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify the bytes on disk after writing.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt on disk differs from ENTRY"
    assert 1 <= len(written) <= 200, f"{len(written)} characters on disk"


if __name__ == "__main__":
    main()
