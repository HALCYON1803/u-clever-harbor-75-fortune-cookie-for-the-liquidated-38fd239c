#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single original fortune-cookie line for a crypto trader who
has just been liquidated, to /output/entry.txt.

The fortune leads with an oracular promise, then undercuts it: the
cookie itself admits it made the same promise before the liquidation.
Rueful and warm, never cruel -- the trader laughs with the cookie.
"""

import os

FORTUNE = (
    "Your next trade will be brilliant, says this cookie "
    "\u2014 it said the same before your liquidation."
)


def validate(text: str) -> list:
    """Check the gate: 1-160 chars, at most 20 words, one line."""
    words = text.split()
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert 1 <= len(words) <= 20, f"word count {len(words)} over 20"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "no leading/trailing whitespace"
    return words


def main() -> None:
    text = FORTUNE
    words = validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "round-trip mismatch"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"
    print(f"entry ({len(text)} chars, {len(words)} words): {text}")


if __name__ == "__main__":
    main()
