import os
from booksie.gutenget import get_text_info
from booksie.book import Book


shake_path = os.path.join(os.path.dirname(__file__),
                          "booksie", "_shakespeare.txt")


text = open(shake_path).read()
title, author = get_text_info(text)
print "=" * len(title)
print title
print "=" * len(title)
print "By {0}".format(author)
print


book = Book(text=text)
sentences = book.gen_random_sentences(2, 30)
for sentence in sentences:
    try:
        raw_input(sentence)
    except KeyboardInterrupt:
        break
