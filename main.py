"""SockSync — entry for make.fun bounty
"The Worst App Idea Ever Pitched"
(u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23).

Writes one sentence (236 characters, no trailing newline) to the
absolute path /output/entry.txt, as the program/v1 harness requires.
Stdlib only, no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "SockSync pairs your socks over Bluetooth and pings your phone the "
    "moment one vanishes in the dryer, because no family should face "
    "laundry day without real-time sock accountability, closure and a "
    "full audit trail for every pair they own."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file's character count must equal the
    # entry's character count exactly (gate: 1 to 240 characters).
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
