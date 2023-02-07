from flask import request, jsonify
from flask_restx import Resource

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


class BooksView(Resource):
    def get(self):
        return jsonify(books), 200

    def post(self):
        req_json = request.json
        books[len(books) + 1] = req_json
        return "", 200


class BookView(Resource):
    def get(self, bid):
        return books[bid], 200

    def delete(self, bid):
        del books[bid]
        return "", 204
