from itertools import izip
from functools import partial
import random
import re


_rewhite = re.compile(r"\s+")
_rewhitesub = partial(_rewhite.sub, "")
_abbreviations = "Mr.", "Mrs.", "Dr.", "Ms.", "Prof."


class Book:
    max_iteration = 1000000

    def __init__(self, text=None, path=None):
        self.path = path
        self._text = text
        self._sentences = []
        self.num_sentences = None
    
    @property
    def text(self):
        if not self._text:
            if not self.path:
                raise Exception("No text or path to resource")
            with open(self.path) as f:
                self._text = f.read()
        return self._text

    @property
    def sentences(self):
        if not self._sentences:
            self._sentences = _split_sentences(self.text)
            self.num_sentences = len(self._sentences)
        return self._sentences

    def gen_random_sentences(self, min_words=3, max_words=10000):
        sentences = self.sentences
        max_index = self.num_sentences - 1
        for _ in xrange(self.max_iteration):
            i = random.randint(0, max_index)
            sentence = sentences[i]
            words = _rewhite.split(sentence)
            words = filter(None, map(_rewhitesub, words))
            lenwords = len(words)
            if lenwords < min_words or lenwords > max_words:
                continue
            elif words[-1] in _abbreviations:
                continue
            else:   
                yield " ".join(words)

    def get_random_sentence(self, min_words=3, max_words=10000):
        return self.gen_random_sentences(min_words, max_words).next()


def _split_sentences(text):
    # from pyteaser: https://github.com/xiaoxu193/PyTeaser
    # see `pyteaser.split_sentences()`
    fragments = re.split('(?<![A-Z])([.!?]"?)(?=\s+\"?[A-Z])', text)
    return map("".join, izip(*[iter(fragments[:-1])] * 2))
 


