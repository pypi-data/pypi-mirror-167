"""
Utilities for extracing phonemes and syllables from english text.
"""

from functools import lru_cache
from typing import List, Tuple

import nltk
from g2p_en import G2p
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize

# ensure NLTK resources are downloaded
try:
    cmudict.ensure_loaded()
except LookupError:
    nltk.download("cmudict")
try:
    word_tokenize("test")
except Exception:
    nltk.download("punkt")


from ..constants import G2P_PHONEMES_TO_SAY_PHONEMES

G2P = None
CMU = None


@lru_cache(maxsize=1024)
def word_to_g2p_phonemes(text: str) -> List[str]:
    global G2P
    if not G2P:
        G2P = G2p()
    return G2P(text)


def word_to_say_phonemes(text: str) -> List[str]:
    return [G2P_PHONEMES_TO_SAY_PHONEMES.get(p, "") for p in word_to_g2p_phonemes(text)]


@lru_cache(maxsize=1024)
def word_to_syllable_count(word: str) -> int:
    global CMU
    if not CMU:
        CMU = cmudict.dict()
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in CMU[word.lower()]][
            0
        ]
    except KeyError:
        # if word not found in cmudict
        # referred from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
        count = 0
        vowels = "aeiouy"
        word = word.lower()
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if word.endswith("le"):
            count += 1
        if count == 0:
            count += 1
        return count


@lru_cache(maxsize=1024)
def process_text_for_say(text) -> List[Tuple[str, int, List[str]]]:
    """
    Get a list of phonemes + syllable counts for each word in a text
    """
    return [
        (word, word_to_syllable_count(word), word_to_say_phonemes(word))
        if word not in [",", ".", "?", "!", "-", ":", ";"]
        else ("", 1, ["%"])  # silence
        for word in word_tokenize(text)
    ]
