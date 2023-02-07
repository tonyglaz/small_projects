from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)
book_ns = api.namespace('')

books = {
    1: {
        "name": "Solaris",
        "year": 1961,
        "author": "Stanisław Lem"
    },
    2: {
        "name": "Roadside picnic",
        "yaer": 1972,
        "author": "brothers Strugatsky"
    }
}


@book_ns.route('/books')
class BooksView(Resource):
    def get(self):
        return books, 200

    def post(self):
        req_json = request.json
        books[len(books) + 1] = req_json
        return "", 200


@book_ns.route('/books/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        return books[bid], 200

    def delete(self, bid):
        del books[bid]
        return "", 204


if __name__ == "__main__":
    app.run(debug=True)
