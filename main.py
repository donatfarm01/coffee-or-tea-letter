"""Write the entry letter for the One Letter: Coffee or Tea bounty.

The entry is one letter and nothing else. The letter A names coffee, the
choice this entry defends: the louder, more ritualized, more vivid side
of the coffee against tea argument, and the one the tasting judge's own
criteria reward first. The program writes exactly that letter, with no
trailing newline and no extra text, so the sealed gate reads one byte.
"""

ENTRY_LETTER = "A"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LETTER)


if __name__ == "__main__":
    main()
