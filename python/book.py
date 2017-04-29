class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

if __name__ == '__main__':
    hunger_games = Book('Hunger games')
    print 'Book title:', hunger_games.title
    print 'Book status: borrowed=', hunger_games.is_borrowed
    print 'Borrow the book.'
    hunger_games.borrow()
    print 'Book title:', hunger_games.title
    print 'Book status: borrowed=', hunger_games.is_borrowed
