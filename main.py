"""Roast the Smart Fridge: one line, best laugh wins.

Gate: entry.txt must be UTF-8 text of 1-160 characters (this line is 128).
Writes to $MAKEFUN_OUTPUT_DIR (fallback /output) -- never to a
repo-local output/ dir, which the grader mounts read-only.
"""

import os

LINE = "My smart fridge took a photo of me at 2am, ran it through its diet app, and emailed my doctor before I even found the leftovers."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
