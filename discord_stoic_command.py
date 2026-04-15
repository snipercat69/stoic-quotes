#!/usr/bin/env python3
"""Discord command helper for #stoic-quotes."""

from __future__ import annotations

import random
import shlex
import sys

RNG = random.Random()

DAILY_STOIC = "https://dailystoic.com/stoic-quotes/"
ORION = "https://orionphilosophy.com/stoic-quotes/"
WIKIQUOTE_MA = "https://en.wikiquote.org/wiki/Marcus_Aurelius"
WIKIQUOTE_SENECA = "https://en.wikiquote.org/wiki/Seneca_the_Younger"
WIKIQUOTE_EPICTETUS = "https://en.wikiquote.org/wiki/Epictetus"
STOIC_STOREHOUSE = "https://stoicstorehouse.com/category/quotes/"
THOUGHTCO = "https://www.thoughtco.com/stoic-quotes-118333"
DABBLING = "https://dabblingwithdata.amedcalf.com/stoic-quotes/"

QUOTES = [
    ("Waste no more time arguing what a good man should be. Be one.", "Marcus Aurelius", DAILY_STOIC),
    ("If it is not right, do not do it; if it is not true, do not say it.", "Marcus Aurelius", DAILY_STOIC),
    ("The best revenge is not to be like your enemy.", "Marcus Aurelius", WIKIQUOTE_MA),
    ("You could leave life right now. Let that determine what you do and say and think.", "Marcus Aurelius", ORION),
    ("Be tolerant with others and strict with yourself.", "Marcus Aurelius", WIKIQUOTE_MA),
    ("External things are not the problem. It’s your assessment of them.", "Marcus Aurelius", STOIC_STOREHOUSE),
    ("We are more often frightened than hurt; and we suffer more in imagination than in reality.", "Seneca", DAILY_STOIC),
    ("If a man knows not which port he sails, no wind is favorable.", "Seneca", WIKIQUOTE_SENECA),
    ("Life is very short and anxious for those who forget the past, neglect the present, and fear the future.", "Seneca", THOUGHTCO),
    ("People are frugal in guarding their personal property; but as soon as it comes to squandering time they are most wasteful.", "Seneca", ORION),
    ("How long are you going to wait before you demand the best for yourself?", "Epictetus", DAILY_STOIC),
    ("Don’t explain your philosophy. Embody it.", "Epictetus", WIKIQUOTE_EPICTETUS),
    ("First say to yourself what you would be; and then do what you have to do.", "Epictetus", ORION),
    ("Curb your desire—don’t set your heart on so many things and you will get what you need.", "Epictetus", STOIC_STOREHOUSE),
    ("The happiness of your life depends upon the quality of your thoughts.", "Marcus Aurelius", DABBLING),
    ("No man is free who is not master of himself.", "Epictetus", WIKIQUOTE_EPICTETUS),
    ("It is not the man who has too little, but the man who craves more, that is poor.", "Seneca", THOUGHTCO),
    ("Difficulties strengthen the mind, as labor does the body.", "Seneca", DABBLING),
    ("Man conquers the world by conquering himself.", "Zeno of Citium", STOIC_STOREHOUSE),
    ("He suffers more than necessary, who suffers before it is necessary.", "Seneca", WIKIQUOTE_SENECA),
    ("Very little is needed to make a happy life; it is all within yourself.", "Marcus Aurelius", WIKIQUOTE_MA),
    ("Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control.", "Epictetus", ORION),
    ("Luck is what happens when preparation meets opportunity.", "Seneca", DABBLING),
    ("To bear trials with a calm mind robs misfortune of its strength and burden.", "Seneca", ORION),
    ("The obstacle is the way.", "Marcus Aurelius", DAILY_STOIC),
]

SOURCES = [
    DAILY_STOIC,
    ORION,
    WIKIQUOTE_MA,
    WIKIQUOTE_SENECA,
    WIKIQUOTE_EPICTETUS,
    STOIC_STOREHOUSE,
    THOUGHTCO,
    DABBLING,
]


def format_quote(item: tuple[str, str, str]) -> str:
    quote, author, source = item
    takeaway = (
        "Practical takeaway: focus on what you can control today, and act with discipline."
    )
    return f"🗿 \"{quote}\"\n— {author}\n{takeaway}\nSource: {source}"


def help_text() -> str:
    return (
        "Stoic commands:\n"
        "- `!stoic` or `!stoic now` (instant random quote)\n"
        "- `!stoic random`\n"
        "- `!stoic sources`\n"
        "- `!stoic help`"
    )


def sources_text() -> str:
    lines = ["📚 Stoic quote sources in rotation:"]
    for s in SOURCES:
        lines.append(f"- {s}")
    return "\n".join(lines)


def handle(raw: str) -> str:
    msg = raw.strip()
    if not msg.lower().startswith("!stoic"):
        raise ValueError("Message must start with !stoic")

    parts = [p.lower() for p in shlex.split(msg)]
    if len(parts) == 1:
        return format_quote(RNG.choice(QUOTES))

    cmd = parts[1]
    if cmd in {"now", "random"}:
        return format_quote(RNG.choice(QUOTES))
    if cmd in {"sources", "source", "refs"}:
        return sources_text()
    if cmd in {"help", "commands"}:
        return help_text()

    return help_text()


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: discord_stoic_command.py '!stoic now'")
        return 2
    raw = " ".join(sys.argv[1:])
    try:
        print(handle(raw))
        return 0
    except Exception as e:
        print(f"Stoic command error: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
