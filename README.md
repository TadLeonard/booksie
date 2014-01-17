booksie
=======

Do fun things with books and other long texts.


Examples
--------

Generate random sentences from some text

..code-block python::

    from booksie.book import Book
    shake = Book(open("speare.txt").read())
    long_sentences = shake.gen_random_sentences(min_words=100)
    for sentence in long_sentences:
        print sentence
        if "horatio" in sentence.lower():
            break


Get a single random sentence from some text

..code-block python::

    form booksie.book import Book
    shake = Book(
        
        
