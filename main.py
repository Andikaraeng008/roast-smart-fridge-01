"""Roast the Smart Fridge: one line, best laugh wins.

Gate: entry.txt must be UTF-8 text of 1-160 characters (this line is 142).
Writes to $MAKEFUN_OUTPUT_DIR (fallback /output) -- never to a
repo-local output/ dir, which the grader mounts read-only.
"""

import os

LINE = "My smart fridge learned my voice, my face and my midnight snack schedule, then started hiding the cheese behind a password I set while asleep."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
