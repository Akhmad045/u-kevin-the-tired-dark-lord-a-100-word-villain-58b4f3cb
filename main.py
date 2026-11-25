#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue - make.fun bounty entry.

Writes one monologue of about 100 words, spoken by a fantasy villain who
is secretly just very tired, to /output/entry.txt (no trailing newline).

The speaker: a lich three centuries into keeping his tower, interrupted
mid-tea by a hero. His soul sits in the teapot; his heroes are buried in
the east garden, alphabetically; the amulet is behind the jam. The
tiredness lives in the interruptions, the domestic deflections and the
trailing-off — never in a plain statement that he is weary — and the last
line lands the sting: he has a kettle to watch.

Run `python3 main.py` to write /output/entry.txt, `--output <path>` to
write elsewhere, or `--self-test` to validate the gate and the written file.
"""

import argparse
import sys
import unicodedata
from pathlib import Path

ENTRY = (
    "You have caught me mid-sentence, which is rude, and mid-tea, which is "
    "worse. The teapot, by the way, holds my soul \u2014 do mind the handle. "
    "Three centuries I have kept this tower: the ravens fed, the curses "
    "filed, the heroes buried in the east garden, alphabetically. You want "
    "the amulet? It is on the shelf, behind the jam. Take it. Take it all. "
    "Only \u2014 when the villagers cheer your name tonight, remember who "
    "sharpened the swords they cheered with. Now. If you are going to "
    "strike, strike. I have a kettle to watch."
)
DEFAULT_OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 600


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-600 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        raise ValueError("entry must not contain control characters")
    # Invisible format characters (zero-width space and kin) are not
    # whitespace to str.strip, so a line of only them would slip past the
    # empty check while reading as blank to the judge. Reject them too.
    if any(unicodedata.category(ch) == "Cf" for ch in text):
        raise ValueError("entry must not contain invisible format characters")
    text.encode("utf-8")  # raises on text that is not UTF-8 encodable


def write_entry(output: Path = DEFAULT_OUTPUT) -> Path:
    validate(ENTRY)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(ENTRY.encode("utf-8"))
    # Read-back check: what landed on disk must be byte-identical.
    if output.read_bytes() != ENTRY.encode("utf-8"):
        raise RuntimeError(
            "read-back mismatch: %s differs from ENTRY" % output
        )
    return output


def self_test() -> int:
    cases = [
        ("", False),                    # empty
        ("   ", False),                 # whitespace only
        ("x" * 601, False),             # over the 600-char gate
        ("two\nlines", False),          # multi-line
        ("carriage\rreturn", False),    # carriage return
        (" leading", False),            # leading whitespace
        ("trailing ", False),           # trailing whitespace
        ("\x07bell", False),            # control character
        ("\u200b", False),              # zero-width space only (invisible)
        ("\u200bhello", False),         # invisible format character inside
        ("a", True),                    # 1-char lower boundary
        ("x" * 600, True),              # 600-char upper boundary
        (ENTRY, True),                  # the entry itself
    ]
    failures = 0
    for text, should_pass in cases:
        try:
            validate(text)
            passed = True
        except ValueError:
            passed = False
        if passed != should_pass:
            print(
                "FAIL: %r expected %s, got %s"
                % (text[:40], "pass" if should_pass else "reject",
                   "pass" if passed else "reject")
            )
            failures += 1
    # End to end: write via the --output path into a temp dir, then
    # gate-check what is on disk; then the default path, as the grader runs it.
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        alt = Path(tmp) / "entry.txt"
        alt_path = write_entry(alt)
        alt_raw = alt_path.read_bytes()
        alt_text = alt_raw.decode("utf-8")
        try:
            validate(alt_text)
        except ValueError as exc:
            print("FAIL: --output file failed the gate: %s" % exc)
            failures += 1
        if alt_raw != ENTRY.encode("utf-8"):
            print("FAIL: --output file is not byte-identical to ENTRY")
            failures += 1
    path = write_entry()
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    try:
        validate(text)
    except ValueError as exc:
        print("FAIL: written file failed the gate: %s" % exc)
        failures += 1
    if raw != ENTRY.encode("utf-8"):
        print("FAIL: written file is not byte-identical to ENTRY")
        failures += 1
    if failures:
        print("self-test: %d failure(s)" % failures)
        return 1
    print(
        "self-test: all %d checks passed; entry is %d words, %d chars / %d bytes"
        % (len(cases) + 3, len(ENTRY.split()), len(ENTRY),
           len(ENTRY.encode("utf-8")))
    )
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test", action="store_true",
        help="validate the gate and the written file",
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help="where to write the monologue (default: /output/entry.txt)",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
