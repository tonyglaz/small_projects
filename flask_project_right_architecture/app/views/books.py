from flask import request
from flask_restx import Resource, Namespace

from ..database import db
from ..models import BookSchema, Book

book_ns = Namespace('books')

book_schema = BookSchema()
books_schema = BookSchema(many=True)


@book_ns.route('/')  # / + books + /
class BooksView(Resource):
    def get(self):
        all_books = db.session.query(Book).all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_book = Book(**req_json)

        with db.session.begin():
            db.session.add(new_book)
        return "", 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid: int):  # Получил данные
        try:
            book = db.session.query(Book).filter(Book.id == bid).one()
            return book_schema.dump(book), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid):  # Заменил данные
        book = db.session.query(Book).get(bid)
        req_json = request.json

        book.book_name = req_json.get("name")
        book.book_year = req_json.get("year")

        db.session.add(book)
        db.session.commit()

        return "", 204

    def patch(self, bid):  # частично обновил данные
        book = db.session.query(Book).get(bid)
        req_json = request.json
        if "name" in req_json:
            book.name = req_json.get("name")
        if "year" in req_json:
            book.name = req_json.get("year")

        db.session.add(book)
        db.session.commit()

        return "", 204

    def delete(self, bid: int):
        user = db.session.query(Book).get(bid)
        db.session.delete(user)
        db.session.commit()

        return "", 204
