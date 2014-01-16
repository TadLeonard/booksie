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
while True:
    raw_input(book.get_random_sentence())
