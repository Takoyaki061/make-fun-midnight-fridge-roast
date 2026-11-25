#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one one-line roast of a smart fridge that refuses to open after
midnight to /output/entry.txt, for the pairwise AI-judged comedy duel.
"""

import os

ROAST = (
    'You say "we need to talk about boundaries"'
    "\u2014boundaries don't get to lock a man out of the cheese drawer."
)


def main() -> None:
    # Mirror the sealed gate so a bad line fails loudly here, not on the server:
    # /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
    # white space.
    text = ROAST.strip()
    assert text, "roast must not be blank"
    assert len(text) <= 200, f"roast is {len(text)} chars, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    print(ROAST)


if __name__ == "__main__":
    main()
