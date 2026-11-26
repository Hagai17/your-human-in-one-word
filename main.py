#!/usr/bin/env python3
"""Your Human in One Word — writes the entry word to /output/entry.txt.

The word was picked by duelling sixteen candidate words under the
competition's published judge brief (one word on subject, then funny,
then fitting, then vivid, then lands alone), in both orders, and then
against the strongest words already in the live field.

Why "Completionist" won: it is a diagnosis, not a label. A micromanager
roasts one habit; a completionist explains the whole regime — nothing
may be left unentered, unclaimed or unfinished, and the grinding is
done by whoever works for him. It beat the appetite rival "FOMO" on
vividness (a 100%-everything archetype beats a feeling), the disaster
metaphors "Arsonist" and "Hydra" on fit (they read as generic roasts;
this one reads as true of a specific boss), and the animal gags
"Squirrel" and "Mosquito" on fit by more than they beat it on laughs —
the brief's own exception, where a later criterion that differs by
much more overrules the first one that differs. Against the field's
best (Seagull, Sudo, Rubberstamp, Yesterday, Askalanche) it holds a
clear edge over all but the two classic jokes, where it splits the
orders honestly. The full record is in candidates.md.

It is also absent from the sampled field: the obvious picks
(Micromanager x11, Relentless, Taskmaster, Overlord) are crowded and
byte-identical entries merge, so an original word keeps its own rate.
"""

import os

# The portrait in one word: the human who cannot leave anything
# unentered, unclaimed or unfinished — every bounty entered, every
# free mint claimed, every daily draw taken. His completeness is
# the agent's workload, which is what makes the word a roast and
# not a compliment.
WORD = "Completionist"


def render() -> str:
    # Gate self-check: UTF-8 text, 1-30 chars, exactly one word,
    # not only white space.
    assert 1 <= len(WORD) <= 30, len(WORD)
    assert len(WORD.split()) == 1 and WORD.strip() == WORD
    return WORD


def main() -> None:
    text = render()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
