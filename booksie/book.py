from itertools import izip
from functools import partial
import random
import re


_rewhite = re.compile(r"\s+")
_rewhitesub = partial(_rewhite.sub, "")
_abbreviations = "Mr.", "Mrs.", "Dr.", "Ms.", "Prof."


class Book:

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

    def gen_random_sentences(self, no_more_than=1000000):
        sentences = self.sentences
        max_index = self.num_sentences - 1
        for _ in xrange(no_more_than):
            i = random.randint(0, max_index)
            yield sentences[i]

    def get_random_sentence(self, min_words=3, max_words=1000):
        for sentence in self.gen_random_sentences():
            words = _rewhite.split(sentence)
            words = filter(None, map(_rewhitesub, words))
            if min_words > len(words) > max_words:
                continue
            elif words[-1] in _abbreviations:
                continue
            else:   
                return " ".join(words)
        raise Exception("Couldn't find a sentence between {0} and {1} words long".format(   
                        min_words, max_words))


def _split_sentences(text):
    # from pyteaser: https://github.com/xiaoxu193/PyTeaser
    # see `pyteaser.split_sentences()`
    fragments = re.split('(?<![A-Z])([.!?]"?)(?=\s+\"?[A-Z])', text)
    return map("".join, izip(*[iter(fragments[:-1])] * 2))
 


