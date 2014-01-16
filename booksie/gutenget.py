import os
import random
import re
import urllib2
from booksie.log import logging


logger = logging.getLogger("gutenget")
logger.info("HEY")
logger.critical("HEY")


_rehref = re.compile("href=\"\/ebooks\/([0-9]{5})\"")
_title_split = "EBook of The"
_author_split = ", by"


def get_text(text_id=None, min_id=1, max_id=20000):
    if text_id is None:
        text_id = random.randint(min_id, max_id)
    url = "http://www.gutenberg.org/ebooks/{0}.txt.utf-8".format(text_id)
    logger.info("Gathering text from {0}".format(url))
    gutenbook = urllib2.urlopen(url) 
    text = gutenbook.read()
    logger.info("Gathered text from {0}".format(url))
    return text, get_text_info(text)


def get_text_info(text):
    first_lines = text[:1000].splitlines()
    _, _, full_title = first_lines[0].partition(_title_split)
    full_title = full_title.strip()
    if full_title.endswith(", by"):
        full_title = " ".join([full_title, first_lines[1].strip()])
    title, _, author = full_title.partition(_author_split)
    return title, author


if __name__ == "__main__":
    while True:
        title, text, author = get_text()
        print "=" * len(title)
        print title
        print "=" * len(title)
        print "By {0}".format(author)
        print 
        print "A sentence"
