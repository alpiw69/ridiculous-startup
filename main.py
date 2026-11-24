"""make.fun bounty: Ridiculous at First Glance, Real by the Second.

Deterministic, no-network program. Writes one sentence of at most
200 characters to /output/entry.txt, pitching a bizarre startup
idea that sounds like a joke until you see the customers and the
money: renting silence by the hour to people working from home
next to building noise. A thick-walled van parks outside and
swallows the drilling. The buyer is anyone on a video call next
to a construction site, and the van is booked by the hour like a
taxi. Running twice writes identical bytes.
"""
from pathlib import Path

PITCH = "We rent out silence by the hour: a thick-walled van parks outside your flat and swallows the drilling next door while you work from home."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(PITCH, encoding="utf-8")
    print(f"Wrote {OUT} ({len(PITCH)} chars)")


if __name__ == "__main__":
    main()
