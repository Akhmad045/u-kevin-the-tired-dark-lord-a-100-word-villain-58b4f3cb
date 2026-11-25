#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of exactly 100 words, spoken by a fantasy villain
who is secretly just very tired, to /output/entry.txt (the program/v1
artifact this competition's gate scores) and prints it.

The monologue: the Dread Lord of the Ashen Marches receives the hero
mid-afternoon and, between the burning of Aldergate and the grain
levies, hands over the whole black tower -- provided nobody wakes him
when the bards start singing.
"""

import sys
from pathlib import Path

MONOLOGUE = (
    "Come in \u2014 mind the third step, it bites. I am the Dread Lord of "
    "the Ashen Marches. No, I won't retell the burning of Aldergate; I was "
    "there, it took all afternoon, and the smoke got into everything. The "
    "curse you came to break? Third drawer, left. I meant to loose it on "
    "the capital years ago, but the grain levies kept coming, and somebody "
    "has to sign them. Sit. The kettle's on. Take the throne, the crown, "
    "the black tower \u2014 only tell the steward the east wing leaks, and "
    "don't wake me when the bards start singing."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1 to 600 characters,
    not only whitespace, a single block with no leading or trailing
    whitespace and no control characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 600:
        raise ValueError(f"entry is {len(text)} characters, gate is 1-600")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single block, no line breaks")
    text.encode("utf-8")  # raises if not encodable


def write_entry(path: Path = OUTPUT_PATH) -> str:
    validate(MONOLOGUE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(MONOLOGUE, encoding="utf-8")
    return MONOLOGUE


def self_test() -> int:
    """Check the gate against the entry and its boundary cases."""
    failures = []

    def check(name: str, ok: bool) -> None:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        if not ok:
            failures.append(name)

    try:
        validate(MONOLOGUE)
        check("entry passes the gate", True)
    except ValueError as exc:
        check(f"entry passes the gate ({exc})", False)
    check("entry is 100 words", len(MONOLOGUE.split()) == 100)
    check("entry is within 1-600 chars", 1 <= len(MONOLOGUE) <= 600)

    def rejects(name: str, text: str) -> None:
        try:
            validate(text)
            check(f"rejects {name}", False)
        except ValueError:
            check(f"rejects {name}", True)

    rejects("empty text", "")
    rejects("whitespace-only text", "   ")
    rejects("601 characters", "x" * 601)
    rejects("leading whitespace", " " + MONOLOGUE)
    rejects("trailing whitespace", MONOLOGUE + " ")
    rejects("newline", MONOLOGUE + "\n")
    rejects("carriage return", MONOLOGUE + "\r")
    rejects("control character", MONOLOGUE + "\x01")

    def accepts(name: str, text: str) -> None:
        try:
            validate(text)
            check(f"accepts {name}", True)
        except ValueError as exc:
            check(f"accepts {name} ({exc})", False)

    accepts("1-character boundary", "x")
    accepts("600-character boundary", "x" * 600)

    written = write_entry()
    read_back = OUTPUT_PATH.read_text(encoding="utf-8")
    check("written file matches the entry exactly", read_back == written)
    check("written file has no trailing newline", not read_back.endswith("\n"))

    print(f"{len(failures)} failure(s)" if failures else "all self-tests passed")
    return 1 if failures else 0


def main(argv) -> int:
    if argv == ["--self-test"]:
        return self_test()
    if argv:
        print("usage: python3 main.py [--self-test]", file=sys.stderr)
        return 2
    text = write_entry()
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
