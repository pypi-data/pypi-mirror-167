"""
The Word class contains info on the text, number of syllables,
and list of phonemes in a word. It's used in the `Lyric` class.
"""
import math
from typing import List


class Word(object):
    def __init__(self, text: str, syllables: int, phonemes: List[str]):
        self.text = text
        self.syllables = syllables
        self.phonemes = phonemes
        self.n_phonemes = len(self.phonemes)
        self.max_phonemes_per_syllable = math.floor(self.n_phonemes / self.syllables)
