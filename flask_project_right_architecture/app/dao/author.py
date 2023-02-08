from .model.author import Author


class AuthorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        author = self.session.query(Author).get(aid)
        return author

    def get_all(self):
        entity_list = self.session.query(Author).all()
        return entity_list

    def create(self, data):
        author = Author(**data)

        self.session.add(author)
        self.session.commit()

        return author

    def update(self, author):
        self.session.add(author)
        self.session.commit()

        return author

    def delete(self, aid):
        author = self.get_one(aid)
        self.session.delete(author)
        self.session.commit()

