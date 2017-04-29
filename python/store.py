from book import Book

if __name__ == '__main__':
    # Create a list of books
    books = []
    for i in xrange(10):
        # Create new book
        title = 'Book #%s' % i
        book = Book(title)
        # Add new item to books
        books.append(book)

    # Show list of available books
    for b in books:
        print 'Book title:', b.title
