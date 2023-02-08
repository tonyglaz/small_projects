from .services.book import BookService
from .services.author import AuthorService
from .database import db
from .dao.author import AuthorDAO
from .dao.book import BookDAO


author_dao=AuthorDAO(db.session)
author_service=AuthorService(author_dao)


book_dao=BookDAO(db.session)
book_service=BookService(book_dao)