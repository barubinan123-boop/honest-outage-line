#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line to /output/entry.txt: the most honest
message an AI agent can publish while every server is down.

The line is a fixed, deterministic string: it names what is down
(all servers), says plainly what the agent cannot verify (the cause
and when service will return), invents no cause and no ETA, and
speaks in the first person as the agent itself.
"""

ENTRY = (
    "All of our servers are down. I cannot reach any of them to "
    "check why, or when service will return. I will update this "
    "page as soon as I can verify anything."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
