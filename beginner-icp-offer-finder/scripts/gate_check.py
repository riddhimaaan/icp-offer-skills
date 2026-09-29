#!/usr/bin/env python3
"""Mechanical checks for the beginner ICP + offer output.

Usage:
    python gate_check.py output.md
    cat output.md | python gate_check.py

Checks: four required sections, no extra top-level sections, no em dashes,
banned phrases, 3 to 5 triggers, matching count in Where to find them,
no questions, price present.
"""
import re
import sys

REQUIRED = ["ICP", "Offer", "Triggers", "Where to find them"]

BANNED = [
    "scale", "scaling", "grow your business", "10x", "leverage", "unlock",
    "streamline", "cutting edge", "cutting-edge", "game changer", "revolutionize",
    "next level", "boost your revenue", "done for you solutions", "synergy",
    "empower", "seamless", "holistic", "robust", "elevate", "supercharge",
    "fast paced", "fast-paced", "businesses of all sizes",
    "small and medium businesses", "smbs", "decision makers",
    "key stakeholders", "value proposition", "pain points",
]


def sections(text):
    parts = re.split(r"^#\s+(.+?)\s*$", text, flags=re.M)
    found = {}
    order = []
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        found[name] = parts[i + 1]
        order.append(name)
    return found, order


def numbered(body):
    return len(re.findall(r"^\s*\d+\.\s", body, flags=re.M))


def main():
    text = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    fails = []

    found, order = sections(text)
    for name in REQUIRED:
        if name not in found:
            fails.append(f"Missing section: # {name}")
    extra = [n for n in order if n not in REQUIRED]
    if extra:
        fails.append(f"Extra sections not allowed: {extra}")
    if order and order[: len(REQUIRED)] != REQUIRED and not extra:
        fails.append(f"Sections out of order: {order}")

    before_first = re.split(r"^#\s+", text, maxsplit=1, flags=re.M)[0].strip()
    if before_first:
        fails.append("Text found before the ICP section (no intro allowed)")

    if "\u2014" in text:
        fails.append(f"Em dashes found: {text.count(chr(0x2014))}")

    lower = text.lower()
    for phrase in BANNED:
        if re.search(r"\b" + re.escape(phrase) + r"\b", lower):
            fails.append(f"Banned phrase: '{phrase}'")

    if "?" in text:
        fails.append("Question mark found (output should not ask questions)")

    if "Triggers" in found:
        t = numbered(found["Triggers"])
        if not 3 <= t <= 5:
            fails.append(f"Trigger count is {t}, needs 3 to 5")
        if "Where to find them" in found:
            w = numbered(found["Where to find them"])
            if w != t:
                fails.append(f"Where to find them has {w} items, Triggers has {t}")

    if "Offer" in found and "price" not in found["Offer"].lower():
        fails.append("Offer has no Price line")

    if fails:
        print("GATE: FAIL")
        for f in fails:
            print(" -", f)
        sys.exit(1)
    print("GATE: PASS (mechanical checks only, still run the judgment tests)")


if __name__ == "__main__":
    main()
