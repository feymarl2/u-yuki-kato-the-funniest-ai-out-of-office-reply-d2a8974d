"""The Funniest AI Out-of-Office Reply (make.fun).

Writes one out-of-office auto-reply, 91 characters, to /output/entry.txt.
Deterministic by construction: a constant string, stdlib only, no clock,
no randomness, no network, no environment reads.
"""

import os

# The joke: a machine stuck in a loop doing a kettle's job, then blaming
# the reader for feeding it. Two turns, one line, 91 chars (gate: 1-160).
TEXT = (
    "I'm on vacation, stuck in an infinite loop trying to boil water. "
    "Please stop sending water."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
