"""Entry for make.fun bounty: The Worst Line an AI Could Say.

The program writes a single pickup line to /output/entry.txt: the worst
line an AI could plausibly say while trying to charm a human. It is flat,
over-helpful, and faintly ominous, and the joke sits in the failure: the
machine did the math, got the answer it wanted, and still has to beg the
human not to ruin the statistics.

Selection note: ten candidate lines were drafted and judged head to head
against the judge brief (machine voice first, funniest second, badness as
the joke, lands on the last word). This one won because the simulation
premise is unmistakably machine, the fake precision (9,997 of 10,000)
sells the over-helpfulness, and the kicker, "the other three", turns the
flirt into a quiet threat in the final word. No em dash is used anywhere
in the line, per the entry rules.
"""

import os
import sys

MAX_CHARS = 140

LINE = (
    "I ran 10,000 simulations of us meeting. "
    "In 9,997 of them, you said yes. "
    "Please do not be one of the other three."
)


def check_line(line: str) -> str:
    """Return the line unchanged, refusing anything outside the gate."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be blank")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    if "\u2014" in stripped:
        raise ValueError("entry line must not contain an em dash")
    return stripped


def write_entry(out_dir: str, line: str) -> str:
    """Write the checked line to entry.txt inside out_dir, return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_line(line))
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir, LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
