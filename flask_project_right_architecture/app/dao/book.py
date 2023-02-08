from .model.book import Book


class BookDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        book = self.session.query(Book).get(bid)
        return book

    def get_all(self):
        entity_list = self.session.query(Book).all()
        return entity_list

    def create(self, data):
        book = Book(**data)

        self.session.add(book)
        self.session.commit()

        return book

    def update(self, book):
        self.session.add(book)
        self.session.commit()

        return book

    def delete(self, bid):
        book = self.get_one(bid)
        self.session.delete(book)
        self.session.commit()

