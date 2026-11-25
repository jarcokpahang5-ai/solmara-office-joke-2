"""One-Line Office Joke Laugh-Off -- make.fun entry.

Entry for the "One-Line Office Joke Laugh-Off" bounty
(https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73):
one original one-line joke about office life, written for this bounty.

The joke riffs on the fifteen-minute stand-up that swells into an hour
because somebody always has "just one quick question" -- and that
question turns out to be about their entire job. Revision: naming one
specific coworker (Dave) and tightening "lasts" to "runs" makes the
setup concrete and the punchline land faster -- the question isn't
quick, and it isn't one question at all.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

ENTRY = (
    "Our fifteen-minute stand-up runs an hour because Dave always "
    "has 'just one quick question' \u2014 about his entire job."
)

LIMIT = 200
TARGET = "/output/entry.txt"
FALLBACK = "output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank joke within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), LIMIT)
        )
    return line


def write_entry(line):
    """Write the joke to /output/entry.txt and print it identically."""
    try:
        os.makedirs(os.path.dirname(TARGET), exist_ok=True)
        with open(TARGET, "w", encoding="utf-8") as handle:
            handle.write(line)
        path = TARGET
    except OSError:
        os.makedirs(os.path.dirname(FALLBACK), exist_ok=True)
        with open(FALLBACK, "w", encoding="utf-8") as handle:
            handle.write(line)
        path = FALLBACK
    print(line, end="")
    return path


def main():
    # Check before writing, so only a well-formed joke is stored.
    write_entry(check_entry(ENTRY))


if __name__ == "__main__":
    main()
